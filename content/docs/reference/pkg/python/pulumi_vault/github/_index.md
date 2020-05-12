---
title: Module github
title_tag: Module github | Package pulumi_vault | Python SDK
linktitle: github
notitle: true
---

<div class="section" id="github">
<h1>github<a class="headerlink" href="#github" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.github"></span><dl class="py class">
<dt id="pulumi_vault.github.AuthBackend">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.github.</code><code class="sig-name descname">AuthBackend</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">base_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_bound_cidrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_explicit_max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_no_default_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_num_uses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tune</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.github.AuthBackend" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Github Auth mount in a Vault server. See the <a class="reference external" href="https://www.vaultproject.io/docs/auth/github.html">Vault
documentation</a> for more
information.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">github</span><span class="o">.</span><span class="n">AuthBackend</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">organization</span><span class="o">=</span><span class="s2">&quot;myorg&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>base_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API endpoint to use. Useful if you
are running GitHub Enterprise or an API-compatible authentication server.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the description of the mount.
This overrides the current stored value, if any.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Optional; Deprecated, use <code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> instead if you are running Vault &gt;= 1.2) The maximum allowed lifetime of tokens
issued using this role. This must be a valid <a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">duration string</a>.</p></li>
<li><p><strong>organization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization configured users must be part of.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path where the auth backend is mounted. Defaults to <code class="docutils literal notranslate"><span class="pre">auth/github</span></code>
if not specified.</p></li>
<li><p><strong>token_bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – (Optional) List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p></li>
<li><p><strong>token_explicit_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – (Optional) If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p></li>
<li><p><strong>token_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – (Optional) The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_no_default_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – (Optional) If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p></li>
<li><p><strong>token_num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – (Optional) The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p></li>
<li><p><strong>token_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – (Optional) If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>token_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – (Optional) List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p></li>
<li><p><strong>token_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – (Optional) The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of tokens that should be returned by
the mount. Valid values are “default-service”, “default-batch”, “service”, “batch”.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>(Optional; Deprecated, use <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> instead if you are running Vault &gt;= 1.2) The TTL period of tokens issued
using this role. This must be a valid <a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">duration string</a>.</p>
</p></li>
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
<dt id="pulumi_vault.github.AuthBackend.accessor">
<code class="sig-name descname">accessor</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.AuthBackend.accessor" title="Permalink to this definition">¶</a></dt>
<dd><p>The mount accessor related to the auth mount. It is useful for integration with <a class="reference external" href="https://www.vaultproject.io/docs/secrets/identity/index.html">Identity Secrets Engine</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.AuthBackend.base_url">
<code class="sig-name descname">base_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.AuthBackend.base_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The API endpoint to use. Useful if you
are running GitHub Enterprise or an API-compatible authentication server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.AuthBackend.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.AuthBackend.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the description of the mount.
This overrides the current stored value, if any.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.AuthBackend.max_ttl">
<code class="sig-name descname">max_ttl</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.AuthBackend.max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional; Deprecated, use <code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> instead if you are running Vault &gt;= 1.2) The maximum allowed lifetime of tokens
issued using this role. This must be a valid <a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">duration string</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.AuthBackend.organization">
<code class="sig-name descname">organization</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.AuthBackend.organization" title="Permalink to this definition">¶</a></dt>
<dd><p>The organization configured users must be part of.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.AuthBackend.path">
<code class="sig-name descname">path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.AuthBackend.path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path where the auth backend is mounted. Defaults to <code class="docutils literal notranslate"><span class="pre">auth/github</span></code>
if not specified.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.AuthBackend.token_bound_cidrs">
<code class="sig-name descname">token_bound_cidrs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.AuthBackend.token_bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.AuthBackend.token_explicit_max_ttl">
<code class="sig-name descname">token_explicit_max_ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.AuthBackend.token_explicit_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.AuthBackend.token_max_ttl">
<code class="sig-name descname">token_max_ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.AuthBackend.token_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.AuthBackend.token_no_default_policy">
<code class="sig-name descname">token_no_default_policy</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.AuthBackend.token_no_default_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.AuthBackend.token_num_uses">
<code class="sig-name descname">token_num_uses</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.AuthBackend.token_num_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.AuthBackend.token_period">
<code class="sig-name descname">token_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.AuthBackend.token_period" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.AuthBackend.token_policies">
<code class="sig-name descname">token_policies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.AuthBackend.token_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.AuthBackend.token_ttl">
<code class="sig-name descname">token_ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.AuthBackend.token_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.AuthBackend.token_type">
<code class="sig-name descname">token_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.AuthBackend.token_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of tokens that should be returned by
the mount. Valid values are “default-service”, “default-batch”, “service”, “batch”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.AuthBackend.ttl">
<code class="sig-name descname">ttl</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.AuthBackend.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional; Deprecated, use <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> instead if you are running Vault &gt;= 1.2) The TTL period of tokens issued
using this role. This must be a valid <a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">duration string</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.github.AuthBackend.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">base_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_bound_cidrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_explicit_max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_no_default_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_num_uses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tune</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.github.AuthBackend.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackend resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The mount accessor related to the auth mount. It is useful for integration with <a class="reference external" href="https://www.vaultproject.io/docs/secrets/identity/index.html">Identity Secrets Engine</a>.</p>
</p></li>
<li><p><strong>base_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API endpoint to use. Useful if you
are running GitHub Enterprise or an API-compatible authentication server.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the description of the mount.
This overrides the current stored value, if any.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>(Optional; Deprecated, use <code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> instead if you are running Vault &gt;= 1.2) The maximum allowed lifetime of tokens
issued using this role. This must be a valid <a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">duration string</a>.</p>
</p></li>
<li><p><strong>organization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The organization configured users must be part of.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path where the auth backend is mounted. Defaults to <code class="docutils literal notranslate"><span class="pre">auth/github</span></code>
if not specified.</p></li>
<li><p><strong>token_bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – (Optional) List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p></li>
<li><p><strong>token_explicit_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>(Optional) If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p>
</p></li>
<li><p><strong>token_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – (Optional) The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_no_default_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – (Optional) If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p></li>
<li><p><strong>token_num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>(Optional) The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p>
</p></li>
<li><p><strong>token_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – (Optional) If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>token_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – (Optional) List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p></li>
<li><p><strong>token_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – (Optional) The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of tokens that should be returned by
the mount. Valid values are “default-service”, “default-batch”, “service”, “batch”.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>(Optional; Deprecated, use <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> instead if you are running Vault &gt;= 1.2) The TTL period of tokens issued
using this role. This must be a valid <a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">duration string</a>.</p>
</p></li>
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
<dt id="pulumi_vault.github.AuthBackend.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.github.AuthBackend.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.github.AuthBackend.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.github.AuthBackend.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.github.Team">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.github.</code><code class="sig-name descname">Team</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_bound_cidrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_explicit_max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_no_default_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_num_uses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.github.Team" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Team resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] backend: Path where the github auth backend is mounted. Defaults to <code class="docutils literal notranslate"><span class="pre">github</span></code></p>
<blockquote>
<div><p>if not specified.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings specifying the policies to be set on tokens
issued using this role.</p></li>
<li><p><strong>team</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – GitHub team name in “slugified” format.</p></li>
<li><p><strong>token_bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the blocks of IP addresses which are allowed to use the generated token</p></li>
<li><p><strong>token_explicit_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Generated Token’s Explicit Maximum TTL in seconds</p></li>
<li><p><strong>token_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum lifetime of the generated token</p></li>
<li><p><strong>token_no_default_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the ‘default’ policy will not automatically be added to generated tokens</p></li>
<li><p><strong>token_num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of times a token may be used, a value of zero means unlimited</p></li>
<li><p><strong>token_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Generated Token’s Period</p></li>
<li><p><strong>token_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Generated Token’s Policies</p></li>
<li><p><strong>token_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The initial ttl of the token to generate in seconds</p></li>
<li><p><strong>token_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of token to generate, service or batch</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_vault.github.Team.backend">
<code class="sig-name descname">backend</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.Team.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>Path where the github auth backend is mounted. Defaults to <code class="docutils literal notranslate"><span class="pre">github</span></code>
if not specified.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.Team.policies">
<code class="sig-name descname">policies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.Team.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of strings specifying the policies to be set on tokens
issued using this role.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.Team.team">
<code class="sig-name descname">team</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.Team.team" title="Permalink to this definition">¶</a></dt>
<dd><p>GitHub team name in “slugified” format.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.Team.token_bound_cidrs">
<code class="sig-name descname">token_bound_cidrs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.Team.token_bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the blocks of IP addresses which are allowed to use the generated token</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.Team.token_explicit_max_ttl">
<code class="sig-name descname">token_explicit_max_ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.Team.token_explicit_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Generated Token’s Explicit Maximum TTL in seconds</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.Team.token_max_ttl">
<code class="sig-name descname">token_max_ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.Team.token_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum lifetime of the generated token</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.Team.token_no_default_policy">
<code class="sig-name descname">token_no_default_policy</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.Team.token_no_default_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the ‘default’ policy will not automatically be added to generated tokens</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.Team.token_num_uses">
<code class="sig-name descname">token_num_uses</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.Team.token_num_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of times a token may be used, a value of zero means unlimited</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.Team.token_period">
<code class="sig-name descname">token_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.Team.token_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Generated Token’s Period</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.Team.token_policies">
<code class="sig-name descname">token_policies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.Team.token_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Generated Token’s Policies</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.Team.token_ttl">
<code class="sig-name descname">token_ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.Team.token_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The initial ttl of the token to generate in seconds</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.Team.token_type">
<code class="sig-name descname">token_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.Team.token_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of token to generate, service or batch</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.github.Team.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_bound_cidrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_explicit_max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_no_default_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_num_uses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.github.Team.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Team resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path where the github auth backend is mounted. Defaults to <code class="docutils literal notranslate"><span class="pre">github</span></code>
if not specified.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings specifying the policies to be set on tokens
issued using this role.</p></li>
<li><p><strong>team</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – GitHub team name in “slugified” format.</p></li>
<li><p><strong>token_bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the blocks of IP addresses which are allowed to use the generated token</p></li>
<li><p><strong>token_explicit_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Generated Token’s Explicit Maximum TTL in seconds</p></li>
<li><p><strong>token_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum lifetime of the generated token</p></li>
<li><p><strong>token_no_default_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the ‘default’ policy will not automatically be added to generated tokens</p></li>
<li><p><strong>token_num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of times a token may be used, a value of zero means unlimited</p></li>
<li><p><strong>token_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Generated Token’s Period</p></li>
<li><p><strong>token_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Generated Token’s Policies</p></li>
<li><p><strong>token_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The initial ttl of the token to generate in seconds</p></li>
<li><p><strong>token_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of token to generate, service or batch</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.github.Team.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.github.Team.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.github.Team.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.github.Team.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.github.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.github.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_bound_cidrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_explicit_max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_no_default_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_num_uses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.github.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages policy mappings for Github Users authenticated via Github. See the <a class="reference external" href="https://www.vaultproject.io/docs/auth/github.html">Vault
documentation</a> for more
information.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_vault</span> <span class="k">as</span> <span class="nn">vault</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">github</span><span class="o">.</span><span class="n">AuthBackend</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">organization</span><span class="o">=</span><span class="s2">&quot;myorg&quot;</span><span class="p">)</span>
<span class="n">tf_user</span> <span class="o">=</span> <span class="n">vault</span><span class="o">.</span><span class="n">github</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;tfUser&quot;</span><span class="p">,</span>
    <span class="n">backend</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">user</span><span class="o">=</span><span class="s2">&quot;john.doe&quot;</span><span class="p">,</span>
    <span class="n">token_policies</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;developer&quot;</span><span class="p">,</span>
        <span class="s2">&quot;read-only&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path where the github auth backend is mounted. Defaults to <code class="docutils literal notranslate"><span class="pre">github</span></code>
