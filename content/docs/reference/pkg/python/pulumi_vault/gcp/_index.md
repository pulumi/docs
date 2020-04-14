---
title: Module gcp
title_tag: Module gcp | Package pulumi_vault | Python SDK
linktitle: gcp
notitle: true
---

<div class="section" id="gcp">
<h1>gcp<a class="headerlink" href="#gcp" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.gcp"></span><dl class="class">
<dt id="pulumi_vault.gcp.AuthBackend">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.gcp.</code><code class="sig-name descname">AuthBackend</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_email=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">credentials=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">private_key_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.gcp.AuthBackend" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to configure the <a class="reference external" href="https://www.vaultproject.io/docs/auth/gcp.html">GCP auth backend within Vault</a>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/gcp_auth_backend.html.md">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/gcp_auth_backend.html.md</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The clients email associated with the credentials</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Client ID of the credentials</p></li>
<li><p><strong>credentials</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON string containing the contents of a GCP credentials file. If this value is empty, Vault will try to use Application Default Credentials from the machine on which the Vault server is running.</p></li>
<li><p><strong>private_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the private key from the credentials</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GCP Project ID</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackend.client_email">
<code class="sig-name descname">client_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackend.client_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The clients email associated with the credentials</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackend.client_id">
<code class="sig-name descname">client_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackend.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Client ID of the credentials</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackend.credentials">
<code class="sig-name descname">credentials</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackend.credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON string containing the contents of a GCP credentials file. If this value is empty, Vault will try to use Application Default Credentials from the machine on which the Vault server is running.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackend.private_key_id">
<code class="sig-name descname">private_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackend.private_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the private key from the credentials</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackend.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackend.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCP Project ID</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.gcp.AuthBackend.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">client_email=None</em>, <em class="sig-param">client_id=None</em>, <em class="sig-param">credentials=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">private_key_id=None</em>, <em class="sig-param">project_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.gcp.AuthBackend.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackend resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The clients email associated with the credentials</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Client ID of the credentials</p></li>
<li><p><strong>credentials</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON string containing the contents of a GCP credentials file. If this value is empty, Vault will try to use Application Default Credentials from the machine on which the Vault server is running.</p></li>
<li><p><strong>private_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the private key from the credentials</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GCP Project ID</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.gcp.AuthBackend.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.gcp.AuthBackend.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.gcp.AuthBackend.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.gcp.AuthBackend.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.gcp.AuthBackendRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.gcp.</code><code class="sig-name descname">AuthBackendRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_group_aliases=None</em>, <em class="sig-param">allow_gce_inference=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">bound_instance_groups=None</em>, <em class="sig-param">bound_labels=None</em>, <em class="sig-param">bound_projects=None</em>, <em class="sig-param">bound_regions=None</em>, <em class="sig-param">bound_service_accounts=None</em>, <em class="sig-param">bound_zones=None</em>, <em class="sig-param">max_jwt_exp=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create a role in an <a class="reference external" href="https://www.vaultproject.io/docs/auth/gcp.html">GCP auth backend within Vault</a>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/gcp_auth_backend_role.html.md">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/gcp_auth_backend_role.html.md</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_gce_inference</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag to determine if this role should allow GCE instances to authenticate by inferring service accounts from the GCE identity metadata token.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to the mounted GCP auth backend</p></li>
<li><p><strong>bound_instance_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The instance groups that an authorized instance must belong to in order to be authenticated. If specified, either <code class="docutils literal notranslate"><span class="pre">bound_zones</span></code> or <code class="docutils literal notranslate"><span class="pre">bound_regions</span></code> must be set too.</p></li>
<li><p><strong>bound_labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A comma-separated list of GCP labels formatted as <code class="docutils literal notranslate"><span class="pre">&quot;key:value&quot;</span></code> strings that must be set on authorized GCE instances. Because GCP labels are not currently ACL’d, we recommend that this be used in conjunction with other restrictions.</p></li>
<li><p><strong>bound_projects</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – GCP Projects that the role exists within</p></li>
<li><p><strong>bound_regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of regions that a GCE instance must belong to in order to be authenticated. If bound_instance_groups is provided, it is assumed to be a regional group and the group must belong to this region. If bound_zones are provided, this attribute is ignored.</p></li>
<li><p><strong>bound_service_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – GCP Service Accounts allowed to issue tokens under this role. (Note: <strong>Required</strong> if role is <code class="docutils literal notranslate"><span class="pre">iam</span></code>)</p></li>
<li><p><strong>bound_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of zones that a GCE instance must belong to in order to be authenticated. If bound_instance_groups is provided, it is assumed to be a zonal group and the group must belong to this zone.</p></li>
<li><p><strong>max_jwt_exp</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The number of seconds past the time of authentication that the login param JWT must expire within. For example, if a user attempts to login with a token that expires within an hour and this is set to 15 minutes, Vault will return an error prompting the user to create a new signed JWT with a shorter <code class="docutils literal notranslate"><span class="pre">exp</span></code>. The GCE metadata tokens currently do not allow the <code class="docutils literal notranslate"><span class="pre">exp</span></code> claim to be customized.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum allowed lifetime of tokens
issued using this role, provided as a number of seconds.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings
specifying the policies to be set on tokens issued using this role.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the GCP role</p></li>
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
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TTL period of tokens issued
using this role, provided as a number of seconds.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of GCP authentication role (either <code class="docutils literal notranslate"><span class="pre">gce</span></code> or <code class="docutils literal notranslate"><span class="pre">iam</span></code>)</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.allow_gce_inference">
<code class="sig-name descname">allow_gce_inference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.allow_gce_inference" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag to determine if this role should allow GCE instances to authenticate by inferring service accounts from the GCE identity metadata token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>Path to the mounted GCP auth backend</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.bound_instance_groups">
<code class="sig-name descname">bound_instance_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.bound_instance_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance groups that an authorized instance must belong to in order to be authenticated. If specified, either <code class="docutils literal notranslate"><span class="pre">bound_zones</span></code> or <code class="docutils literal notranslate"><span class="pre">bound_regions</span></code> must be set too.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.bound_labels">
<code class="sig-name descname">bound_labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.bound_labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma-separated list of GCP labels formatted as <code class="docutils literal notranslate"><span class="pre">&quot;key:value&quot;</span></code> strings that must be set on authorized GCE instances. Because GCP labels are not currently ACL’d, we recommend that this be used in conjunction with other restrictions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.bound_projects">
<code class="sig-name descname">bound_projects</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.bound_projects" title="Permalink to this definition">¶</a></dt>
<dd><p>GCP Projects that the role exists within</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.bound_regions">
<code class="sig-name descname">bound_regions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.bound_regions" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of regions that a GCE instance must belong to in order to be authenticated. If bound_instance_groups is provided, it is assumed to be a regional group and the group must belong to this region. If bound_zones are provided, this attribute is ignored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.bound_service_accounts">
<code class="sig-name descname">bound_service_accounts</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.bound_service_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>GCP Service Accounts allowed to issue tokens under this role. (Note: <strong>Required</strong> if role is <code class="docutils literal notranslate"><span class="pre">iam</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.bound_zones">
<code class="sig-name descname">bound_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.bound_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of zones that a GCE instance must belong to in order to be authenticated. If bound_instance_groups is provided, it is assumed to be a zonal group and the group must belong to this zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.max_jwt_exp">
<code class="sig-name descname">max_jwt_exp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.max_jwt_exp" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of seconds past the time of authentication that the login param JWT must expire within. For example, if a user attempts to login with a token that expires within an hour and this is set to 15 minutes, Vault will return an error prompting the user to create a new signed JWT with a shorter <code class="docutils literal notranslate"><span class="pre">exp</span></code>. The GCE metadata tokens currently do not allow the <code class="docutils literal notranslate"><span class="pre">exp</span></code> claim to be customized.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.max_ttl">
<code class="sig-name descname">max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum allowed lifetime of tokens
issued using this role, provided as a number of seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.period" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.policies">
<code class="sig-name descname">policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of strings
specifying the policies to be set on tokens issued using this role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.role" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the GCP role</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.token_bound_cidrs">
<code class="sig-name descname">token_bound_cidrs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.token_bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>List of CIDR blocks; if set, specifies blocks of IP
addresses which can authenticate successfully, and ties the resulting token to these blocks
as well.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.token_explicit_max_ttl">
<code class="sig-name descname">token_explicit_max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.token_explicit_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, will encode an
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">explicit max TTL</a>
onto the token in number of seconds. This is a hard cap even if <code class="docutils literal notranslate"><span class="pre">token_ttl</span></code> and
<code class="docutils literal notranslate"><span class="pre">token_max_ttl</span></code> would otherwise allow a renewal.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.token_max_ttl">
<code class="sig-name descname">token_max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.token_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.token_no_default_policy">
<code class="sig-name descname">token_no_default_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.token_no_default_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, the default policy will not be set on
generated tokens; otherwise it will be added to the policies set in token_policies.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.token_num_uses">
<code class="sig-name descname">token_num_uses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.token_num_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>The
<a class="reference external" href="https://www.vaultproject.io/docs/concepts/tokens.html#token-time-to-live-periodic-tokens-and-explicit-max-ttls">period</a>,
if any, in number of seconds to set on the token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.token_period">
<code class="sig-name descname">token_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.token_period" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.token_policies">
<code class="sig-name descname">token_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.token_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>List of policies to encode onto generated tokens. Depending
on the auth method, this list may be supplemented by user/group/other values.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.token_ttl">
<code class="sig-name descname">token_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.token_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The incremental lifetime for generated tokens in number of seconds.
Its current value will be referenced at renewal time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.token_type">
<code class="sig-name descname">token_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.token_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of token that should be generated. Can be <code class="docutils literal notranslate"><span class="pre">service</span></code>,
<code class="docutils literal notranslate"><span class="pre">batch</span></code>, or <code class="docutils literal notranslate"><span class="pre">default</span></code> to use the mount’s tuned default (which unless changed will be
<code class="docutils literal notranslate"><span class="pre">service</span></code> tokens). For token store roles, there are two additional possibilities:
<code class="docutils literal notranslate"><span class="pre">default-service</span></code> and <code class="docutils literal notranslate"><span class="pre">default-batch</span></code> which specify the type to return unless the client
requests a different type at generation time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.ttl">
<code class="sig-name descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL period of tokens issued
using this role, provided as a number of seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.AuthBackendRole.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of GCP authentication role (either <code class="docutils literal notranslate"><span class="pre">gce</span></code> or <code class="docutils literal notranslate"><span class="pre">iam</span></code>)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.gcp.AuthBackendRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_group_aliases=None</em>, <em class="sig-param">allow_gce_inference=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">bound_instance_groups=None</em>, <em class="sig-param">bound_labels=None</em>, <em class="sig-param">bound_projects=None</em>, <em class="sig-param">bound_regions=None</em>, <em class="sig-param">bound_service_accounts=None</em>, <em class="sig-param">bound_zones=None</em>, <em class="sig-param">max_jwt_exp=None</em>, <em class="sig-param">max_ttl=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">policies=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_gce_inference</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag to determine if this role should allow GCE instances to authenticate by inferring service accounts from the GCE identity metadata token.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to the mounted GCP auth backend</p></li>
<li><p><strong>bound_instance_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The instance groups that an authorized instance must belong to in order to be authenticated. If specified, either <code class="docutils literal notranslate"><span class="pre">bound_zones</span></code> or <code class="docutils literal notranslate"><span class="pre">bound_regions</span></code> must be set too.</p></li>
<li><p><strong>bound_labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A comma-separated list of GCP labels formatted as <code class="docutils literal notranslate"><span class="pre">&quot;key:value&quot;</span></code> strings that must be set on authorized GCE instances. Because GCP labels are not currently ACL’d, we recommend that this be used in conjunction with other restrictions.</p></li>
<li><p><strong>bound_projects</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – GCP Projects that the role exists within</p></li>
<li><p><strong>bound_regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of regions that a GCE instance must belong to in order to be authenticated. If bound_instance_groups is provided, it is assumed to be a regional group and the group must belong to this region. If bound_zones are provided, this attribute is ignored.</p></li>
<li><p><strong>bound_service_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – GCP Service Accounts allowed to issue tokens under this role. (Note: <strong>Required</strong> if role is <code class="docutils literal notranslate"><span class="pre">iam</span></code>)</p></li>
<li><p><strong>bound_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of zones that a GCE instance must belong to in order to be authenticated. If bound_instance_groups is provided, it is assumed to be a zonal group and the group must belong to this zone.</p></li>
<li><p><strong>max_jwt_exp</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The number of seconds past the time of authentication that the login param JWT must expire within. For example, if a user attempts to login with a token that expires within an hour and this is set to 15 minutes, Vault will return an error prompting the user to create a new signed JWT with a shorter <code class="docutils literal notranslate"><span class="pre">exp</span></code>. The GCE metadata tokens currently do not allow the <code class="docutils literal notranslate"><span class="pre">exp</span></code> claim to be customized.</p></li>
<li><p><strong>max_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum allowed lifetime of tokens
issued using this role, provided as a number of seconds.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set, indicates that the
token generated using this role should never expire. The token should be renewed within the
duration specified by this value. At each renewal, the token’s TTL will be set to the
value of this field. Specified in seconds.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings
specifying the policies to be set on tokens issued using this role.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the GCP role</p></li>
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
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TTL period of tokens issued
using this role, provided as a number of seconds.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of GCP authentication role (either <code class="docutils literal notranslate"><span class="pre">gce</span></code> or <code class="docutils literal notranslate"><span class="pre">iam</span></code>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.gcp.AuthBackendRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.gcp.AuthBackendRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.gcp.AuthBackendRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.gcp.SecretBackend">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.gcp.</code><code class="sig-name descname">SecretBackend</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">credentials=None</em>, <em class="sig-param">default_lease_ttl_seconds=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">max_lease_ttl_seconds=None</em>, <em class="sig-param">path=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.gcp.SecretBackend" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecretBackend resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] credentials: The GCP service account credentials in JSON format.
:param pulumi.Input[float] default_lease_ttl_seconds: The default TTL for credentials</p>
<blockquote>
<div><p>issued by this backend. Defaults to ‘0’.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-friendly description for this backend.</p></li>
<li><p><strong>max_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum TTL that can be requested
for credentials issued by this backend. Defaults to ‘0’.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique path this backend should be mounted at. Must
not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">gcp</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_vault.gcp.SecretBackend.credentials">
<code class="sig-name descname">credentials</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.SecretBackend.credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCP service account credentials in JSON format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.SecretBackend.default_lease_ttl_seconds">
<code class="sig-name descname">default_lease_ttl_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.SecretBackend.default_lease_ttl_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The default TTL for credentials
issued by this backend. Defaults to ‘0’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.SecretBackend.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.SecretBackend.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-friendly description for this backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.SecretBackend.max_lease_ttl_seconds">
<code class="sig-name descname">max_lease_ttl_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.SecretBackend.max_lease_ttl_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum TTL that can be requested
for credentials issued by this backend. Defaults to ‘0’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.SecretBackend.path">
<code class="sig-name descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.SecretBackend.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique path this backend should be mounted at. Must
not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">gcp</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.gcp.SecretBackend.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">credentials=None</em>, <em class="sig-param">default_lease_ttl_seconds=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">max_lease_ttl_seconds=None</em>, <em class="sig-param">path=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.gcp.SecretBackend.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretBackend resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>credentials</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GCP service account credentials in JSON format.</p></li>
<li><p><strong>default_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The default TTL for credentials
issued by this backend. Defaults to ‘0’.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-friendly description for this backend.</p></li>
<li><p><strong>max_lease_ttl_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum TTL that can be requested
for credentials issued by this backend. Defaults to ‘0’.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique path this backend should be mounted at. Must
not begin or end with a <code class="docutils literal notranslate"><span class="pre">/</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">gcp</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.gcp.SecretBackend.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.gcp.SecretBackend.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.gcp.SecretBackend.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.gcp.SecretBackend.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.gcp.SecretRoleset">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.gcp.</code><code class="sig-name descname">SecretRoleset</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">bindings=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">roleset=None</em>, <em class="sig-param">secret_type=None</em>, <em class="sig-param">token_scopes=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.gcp.SecretRoleset" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Roleset in the <a class="reference external" href="https://www.vaultproject.io/docs/secrets/gcp/index.html">GCP Secrets Engine</a> for Vault.</p>
<p>Each Roleset is <a class="reference external" href="https://www.vaultproject.io/docs/secrets/gcp/index.html#service-accounts-are-tied-to-rolesets">tied</a> to a Service Account, and can have one or more <a class="reference external" href="https://www.vaultproject.io/docs/secrets/gcp/index.html#roleset-bindings">bindings</a> associated with it.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/gcp_secret_roleset.html.md">https://github.com/terraform-providers/terraform-provider-vault/blob/master/website/docs/r/gcp_secret_roleset.html.md</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path where the GCP Secrets Engine is mounted</p></li>
<li><p><strong>bindings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Bindings to create for this roleset. This can be specified multiple times for multiple bindings. Structure is documented below.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the GCP project that this roleset’s service account will belong to.</p></li>
<li><p><strong>roleset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Roleset to create</p></li>
<li><p><strong>secret_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of secret generated for this role set. Accepted values: <code class="docutils literal notranslate"><span class="pre">access_token</span></code>, <code class="docutils literal notranslate"><span class="pre">service_account_key</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">access_token</span></code>.</p></li>
<li><p><strong>token_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of OAuth scopes to assign to <code class="docutils literal notranslate"><span class="pre">access_token</span></code> secrets generated under this role set (<code class="docutils literal notranslate"><span class="pre">access_token</span></code> role sets only).</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bindings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Resource or resource path for which IAM policy information will be bound. The resource path may be specified in a few different <a class="reference external" href="https://www.vaultproject.io/docs/secrets/gcp/index.html#roleset-bindings">formats</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">roles</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of <a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles">GCP IAM roles</a> for the resource.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_vault.gcp.SecretRoleset.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.SecretRoleset.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>Path where the GCP Secrets Engine is mounted</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.SecretRoleset.bindings">
<code class="sig-name descname">bindings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.SecretRoleset.bindings" title="Permalink to this definition">¶</a></dt>
<dd><p>Bindings to create for this roleset. This can be specified multiple times for multiple bindings. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Resource or resource path for which IAM policy information will be bound. The resource path may be specified in a few different <a class="reference external" href="https://www.vaultproject.io/docs/secrets/gcp/index.html#roleset-bindings">formats</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">roles</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of <a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles">GCP IAM roles</a> for the resource.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.SecretRoleset.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.SecretRoleset.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the GCP project that this roleset’s service account will belong to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.SecretRoleset.roleset">
<code class="sig-name descname">roleset</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.SecretRoleset.roleset" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Roleset to create</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.SecretRoleset.secret_type">
<code class="sig-name descname">secret_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.SecretRoleset.secret_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of secret generated for this role set. Accepted values: <code class="docutils literal notranslate"><span class="pre">access_token</span></code>, <code class="docutils literal notranslate"><span class="pre">service_account_key</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">access_token</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.SecretRoleset.service_account_email">
<code class="sig-name descname">service_account_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.SecretRoleset.service_account_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email of the service account created by Vault for this Roleset</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.gcp.SecretRoleset.token_scopes">
<code class="sig-name descname">token_scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.gcp.SecretRoleset.token_scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of OAuth scopes to assign to <code class="docutils literal notranslate"><span class="pre">access_token</span></code> secrets generated under this role set (<code class="docutils literal notranslate"><span class="pre">access_token</span></code> role sets only).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.gcp.SecretRoleset.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">bindings=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">roleset=None</em>, <em class="sig-param">secret_type=None</em>, <em class="sig-param">service_account_email=None</em>, <em class="sig-param">token_scopes=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.gcp.SecretRoleset.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecretRoleset resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path where the GCP Secrets Engine is mounted</p></li>
<li><p><strong>bindings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Bindings to create for this roleset. This can be specified multiple times for multiple bindings. Structure is documented below.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the GCP project that this roleset’s service account will belong to.</p></li>
<li><p><strong>roleset</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Roleset to create</p></li>
<li><p><strong>secret_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of secret generated for this role set. Accepted values: <code class="docutils literal notranslate"><span class="pre">access_token</span></code>, <code class="docutils literal notranslate"><span class="pre">service_account_key</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">access_token</span></code>.</p></li>
<li><p><strong>service_account_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email of the service account created by Vault for this Roleset</p></li>
<li><p><strong>token_scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of OAuth scopes to assign to <code class="docutils literal notranslate"><span class="pre">access_token</span></code> secrets generated under this role set (<code class="docutils literal notranslate"><span class="pre">access_token</span></code> role sets only).</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bindings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Resource or resource path for which IAM policy information will be bound. The resource path may be specified in a few different <a class="reference external" href="https://www.vaultproject.io/docs/secrets/gcp/index.html#roleset-bindings">formats</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">roles</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of <a class="reference external" href="https://cloud.google.com/iam/docs/understanding-roles">GCP IAM roles</a> for the resource.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.gcp.SecretRoleset.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.gcp.SecretRoleset.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.gcp.SecretRoleset.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.gcp.SecretRoleset.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
