---
title: Module alicloud
title_tag: Module alicloud | Package pulumi_vault | Python SDK
linktitle: alicloud
notitle: true
---

<div class="section" id="alicloud">
<h1>alicloud<a class="headerlink" href="#alicloud" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-vault/issues">pulumi/pulumi-vault repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-vault/issues">terraform-providers/terraform-provider-vault repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_vault.alicloud"></span><dl class="class">
<dt id="pulumi_vault.alicloud.AuthBackendRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_vault.alicloud.</code><code class="sig-name descname">AuthBackendRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.alicloud.AuthBackendRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AuthBackendRole resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: The role’s arn.
:param pulumi.Input[str] backend: Auth backend.
:param pulumi.Input[str] role: Name of the role. Must correspond with the name of the role reflected in the arn.
:param pulumi.Input[list] token_bound_cidrs: Specifies the blocks of IP addresses which are allowed to use the generated token
:param pulumi.Input[float] token_explicit_max_ttl: Generated Token’s Explicit Maximum TTL in seconds
:param pulumi.Input[float] token_max_ttl: The maximum lifetime of the generated token
:param pulumi.Input[bool] token_no_default_policy: If true, the ‘default’ policy will not automatically be added to generated tokens
:param pulumi.Input[float] token_num_uses: The maximum number of times a token may be used, a value of zero means unlimited
:param pulumi.Input[float] token_period: Generated Token’s Period
:param pulumi.Input[list] token_policies: Generated Token’s Policies
:param pulumi.Input[float] token_ttl: The initial ttl of the token to generate in seconds
:param pulumi.Input[str] token_type: The type of token to generate, service or batch</p>
<dl class="attribute">
<dt id="pulumi_vault.alicloud.AuthBackendRole.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.alicloud.AuthBackendRole.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The role’s arn.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.alicloud.AuthBackendRole.backend">
<code class="sig-name descname">backend</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.alicloud.AuthBackendRole.backend" title="Permalink to this definition">¶</a></dt>
<dd><p>Auth backend.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.alicloud.AuthBackendRole.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.alicloud.AuthBackendRole.role" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the role. Must correspond with the name of the role reflected in the arn.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.alicloud.AuthBackendRole.token_bound_cidrs">
<code class="sig-name descname">token_bound_cidrs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.alicloud.AuthBackendRole.token_bound_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the blocks of IP addresses which are allowed to use the generated token</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.alicloud.AuthBackendRole.token_explicit_max_ttl">
<code class="sig-name descname">token_explicit_max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.alicloud.AuthBackendRole.token_explicit_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>Generated Token’s Explicit Maximum TTL in seconds</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.alicloud.AuthBackendRole.token_max_ttl">
<code class="sig-name descname">token_max_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.alicloud.AuthBackendRole.token_max_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum lifetime of the generated token</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.alicloud.AuthBackendRole.token_no_default_policy">
<code class="sig-name descname">token_no_default_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.alicloud.AuthBackendRole.token_no_default_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the ‘default’ policy will not automatically be added to generated tokens</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.alicloud.AuthBackendRole.token_num_uses">
<code class="sig-name descname">token_num_uses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.alicloud.AuthBackendRole.token_num_uses" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of times a token may be used, a value of zero means unlimited</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.alicloud.AuthBackendRole.token_period">
<code class="sig-name descname">token_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.alicloud.AuthBackendRole.token_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Generated Token’s Period</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.alicloud.AuthBackendRole.token_policies">
<code class="sig-name descname">token_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.alicloud.AuthBackendRole.token_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Generated Token’s Policies</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.alicloud.AuthBackendRole.token_ttl">
<code class="sig-name descname">token_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.alicloud.AuthBackendRole.token_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The initial ttl of the token to generate in seconds</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_vault.alicloud.AuthBackendRole.token_type">
<code class="sig-name descname">token_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_vault.alicloud.AuthBackendRole.token_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of token to generate, service or batch</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_vault.alicloud.AuthBackendRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">backend=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">token_bound_cidrs=None</em>, <em class="sig-param">token_explicit_max_ttl=None</em>, <em class="sig-param">token_max_ttl=None</em>, <em class="sig-param">token_no_default_policy=None</em>, <em class="sig-param">token_num_uses=None</em>, <em class="sig-param">token_period=None</em>, <em class="sig-param">token_policies=None</em>, <em class="sig-param">token_ttl=None</em>, <em class="sig-param">token_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.alicloud.AuthBackendRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AuthBackendRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role’s arn.</p></li>
<li><p><strong>backend</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Auth backend.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the role. Must correspond with the name of the role reflected in the arn.</p></li>
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

<dl class="method">
<dt id="pulumi_vault.alicloud.AuthBackendRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.alicloud.AuthBackendRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_vault.alicloud.AuthBackendRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_vault.alicloud.AuthBackendRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
