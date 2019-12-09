---
title: Module azure
title_tag: Module azure | Package pulumi_vault | Python SDK
linktitle: azure
notitle: true
---

<div class="section" id="azure">
<h1>azure<a class="headerlink" href="#azure" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.azure"></span><dl class="class">
<dt id="pulumi_vault.azure.AuthBackendConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.azure.</code><code class="sig-name descname">AuthBackendConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">environment=None</em>, <em class="sig-param">resource=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.azure.AuthBackendConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AuthBackendConfig resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the Azure auth backend being configured was
mounted at.  Defaults to <code class="docutils literal notranslate"><span class="pre">azure</span></code>.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client id for credentials to query the Azure APIs.
Currently read permissions to query compute resources are required.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client secret for credentials to query the
Azure APIs.</p></li>
<li><p><strong>environment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure cloud environment. Valid values:
AzurePublicCloud, AzureUSGovernmentCloud, AzureChinaCloud,
AzureGermanCloud.  Defaults to <code class="docutils literal notranslate"><span class="pre">AzurePublicCloud</span></code>.</p></li>
<li><p><strong>resource</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The configured URL for the application registered in
Azure Active Directory.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tenant id for the Azure Active Directory
organization.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/azure_auth_backend_config.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/azure_auth_backend_config.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendConfig.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendConfig.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>The path the Azure auth backend being configured was
mounted at.  Defaults to <code class="docutils literal notranslate"><span class="pre">azure</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendConfig.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendConfig.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The client id for credentials to query the Azure APIs.
Currently read permissions to query compute resources are required.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendConfig.client_secret">
<code class="sig-name descname">client_secret</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendConfig.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>The client secret for credentials to query the
Azure APIs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendConfig.environment">
<code class="sig-name descname">environment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendConfig.environment" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure cloud environment. Valid values:
AzurePublicCloud, AzureUSGovernmentCloud, AzureChinaCloud,
AzureGermanCloud.  Defaults to <code class="docutils literal notranslate"><span class="pre">AzurePublicCloud</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendConfig.resource">
<code class="sig-name descname">resource</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendConfig.resource" title="Permalink to this definition">¶</a></dt>
<dd><p>The configured URL for the application registered in
Azure Active Directory.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendConfig.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendConfig.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The tenant id for the Azure Active Directory
organization.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.azure.AuthBackendConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">environment=None</em>, <em class="sig-param">resource=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.azure.AuthBackendConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path the Azure auth backend being configured was
mounted at.  Defaults to <code class="docutils literal notranslate"><span class="pre">azure</span></code>.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client id for credentials to query the Azure APIs.
Currently read permissions to query compute resources are required.</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client secret for credentials to query the
Azure APIs.</p></li>
<li><p><strong>environment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure cloud environment. Valid values:
AzurePublicCloud, AzureUSGovernmentCloud, AzureChinaCloud,
AzureGermanCloud.  Defaults to <code class="docutils literal notranslate"><span class="pre">AzurePublicCloud</span></code>.</p></li>
<li><p><strong>resource</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The configured URL for the application registered in
Azure Active Directory.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tenant id for the Azure Active Directory
organization.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/azure_auth_backend_config.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/azure_auth_backend_config.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.azure.AuthBackendConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.azure.AuthBackendConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.azure.AuthBackendConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.azure.AuthBackendConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.azure.AuthBackendRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.azure.</code><code class="sig-name descname">AuthBackendRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">bound_group_ids=None</em>, <em class="sig-param">bound_locations=None</em>, <em class="sig-param">bound_resource_groups=None</em>, <em class="sig-param">bound_scale_sets=None</em>, <em class="sig-param">bound_service_principal_ids=None</em>, <em class="sig-param">bound_subscription_ids=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure auth backend role in a Vault server. Roles constrain the
instances or principals that can perform the login operation against the
backend. See the <a class="reference external" href="https://www.vaultproject.io/docs/auth/azure.html">Vault
documentation</a> for more
information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bound_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the groups
that can perform the login operation that they should be using the group
ID specified by this field.</p></li>
<li><p><strong>bound_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the virtual machines
that can perform the login operation that the location in their identity
document must match the one specified by this field.</p></li>
<li><p><strong>bound_resource_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the virtual
machiness that can perform the login operation that they be associated with
the resource group that matches the value specified by this field.</p></li>
<li><p><strong>bound_scale_sets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the virtual
machines that can perform the login operation that they must match the scale set
specified by this field.</p></li>
<li><p><strong>bound_service_principal_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the
service principals that can perform the login operation that they should be possess
the ids specified by this field.</p></li>
<li><p><strong>bound_subscription_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the subscriptions
that can perform the login operation to ones which  matches the value specified by this
field.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum allowed lifetime of tokens
issued using this role, provided as a number of seconds.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings
specifying the policies to be set on tokens issued using this role.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role.</p></li>
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
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/azure_auth_backend_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/azure_auth_backend_role.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.bound_group_ids">
<code class="sig-name descname">bound_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.bound_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, defines a constraint on the groups
that can perform the login operation that they should be using the group
ID specified by this field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.bound_locations">
<code class="sig-name descname">bound_locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.bound_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, defines a constraint on the virtual machines
that can perform the login operation that the location in their identity
document must match the one specified by this field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.bound_resource_groups">
<code class="sig-name descname">bound_resource_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.bound_resource_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, defines a constraint on the virtual
machiness that can perform the login operation that they be associated with
the resource group that matches the value specified by this field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.bound_scale_sets">
<code class="sig-name descname">bound_scale_sets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.bound_scale_sets" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, defines a constraint on the virtual
machines that can perform the login operation that they must match the scale set
specified by this field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.bound_service_principal_ids">
<code class="sig-name descname">bound_service_principal_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.bound_service_principal_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, defines a constraint on the
service principals that can perform the login operation that they should be possess
the ids specified by this field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.bound_subscription_ids">
<code class="sig-name descname">bound_subscription_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.bound_subscription_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, defines a constraint on the subscriptions
that can perform the login operation to ones which  matches the value specified by this
field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.max_ttl">
<code class="sig-name descname">max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum allowed lifetime of tokens
issued using this role, provided as a number of seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.period" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of strings
specifying the policies to be set on tokens issued using this role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.token_bound_cidrs">
<code class="sig-name descname">token_bound_cidrs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.token_bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.token_explicit_max_ttl">
<code class="sig-name descname">token_explicit_max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.token_explicit_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.token_max_ttl">
<code class="sig-name descname">token_max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.token_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.token_no_default_policy">
<code class="sig-name descname">token_no_default_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.token_no_default_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.token_num_uses">
<code class="sig-name descname">token_num_uses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.token_num_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.token_period">
<code class="sig-name descname">token_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.token_period" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.token_policies">
<code class="sig-name descname">token_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.token_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.token_ttl">
<code class="sig-name descname">token_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.token_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.token_type">
<code class="sig-name descname">token_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.token_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of token that should be generated. Can be <code class="docutils literal notranslate"><span class="pre">service</span></code>,
<code class="docutils literal notranslate"><span class="pre">batch</span></code>, or <code class="docutils literal notranslate"><span class="pre">default</span></code> to use the mount’s tuned default (which unless changed will be
<code class="docutils literal notranslate"><span class="pre">service</span></code> tokens). For token store roles, there are two additional possibilities:
<code class="docutils literal notranslate"><span class="pre">default-service</span></code> and <code class="docutils literal notranslate"><span class="pre">default-batch</span></code> which specify the type to return unless the client
requests a different type at generation time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.AuthBackendRole.ttl">
<code class="sig-name descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL period of tokens issued
using this role, provided as a number of seconds.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.azure.AuthBackendRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">bound_group_ids=None</em>, <em class="sig-param">bound_locations=None</em>, <em class="sig-param">bound_resource_groups=None</em>, <em class="sig-param">bound_scale_sets=None</em>, <em class="sig-param">bound_service_principal_ids=None</em>, <em class="sig-param">bound_subscription_ids=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em>, <em class="sig-param">ttl=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bound_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the groups
that can perform the login operation that they should be using the group
ID specified by this field.</p></li>
<li><p><strong>bound_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the virtual machines
that can perform the login operation that the location in their identity
document must match the one specified by this field.</p></li>
<li><p><strong>bound_resource_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the virtual
machiness that can perform the login operation that they be associated with
the resource group that matches the value specified by this field.</p></li>
<li><p><strong>bound_scale_sets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the virtual
machines that can perform the login operation that they must match the scale set
specified by this field.</p></li>
<li><p><strong>bound_service_principal_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the
service principals that can perform the login operation that they should be possess
the ids specified by this field.</p></li>
<li><p><strong>bound_subscription_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If set, defines a constraint on the subscriptions
that can perform the login operation to ones which  matches the value specified by this
field.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum allowed lifetime of tokens
issued using this role, provided as a number of seconds.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings
specifying the policies to be set on tokens issued using this role.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role.</p></li>
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
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/azure_auth_backend_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/azure_auth_backend_role.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.azure.AuthBackendRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.azure.AuthBackendRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.azure.AuthBackendRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.azure.Backend">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.azure.</code><code class="sig-name descname">Backend</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">environment=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">subscription_id=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.azure.Backend" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Backend resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/azure_secret_backend.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/azure_secret_backend.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_vault.azure.Backend.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">client_secret=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">environment=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">subscription_id=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.azure.Backend.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Backend resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/azure_secret_backend.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/azure_secret_backend.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.azure.Backend.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.azure.Backend.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.azure.Backend.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.azure.Backend.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.azure.BackendRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.azure.</code><code class="sig-name descname">BackendRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_object_id=None</em>, <em class="sig-param">azure_roles=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.azure.BackendRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a BackendRole resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application Object ID for an existing service principal that will
be used instead of creating dynamic service principals. If present, <code class="docutils literal notranslate"><span class="pre">azure_roles</span></code> will be ignored.</p></li>
<li><p><strong>azure_roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Azure roles to be assigned to the generated service principal.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to the mounted Azure auth backend</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the maximum TTL for service principals generated using this role. Accepts time
suffixed strings (“1h”) or an integer number of seconds. Defaults to the system/engine max TTL time.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Azure role</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the default TTL for service principals generated using this role.
Accepts time suffixed strings (“1h”) or an integer number of seconds. Defaults to the system/engine default TTL time.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>azure_roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">role_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/azure_secret_backend_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/azure_secret_backend_role.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_vault.azure.BackendRole.application_object_id">
<code class="sig-name descname">application_object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.BackendRole.application_object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Application Object ID for an existing service principal that will
be used instead of creating dynamic service principals. If present, <code class="docutils literal notranslate"><span class="pre">azure_roles</span></code> will be ignored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.BackendRole.azure_roles">
<code class="sig-name descname">azure_roles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.BackendRole.azure_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Azure roles to be assigned to the generated service principal.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">role_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.BackendRole.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.BackendRole.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>Path to the mounted Azure auth backend</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.BackendRole.max_ttl">
<code class="sig-name descname">max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.BackendRole.max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum TTL for service principals generated using this role. Accepts time
suffixed strings (“1h”) or an integer number of seconds. Defaults to the system/engine max TTL time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.BackendRole.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.BackendRole.role" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Azure role</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.azure.BackendRole.ttl">
<code class="sig-name descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.azure.BackendRole.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the default TTL for service principals generated using this role.
Accepts time suffixed strings (“1h”) or an integer number of seconds. Defaults to the system/engine default TTL time.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.azure.BackendRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_object_id=None</em>, <em class="sig-param">azure_roles=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">ttl=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.azure.BackendRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BackendRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application Object ID for an existing service principal that will
be used instead of creating dynamic service principals. If present, <code class="docutils literal notranslate"><span class="pre">azure_roles</span></code> will be ignored.</p></li>
<li><p><strong>azure_roles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Azure roles to be assigned to the generated service principal.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to the mounted Azure auth backend</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the maximum TTL for service principals generated using this role. Accepts time
suffixed strings (“1h”) or an integer number of seconds. Defaults to the system/engine max TTL time.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Azure role</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the default TTL for service principals generated using this role.
Accepts time suffixed strings (“1h”) or an integer number of seconds. Defaults to the system/engine default TTL time.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>azure_roles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">role_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/azure_secret_backend_role.html.markdown">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/azure_secret_backend_role.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.azure.BackendRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.azure.BackendRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.azure.BackendRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.azure.BackendRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
