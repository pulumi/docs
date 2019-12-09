---
title: Module app_role
title_tag: Module app_role | Package pulumi_vault | Python SDK
linktitle: app_role
notitle: true
---

<div class="section" id="app-role">
<h1>app_role<a class="headerlink" href="#app-role" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.app_role"></span><dl class="class">
<dt id="pulumi_vault.app_role.AuthBackendLogin">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.app_role.</code><code class="sig-name descname">AuthBackendLogin</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">role_id=None</em>, <em class="sig-param">secret_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendLogin" title="Permalink to this definition">¶</a></dt>
<dd><p>Logs into Vault using the AppRole auth backend. See the <a class="reference external" href="https://www.vaultproject.io/docs/auth/approle.html">Vault
documentation</a> for more
information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique path of the Vault backend to log in with.</p></li>
<li><p><strong>role_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the role to log in with.</p></li>
<li><p><strong>secret_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secret ID of the role to log in with. Required
unless <code class="docutils literal notranslate"><span class="pre">bind_secret_id</span></code> is set to false on the role.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/approle_auth_backend_login.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/approle_auth_backend_login.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendLogin.accessor">
<code class="sig-name descname">accessor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendLogin.accessor" title="Permalink to this definition">¶</a></dt>
<dd><p>The accessor for the token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendLogin.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendLogin.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique path of the Vault backend to log in with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendLogin.client_token">
<code class="sig-name descname">client_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendLogin.client_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The Vault token created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendLogin.lease_duration">
<code class="sig-name descname">lease_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendLogin.lease_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>How long the token is valid for, in seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendLogin.lease_started">
<code class="sig-name descname">lease_started</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendLogin.lease_started" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time the lease started, in RFC 3339 format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendLogin.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendLogin.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>The metadata associated with the token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendLogin.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendLogin.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of policies applied to the token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendLogin.renewable">
<code class="sig-name descname">renewable</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendLogin.renewable" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the token is renewable or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendLogin.role_id">
<code class="sig-name descname">role_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendLogin.role_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the role to log in with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendLogin.secret_id">
<code class="sig-name descname">secret_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendLogin.secret_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret ID of the role to log in with. Required
unless <code class="docutils literal notranslate"><span class="pre">bind_secret_id</span></code> is set to false on the role.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.app_role.AuthBackendLogin.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessor=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">client_token=None</em>, <em class="sig-param">lease_duration=None</em>, <em class="sig-param">lease_started=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">renewable=None</em>, <em class="sig-param">role_id=None</em>, <em class="sig-param">secret_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendLogin.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendLogin resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The accessor for the token.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique path of the Vault backend to log in with.</p></li>
<li><p><strong>client_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Vault token created.</p></li>
<li><p><strong>lease_duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How long the token is valid for, in seconds.</p></li>
<li><p><strong>lease_started</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date and time the lease started, in RFC 3339 format.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The metadata associated with the token.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of policies applied to the token.</p></li>
<li><p><strong>renewable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the token is renewable or not.</p></li>
<li><p><strong>role_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the role to log in with.</p></li>
<li><p><strong>secret_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secret ID of the role to log in with. Required
unless <code class="docutils literal notranslate"><span class="pre">bind_secret_id</span></code> is set to false on the role.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/approle_auth_backend_login.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/approle_auth_backend_login.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.app_role.AuthBackendLogin.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendLogin.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.app_role.AuthBackendLogin.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendLogin.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.app_role.AuthBackendRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.app_role.</code><code class="sig-name descname">AuthBackendRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">bind_secret_id=None</em>, <em class="sig-param">bound_cidr_lists=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">role_id=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">secret_id_bound_cidrs=None</em>, <em class="sig-param">secret_id_num_uses=None</em>, <em class="sig-param">secret_id_ttl=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AppRole auth backend role in a Vault server. See the <a class="reference external" href="https://www.vaultproject.io/docs/auth/approle.html">Vault
documentation</a> for more
information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the auth backend to configure.
Defaults to <code class="docutils literal notranslate"><span class="pre">approle</span></code>.</p></li>
<li><p><strong>bind_secret_id</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to require <code class="docutils literal notranslate"><span class="pre">secret_id</span></code> to be
presented when logging in using this AppRole. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>bound_cidr_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set,
specifies blocks of IP addresses which can perform the login operation.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings
specifying the policies to be set on tokens issued using this role.</p></li>
<li><p><strong>role_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RoleID of this role. If not specified, one will be
auto-generated.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role.</p></li>
<li><p><strong>secret_id_bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set,
specifies blocks of IP addresses which can perform the login operation.</p></li>
<li><p><strong>secret_id_num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of times any particular SecretID
can be used to fetch a token from this AppRole, after which the SecretID will
expire. A value of zero will allow unlimited uses.</p></li>
<li><p><strong>secret_id_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of seconds after which any SecretID
expires.</p></li>
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
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/approle_auth_backend_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/approle_auth_backend_role.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name of the auth backend to configure.
Defaults to <code class="docutils literal notranslate"><span class="pre">approle</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.bind_secret_id">
<code class="sig-name descname">bind_secret_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.bind_secret_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to require <code class="docutils literal notranslate"><span class="pre">secret_id</span></code> to be
presented when logging in using this AppRole. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.bound_cidr_lists">
<code class="sig-name descname">bound_cidr_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.bound_cidr_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>If set,
specifies blocks of IP addresses which can perform the login operation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.period" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of strings
specifying the policies to be set on tokens issued using this role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.role_id">
<code class="sig-name descname">role_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.role_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The RoleID of this role. If not specified, one will be
auto-generated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.role_name">
<code class="sig-name descname">role_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.secret_id_bound_cidrs">
<code class="sig-name descname">secret_id_bound_cidrs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.secret_id_bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>If set,
specifies blocks of IP addresses which can perform the login operation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.secret_id_num_uses">
<code class="sig-name descname">secret_id_num_uses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.secret_id_num_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of times any particular SecretID
can be used to fetch a token from this AppRole, after which the SecretID will
expire. A value of zero will allow unlimited uses.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.secret_id_ttl">
<code class="sig-name descname">secret_id_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.secret_id_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of seconds after which any SecretID
expires.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.token_bound_cidrs">
<code class="sig-name descname">token_bound_cidrs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.token_bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.token_explicit_max_ttl">
<code class="sig-name descname">token_explicit_max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.token_explicit_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.token_max_ttl">
<code class="sig-name descname">token_max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.token_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.token_no_default_policy">
<code class="sig-name descname">token_no_default_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.token_no_default_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.token_num_uses">
<code class="sig-name descname">token_num_uses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.token_num_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.token_period">
<code class="sig-name descname">token_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.token_period" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.token_policies">
<code class="sig-name descname">token_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.token_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.token_ttl">
<code class="sig-name descname">token_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.token_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRole.token_type">
<code class="sig-name descname">token_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.token_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of token that should be generated. Can be <code class="docutils literal notranslate"><span class="pre">service</span></code>,
<code class="docutils literal notranslate"><span class="pre">batch</span></code>, or <code class="docutils literal notranslate"><span class="pre">default</span></code> to use the mount’s tuned default (which unless changed will be
<code class="docutils literal notranslate"><span class="pre">service</span></code> tokens). For token store roles, there are two additional possibilities:
<code class="docutils literal notranslate"><span class="pre">default-service</span></code> and <code class="docutils literal notranslate"><span class="pre">default-batch</span></code> which specify the type to return unless the client
requests a different type at generation time.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.app_role.AuthBackendRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">bind_secret_id=None</em>, <em class="sig-param">bound_cidr_lists=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">role_id=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">secret_id_bound_cidrs=None</em>, <em class="sig-param">secret_id_num_uses=None</em>, <em class="sig-param">secret_id_ttl=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the auth backend to configure.
Defaults to <code class="docutils literal notranslate"><span class="pre">approle</span></code>.</p></li>
<li><p><strong>bind_secret_id</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to require <code class="docutils literal notranslate"><span class="pre">secret_id</span></code> to be
presented when logging in using this AppRole. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>bound_cidr_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set,
specifies blocks of IP addresses which can perform the login operation.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings
specifying the policies to be set on tokens issued using this role.</p></li>
<li><p><strong>role_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The RoleID of this role. If not specified, one will be
auto-generated.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role.</p></li>
<li><p><strong>secret_id_bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set,
specifies blocks of IP addresses which can perform the login operation.</p></li>
<li><p><strong>secret_id_num_uses</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of times any particular SecretID
can be used to fetch a token from this AppRole, after which the SecretID will
expire. A value of zero will allow unlimited uses.</p></li>
<li><p><strong>secret_id_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of seconds after which any SecretID
expires.</p></li>
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
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/approle_auth_backend_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/approle_auth_backend_role.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.app_role.AuthBackendRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.app_role.AuthBackendRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.app_role.AuthBackendRoleSecretID">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.app_role.</code><code class="sig-name descname">AuthBackendRoleSecretID</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">cidr_lists=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">secret_id=None</em>, <em class="sig-param">wrapping_ttl=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRoleSecretID" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AppRole auth backend SecretID in a Vault server. See the <a class="reference external" href="https://www.vaultproject.io/docs/auth/approle.html">Vault
documentation</a> for more
information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidr_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, specifies blocks of IP addresses which can
perform the login operation using this SecretID.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON-encoded string containing metadata in
key-value pairs to be set on tokens issued with this SecretID.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role to create the SecretID for.</p></li>
<li><p><strong>secret_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SecretID to be created. If set, uses “Push”
mode.  Defaults to Vault auto-generating SecretIDs.</p></li>
<li><p><strong>wrapping_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set, the SecretID response will be
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/response-wrapping.html">response-wrapped</a>
and available for the duration specified. Only a single unwrapping of the
token is allowed.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/approle_auth_backend_role_secret_id.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/approle_auth_backend_role_secret_id.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRoleSecretID.accessor">
<code class="sig-name descname">accessor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRoleSecretID.accessor" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for this SecretID that can be safely logged.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRoleSecretID.cidr_lists">
<code class="sig-name descname">cidr_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRoleSecretID.cidr_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, specifies blocks of IP addresses which can
perform the login operation using this SecretID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRoleSecretID.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRoleSecretID.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON-encoded string containing metadata in
key-value pairs to be set on tokens issued with this SecretID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRoleSecretID.role_name">
<code class="sig-name descname">role_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRoleSecretID.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role to create the SecretID for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRoleSecretID.secret_id">
<code class="sig-name descname">secret_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRoleSecretID.secret_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The SecretID to be created. If set, uses “Push”
mode.  Defaults to Vault auto-generating SecretIDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRoleSecretID.wrapping_accessor">
<code class="sig-name descname">wrapping_accessor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRoleSecretID.wrapping_accessor" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for the response-wrapped SecretID that can
be safely logged.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRoleSecretID.wrapping_token">
<code class="sig-name descname">wrapping_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRoleSecretID.wrapping_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The token used to retrieve a response-wrapped SecretID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.AuthBackendRoleSecretID.wrapping_ttl">
<code class="sig-name descname">wrapping_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRoleSecretID.wrapping_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, the SecretID response will be
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/response-wrapping.html">response-wrapped</a>
and available for the duration specified. Only a single unwrapping of the
token is allowed.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.app_role.AuthBackendRoleSecretID.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">accessor=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">cidr_lists=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">secret_id=None</em>, <em class="sig-param">wrapping_accessor=None</em>, <em class="sig-param">wrapping_token=None</em>, <em class="sig-param">wrapping_ttl=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRoleSecretID.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendRoleSecretID resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for this SecretID that can be safely logged.</p></li>
<li><p><strong>cidr_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, specifies blocks of IP addresses which can
perform the login operation using this SecretID.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON-encoded string containing metadata in
key-value pairs to be set on tokens issued with this SecretID.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role to create the SecretID for.</p></li>
<li><p><strong>secret_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SecretID to be created. If set, uses “Push”
mode.  Defaults to Vault auto-generating SecretIDs.</p></li>
<li><p><strong>wrapping_accessor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the response-wrapped SecretID that can
be safely logged.</p></li>
<li><p><strong>wrapping_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The token used to retrieve a response-wrapped SecretID.</p></li>
<li><p><strong>wrapping_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>If set, the SecretID response will be
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/response-wrapping.html">response-wrapped</a>
and available for the duration specified. Only a single unwrapping of the
token is allowed.</p>
</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/approle_auth_backend_role_secret_id.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/approle_auth_backend_role_secret_id.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.app_role.AuthBackendRoleSecretID.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRoleSecretID.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.app_role.AuthBackendRoleSecretID.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.app_role.AuthBackendRoleSecretID.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.app_role.AwaitableGetAuthBackendRoleIdResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.app_role.</code><code class="sig-name descname">AwaitableGetAuthBackendRoleIdResult</code><span class="sig-paren">(</span><em class="sig-param">backend=None</em>, <em class="sig-param">role_id=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.app_role.AwaitableGetAuthBackendRoleIdResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_vault.app_role.GetAuthBackendRoleIdResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.app_role.</code><code class="sig-name descname">GetAuthBackendRoleIdResult</code><span class="sig-paren">(</span><em class="sig-param">backend=None</em>, <em class="sig-param">role_id=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.app_role.GetAuthBackendRoleIdResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAuthBackendRoleId.</p>
<dl class="attribute">
<dt id="pulumi_vault.app_role.GetAuthBackendRoleIdResult.role_id">
<code class="sig-name descname">role_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.GetAuthBackendRoleIdResult.role_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The RoleID of the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.app_role.GetAuthBackendRoleIdResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.app_role.GetAuthBackendRoleIdResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_vault.app_role.get_auth_backend_role_id">
<code class="sig-prename descclassname">pulumi_vault.app_role.</code><code class="sig-name descname">get_auth_backend_role_id</code><span class="sig-paren">(</span><em class="sig-param">backend=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.app_role.get_auth_backend_role_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Reads the Role ID of an AppRole from a Vault server.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>backend</strong> (<em>str</em>) – The unique name for the AppRole backend the role to
retrieve a RoleID for resides in. Defaults to “approle”.</p></li>
<li><p><strong>role_name</strong> (<em>str</em>) – The name of the role to retrieve the Role ID for.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/d/approle_auth_backend_role_id.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/d/approle_auth_backend_role_id.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