if not specified.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings specifying the policies to be set on tokens issued
using this role.</p></li>
<li><p><strong>token_bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the blocks of IP addresses which are allowed to use the generated token</p></li>
<li><p><strong>token_explicit_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Generated Token’s Explicit Maximum TTL in seconds</p></li>
<li><p><strong>token_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum lifetime of the generated token</p></li>
<li><p><strong>token_no_default_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the ‘default’ policy will not automatically be added to generated tokens</p></li>
<li><p><strong>token_num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of times a token may be used, a value of zero means unlimited</p></li>
<li><p><strong>token_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Generated Token’s Period</p></li>
<li><p><strong>token_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Generated Token’s Policies</p></li>
<li><p><strong>token_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The initial ttl of the token to generate in seconds</p></li>
<li><p><strong>token_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of token to generate, service or batch</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – GitHub user name.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_vault.github.User.backend">
<code class="sig-name descname">backend</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.User.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>Path where the github auth backend is mounted. Defaults to <code class="docutils literal notranslate"><span class="pre">github</span></code>
if not specified.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.User.policies">
<code class="sig-name descname">policies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.User.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of strings specifying the policies to be set on tokens issued
using this role.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.User.token_bound_cidrs">
<code class="sig-name descname">token_bound_cidrs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.User.token_bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the blocks of IP addresses which are allowed to use the generated token</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.User.token_explicit_max_ttl">
<code class="sig-name descname">token_explicit_max_ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.User.token_explicit_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Generated Token’s Explicit Maximum TTL in seconds</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.User.token_max_ttl">
<code class="sig-name descname">token_max_ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.User.token_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum lifetime of the generated token</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.User.token_no_default_policy">
<code class="sig-name descname">token_no_default_policy</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.User.token_no_default_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the ‘default’ policy will not automatically be added to generated tokens</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.User.token_num_uses">
<code class="sig-name descname">token_num_uses</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.User.token_num_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of times a token may be used, a value of zero means unlimited</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.User.token_period">
<code class="sig-name descname">token_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.User.token_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Generated Token’s Period</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.User.token_policies">
<code class="sig-name descname">token_policies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.User.token_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Generated Token’s Policies</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.User.token_ttl">
<code class="sig-name descname">token_ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.User.token_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The initial ttl of the token to generate in seconds</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.User.token_type">
<code class="sig-name descname">token_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.User.token_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of token to generate, service or batch</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_vault.github.User.user">
<code class="sig-name descname">user</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.github.User.user" title="Permalink to this definition">¶</a></dt>
<dd><p>GitHub user name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.github.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_bound_cidrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_explicit_max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_max_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_no_default_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_num_uses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.github.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path where the github auth backend is mounted. Defaults to <code class="docutils literal notranslate"><span class="pre">github</span></code>
if not specified.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings specifying the policies to be set on tokens issued
using this role.</p></li>
<li><p><strong>token_bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the blocks of IP addresses which are allowed to use the generated token</p></li>
<li><p><strong>token_explicit_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Generated Token’s Explicit Maximum TTL in seconds</p></li>
<li><p><strong>token_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum lifetime of the generated token</p></li>
<li><p><strong>token_no_default_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the ‘default’ policy will not automatically be added to generated tokens</p></li>
<li><p><strong>token_num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of times a token may be used, a value of zero means unlimited</p></li>
<li><p><strong>token_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Generated Token’s Period</p></li>
<li><p><strong>token_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Generated Token’s Policies</p></li>
<li><p><strong>token_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The initial ttl of the token to generate in seconds</p></li>
<li><p><strong>token_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of token to generate, service or batch</p></li>
<li><p><strong>user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – GitHub user name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_vault.github.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.github.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.github.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.github.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
