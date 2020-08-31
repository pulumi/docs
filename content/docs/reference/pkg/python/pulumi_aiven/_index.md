---
title: Package pulumi_aiven
title_tag: Package pulumi_aiven | Python SDK
linktitle: pulumi_aiven
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "aiven" >}}

<div class="section" id="module-pulumi_aiven">
<span id="pulumi-aiven"></span><h1>Pulumi Aiven<a class="headerlink" href="#module-pulumi_aiven" title="Permalink to this headline">¶</a></h1>
<dl class="py class">
<dt id="pulumi_aiven.Account">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">Account</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Account" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">account1</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">Account</span><span class="p">(</span><span class="s2">&quot;account1&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of creation</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account name</p></li>
<li><p><strong>owner_team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Owner team id</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tenant id</p></li>
<li><p><strong>update_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of last update</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_aiven.Account.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.account.Account<a class="headerlink" href="#pulumi_aiven.Account.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Account resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account id</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of creation</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account name</p></li>
<li><p><strong>owner_team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Owner team id</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tenant id</p></li>
<li><p><strong>update_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of last update</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Account.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_aiven.Account.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account id</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Account.create_time">
<em class="property">property </em><code class="sig-name descname">create_time</code><a class="headerlink" href="#pulumi_aiven.Account.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of creation</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Account.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_aiven.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Account name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Account.owner_team_id">
<em class="property">property </em><code class="sig-name descname">owner_team_id</code><a class="headerlink" href="#pulumi_aiven.Account.owner_team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Owner team id</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Account.tenant_id">
<em class="property">property </em><code class="sig-name descname">tenant_id</code><a class="headerlink" href="#pulumi_aiven.Account.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Tenant id</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Account.update_time">
<em class="property">property </em><code class="sig-name descname">update_time</code><a class="headerlink" href="#pulumi_aiven.Account.update_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of last update</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Account.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Account.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.AccountAuthentication">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AccountAuthentication</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authentication_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_acs_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_certificate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_entity_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_idp_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_metadata_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountAuthentication" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AccountAuthentication resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] account_id: Account id
:param pulumi.Input[str] authentication_id: Account authentication id
:param pulumi.Input[str] create_time: Time of creation
:param pulumi.Input[bool] enabled: Status of account authentication method
:param pulumi.Input[str] name: Account team name
:param pulumi.Input[str] saml_acs_url: SAML Assertion Consumer Service URL
:param pulumi.Input[str] saml_certificate: SAML Certificate
:param pulumi.Input[str] saml_entity_id: SAML Entity id
:param pulumi.Input[str] saml_idp_url: SAML Idp URL
:param pulumi.Input[str] saml_metadata_url: SAML Metadata URL
:param pulumi.Input[str] type: Account authentication id
:param pulumi.Input[str] update_time: Time of last update</p>
<dl class="py method">
<dt id="pulumi_aiven.AccountAuthentication.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authentication_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_acs_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_certificate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_entity_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_idp_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_metadata_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.account_authentication.AccountAuthentication<a class="headerlink" href="#pulumi_aiven.AccountAuthentication.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountAuthentication resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account id</p></li>
<li><p><strong>authentication_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account authentication id</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of creation</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Status of account authentication method</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team name</p></li>
<li><p><strong>saml_acs_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SAML Assertion Consumer Service URL</p></li>
<li><p><strong>saml_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SAML Certificate</p></li>
<li><p><strong>saml_entity_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SAML Entity id</p></li>
<li><p><strong>saml_idp_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SAML Idp URL</p></li>
<li><p><strong>saml_metadata_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SAML Metadata URL</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account authentication id</p></li>
<li><p><strong>update_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of last update</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountAuthentication.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_aiven.AccountAuthentication.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account id</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountAuthentication.authentication_id">
<em class="property">property </em><code class="sig-name descname">authentication_id</code><a class="headerlink" href="#pulumi_aiven.AccountAuthentication.authentication_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account authentication id</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountAuthentication.create_time">
<em class="property">property </em><code class="sig-name descname">create_time</code><a class="headerlink" href="#pulumi_aiven.AccountAuthentication.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of creation</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountAuthentication.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_aiven.AccountAuthentication.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of account authentication method</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountAuthentication.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_aiven.AccountAuthentication.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Account team name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountAuthentication.saml_acs_url">
<em class="property">property </em><code class="sig-name descname">saml_acs_url</code><a class="headerlink" href="#pulumi_aiven.AccountAuthentication.saml_acs_url" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML Assertion Consumer Service URL</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountAuthentication.saml_certificate">
<em class="property">property </em><code class="sig-name descname">saml_certificate</code><a class="headerlink" href="#pulumi_aiven.AccountAuthentication.saml_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML Certificate</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountAuthentication.saml_entity_id">
<em class="property">property </em><code class="sig-name descname">saml_entity_id</code><a class="headerlink" href="#pulumi_aiven.AccountAuthentication.saml_entity_id" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML Entity id</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountAuthentication.saml_idp_url">
<em class="property">property </em><code class="sig-name descname">saml_idp_url</code><a class="headerlink" href="#pulumi_aiven.AccountAuthentication.saml_idp_url" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML Idp URL</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountAuthentication.saml_metadata_url">
<em class="property">property </em><code class="sig-name descname">saml_metadata_url</code><a class="headerlink" href="#pulumi_aiven.AccountAuthentication.saml_metadata_url" title="Permalink to this definition">¶</a></dt>
<dd><p>SAML Metadata URL</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountAuthentication.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_aiven.AccountAuthentication.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Account authentication id</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountAuthentication.update_time">
<em class="property">property </em><code class="sig-name descname">update_time</code><a class="headerlink" href="#pulumi_aiven.AccountAuthentication.update_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of last update</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountAuthentication.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountAuthentication.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.AccountAuthentication.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountAuthentication.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.AccountTeam">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AccountTeam</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeam" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">account_team1</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">AccountTeam</span><span class="p">(</span><span class="s2">&quot;accountTeam1&quot;</span><span class="p">,</span> <span class="n">account_id</span><span class="o">=</span><span class="n">aiven_account</span><span class="p">[</span><span class="s2">&quot;team&quot;</span><span class="p">][</span><span class="s2">&quot;account_id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account id</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of creation</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team name</p></li>
<li><p><strong>update_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of last update</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_aiven.AccountTeam.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.account_team.AccountTeam<a class="headerlink" href="#pulumi_aiven.AccountTeam.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountTeam resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account id</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of creation</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team name</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team id</p></li>
<li><p><strong>update_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of last update</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountTeam.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_aiven.AccountTeam.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account id</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountTeam.create_time">
<em class="property">property </em><code class="sig-name descname">create_time</code><a class="headerlink" href="#pulumi_aiven.AccountTeam.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of creation</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountTeam.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_aiven.AccountTeam.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Account team name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountTeam.team_id">
<em class="property">property </em><code class="sig-name descname">team_id</code><a class="headerlink" href="#pulumi_aiven.AccountTeam.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account team id</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountTeam.update_time">
<em class="property">property </em><code class="sig-name descname">update_time</code><a class="headerlink" href="#pulumi_aiven.AccountTeam.update_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of last update</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountTeam.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeam.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.AccountTeam.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeam.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.AccountTeamMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AccountTeamMember</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accepted</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">invited_by_user_email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeamMember" title="Permalink to this definition">¶</a></dt>
<dd><p>During the creation of <code class="docutils literal notranslate"><span class="pre">AccountTeamMember</span></code> resource, an email invitation will be sent
to a user using <code class="docutils literal notranslate"><span class="pre">user_email</span></code> address. If the user accepts an invitation, he or she will become a member of the account team.
The deletion of <code class="docutils literal notranslate"><span class="pre">AccountTeamMember</span></code> will not only delete invitation if one was sent but not yet accepted by the
user, and it will also eliminate an account team member if one has accepted an invitation previously.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">AccountTeamMember</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="n">aiven_account</span><span class="p">[</span><span class="s2">&quot;developers&quot;</span><span class="p">][</span><span class="s2">&quot;account_id&quot;</span><span class="p">],</span>
    <span class="n">team_id</span><span class="o">=</span><span class="n">aiven_account</span><span class="p">[</span><span class="s2">&quot;developers&quot;</span><span class="p">][</span><span class="s2">&quot;account_id&quot;</span><span class="p">],</span>
    <span class="n">user_email</span><span class="o">=</span><span class="s2">&quot;user+1@example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accepted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Team member invitation status</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account id</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of creation</p></li>
<li><p><strong>invited_by_user_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Team invited by user email</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team id</p></li>
<li><p><strong>user_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Team invite user email</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_aiven.AccountTeamMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accepted</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">invited_by_user_email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.account_team_member.AccountTeamMember<a class="headerlink" href="#pulumi_aiven.AccountTeamMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountTeamMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accepted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Team member invitation status</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account id</p></li>
<li><p><strong>create_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of creation</p></li>
<li><p><strong>invited_by_user_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Team invited by user email</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team id</p></li>
<li><p><strong>user_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Team invite user email</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountTeamMember.accepted">
<em class="property">property </em><code class="sig-name descname">accepted</code><a class="headerlink" href="#pulumi_aiven.AccountTeamMember.accepted" title="Permalink to this definition">¶</a></dt>
<dd><p>Team member invitation status</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountTeamMember.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_aiven.AccountTeamMember.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account id</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountTeamMember.create_time">
<em class="property">property </em><code class="sig-name descname">create_time</code><a class="headerlink" href="#pulumi_aiven.AccountTeamMember.create_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of creation</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountTeamMember.invited_by_user_email">
<em class="property">property </em><code class="sig-name descname">invited_by_user_email</code><a class="headerlink" href="#pulumi_aiven.AccountTeamMember.invited_by_user_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Team invited by user email</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountTeamMember.team_id">
<em class="property">property </em><code class="sig-name descname">team_id</code><a class="headerlink" href="#pulumi_aiven.AccountTeamMember.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account team id</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountTeamMember.user_email">
<em class="property">property </em><code class="sig-name descname">user_email</code><a class="headerlink" href="#pulumi_aiven.AccountTeamMember.user_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Team invite user email</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountTeamMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeamMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.AccountTeamMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeamMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.AccountTeamProject">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AccountTeamProject</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeamProject" title="Permalink to this definition">¶</a></dt>
<dd><p>The account team project is intended to link and existing project to the existing account team. It is important to note
that the project should have an <code class="docutils literal notranslate"><span class="pre">account_id</span></code> property set and equal to account team you are trying to link this project.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">project1</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project1&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="n">aiven_account_team</span><span class="p">[</span><span class="s2">&quot;developers&quot;</span><span class="p">][</span><span class="s2">&quot;account_id&quot;</span><span class="p">],</span>
    <span class="n">project</span><span class="o">=</span><span class="s2">&quot;project-1&quot;</span><span class="p">)</span>
<span class="n">account_team_project1</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">AccountTeamProject</span><span class="p">(</span><span class="s2">&quot;accountTeamProject1&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="n">aiven_account_team</span><span class="p">[</span><span class="s2">&quot;developers&quot;</span><span class="p">][</span><span class="s2">&quot;account_id&quot;</span><span class="p">],</span>
    <span class="n">project_name</span><span class="o">=</span><span class="n">project1</span><span class="o">.</span><span class="n">project</span><span class="p">,</span>
    <span class="n">team_id</span><span class="o">=</span><span class="n">aiven_account_team</span><span class="p">[</span><span class="s2">&quot;developers&quot;</span><span class="p">][</span><span class="s2">&quot;team_id&quot;</span><span class="p">],</span>
    <span class="n">team_type</span><span class="o">=</span><span class="s2">&quot;admin&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account id</p></li>
