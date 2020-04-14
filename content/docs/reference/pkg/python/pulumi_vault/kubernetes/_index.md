---
title: Module kubernetes
title_tag: Module kubernetes | Package pulumi_vault | Python SDK
linktitle: kubernetes
notitle: true
---

<div class="section" id="kubernetes">
<h1>kubernetes<a class="headerlink" href="#kubernetes" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.kubernetes"></span><dl class="class">
<dt id="pulumi_vault.kubernetes.AuthBackendConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.kubernetes.</code><code class="sig-name descname">AuthBackendConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">kubernetes_ca_cert=None</em>, <em class="sig-param">kubernetes_host=None</em>, <em class="sig-param">pem_keys=None</em>, <em class="sig-param">token_reviewer_jwt=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Kubernetes auth backend config in a Vault server. See the <a class="reference external" href="https://www.vaultproject.io/docs/auth/kubernetes.html">Vault
documentation</a> for more
information.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/kubernetes_auth_backend_config.md">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/kubernetes_auth_backend_config.md</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique name of the kubernetes backend to configure.</p></li>
<li><p><strong>issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Optional JWT issuer. If no issuer is specified, <code class="docutils literal notranslate"><span class="pre">kubernetes.io/serviceaccount</span></code> will be used as the default issuer.</p></li>
<li><p><strong>kubernetes_ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.</p></li>
<li><p><strong>kubernetes_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.</p></li>
<li><p><strong>pem_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these keys.</p></li>
<li><p><strong>token_reviewer_jwt</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used for login will be used to access the API.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendConfig.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendConfig.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique name of the kubernetes backend to configure.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendConfig.issuer">
<code class="sig-name descname">issuer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendConfig.issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional JWT issuer. If no issuer is specified, <code class="docutils literal notranslate"><span class="pre">kubernetes.io/serviceaccount</span></code> will be used as the default issuer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendConfig.kubernetes_ca_cert">
<code class="sig-name descname">kubernetes_ca_cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendConfig.kubernetes_ca_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendConfig.kubernetes_host">
<code class="sig-name descname">kubernetes_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendConfig.kubernetes_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendConfig.pem_keys">
<code class="sig-name descname">pem_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendConfig.pem_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>List of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these keys.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendConfig.token_reviewer_jwt">
<code class="sig-name descname">token_reviewer_jwt</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendConfig.token_reviewer_jwt" title="Permalink to this definition">¶</a></dt>
<dd><p>A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used for login will be used to access the API.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.kubernetes.AuthBackendConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">kubernetes_ca_cert=None</em>, <em class="sig-param">kubernetes_host=None</em>, <em class="sig-param">pem_keys=None</em>, <em class="sig-param">token_reviewer_jwt=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique name of the kubernetes backend to configure.</p></li>
<li><p><strong>issuer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Optional JWT issuer. If no issuer is specified, <code class="docutils literal notranslate"><span class="pre">kubernetes.io/serviceaccount</span></code> will be used as the default issuer.</p></li>
<li><p><strong>kubernetes_ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.</p></li>
<li><p><strong>kubernetes_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.</p></li>
<li><p><strong>pem_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these keys.</p></li>
<li><p><strong>token_reviewer_jwt</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used for login will be used to access the API.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.kubernetes.AuthBackendConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.kubernetes.AuthBackendConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.kubernetes.AuthBackendRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.kubernetes.</code><code class="sig-name descname">AuthBackendRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">audience=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">bound_cidrs=None</em>, <em class="sig-param">bound_service_account_names=None</em>, <em class="sig-param">bound_service_account_namespaces=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">num_uses=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Kubernetes auth backend role in a Vault server. See the <a class="reference external" href="https://www.vaultproject.io/docs/auth/kubernetes.html">Vault
documentation</a> for more
information.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/kubernetes_auth_backend_role.html.md">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/kubernetes_auth_backend_role.html.md</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>audience</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Audience claim to verify in the JWT.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique name of the kubernetes backend to configure.</p></li>
<li><p><strong>bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, a list of
CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.</p></li>
<li><p><strong>bound_service_account_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of service account names able to access this role. If set to <code class="docutils literal notranslate"><span class="pre">[&quot;*&quot;]</span></code> all names are allowed, both this and bound_service_account_namespaces can not be “<a href="#id2"><span class="problematic" id="id3">*</span></a>”.</p></li>
<li><p><strong>bound_service_account_namespaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of namespaces allowed to access this role. If set to <a href="#id4"><span class="problematic" id="id5">`</span></a>[“<em>”]``all namespaces are allowed, both this and bound_service_account_names can not be set to “</em>”.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum allowed lifetime of tokens
issued using this role, provided as a number of seconds.</p></li>
<li><p><strong>num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, puts a use-count
limitation on the issued token.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings
specifying the policies to be set on tokens issued using this role.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the role.</p></li>
<li><p><strong>token_bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p></li>
<li><p><strong>token_explicit_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, will encode an
[explicit max TTL](<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls</a>)
onto the token in number of seconds. This is a hard cap even if``token_ttl<code class="docutils literal notranslate"><span class="pre">and</span></code>token_max_ttl<a href="#id6"><span class="problematic" id="id7">``</span></a>would otherwise allow a renewal.</p></li>
<li><p><strong>token_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_no_default_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p></li>
<li><p><strong>token_num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The
[period](<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls</a>),
if any, in number of seconds to set on the token.</p></li>
<li><p><strong>token_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>token_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p></li>
<li><p><strong>token_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of token that should be generated. Can be``service<code class="docutils literal notranslate"><span class="pre">,</span></code>batch<code class="docutils literal notranslate"><span class="pre">,</span> <span class="pre">or</span></code>default<code class="docutils literal notranslate"><span class="pre">to</span> <span class="pre">use</span> <span class="pre">the</span> <span class="pre">mount's</span> <span class="pre">tuned</span> <span class="pre">default</span> <span class="pre">(which</span> <span class="pre">unless</span> <span class="pre">changed</span> <span class="pre">will</span> <span class="pre">be</span></code>service<code class="docutils literal notranslate"><span class="pre">tokens).</span> <span class="pre">For</span> <span class="pre">token</span> <span class="pre">store</span> <span class="pre">roles,</span> <span class="pre">there</span> <span class="pre">are</span> <span class="pre">two</span> <span class="pre">additional</span> <span class="pre">possibilities:</span></code>default-service<code class="docutils literal notranslate"><span class="pre">and</span></code>default-batch` which specify the type to return unless the client
requests a different type at generation time.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The TTL period of tokens issued
using this role, provided as a number of seconds.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.audience">
<code class="sig-name descname">audience</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.audience" title="Permalink to this definition">¶</a></dt>
<dd><p>Audience claim to verify in the JWT.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique name of the kubernetes backend to configure.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.bound_cidrs">
<code class="sig-name descname">bound_cidrs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, a list of
CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.bound_service_account_names">
<code class="sig-name descname">bound_service_account_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.bound_service_account_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of service account names able to access this role. If set to <code class="docutils literal notranslate"><span class="pre">[&quot;*&quot;]</span></code> all names are allowed, both this and bound_service_account_namespaces can not be “*”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.bound_service_account_namespaces">
<code class="sig-name descname">bound_service_account_namespaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.bound_service_account_namespaces" title="Permalink to this definition">¶</a></dt>
<dd><p>List of namespaces allowed to access this role. If set to <code class="docutils literal notranslate"><span class="pre">[&quot;*&quot;]</span></code> all namespaces are allowed, both this and bound_service_account_names can not be set to “*”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.max_ttl">
<code class="sig-name descname">max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum allowed lifetime of tokens
issued using this role, provided as a number of seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.num_uses">
<code class="sig-name descname">num_uses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.num_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, puts a use-count
limitation on the issued token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.period" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of strings
specifying the policies to be set on tokens issued using this role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.role_name">
<code class="sig-name descname">role_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.token_bound_cidrs">
<code class="sig-name descname">token_bound_cidrs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.token_bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.token_explicit_max_ttl">
<code class="sig-name descname">token_explicit_max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.token_explicit_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.token_max_ttl">
<code class="sig-name descname">token_max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.token_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.token_no_default_policy">
<code class="sig-name descname">token_no_default_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.token_no_default_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.token_num_uses">
<code class="sig-name descname">token_num_uses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.token_num_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.token_period">
<code class="sig-name descname">token_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.token_period" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.token_policies">
<code class="sig-name descname">token_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.token_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.token_ttl">
<code class="sig-name descname">token_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.token_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.token_type">
<code class="sig-name descname">token_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.token_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of token that should be generated. Can be <code class="docutils literal notranslate"><span class="pre">service</span></code>,
<code class="docutils literal notranslate"><span class="pre">batch</span></code>, or <code class="docutils literal notranslate"><span class="pre">default</span></code> to use the mount’s tuned default (which unless changed will be
<code class="docutils literal notranslate"><span class="pre">service</span></code> tokens). For token store roles, there are two additional possibilities:
<code class="docutils literal notranslate"><span class="pre">default-service</span></code> and <code class="docutils literal notranslate"><span class="pre">default-batch</span></code> which specify the type to return unless the client
requests a different type at generation time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.ttl">
<code class="sig-name descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL period of tokens issued
using this role, provided as a number of seconds.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">audience=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">bound_cidrs=None</em>, <em class="sig-param">bound_service_account_names=None</em>, <em class="sig-param">bound_service_account_namespaces=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">num_uses=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em>, <em class="sig-param">ttl=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>audience</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Audience claim to verify in the JWT.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique name of the kubernetes backend to configure.</p></li>
<li><p><strong>bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, a list of
CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.</p></li>
<li><p><strong>bound_service_account_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of service account names able to access this role. If set to <code class="docutils literal notranslate"><span class="pre">[&quot;*&quot;]</span></code> all names are allowed, both this and bound_service_account_namespaces can not be “<a href="#id8"><span class="problematic" id="id9">*</span></a>”.</p></li>
<li><p><strong>bound_service_account_namespaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of namespaces allowed to access this role. If set to <a href="#id10"><span class="problematic" id="id11">`</span></a>[“<em>”]``all namespaces are allowed, both this and bound_service_account_names can not be set to “</em>”.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum allowed lifetime of tokens
issued using this role, provided as a number of seconds.</p></li>
<li><p><strong>num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, puts a use-count
limitation on the issued token.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings
specifying the policies to be set on tokens issued using this role.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the role.</p></li>
<li><p><strong>token_bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p></li>
<li><p><strong>token_explicit_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, will encode an
[explicit max TTL](<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls</a>)
onto the token in number of seconds. This is a hard cap even if``token_ttl<code class="docutils literal notranslate"><span class="pre">and</span></code>token_max_ttl<a href="#id12"><span class="problematic" id="id13">``</span></a>would otherwise allow a renewal.</p></li>
<li><p><strong>token_max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_no_default_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p></li>
<li><p><strong>token_num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The
[period](<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls</a>),
if any, in number of seconds to set on the token.</p></li>
<li><p><strong>token_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>token_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p></li>
<li><p><strong>token_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of token that should be generated. Can be``service<code class="docutils literal notranslate"><span class="pre">,</span></code>batch<code class="docutils literal notranslate"><span class="pre">,</span> <span class="pre">or</span></code>default<code class="docutils literal notranslate"><span class="pre">to</span> <span class="pre">use</span> <span class="pre">the</span> <span class="pre">mount's</span> <span class="pre">tuned</span> <span class="pre">default</span> <span class="pre">(which</span> <span class="pre">unless</span> <span class="pre">changed</span> <span class="pre">will</span> <span class="pre">be</span></code>service<code class="docutils literal notranslate"><span class="pre">tokens).</span> <span class="pre">For</span> <span class="pre">token</span> <span class="pre">store</span> <span class="pre">roles,</span> <span class="pre">there</span> <span class="pre">are</span> <span class="pre">two</span> <span class="pre">additional</span> <span class="pre">possibilities:</span></code>default-service<code class="docutils literal notranslate"><span class="pre">and</span></code>default-batch` which specify the type to return unless the client
requests a different type at generation time.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The TTL period of tokens issued
using this role, provided as a number of seconds.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.kubernetes.AuthBackendRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.kubernetes.AuthBackendRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.kubernetes.AuthBackendRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.kubernetes.AwaitableGetAuthBackendConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.kubernetes.</code><code class="sig-name descname">AwaitableGetAuthBackendConfigResult</code><span class="sig-paren">(</span><em class="sig-param">backend=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">kubernetes_ca_cert=None</em>, <em class="sig-param">kubernetes_host=None</em>, <em class="sig-param">pem_keys=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.kubernetes.AwaitableGetAuthBackendConfigResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_vault.kubernetes.AwaitableGetAuthBackendRoleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.kubernetes.</code><code class="sig-name descname">AwaitableGetAuthBackendRoleResult</code><span class="sig-paren">(</span><em class="sig-param">audience=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">bound_cidrs=None</em>, <em class="sig-param">bound_service_account_names=None</em>, <em class="sig-param">bound_service_account_namespaces=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">num_uses=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em>, <em class="sig-param">ttl=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.kubernetes.AwaitableGetAuthBackendRoleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_vault.kubernetes.GetAuthBackendConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.kubernetes.</code><code class="sig-name descname">GetAuthBackendConfigResult</code><span class="sig-paren">(</span><em class="sig-param">backend=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">kubernetes_ca_cert=None</em>, <em class="sig-param">kubernetes_host=None</em>, <em class="sig-param">pem_keys=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendConfigResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAuthBackendConfig.</p>
<dl class="attribute">
<dt id="pulumi_vault.kubernetes.GetAuthBackendConfigResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendConfigResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.GetAuthBackendConfigResult.issuer">
<code class="sig-name descname">issuer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendConfigResult.issuer" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional JWT issuer. If no issuer is specified, <code class="docutils literal notranslate"><span class="pre">kubernetes.io/serviceaccount</span></code> will be used as the default issuer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.GetAuthBackendConfigResult.kubernetes_ca_cert">
<code class="sig-name descname">kubernetes_ca_cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendConfigResult.kubernetes_ca_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.GetAuthBackendConfigResult.kubernetes_host">
<code class="sig-name descname">kubernetes_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendConfigResult.kubernetes_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.GetAuthBackendConfigResult.pem_keys">
<code class="sig-name descname">pem_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendConfigResult.pem_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional list of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these keys.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_vault.kubernetes.GetAuthBackendRoleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.kubernetes.</code><code class="sig-name descname">GetAuthBackendRoleResult</code><span class="sig-paren">(</span><em class="sig-param">audience=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">bound_cidrs=None</em>, <em class="sig-param">bound_service_account_names=None</em>, <em class="sig-param">bound_service_account_namespaces=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">num_uses=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em>, <em class="sig-param">ttl=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendRoleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAuthBackendRole.</p>
<dl class="attribute">
<dt id="pulumi_vault.kubernetes.GetAuthBackendRoleResult.audience">
<code class="sig-name descname">audience</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendRoleResult.audience" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) Audience claim to verify in the JWT.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.GetAuthBackendRoleResult.bound_service_account_names">
<code class="sig-name descname">bound_service_account_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendRoleResult.bound_service_account_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of service account names able to access this role. If set to “<em>” all names are allowed, both this and bound_service_account_namespaces can not be “</em>”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.GetAuthBackendRoleResult.bound_service_account_namespaces">
<code class="sig-name descname">bound_service_account_namespaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendRoleResult.bound_service_account_namespaces" title="Permalink to this definition">¶</a></dt>
<dd><p>List of namespaces allowed to access this role. If set to “<em>” all namespaces are allowed, both this and bound_service_account_names can not be set to “</em>”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.GetAuthBackendRoleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendRoleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.GetAuthBackendRoleResult.token_bound_cidrs">
<code class="sig-name descname">token_bound_cidrs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendRoleResult.token_bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.GetAuthBackendRoleResult.token_explicit_max_ttl">
<code class="sig-name descname">token_explicit_max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendRoleResult.token_explicit_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.GetAuthBackendRoleResult.token_max_ttl">
<code class="sig-name descname">token_max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendRoleResult.token_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.GetAuthBackendRoleResult.token_no_default_policy">
<code class="sig-name descname">token_no_default_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendRoleResult.token_no_default_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.GetAuthBackendRoleResult.token_num_uses">
<code class="sig-name descname">token_num_uses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendRoleResult.token_num_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.GetAuthBackendRoleResult.token_period">
<code class="sig-name descname">token_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendRoleResult.token_period" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.GetAuthBackendRoleResult.token_policies">
<code class="sig-name descname">token_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendRoleResult.token_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.GetAuthBackendRoleResult.token_ttl">
<code class="sig-name descname">token_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendRoleResult.token_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.kubernetes.GetAuthBackendRoleResult.token_type">
<code class="sig-name descname">token_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.kubernetes.GetAuthBackendRoleResult.token_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of token that should be generated. Can be <code class="docutils literal notranslate"><span class="pre">service</span></code>,
<code class="docutils literal notranslate"><span class="pre">batch</span></code>, or <code class="docutils literal notranslate"><span class="pre">default</span></code> to use the mount’s tuned default (which unless changed will be
<code class="docutils literal notranslate"><span class="pre">service</span></code> tokens). For token store roles, there are two additional possibilities:
<code class="docutils literal notranslate"><span class="pre">default-service</span></code> and <code class="docutils literal notranslate"><span class="pre">default-batch</span></code> which specify the type to return unless the client
requests a different type at generation time.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_vault.kubernetes.get_auth_backend_config">
<code class="sig-prename descclassname">pulumi_vault.kubernetes.</code><code class="sig-name descname">get_auth_backend_config</code><span class="sig-paren">(</span><em class="sig-param">backend=None</em>, <em class="sig-param">issuer=None</em>, <em class="sig-param">kubernetes_ca_cert=None</em>, <em class="sig-param">kubernetes_host=None</em>, <em class="sig-param">pem_keys=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.kubernetes.get_auth_backend_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Reads the Role of an Kubernetes from a Vault server. See the <a class="reference external" href="https://www.vaultproject.io/api/auth/kubernetes/index.html#read-config">Vault
documentation</a> for more
information.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/d/kubernetes_auth_backend_config.md">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/d/kubernetes_auth_backend_config.md</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>backend</strong> (<em>str</em>) – The unique name for the Kubernetes backend the config to
retrieve Role attributes for resides in. Defaults to “kubernetes”.</p></li>
<li><p><strong>issuer</strong> (<em>str</em>) – Optional JWT issuer. If no issuer is specified, <code class="docutils literal notranslate"><span class="pre">kubernetes.io/serviceaccount</span></code> will be used as the default issuer.</p></li>
<li><p><strong>kubernetes_ca_cert</strong> (<em>str</em>) – PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.</p></li>
<li><p><strong>kubernetes_host</strong> (<em>str</em>) – Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.</p></li>
<li><p><strong>pem_keys</strong> (<em>list</em>) – Optional list of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these keys.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_vault.kubernetes.get_auth_backend_role">
<code class="sig-prename descclassname">pulumi_vault.kubernetes.</code><code class="sig-name descname">get_auth_backend_role</code><span class="sig-paren">(</span><em class="sig-param">audience=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">bound_cidrs=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">num_uses=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.kubernetes.get_auth_backend_role" title="Permalink to this definition">¶</a></dt>
<dd><p>Reads the Role of an Kubernetes from a Vault server. See the <a class="reference external" href="https://www.vaultproject.io/api/auth/kubernetes/index.html#read-role">Vault
documentation</a> for more
information.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/d/kubernetes_auth_backend_role.md">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/d/kubernetes_auth_backend_role.md</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>audience</strong> (<em>str</em>) – (Optional) Audience claim to verify in the JWT.</p></li>
<li><p><strong>backend</strong> (<em>str</em>) – The unique name for the Kubernetes backend the role to
retrieve Role attributes for resides in. Defaults to “kubernetes”.</p></li>
<li><p><strong>role_name</strong> (<em>str</em>) – The name of the role to retrieve the Role attributes for.</p></li>
<li><p><strong>token_bound_cidrs</strong> (<em>list</em>) – List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p></li>
<li><p><strong>token_explicit_max_ttl</strong> (<em>float</em>) – <p>If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p>
</p></li>
<li><p><strong>token_max_ttl</strong> (<em>float</em>) – The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_no_default_policy</strong> (<em>bool</em>) – If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p></li>
<li><p><strong>token_num_uses</strong> (<em>float</em>) – <p>The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p>
</p></li>
<li><p><strong>token_period</strong> (<em>float</em>) – (Optional) If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>token_policies</strong> (<em>list</em>) – List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p></li>
<li><p><strong>token_ttl</strong> (<em>float</em>) – The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p></li>
<li><p><strong>token_type</strong> (<em>str</em>) – The type of token that should be generated. Can be <code class="docutils literal notranslate"><span class="pre">service</span></code>,
<code class="docutils literal notranslate"><span class="pre">batch</span></code>, or <code class="docutils literal notranslate"><span class="pre">default</span></code> to use the mount’s tuned default (which unless changed will be
<code class="docutils literal notranslate"><span class="pre">service</span></code> tokens). For token store roles, there are two additional possibilities:
<code class="docutils literal notranslate"><span class="pre">default-service</span></code> and <code class="docutils literal notranslate"><span class="pre">default-batch</span></code> which specify the type to return unless the client
requests a different type at generation time.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
