---
title: Module token
linktitle: token
notitle: true
---

<div class="section" id="token">
<h1>token<a class="headerlink" href="#token" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.token"></span><dl class="class">
<dt id="pulumi_vault.token.AuthBackendRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.token.</code><code class="sig-name descname">AuthBackendRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allowed_policies=None</em>, <em class="sig-param">bound_cidrs=None</em>, <em class="sig-param">disallowed_policies=None</em>, <em class="sig-param">explicit_max_ttl=None</em>, <em class="sig-param">orphan=None</em>, <em class="sig-param">path_suffix=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">renewable=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages Token auth backend role in a Vault server. See the <a class="reference external" href="https://www.vaultproject.io/docs/auth/token.html">Vault
documentation</a> for more
information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of allowed policies for given role.</p></li>
<li><p><strong>bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, a list of
CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.</p></li>
<li><p><strong>disallowed_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of disallowed policies for given role.</p></li>
<li><p><strong>orphan</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, tokens created against this policy will be orphan tokens.</p></li>
<li><p><strong>path_suffix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tokens created against this role will have the given suffix as part of their path in addition to the role name.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>renewable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wether to disable the ability of the token to be renewed past its initial TTL.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role.</p></li>
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
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/token_auth_backend_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/token_auth_backend_role.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.token.AuthBackendRole.allowed_policies">
<code class="sig-name descname">allowed_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.allowed_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of allowed policies for given role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.token.AuthBackendRole.bound_cidrs">
<code class="sig-name descname">bound_cidrs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, a list of
CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.token.AuthBackendRole.disallowed_policies">
<code class="sig-name descname">disallowed_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.disallowed_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of disallowed policies for given role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.token.AuthBackendRole.orphan">
<code class="sig-name descname">orphan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.orphan" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, tokens created against this policy will be orphan tokens.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.token.AuthBackendRole.path_suffix">
<code class="sig-name descname">path_suffix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.path_suffix" title="Permalink to this definition">¶</a></dt>
<dd><p>Tokens created against this role will have the given suffix as part of their path in addition to the role name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.token.AuthBackendRole.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.period" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.token.AuthBackendRole.renewable">
<code class="sig-name descname">renewable</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.renewable" title="Permalink to this definition">¶</a></dt>
<dd><p>Wether to disable the ability of the token to be renewed past its initial TTL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.token.AuthBackendRole.role_name">
<code class="sig-name descname">role_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.token.AuthBackendRole.token_bound_cidrs">
<code class="sig-name descname">token_bound_cidrs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.token_bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.token.AuthBackendRole.token_explicit_max_ttl">
<code class="sig-name descname">token_explicit_max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.token_explicit_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.token.AuthBackendRole.token_max_ttl">
<code class="sig-name descname">token_max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.token_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.token.AuthBackendRole.token_no_default_policy">
<code class="sig-name descname">token_no_default_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.token_no_default_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.token.AuthBackendRole.token_num_uses">
<code class="sig-name descname">token_num_uses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.token_num_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.token.AuthBackendRole.token_period">
<code class="sig-name descname">token_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.token_period" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.token.AuthBackendRole.token_ttl">
<code class="sig-name descname">token_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.token_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.token.AuthBackendRole.token_type">
<code class="sig-name descname">token_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.token_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of token that should be generated. Can be <code class="docutils literal notranslate"><span class="pre">service</span></code>,
<code class="docutils literal notranslate"><span class="pre">batch</span></code>, or <code class="docutils literal notranslate"><span class="pre">default</span></code> to use the mount’s tuned default (which unless changed will be
<code class="docutils literal notranslate"><span class="pre">service</span></code> tokens). For token store roles, there are two additional possibilities:
<code class="docutils literal notranslate"><span class="pre">default-service</span></code> and <code class="docutils literal notranslate"><span class="pre">default-batch</span></code> which specify the type to return unless the client
requests a different type at generation time.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.token.AuthBackendRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allowed_policies=None</em>, <em class="sig-param">bound_cidrs=None</em>, <em class="sig-param">disallowed_policies=None</em>, <em class="sig-param">explicit_max_ttl=None</em>, <em class="sig-param">orphan=None</em>, <em class="sig-param">path_suffix=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">renewable=None</em>, <em class="sig-param">role_name=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of allowed policies for given role.</p></li>
<li><p><strong>bound_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, a list of
CIDRs valid as the source address for login requests. This value is also encoded into any resulting token.</p></li>
<li><p><strong>disallowed_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of disallowed policies for given role.</p></li>
<li><p><strong>orphan</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, tokens created against this policy will be orphan tokens.</p></li>
<li><p><strong>path_suffix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tokens created against this role will have the given suffix as part of their path in addition to the role name.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>renewable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wether to disable the ability of the token to be renewed past its initial TTL.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role.</p></li>
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
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/token_auth_backend_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/token_auth_backend_role.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.token.AuthBackendRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.token.AuthBackendRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.token.AuthBackendRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
