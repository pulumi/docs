---
title: Module l_dap
title_tag: Module l_dap | Package pulumi_vault | Python SDK
linktitle: l_dap
notitle: true
---

<div class="section" id="l-dap">
<h1>l_dap<a class="headerlink" href="#l-dap" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.l_dap"></span><dl class="class">
<dt id="pulumi_vault.l_dap.AuthBackend">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.l_dap.</code><code class="sig-name descname">AuthBackend</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">binddn=None</em>, <em class="sig-param">bindpass=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">deny_null_bind=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">discoverdn=None</em>, <em class="sig-param">groupattr=None</em>, <em class="sig-param">groupdn=None</em>, <em class="sig-param">groupfilter=None</em>, <em class="sig-param">insecure_tls=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">starttls=None</em>, <em class="sig-param">tls_max_version=None</em>, <em class="sig-param">tls_min_version=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em>, <em class="sig-param">upndomain=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">use_token_groups=None</em>, <em class="sig-param">userattr=None</em>, <em class="sig-param">userdn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource for managing an <a class="reference external" href="https://www.vaultproject.io/docs/auth/ldap.html">LDAP auth backend within Vault</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>binddn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DN of object to bind when performing user search</p></li>
<li><p><strong>bindpass</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password to use with <code class="docutils literal notranslate"><span class="pre">binddn</span></code> when performing user search</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Trusted CA to validate TLS certificate</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description for the LDAP auth backend mount</p></li>
<li><p><strong>groupattr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – LDAP attribute to follow on objects returned by groupfilter</p></li>
<li><p><strong>groupdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base DN under which to perform group search</p></li>
<li><p><strong>groupfilter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Go template used to construct group membership query</p></li>
<li><p><strong>insecure_tls</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Control whether or TLS certificates must be validated</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to mount the LDAP auth backend under</p></li>
<li><p><strong>starttls</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Control use of TLS when conecting to LDAP</p></li>
<li><p><strong>tls_max_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Maximum acceptable version of TLS</p></li>
<li><p><strong>tls_min_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Minimum acceptable version of TLS</p></li>
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
<li><p><strong>upndomain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The userPrincipalDomain used to construct UPN string</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the LDAP server</p></li>
<li><p><strong>use_token_groups</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Use the Active Directory tokenGroups constructed attribute of the user to find the group memberships</p></li>
<li><p><strong>userattr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Attribute on user object matching username passed in</p></li>
<li><p><strong>userdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base DN under which to perform user search</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/ldap_auth_backend.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/ldap_auth_backend.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.accessor">
<code class="sig-name descname">accessor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.accessor" title="Permalink to this definition">¶</a></dt>
<dd><p>The accessor for this auth mount.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.binddn">
<code class="sig-name descname">binddn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.binddn" title="Permalink to this definition">¶</a></dt>
<dd><p>DN of object to bind when performing user search</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.bindpass">
<code class="sig-name descname">bindpass</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.bindpass" title="Permalink to this definition">¶</a></dt>
<dd><p>Password to use with <code class="docutils literal notranslate"><span class="pre">binddn</span></code> when performing user search</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.certificate">
<code class="sig-name descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Trusted CA to validate TLS certificate</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description for the LDAP auth backend mount</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.groupattr">
<code class="sig-name descname">groupattr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.groupattr" title="Permalink to this definition">¶</a></dt>
<dd><p>LDAP attribute to follow on objects returned by groupfilter</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.groupdn">
<code class="sig-name descname">groupdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.groupdn" title="Permalink to this definition">¶</a></dt>
<dd><p>Base DN under which to perform group search</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.groupfilter">
<code class="sig-name descname">groupfilter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.groupfilter" title="Permalink to this definition">¶</a></dt>
<dd><p>Go template used to construct group membership query</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.insecure_tls">
<code class="sig-name descname">insecure_tls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.insecure_tls" title="Permalink to this definition">¶</a></dt>
<dd><p>Control whether or TLS certificates must be validated</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path to mount the LDAP auth backend under</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.starttls">
<code class="sig-name descname">starttls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.starttls" title="Permalink to this definition">¶</a></dt>
<dd><p>Control use of TLS when conecting to LDAP</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.tls_max_version">
<code class="sig-name descname">tls_max_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.tls_max_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum acceptable version of TLS</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.tls_min_version">
<code class="sig-name descname">tls_min_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.tls_min_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum acceptable version of TLS</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.token_bound_cidrs">
<code class="sig-name descname">token_bound_cidrs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.token_bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.token_explicit_max_ttl">
<code class="sig-name descname">token_explicit_max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.token_explicit_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.token_max_ttl">
<code class="sig-name descname">token_max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.token_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.token_no_default_policy">
<code class="sig-name descname">token_no_default_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.token_no_default_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.token_num_uses">
<code class="sig-name descname">token_num_uses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.token_num_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.token_period">
<code class="sig-name descname">token_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.token_period" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.token_policies">
<code class="sig-name descname">token_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.token_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.token_ttl">
<code class="sig-name descname">token_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.token_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.token_type">
<code class="sig-name descname">token_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.token_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of token that should be generated. Can be <code class="docutils literal notranslate"><span class="pre">service</span></code>,
<code class="docutils literal notranslate"><span class="pre">batch</span></code>, or <code class="docutils literal notranslate"><span class="pre">default</span></code> to use the mount’s tuned default (which unless changed will be
<code class="docutils literal notranslate"><span class="pre">service</span></code> tokens). For token store roles, there are two additional possibilities:
<code class="docutils literal notranslate"><span class="pre">default-service</span></code> and <code class="docutils literal notranslate"><span class="pre">default-batch</span></code> which specify the type to return unless the client
requests a different type at generation time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.upndomain">
<code class="sig-name descname">upndomain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.upndomain" title="Permalink to this definition">¶</a></dt>
<dd><p>The userPrincipalDomain used to construct UPN string</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the LDAP server</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.use_token_groups">
<code class="sig-name descname">use_token_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.use_token_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the Active Directory tokenGroups constructed attribute of the user to find the group memberships</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.userattr">
<code class="sig-name descname">userattr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.userattr" title="Permalink to this definition">¶</a></dt>
<dd><p>Attribute on user object matching username passed in</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackend.userdn">
<code class="sig-name descname">userdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.userdn" title="Permalink to this definition">¶</a></dt>
<dd><p>Base DN under which to perform user search</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.l_dap.AuthBackend.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessor=None</em>, <em class="sig-param">binddn=None</em>, <em class="sig-param">bindpass=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">deny_null_bind=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">discoverdn=None</em>, <em class="sig-param">groupattr=None</em>, <em class="sig-param">groupdn=None</em>, <em class="sig-param">groupfilter=None</em>, <em class="sig-param">insecure_tls=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">starttls=None</em>, <em class="sig-param">tls_max_version=None</em>, <em class="sig-param">tls_min_version=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em>, <em class="sig-param">upndomain=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">use_token_groups=None</em>, <em class="sig-param">userattr=None</em>, <em class="sig-param">userdn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackend resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The accessor for this auth mount.</p></li>
<li><p><strong>binddn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DN of object to bind when performing user search</p></li>
<li><p><strong>bindpass</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password to use with <code class="docutils literal notranslate"><span class="pre">binddn</span></code> when performing user search</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Trusted CA to validate TLS certificate</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description for the LDAP auth backend mount</p></li>
<li><p><strong>groupattr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – LDAP attribute to follow on objects returned by groupfilter</p></li>
<li><p><strong>groupdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base DN under which to perform group search</p></li>
<li><p><strong>groupfilter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Go template used to construct group membership query</p></li>
<li><p><strong>insecure_tls</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Control whether or TLS certificates must be validated</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to mount the LDAP auth backend under</p></li>
<li><p><strong>starttls</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Control use of TLS when conecting to LDAP</p></li>
<li><p><strong>tls_max_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Maximum acceptable version of TLS</p></li>
<li><p><strong>tls_min_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Minimum acceptable version of TLS</p></li>
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
<li><p><strong>upndomain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The userPrincipalDomain used to construct UPN string</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the LDAP server</p></li>
<li><p><strong>use_token_groups</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Use the Active Directory tokenGroups constructed attribute of the user to find the group memberships</p></li>
<li><p><strong>userattr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Attribute on user object matching username passed in</p></li>
<li><p><strong>userdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base DN under which to perform user search</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/ldap_auth_backend.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/ldap_auth_backend.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.l_dap.AuthBackend.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.l_dap.AuthBackend.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackend.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.l_dap.AuthBackendGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.l_dap.</code><code class="sig-name descname">AuthBackendGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">groupname=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackendGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create a group in an <a class="reference external" href="https://www.vaultproject.io/docs/auth/ldap.html">LDAP auth backend within Vault</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to the authentication backend</p></li>
<li><p><strong>groupname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The LDAP groupname</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Policies which should be granted to members of the group</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/ldap_auth_backend_group.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/ldap_auth_backend_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackendGroup.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackendGroup.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>Path to the authentication backend</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackendGroup.groupname">
<code class="sig-name descname">groupname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackendGroup.groupname" title="Permalink to this definition">¶</a></dt>
<dd><p>The LDAP groupname</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackendGroup.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackendGroup.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Policies which should be granted to members of the group</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.l_dap.AuthBackendGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">groupname=None</em>, <em class="sig-param">policies=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackendGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to the authentication backend</p></li>
<li><p><strong>groupname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The LDAP groupname</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Policies which should be granted to members of the group</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/ldap_auth_backend_group.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/ldap_auth_backend_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.l_dap.AuthBackendGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackendGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.l_dap.AuthBackendGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackendGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.l_dap.AuthBackendUser">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.l_dap.</code><code class="sig-name descname">AuthBackendUser</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackendUser" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create a user in an <a class="reference external" href="https://www.vaultproject.io/docs/auth/ldap.html">LDAP auth backend within Vault</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to the authentication backend</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Override LDAP groups which should be granted to user</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Policies which should be granted to user</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The LDAP username</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/ldap_auth_backend_user.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/ldap_auth_backend_user.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackendUser.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackendUser.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>Path to the authentication backend</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackendUser.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackendUser.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Override LDAP groups which should be granted to user</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackendUser.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackendUser.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Policies which should be granted to user</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.l_dap.AuthBackendUser.username">
<code class="sig-name descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackendUser.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The LDAP username</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.l_dap.AuthBackendUser.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">groups=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackendUser.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendUser resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to the authentication backend</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Override LDAP groups which should be granted to user</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Policies which should be granted to user</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The LDAP username</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/ldap_auth_backend_user.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/ldap_auth_backend_user.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.l_dap.AuthBackendUser.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackendUser.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.l_dap.AuthBackendUser.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.l_dap.AuthBackendUser.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