<li><p><strong>project_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team project name</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team id</p></li>
<li><p><strong>team_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team project type, can one of the following values: admin, developer, operator and read_only</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_aiven.AccountTeamProject.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.account_team_project.AccountTeamProject<a class="headerlink" href="#pulumi_aiven.AccountTeamProject.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AccountTeamProject resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account id</p></li>
<li><p><strong>project_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team project name</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team id</p></li>
<li><p><strong>team_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account team project type, can one of the following values: admin, developer, operator and read_only</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountTeamProject.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_aiven.AccountTeamProject.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account id</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountTeamProject.project_name">
<em class="property">property </em><code class="sig-name descname">project_name</code><a class="headerlink" href="#pulumi_aiven.AccountTeamProject.project_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Account team project name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountTeamProject.team_id">
<em class="property">property </em><code class="sig-name descname">team_id</code><a class="headerlink" href="#pulumi_aiven.AccountTeamProject.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account team id</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountTeamProject.team_type">
<em class="property">property </em><code class="sig-name descname">team_type</code><a class="headerlink" href="#pulumi_aiven.AccountTeamProject.team_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Account team project type, can one of the following values: admin, developer, operator and read_only</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.AccountTeamProject.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeamProject.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.AccountTeamProject.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AccountTeamProject.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.AwaitableGetAccountAuthenticationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetAccountAuthenticationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authentication_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_acs_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_entity_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_idp_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_metadata_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_time</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetAccountAuthenticationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_time</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetAccountTeamMemberResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetAccountTeamMemberResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">accepted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">invited_by_user_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_email</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetAccountTeamMemberResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetAccountTeamProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetAccountTeamProjectResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetAccountTeamProjectResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetAccountTeamResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetAccountTeamResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_time</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetAccountTeamResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetCassandaResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetCassandaResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cassandra</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cassandra_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetCassandaResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetConnectionPoolResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetConnectionPoolResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">connection_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetConnectionPoolResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetDatabaseResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetDatabaseResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lc_collate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lc_ctype</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetDatabaseResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetElasticSearchAclResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetElasticSearchAclResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">acls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extended_acl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetElasticSearchAclResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetElasticSearchResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetElasticSearchResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetElasticSearchResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetGrafanaResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetGrafanaResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetGrafanaResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetInfluxDbResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetInfluxDbResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetInfluxDbResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetKafkaAclResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetKafkaAclResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permission</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topic</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetKafkaAclResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetKafkaConnectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetKafkaConnectResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetKafkaConnectResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetKafkaConnectorResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetKafkaConnectorResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connector_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_author</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_class</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_doc_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_title</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tasks</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetKafkaConnectorResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetKafkaMirrorMakerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetKafkaMirrorMakerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetKafkaMirrorMakerResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetKafkaResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetKafkaResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_acl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetKafkaResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetKafkaSchemaConfigurationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetKafkaSchemaConfigurationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetKafkaSchemaConfigurationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetKafkaSchemaResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetKafkaSchemaResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetKafkaSchemaResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetKafkaTopicResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetKafkaTopicResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cleanup_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_in_sync_replicas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partitions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_bytes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_hours</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topic_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetKafkaTopicResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetMirrorMakerReplicationFlowResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetMirrorMakerReplicationFlowResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_cluster</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_cluster</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topics_blacklists</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetMirrorMakerReplicationFlowResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetMySqlResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetMySqlResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetMySqlResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetPgResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetPgResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetPgResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetProjectResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_emails</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">card_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">copy_from_project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">technical_emails</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetProjectUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetProjectUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">accepted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetProjectUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetProjectVpcResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetProjectVpcResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetProjectVpcResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetRedisResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetRedisResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetRedisResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetServiceComponentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetServiceComponentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">component</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_authentication_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usage</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetServiceComponentResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetServiceIntegrationEndpointResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetServiceIntegrationEndpointResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datadog_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_elasticsearch_logs_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prometheus_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rsyslog_user_config</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetServiceIntegrationEndpointResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetServiceIntegrationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetServiceIntegrationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">destination_endpoint_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mirrormaker_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_endpoint_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_service_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetServiceIntegrationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cassandra</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cassandra_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetServiceUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetServiceUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetServiceUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetTransitGatewayVpcAttachmentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetTransitGatewayVpcAttachmentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_cloud_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_vpc</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peering_connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_peer_network_cidrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetTransitGatewayVpcAttachmentResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.AwaitableGetVpcPeeringConnectionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">AwaitableGetVpcPeeringConnectionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_azure_app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_azure_tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_cloud_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_resource_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_vpc</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peering_connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.AwaitableGetVpcPeeringConnectionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.Cassandra">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">Cassandra</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cassandra</span><span class="p">:</span> <span class="n">Union[CassandraCassandraArgs, Mapping[str, Any], Awaitable[Union[CassandraCassandraArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cassandra_user_config</span><span class="p">:</span> <span class="n">Union[CassandraCassandraUserConfigArgs, Mapping[str, Any], Awaitable[Union[CassandraCassandraUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[CassandraServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[CassandraServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[CassandraServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[CassandraServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Cassandra" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Cassandra resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[pulumi.InputType[‘CassandraCassandraArgs’]] cassandra: Cassandra server provided values
:param pulumi.Input[pulumi.InputType[‘CassandraCassandraUserConfigArgs’]] cassandra_user_config: Cassandra user configurable settings
:param pulumi.Input[str] cloud_name: Cloud the service runs in
:param pulumi.Input[str] maintenance_window_dow: Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.
:param pulumi.Input[str] maintenance_window_time: Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.
:param pulumi.Input[str] plan: Subscription plan
:param pulumi.Input[str] project: Target project
:param pulumi.Input[str] project_vpc_id: Identifier of the VPC the service should be in, if any
:param pulumi.Input[List[pulumi.Input[pulumi.InputType[‘CassandraServiceIntegrationArgs’]]]] service_integrations: Service integrations to specify when creating a service. Not applied after initial service creation
:param pulumi.Input[str] service_name: Service name
:param pulumi.Input[bool] termination_protection: Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
<dl class="py method">
<dt id="pulumi_aiven.Cassandra.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cassandra</span><span class="p">:</span> <span class="n">Union[CassandraCassandraArgs, Mapping[str, Any], Awaitable[Union[CassandraCassandraArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cassandra_user_config</span><span class="p">:</span> <span class="n">Union[CassandraCassandraUserConfigArgs, Mapping[str, Any], Awaitable[Union[CassandraCassandraUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Union[List[Union[CassandraComponentArgs, Mapping[str, Any], Awaitable[Union[CassandraComponentArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[CassandraComponentArgs, Mapping[str, Any], Awaitable[Union[CassandraComponentArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[CassandraServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[CassandraServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[CassandraServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[CassandraServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.cassandra.Cassandra<a class="headerlink" href="#pulumi_aiven.Cassandra.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cassandra resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cassandra</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'CassandraCassandraArgs'</em><em>]</em><em>]</em>) – Cassandra server provided values</p></li>
<li><p><strong>cassandra_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'CassandraCassandraUserConfigArgs'</em><em>]</em><em>]</em>) – Cassandra user configurable settings</p></li>
<li><p><strong>cloud_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud the service runs in</p></li>
<li><p><strong>components</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'CassandraComponentArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service component information objects</p></li>
<li><p><strong>maintenance_window_dow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p></li>
<li><p><strong>maintenance_window_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subscription plan</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target project</p></li>
<li><p><strong>project_vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the VPC the service should be in, if any</p></li>
<li><p><strong>service_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service hostname</p></li>
<li><p><strong>service_integrations</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'CassandraServiceIntegrationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service integrations to specify when creating a service. Not applied after initial service creation</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service name</p></li>
<li><p><strong>service_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password used for connecting to the service, if applicable</p></li>
<li><p><strong>service_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Service port</p></li>
<li><p><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Aiven internal service type code</p></li>
<li><p><strong>service_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p></li>
<li><p><strong>service_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username used for connecting to the service, if applicable</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service state</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Prevent service from being deleted. It is recommended to have this enabled for all services.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.cassandra">
<em class="property">property </em><code class="sig-name descname">cassandra</code><a class="headerlink" href="#pulumi_aiven.Cassandra.cassandra" title="Permalink to this definition">¶</a></dt>
<dd><p>Cassandra server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.cassandra_user_config">
<em class="property">property </em><code class="sig-name descname">cassandra_user_config</code><a class="headerlink" href="#pulumi_aiven.Cassandra.cassandra_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Cassandra user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.cloud_name">
<em class="property">property </em><code class="sig-name descname">cloud_name</code><a class="headerlink" href="#pulumi_aiven.Cassandra.cloud_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud the service runs in</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.components">
<em class="property">property </em><code class="sig-name descname">components</code><a class="headerlink" href="#pulumi_aiven.Cassandra.components" title="Permalink to this definition">¶</a></dt>
<dd><p>Service component information objects</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.maintenance_window_dow">
<em class="property">property </em><code class="sig-name descname">maintenance_window_dow</code><a class="headerlink" href="#pulumi_aiven.Cassandra.maintenance_window_dow" title="Permalink to this definition">¶</a></dt>
<dd><p>Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.maintenance_window_time">
<em class="property">property </em><code class="sig-name descname">maintenance_window_time</code><a class="headerlink" href="#pulumi_aiven.Cassandra.maintenance_window_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.plan">
<em class="property">property </em><code class="sig-name descname">plan</code><a class="headerlink" href="#pulumi_aiven.Cassandra.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Subscription plan</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.Cassandra.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Target project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.project_vpc_id">
<em class="property">property </em><code class="sig-name descname">project_vpc_id</code><a class="headerlink" href="#pulumi_aiven.Cassandra.project_vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the VPC the service should be in, if any</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.service_host">
<em class="property">property </em><code class="sig-name descname">service_host</code><a class="headerlink" href="#pulumi_aiven.Cassandra.service_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Service hostname</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.service_integrations">
<em class="property">property </em><code class="sig-name descname">service_integrations</code><a class="headerlink" href="#pulumi_aiven.Cassandra.service_integrations" title="Permalink to this definition">¶</a></dt>
<dd><p>Service integrations to specify when creating a service. Not applied after initial service creation</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.Cassandra.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.service_password">
<em class="property">property </em><code class="sig-name descname">service_password</code><a class="headerlink" href="#pulumi_aiven.Cassandra.service_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.service_port">
<em class="property">property </em><code class="sig-name descname">service_port</code><a class="headerlink" href="#pulumi_aiven.Cassandra.service_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Service port</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.service_type">
<em class="property">property </em><code class="sig-name descname">service_type</code><a class="headerlink" href="#pulumi_aiven.Cassandra.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Aiven internal service type code</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.service_uri">
<em class="property">property </em><code class="sig-name descname">service_uri</code><a class="headerlink" href="#pulumi_aiven.Cassandra.service_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.service_username">
<em class="property">property </em><code class="sig-name descname">service_username</code><a class="headerlink" href="#pulumi_aiven.Cassandra.service_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_aiven.Cassandra.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Service state</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.termination_protection">
<em class="property">property </em><code class="sig-name descname">termination_protection</code><a class="headerlink" href="#pulumi_aiven.Cassandra.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Cassandra.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Cassandra.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Cassandra.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Cassandra.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ConnectionPool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">ConnectionPool</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_size</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ConnectionPool" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">mytestpool</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">ConnectionPool</span><span class="p">(</span><span class="s2">&quot;mytestpool&quot;</span><span class="p">,</span>
    <span class="n">database_name</span><span class="o">=</span><span class="n">aiven_database</span><span class="p">[</span><span class="s2">&quot;mydatabase&quot;</span><span class="p">][</span><span class="s2">&quot;database_name&quot;</span><span class="p">],</span>
    <span class="n">pool_mode</span><span class="o">=</span><span class="s2">&quot;transaction&quot;</span><span class="p">,</span>
    <span class="n">pool_name</span><span class="o">=</span><span class="s2">&quot;mypool&quot;</span><span class="p">,</span>
    <span class="n">pool_size</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">aiven_project</span><span class="p">[</span><span class="s2">&quot;myproject&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">service_name</span><span class="o">=</span><span class="n">aiven_service</span><span class="p">[</span><span class="s2">&quot;myservice&quot;</span><span class="p">][</span><span class="s2">&quot;service_name&quot;</span><span class="p">],</span>
    <span class="n">username</span><span class="o">=</span><span class="n">aiven_service_user</span><span class="p">[</span><span class="s2">&quot;myserviceuser&quot;</span><span class="p">][</span><span class="s2">&quot;username&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the database the pool connects to</p></li>
<li><p><strong>pool_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Mode the pool operates in (session, transaction, statement)</p></li>
<li><p><strong>pool_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the pool</p></li>
<li><p><strong>pool_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of connections the pool may create towards the backend server</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the connection pool to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the connection pool to</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the service user used to connect to the database</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_aiven.ConnectionPool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_uri</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_size</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.connection_pool.ConnectionPool<a class="headerlink" href="#pulumi_aiven.ConnectionPool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ConnectionPool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI for connecting to the pool</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the database the pool connects to</p></li>
<li><p><strong>pool_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Mode the pool operates in (session, transaction, statement)</p></li>
<li><p><strong>pool_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the pool</p></li>
<li><p><strong>pool_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of connections the pool may create towards the backend server</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the connection pool to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the connection pool to</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the service user used to connect to the database</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ConnectionPool.connection_uri">
<em class="property">property </em><code class="sig-name descname">connection_uri</code><a class="headerlink" href="#pulumi_aiven.ConnectionPool.connection_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI for connecting to the pool</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ConnectionPool.database_name">
<em class="property">property </em><code class="sig-name descname">database_name</code><a class="headerlink" href="#pulumi_aiven.ConnectionPool.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the database the pool connects to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ConnectionPool.pool_mode">
<em class="property">property </em><code class="sig-name descname">pool_mode</code><a class="headerlink" href="#pulumi_aiven.ConnectionPool.pool_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Mode the pool operates in (session, transaction, statement)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ConnectionPool.pool_name">
<em class="property">property </em><code class="sig-name descname">pool_name</code><a class="headerlink" href="#pulumi_aiven.ConnectionPool.pool_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the pool</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ConnectionPool.pool_size">
<em class="property">property </em><code class="sig-name descname">pool_size</code><a class="headerlink" href="#pulumi_aiven.ConnectionPool.pool_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of connections the pool may create towards the backend server</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ConnectionPool.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.ConnectionPool.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the connection pool to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ConnectionPool.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.ConnectionPool.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the connection pool to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ConnectionPool.username">
<em class="property">property </em><code class="sig-name descname">username</code><a class="headerlink" href="#pulumi_aiven.ConnectionPool.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the service user used to connect to the database</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ConnectionPool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ConnectionPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ConnectionPool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ConnectionPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Database">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">Database</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lc_collate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lc_ctype</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Database" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">mydatabase</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">Database</span><span class="p">(</span><span class="s2">&quot;mydatabase&quot;</span><span class="p">,</span>
    <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;&lt;DATABASE_NAME&gt;&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">aiven_project</span><span class="p">[</span><span class="s2">&quot;myproject&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">service_name</span><span class="o">=</span><span class="n">aiven_service</span><span class="p">[</span><span class="s2">&quot;myservice&quot;</span><span class="p">][</span><span class="s2">&quot;service_name&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service database name</p></li>
<li><p><strong>lc_collate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default string sort order (LC_COLLATE) of the database. Default value: en_US.UTF-8</p></li>
<li><p><strong>lc_ctype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default character classification (LC_CTYPE) of the database. Default value: en_US.UTF-8</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the database to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the database to</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – It is a Terraform client-side deletion protections, which prevents the database from being deleted by Terraform. It is
recommended to enable this for any production databases containing critical data.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_aiven.Database.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lc_collate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lc_ctype</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.database.Database<a class="headerlink" href="#pulumi_aiven.Database.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Database resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service database name</p></li>
<li><p><strong>lc_collate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default string sort order (LC_COLLATE) of the database. Default value: en_US.UTF-8</p></li>
<li><p><strong>lc_ctype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default character classification (LC_CTYPE) of the database. Default value: en_US.UTF-8</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the database to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the database to</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – It is a Terraform client-side deletion protections, which prevents the database from being deleted by Terraform. It is
recommended to enable this for any production databases containing critical data.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Database.database_name">
<em class="property">property </em><code class="sig-name descname">database_name</code><a class="headerlink" href="#pulumi_aiven.Database.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service database name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Database.lc_collate">
<em class="property">property </em><code class="sig-name descname">lc_collate</code><a class="headerlink" href="#pulumi_aiven.Database.lc_collate" title="Permalink to this definition">¶</a></dt>
<dd><p>Default string sort order (LC_COLLATE) of the database. Default value: en_US.UTF-8</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Database.lc_ctype">
<em class="property">property </em><code class="sig-name descname">lc_ctype</code><a class="headerlink" href="#pulumi_aiven.Database.lc_ctype" title="Permalink to this definition">¶</a></dt>
<dd><p>Default character classification (LC_CTYPE) of the database. Default value: en_US.UTF-8</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Database.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.Database.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the database to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Database.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.Database.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the database to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Database.termination_protection">
<em class="property">property </em><code class="sig-name descname">termination_protection</code><a class="headerlink" href="#pulumi_aiven.Database.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>It is a Terraform client-side deletion protections, which prevents the database from being deleted by Terraform. It is
recommended to enable this for any production databases containing critical data.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Database.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Database.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ElasticSearch">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">ElasticSearch</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch</span><span class="p">:</span> <span class="n">Union[ElasticSearchElasticsearchArgs, Mapping[str, Any], Awaitable[Union[ElasticSearchElasticsearchArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch_user_config</span><span class="p">:</span> <span class="n">Union[ElasticSearchElasticsearchUserConfigArgs, Mapping[str, Any], Awaitable[Union[ElasticSearchElasticsearchUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[ElasticSearchServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[ElasticSearchServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ElasticSearchServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[ElasticSearchServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ElasticSearch" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ElasticSearch resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] cloud_name: Cloud the service runs in
:param pulumi.Input[pulumi.InputType[‘ElasticSearchElasticsearchArgs’]] elasticsearch: Elasticsearch server provided values
:param pulumi.Input[pulumi.InputType[‘ElasticSearchElasticsearchUserConfigArgs’]] elasticsearch_user_config: Elasticsearch user configurable settings
:param pulumi.Input[str] maintenance_window_dow: Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.
:param pulumi.Input[str] maintenance_window_time: Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.
:param pulumi.Input[str] plan: Subscription plan
:param pulumi.Input[str] project: Target project
:param pulumi.Input[str] project_vpc_id: Identifier of the VPC the service should be in, if any
:param pulumi.Input[List[pulumi.Input[pulumi.InputType[‘ElasticSearchServiceIntegrationArgs’]]]] service_integrations: Service integrations to specify when creating a service. Not applied after initial service creation
:param pulumi.Input[str] service_name: Service name
:param pulumi.Input[bool] termination_protection: Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Union[List[Union[ElasticSearchComponentArgs, Mapping[str, Any], Awaitable[Union[ElasticSearchComponentArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ElasticSearchComponentArgs, Mapping[str, Any], Awaitable[Union[ElasticSearchComponentArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch</span><span class="p">:</span> <span class="n">Union[ElasticSearchElasticsearchArgs, Mapping[str, Any], Awaitable[Union[ElasticSearchElasticsearchArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch_user_config</span><span class="p">:</span> <span class="n">Union[ElasticSearchElasticsearchUserConfigArgs, Mapping[str, Any], Awaitable[Union[ElasticSearchElasticsearchUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[ElasticSearchServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[ElasticSearchServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ElasticSearchServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[ElasticSearchServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.elastic_search.ElasticSearch<a class="headerlink" href="#pulumi_aiven.ElasticSearch.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ElasticSearch resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud the service runs in</p></li>
<li><p><strong>components</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ElasticSearchComponentArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service component information objects</p></li>
<li><p><strong>elasticsearch</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ElasticSearchElasticsearchArgs'</em><em>]</em><em>]</em>) – Elasticsearch server provided values</p></li>
<li><p><strong>elasticsearch_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ElasticSearchElasticsearchUserConfigArgs'</em><em>]</em><em>]</em>) – Elasticsearch user configurable settings</p></li>
<li><p><strong>maintenance_window_dow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p></li>
<li><p><strong>maintenance_window_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subscription plan</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target project</p></li>
<li><p><strong>project_vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the VPC the service should be in, if any</p></li>
<li><p><strong>service_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service hostname</p></li>
<li><p><strong>service_integrations</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ElasticSearchServiceIntegrationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service integrations to specify when creating a service. Not applied after initial service creation</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service name</p></li>
<li><p><strong>service_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password used for connecting to the service, if applicable</p></li>
<li><p><strong>service_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Service port</p></li>
<li><p><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Aiven internal service type code</p></li>
<li><p><strong>service_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p></li>
<li><p><strong>service_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username used for connecting to the service, if applicable</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service state</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Prevent service from being deleted. It is recommended to have this enabled for all services.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.cloud_name">
<em class="property">property </em><code class="sig-name descname">cloud_name</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.cloud_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud the service runs in</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.components">
<em class="property">property </em><code class="sig-name descname">components</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.components" title="Permalink to this definition">¶</a></dt>
<dd><p>Service component information objects</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.elasticsearch">
<em class="property">property </em><code class="sig-name descname">elasticsearch</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.elasticsearch" title="Permalink to this definition">¶</a></dt>
<dd><p>Elasticsearch server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.elasticsearch_user_config">
<em class="property">property </em><code class="sig-name descname">elasticsearch_user_config</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.elasticsearch_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Elasticsearch user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.maintenance_window_dow">
<em class="property">property </em><code class="sig-name descname">maintenance_window_dow</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.maintenance_window_dow" title="Permalink to this definition">¶</a></dt>
<dd><p>Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.maintenance_window_time">
<em class="property">property </em><code class="sig-name descname">maintenance_window_time</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.maintenance_window_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.plan">
<em class="property">property </em><code class="sig-name descname">plan</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Subscription plan</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Target project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.project_vpc_id">
<em class="property">property </em><code class="sig-name descname">project_vpc_id</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.project_vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the VPC the service should be in, if any</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.service_host">
<em class="property">property </em><code class="sig-name descname">service_host</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.service_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Service hostname</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.service_integrations">
<em class="property">property </em><code class="sig-name descname">service_integrations</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.service_integrations" title="Permalink to this definition">¶</a></dt>
<dd><p>Service integrations to specify when creating a service. Not applied after initial service creation</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.service_password">
<em class="property">property </em><code class="sig-name descname">service_password</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.service_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.service_port">
<em class="property">property </em><code class="sig-name descname">service_port</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.service_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Service port</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.service_type">
<em class="property">property </em><code class="sig-name descname">service_type</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Aiven internal service type code</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.service_uri">
<em class="property">property </em><code class="sig-name descname">service_uri</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.service_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.service_username">
<em class="property">property </em><code class="sig-name descname">service_username</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.service_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Service state</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.termination_protection">
<em class="property">property </em><code class="sig-name descname">termination_protection</code><a class="headerlink" href="#pulumi_aiven.ElasticSearch.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearch.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ElasticSearch.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ElasticSearch.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ElasticSearch.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ElasticSearchAcl">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">ElasticSearchAcl</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acls</span><span class="p">:</span> <span class="n">Union[List[Union[ElasticSearchAclAclArgs, Mapping[str, Any], Awaitable[Union[ElasticSearchAclAclArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ElasticSearchAclAclArgs, Mapping[str, Any], Awaitable[Union[ElasticSearchAclAclArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extended_acl</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ElasticSearchAcl" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ElasticSearchAcl resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[List[pulumi.Input[pulumi.InputType[‘ElasticSearchAclAclArgs’]]]] acls: List of Elasticsearch ACLs
:param pulumi.Input[bool] enabled: Enable Elasticsearch ACLs. When disabled authenticated service users have unrestricted access
:param pulumi.Input[bool] extended_acl: Index rules can be applied in a limited fashion to the _mget, _msearch and _bulk APIs (and only those) by enabling the</p>
<blockquote>
<div><p>ExtendedAcl option for the service. When it is enabled, users can use these APIs as long as all operations only target
indexes they have been granted access to</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the Elasticsearch ACLs to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the Elasticsearch ACLs to</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_aiven.ElasticSearchAcl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acls</span><span class="p">:</span> <span class="n">Union[List[Union[ElasticSearchAclAclArgs, Mapping[str, Any], Awaitable[Union[ElasticSearchAclAclArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ElasticSearchAclAclArgs, Mapping[str, Any], Awaitable[Union[ElasticSearchAclAclArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extended_acl</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.elastic_search_acl.ElasticSearchAcl<a class="headerlink" href="#pulumi_aiven.ElasticSearchAcl.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ElasticSearchAcl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acls</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ElasticSearchAclAclArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of Elasticsearch ACLs</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable Elasticsearch ACLs. When disabled authenticated service users have unrestricted access</p></li>
<li><p><strong>extended_acl</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Index rules can be applied in a limited fashion to the _mget, _msearch and _bulk APIs (and only those) by enabling the
ExtendedAcl option for the service. When it is enabled, users can use these APIs as long as all operations only target
indexes they have been granted access to</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the Elasticsearch ACLs to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the Elasticsearch ACLs to</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearchAcl.acls">
<em class="property">property </em><code class="sig-name descname">acls</code><a class="headerlink" href="#pulumi_aiven.ElasticSearchAcl.acls" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Elasticsearch ACLs</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearchAcl.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_aiven.ElasticSearchAcl.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable Elasticsearch ACLs. When disabled authenticated service users have unrestricted access</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearchAcl.extended_acl">
<em class="property">property </em><code class="sig-name descname">extended_acl</code><a class="headerlink" href="#pulumi_aiven.ElasticSearchAcl.extended_acl" title="Permalink to this definition">¶</a></dt>
<dd><p>Index rules can be applied in a limited fashion to the _mget, _msearch and _bulk APIs (and only those) by enabling the
ExtendedAcl option for the service. When it is enabled, users can use these APIs as long as all operations only target
indexes they have been granted access to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearchAcl.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.ElasticSearchAcl.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the Elasticsearch ACLs to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearchAcl.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.ElasticSearchAcl.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the Elasticsearch ACLs to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ElasticSearchAcl.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ElasticSearchAcl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ElasticSearchAcl.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ElasticSearchAcl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.GetAccountAuthenticationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetAccountAuthenticationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authentication_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_acs_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_certificate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_entity_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_idp_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_metadata_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_time</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetAccountAuthenticationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccountAuthentication.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetAccountAuthenticationResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetAccountAuthenticationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_time</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetAccountResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetAccountTeamMemberResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetAccountTeamMemberResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">accepted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">invited_by_user_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_email</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetAccountTeamMemberResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccountTeamMember.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetAccountTeamMemberResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetAccountTeamMemberResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetAccountTeamProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetAccountTeamProjectResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetAccountTeamProjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccountTeamProject.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetAccountTeamProjectResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetAccountTeamProjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetAccountTeamResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetAccountTeamResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_time</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetAccountTeamResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccountTeam.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetAccountTeamResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetAccountTeamResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetCassandaResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetCassandaResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cassandra</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cassandra_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetCassandaResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCassanda.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetCassandaResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetCassandaResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetConnectionPoolResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetConnectionPoolResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">connection_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetConnectionPoolResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getConnectionPool.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetConnectionPoolResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetConnectionPoolResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetDatabaseResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetDatabaseResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lc_collate</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lc_ctype</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetDatabaseResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDatabase.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetDatabaseResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetDatabaseResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetElasticSearchAclResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetElasticSearchAclResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">acls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extended_acl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetElasticSearchAclResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getElasticSearchAcl.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetElasticSearchAclResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetElasticSearchAclResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetElasticSearchResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetElasticSearchResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetElasticSearchResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getElasticSearch.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetElasticSearchResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetElasticSearchResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetGrafanaResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetGrafanaResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetGrafanaResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGrafana.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetGrafanaResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetGrafanaResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetInfluxDbResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetInfluxDbResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetInfluxDbResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInfluxDb.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetInfluxDbResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetInfluxDbResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetKafkaAclResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetKafkaAclResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permission</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topic</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetKafkaAclResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKafkaAcl.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetKafkaAclResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetKafkaAclResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetKafkaConnectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetKafkaConnectResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetKafkaConnectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKafkaConnect.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetKafkaConnectResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetKafkaConnectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetKafkaConnectorResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetKafkaConnectorResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connector_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_author</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_class</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_doc_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_title</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tasks</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetKafkaConnectorResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKafkaConnector.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetKafkaConnectorResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetKafkaConnectorResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetKafkaMirrorMakerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetKafkaMirrorMakerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetKafkaMirrorMakerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKafkaMirrorMaker.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetKafkaMirrorMakerResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetKafkaMirrorMakerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetKafkaResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetKafkaResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_acl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetKafkaResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKafka.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetKafkaResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetKafkaResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetKafkaSchemaConfigurationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetKafkaSchemaConfigurationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetKafkaSchemaConfigurationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKafkaSchemaConfiguration.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetKafkaSchemaConfigurationResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetKafkaSchemaConfigurationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetKafkaSchemaResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetKafkaSchemaResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetKafkaSchemaResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKafkaSchema.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetKafkaSchemaResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetKafkaSchemaResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetKafkaTopicResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetKafkaTopicResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cleanup_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_in_sync_replicas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partitions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_bytes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_hours</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topic_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetKafkaTopicResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKafkaTopic.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetKafkaTopicResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetKafkaTopicResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetMirrorMakerReplicationFlowResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetMirrorMakerReplicationFlowResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_cluster</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_cluster</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topics_blacklists</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetMirrorMakerReplicationFlowResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getMirrorMakerReplicationFlow.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetMirrorMakerReplicationFlowResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetMirrorMakerReplicationFlowResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetMySqlResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetMySqlResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetMySqlResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getMySql.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetMySqlResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetMySqlResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetPgResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetPgResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetPgResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPg.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetPgResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetPgResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetProjectResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_emails</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">card_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">copy_from_project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">technical_emails</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProject.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetProjectResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetProjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetProjectUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetProjectUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">accepted</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetProjectUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProjectUser.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetProjectUserResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetProjectUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetProjectVpcResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetProjectVpcResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetProjectVpcResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProjectVpc.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetProjectVpcResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetProjectVpcResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetRedisResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetRedisResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetRedisResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRedis.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetRedisResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetRedisResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetServiceComponentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetServiceComponentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">component</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_authentication_method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usage</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetServiceComponentResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServiceComponent.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetServiceComponentResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetServiceComponentResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetServiceIntegrationEndpointResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetServiceIntegrationEndpointResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datadog_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_elasticsearch_logs_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prometheus_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rsyslog_user_config</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetServiceIntegrationEndpointResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServiceIntegrationEndpoint.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetServiceIntegrationEndpointResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetServiceIntegrationEndpointResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetServiceIntegrationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetServiceIntegrationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">destination_endpoint_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mirrormaker_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_endpoint_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_service_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetServiceIntegrationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServiceIntegration.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetServiceIntegrationResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetServiceIntegrationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cassandra</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cassandra_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis_user_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getService.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetServiceResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetServiceUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetServiceUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetServiceUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServiceUser.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetServiceUserResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetServiceUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetTransitGatewayVpcAttachmentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetTransitGatewayVpcAttachmentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_cloud_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_vpc</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peering_connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_peer_network_cidrs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetTransitGatewayVpcAttachmentResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTransitGatewayVpcAttachment.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetTransitGatewayVpcAttachmentResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetTransitGatewayVpcAttachmentResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.GetVpcPeeringConnectionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">GetVpcPeeringConnectionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_azure_app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_azure_tenant_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_cloud_account</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_resource_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_vpc</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peering_connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.GetVpcPeeringConnectionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVpcPeeringConnection.</p>
<dl class="py method">
<dt id="pulumi_aiven.GetVpcPeeringConnectionResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_aiven.GetVpcPeeringConnectionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aiven.Grafana">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">Grafana</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana</span><span class="p">:</span> <span class="n">Union[GrafanaGrafanaArgs, Mapping[str, Any], Awaitable[Union[GrafanaGrafanaArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana_user_config</span><span class="p">:</span> <span class="n">Union[GrafanaGrafanaUserConfigArgs, Mapping[str, Any], Awaitable[Union[GrafanaGrafanaUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[GrafanaServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[GrafanaServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[GrafanaServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[GrafanaServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Grafana" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Grafana resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] cloud_name: Cloud the service runs in
:param pulumi.Input[pulumi.InputType[‘GrafanaGrafanaArgs’]] grafana: Grafana server provided values
:param pulumi.Input[pulumi.InputType[‘GrafanaGrafanaUserConfigArgs’]] grafana_user_config: Grafana user configurable settings
:param pulumi.Input[str] maintenance_window_dow: Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.
:param pulumi.Input[str] maintenance_window_time: Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.
:param pulumi.Input[str] plan: Subscription plan
:param pulumi.Input[str] project: Target project
:param pulumi.Input[str] project_vpc_id: Identifier of the VPC the service should be in, if any
:param pulumi.Input[List[pulumi.Input[pulumi.InputType[‘GrafanaServiceIntegrationArgs’]]]] service_integrations: Service integrations to specify when creating a service. Not applied after initial service creation
:param pulumi.Input[str] service_name: Service name
:param pulumi.Input[bool] termination_protection: Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
<dl class="py method">
<dt id="pulumi_aiven.Grafana.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Union[List[Union[GrafanaComponentArgs, Mapping[str, Any], Awaitable[Union[GrafanaComponentArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[GrafanaComponentArgs, Mapping[str, Any], Awaitable[Union[GrafanaComponentArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana</span><span class="p">:</span> <span class="n">Union[GrafanaGrafanaArgs, Mapping[str, Any], Awaitable[Union[GrafanaGrafanaArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana_user_config</span><span class="p">:</span> <span class="n">Union[GrafanaGrafanaUserConfigArgs, Mapping[str, Any], Awaitable[Union[GrafanaGrafanaUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[GrafanaServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[GrafanaServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[GrafanaServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[GrafanaServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.grafana.Grafana<a class="headerlink" href="#pulumi_aiven.Grafana.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Grafana resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud the service runs in</p></li>
<li><p><strong>components</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GrafanaComponentArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service component information objects</p></li>
<li><p><strong>grafana</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GrafanaGrafanaArgs'</em><em>]</em><em>]</em>) – Grafana server provided values</p></li>
<li><p><strong>grafana_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GrafanaGrafanaUserConfigArgs'</em><em>]</em><em>]</em>) – Grafana user configurable settings</p></li>
<li><p><strong>maintenance_window_dow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p></li>
<li><p><strong>maintenance_window_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subscription plan</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target project</p></li>
<li><p><strong>project_vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the VPC the service should be in, if any</p></li>
<li><p><strong>service_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service hostname</p></li>
<li><p><strong>service_integrations</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GrafanaServiceIntegrationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service integrations to specify when creating a service. Not applied after initial service creation</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service name</p></li>
<li><p><strong>service_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password used for connecting to the service, if applicable</p></li>
<li><p><strong>service_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Service port</p></li>
<li><p><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Aiven internal service type code</p></li>
<li><p><strong>service_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p></li>
<li><p><strong>service_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username used for connecting to the service, if applicable</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service state</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Prevent service from being deleted. It is recommended to have this enabled for all services.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.cloud_name">
<em class="property">property </em><code class="sig-name descname">cloud_name</code><a class="headerlink" href="#pulumi_aiven.Grafana.cloud_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud the service runs in</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.components">
<em class="property">property </em><code class="sig-name descname">components</code><a class="headerlink" href="#pulumi_aiven.Grafana.components" title="Permalink to this definition">¶</a></dt>
<dd><p>Service component information objects</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.grafana">
<em class="property">property </em><code class="sig-name descname">grafana</code><a class="headerlink" href="#pulumi_aiven.Grafana.grafana" title="Permalink to this definition">¶</a></dt>
<dd><p>Grafana server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.grafana_user_config">
<em class="property">property </em><code class="sig-name descname">grafana_user_config</code><a class="headerlink" href="#pulumi_aiven.Grafana.grafana_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Grafana user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.maintenance_window_dow">
<em class="property">property </em><code class="sig-name descname">maintenance_window_dow</code><a class="headerlink" href="#pulumi_aiven.Grafana.maintenance_window_dow" title="Permalink to this definition">¶</a></dt>
<dd><p>Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.maintenance_window_time">
<em class="property">property </em><code class="sig-name descname">maintenance_window_time</code><a class="headerlink" href="#pulumi_aiven.Grafana.maintenance_window_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.plan">
<em class="property">property </em><code class="sig-name descname">plan</code><a class="headerlink" href="#pulumi_aiven.Grafana.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Subscription plan</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.Grafana.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Target project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.project_vpc_id">
<em class="property">property </em><code class="sig-name descname">project_vpc_id</code><a class="headerlink" href="#pulumi_aiven.Grafana.project_vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the VPC the service should be in, if any</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.service_host">
<em class="property">property </em><code class="sig-name descname">service_host</code><a class="headerlink" href="#pulumi_aiven.Grafana.service_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Service hostname</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.service_integrations">
<em class="property">property </em><code class="sig-name descname">service_integrations</code><a class="headerlink" href="#pulumi_aiven.Grafana.service_integrations" title="Permalink to this definition">¶</a></dt>
<dd><p>Service integrations to specify when creating a service. Not applied after initial service creation</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.Grafana.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.service_password">
<em class="property">property </em><code class="sig-name descname">service_password</code><a class="headerlink" href="#pulumi_aiven.Grafana.service_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.service_port">
<em class="property">property </em><code class="sig-name descname">service_port</code><a class="headerlink" href="#pulumi_aiven.Grafana.service_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Service port</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.service_type">
<em class="property">property </em><code class="sig-name descname">service_type</code><a class="headerlink" href="#pulumi_aiven.Grafana.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Aiven internal service type code</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.service_uri">
<em class="property">property </em><code class="sig-name descname">service_uri</code><a class="headerlink" href="#pulumi_aiven.Grafana.service_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.service_username">
<em class="property">property </em><code class="sig-name descname">service_username</code><a class="headerlink" href="#pulumi_aiven.Grafana.service_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_aiven.Grafana.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Service state</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.termination_protection">
<em class="property">property </em><code class="sig-name descname">termination_protection</code><a class="headerlink" href="#pulumi_aiven.Grafana.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Grafana.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Grafana.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Grafana.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Grafana.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.InfluxDb">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">InfluxDb</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb</span><span class="p">:</span> <span class="n">Union[InfluxDbInfluxdbArgs, Mapping[str, Any], Awaitable[Union[InfluxDbInfluxdbArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb_user_config</span><span class="p">:</span> <span class="n">Union[InfluxDbInfluxdbUserConfigArgs, Mapping[str, Any], Awaitable[Union[InfluxDbInfluxdbUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[InfluxDbServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[InfluxDbServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[InfluxDbServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[InfluxDbServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.InfluxDb" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a InfluxDb resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] cloud_name: Cloud the service runs in
:param pulumi.Input[pulumi.InputType[‘InfluxDbInfluxdbArgs’]] influxdb: InfluxDB server provided values
:param pulumi.Input[pulumi.InputType[‘InfluxDbInfluxdbUserConfigArgs’]] influxdb_user_config: InfluxDB user configurable settings
:param pulumi.Input[str] maintenance_window_dow: Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.
:param pulumi.Input[str] maintenance_window_time: Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.
:param pulumi.Input[str] plan: Subscription plan
:param pulumi.Input[str] project: Target project
:param pulumi.Input[str] project_vpc_id: Identifier of the VPC the service should be in, if any
:param pulumi.Input[List[pulumi.Input[pulumi.InputType[‘InfluxDbServiceIntegrationArgs’]]]] service_integrations: Service integrations to specify when creating a service. Not applied after initial service creation
:param pulumi.Input[str] service_name: Service name
:param pulumi.Input[bool] termination_protection: Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Union[List[Union[InfluxDbComponentArgs, Mapping[str, Any], Awaitable[Union[InfluxDbComponentArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[InfluxDbComponentArgs, Mapping[str, Any], Awaitable[Union[InfluxDbComponentArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb</span><span class="p">:</span> <span class="n">Union[InfluxDbInfluxdbArgs, Mapping[str, Any], Awaitable[Union[InfluxDbInfluxdbArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb_user_config</span><span class="p">:</span> <span class="n">Union[InfluxDbInfluxdbUserConfigArgs, Mapping[str, Any], Awaitable[Union[InfluxDbInfluxdbUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[InfluxDbServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[InfluxDbServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[InfluxDbServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[InfluxDbServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.influx_db.InfluxDb<a class="headerlink" href="#pulumi_aiven.InfluxDb.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InfluxDb resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud the service runs in</p></li>
<li><p><strong>components</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InfluxDbComponentArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service component information objects</p></li>
<li><p><strong>influxdb</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InfluxDbInfluxdbArgs'</em><em>]</em><em>]</em>) – InfluxDB server provided values</p></li>
<li><p><strong>influxdb_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InfluxDbInfluxdbUserConfigArgs'</em><em>]</em><em>]</em>) – InfluxDB user configurable settings</p></li>
<li><p><strong>maintenance_window_dow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p></li>
<li><p><strong>maintenance_window_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subscription plan</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target project</p></li>
<li><p><strong>project_vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the VPC the service should be in, if any</p></li>
<li><p><strong>service_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service hostname</p></li>
<li><p><strong>service_integrations</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'InfluxDbServiceIntegrationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service integrations to specify when creating a service. Not applied after initial service creation</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service name</p></li>
<li><p><strong>service_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password used for connecting to the service, if applicable</p></li>
<li><p><strong>service_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Service port</p></li>
<li><p><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Aiven internal service type code</p></li>
<li><p><strong>service_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p></li>
<li><p><strong>service_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username used for connecting to the service, if applicable</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service state</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Prevent service from being deleted. It is recommended to have this enabled for all services.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.cloud_name">
<em class="property">property </em><code class="sig-name descname">cloud_name</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.cloud_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud the service runs in</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.components">
<em class="property">property </em><code class="sig-name descname">components</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.components" title="Permalink to this definition">¶</a></dt>
<dd><p>Service component information objects</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.influxdb">
<em class="property">property </em><code class="sig-name descname">influxdb</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.influxdb" title="Permalink to this definition">¶</a></dt>
<dd><p>InfluxDB server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.influxdb_user_config">
<em class="property">property </em><code class="sig-name descname">influxdb_user_config</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.influxdb_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>InfluxDB user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.maintenance_window_dow">
<em class="property">property </em><code class="sig-name descname">maintenance_window_dow</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.maintenance_window_dow" title="Permalink to this definition">¶</a></dt>
<dd><p>Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.maintenance_window_time">
<em class="property">property </em><code class="sig-name descname">maintenance_window_time</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.maintenance_window_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.plan">
<em class="property">property </em><code class="sig-name descname">plan</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Subscription plan</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Target project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.project_vpc_id">
<em class="property">property </em><code class="sig-name descname">project_vpc_id</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.project_vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the VPC the service should be in, if any</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.service_host">
<em class="property">property </em><code class="sig-name descname">service_host</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.service_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Service hostname</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.service_integrations">
<em class="property">property </em><code class="sig-name descname">service_integrations</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.service_integrations" title="Permalink to this definition">¶</a></dt>
<dd><p>Service integrations to specify when creating a service. Not applied after initial service creation</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.service_password">
<em class="property">property </em><code class="sig-name descname">service_password</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.service_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.service_port">
<em class="property">property </em><code class="sig-name descname">service_port</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.service_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Service port</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.service_type">
<em class="property">property </em><code class="sig-name descname">service_type</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Aiven internal service type code</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.service_uri">
<em class="property">property </em><code class="sig-name descname">service_uri</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.service_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.service_username">
<em class="property">property </em><code class="sig-name descname">service_username</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.service_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Service state</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.termination_protection">
<em class="property">property </em><code class="sig-name descname">termination_protection</code><a class="headerlink" href="#pulumi_aiven.InfluxDb.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.InfluxDb.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.InfluxDb.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.InfluxDb.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.InfluxDb.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Kafka">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">Kafka</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_acl</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka</span><span class="p">:</span> <span class="n">Union[KafkaKafkaArgs, Mapping[str, Any], Awaitable[Union[KafkaKafkaArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_user_config</span><span class="p">:</span> <span class="n">Union[KafkaKafkaUserConfigArgs, Mapping[str, Any], Awaitable[Union[KafkaKafkaUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[KafkaServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[KafkaServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[KafkaServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[KafkaServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Kafka" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Kafka resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] cloud_name: Cloud the service runs in
:param pulumi.Input[bool] default_acl: Create default wildcard Kafka ACL
:param pulumi.Input[pulumi.InputType[‘KafkaKafkaArgs’]] kafka: Kafka server provided values
:param pulumi.Input[pulumi.InputType[‘KafkaKafkaUserConfigArgs’]] kafka_user_config: Kafka user configurable settings
:param pulumi.Input[str] maintenance_window_dow: Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.
:param pulumi.Input[str] maintenance_window_time: Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.
:param pulumi.Input[str] plan: Subscription plan
:param pulumi.Input[str] project: Target project
:param pulumi.Input[str] project_vpc_id: Identifier of the VPC the service should be in, if any
:param pulumi.Input[List[pulumi.Input[pulumi.InputType[‘KafkaServiceIntegrationArgs’]]]] service_integrations: Service integrations to specify when creating a service. Not applied after initial service creation
:param pulumi.Input[str] service_name: Service name
:param pulumi.Input[bool] termination_protection: Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
<dl class="py method">
<dt id="pulumi_aiven.Kafka.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Union[List[Union[KafkaComponentArgs, Mapping[str, Any], Awaitable[Union[KafkaComponentArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[KafkaComponentArgs, Mapping[str, Any], Awaitable[Union[KafkaComponentArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_acl</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka</span><span class="p">:</span> <span class="n">Union[KafkaKafkaArgs, Mapping[str, Any], Awaitable[Union[KafkaKafkaArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_user_config</span><span class="p">:</span> <span class="n">Union[KafkaKafkaUserConfigArgs, Mapping[str, Any], Awaitable[Union[KafkaKafkaUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[KafkaServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[KafkaServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[KafkaServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[KafkaServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.kafka.Kafka<a class="headerlink" href="#pulumi_aiven.Kafka.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Kafka resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud the service runs in</p></li>
<li><p><strong>components</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'KafkaComponentArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service component information objects</p></li>
<li><p><strong>default_acl</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Create default wildcard Kafka ACL</p></li>
<li><p><strong>kafka</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'KafkaKafkaArgs'</em><em>]</em><em>]</em>) – Kafka server provided values</p></li>
<li><p><strong>kafka_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'KafkaKafkaUserConfigArgs'</em><em>]</em><em>]</em>) – Kafka user configurable settings</p></li>
<li><p><strong>maintenance_window_dow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p></li>
<li><p><strong>maintenance_window_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subscription plan</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target project</p></li>
<li><p><strong>project_vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the VPC the service should be in, if any</p></li>
<li><p><strong>service_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service hostname</p></li>
<li><p><strong>service_integrations</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'KafkaServiceIntegrationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service integrations to specify when creating a service. Not applied after initial service creation</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service name</p></li>
<li><p><strong>service_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password used for connecting to the service, if applicable</p></li>
<li><p><strong>service_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Service port</p></li>
<li><p><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Aiven internal service type code</p></li>
<li><p><strong>service_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p></li>
<li><p><strong>service_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username used for connecting to the service, if applicable</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service state</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Prevent service from being deleted. It is recommended to have this enabled for all services.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.cloud_name">
<em class="property">property </em><code class="sig-name descname">cloud_name</code><a class="headerlink" href="#pulumi_aiven.Kafka.cloud_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud the service runs in</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.components">
<em class="property">property </em><code class="sig-name descname">components</code><a class="headerlink" href="#pulumi_aiven.Kafka.components" title="Permalink to this definition">¶</a></dt>
<dd><p>Service component information objects</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.default_acl">
<em class="property">property </em><code class="sig-name descname">default_acl</code><a class="headerlink" href="#pulumi_aiven.Kafka.default_acl" title="Permalink to this definition">¶</a></dt>
<dd><p>Create default wildcard Kafka ACL</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.kafka">
<em class="property">property </em><code class="sig-name descname">kafka</code><a class="headerlink" href="#pulumi_aiven.Kafka.kafka" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.kafka_user_config">
<em class="property">property </em><code class="sig-name descname">kafka_user_config</code><a class="headerlink" href="#pulumi_aiven.Kafka.kafka_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.maintenance_window_dow">
<em class="property">property </em><code class="sig-name descname">maintenance_window_dow</code><a class="headerlink" href="#pulumi_aiven.Kafka.maintenance_window_dow" title="Permalink to this definition">¶</a></dt>
<dd><p>Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.maintenance_window_time">
<em class="property">property </em><code class="sig-name descname">maintenance_window_time</code><a class="headerlink" href="#pulumi_aiven.Kafka.maintenance_window_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.plan">
<em class="property">property </em><code class="sig-name descname">plan</code><a class="headerlink" href="#pulumi_aiven.Kafka.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Subscription plan</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.Kafka.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Target project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.project_vpc_id">
<em class="property">property </em><code class="sig-name descname">project_vpc_id</code><a class="headerlink" href="#pulumi_aiven.Kafka.project_vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the VPC the service should be in, if any</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.service_host">
<em class="property">property </em><code class="sig-name descname">service_host</code><a class="headerlink" href="#pulumi_aiven.Kafka.service_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Service hostname</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.service_integrations">
<em class="property">property </em><code class="sig-name descname">service_integrations</code><a class="headerlink" href="#pulumi_aiven.Kafka.service_integrations" title="Permalink to this definition">¶</a></dt>
<dd><p>Service integrations to specify when creating a service. Not applied after initial service creation</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.Kafka.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.service_password">
<em class="property">property </em><code class="sig-name descname">service_password</code><a class="headerlink" href="#pulumi_aiven.Kafka.service_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.service_port">
<em class="property">property </em><code class="sig-name descname">service_port</code><a class="headerlink" href="#pulumi_aiven.Kafka.service_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Service port</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.service_type">
<em class="property">property </em><code class="sig-name descname">service_type</code><a class="headerlink" href="#pulumi_aiven.Kafka.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Aiven internal service type code</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.service_uri">
<em class="property">property </em><code class="sig-name descname">service_uri</code><a class="headerlink" href="#pulumi_aiven.Kafka.service_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.service_username">
<em class="property">property </em><code class="sig-name descname">service_username</code><a class="headerlink" href="#pulumi_aiven.Kafka.service_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_aiven.Kafka.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Service state</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.termination_protection">
<em class="property">property </em><code class="sig-name descname">termination_protection</code><a class="headerlink" href="#pulumi_aiven.Kafka.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Kafka.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Kafka.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Kafka.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Kafka.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaAcl">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">KafkaAcl</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permission</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topic</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaAcl" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">mytestacl</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">KafkaAcl</span><span class="p">(</span><span class="s2">&quot;mytestacl&quot;</span><span class="p">,</span>
    <span class="n">permission</span><span class="o">=</span><span class="s2">&quot;admin&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">aiven_project</span><span class="p">[</span><span class="s2">&quot;myproject&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">service_name</span><span class="o">=</span><span class="n">aiven_service</span><span class="p">[</span><span class="s2">&quot;myservice&quot;</span><span class="p">][</span><span class="s2">&quot;service_name&quot;</span><span class="p">],</span>
    <span class="n">topic</span><span class="o">=</span><span class="s2">&quot;&lt;TOPIC_NAME_PATTERN&gt;&quot;</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;&lt;USERNAME_PATTERN&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>permission</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka permission to grant (admin, read, readwrite, write)</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the Kafka ACL to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the Kafka ACL to</p></li>
<li><p><strong>topic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Topic name pattern for the ACL entry</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username pattern for the ACL entry</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_aiven.KafkaAcl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permission</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topic</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.kafka_acl.KafkaAcl<a class="headerlink" href="#pulumi_aiven.KafkaAcl.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KafkaAcl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>permission</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka permission to grant (admin, read, readwrite, write)</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the Kafka ACL to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the Kafka ACL to</p></li>
<li><p><strong>topic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Topic name pattern for the ACL entry</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username pattern for the ACL entry</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaAcl.permission">
<em class="property">property </em><code class="sig-name descname">permission</code><a class="headerlink" href="#pulumi_aiven.KafkaAcl.permission" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka permission to grant (admin, read, readwrite, write)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaAcl.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.KafkaAcl.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the Kafka ACL to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaAcl.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.KafkaAcl.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the Kafka ACL to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaAcl.topic">
<em class="property">property </em><code class="sig-name descname">topic</code><a class="headerlink" href="#pulumi_aiven.KafkaAcl.topic" title="Permalink to this definition">¶</a></dt>
<dd><p>Topic name pattern for the ACL entry</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaAcl.username">
<em class="property">property </em><code class="sig-name descname">username</code><a class="headerlink" href="#pulumi_aiven.KafkaAcl.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username pattern for the ACL entry</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaAcl.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaAcl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaAcl.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaAcl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaConnect">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">KafkaConnect</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect</span><span class="p">:</span> <span class="n">Union[KafkaConnectKafkaConnectArgs, Mapping[str, Any], Awaitable[Union[KafkaConnectKafkaConnectArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect_user_config</span><span class="p">:</span> <span class="n">Union[KafkaConnectKafkaConnectUserConfigArgs, Mapping[str, Any], Awaitable[Union[KafkaConnectKafkaConnectUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[KafkaConnectServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[KafkaConnectServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[KafkaConnectServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[KafkaConnectServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaConnect" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a KafkaConnect resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] cloud_name: Cloud the service runs in
:param pulumi.Input[pulumi.InputType[‘KafkaConnectKafkaConnectArgs’]] kafka_connect: Kafka Connect server provided values
:param pulumi.Input[pulumi.InputType[‘KafkaConnectKafkaConnectUserConfigArgs’]] kafka_connect_user_config: Kafka Connect user configurable settings
:param pulumi.Input[str] maintenance_window_dow: Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.
:param pulumi.Input[str] maintenance_window_time: Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.
:param pulumi.Input[str] plan: Subscription plan
:param pulumi.Input[str] project: Target project
:param pulumi.Input[str] project_vpc_id: Identifier of the VPC the service should be in, if any
:param pulumi.Input[List[pulumi.Input[pulumi.InputType[‘KafkaConnectServiceIntegrationArgs’]]]] service_integrations: Service integrations to specify when creating a service. Not applied after initial service creation
:param pulumi.Input[str] service_name: Service name
:param pulumi.Input[bool] termination_protection: Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Union[List[Union[KafkaConnectComponentArgs, Mapping[str, Any], Awaitable[Union[KafkaConnectComponentArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[KafkaConnectComponentArgs, Mapping[str, Any], Awaitable[Union[KafkaConnectComponentArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect</span><span class="p">:</span> <span class="n">Union[KafkaConnectKafkaConnectArgs, Mapping[str, Any], Awaitable[Union[KafkaConnectKafkaConnectArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect_user_config</span><span class="p">:</span> <span class="n">Union[KafkaConnectKafkaConnectUserConfigArgs, Mapping[str, Any], Awaitable[Union[KafkaConnectKafkaConnectUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[KafkaConnectServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[KafkaConnectServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[KafkaConnectServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[KafkaConnectServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.kafka_connect.KafkaConnect<a class="headerlink" href="#pulumi_aiven.KafkaConnect.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KafkaConnect resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud the service runs in</p></li>
<li><p><strong>components</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'KafkaConnectComponentArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service component information objects</p></li>
<li><p><strong>kafka_connect</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'KafkaConnectKafkaConnectArgs'</em><em>]</em><em>]</em>) – Kafka Connect server provided values</p></li>
<li><p><strong>kafka_connect_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'KafkaConnectKafkaConnectUserConfigArgs'</em><em>]</em><em>]</em>) – Kafka Connect user configurable settings</p></li>
<li><p><strong>maintenance_window_dow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p></li>
<li><p><strong>maintenance_window_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subscription plan</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target project</p></li>
<li><p><strong>project_vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the VPC the service should be in, if any</p></li>
<li><p><strong>service_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service hostname</p></li>
<li><p><strong>service_integrations</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'KafkaConnectServiceIntegrationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service integrations to specify when creating a service. Not applied after initial service creation</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service name</p></li>
<li><p><strong>service_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password used for connecting to the service, if applicable</p></li>
<li><p><strong>service_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Service port</p></li>
<li><p><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Aiven internal service type code</p></li>
<li><p><strong>service_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p></li>
<li><p><strong>service_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username used for connecting to the service, if applicable</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service state</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Prevent service from being deleted. It is recommended to have this enabled for all services.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.cloud_name">
<em class="property">property </em><code class="sig-name descname">cloud_name</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.cloud_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud the service runs in</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.components">
<em class="property">property </em><code class="sig-name descname">components</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.components" title="Permalink to this definition">¶</a></dt>
<dd><p>Service component information objects</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.kafka_connect">
<em class="property">property </em><code class="sig-name descname">kafka_connect</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.kafka_connect" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka Connect server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.kafka_connect_user_config">
<em class="property">property </em><code class="sig-name descname">kafka_connect_user_config</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.kafka_connect_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka Connect user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.maintenance_window_dow">
<em class="property">property </em><code class="sig-name descname">maintenance_window_dow</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.maintenance_window_dow" title="Permalink to this definition">¶</a></dt>
<dd><p>Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.maintenance_window_time">
<em class="property">property </em><code class="sig-name descname">maintenance_window_time</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.maintenance_window_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.plan">
<em class="property">property </em><code class="sig-name descname">plan</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Subscription plan</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Target project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.project_vpc_id">
<em class="property">property </em><code class="sig-name descname">project_vpc_id</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.project_vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the VPC the service should be in, if any</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.service_host">
<em class="property">property </em><code class="sig-name descname">service_host</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.service_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Service hostname</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.service_integrations">
<em class="property">property </em><code class="sig-name descname">service_integrations</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.service_integrations" title="Permalink to this definition">¶</a></dt>
<dd><p>Service integrations to specify when creating a service. Not applied after initial service creation</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.service_password">
<em class="property">property </em><code class="sig-name descname">service_password</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.service_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.service_port">
<em class="property">property </em><code class="sig-name descname">service_port</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.service_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Service port</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.service_type">
<em class="property">property </em><code class="sig-name descname">service_type</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Aiven internal service type code</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.service_uri">
<em class="property">property </em><code class="sig-name descname">service_uri</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.service_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.service_username">
<em class="property">property </em><code class="sig-name descname">service_username</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.service_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Service state</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.termination_protection">
<em class="property">property </em><code class="sig-name descname">termination_protection</code><a class="headerlink" href="#pulumi_aiven.KafkaConnect.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnect.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaConnect.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaConnect.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaConnect.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaConnector">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">KafkaConnector</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connector_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaConnector" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a KafkaConnector resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[Mapping[str, pulumi.Input[str]]] config: Kafka Connector configuration parameters
:param pulumi.Input[str] connector_name: Kafka connector name
:param pulumi.Input[str] project: Project to link the kafka connector to
:param pulumi.Input[str] service_name: Service to link the kafka connector to</p>
<dl class="py method">
<dt id="pulumi_aiven.KafkaConnector.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connector_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_author</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_class</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_doc_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_version</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tasks</span><span class="p">:</span> <span class="n">Union[List[Union[KafkaConnectorTaskArgs, Mapping[str, Any], Awaitable[Union[KafkaConnectorTaskArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[KafkaConnectorTaskArgs, Mapping[str, Any], Awaitable[Union[KafkaConnectorTaskArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.kafka_connector.KafkaConnector<a class="headerlink" href="#pulumi_aiven.KafkaConnector.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KafkaConnector resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Kafka Connector configuration parameters</p></li>
<li><p><strong>connector_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka connector name</p></li>
<li><p><strong>plugin_author</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka connector author</p></li>
<li><p><strong>plugin_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka connector Java class</p></li>
<li><p><strong>plugin_doc_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka connector documentation URL</p></li>
<li><p><strong>plugin_title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka connector title</p></li>
<li><p><strong>plugin_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka connector type</p></li>
<li><p><strong>plugin_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka connector version</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the kafka connector to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the kafka connector to</p></li>
<li><p><strong>tasks</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'KafkaConnectorTaskArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of tasks of a connector</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnector.config">
<em class="property">property </em><code class="sig-name descname">config</code><a class="headerlink" href="#pulumi_aiven.KafkaConnector.config" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka Connector configuration parameters</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnector.connector_name">
<em class="property">property </em><code class="sig-name descname">connector_name</code><a class="headerlink" href="#pulumi_aiven.KafkaConnector.connector_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka connector name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnector.plugin_author">
<em class="property">property </em><code class="sig-name descname">plugin_author</code><a class="headerlink" href="#pulumi_aiven.KafkaConnector.plugin_author" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka connector author</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnector.plugin_class">
<em class="property">property </em><code class="sig-name descname">plugin_class</code><a class="headerlink" href="#pulumi_aiven.KafkaConnector.plugin_class" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka connector Java class</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnector.plugin_doc_url">
<em class="property">property </em><code class="sig-name descname">plugin_doc_url</code><a class="headerlink" href="#pulumi_aiven.KafkaConnector.plugin_doc_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka connector documentation URL</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnector.plugin_title">
<em class="property">property </em><code class="sig-name descname">plugin_title</code><a class="headerlink" href="#pulumi_aiven.KafkaConnector.plugin_title" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka connector title</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnector.plugin_type">
<em class="property">property </em><code class="sig-name descname">plugin_type</code><a class="headerlink" href="#pulumi_aiven.KafkaConnector.plugin_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka connector type</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnector.plugin_version">
<em class="property">property </em><code class="sig-name descname">plugin_version</code><a class="headerlink" href="#pulumi_aiven.KafkaConnector.plugin_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka connector version</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnector.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.KafkaConnector.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the kafka connector to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnector.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.KafkaConnector.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the kafka connector to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnector.tasks">
<em class="property">property </em><code class="sig-name descname">tasks</code><a class="headerlink" href="#pulumi_aiven.KafkaConnector.tasks" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tasks of a connector</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaConnector.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaConnector.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaConnector.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaConnector.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaMirrorMaker">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">KafkaMirrorMaker</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker</span><span class="p">:</span> <span class="n">Union[KafkaMirrorMakerKafkaMirrormakerArgs, Mapping[str, Any], Awaitable[Union[KafkaMirrorMakerKafkaMirrormakerArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker_user_config</span><span class="p">:</span> <span class="n">Union[KafkaMirrorMakerKafkaMirrormakerUserConfigArgs, Mapping[str, Any], Awaitable[Union[KafkaMirrorMakerKafkaMirrormakerUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[KafkaMirrorMakerServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[KafkaMirrorMakerServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[KafkaMirrorMakerServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[KafkaMirrorMakerServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a KafkaMirrorMaker resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] cloud_name: Cloud the service runs in
:param pulumi.Input[pulumi.InputType[‘KafkaMirrorMakerKafkaMirrormakerArgs’]] kafka_mirrormaker: Kafka MirrorMaker 2 server provided values
:param pulumi.Input[pulumi.InputType[‘KafkaMirrorMakerKafkaMirrormakerUserConfigArgs’]] kafka_mirrormaker_user_config: Kafka MirrorMaker 2 specific user configurable settings
:param pulumi.Input[str] maintenance_window_dow: Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.
:param pulumi.Input[str] maintenance_window_time: Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.
:param pulumi.Input[str] plan: Subscription plan
:param pulumi.Input[str] project: Target project
:param pulumi.Input[str] project_vpc_id: Identifier of the VPC the service should be in, if any
:param pulumi.Input[List[pulumi.Input[pulumi.InputType[‘KafkaMirrorMakerServiceIntegrationArgs’]]]] service_integrations: Service integrations to specify when creating a service. Not applied after initial service creation
:param pulumi.Input[str] service_name: Service name
:param pulumi.Input[bool] termination_protection: Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Union[List[Union[KafkaMirrorMakerComponentArgs, Mapping[str, Any], Awaitable[Union[KafkaMirrorMakerComponentArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[KafkaMirrorMakerComponentArgs, Mapping[str, Any], Awaitable[Union[KafkaMirrorMakerComponentArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker</span><span class="p">:</span> <span class="n">Union[KafkaMirrorMakerKafkaMirrormakerArgs, Mapping[str, Any], Awaitable[Union[KafkaMirrorMakerKafkaMirrormakerArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker_user_config</span><span class="p">:</span> <span class="n">Union[KafkaMirrorMakerKafkaMirrormakerUserConfigArgs, Mapping[str, Any], Awaitable[Union[KafkaMirrorMakerKafkaMirrormakerUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[KafkaMirrorMakerServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[KafkaMirrorMakerServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[KafkaMirrorMakerServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[KafkaMirrorMakerServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.kafka_mirror_maker.KafkaMirrorMaker<a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KafkaMirrorMaker resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud the service runs in</p></li>
<li><p><strong>components</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'KafkaMirrorMakerComponentArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service component information objects</p></li>
<li><p><strong>kafka_mirrormaker</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'KafkaMirrorMakerKafkaMirrormakerArgs'</em><em>]</em><em>]</em>) – Kafka MirrorMaker 2 server provided values</p></li>
<li><p><strong>kafka_mirrormaker_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'KafkaMirrorMakerKafkaMirrormakerUserConfigArgs'</em><em>]</em><em>]</em>) – Kafka MirrorMaker 2 specific user configurable settings</p></li>
<li><p><strong>maintenance_window_dow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p></li>
<li><p><strong>maintenance_window_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subscription plan</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target project</p></li>
<li><p><strong>project_vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the VPC the service should be in, if any</p></li>
<li><p><strong>service_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service hostname</p></li>
<li><p><strong>service_integrations</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'KafkaMirrorMakerServiceIntegrationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service integrations to specify when creating a service. Not applied after initial service creation</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service name</p></li>
<li><p><strong>service_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password used for connecting to the service, if applicable</p></li>
<li><p><strong>service_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Service port</p></li>
<li><p><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Aiven internal service type code</p></li>
<li><p><strong>service_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p></li>
<li><p><strong>service_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username used for connecting to the service, if applicable</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service state</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Prevent service from being deleted. It is recommended to have this enabled for all services.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.cloud_name">
<em class="property">property </em><code class="sig-name descname">cloud_name</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.cloud_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud the service runs in</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.components">
<em class="property">property </em><code class="sig-name descname">components</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.components" title="Permalink to this definition">¶</a></dt>
<dd><p>Service component information objects</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.kafka_mirrormaker">
<em class="property">property </em><code class="sig-name descname">kafka_mirrormaker</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.kafka_mirrormaker" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka MirrorMaker 2 server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.kafka_mirrormaker_user_config">
<em class="property">property </em><code class="sig-name descname">kafka_mirrormaker_user_config</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.kafka_mirrormaker_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka MirrorMaker 2 specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.maintenance_window_dow">
<em class="property">property </em><code class="sig-name descname">maintenance_window_dow</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.maintenance_window_dow" title="Permalink to this definition">¶</a></dt>
<dd><p>Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.maintenance_window_time">
<em class="property">property </em><code class="sig-name descname">maintenance_window_time</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.maintenance_window_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.plan">
<em class="property">property </em><code class="sig-name descname">plan</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Subscription plan</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Target project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.project_vpc_id">
<em class="property">property </em><code class="sig-name descname">project_vpc_id</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.project_vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the VPC the service should be in, if any</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.service_host">
<em class="property">property </em><code class="sig-name descname">service_host</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.service_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Service hostname</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.service_integrations">
<em class="property">property </em><code class="sig-name descname">service_integrations</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.service_integrations" title="Permalink to this definition">¶</a></dt>
<dd><p>Service integrations to specify when creating a service. Not applied after initial service creation</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.service_password">
<em class="property">property </em><code class="sig-name descname">service_password</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.service_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.service_port">
<em class="property">property </em><code class="sig-name descname">service_port</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.service_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Service port</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.service_type">
<em class="property">property </em><code class="sig-name descname">service_type</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Aiven internal service type code</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.service_uri">
<em class="property">property </em><code class="sig-name descname">service_uri</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.service_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.service_username">
<em class="property">property </em><code class="sig-name descname">service_username</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.service_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Service state</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.termination_protection">
<em class="property">property </em><code class="sig-name descname">termination_protection</code><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaMirrorMaker.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaMirrorMaker.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaMirrorMaker.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaSchema">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">KafkaSchema</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaSchema" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a KafkaSchema resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] project: Project to link the Kafka Schema to
:param pulumi.Input[str] schema: Kafka Schema configuration should be a valid Avro Schema JSON format
:param pulumi.Input[str] service_name: Service to link the Kafka Schema to
:param pulumi.Input[str] subject_name: Kafka Schema Subject name</p>
<dl class="py method">
<dt id="pulumi_aiven.KafkaSchema.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.kafka_schema.KafkaSchema<a class="headerlink" href="#pulumi_aiven.KafkaSchema.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KafkaSchema resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the Kafka Schema to</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka Schema configuration should be a valid Avro Schema JSON format</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the Kafka Schema to</p></li>
<li><p><strong>subject_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka Schema Subject name</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Kafka Schema configuration version</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaSchema.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.KafkaSchema.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the Kafka Schema to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaSchema.schema">
<em class="property">property </em><code class="sig-name descname">schema</code><a class="headerlink" href="#pulumi_aiven.KafkaSchema.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka Schema configuration should be a valid Avro Schema JSON format</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaSchema.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.KafkaSchema.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the Kafka Schema to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaSchema.subject_name">
<em class="property">property </em><code class="sig-name descname">subject_name</code><a class="headerlink" href="#pulumi_aiven.KafkaSchema.subject_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka Schema Subject name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaSchema.version">
<em class="property">property </em><code class="sig-name descname">version</code><a class="headerlink" href="#pulumi_aiven.KafkaSchema.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka Schema configuration version</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaSchema.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaSchema.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaSchema.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaSchema.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaSchemaConfiguration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">KafkaSchemaConfiguration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compatibility_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaSchemaConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a KafkaSchemaConfiguration resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] compatibility_level: Kafka Schemas compatibility level
:param pulumi.Input[str] project: Project to link the Kafka Schemas Configuration to
:param pulumi.Input[str] service_name: Service to link the Kafka Schemas Configuration to</p>
<dl class="py method">
<dt id="pulumi_aiven.KafkaSchemaConfiguration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compatibility_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.kafka_schema_configuration.KafkaSchemaConfiguration<a class="headerlink" href="#pulumi_aiven.KafkaSchemaConfiguration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KafkaSchemaConfiguration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>compatibility_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Kafka Schemas compatibility level</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the Kafka Schemas Configuration to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the Kafka Schemas Configuration to</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaSchemaConfiguration.compatibility_level">
<em class="property">property </em><code class="sig-name descname">compatibility_level</code><a class="headerlink" href="#pulumi_aiven.KafkaSchemaConfiguration.compatibility_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka Schemas compatibility level</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaSchemaConfiguration.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.KafkaSchemaConfiguration.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the Kafka Schemas Configuration to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaSchemaConfiguration.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.KafkaSchemaConfiguration.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the Kafka Schemas Configuration to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaSchemaConfiguration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaSchemaConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaSchemaConfiguration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaSchemaConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaTopic">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">KafkaTopic</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cleanup_policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_in_sync_replicas</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partitions</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_bytes</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_hours</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topic_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaTopic" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">mytesttopic</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">KafkaTopic</span><span class="p">(</span><span class="s2">&quot;mytesttopic&quot;</span><span class="p">,</span>
    <span class="n">cleanup_policy</span><span class="o">=</span><span class="s2">&quot;delete&quot;</span><span class="p">,</span>
    <span class="n">minimum_in_sync_replicas</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">partitions</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">aiven_project</span><span class="p">[</span><span class="s2">&quot;myproject&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">replication</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
    <span class="n">retention_bytes</span><span class="o">=-</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">retention_hours</span><span class="o">=</span><span class="mi">72</span><span class="p">,</span>
    <span class="n">service_name</span><span class="o">=</span><span class="n">aiven_service</span><span class="p">[</span><span class="s2">&quot;myservice&quot;</span><span class="p">][</span><span class="s2">&quot;service_name&quot;</span><span class="p">],</span>
    <span class="n">topic_name</span><span class="o">=</span><span class="s2">&quot;&lt;TOPIC_NAME&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cleanup_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Topic cleanup policy. Allowed values: delete, compact</p></li>
<li><p><strong>minimum_in_sync_replicas</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum required nodes in-sync replicas (ISR) to produce to a partition</p></li>
<li><p><strong>partitions</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of partitions to create in the topic</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the kafka topic to</p></li>
<li><p><strong>replication</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Replication factor for the topic</p></li>
<li><p><strong>retention_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Retention bytes</p></li>
<li><p><strong>retention_hours</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Retention period (hours)</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the kafka topic to</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – It is a Terraform client-side deletion protection, which prevents a Kafka topic from being deleted. It is recommended to
enable this for any production Kafka topic containing critical data.</p></li>
<li><p><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Topic name</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_aiven.KafkaTopic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cleanup_policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_in_sync_replicas</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partitions</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_bytes</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_hours</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topic_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.kafka_topic.KafkaTopic<a class="headerlink" href="#pulumi_aiven.KafkaTopic.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KafkaTopic resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cleanup_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Topic cleanup policy. Allowed values: delete, compact</p></li>
<li><p><strong>minimum_in_sync_replicas</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum required nodes in-sync replicas (ISR) to produce to a partition</p></li>
<li><p><strong>partitions</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of partitions to create in the topic</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the kafka topic to</p></li>
<li><p><strong>replication</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Replication factor for the topic</p></li>
<li><p><strong>retention_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Retention bytes</p></li>
<li><p><strong>retention_hours</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Retention period (hours)</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the kafka topic to</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – It is a Terraform client-side deletion protection, which prevents a Kafka topic from being deleted. It is recommended to
enable this for any production Kafka topic containing critical data.</p></li>
<li><p><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Topic name</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaTopic.cleanup_policy">
<em class="property">property </em><code class="sig-name descname">cleanup_policy</code><a class="headerlink" href="#pulumi_aiven.KafkaTopic.cleanup_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Topic cleanup policy. Allowed values: delete, compact</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaTopic.minimum_in_sync_replicas">
<em class="property">property </em><code class="sig-name descname">minimum_in_sync_replicas</code><a class="headerlink" href="#pulumi_aiven.KafkaTopic.minimum_in_sync_replicas" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum required nodes in-sync replicas (ISR) to produce to a partition</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaTopic.partitions">
<em class="property">property </em><code class="sig-name descname">partitions</code><a class="headerlink" href="#pulumi_aiven.KafkaTopic.partitions" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of partitions to create in the topic</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaTopic.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.KafkaTopic.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the kafka topic to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaTopic.replication">
<em class="property">property </em><code class="sig-name descname">replication</code><a class="headerlink" href="#pulumi_aiven.KafkaTopic.replication" title="Permalink to this definition">¶</a></dt>
<dd><p>Replication factor for the topic</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaTopic.retention_bytes">
<em class="property">property </em><code class="sig-name descname">retention_bytes</code><a class="headerlink" href="#pulumi_aiven.KafkaTopic.retention_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>Retention bytes</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaTopic.retention_hours">
<em class="property">property </em><code class="sig-name descname">retention_hours</code><a class="headerlink" href="#pulumi_aiven.KafkaTopic.retention_hours" title="Permalink to this definition">¶</a></dt>
<dd><p>Retention period (hours)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaTopic.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.KafkaTopic.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the kafka topic to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaTopic.termination_protection">
<em class="property">property </em><code class="sig-name descname">termination_protection</code><a class="headerlink" href="#pulumi_aiven.KafkaTopic.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>It is a Terraform client-side deletion protection, which prevents a Kafka topic from being deleted. It is recommended to
enable this for any production Kafka topic containing critical data.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaTopic.topic_name">
<em class="property">property </em><code class="sig-name descname">topic_name</code><a class="headerlink" href="#pulumi_aiven.KafkaTopic.topic_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Topic name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.KafkaTopic.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaTopic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.KafkaTopic.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.KafkaTopic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.MirrorMakerReplicationFlow">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">MirrorMakerReplicationFlow</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_cluster</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_cluster</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topics</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topics_blacklists</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.MirrorMakerReplicationFlow" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a MirrorMakerReplicationFlow resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] enable: Enable of disable replication flows for a service
:param pulumi.Input[str] project: Project to link the kafka topic to
:param pulumi.Input[str] service_name: Service to link the kafka topic to
:param pulumi.Input[str] source_cluster: Source cluster alias
:param pulumi.Input[str] target_cluster: Target cluster alias
:param pulumi.Input[List[pulumi.Input[str]]] topics: List of topics and/or regular expressions to replicate
:param pulumi.Input[List[pulumi.Input[str]]] topics_blacklists: List of topics and/or regular expressions to not replicate.</p>
<dl class="py method">
<dt id="pulumi_aiven.MirrorMakerReplicationFlow.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_cluster</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_cluster</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topics</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topics_blacklists</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.mirror_maker_replication_flow.MirrorMakerReplicationFlow<a class="headerlink" href="#pulumi_aiven.MirrorMakerReplicationFlow.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MirrorMakerReplicationFlow resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable of disable replication flows for a service</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the kafka topic to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the kafka topic to</p></li>
<li><p><strong>source_cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Source cluster alias</p></li>
<li><p><strong>target_cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target cluster alias</p></li>
<li><p><strong>topics</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of topics and/or regular expressions to replicate</p></li>
<li><p><strong>topics_blacklists</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of topics and/or regular expressions to not replicate.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MirrorMakerReplicationFlow.enable">
<em class="property">property </em><code class="sig-name descname">enable</code><a class="headerlink" href="#pulumi_aiven.MirrorMakerReplicationFlow.enable" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable of disable replication flows for a service</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MirrorMakerReplicationFlow.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.MirrorMakerReplicationFlow.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the kafka topic to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MirrorMakerReplicationFlow.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.MirrorMakerReplicationFlow.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the kafka topic to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MirrorMakerReplicationFlow.source_cluster">
<em class="property">property </em><code class="sig-name descname">source_cluster</code><a class="headerlink" href="#pulumi_aiven.MirrorMakerReplicationFlow.source_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Source cluster alias</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MirrorMakerReplicationFlow.target_cluster">
<em class="property">property </em><code class="sig-name descname">target_cluster</code><a class="headerlink" href="#pulumi_aiven.MirrorMakerReplicationFlow.target_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Target cluster alias</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MirrorMakerReplicationFlow.topics">
<em class="property">property </em><code class="sig-name descname">topics</code><a class="headerlink" href="#pulumi_aiven.MirrorMakerReplicationFlow.topics" title="Permalink to this definition">¶</a></dt>
<dd><p>List of topics and/or regular expressions to replicate</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MirrorMakerReplicationFlow.topics_blacklists">
<em class="property">property </em><code class="sig-name descname">topics_blacklists</code><a class="headerlink" href="#pulumi_aiven.MirrorMakerReplicationFlow.topics_blacklists" title="Permalink to this definition">¶</a></dt>
<dd><p>List of topics and/or regular expressions to not replicate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MirrorMakerReplicationFlow.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.MirrorMakerReplicationFlow.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.MirrorMakerReplicationFlow.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.MirrorMakerReplicationFlow.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.MySql">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">MySql</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql</span><span class="p">:</span> <span class="n">Union[MySqlMysqlArgs, Mapping[str, Any], Awaitable[Union[MySqlMysqlArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql_user_config</span><span class="p">:</span> <span class="n">Union[MySqlMysqlUserConfigArgs, Mapping[str, Any], Awaitable[Union[MySqlMysqlUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[MySqlServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[MySqlServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[MySqlServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[MySqlServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.MySql" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a MySql resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] cloud_name: Cloud the service runs in
:param pulumi.Input[str] maintenance_window_dow: Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.
:param pulumi.Input[str] maintenance_window_time: Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.
:param pulumi.Input[pulumi.InputType[‘MySqlMysqlArgs’]] mysql: MySQL specific server provided values
:param pulumi.Input[pulumi.InputType[‘MySqlMysqlUserConfigArgs’]] mysql_user_config: MySQL specific user configurable settings
:param pulumi.Input[str] plan: Subscription plan
:param pulumi.Input[str] project: Target project
:param pulumi.Input[str] project_vpc_id: Identifier of the VPC the service should be in, if any
:param pulumi.Input[List[pulumi.Input[pulumi.InputType[‘MySqlServiceIntegrationArgs’]]]] service_integrations: Service integrations to specify when creating a service. Not applied after initial service creation
:param pulumi.Input[str] service_name: Service name
:param pulumi.Input[bool] termination_protection: Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
<dl class="py method">
<dt id="pulumi_aiven.MySql.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Union[List[Union[MySqlComponentArgs, Mapping[str, Any], Awaitable[Union[MySqlComponentArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[MySqlComponentArgs, Mapping[str, Any], Awaitable[Union[MySqlComponentArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql</span><span class="p">:</span> <span class="n">Union[MySqlMysqlArgs, Mapping[str, Any], Awaitable[Union[MySqlMysqlArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql_user_config</span><span class="p">:</span> <span class="n">Union[MySqlMysqlUserConfigArgs, Mapping[str, Any], Awaitable[Union[MySqlMysqlUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[MySqlServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[MySqlServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[MySqlServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[MySqlServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.my_sql.MySql<a class="headerlink" href="#pulumi_aiven.MySql.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MySql resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud the service runs in</p></li>
<li><p><strong>components</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MySqlComponentArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service component information objects</p></li>
<li><p><strong>maintenance_window_dow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p></li>
<li><p><strong>maintenance_window_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p></li>
<li><p><strong>mysql</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MySqlMysqlArgs'</em><em>]</em><em>]</em>) – MySQL specific server provided values</p></li>
<li><p><strong>mysql_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MySqlMysqlUserConfigArgs'</em><em>]</em><em>]</em>) – MySQL specific user configurable settings</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subscription plan</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target project</p></li>
<li><p><strong>project_vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the VPC the service should be in, if any</p></li>
<li><p><strong>service_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service hostname</p></li>
<li><p><strong>service_integrations</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MySqlServiceIntegrationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service integrations to specify when creating a service. Not applied after initial service creation</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service name</p></li>
<li><p><strong>service_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password used for connecting to the service, if applicable</p></li>
<li><p><strong>service_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Service port</p></li>
<li><p><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Aiven internal service type code</p></li>
<li><p><strong>service_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p></li>
<li><p><strong>service_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username used for connecting to the service, if applicable</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service state</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Prevent service from being deleted. It is recommended to have this enabled for all services.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.cloud_name">
<em class="property">property </em><code class="sig-name descname">cloud_name</code><a class="headerlink" href="#pulumi_aiven.MySql.cloud_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud the service runs in</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.components">
<em class="property">property </em><code class="sig-name descname">components</code><a class="headerlink" href="#pulumi_aiven.MySql.components" title="Permalink to this definition">¶</a></dt>
<dd><p>Service component information objects</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.maintenance_window_dow">
<em class="property">property </em><code class="sig-name descname">maintenance_window_dow</code><a class="headerlink" href="#pulumi_aiven.MySql.maintenance_window_dow" title="Permalink to this definition">¶</a></dt>
<dd><p>Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.maintenance_window_time">
<em class="property">property </em><code class="sig-name descname">maintenance_window_time</code><a class="headerlink" href="#pulumi_aiven.MySql.maintenance_window_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.mysql">
<em class="property">property </em><code class="sig-name descname">mysql</code><a class="headerlink" href="#pulumi_aiven.MySql.mysql" title="Permalink to this definition">¶</a></dt>
<dd><p>MySQL specific server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.mysql_user_config">
<em class="property">property </em><code class="sig-name descname">mysql_user_config</code><a class="headerlink" href="#pulumi_aiven.MySql.mysql_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>MySQL specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.plan">
<em class="property">property </em><code class="sig-name descname">plan</code><a class="headerlink" href="#pulumi_aiven.MySql.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Subscription plan</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.MySql.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Target project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.project_vpc_id">
<em class="property">property </em><code class="sig-name descname">project_vpc_id</code><a class="headerlink" href="#pulumi_aiven.MySql.project_vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the VPC the service should be in, if any</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.service_host">
<em class="property">property </em><code class="sig-name descname">service_host</code><a class="headerlink" href="#pulumi_aiven.MySql.service_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Service hostname</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.service_integrations">
<em class="property">property </em><code class="sig-name descname">service_integrations</code><a class="headerlink" href="#pulumi_aiven.MySql.service_integrations" title="Permalink to this definition">¶</a></dt>
<dd><p>Service integrations to specify when creating a service. Not applied after initial service creation</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.MySql.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.service_password">
<em class="property">property </em><code class="sig-name descname">service_password</code><a class="headerlink" href="#pulumi_aiven.MySql.service_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.service_port">
<em class="property">property </em><code class="sig-name descname">service_port</code><a class="headerlink" href="#pulumi_aiven.MySql.service_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Service port</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.service_type">
<em class="property">property </em><code class="sig-name descname">service_type</code><a class="headerlink" href="#pulumi_aiven.MySql.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Aiven internal service type code</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.service_uri">
<em class="property">property </em><code class="sig-name descname">service_uri</code><a class="headerlink" href="#pulumi_aiven.MySql.service_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.service_username">
<em class="property">property </em><code class="sig-name descname">service_username</code><a class="headerlink" href="#pulumi_aiven.MySql.service_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_aiven.MySql.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Service state</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.termination_protection">
<em class="property">property </em><code class="sig-name descname">termination_protection</code><a class="headerlink" href="#pulumi_aiven.MySql.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.MySql.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.MySql.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.MySql.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.MySql.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Pg">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">Pg</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg</span><span class="p">:</span> <span class="n">Union[PgPgArgs, Mapping[str, Any], Awaitable[Union[PgPgArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg_user_config</span><span class="p">:</span> <span class="n">Union[PgPgUserConfigArgs, Mapping[str, Any], Awaitable[Union[PgPgUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[PgServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[PgServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[PgServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[PgServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Pg" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Pg resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] cloud_name: Cloud the service runs in
:param pulumi.Input[str] maintenance_window_dow: Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.
:param pulumi.Input[str] maintenance_window_time: Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.
:param pulumi.Input[pulumi.InputType[‘PgPgArgs’]] pg: PostgreSQL specific server provided values
:param pulumi.Input[pulumi.InputType[‘PgPgUserConfigArgs’]] pg_user_config: PostgreSQL specific user configurable settings
:param pulumi.Input[str] plan: Subscription plan
:param pulumi.Input[str] project: Target project
:param pulumi.Input[str] project_vpc_id: Identifier of the VPC the service should be in, if any
:param pulumi.Input[List[pulumi.Input[pulumi.InputType[‘PgServiceIntegrationArgs’]]]] service_integrations: Service integrations to specify when creating a service. Not applied after initial service creation
:param pulumi.Input[str] service_name: Service name
:param pulumi.Input[bool] termination_protection: Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
<dl class="py method">
<dt id="pulumi_aiven.Pg.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Union[List[Union[PgComponentArgs, Mapping[str, Any], Awaitable[Union[PgComponentArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[PgComponentArgs, Mapping[str, Any], Awaitable[Union[PgComponentArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg</span><span class="p">:</span> <span class="n">Union[PgPgArgs, Mapping[str, Any], Awaitable[Union[PgPgArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg_user_config</span><span class="p">:</span> <span class="n">Union[PgPgUserConfigArgs, Mapping[str, Any], Awaitable[Union[PgPgUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[PgServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[PgServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[PgServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[PgServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.pg.Pg<a class="headerlink" href="#pulumi_aiven.Pg.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Pg resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud the service runs in</p></li>
<li><p><strong>components</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'PgComponentArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service component information objects</p></li>
<li><p><strong>maintenance_window_dow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p></li>
<li><p><strong>maintenance_window_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p></li>
<li><p><strong>pg</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'PgPgArgs'</em><em>]</em><em>]</em>) – PostgreSQL specific server provided values</p></li>
<li><p><strong>pg_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'PgPgUserConfigArgs'</em><em>]</em><em>]</em>) – PostgreSQL specific user configurable settings</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subscription plan</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target project</p></li>
<li><p><strong>project_vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the VPC the service should be in, if any</p></li>
<li><p><strong>service_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service hostname</p></li>
<li><p><strong>service_integrations</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'PgServiceIntegrationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service integrations to specify when creating a service. Not applied after initial service creation</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service name</p></li>
<li><p><strong>service_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password used for connecting to the service, if applicable</p></li>
<li><p><strong>service_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Service port</p></li>
<li><p><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Aiven internal service type code</p></li>
<li><p><strong>service_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p></li>
<li><p><strong>service_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username used for connecting to the service, if applicable</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service state</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Prevent service from being deleted. It is recommended to have this enabled for all services.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.cloud_name">
<em class="property">property </em><code class="sig-name descname">cloud_name</code><a class="headerlink" href="#pulumi_aiven.Pg.cloud_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud the service runs in</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.components">
<em class="property">property </em><code class="sig-name descname">components</code><a class="headerlink" href="#pulumi_aiven.Pg.components" title="Permalink to this definition">¶</a></dt>
<dd><p>Service component information objects</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.maintenance_window_dow">
<em class="property">property </em><code class="sig-name descname">maintenance_window_dow</code><a class="headerlink" href="#pulumi_aiven.Pg.maintenance_window_dow" title="Permalink to this definition">¶</a></dt>
<dd><p>Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.maintenance_window_time">
<em class="property">property </em><code class="sig-name descname">maintenance_window_time</code><a class="headerlink" href="#pulumi_aiven.Pg.maintenance_window_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.pg">
<em class="property">property </em><code class="sig-name descname">pg</code><a class="headerlink" href="#pulumi_aiven.Pg.pg" title="Permalink to this definition">¶</a></dt>
<dd><p>PostgreSQL specific server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.pg_user_config">
<em class="property">property </em><code class="sig-name descname">pg_user_config</code><a class="headerlink" href="#pulumi_aiven.Pg.pg_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>PostgreSQL specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.plan">
<em class="property">property </em><code class="sig-name descname">plan</code><a class="headerlink" href="#pulumi_aiven.Pg.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Subscription plan</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.Pg.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Target project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.project_vpc_id">
<em class="property">property </em><code class="sig-name descname">project_vpc_id</code><a class="headerlink" href="#pulumi_aiven.Pg.project_vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the VPC the service should be in, if any</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.service_host">
<em class="property">property </em><code class="sig-name descname">service_host</code><a class="headerlink" href="#pulumi_aiven.Pg.service_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Service hostname</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.service_integrations">
<em class="property">property </em><code class="sig-name descname">service_integrations</code><a class="headerlink" href="#pulumi_aiven.Pg.service_integrations" title="Permalink to this definition">¶</a></dt>
<dd><p>Service integrations to specify when creating a service. Not applied after initial service creation</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.Pg.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.service_password">
<em class="property">property </em><code class="sig-name descname">service_password</code><a class="headerlink" href="#pulumi_aiven.Pg.service_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.service_port">
<em class="property">property </em><code class="sig-name descname">service_port</code><a class="headerlink" href="#pulumi_aiven.Pg.service_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Service port</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.service_type">
<em class="property">property </em><code class="sig-name descname">service_type</code><a class="headerlink" href="#pulumi_aiven.Pg.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Aiven internal service type code</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.service_uri">
<em class="property">property </em><code class="sig-name descname">service_uri</code><a class="headerlink" href="#pulumi_aiven.Pg.service_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.service_username">
<em class="property">property </em><code class="sig-name descname">service_username</code><a class="headerlink" href="#pulumi_aiven.Pg.service_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_aiven.Pg.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Service state</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.termination_protection">
<em class="property">property </em><code class="sig-name descname">termination_protection</code><a class="headerlink" href="#pulumi_aiven.Pg.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Pg.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Pg.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Pg.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Pg.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Project">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">Project</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_emails</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_cert</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">card_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">copy_from_project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country_code</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">technical_emails</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Project" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">myproject</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;myproject&quot;</span><span class="p">,</span>
    <span class="n">card_id</span><span class="o">=</span><span class="s2">&quot;&lt;FULL_CARD_ID/LAST4_DIGITS&gt;&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT_NAME&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account ID</p></li>
<li><p><strong>billing_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Billing name and address of the project</p></li>
<li><p><strong>billing_emails</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Billing contact emails of the project</p></li>
<li><p><strong>ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project root CA. This is used by some services like Kafka to sign service certificate</p></li>
<li><p><strong>card_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Credit card ID</p></li>
<li><p><strong>copy_from_project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Copy properties from another project. Only has effect when a new project is created.</p></li>
<li><p><strong>country_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Billing country code of the project</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project name</p></li>
<li><p><strong>technical_emails</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Technical contact emails of the project</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_aiven.Project.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_emails</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_cert</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">card_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">copy_from_project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country_code</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">technical_emails</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.project.Project<a class="headerlink" href="#pulumi_aiven.Project.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Project resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account ID</p></li>
<li><p><strong>billing_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Billing name and address of the project</p></li>
<li><p><strong>billing_emails</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Billing contact emails of the project</p></li>
<li><p><strong>ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project root CA. This is used by some services like Kafka to sign service certificate</p></li>
<li><p><strong>card_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Credit card ID</p></li>
<li><p><strong>copy_from_project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Copy properties from another project. Only has effect when a new project is created.</p></li>
<li><p><strong>country_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Billing country code of the project</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project name</p></li>
<li><p><strong>technical_emails</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Technical contact emails of the project</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Project.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_aiven.Project.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account ID</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Project.billing_address">
<em class="property">property </em><code class="sig-name descname">billing_address</code><a class="headerlink" href="#pulumi_aiven.Project.billing_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Billing name and address of the project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Project.billing_emails">
<em class="property">property </em><code class="sig-name descname">billing_emails</code><a class="headerlink" href="#pulumi_aiven.Project.billing_emails" title="Permalink to this definition">¶</a></dt>
<dd><p>Billing contact emails of the project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Project.ca_cert">
<em class="property">property </em><code class="sig-name descname">ca_cert</code><a class="headerlink" href="#pulumi_aiven.Project.ca_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>Project root CA. This is used by some services like Kafka to sign service certificate</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Project.card_id">
<em class="property">property </em><code class="sig-name descname">card_id</code><a class="headerlink" href="#pulumi_aiven.Project.card_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Credit card ID</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Project.copy_from_project">
<em class="property">property </em><code class="sig-name descname">copy_from_project</code><a class="headerlink" href="#pulumi_aiven.Project.copy_from_project" title="Permalink to this definition">¶</a></dt>
<dd><p>Copy properties from another project. Only has effect when a new project is created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Project.country_code">
<em class="property">property </em><code class="sig-name descname">country_code</code><a class="headerlink" href="#pulumi_aiven.Project.country_code" title="Permalink to this definition">¶</a></dt>
<dd><p>Billing country code of the project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Project.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.Project.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Project.technical_emails">
<em class="property">property </em><code class="sig-name descname">technical_emails</code><a class="headerlink" href="#pulumi_aiven.Project.technical_emails" title="Permalink to this definition">¶</a></dt>
<dd><p>Technical contact emails of the project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Project.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Project.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ProjectUser">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">ProjectUser</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ProjectUser" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">mytestuser</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">ProjectUser</span><span class="p">(</span><span class="s2">&quot;mytestuser&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;john.doe@example.com&quot;</span><span class="p">,</span>
    <span class="n">member_type</span><span class="o">=</span><span class="s2">&quot;admin&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">aiven_project</span><span class="p">[</span><span class="s2">&quot;myproject&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address of the user</p></li>
<li><p><strong>member_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project membership type. One of: admin, developer, operator</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project the user belongs to</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_aiven.ProjectUser.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accepted</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.project_user.ProjectUser<a class="headerlink" href="#pulumi_aiven.ProjectUser.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectUser resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accepted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user has accepted project membership or not</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address of the user</p></li>
<li><p><strong>member_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project membership type. One of: admin, developer, operator</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project the user belongs to</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ProjectUser.accepted">
<em class="property">property </em><code class="sig-name descname">accepted</code><a class="headerlink" href="#pulumi_aiven.ProjectUser.accepted" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user has accepted project membership or not</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ProjectUser.email">
<em class="property">property </em><code class="sig-name descname">email</code><a class="headerlink" href="#pulumi_aiven.ProjectUser.email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email address of the user</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ProjectUser.member_type">
<em class="property">property </em><code class="sig-name descname">member_type</code><a class="headerlink" href="#pulumi_aiven.ProjectUser.member_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Project membership type. One of: admin, developer, operator</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ProjectUser.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.ProjectUser.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project the user belongs to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ProjectUser.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ProjectUser.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ProjectUser.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ProjectUser.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ProjectVpc">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">ProjectVpc</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_cidr</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ProjectVpc" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">myvpc</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">ProjectVpc</span><span class="p">(</span><span class="s2">&quot;myvpc&quot;</span><span class="p">,</span>
    <span class="n">cloud_name</span><span class="o">=</span><span class="s2">&quot;google-europe-west1&quot;</span><span class="p">,</span>
    <span class="n">network_cidr</span><span class="o">=</span><span class="s2">&quot;192.168.0.1/24&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">aiven_project</span><span class="p">[</span><span class="s2">&quot;myproject&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud the VPC is in</p></li>
<li><p><strong>network_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network address range used by the VPC like 192.168.0.0/24</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project the VPC belongs to</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_aiven.ProjectVpc.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_cidr</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.project_vpc.ProjectVpc<a class="headerlink" href="#pulumi_aiven.ProjectVpc.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectVpc resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud the VPC is in</p></li>
<li><p><strong>network_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network address range used by the VPC like 192.168.0.0/24</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project the VPC belongs to</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – State of the VPC (APPROVED, ACTIVE, DELETING, DELETED)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ProjectVpc.cloud_name">
<em class="property">property </em><code class="sig-name descname">cloud_name</code><a class="headerlink" href="#pulumi_aiven.ProjectVpc.cloud_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud the VPC is in</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ProjectVpc.network_cidr">
<em class="property">property </em><code class="sig-name descname">network_cidr</code><a class="headerlink" href="#pulumi_aiven.ProjectVpc.network_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>Network address range used by the VPC like 192.168.0.0/24</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ProjectVpc.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.ProjectVpc.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project the VPC belongs to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ProjectVpc.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_aiven.ProjectVpc.state" title="Permalink to this definition">¶</a></dt>
<dd><p>State of the VPC (APPROVED, ACTIVE, DELETING, DELETED)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ProjectVpc.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ProjectVpc.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ProjectVpc.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ProjectVpc.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the aiven package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Aiven Authentication Token</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_aiven.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Redis">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">Redis</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis</span><span class="p">:</span> <span class="n">Union[RedisRedisArgs, Mapping[str, Any], Awaitable[Union[RedisRedisArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis_user_config</span><span class="p">:</span> <span class="n">Union[RedisRedisUserConfigArgs, Mapping[str, Any], Awaitable[Union[RedisRedisUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[RedisServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[RedisServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[RedisServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[RedisServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Redis" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Redis resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] cloud_name: Cloud the service runs in
:param pulumi.Input[str] maintenance_window_dow: Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.
:param pulumi.Input[str] maintenance_window_time: Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.
:param pulumi.Input[str] plan: Subscription plan
:param pulumi.Input[str] project: Target project
:param pulumi.Input[str] project_vpc_id: Identifier of the VPC the service should be in, if any
:param pulumi.Input[pulumi.InputType[‘RedisRedisArgs’]] redis: Redis server provided values
:param pulumi.Input[pulumi.InputType[‘RedisRedisUserConfigArgs’]] redis_user_config: Redis user configurable settings
:param pulumi.Input[List[pulumi.Input[pulumi.InputType[‘RedisServiceIntegrationArgs’]]]] service_integrations: Service integrations to specify when creating a service. Not applied after initial service creation
:param pulumi.Input[str] service_name: Service name
:param pulumi.Input[bool] termination_protection: Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
<dl class="py method">
<dt id="pulumi_aiven.Redis.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Union[List[Union[RedisComponentArgs, Mapping[str, Any], Awaitable[Union[RedisComponentArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[RedisComponentArgs, Mapping[str, Any], Awaitable[Union[RedisComponentArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis</span><span class="p">:</span> <span class="n">Union[RedisRedisArgs, Mapping[str, Any], Awaitable[Union[RedisRedisArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis_user_config</span><span class="p">:</span> <span class="n">Union[RedisRedisUserConfigArgs, Mapping[str, Any], Awaitable[Union[RedisRedisUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[RedisServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[RedisServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[RedisServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[RedisServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.redis.Redis<a class="headerlink" href="#pulumi_aiven.Redis.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Redis resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud the service runs in</p></li>
<li><p><strong>components</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RedisComponentArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service component information objects</p></li>
<li><p><strong>maintenance_window_dow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p></li>
<li><p><strong>maintenance_window_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subscription plan</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target project</p></li>
<li><p><strong>project_vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the VPC the service should be in, if any</p></li>
<li><p><strong>redis</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RedisRedisArgs'</em><em>]</em><em>]</em>) – Redis server provided values</p></li>
<li><p><strong>redis_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RedisRedisUserConfigArgs'</em><em>]</em><em>]</em>) – Redis user configurable settings</p></li>
<li><p><strong>service_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service hostname</p></li>
<li><p><strong>service_integrations</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RedisServiceIntegrationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service integrations to specify when creating a service. Not applied after initial service creation</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service name</p></li>
<li><p><strong>service_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password used for connecting to the service, if applicable</p></li>
<li><p><strong>service_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Service port</p></li>
<li><p><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Aiven internal service type code</p></li>
<li><p><strong>service_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p></li>
<li><p><strong>service_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username used for connecting to the service, if applicable</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service state</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Prevent service from being deleted. It is recommended to have this enabled for all services.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.cloud_name">
<em class="property">property </em><code class="sig-name descname">cloud_name</code><a class="headerlink" href="#pulumi_aiven.Redis.cloud_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud the service runs in</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.components">
<em class="property">property </em><code class="sig-name descname">components</code><a class="headerlink" href="#pulumi_aiven.Redis.components" title="Permalink to this definition">¶</a></dt>
<dd><p>Service component information objects</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.maintenance_window_dow">
<em class="property">property </em><code class="sig-name descname">maintenance_window_dow</code><a class="headerlink" href="#pulumi_aiven.Redis.maintenance_window_dow" title="Permalink to this definition">¶</a></dt>
<dd><p>Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.maintenance_window_time">
<em class="property">property </em><code class="sig-name descname">maintenance_window_time</code><a class="headerlink" href="#pulumi_aiven.Redis.maintenance_window_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.plan">
<em class="property">property </em><code class="sig-name descname">plan</code><a class="headerlink" href="#pulumi_aiven.Redis.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Subscription plan</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.Redis.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Target project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.project_vpc_id">
<em class="property">property </em><code class="sig-name descname">project_vpc_id</code><a class="headerlink" href="#pulumi_aiven.Redis.project_vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the VPC the service should be in, if any</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.redis">
<em class="property">property </em><code class="sig-name descname">redis</code><a class="headerlink" href="#pulumi_aiven.Redis.redis" title="Permalink to this definition">¶</a></dt>
<dd><p>Redis server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.redis_user_config">
<em class="property">property </em><code class="sig-name descname">redis_user_config</code><a class="headerlink" href="#pulumi_aiven.Redis.redis_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Redis user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.service_host">
<em class="property">property </em><code class="sig-name descname">service_host</code><a class="headerlink" href="#pulumi_aiven.Redis.service_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Service hostname</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.service_integrations">
<em class="property">property </em><code class="sig-name descname">service_integrations</code><a class="headerlink" href="#pulumi_aiven.Redis.service_integrations" title="Permalink to this definition">¶</a></dt>
<dd><p>Service integrations to specify when creating a service. Not applied after initial service creation</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.Redis.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.service_password">
<em class="property">property </em><code class="sig-name descname">service_password</code><a class="headerlink" href="#pulumi_aiven.Redis.service_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.service_port">
<em class="property">property </em><code class="sig-name descname">service_port</code><a class="headerlink" href="#pulumi_aiven.Redis.service_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Service port</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.service_type">
<em class="property">property </em><code class="sig-name descname">service_type</code><a class="headerlink" href="#pulumi_aiven.Redis.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Aiven internal service type code</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.service_uri">
<em class="property">property </em><code class="sig-name descname">service_uri</code><a class="headerlink" href="#pulumi_aiven.Redis.service_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.service_username">
<em class="property">property </em><code class="sig-name descname">service_username</code><a class="headerlink" href="#pulumi_aiven.Redis.service_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_aiven.Redis.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Service state</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.termination_protection">
<em class="property">property </em><code class="sig-name descname">termination_protection</code><a class="headerlink" href="#pulumi_aiven.Redis.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Redis.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Redis.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Redis.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Redis.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Service">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">Service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cassandra</span><span class="p">:</span> <span class="n">Union[ServiceCassandraArgs, Mapping[str, Any], Awaitable[Union[ServiceCassandraArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cassandra_user_config</span><span class="p">:</span> <span class="n">Union[ServiceCassandraUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceCassandraUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch</span><span class="p">:</span> <span class="n">Union[ServiceElasticsearchArgs, Mapping[str, Any], Awaitable[Union[ServiceElasticsearchArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch_user_config</span><span class="p">:</span> <span class="n">Union[ServiceElasticsearchUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceElasticsearchUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana</span><span class="p">:</span> <span class="n">Union[ServiceGrafanaArgs, Mapping[str, Any], Awaitable[Union[ServiceGrafanaArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana_user_config</span><span class="p">:</span> <span class="n">Union[ServiceGrafanaUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceGrafanaUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb</span><span class="p">:</span> <span class="n">Union[ServiceInfluxdbArgs, Mapping[str, Any], Awaitable[Union[ServiceInfluxdbArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb_user_config</span><span class="p">:</span> <span class="n">Union[ServiceInfluxdbUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceInfluxdbUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka</span><span class="p">:</span> <span class="n">Union[ServiceKafkaArgs, Mapping[str, Any], Awaitable[Union[ServiceKafkaArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect</span><span class="p">:</span> <span class="n">Union[ServiceKafkaConnectArgs, Mapping[str, Any], Awaitable[Union[ServiceKafkaConnectArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect_user_config</span><span class="p">:</span> <span class="n">Union[ServiceKafkaConnectUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceKafkaConnectUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker</span><span class="p">:</span> <span class="n">Union[ServiceKafkaMirrormakerArgs, Mapping[str, Any], Awaitable[Union[ServiceKafkaMirrormakerArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker_user_config</span><span class="p">:</span> <span class="n">Union[ServiceKafkaMirrormakerUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceKafkaMirrormakerUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_user_config</span><span class="p">:</span> <span class="n">Union[ServiceKafkaUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceKafkaUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql</span><span class="p">:</span> <span class="n">Union[ServiceMysqlArgs, Mapping[str, Any], Awaitable[Union[ServiceMysqlArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql_user_config</span><span class="p">:</span> <span class="n">Union[ServiceMysqlUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceMysqlUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg</span><span class="p">:</span> <span class="n">Union[ServicePgArgs, Mapping[str, Any], Awaitable[Union[ServicePgArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg_user_config</span><span class="p">:</span> <span class="n">Union[ServicePgUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServicePgUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis</span><span class="p">:</span> <span class="n">Union[ServiceRedisArgs, Mapping[str, Any], Awaitable[Union[ServiceRedisArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis_user_config</span><span class="p">:</span> <span class="n">Union[ServiceRedisUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceRedisUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[ServiceServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[ServiceServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ServiceServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[ServiceServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Service" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">myservice</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">Service</span><span class="p">(</span><span class="s2">&quot;myservice&quot;</span><span class="p">,</span>
    <span class="n">cloud_name</span><span class="o">=</span><span class="s2">&quot;google-europe-west1&quot;</span><span class="p">,</span>
    <span class="n">pg_user_config</span><span class="o">=</span><span class="n">aiven</span><span class="o">.</span><span class="n">ServicePgUserConfigArgs</span><span class="p">(</span>
        <span class="n">ip_filters</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;0.0.0.0/0&quot;</span><span class="p">],</span>
        <span class="n">pg_version</span><span class="o">=</span><span class="s2">&quot;10&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">plan</span><span class="o">=</span><span class="s2">&quot;business-8&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">aiven_project</span><span class="p">[</span><span class="s2">&quot;myproject&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">project_vpc_id</span><span class="o">=</span><span class="n">aiven_project_vpc</span><span class="p">[</span><span class="s2">&quot;vpc_gcp_europe_west1&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">service_name</span><span class="o">=</span><span class="s2">&quot;&lt;SERVICE_NAME&gt;&quot;</span><span class="p">,</span>
    <span class="n">service_type</span><span class="o">=</span><span class="s2">&quot;pg&quot;</span><span class="p">,</span>
    <span class="n">termination_protection</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cassandra</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceCassandraArgs'</em><em>]</em><em>]</em>) – Cassandra specific server provided values</p></li>
<li><p><strong>cassandra_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceCassandraUserConfigArgs'</em><em>]</em><em>]</em>) – Cassandra specific user configurable settings</p></li>
<li><p><strong>cloud_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud the service runs in</p></li>
<li><p><strong>elasticsearch</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceElasticsearchArgs'</em><em>]</em><em>]</em>) – Elasticsearch specific server provided values</p></li>
<li><p><strong>elasticsearch_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceElasticsearchUserConfigArgs'</em><em>]</em><em>]</em>) – Elasticsearch specific user configurable settings</p></li>
<li><p><strong>grafana</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceGrafanaArgs'</em><em>]</em><em>]</em>) – Grafana specific server provided values</p></li>
<li><p><strong>grafana_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceGrafanaUserConfigArgs'</em><em>]</em><em>]</em>) – Grafana specific user configurable settings</p></li>
<li><p><strong>influxdb</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceInfluxdbArgs'</em><em>]</em><em>]</em>) – InfluxDB specific server provided values</p></li>
<li><p><strong>influxdb_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceInfluxdbUserConfigArgs'</em><em>]</em><em>]</em>) – InfluxDB specific user configurable settings</p></li>
<li><p><strong>kafka</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceKafkaArgs'</em><em>]</em><em>]</em>) – Kafka specific server provided values</p></li>
<li><p><strong>kafka_connect</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceKafkaConnectArgs'</em><em>]</em><em>]</em>) – Kafka Connect specific server provided values</p></li>
<li><p><strong>kafka_connect_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceKafkaConnectUserConfigArgs'</em><em>]</em><em>]</em>) – Kafka Connect specific user configurable settings</p></li>
<li><p><strong>kafka_mirrormaker</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceKafkaMirrormakerArgs'</em><em>]</em><em>]</em>) – Kafka MirrorMaker 2 specific server provided values</p></li>
<li><p><strong>kafka_mirrormaker_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceKafkaMirrormakerUserConfigArgs'</em><em>]</em><em>]</em>) – Kafka MirrorMaker 2 specific user configurable settings</p></li>
<li><p><strong>kafka_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceKafkaUserConfigArgs'</em><em>]</em><em>]</em>) – Kafka specific user configurable settings</p></li>
<li><p><strong>maintenance_window_dow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p></li>
<li><p><strong>maintenance_window_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p></li>
<li><p><strong>mysql</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceMysqlArgs'</em><em>]</em><em>]</em>) – MySQL specific server provided values</p></li>
<li><p><strong>mysql_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceMysqlUserConfigArgs'</em><em>]</em><em>]</em>) – MySQL specific user configurable settings</p></li>
<li><p><strong>pg</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServicePgArgs'</em><em>]</em><em>]</em>) – PostgreSQL specific server provided values</p></li>
<li><p><strong>pg_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServicePgUserConfigArgs'</em><em>]</em><em>]</em>) – PostgreSQL specific user configurable settings</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subscription plan</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target project</p></li>
<li><p><strong>project_vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the VPC the service should be in, if any</p></li>
<li><p><strong>redis</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceRedisArgs'</em><em>]</em><em>]</em>) – Redis specific server provided values</p></li>
<li><p><strong>redis_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceRedisUserConfigArgs'</em><em>]</em><em>]</em>) – Redis specific user configurable settings</p></li>
<li><p><strong>service_integrations</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceServiceIntegrationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service integrations to specify when creating a service. Not applied after initial service creation</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service name</p></li>
<li><p><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service type code</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Prevent service from being deleted. It is recommended to have this enabled for all services.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_aiven.Service.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cassandra</span><span class="p">:</span> <span class="n">Union[ServiceCassandraArgs, Mapping[str, Any], Awaitable[Union[ServiceCassandraArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cassandra_user_config</span><span class="p">:</span> <span class="n">Union[ServiceCassandraUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceCassandraUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Union[List[Union[ServiceComponentArgs, Mapping[str, Any], Awaitable[Union[ServiceComponentArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ServiceComponentArgs, Mapping[str, Any], Awaitable[Union[ServiceComponentArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch</span><span class="p">:</span> <span class="n">Union[ServiceElasticsearchArgs, Mapping[str, Any], Awaitable[Union[ServiceElasticsearchArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch_user_config</span><span class="p">:</span> <span class="n">Union[ServiceElasticsearchUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceElasticsearchUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana</span><span class="p">:</span> <span class="n">Union[ServiceGrafanaArgs, Mapping[str, Any], Awaitable[Union[ServiceGrafanaArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana_user_config</span><span class="p">:</span> <span class="n">Union[ServiceGrafanaUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceGrafanaUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb</span><span class="p">:</span> <span class="n">Union[ServiceInfluxdbArgs, Mapping[str, Any], Awaitable[Union[ServiceInfluxdbArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb_user_config</span><span class="p">:</span> <span class="n">Union[ServiceInfluxdbUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceInfluxdbUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka</span><span class="p">:</span> <span class="n">Union[ServiceKafkaArgs, Mapping[str, Any], Awaitable[Union[ServiceKafkaArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect</span><span class="p">:</span> <span class="n">Union[ServiceKafkaConnectArgs, Mapping[str, Any], Awaitable[Union[ServiceKafkaConnectArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect_user_config</span><span class="p">:</span> <span class="n">Union[ServiceKafkaConnectUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceKafkaConnectUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker</span><span class="p">:</span> <span class="n">Union[ServiceKafkaMirrormakerArgs, Mapping[str, Any], Awaitable[Union[ServiceKafkaMirrormakerArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker_user_config</span><span class="p">:</span> <span class="n">Union[ServiceKafkaMirrormakerUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceKafkaMirrormakerUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_user_config</span><span class="p">:</span> <span class="n">Union[ServiceKafkaUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceKafkaUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql</span><span class="p">:</span> <span class="n">Union[ServiceMysqlArgs, Mapping[str, Any], Awaitable[Union[ServiceMysqlArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql_user_config</span><span class="p">:</span> <span class="n">Union[ServiceMysqlUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceMysqlUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg</span><span class="p">:</span> <span class="n">Union[ServicePgArgs, Mapping[str, Any], Awaitable[Union[ServicePgArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg_user_config</span><span class="p">:</span> <span class="n">Union[ServicePgUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServicePgUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis</span><span class="p">:</span> <span class="n">Union[ServiceRedisArgs, Mapping[str, Any], Awaitable[Union[ServiceRedisArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis_user_config</span><span class="p">:</span> <span class="n">Union[ServiceRedisUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceRedisUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Union[List[Union[ServiceServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[ServiceServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ServiceServiceIntegrationArgs, Mapping[str, Any], Awaitable[Union[ServiceServiceIntegrationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.service.Service<a class="headerlink" href="#pulumi_aiven.Service.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Service resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cassandra</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceCassandraArgs'</em><em>]</em><em>]</em>) – Cassandra specific server provided values</p></li>
<li><p><strong>cassandra_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceCassandraUserConfigArgs'</em><em>]</em><em>]</em>) – Cassandra specific user configurable settings</p></li>
<li><p><strong>cloud_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud the service runs in</p></li>
<li><p><strong>components</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceComponentArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service component information objects</p></li>
<li><p><strong>elasticsearch</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceElasticsearchArgs'</em><em>]</em><em>]</em>) – Elasticsearch specific server provided values</p></li>
<li><p><strong>elasticsearch_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceElasticsearchUserConfigArgs'</em><em>]</em><em>]</em>) – Elasticsearch specific user configurable settings</p></li>
<li><p><strong>grafana</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceGrafanaArgs'</em><em>]</em><em>]</em>) – Grafana specific server provided values</p></li>
<li><p><strong>grafana_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceGrafanaUserConfigArgs'</em><em>]</em><em>]</em>) – Grafana specific user configurable settings</p></li>
<li><p><strong>influxdb</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceInfluxdbArgs'</em><em>]</em><em>]</em>) – InfluxDB specific server provided values</p></li>
<li><p><strong>influxdb_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceInfluxdbUserConfigArgs'</em><em>]</em><em>]</em>) – InfluxDB specific user configurable settings</p></li>
<li><p><strong>kafka</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceKafkaArgs'</em><em>]</em><em>]</em>) – Kafka specific server provided values</p></li>
<li><p><strong>kafka_connect</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceKafkaConnectArgs'</em><em>]</em><em>]</em>) – Kafka Connect specific server provided values</p></li>
<li><p><strong>kafka_connect_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceKafkaConnectUserConfigArgs'</em><em>]</em><em>]</em>) – Kafka Connect specific user configurable settings</p></li>
<li><p><strong>kafka_mirrormaker</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceKafkaMirrormakerArgs'</em><em>]</em><em>]</em>) – Kafka MirrorMaker 2 specific server provided values</p></li>
<li><p><strong>kafka_mirrormaker_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceKafkaMirrormakerUserConfigArgs'</em><em>]</em><em>]</em>) – Kafka MirrorMaker 2 specific user configurable settings</p></li>
<li><p><strong>kafka_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceKafkaUserConfigArgs'</em><em>]</em><em>]</em>) – Kafka specific user configurable settings</p></li>
<li><p><strong>maintenance_window_dow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p></li>
<li><p><strong>maintenance_window_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p></li>
<li><p><strong>mysql</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceMysqlArgs'</em><em>]</em><em>]</em>) – MySQL specific server provided values</p></li>
<li><p><strong>mysql_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceMysqlUserConfigArgs'</em><em>]</em><em>]</em>) – MySQL specific user configurable settings</p></li>
<li><p><strong>pg</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServicePgArgs'</em><em>]</em><em>]</em>) – PostgreSQL specific server provided values</p></li>
<li><p><strong>pg_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServicePgUserConfigArgs'</em><em>]</em><em>]</em>) – PostgreSQL specific user configurable settings</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subscription plan</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target project</p></li>
<li><p><strong>project_vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the VPC the service should be in, if any</p></li>
<li><p><strong>redis</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceRedisArgs'</em><em>]</em><em>]</em>) – Redis specific server provided values</p></li>
<li><p><strong>redis_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceRedisUserConfigArgs'</em><em>]</em><em>]</em>) – Redis specific user configurable settings</p></li>
<li><p><strong>service_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service hostname</p></li>
<li><p><strong>service_integrations</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceServiceIntegrationArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Service integrations to specify when creating a service. Not applied after initial service creation</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service name</p></li>
<li><p><strong>service_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password used for connecting to the service, if applicable</p></li>
<li><p><strong>service_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Service port</p></li>
<li><p><strong>service_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service type code</p></li>
<li><p><strong>service_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p></li>
<li><p><strong>service_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username used for connecting to the service, if applicable</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service state</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Prevent service from being deleted. It is recommended to have this enabled for all services.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.cassandra">
<em class="property">property </em><code class="sig-name descname">cassandra</code><a class="headerlink" href="#pulumi_aiven.Service.cassandra" title="Permalink to this definition">¶</a></dt>
<dd><p>Cassandra specific server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.cassandra_user_config">
<em class="property">property </em><code class="sig-name descname">cassandra_user_config</code><a class="headerlink" href="#pulumi_aiven.Service.cassandra_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Cassandra specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.cloud_name">
<em class="property">property </em><code class="sig-name descname">cloud_name</code><a class="headerlink" href="#pulumi_aiven.Service.cloud_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud the service runs in</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.components">
<em class="property">property </em><code class="sig-name descname">components</code><a class="headerlink" href="#pulumi_aiven.Service.components" title="Permalink to this definition">¶</a></dt>
<dd><p>Service component information objects</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.elasticsearch">
<em class="property">property </em><code class="sig-name descname">elasticsearch</code><a class="headerlink" href="#pulumi_aiven.Service.elasticsearch" title="Permalink to this definition">¶</a></dt>
<dd><p>Elasticsearch specific server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.elasticsearch_user_config">
<em class="property">property </em><code class="sig-name descname">elasticsearch_user_config</code><a class="headerlink" href="#pulumi_aiven.Service.elasticsearch_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Elasticsearch specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.grafana">
<em class="property">property </em><code class="sig-name descname">grafana</code><a class="headerlink" href="#pulumi_aiven.Service.grafana" title="Permalink to this definition">¶</a></dt>
<dd><p>Grafana specific server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.grafana_user_config">
<em class="property">property </em><code class="sig-name descname">grafana_user_config</code><a class="headerlink" href="#pulumi_aiven.Service.grafana_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Grafana specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.influxdb">
<em class="property">property </em><code class="sig-name descname">influxdb</code><a class="headerlink" href="#pulumi_aiven.Service.influxdb" title="Permalink to this definition">¶</a></dt>
<dd><p>InfluxDB specific server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.influxdb_user_config">
<em class="property">property </em><code class="sig-name descname">influxdb_user_config</code><a class="headerlink" href="#pulumi_aiven.Service.influxdb_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>InfluxDB specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.kafka">
<em class="property">property </em><code class="sig-name descname">kafka</code><a class="headerlink" href="#pulumi_aiven.Service.kafka" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka specific server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.kafka_connect">
<em class="property">property </em><code class="sig-name descname">kafka_connect</code><a class="headerlink" href="#pulumi_aiven.Service.kafka_connect" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka Connect specific server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.kafka_connect_user_config">
<em class="property">property </em><code class="sig-name descname">kafka_connect_user_config</code><a class="headerlink" href="#pulumi_aiven.Service.kafka_connect_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka Connect specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.kafka_mirrormaker">
<em class="property">property </em><code class="sig-name descname">kafka_mirrormaker</code><a class="headerlink" href="#pulumi_aiven.Service.kafka_mirrormaker" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka MirrorMaker 2 specific server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.kafka_mirrormaker_user_config">
<em class="property">property </em><code class="sig-name descname">kafka_mirrormaker_user_config</code><a class="headerlink" href="#pulumi_aiven.Service.kafka_mirrormaker_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka MirrorMaker 2 specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.kafka_user_config">
<em class="property">property </em><code class="sig-name descname">kafka_user_config</code><a class="headerlink" href="#pulumi_aiven.Service.kafka_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.maintenance_window_dow">
<em class="property">property </em><code class="sig-name descname">maintenance_window_dow</code><a class="headerlink" href="#pulumi_aiven.Service.maintenance_window_dow" title="Permalink to this definition">¶</a></dt>
<dd><p>Day of week when maintenance operations should be performed. One monday, tuesday, wednesday, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.maintenance_window_time">
<em class="property">property </em><code class="sig-name descname">maintenance_window_time</code><a class="headerlink" href="#pulumi_aiven.Service.maintenance_window_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Time of day when maintenance operations should be performed. UTC time in HH:mm:ss format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.mysql">
<em class="property">property </em><code class="sig-name descname">mysql</code><a class="headerlink" href="#pulumi_aiven.Service.mysql" title="Permalink to this definition">¶</a></dt>
<dd><p>MySQL specific server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.mysql_user_config">
<em class="property">property </em><code class="sig-name descname">mysql_user_config</code><a class="headerlink" href="#pulumi_aiven.Service.mysql_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>MySQL specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.pg">
<em class="property">property </em><code class="sig-name descname">pg</code><a class="headerlink" href="#pulumi_aiven.Service.pg" title="Permalink to this definition">¶</a></dt>
<dd><p>PostgreSQL specific server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.pg_user_config">
<em class="property">property </em><code class="sig-name descname">pg_user_config</code><a class="headerlink" href="#pulumi_aiven.Service.pg_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>PostgreSQL specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.plan">
<em class="property">property </em><code class="sig-name descname">plan</code><a class="headerlink" href="#pulumi_aiven.Service.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Subscription plan</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.Service.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Target project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.project_vpc_id">
<em class="property">property </em><code class="sig-name descname">project_vpc_id</code><a class="headerlink" href="#pulumi_aiven.Service.project_vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the VPC the service should be in, if any</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.redis">
<em class="property">property </em><code class="sig-name descname">redis</code><a class="headerlink" href="#pulumi_aiven.Service.redis" title="Permalink to this definition">¶</a></dt>
<dd><p>Redis specific server provided values</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.redis_user_config">
<em class="property">property </em><code class="sig-name descname">redis_user_config</code><a class="headerlink" href="#pulumi_aiven.Service.redis_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Redis specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.service_host">
<em class="property">property </em><code class="sig-name descname">service_host</code><a class="headerlink" href="#pulumi_aiven.Service.service_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Service hostname</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.service_integrations">
<em class="property">property </em><code class="sig-name descname">service_integrations</code><a class="headerlink" href="#pulumi_aiven.Service.service_integrations" title="Permalink to this definition">¶</a></dt>
<dd><p>Service integrations to specify when creating a service. Not applied after initial service creation</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.Service.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.service_password">
<em class="property">property </em><code class="sig-name descname">service_password</code><a class="headerlink" href="#pulumi_aiven.Service.service_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.service_port">
<em class="property">property </em><code class="sig-name descname">service_port</code><a class="headerlink" href="#pulumi_aiven.Service.service_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Service port</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.service_type">
<em class="property">property </em><code class="sig-name descname">service_type</code><a class="headerlink" href="#pulumi_aiven.Service.service_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Service type code</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.service_uri">
<em class="property">property </em><code class="sig-name descname">service_uri</code><a class="headerlink" href="#pulumi_aiven.Service.service_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI for connecting to the service. Service specific info is under “kafka”, “pg”, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.service_username">
<em class="property">property </em><code class="sig-name descname">service_username</code><a class="headerlink" href="#pulumi_aiven.Service.service_username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username used for connecting to the service, if applicable</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_aiven.Service.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Service state</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.termination_protection">
<em class="property">property </em><code class="sig-name descname">termination_protection</code><a class="headerlink" href="#pulumi_aiven.Service.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Prevent service from being deleted. It is recommended to have this enabled for all services.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.Service.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.Service.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ServiceIntegration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">ServiceIntegration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_endpoint_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect_user_config</span><span class="p">:</span> <span class="n">Union[ServiceIntegrationKafkaConnectUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceIntegrationKafkaConnectUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker_user_config</span><span class="p">:</span> <span class="n">Union[ServiceIntegrationKafkaMirrormakerUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceIntegrationKafkaMirrormakerUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs_user_config</span><span class="p">:</span> <span class="n">Union[ServiceIntegrationLogsUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceIntegrationLogsUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mirrormaker_user_config</span><span class="p">:</span> <span class="n">Union[ServiceIntegrationMirrormakerUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceIntegrationMirrormakerUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_endpoint_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceIntegration" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">myintegration</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">ServiceIntegration</span><span class="p">(</span><span class="s2">&quot;myintegration&quot;</span><span class="p">,</span>
    <span class="n">destination_endpoint_id</span><span class="o">=</span><span class="n">aiven_service_integration_endpoint</span><span class="p">[</span><span class="s2">&quot;myendpoint&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">destination_service_name</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
    <span class="n">integration_type</span><span class="o">=</span><span class="s2">&quot;datadog&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">aiven_project</span><span class="p">[</span><span class="s2">&quot;myproject&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">source_endpoint_id</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
    <span class="n">source_service_name</span><span class="o">=</span><span class="n">aiven_service</span><span class="p">[</span><span class="s2">&quot;testkafka&quot;</span><span class="p">][</span><span class="s2">&quot;service_name&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination endpoint for the integration (if any)</p></li>
<li><p><strong>destination_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination service for the integration (if any)</p></li>
<li><p><strong>integration_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the service integration</p></li>
<li><p><strong>kafka_connect_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceIntegrationKafkaConnectUserConfigArgs'</em><em>]</em><em>]</em>) – Kafka Connect specific user configurable settings</p></li>
<li><p><strong>kafka_mirrormaker_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceIntegrationKafkaMirrormakerUserConfigArgs'</em><em>]</em><em>]</em>) – Mirrormaker 2 integration specific user configurable settings</p></li>
<li><p><strong>logs_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceIntegrationLogsUserConfigArgs'</em><em>]</em><em>]</em>) – Log integration specific user configurable settings</p></li>
<li><p><strong>mirrormaker_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceIntegrationMirrormakerUserConfigArgs'</em><em>]</em><em>]</em>) – Mirrormaker 1 integration specific user configurable settings</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project the integration belongs to</p></li>
<li><p><strong>source_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Source endpoint for the integration (if any)</p></li>
<li><p><strong>source_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Source service for the integration (if any)</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_endpoint_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect_user_config</span><span class="p">:</span> <span class="n">Union[ServiceIntegrationKafkaConnectUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceIntegrationKafkaConnectUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker_user_config</span><span class="p">:</span> <span class="n">Union[ServiceIntegrationKafkaMirrormakerUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceIntegrationKafkaMirrormakerUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs_user_config</span><span class="p">:</span> <span class="n">Union[ServiceIntegrationLogsUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceIntegrationLogsUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mirrormaker_user_config</span><span class="p">:</span> <span class="n">Union[ServiceIntegrationMirrormakerUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceIntegrationMirrormakerUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_endpoint_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.service_integration.ServiceIntegration<a class="headerlink" href="#pulumi_aiven.ServiceIntegration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceIntegration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination endpoint for the integration (if any)</p></li>
<li><p><strong>destination_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination service for the integration (if any)</p></li>
<li><p><strong>integration_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the service integration</p></li>
<li><p><strong>kafka_connect_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceIntegrationKafkaConnectUserConfigArgs'</em><em>]</em><em>]</em>) – Kafka Connect specific user configurable settings</p></li>
<li><p><strong>kafka_mirrormaker_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceIntegrationKafkaMirrormakerUserConfigArgs'</em><em>]</em><em>]</em>) – Mirrormaker 2 integration specific user configurable settings</p></li>
<li><p><strong>logs_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceIntegrationLogsUserConfigArgs'</em><em>]</em><em>]</em>) – Log integration specific user configurable settings</p></li>
<li><p><strong>mirrormaker_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceIntegrationMirrormakerUserConfigArgs'</em><em>]</em><em>]</em>) – Mirrormaker 1 integration specific user configurable settings</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project the integration belongs to</p></li>
<li><p><strong>source_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Source endpoint for the integration (if any)</p></li>
<li><p><strong>source_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Source service for the integration (if any)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegration.destination_endpoint_id">
<em class="property">property </em><code class="sig-name descname">destination_endpoint_id</code><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.destination_endpoint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Destination endpoint for the integration (if any)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegration.destination_service_name">
<em class="property">property </em><code class="sig-name descname">destination_service_name</code><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.destination_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Destination service for the integration (if any)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegration.integration_type">
<em class="property">property </em><code class="sig-name descname">integration_type</code><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.integration_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the service integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegration.kafka_connect_user_config">
<em class="property">property </em><code class="sig-name descname">kafka_connect_user_config</code><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.kafka_connect_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Kafka Connect specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegration.kafka_mirrormaker_user_config">
<em class="property">property </em><code class="sig-name descname">kafka_mirrormaker_user_config</code><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.kafka_mirrormaker_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Mirrormaker 2 integration specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegration.logs_user_config">
<em class="property">property </em><code class="sig-name descname">logs_user_config</code><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.logs_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Log integration specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegration.mirrormaker_user_config">
<em class="property">property </em><code class="sig-name descname">mirrormaker_user_config</code><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.mirrormaker_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Mirrormaker 1 integration specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegration.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project the integration belongs to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegration.source_endpoint_id">
<em class="property">property </em><code class="sig-name descname">source_endpoint_id</code><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.source_endpoint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Source endpoint for the integration (if any)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegration.source_service_name">
<em class="property">property </em><code class="sig-name descname">source_service_name</code><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.source_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Source service for the integration (if any)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ServiceIntegration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceIntegration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ServiceIntegrationEndpoint">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">ServiceIntegrationEndpoint</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datadog_user_config</span><span class="p">:</span> <span class="n">Union[ServiceIntegrationEndpointDatadogUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceIntegrationEndpointDatadogUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_elasticsearch_logs_user_config</span><span class="p">:</span> <span class="n">Union[ServiceIntegrationEndpointExternalElasticsearchLogsUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceIntegrationEndpointExternalElasticsearchLogsUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prometheus_user_config</span><span class="p">:</span> <span class="n">Union[ServiceIntegrationEndpointPrometheusUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceIntegrationEndpointPrometheusUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rsyslog_user_config</span><span class="p">:</span> <span class="n">Union[ServiceIntegrationEndpointRsyslogUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceIntegrationEndpointRsyslogUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">myendpoint</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">ServiceIntegrationEndpoint</span><span class="p">(</span><span class="s2">&quot;myendpoint&quot;</span><span class="p">,</span>
    <span class="n">datadog_user_config</span><span class="o">=</span><span class="n">aiven</span><span class="o">.</span><span class="n">ServiceIntegrationEndpointDatadogUserConfigArgs</span><span class="p">(</span>
        <span class="n">datadog_api_key</span><span class="o">=</span><span class="s2">&quot;&lt;DATADOG_API_KEY&gt;&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">endpoint_name</span><span class="o">=</span><span class="s2">&quot;&lt;ENDPOINT_NAME&gt;&quot;</span><span class="p">,</span>
    <span class="n">endpoint_type</span><span class="o">=</span><span class="s2">&quot;datadog&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">aiven_project</span><span class="p">[</span><span class="s2">&quot;myproject&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>datadog_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceIntegrationEndpointDatadogUserConfigArgs'</em><em>]</em><em>]</em>) – Datadog specific user configurable settings</p></li>
<li><p><strong>endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the service integration endpoint</p></li>
<li><p><strong>endpoint_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the service integration endpoint</p></li>
<li><p><strong>external_elasticsearch_logs_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceIntegrationEndpointExternalElasticsearchLogsUserConfigArgs'</em><em>]</em><em>]</em>) – external elasticsearch specific user configurable settings</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project the service integration endpoint belongs to</p></li>
<li><p><strong>prometheus_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceIntegrationEndpointPrometheusUserConfigArgs'</em><em>]</em><em>]</em>) – Prometheus specific user configurable settings</p></li>
<li><p><strong>rsyslog_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceIntegrationEndpointRsyslogUserConfigArgs'</em><em>]</em><em>]</em>) – rsyslog specific user configurable settings</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datadog_user_config</span><span class="p">:</span> <span class="n">Union[ServiceIntegrationEndpointDatadogUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceIntegrationEndpointDatadogUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_elasticsearch_logs_user_config</span><span class="p">:</span> <span class="n">Union[ServiceIntegrationEndpointExternalElasticsearchLogsUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceIntegrationEndpointExternalElasticsearchLogsUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prometheus_user_config</span><span class="p">:</span> <span class="n">Union[ServiceIntegrationEndpointPrometheusUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceIntegrationEndpointPrometheusUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rsyslog_user_config</span><span class="p">:</span> <span class="n">Union[ServiceIntegrationEndpointRsyslogUserConfigArgs, Mapping[str, Any], Awaitable[Union[ServiceIntegrationEndpointRsyslogUserConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.service_integration_endpoint.ServiceIntegrationEndpoint<a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceIntegrationEndpoint resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>datadog_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceIntegrationEndpointDatadogUserConfigArgs'</em><em>]</em><em>]</em>) – Datadog specific user configurable settings</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>endpoint_config</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Integration endpoint specific backend configuration</p></li>
<li><p><strong>endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the service integration endpoint</p></li>
<li><p><strong>endpoint_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the service integration endpoint</p></li>
<li><p><strong>external_elasticsearch_logs_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceIntegrationEndpointExternalElasticsearchLogsUserConfigArgs'</em><em>]</em><em>]</em>) – external elasticsearch specific user configurable settings</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project the service integration endpoint belongs to</p></li>
<li><p><strong>prometheus_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceIntegrationEndpointPrometheusUserConfigArgs'</em><em>]</em><em>]</em>) – Prometheus specific user configurable settings</p></li>
<li><p><strong>rsyslog_user_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceIntegrationEndpointRsyslogUserConfigArgs'</em><em>]</em><em>]</em>) – rsyslog specific user configurable settings</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.datadog_user_config">
<em class="property">property </em><code class="sig-name descname">datadog_user_config</code><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.datadog_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Datadog specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.endpoint_config">
<em class="property">property </em><code class="sig-name descname">endpoint_config</code><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.endpoint_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Integration endpoint specific backend configuration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.endpoint_name">
<em class="property">property </em><code class="sig-name descname">endpoint_name</code><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.endpoint_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the service integration endpoint</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.endpoint_type">
<em class="property">property </em><code class="sig-name descname">endpoint_type</code><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.endpoint_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the service integration endpoint</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.external_elasticsearch_logs_user_config">
<em class="property">property </em><code class="sig-name descname">external_elasticsearch_logs_user_config</code><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.external_elasticsearch_logs_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>external elasticsearch specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project the service integration endpoint belongs to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.prometheus_user_config">
<em class="property">property </em><code class="sig-name descname">prometheus_user_config</code><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.prometheus_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Prometheus specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.rsyslog_user_config">
<em class="property">property </em><code class="sig-name descname">rsyslog_user_config</code><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.rsyslog_user_config" title="Permalink to this definition">¶</a></dt>
<dd><p>rsyslog specific user configurable settings</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ServiceIntegrationEndpoint.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceIntegrationEndpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ServiceUser">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">ServiceUser</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceUser" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">myserviceuser</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">ServiceUser</span><span class="p">(</span><span class="s2">&quot;myserviceuser&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">aiven_project</span><span class="p">[</span><span class="s2">&quot;myproject&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">service_name</span><span class="o">=</span><span class="n">aiven_service</span><span class="p">[</span><span class="s2">&quot;myservice&quot;</span><span class="p">][</span><span class="s2">&quot;service_name&quot;</span><span class="p">],</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;&lt;USERNAME&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the user to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the user to</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the user account</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_aiven.ServiceUser.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_cert</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.service_user.ServiceUser<a class="headerlink" href="#pulumi_aiven.ServiceUser.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceUser resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access certificate for the user if applicable for the service in question</p></li>
<li><p><strong>access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Access certificate key for the user if applicable for the service in question</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password of the user</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project to link the user to</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service to link the user to</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the user account</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the user account</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceUser.access_cert">
<em class="property">property </em><code class="sig-name descname">access_cert</code><a class="headerlink" href="#pulumi_aiven.ServiceUser.access_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>Access certificate for the user if applicable for the service in question</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceUser.access_key">
<em class="property">property </em><code class="sig-name descname">access_key</code><a class="headerlink" href="#pulumi_aiven.ServiceUser.access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Access certificate key for the user if applicable for the service in question</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceUser.password">
<em class="property">property </em><code class="sig-name descname">password</code><a class="headerlink" href="#pulumi_aiven.ServiceUser.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password of the user</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceUser.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_aiven.ServiceUser.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project to link the user to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceUser.service_name">
<em class="property">property </em><code class="sig-name descname">service_name</code><a class="headerlink" href="#pulumi_aiven.ServiceUser.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Service to link the user to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceUser.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_aiven.ServiceUser.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the user account</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceUser.username">
<em class="property">property </em><code class="sig-name descname">username</code><a class="headerlink" href="#pulumi_aiven.ServiceUser.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the user account</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.ServiceUser.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceUser.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.ServiceUser.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.ServiceUser.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.TransitGatewayVpcAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">TransitGatewayVpcAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_cloud_account</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_vpc</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_peer_network_cidrs</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.TransitGatewayVpcAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a TransitGatewayVpcAttachment resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] peer_cloud_account: AWS account ID or GCP project ID of the peered VPC
:param pulumi.Input[str] peer_region: AWS region of the peered VPC (if not in the same region as Aiven VPC)
:param pulumi.Input[str] peer_vpc: Transit gateway ID
:param pulumi.Input[List[pulumi.Input[str]]] user_peer_network_cidrs: List of private IPv4 ranges to route through the peering connection
:param pulumi.Input[str] vpc_id: The VPC the peering connection belongs to</p>
<dl class="py method">
<dt id="pulumi_aiven.TransitGatewayVpcAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_cloud_account</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_vpc</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peering_connection_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state_info</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_peer_network_cidrs</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.transit_gateway_vpc_attachment.TransitGatewayVpcAttachment<a class="headerlink" href="#pulumi_aiven.TransitGatewayVpcAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TransitGatewayVpcAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>peer_cloud_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS account ID or GCP project ID of the peered VPC</p></li>
<li><p><strong>peer_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS region of the peered VPC (if not in the same region as Aiven VPC)</p></li>
<li><p><strong>peer_vpc</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Transit gateway ID</p></li>
<li><p><strong>peering_connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud provider identifier for the peering connection if available</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – State of the peering connection</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>state_info</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – State-specific help or error information</p></li>
<li><p><strong>user_peer_network_cidrs</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of private IPv4 ranges to route through the peering connection</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC the peering connection belongs to</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.TransitGatewayVpcAttachment.peer_cloud_account">
<em class="property">property </em><code class="sig-name descname">peer_cloud_account</code><a class="headerlink" href="#pulumi_aiven.TransitGatewayVpcAttachment.peer_cloud_account" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS account ID or GCP project ID of the peered VPC</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.TransitGatewayVpcAttachment.peer_region">
<em class="property">property </em><code class="sig-name descname">peer_region</code><a class="headerlink" href="#pulumi_aiven.TransitGatewayVpcAttachment.peer_region" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS region of the peered VPC (if not in the same region as Aiven VPC)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.TransitGatewayVpcAttachment.peer_vpc">
<em class="property">property </em><code class="sig-name descname">peer_vpc</code><a class="headerlink" href="#pulumi_aiven.TransitGatewayVpcAttachment.peer_vpc" title="Permalink to this definition">¶</a></dt>
<dd><p>Transit gateway ID</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.TransitGatewayVpcAttachment.peering_connection_id">
<em class="property">property </em><code class="sig-name descname">peering_connection_id</code><a class="headerlink" href="#pulumi_aiven.TransitGatewayVpcAttachment.peering_connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud provider identifier for the peering connection if available</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.TransitGatewayVpcAttachment.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_aiven.TransitGatewayVpcAttachment.state" title="Permalink to this definition">¶</a></dt>
<dd><p>State of the peering connection</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.TransitGatewayVpcAttachment.state_info">
<em class="property">property </em><code class="sig-name descname">state_info</code><a class="headerlink" href="#pulumi_aiven.TransitGatewayVpcAttachment.state_info" title="Permalink to this definition">¶</a></dt>
<dd><p>State-specific help or error information</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.TransitGatewayVpcAttachment.user_peer_network_cidrs">
<em class="property">property </em><code class="sig-name descname">user_peer_network_cidrs</code><a class="headerlink" href="#pulumi_aiven.TransitGatewayVpcAttachment.user_peer_network_cidrs" title="Permalink to this definition">¶</a></dt>
<dd><p>List of private IPv4 ranges to route through the peering connection</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.TransitGatewayVpcAttachment.vpc_id">
<em class="property">property </em><code class="sig-name descname">vpc_id</code><a class="headerlink" href="#pulumi_aiven.TransitGatewayVpcAttachment.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC the peering connection belongs to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.TransitGatewayVpcAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.TransitGatewayVpcAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.TransitGatewayVpcAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.TransitGatewayVpcAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.VpcPeeringConnection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">VpcPeeringConnection</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_cloud_account</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_vpc</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">mypeeringconnection</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">VpcPeeringConnection</span><span class="p">(</span><span class="s2">&quot;mypeeringconnection&quot;</span><span class="p">,</span>
    <span class="n">peer_cloud_account</span><span class="o">=</span><span class="s2">&quot;&lt;PEER_ACCOUNT_ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">peer_region</span><span class="o">=</span><span class="s2">&quot;&lt;PEER_REGION&gt;&quot;</span><span class="p">,</span>
    <span class="n">peer_vpc</span><span class="o">=</span><span class="s2">&quot;&lt;PEER_VPC_ID/NAME&gt;&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">aiven_project_vpc</span><span class="p">[</span><span class="s2">&quot;myvpc&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>peer_cloud_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS account ID or GCP project ID of the peered VPC</p></li>
<li><p><strong>peer_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS region of the peered VPC (if not in the same region as Aiven VPC)</p></li>
<li><p><strong>peer_vpc</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS VPC ID or GCP VPC network name of the peered VPC</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC the peering connection belongs to</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_aiven.VpcPeeringConnection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_azure_app_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_azure_tenant_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_cloud_account</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_resource_group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_vpc</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peering_connection_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state_info</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.vpc_peering_connection.VpcPeeringConnection<a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VpcPeeringConnection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>peer_azure_app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Azure app registration id in UUID4 form that is allowed to create a peering to the peer vnet</p></li>
<li><p><strong>peer_azure_tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Azure tenant id in UUID4 form</p></li>
<li><p><strong>peer_cloud_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS account ID or GCP project ID of the peered VPC</p></li>
<li><p><strong>peer_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS region of the peered VPC (if not in the same region as Aiven VPC)</p></li>
<li><p><strong>peer_resource_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Azure resource group name of the peered VPC</p></li>
<li><p><strong>peer_vpc</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS VPC ID or GCP VPC network name of the peered VPC</p></li>
<li><p><strong>peering_connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud provider identifier for the peering connection if available</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – State of the peering connection</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>state_info</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – State-specific help or error information</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC the peering connection belongs to</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.VpcPeeringConnection.peer_azure_app_id">
<em class="property">property </em><code class="sig-name descname">peer_azure_app_id</code><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.peer_azure_app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Azure app registration id in UUID4 form that is allowed to create a peering to the peer vnet</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.VpcPeeringConnection.peer_azure_tenant_id">
<em class="property">property </em><code class="sig-name descname">peer_azure_tenant_id</code><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.peer_azure_tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Azure tenant id in UUID4 form</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.VpcPeeringConnection.peer_cloud_account">
<em class="property">property </em><code class="sig-name descname">peer_cloud_account</code><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.peer_cloud_account" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS account ID or GCP project ID of the peered VPC</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.VpcPeeringConnection.peer_region">
<em class="property">property </em><code class="sig-name descname">peer_region</code><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.peer_region" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS region of the peered VPC (if not in the same region as Aiven VPC)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.VpcPeeringConnection.peer_resource_group">
<em class="property">property </em><code class="sig-name descname">peer_resource_group</code><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.peer_resource_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Azure resource group name of the peered VPC</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.VpcPeeringConnection.peer_vpc">
<em class="property">property </em><code class="sig-name descname">peer_vpc</code><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.peer_vpc" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS VPC ID or GCP VPC network name of the peered VPC</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.VpcPeeringConnection.peering_connection_id">
<em class="property">property </em><code class="sig-name descname">peering_connection_id</code><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.peering_connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud provider identifier for the peering connection if available</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.VpcPeeringConnection.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.state" title="Permalink to this definition">¶</a></dt>
<dd><p>State of the peering connection</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.VpcPeeringConnection.state_info">
<em class="property">property </em><code class="sig-name descname">state_info</code><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.state_info" title="Permalink to this definition">¶</a></dt>
<dd><p>State-specific help or error information</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.VpcPeeringConnection.vpc_id">
<em class="property">property </em><code class="sig-name descname">vpc_id</code><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC the peering connection belongs to</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aiven.VpcPeeringConnection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aiven.VpcPeeringConnection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aiven.VpcPeeringConnection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_aiven.get_account">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_account</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_account.AwaitableGetAccountResult<a class="headerlink" href="#pulumi_aiven.get_account" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">account1</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">get_account</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;&lt;ACCOUNT_NAME&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_account_authentication">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_account_authentication</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authentication_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_acs_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_certificate</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_entity_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_idp_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">saml_metadata_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_account_authentication.AwaitableGetAccountAuthenticationResult<a class="headerlink" href="#pulumi_aiven.get_account_authentication" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_account_team">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_account_team</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_account_team.AwaitableGetAccountTeamResult<a class="headerlink" href="#pulumi_aiven.get_account_team" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">account_team1</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">get_account_team</span><span class="p">(</span><span class="n">account_id</span><span class="o">=</span><span class="n">aiven_account</span><span class="p">[</span><span class="s2">&quot;team&quot;</span><span class="p">][</span><span class="s2">&quot;account_id&quot;</span><span class="p">],</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;account_team1&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_account_team_member">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_account_team_member</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">accepted</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">invited_by_user_email</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_email</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_account_team_member.AwaitableGetAccountTeamMemberResult<a class="headerlink" href="#pulumi_aiven.get_account_team_member" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">get_account_team_member</span><span class="p">(</span><span class="n">account_id</span><span class="o">=</span><span class="n">aiven_account</span><span class="p">[</span><span class="s2">&quot;developers&quot;</span><span class="p">][</span><span class="s2">&quot;account_id&quot;</span><span class="p">],</span>
    <span class="n">team_id</span><span class="o">=</span><span class="n">aiven_account</span><span class="p">[</span><span class="s2">&quot;developers&quot;</span><span class="p">][</span><span class="s2">&quot;account_id&quot;</span><span class="p">],</span>
    <span class="n">user_email</span><span class="o">=</span><span class="s2">&quot;user+1@example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_account_team_project">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_account_team_project</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_account_team_project.AwaitableGetAccountTeamProjectResult<a class="headerlink" href="#pulumi_aiven.get_account_team_project" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">account_team_project1</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">get_account_team_project</span><span class="p">(</span><span class="n">account_id</span><span class="o">=</span><span class="n">aiven_account_team</span><span class="p">[</span><span class="s2">&quot;developers&quot;</span><span class="p">][</span><span class="s2">&quot;account_id&quot;</span><span class="p">],</span>
    <span class="n">project_name</span><span class="o">=</span><span class="n">aiven_project</span><span class="p">[</span><span class="s2">&quot;project1&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">team_id</span><span class="o">=</span><span class="n">aiven_account_team</span><span class="p">[</span><span class="s2">&quot;developers&quot;</span><span class="p">][</span><span class="s2">&quot;team_id&quot;</span><span class="p">])</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_cassanda">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_cassanda</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cassandra</span><span class="p">:</span> <span class="n">Union[GetCassandaCassandraArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cassandra_user_config</span><span class="p">:</span> <span class="n">Union[GetCassandaCassandraUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetCassandaComponentArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetCassandaServiceIntegrationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_cassanda.AwaitableGetCassandaResult<a class="headerlink" href="#pulumi_aiven.get_cassanda" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_connection_pool">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_connection_pool</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">connection_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_mode</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_size</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_connection_pool.AwaitableGetConnectionPoolResult<a class="headerlink" href="#pulumi_aiven.get_connection_pool" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">mytestpool</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">get_connection_pool</span><span class="p">(</span><span class="n">project</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;aiven_service&quot;</span><span class="p">][</span><span class="s2">&quot;myservice&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">service_name</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;aiven_service&quot;</span><span class="p">][</span><span class="s2">&quot;myservice&quot;</span><span class="p">][</span><span class="s2">&quot;service_name&quot;</span><span class="p">],</span>
    <span class="n">pool_name</span><span class="o">=</span><span class="s2">&quot;&lt;POOLNAME&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_database">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_database</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">database_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lc_collate</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lc_ctype</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_database.AwaitableGetDatabaseResult<a class="headerlink" href="#pulumi_aiven.get_database" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">mydatabase</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">get_database</span><span class="p">(</span><span class="n">project</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;aiven_service&quot;</span><span class="p">][</span><span class="s2">&quot;myservice&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">service_name</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;aiven_service&quot;</span><span class="p">][</span><span class="s2">&quot;myservice&quot;</span><span class="p">][</span><span class="s2">&quot;service_name&quot;</span><span class="p">],</span>
    <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;&lt;DATABASE_NAME&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_elastic_search">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_elastic_search</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetElasticSearchComponentArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch</span><span class="p">:</span> <span class="n">Union[GetElasticSearchElasticsearchArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch_user_config</span><span class="p">:</span> <span class="n">Union[GetElasticSearchElasticsearchUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetElasticSearchServiceIntegrationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_elastic_search.AwaitableGetElasticSearchResult<a class="headerlink" href="#pulumi_aiven.get_elastic_search" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_elastic_search_acl">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_elastic_search_acl</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">acls</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetElasticSearchAclAclArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extended_acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_elastic_search_acl.AwaitableGetElasticSearchAclResult<a class="headerlink" href="#pulumi_aiven.get_elastic_search_acl" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_grafana">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_grafana</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetGrafanaComponentArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana</span><span class="p">:</span> <span class="n">Union[GetGrafanaGrafanaArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana_user_config</span><span class="p">:</span> <span class="n">Union[GetGrafanaGrafanaUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetGrafanaServiceIntegrationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_grafana.AwaitableGetGrafanaResult<a class="headerlink" href="#pulumi_aiven.get_grafana" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_influx_db">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_influx_db</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetInfluxDbComponentArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb</span><span class="p">:</span> <span class="n">Union[GetInfluxDbInfluxdbArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb_user_config</span><span class="p">:</span> <span class="n">Union[GetInfluxDbInfluxdbUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetInfluxDbServiceIntegrationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_influx_db.AwaitableGetInfluxDbResult<a class="headerlink" href="#pulumi_aiven.get_influx_db" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_kafka">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_kafka</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetKafkaComponentArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_acl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka</span><span class="p">:</span> <span class="n">Union[GetKafkaKafkaArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_user_config</span><span class="p">:</span> <span class="n">Union[GetKafkaKafkaUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetKafkaServiceIntegrationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_kafka.AwaitableGetKafkaResult<a class="headerlink" href="#pulumi_aiven.get_kafka" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_kafka_acl">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_kafka_acl</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">permission</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topic</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_kafka_acl.AwaitableGetKafkaAclResult<a class="headerlink" href="#pulumi_aiven.get_kafka_acl" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_kafka_connect">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_kafka_connect</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetKafkaConnectComponentArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect</span><span class="p">:</span> <span class="n">Union[GetKafkaConnectKafkaConnectArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect_user_config</span><span class="p">:</span> <span class="n">Union[GetKafkaConnectKafkaConnectUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetKafkaConnectServiceIntegrationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_kafka_connect.AwaitableGetKafkaConnectResult<a class="headerlink" href="#pulumi_aiven.get_kafka_connect" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_kafka_connector">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_kafka_connector</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connector_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_author</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_class</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_doc_url</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_title</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tasks</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetKafkaConnectorTaskArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_kafka_connector.AwaitableGetKafkaConnectorResult<a class="headerlink" href="#pulumi_aiven.get_kafka_connector" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_kafka_mirror_maker">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_kafka_mirror_maker</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetKafkaMirrorMakerComponentArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker</span><span class="p">:</span> <span class="n">Union[GetKafkaMirrorMakerKafkaMirrormakerArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker_user_config</span><span class="p">:</span> <span class="n">Union[GetKafkaMirrorMakerKafkaMirrormakerUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetKafkaMirrorMakerServiceIntegrationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_kafka_mirror_maker.AwaitableGetKafkaMirrorMakerResult<a class="headerlink" href="#pulumi_aiven.get_kafka_mirror_maker" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_kafka_schema">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_kafka_schema</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_kafka_schema.AwaitableGetKafkaSchemaResult<a class="headerlink" href="#pulumi_aiven.get_kafka_schema" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_kafka_schema_configuration">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_kafka_schema_configuration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_kafka_schema_configuration.AwaitableGetKafkaSchemaConfigurationResult<a class="headerlink" href="#pulumi_aiven.get_kafka_schema_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_kafka_topic">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_kafka_topic</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cleanup_policy</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_in_sync_replicas</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partitions</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_bytes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_hours</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topic_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_kafka_topic.AwaitableGetKafkaTopicResult<a class="headerlink" href="#pulumi_aiven.get_kafka_topic" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">mytesttopic</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">get_kafka_topic</span><span class="p">(</span><span class="n">project</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;aiven_service&quot;</span><span class="p">][</span><span class="s2">&quot;myservice&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">service_name</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;aiven_service&quot;</span><span class="p">][</span><span class="s2">&quot;myservice&quot;</span><span class="p">][</span><span class="s2">&quot;service_name&quot;</span><span class="p">],</span>
    <span class="n">topic_name</span><span class="o">=</span><span class="s2">&quot;&lt;TOPIC_NAME&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_mirror_maker_replication_flow">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_mirror_maker_replication_flow</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_cluster</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_cluster</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topics</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topics_blacklists</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_mirror_maker_replication_flow.AwaitableGetMirrorMakerReplicationFlowResult<a class="headerlink" href="#pulumi_aiven.get_mirror_maker_replication_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_my_sql">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_my_sql</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetMySqlComponentArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql</span><span class="p">:</span> <span class="n">Union[GetMySqlMysqlArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql_user_config</span><span class="p">:</span> <span class="n">Union[GetMySqlMysqlUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetMySqlServiceIntegrationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_my_sql.AwaitableGetMySqlResult<a class="headerlink" href="#pulumi_aiven.get_my_sql" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_pg">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_pg</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetPgComponentArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg</span><span class="p">:</span> <span class="n">Union[GetPgPgArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg_user_config</span><span class="p">:</span> <span class="n">Union[GetPgPgUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetPgServiceIntegrationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_pg.AwaitableGetPgResult<a class="headerlink" href="#pulumi_aiven.get_pg" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_project">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_project</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_address</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_emails</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_cert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">card_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">copy_from_project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country_code</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">technical_emails</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_project.AwaitableGetProjectResult<a class="headerlink" href="#pulumi_aiven.get_project" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">myproject</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">get_project</span><span class="p">(</span><span class="n">project</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT_NAME&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_project_user">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_project_user</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">accepted</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">member_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_project_user.AwaitableGetProjectUserResult<a class="headerlink" href="#pulumi_aiven.get_project_user" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">mytestuser</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">get_project_user</span><span class="p">(</span><span class="n">project</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;aiven_project&quot;</span><span class="p">][</span><span class="s2">&quot;myproject&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;john.doe@example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_project_vpc">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_project_vpc</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_cidr</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_project_vpc.AwaitableGetProjectVpcResult<a class="headerlink" href="#pulumi_aiven.get_project_vpc" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">myvpc</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">get_project_vpc</span><span class="p">(</span><span class="n">project</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;aiven_project&quot;</span><span class="p">][</span><span class="s2">&quot;myproject&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">cloud_name</span><span class="o">=</span><span class="s2">&quot;google-europe-west1&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_redis">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_redis</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetRedisComponentArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis</span><span class="p">:</span> <span class="n">Union[GetRedisRedisArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis_user_config</span><span class="p">:</span> <span class="n">Union[GetRedisRedisUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetRedisServiceIntegrationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_redis.AwaitableGetRedisResult<a class="headerlink" href="#pulumi_aiven.get_redis" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_service">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cassandra</span><span class="p">:</span> <span class="n">Union[GetServiceCassandraArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cassandra_user_config</span><span class="p">:</span> <span class="n">Union[GetServiceCassandraUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetServiceComponentArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch</span><span class="p">:</span> <span class="n">Union[GetServiceElasticsearchArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">elasticsearch_user_config</span><span class="p">:</span> <span class="n">Union[GetServiceElasticsearchUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana</span><span class="p">:</span> <span class="n">Union[GetServiceGrafanaArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grafana_user_config</span><span class="p">:</span> <span class="n">Union[GetServiceGrafanaUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb</span><span class="p">:</span> <span class="n">Union[GetServiceInfluxdbArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">influxdb_user_config</span><span class="p">:</span> <span class="n">Union[GetServiceInfluxdbUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka</span><span class="p">:</span> <span class="n">Union[GetServiceKafkaArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect</span><span class="p">:</span> <span class="n">Union[GetServiceKafkaConnectArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect_user_config</span><span class="p">:</span> <span class="n">Union[GetServiceKafkaConnectUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker</span><span class="p">:</span> <span class="n">Union[GetServiceKafkaMirrormakerArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker_user_config</span><span class="p">:</span> <span class="n">Union[GetServiceKafkaMirrormakerUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_user_config</span><span class="p">:</span> <span class="n">Union[GetServiceKafkaUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_dow</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintenance_window_time</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql</span><span class="p">:</span> <span class="n">Union[GetServiceMysqlArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mysql_user_config</span><span class="p">:</span> <span class="n">Union[GetServiceMysqlUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg</span><span class="p">:</span> <span class="n">Union[GetServicePgArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pg_user_config</span><span class="p">:</span> <span class="n">Union[GetServicePgUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_vpc_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis</span><span class="p">:</span> <span class="n">Union[GetServiceRedisArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redis_user_config</span><span class="p">:</span> <span class="n">Union[GetServiceRedisUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_integrations</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetServiceServiceIntegrationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_port</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_uri</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">termination_protection</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_service.AwaitableGetServiceResult<a class="headerlink" href="#pulumi_aiven.get_service" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">myservice</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">get_service</span><span class="p">(</span><span class="n">project</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;aiven_project&quot;</span><span class="p">][</span><span class="s2">&quot;myproject&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">service_name</span><span class="o">=</span><span class="s2">&quot;&lt;SERVICE_NAME&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_service_component">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_service_component</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">component</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_authentication_method</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usage</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_service_component.AwaitableGetServiceComponentResult<a class="headerlink" href="#pulumi_aiven.get_service_component" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_service_integration">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_service_integration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">destination_endpoint_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">integration_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_connect_user_config</span><span class="p">:</span> <span class="n">Union[GetServiceIntegrationKafkaConnectUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_mirrormaker_user_config</span><span class="p">:</span> <span class="n">Union[GetServiceIntegrationKafkaMirrormakerUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs_user_config</span><span class="p">:</span> <span class="n">Union[GetServiceIntegrationLogsUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mirrormaker_user_config</span><span class="p">:</span> <span class="n">Union[GetServiceIntegrationMirrormakerUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_endpoint_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_service_integration.AwaitableGetServiceIntegrationResult<a class="headerlink" href="#pulumi_aiven.get_service_integration" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_service_integration_endpoint">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_service_integration_endpoint</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datadog_user_config</span><span class="p">:</span> <span class="n">Union[GetServiceIntegrationEndpointDatadogUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_config</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_elasticsearch_logs_user_config</span><span class="p">:</span> <span class="n">Union[GetServiceIntegrationEndpointExternalElasticsearchLogsUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prometheus_user_config</span><span class="p">:</span> <span class="n">Union[GetServiceIntegrationEndpointPrometheusUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rsyslog_user_config</span><span class="p">:</span> <span class="n">Union[GetServiceIntegrationEndpointRsyslogUserConfigArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_service_integration_endpoint.AwaitableGetServiceIntegrationEndpointResult<a class="headerlink" href="#pulumi_aiven.get_service_integration_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">myendpoint</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">get_service_integration_endpoint</span><span class="p">(</span><span class="n">project</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;aiven_project&quot;</span><span class="p">][</span><span class="s2">&quot;myproject&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">endpoint_name</span><span class="o">=</span><span class="s2">&quot;&lt;ENDPOINT_NAME&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_service_user">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_service_user</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_cert</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_key</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_service_user.AwaitableGetServiceUserResult<a class="headerlink" href="#pulumi_aiven.get_service_user" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">myserviceuser</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">get_service_user</span><span class="p">(</span><span class="n">project</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;aiven_service&quot;</span><span class="p">][</span><span class="s2">&quot;myservice&quot;</span><span class="p">][</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">service_name</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;aiven_service&quot;</span><span class="p">][</span><span class="s2">&quot;myservice&quot;</span><span class="p">][</span><span class="s2">&quot;service_name&quot;</span><span class="p">],</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;&lt;USERNAME&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_transit_gateway_vpc_attachment">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_transit_gateway_vpc_attachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">peer_cloud_account</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_region</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_vpc</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peering_connection_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state_info</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_peer_network_cidrs</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_transit_gateway_vpc_attachment.AwaitableGetTransitGatewayVpcAttachmentResult<a class="headerlink" href="#pulumi_aiven.get_transit_gateway_vpc_attachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aiven.get_vpc_peering_connection">
<code class="sig-prename descclassname">pulumi_aiven.</code><code class="sig-name descname">get_vpc_peering_connection</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">peer_azure_app_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_azure_tenant_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_cloud_account</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_region</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_resource_group</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_vpc</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peering_connection_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state_info</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_aiven.get_vpc_peering_connection.AwaitableGetVpcPeeringConnectionResult<a class="headerlink" href="#pulumi_aiven.get_vpc_peering_connection" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aiven</span> <span class="k">as</span> <span class="nn">aiven</span>

<span class="n">mypeeringconnection</span> <span class="o">=</span> <span class="n">aiven</span><span class="o">.</span><span class="n">get_vpc_peering_connection</span><span class="p">(</span><span class="n">vpc_id</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;aiven_project_vpc&quot;</span><span class="p">][</span><span class="s2">&quot;vpc_id&quot;</span><span class="p">],</span>
    <span class="n">peer_cloud_account</span><span class="o">=</span><span class="s2">&quot;&lt;PEER_ACCOUNT_ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">peer_vpc</span><span class="o">=</span><span class="s2">&quot;&lt;PEER_VPC_ID/NAME&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

</div>
