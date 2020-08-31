---
title: Package pulumi_keycloak
title_tag: Package pulumi_keycloak | Python SDK
linktitle: pulumi_keycloak
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "keycloak" >}}

<div class="section" id="module-pulumi_keycloak">
<span id="pulumi-keycloak"></span><h1>Pulumi Keycloak<a class="headerlink" href="#module-pulumi_keycloak" title="Permalink to this headline">¶</a></h1>
<dl class="py class">
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">AttributeImporterIdentityProviderMapper</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attribute_friendly_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attribute_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">claim_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extra_config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity_provider_alias</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_attribute</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows to create and manage identity provider mappers within Keycloak.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">test_mapper</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">AttributeImporterIdentityProviderMapper</span><span class="p">(</span><span class="s2">&quot;testMapper&quot;</span><span class="p">,</span>
    <span class="n">attribute_name</span><span class="o">=</span><span class="s2">&quot;http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname&quot;</span><span class="p">,</span>
    <span class="n">identity_provider_alias</span><span class="o">=</span><span class="s2">&quot;idp_alias&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">,</span>
    <span class="n">user_attribute</span><span class="o">=</span><span class="s2">&quot;lastName&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm</span></code> - (Required) The name of the realm.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The name of the mapper.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identity_provider_alias</span></code> - (Required) The alias of the associated identity provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_attribute</span></code> - (Required) The user attribute name to store SAML attribute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attribute_name</span></code> - (Optional) The Name of attribute to search for in assertion. You can leave this blank and specify a friendly name instead.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attribute_friendly_name</span></code> - (Optional) The friendly name of attribute to search for in assertion.  You can leave this blank and specify an attribute name instead.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">claim_name</span></code> - (Optional) The claim name.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attribute_friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Attribute Friendly Name</p></li>
<li><p><strong>attribute_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Attribute Name</p></li>
<li><p><strong>claim_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Claim Name</p></li>
<li><p><strong>identity_provider_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IDP Alias</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IDP Mapper Name</p></li>
<li><p><strong>realm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Realm Name</p></li>
<li><p><strong>user_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User Attribute</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attribute_friendly_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attribute_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">claim_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extra_config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity_provider_alias</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_attribute</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.attribute_importer_identity_provider_mapper.AttributeImporterIdentityProviderMapper<a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AttributeImporterIdentityProviderMapper resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attribute_friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Attribute Friendly Name</p></li>
<li><p><strong>attribute_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Attribute Name</p></li>
<li><p><strong>claim_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Claim Name</p></li>
<li><p><strong>identity_provider_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IDP Alias</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IDP Mapper Name</p></li>
<li><p><strong>realm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Realm Name</p></li>
<li><p><strong>user_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User Attribute</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper.attribute_friendly_name">
<em class="property">property </em><code class="sig-name descname">attribute_friendly_name</code><a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper.attribute_friendly_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Attribute Friendly Name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper.attribute_name">
<em class="property">property </em><code class="sig-name descname">attribute_name</code><a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper.attribute_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Attribute Name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper.claim_name">
<em class="property">property </em><code class="sig-name descname">claim_name</code><a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper.claim_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Claim Name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper.identity_provider_alias">
<em class="property">property </em><code class="sig-name descname">identity_provider_alias</code><a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper.identity_provider_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>IDP Alias</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper.name" title="Permalink to this definition">¶</a></dt>
<dd><p>IDP Mapper Name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper.realm">
<em class="property">property </em><code class="sig-name descname">realm</code><a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper.realm" title="Permalink to this definition">¶</a></dt>
<dd><p>Realm Name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper.user_attribute">
<em class="property">property </em><code class="sig-name descname">user_attribute</code><a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper.user_attribute" title="Permalink to this definition">¶</a></dt>
<dd><p>User Attribute</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.AttributeToRoleIdentityMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">AttributeToRoleIdentityMapper</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attribute_friendly_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attribute_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attribute_value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">claim_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">claim_value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extra_config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity_provider_alias</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.AttributeToRoleIdentityMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AttributeToRoleIdentityMapper resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] attribute_friendly_name: Attribute Friendly Name
:param pulumi.Input[str] attribute_name: Attribute Name
:param pulumi.Input[str] attribute_value: Attribute Value
:param pulumi.Input[str] claim_name: OIDC Claim Name
:param pulumi.Input[str] claim_value: OIDC Claim Value
:param pulumi.Input[str] identity_provider_alias: IDP Alias
:param pulumi.Input[str] name: IDP Mapper Name
:param pulumi.Input[str] realm: Realm Name
:param pulumi.Input[str] role: Role Name</p>
<dl class="py method">
<dt id="pulumi_keycloak.AttributeToRoleIdentityMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attribute_friendly_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attribute_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attribute_value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">claim_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">claim_value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extra_config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity_provider_alias</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.attribute_to_role_identity_mapper.AttributeToRoleIdentityMapper<a class="headerlink" href="#pulumi_keycloak.AttributeToRoleIdentityMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AttributeToRoleIdentityMapper resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attribute_friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Attribute Friendly Name</p></li>
<li><p><strong>attribute_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Attribute Name</p></li>
<li><p><strong>attribute_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Attribute Value</p></li>
<li><p><strong>claim_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – OIDC Claim Name</p></li>
<li><p><strong>claim_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – OIDC Claim Value</p></li>
<li><p><strong>identity_provider_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IDP Alias</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IDP Mapper Name</p></li>
<li><p><strong>realm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Realm Name</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role Name</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeToRoleIdentityMapper.attribute_friendly_name">
<em class="property">property </em><code class="sig-name descname">attribute_friendly_name</code><a class="headerlink" href="#pulumi_keycloak.AttributeToRoleIdentityMapper.attribute_friendly_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Attribute Friendly Name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeToRoleIdentityMapper.attribute_name">
<em class="property">property </em><code class="sig-name descname">attribute_name</code><a class="headerlink" href="#pulumi_keycloak.AttributeToRoleIdentityMapper.attribute_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Attribute Name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeToRoleIdentityMapper.attribute_value">
<em class="property">property </em><code class="sig-name descname">attribute_value</code><a class="headerlink" href="#pulumi_keycloak.AttributeToRoleIdentityMapper.attribute_value" title="Permalink to this definition">¶</a></dt>
<dd><p>Attribute Value</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeToRoleIdentityMapper.claim_name">
<em class="property">property </em><code class="sig-name descname">claim_name</code><a class="headerlink" href="#pulumi_keycloak.AttributeToRoleIdentityMapper.claim_name" title="Permalink to this definition">¶</a></dt>
<dd><p>OIDC Claim Name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeToRoleIdentityMapper.claim_value">
<em class="property">property </em><code class="sig-name descname">claim_value</code><a class="headerlink" href="#pulumi_keycloak.AttributeToRoleIdentityMapper.claim_value" title="Permalink to this definition">¶</a></dt>
<dd><p>OIDC Claim Value</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeToRoleIdentityMapper.identity_provider_alias">
<em class="property">property </em><code class="sig-name descname">identity_provider_alias</code><a class="headerlink" href="#pulumi_keycloak.AttributeToRoleIdentityMapper.identity_provider_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>IDP Alias</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeToRoleIdentityMapper.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_keycloak.AttributeToRoleIdentityMapper.name" title="Permalink to this definition">¶</a></dt>
<dd><p>IDP Mapper Name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeToRoleIdentityMapper.realm">
<em class="property">property </em><code class="sig-name descname">realm</code><a class="headerlink" href="#pulumi_keycloak.AttributeToRoleIdentityMapper.realm" title="Permalink to this definition">¶</a></dt>
<dd><p>Realm Name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeToRoleIdentityMapper.role">
<em class="property">property </em><code class="sig-name descname">role</code><a class="headerlink" href="#pulumi_keycloak.AttributeToRoleIdentityMapper.role" title="Permalink to this definition">¶</a></dt>
<dd><p>Role Name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeToRoleIdentityMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.AttributeToRoleIdentityMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.AttributeToRoleIdentityMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.AttributeToRoleIdentityMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.AwaitableGetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">AwaitableGetGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.AwaitableGetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_keycloak.AwaitableGetRealmKeysResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">AwaitableGetRealmKeysResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">algorithms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statuses</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.AwaitableGetRealmKeysResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_keycloak.AwaitableGetRealmResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">AwaitableGetRealmResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_code_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan_login</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan_user_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_token_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_token_lifespan_for_implicit_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_theme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_token_generated_by_admin_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_token_generated_by_user_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_theme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">browser_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_authentication_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">direct_grant_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name_html</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_authentication_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">duplicate_emails_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edit_username_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_theme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internal_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internationalizations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_theme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_with_email_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_idle_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_max_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_token_max_reuse</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_email_as_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remember_me</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_credentials_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_password_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_defenses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">smtp_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_required</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_idle_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_max_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_managed_access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verify_email</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.AwaitableGetRealmResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_keycloak.AwaitableGetRoleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">AwaitableGetRoleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.AwaitableGetRoleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_keycloak.CustomUserFederation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">CustomUserFederation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cache_policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.CustomUserFederation" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a CustomUserFederation resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] enabled: When false, this provider will not be used when performing queries for users.
:param pulumi.Input[str] name: Display name of the provider when displayed in the console.
:param pulumi.Input[str] parent_id: The parent_id of the generated component. will use realm_id if not specified.
:param pulumi.Input[float] priority: Priority of this provider when looking up users. Lower values are first.
:param pulumi.Input[str] provider_id: The unique ID of the custom provider, specified in the <code class="docutils literal notranslate"><span class="pre">getId</span></code> implementation for the UserStorageProviderFactory</p>
<blockquote>
<div><p>interface</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm (name) this provider will provide user federation for.</p>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.CustomUserFederation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cache_policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.custom_user_federation.CustomUserFederation<a class="headerlink" href="#pulumi_keycloak.CustomUserFederation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CustomUserFederation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When false, this provider will not be used when performing queries for users.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the provider when displayed in the console.</p></li>
<li><p><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The parent_id of the generated component. will use realm_id if not specified.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Priority of this provider when looking up users. Lower values are first.</p></li>
<li><p><strong>provider_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID of the custom provider, specified in the <code class="docutils literal notranslate"><span class="pre">getId</span></code> implementation for the UserStorageProviderFactory
interface</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm (name) this provider will provide user federation for.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.CustomUserFederation.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_keycloak.CustomUserFederation.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>When false, this provider will not be used when performing queries for users.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.CustomUserFederation.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_keycloak.CustomUserFederation.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name of the provider when displayed in the console.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.CustomUserFederation.parent_id">
<em class="property">property </em><code class="sig-name descname">parent_id</code><a class="headerlink" href="#pulumi_keycloak.CustomUserFederation.parent_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The parent_id of the generated component. will use realm_id if not specified.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.CustomUserFederation.priority">
<em class="property">property </em><code class="sig-name descname">priority</code><a class="headerlink" href="#pulumi_keycloak.CustomUserFederation.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Priority of this provider when looking up users. Lower values are first.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.CustomUserFederation.provider_id">
<em class="property">property </em><code class="sig-name descname">provider_id</code><a class="headerlink" href="#pulumi_keycloak.CustomUserFederation.provider_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID of the custom provider, specified in the <code class="docutils literal notranslate"><span class="pre">getId</span></code> implementation for the UserStorageProviderFactory
interface</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.CustomUserFederation.realm_id">
<em class="property">property </em><code class="sig-name descname">realm_id</code><a class="headerlink" href="#pulumi_keycloak.CustomUserFederation.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm (name) this provider will provide user federation for.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.CustomUserFederation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.CustomUserFederation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.CustomUserFederation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.CustomUserFederation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.DefaultGroups">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">DefaultGroups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_ids</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.DefaultGroups" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for managing a realm’s default groups.</p>
<p>Note that you should not use <code class="docutils literal notranslate"><span class="pre">DefaultGroups</span></code> with a group with memberships managed
by <code class="docutils literal notranslate"><span class="pre">GroupMemberships</span></code>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">)</span>
<span class="n">group</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;group&quot;</span><span class="p">,</span> <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">default</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">DefaultGroups</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">group_ids</span><span class="o">=</span><span class="p">[</span><span class="n">group</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this group exists in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group_ids</span></code> - (Required) A set of group ids that should be default groups on the realm referenced by <code class="docutils literal notranslate"><span class="pre">realm_id</span></code>.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.DefaultGroups.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_ids</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.default_groups.DefaultGroups<a class="headerlink" href="#pulumi_keycloak.DefaultGroups.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DefaultGroups resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.DefaultGroups.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.DefaultGroups.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.DefaultGroups.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.DefaultGroups.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.GenericClientProtocolMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">GenericClientProtocolMapper</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_scope_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_mapper</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GenericClientProtocolMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing protocol mapper for both types of clients (openid-connect and saml) within Keycloak.</p>
<p>There are two uses cases for using this resource:</p>
<ul class="simple">
<li><p>If you implemented a custom protocol mapper, this resource can be used to configure it</p></li>
<li><p>If the provider doesn’t support a particular protocol mapper, this resource can be used instead.</p></li>
</ul>
<p>Due to the generic nature of this mapper, it is less user-friendly and more prone to configuration errors.
Therefore, if possible, a specific mapper should be used.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">)</span>
<span class="n">saml_client</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">saml</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="s2">&quot;samlClient&quot;</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="s2">&quot;test-client&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">saml_hardcode_attribute_mapper</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">GenericClientProtocolMapper</span><span class="p">(</span><span class="s2">&quot;samlHardcodeAttributeMapper&quot;</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="n">saml_client</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;attribute.name&quot;</span><span class="p">:</span> <span class="s2">&quot;name&quot;</span><span class="p">,</span>
        <span class="s2">&quot;attribute.nameformat&quot;</span><span class="p">:</span> <span class="s2">&quot;Basic&quot;</span><span class="p">,</span>
        <span class="s2">&quot;attribute.value&quot;</span><span class="p">:</span> <span class="s2">&quot;value&quot;</span><span class="p">,</span>
        <span class="s2">&quot;friendly.name&quot;</span><span class="p">:</span> <span class="s2">&quot;display name&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">protocol</span><span class="o">=</span><span class="s2">&quot;saml&quot;</span><span class="p">,</span>
    <span class="n">protocol_mapper</span><span class="o">=</span><span class="s2">&quot;saml-hardcode-attribute-mapper&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this protocol mapper exists within.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> - (Required) The client this protocol mapper is attached to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The display name of this protocol mapper in the GUI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> - (Required) The type of client (either <code class="docutils literal notranslate"><span class="pre">openid-connect</span></code> or <code class="docutils literal notranslate"><span class="pre">saml</span></code>). The type must match the type of the client.</p></li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">protocol_mapper</span></code> - (Required) The name of the protocol mapper. The protocol mapper must be</dt><dd><p>compatible with the specified client.</p>
</dd>
</dl>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">config</span></code> - (Required) A map with key / value pairs for configuring the protocol mapper. The supported keys depends on the protocol mapper.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mapper’s associated client. Cannot be used at the same time as client_scope_id.</p></li>
<li><p><strong>client_scope_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mapper’s associated client scope. Cannot be used at the same time as client_id.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-friendly name that will appear in the Keycloak console.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol of the client (openid-connect / saml).</p></li>
<li><p><strong>protocol_mapper</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the protocol mapper.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm id where the associated client or client scope exists.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.GenericClientProtocolMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_scope_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol_mapper</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.generic_client_protocol_mapper.GenericClientProtocolMapper<a class="headerlink" href="#pulumi_keycloak.GenericClientProtocolMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GenericClientProtocolMapper resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mapper’s associated client. Cannot be used at the same time as client_scope_id.</p></li>
<li><p><strong>client_scope_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mapper’s associated client scope. Cannot be used at the same time as client_id.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-friendly name that will appear in the Keycloak console.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol of the client (openid-connect / saml).</p></li>
<li><p><strong>protocol_mapper</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the protocol mapper.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm id where the associated client or client scope exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientProtocolMapper.client_id">
<em class="property">property </em><code class="sig-name descname">client_id</code><a class="headerlink" href="#pulumi_keycloak.GenericClientProtocolMapper.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The mapper’s associated client. Cannot be used at the same time as client_scope_id.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientProtocolMapper.client_scope_id">
<em class="property">property </em><code class="sig-name descname">client_scope_id</code><a class="headerlink" href="#pulumi_keycloak.GenericClientProtocolMapper.client_scope_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The mapper’s associated client scope. Cannot be used at the same time as client_id.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientProtocolMapper.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_keycloak.GenericClientProtocolMapper.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-friendly name that will appear in the Keycloak console.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientProtocolMapper.protocol">
<em class="property">property </em><code class="sig-name descname">protocol</code><a class="headerlink" href="#pulumi_keycloak.GenericClientProtocolMapper.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol of the client (openid-connect / saml).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientProtocolMapper.protocol_mapper">
<em class="property">property </em><code class="sig-name descname">protocol_mapper</code><a class="headerlink" href="#pulumi_keycloak.GenericClientProtocolMapper.protocol_mapper" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the protocol mapper.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientProtocolMapper.realm_id">
<em class="property">property </em><code class="sig-name descname">realm_id</code><a class="headerlink" href="#pulumi_keycloak.GenericClientProtocolMapper.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm id where the associated client or client scope exists.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientProtocolMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GenericClientProtocolMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.GenericClientProtocolMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GenericClientProtocolMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.GenericClientRoleMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">GenericClientRoleMapper</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_scope_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GenericClientRoleMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a GenericClientRoleMapper resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] client_id: The destination client of the client role. Cannot be used at the same time as client_scope_id.
:param pulumi.Input[str] client_scope_id: The destination client scope of the client role. Cannot be used at the same time as client_id.
:param pulumi.Input[str] realm_id: The realm id where the associated client or client scope exists.
:param pulumi.Input[str] role_id: Id of the role to assign</p>
<dl class="py method">
<dt id="pulumi_keycloak.GenericClientRoleMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_scope_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.generic_client_role_mapper.GenericClientRoleMapper<a class="headerlink" href="#pulumi_keycloak.GenericClientRoleMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GenericClientRoleMapper resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination client of the client role. Cannot be used at the same time as client_scope_id.</p></li>
<li><p><strong>client_scope_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination client scope of the client role. Cannot be used at the same time as client_id.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm id where the associated client or client scope exists.</p></li>
<li><p><strong>role_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of the role to assign</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientRoleMapper.client_id">
<em class="property">property </em><code class="sig-name descname">client_id</code><a class="headerlink" href="#pulumi_keycloak.GenericClientRoleMapper.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination client of the client role. Cannot be used at the same time as client_scope_id.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientRoleMapper.client_scope_id">
<em class="property">property </em><code class="sig-name descname">client_scope_id</code><a class="headerlink" href="#pulumi_keycloak.GenericClientRoleMapper.client_scope_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination client scope of the client role. Cannot be used at the same time as client_id.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientRoleMapper.realm_id">
<em class="property">property </em><code class="sig-name descname">realm_id</code><a class="headerlink" href="#pulumi_keycloak.GenericClientRoleMapper.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm id where the associated client or client scope exists.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientRoleMapper.role_id">
<em class="property">property </em><code class="sig-name descname">role_id</code><a class="headerlink" href="#pulumi_keycloak.GenericClientRoleMapper.role_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Id of the role to assign</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientRoleMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GenericClientRoleMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.GenericClientRoleMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GenericClientRoleMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.GetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">GetGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="py method">
<dt id="pulumi_keycloak.GetGroupResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_keycloak.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_keycloak.GetRealmKeysResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">GetRealmKeysResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">algorithms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statuses</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GetRealmKeysResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRealmKeys.</p>
<dl class="py method">
<dt id="pulumi_keycloak.GetRealmKeysResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_keycloak.GetRealmKeysResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_keycloak.GetRealmResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">GetRealmResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_code_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan_login</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan_user_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_token_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_token_lifespan_for_implicit_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_theme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_token_generated_by_admin_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_token_generated_by_user_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_theme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">browser_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_authentication_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">direct_grant_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name_html</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_authentication_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">duplicate_emails_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edit_username_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_theme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internal_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internationalizations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_theme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_with_email_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_idle_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_max_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_token_max_reuse</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_email_as_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remember_me</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_credentials_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_password_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_defenses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">smtp_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_required</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_idle_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_max_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_managed_access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verify_email</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GetRealmResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRealm.</p>
<dl class="py method">
<dt id="pulumi_keycloak.GetRealmResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_keycloak.GetRealmResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_keycloak.GetRoleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">GetRoleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GetRoleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRole.</p>
<dl class="py method">
<dt id="pulumi_keycloak.GetRoleResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_keycloak.GetRoleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_keycloak.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing Groups within Keycloak.</p>
<p>Groups provide a logical wrapping for users within Keycloak. Users within a
group can share attributes and roles, and group membership can be mapped
to a claim.</p>
<p>Attributes can also be defined on Groups.</p>
<p>Groups can also be federated from external data sources, such as LDAP or Active Directory.
This resource <strong>should not</strong> be used to manage groups that were created this way.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">)</span>
<span class="n">parent_group</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;parentGroup&quot;</span><span class="p">,</span> <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">child_group</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;childGroup&quot;</span><span class="p">,</span>
    <span class="n">parent_id</span><span class="o">=</span><span class="n">parent_group</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">child_group_with_optional_attributes</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;childGroupWithOptionalAttributes&quot;</span><span class="p">,</span>
    <span class="n">attributes</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;key1&quot;</span><span class="p">:</span> <span class="s2">&quot;value1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;key2&quot;</span><span class="p">:</span> <span class="s2">&quot;value2&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">parent_id</span><span class="o">=</span><span class="n">parent_group</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this group exists in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parent_id</span></code> - (Optional) The ID of this group’s parent. If omitted, this group will be defined at the root level.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The name of the group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> - (Optional) A dict of key/value pairs to set as custom attributes for the group.</p></li>
</ul>
<p>In addition to the arguments listed above, the following computed attributes are exported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> - The complete path of the group. For example, the child group’s path in the example configuration would be <code class="docutils literal notranslate"><span class="pre">/parent-group/child-group</span></code>.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.group.Group<a class="headerlink" href="#pulumi_keycloak.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.GroupMemberships">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">GroupMemberships</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GroupMemberships" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a GroupMemberships resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_keycloak.GroupMemberships.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.group_memberships.GroupMemberships<a class="headerlink" href="#pulumi_keycloak.GroupMemberships.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupMemberships resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GroupMemberships.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GroupMemberships.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.GroupMemberships.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GroupMemberships.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.GroupRoles">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">GroupRoles</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_ids</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GroupRoles" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a GroupRoles resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_keycloak.GroupRoles.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_ids</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.group_roles.GroupRoles<a class="headerlink" href="#pulumi_keycloak.GroupRoles.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupRoles resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GroupRoles.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GroupRoles.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.GroupRoles.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GroupRoles.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.HardcodedAttributeIdentityProviderMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">HardcodedAttributeIdentityProviderMapper</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attribute_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attribute_value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extra_config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity_provider_alias</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_session</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.HardcodedAttributeIdentityProviderMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a HardcodedAttributeIdentityProviderMapper resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] attribute_name: OIDC Claim
:param pulumi.Input[str] attribute_value: User Attribute
:param pulumi.Input[str] identity_provider_alias: IDP Alias
:param pulumi.Input[str] name: IDP Mapper Name
:param pulumi.Input[str] realm: Realm Name
:param pulumi.Input[bool] user_session: Is Attribute Related To a User Session</p>
<dl class="py method">
<dt id="pulumi_keycloak.HardcodedAttributeIdentityProviderMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attribute_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attribute_value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extra_config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity_provider_alias</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_session</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.hardcoded_attribute_identity_provider_mapper.HardcodedAttributeIdentityProviderMapper<a class="headerlink" href="#pulumi_keycloak.HardcodedAttributeIdentityProviderMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HardcodedAttributeIdentityProviderMapper resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attribute_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – OIDC Claim</p></li>
<li><p><strong>attribute_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User Attribute</p></li>
<li><p><strong>identity_provider_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IDP Alias</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IDP Mapper Name</p></li>
<li><p><strong>realm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Realm Name</p></li>
<li><p><strong>user_session</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is Attribute Related To a User Session</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.HardcodedAttributeIdentityProviderMapper.attribute_name">
<em class="property">property </em><code class="sig-name descname">attribute_name</code><a class="headerlink" href="#pulumi_keycloak.HardcodedAttributeIdentityProviderMapper.attribute_name" title="Permalink to this definition">¶</a></dt>
<dd><p>OIDC Claim</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.HardcodedAttributeIdentityProviderMapper.attribute_value">
<em class="property">property </em><code class="sig-name descname">attribute_value</code><a class="headerlink" href="#pulumi_keycloak.HardcodedAttributeIdentityProviderMapper.attribute_value" title="Permalink to this definition">¶</a></dt>
<dd><p>User Attribute</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.HardcodedAttributeIdentityProviderMapper.identity_provider_alias">
<em class="property">property </em><code class="sig-name descname">identity_provider_alias</code><a class="headerlink" href="#pulumi_keycloak.HardcodedAttributeIdentityProviderMapper.identity_provider_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>IDP Alias</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.HardcodedAttributeIdentityProviderMapper.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_keycloak.HardcodedAttributeIdentityProviderMapper.name" title="Permalink to this definition">¶</a></dt>
<dd><p>IDP Mapper Name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.HardcodedAttributeIdentityProviderMapper.realm">
<em class="property">property </em><code class="sig-name descname">realm</code><a class="headerlink" href="#pulumi_keycloak.HardcodedAttributeIdentityProviderMapper.realm" title="Permalink to this definition">¶</a></dt>
<dd><p>Realm Name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.HardcodedAttributeIdentityProviderMapper.user_session">
<em class="property">property </em><code class="sig-name descname">user_session</code><a class="headerlink" href="#pulumi_keycloak.HardcodedAttributeIdentityProviderMapper.user_session" title="Permalink to this definition">¶</a></dt>
<dd><p>Is Attribute Related To a User Session</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.HardcodedAttributeIdentityProviderMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.HardcodedAttributeIdentityProviderMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.HardcodedAttributeIdentityProviderMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.HardcodedAttributeIdentityProviderMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.HardcodedRoleIdentityMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">HardcodedRoleIdentityMapper</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extra_config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity_provider_alias</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.HardcodedRoleIdentityMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a HardcodedRoleIdentityMapper resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] identity_provider_alias: IDP Alias
:param pulumi.Input[str] name: IDP Mapper Name
:param pulumi.Input[str] realm: Realm Name
:param pulumi.Input[str] role: Role Name</p>
<dl class="py method">
<dt id="pulumi_keycloak.HardcodedRoleIdentityMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extra_config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity_provider_alias</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.hardcoded_role_identity_mapper.HardcodedRoleIdentityMapper<a class="headerlink" href="#pulumi_keycloak.HardcodedRoleIdentityMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HardcodedRoleIdentityMapper resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>identity_provider_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IDP Alias</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IDP Mapper Name</p></li>
<li><p><strong>realm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Realm Name</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role Name</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.HardcodedRoleIdentityMapper.identity_provider_alias">
<em class="property">property </em><code class="sig-name descname">identity_provider_alias</code><a class="headerlink" href="#pulumi_keycloak.HardcodedRoleIdentityMapper.identity_provider_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>IDP Alias</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.HardcodedRoleIdentityMapper.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_keycloak.HardcodedRoleIdentityMapper.name" title="Permalink to this definition">¶</a></dt>
<dd><p>IDP Mapper Name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.HardcodedRoleIdentityMapper.realm">
<em class="property">property </em><code class="sig-name descname">realm</code><a class="headerlink" href="#pulumi_keycloak.HardcodedRoleIdentityMapper.realm" title="Permalink to this definition">¶</a></dt>
<dd><p>Realm Name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.HardcodedRoleIdentityMapper.role">
<em class="property">property </em><code class="sig-name descname">role</code><a class="headerlink" href="#pulumi_keycloak.HardcodedRoleIdentityMapper.role" title="Permalink to this definition">¶</a></dt>
<dd><p>Role Name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.HardcodedRoleIdentityMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.HardcodedRoleIdentityMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.HardcodedRoleIdentityMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.HardcodedRoleIdentityMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">IdentityProviderTokenExchangeScopePermission</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clients</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_alias</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a IdentityProviderTokenExchangeScopePermission resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[List[pulumi.Input[str]]] clients: Ids of the clients for which a policy will be created and set on scope based token exchange permission
:param pulumi.Input[str] policy_type: Type of policy that is created. At the moment only ‘client’ type is supported</p>
<dl class="py method">
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_idp_resource_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_resource_server_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_token_exchange_scope_permission_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clients</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_alias</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.identity_provider_token_exchange_scope_permission.IdentityProviderTokenExchangeScopePermission<a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IdentityProviderTokenExchangeScopePermission resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorization_idp_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource id representing the identity provider, this automatically created by keycloak</p></li>
<li><p><strong>authorization_resource_server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource server id representing the realm management client on which this permission is managed</p></li>
<li><p><strong>authorization_token_exchange_scope_permission_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Permission id representing the Permission with scope ‘Token Exchange’ and the resource ‘authorization_idp_resource_id’,
this automatically created by keycloak, the policy id will be set on this permission</p></li>
<li><p><strong>clients</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Ids of the clients for which a policy will be created and set on scope based token exchange permission</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Policy id that will be set on the scope based token exchange permission automatically created by enabling permissions on
the reference identity provider</p></li>
<li><p><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of policy that is created. At the moment only ‘client’ type is supported</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.authorization_idp_resource_id">
<em class="property">property </em><code class="sig-name descname">authorization_idp_resource_id</code><a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.authorization_idp_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource id representing the identity provider, this automatically created by keycloak</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.authorization_resource_server_id">
<em class="property">property </em><code class="sig-name descname">authorization_resource_server_id</code><a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.authorization_resource_server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource server id representing the realm management client on which this permission is managed</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.authorization_token_exchange_scope_permission_id">
<em class="property">property </em><code class="sig-name descname">authorization_token_exchange_scope_permission_id</code><a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.authorization_token_exchange_scope_permission_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Permission id representing the Permission with scope ‘Token Exchange’ and the resource ‘authorization_idp_resource_id’,
this automatically created by keycloak, the policy id will be set on this permission</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.clients">
<em class="property">property </em><code class="sig-name descname">clients</code><a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.clients" title="Permalink to this definition">¶</a></dt>
<dd><p>Ids of the clients for which a policy will be created and set on scope based token exchange permission</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.policy_id">
<em class="property">property </em><code class="sig-name descname">policy_id</code><a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Policy id that will be set on the scope based token exchange permission automatically created by enabling permissions on
the reference identity provider</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.policy_type">
<em class="property">property </em><code class="sig-name descname">policy_type</code><a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.policy_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of policy that is created. At the moment only ‘client’ type is supported</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">base_path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_timeout</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_login</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_ca_certificate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_insecure_skip_verify</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the keycloak package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout (in seconds) of the Keycloak client</p></li>
<li><p><strong>initial_login</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to login to Keycloak instance on provider initialization</p></li>
<li><p><strong>root_ca_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Allows x509 calls using an unknown CA certificate (for development purposes)</p></li>
<li><p><strong>tls_insecure_skip_verify</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allows ignoring insecure certificates when set to true. Defaults to false. Disabling security check is dangerous and
should be avoided.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base URL of the Keycloak instance, before <code class="docutils literal notranslate"><span class="pre">/auth</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.Realm">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">Realm</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan_login</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan_user_action</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_token_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_token_lifespan_for_implicit_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_theme</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_token_generated_by_admin_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_token_generated_by_user_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_theme</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">browser_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_authentication_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_signature_algorithm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">direct_grant_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name_html</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_authentication_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">duplicate_emails_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edit_username_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_theme</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internationalization</span><span class="p">:</span> <span class="n">Union[RealmInternationalizationArgs, Mapping[str, Any], Awaitable[Union[RealmInternationalizationArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_theme</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_with_email_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_idle_timeout</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_max_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_token_max_reuse</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_email_as_username</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remember_me</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_credentials_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_password_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">revoke_refresh_token</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_defenses</span><span class="p">:</span> <span class="n">Union[RealmSecurityDefensesArgs, Mapping[str, Any], Awaitable[Union[RealmSecurityDefensesArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">smtp_server</span><span class="p">:</span> <span class="n">Union[RealmSmtpServerArgs, Mapping[str, Any], Awaitable[Union[RealmSmtpServerArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_required</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_idle_timeout</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_max_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_managed_access</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verify_email</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.Realm" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Realm resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] browser_flow: Which flow should be used for BrowserFlow
:param pulumi.Input[str] client_authentication_flow: Which flow should be used for ClientAuthenticationFlow
:param pulumi.Input[str] direct_grant_flow: Which flow should be used for DirectGrantFlow
:param pulumi.Input[str] docker_authentication_flow: Which flow should be used for DockerAuthenticationFlow
:param pulumi.Input[str] password_policy: String that represents the passwordPolicies that are in place. Each policy is separated with ” and “. Supported policies</p>
<blockquote>
<div><p>can be found in the server-info providers page. example: “upperCase(1) and length(8) and forceExpiredPasswordChange(365)
and notUsername(undefined)”</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>registration_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which flow should be used for RegistrationFlow</p></li>
<li><p><strong>reset_credentials_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which flow should be used for ResetCredentialsFlow</p></li>
<li><p><strong>ssl_required</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SSL Required: Values can be ‘none’, ‘external’ or ‘all’.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.Realm.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan_login</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan_user_action</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_token_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_token_lifespan_for_implicit_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_theme</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_token_generated_by_admin_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_token_generated_by_user_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_theme</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">browser_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_authentication_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_signature_algorithm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">direct_grant_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name_html</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_authentication_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">duplicate_emails_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edit_username_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_theme</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internal_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internationalization</span><span class="p">:</span> <span class="n">Union[RealmInternationalizationArgs, Mapping[str, Any], Awaitable[Union[RealmInternationalizationArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_theme</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_with_email_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_idle_timeout</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_max_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_token_max_reuse</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_email_as_username</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remember_me</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_credentials_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_password_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">revoke_refresh_token</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_defenses</span><span class="p">:</span> <span class="n">Union[RealmSecurityDefensesArgs, Mapping[str, Any], Awaitable[Union[RealmSecurityDefensesArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">smtp_server</span><span class="p">:</span> <span class="n">Union[RealmSmtpServerArgs, Mapping[str, Any], Awaitable[Union[RealmSmtpServerArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_required</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_idle_timeout</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_max_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_managed_access</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verify_email</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.realm.Realm<a class="headerlink" href="#pulumi_keycloak.Realm.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Realm resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>browser_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which flow should be used for BrowserFlow</p></li>
<li><p><strong>client_authentication_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which flow should be used for ClientAuthenticationFlow</p></li>
<li><p><strong>direct_grant_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which flow should be used for DirectGrantFlow</p></li>
<li><p><strong>docker_authentication_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which flow should be used for DockerAuthenticationFlow</p></li>
<li><p><strong>password_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String that represents the passwordPolicies that are in place. Each policy is separated with ” and “. Supported policies
can be found in the server-info providers page. example: “upperCase(1) and length(8) and forceExpiredPasswordChange(365)
and notUsername(undefined)”</p></li>
<li><p><strong>registration_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which flow should be used for RegistrationFlow</p></li>
<li><p><strong>reset_credentials_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Which flow should be used for ResetCredentialsFlow</p></li>
<li><p><strong>ssl_required</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SSL Required: Values can be ‘none’, ‘external’ or ‘all’.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.browser_flow">
<em class="property">property </em><code class="sig-name descname">browser_flow</code><a class="headerlink" href="#pulumi_keycloak.Realm.browser_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>Which flow should be used for BrowserFlow</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.client_authentication_flow">
<em class="property">property </em><code class="sig-name descname">client_authentication_flow</code><a class="headerlink" href="#pulumi_keycloak.Realm.client_authentication_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>Which flow should be used for ClientAuthenticationFlow</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.direct_grant_flow">
<em class="property">property </em><code class="sig-name descname">direct_grant_flow</code><a class="headerlink" href="#pulumi_keycloak.Realm.direct_grant_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>Which flow should be used for DirectGrantFlow</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.docker_authentication_flow">
<em class="property">property </em><code class="sig-name descname">docker_authentication_flow</code><a class="headerlink" href="#pulumi_keycloak.Realm.docker_authentication_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>Which flow should be used for DockerAuthenticationFlow</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.password_policy">
<em class="property">property </em><code class="sig-name descname">password_policy</code><a class="headerlink" href="#pulumi_keycloak.Realm.password_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>String that represents the passwordPolicies that are in place. Each policy is separated with ” and “. Supported policies
can be found in the server-info providers page. example: “upperCase(1) and length(8) and forceExpiredPasswordChange(365)
and notUsername(undefined)”</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.registration_flow">
<em class="property">property </em><code class="sig-name descname">registration_flow</code><a class="headerlink" href="#pulumi_keycloak.Realm.registration_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>Which flow should be used for RegistrationFlow</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.reset_credentials_flow">
<em class="property">property </em><code class="sig-name descname">reset_credentials_flow</code><a class="headerlink" href="#pulumi_keycloak.Realm.reset_credentials_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>Which flow should be used for ResetCredentialsFlow</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.ssl_required">
<em class="property">property </em><code class="sig-name descname">ssl_required</code><a class="headerlink" href="#pulumi_keycloak.Realm.ssl_required" title="Permalink to this definition">¶</a></dt>
<dd><p>SSL Required: Values can be ‘none’, ‘external’ or ‘all’.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.Realm.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.Realm.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.Realm.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.RealmEvents">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">RealmEvents</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_events_details_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_events_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled_event_types</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events_expiration</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events_listeners</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.RealmEvents" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for managing Realm Events settings within Keycloak.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span> <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;test&quot;</span><span class="p">)</span>
<span class="n">realm_events</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">RealmEvents</span><span class="p">(</span><span class="s2">&quot;realmEvents&quot;</span><span class="p">,</span>
    <span class="n">admin_events_details_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">admin_events_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">enabled_event_types</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;LOGIN&quot;</span><span class="p">,</span>
        <span class="s2">&quot;LOGOUT&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">events_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">events_expiration</span><span class="o">=</span><span class="mi">3600</span><span class="p">,</span>
    <span class="n">events_listeners</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;jboss-logging&quot;</span><span class="p">],</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The name of the realm the event settings apply to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">admin_events_enabled</span></code> - (Optional) When true, admin events are saved to the database, making them available through the admin console. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">admin_events_details_enabled</span></code> - (Optional) When true, saved admin events will included detailed information for create/update requests. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">events_enabled</span></code> - (Optional) When true, events from <code class="docutils literal notranslate"><span class="pre">enabled_event_types</span></code> are saved to the database, making them available through the admin console. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">events_expiration</span></code> - (Optional) The amount of time in seconds events will be saved in the database. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> or never.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled_event_types</span></code> - (Optional) The event types that will be saved to the database. Omitting this field enables all event types. Defaults to <code class="docutils literal notranslate"><span class="pre">[]</span></code> or all event types.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">events_listeners</span></code> - (Optional) The event listeners that events should be sent to. Defaults to <code class="docutils literal notranslate"><span class="pre">[]</span></code> or none. Note that new realms enable the <code class="docutils literal notranslate"><span class="pre">jboss-logging</span></code> listener by default, and this resource will remove that unless it is specified.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.RealmEvents.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_events_details_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_events_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled_event_types</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events_expiration</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events_listeners</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.realm_events.RealmEvents<a class="headerlink" href="#pulumi_keycloak.RealmEvents.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RealmEvents resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.RealmEvents.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.RealmEvents.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.RealmEvents.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.RealmEvents.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.RequiredAction">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">RequiredAction</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alias</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_action</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.RequiredAction" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a RequiredAction resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_keycloak.RequiredAction.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alias</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_action</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.required_action.RequiredAction<a class="headerlink" href="#pulumi_keycloak.RequiredAction.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RequiredAction resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.RequiredAction.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.RequiredAction.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.RequiredAction.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.RequiredAction.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.Role">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">Role</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">composite_roles</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.Role" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing roles within Keycloak.</p>
<p>Roles allow you define privileges within Keycloak and map them to users
and groups.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">)</span>
<span class="n">realm_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;realmRole&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;My Realm Role&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">)</span>
<span class="n">client</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">openid</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="s2">&quot;client&quot;</span><span class="p">,</span>
    <span class="n">access_type</span><span class="o">=</span><span class="s2">&quot;BEARER-ONLY&quot;</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="s2">&quot;client&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">client_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;clientRole&quot;</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="n">keycloak_client</span><span class="p">[</span><span class="s2">&quot;client&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;My Client Role&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">)</span>
<span class="n">create_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;createRole&quot;</span><span class="p">,</span> <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">read_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;readRole&quot;</span><span class="p">,</span> <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">update_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;updateRole&quot;</span><span class="p">,</span> <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">delete_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;deleteRole&quot;</span><span class="p">,</span> <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">client</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">openid</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="s2">&quot;client&quot;</span><span class="p">,</span>
    <span class="n">access_type</span><span class="o">=</span><span class="s2">&quot;BEARER-ONLY&quot;</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="s2">&quot;client&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">client_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;clientRole&quot;</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="n">keycloak_client</span><span class="p">[</span><span class="s2">&quot;client&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;My Client Role&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">admin_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;adminRole&quot;</span><span class="p">,</span>
    <span class="n">composite_roles</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;</span><span class="si">{keycloak_role.create_role.id}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="s2">&quot;</span><span class="si">{keycloak_role.read_role.id}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="s2">&quot;</span><span class="si">{keycloak_role.update_role.id}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="s2">&quot;</span><span class="si">{keycloak_role.delete_role.id}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="s2">&quot;</span><span class="si">{keycloak_role.client_role.id}</span><span class="s2">&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this role exists within.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> - (Optional) When specified, this role will be created as
a client role attached to the client with the provided ID</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The name of the role</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> - (Optional) The description of the role</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">composite_roles</span></code> - (Optional) When specified, this role will be a
composite role, composed of all roles that have an ID present within
this list.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.Role.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">composite_roles</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.role.Role<a class="headerlink" href="#pulumi_keycloak.Role.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Role resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Role.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.Role.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.Role.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.Role.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_verified</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">federated_identities</span><span class="p">:</span> <span class="n">Union[List[Union[UserFederatedIdentityArgs, Mapping[str, Any], Awaitable[Union[UserFederatedIdentityArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[UserFederatedIdentityArgs, Mapping[str, Any], Awaitable[Union[UserFederatedIdentityArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">first_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_password</span><span class="p">:</span> <span class="n">Union[UserInitialPasswordArgs, Mapping[str, Any], Awaitable[Union[UserInitialPasswordArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing Users within Keycloak.</p>
<p>This resource was created primarily to enable the acceptance tests for the <code class="docutils literal notranslate"><span class="pre">Group</span></code> resource.
Creating users within Keycloak is not recommended. Instead, users should be federated from external sources
by configuring user federation providers or identity providers.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">)</span>
<span class="n">user</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;bob@domain.com&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">first_name</span><span class="o">=</span><span class="s2">&quot;Bob&quot;</span><span class="p">,</span>
    <span class="n">last_name</span><span class="o">=</span><span class="s2">&quot;Bobson&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;bob&quot;</span><span class="p">)</span>
<span class="n">user_with_initial_password</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;userWithInitialPassword&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;alice@domain.com&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">first_name</span><span class="o">=</span><span class="s2">&quot;Alice&quot;</span><span class="p">,</span>
    <span class="n">initial_password</span><span class="o">=</span><span class="n">keycloak</span><span class="o">.</span><span class="n">UserInitialPasswordArgs</span><span class="p">(</span>
        <span class="n">temporary</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">value</span><span class="o">=</span><span class="s2">&quot;some password&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">last_name</span><span class="o">=</span><span class="s2">&quot;Aliceberg&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;alice&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>The following arguments are supported:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this user belongs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> - (Required) The unique username of this user.</p></li>
<li><dl class="simple">
<dt><code class="docutils literal notranslate"><span class="pre">initial_password</span></code> (Optional) When given, the user’s initial password will be set.</dt><dd><p>This attribute is only respected during initial user creation.</p>
</dd>
</dl>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (Required) The initial password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">temporary</span></code> (Optional) If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the initial password is set up for renewal on first use. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> - (Optional) When false, this user cannot log in. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">email</span></code> - (Optional) The user’s email.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">first_name</span></code> - (Optional) The user’s first name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">last_name</span></code> - (Optional) The user’s last name.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_verified</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">federated_identities</span><span class="p">:</span> <span class="n">Union[List[Union[UserFederatedIdentityArgs, Mapping[str, Any], Awaitable[Union[UserFederatedIdentityArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[UserFederatedIdentityArgs, Mapping[str, Any], Awaitable[Union[UserFederatedIdentityArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">first_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_password</span><span class="p">:</span> <span class="n">Union[UserInitialPasswordArgs, Mapping[str, Any], Awaitable[Union[UserInitialPasswordArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.user.User<a class="headerlink" href="#pulumi_keycloak.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.UserRoles">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">UserRoles</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_ids</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.UserRoles" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a UserRoles resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_keycloak.UserRoles.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_ids</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.user_roles.UserRoles<a class="headerlink" href="#pulumi_keycloak.UserRoles.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserRoles resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.UserRoles.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.UserRoles.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.UserRoles.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.UserRoles.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.UserTemplateImporterIdentityProviderMapper">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">UserTemplateImporterIdentityProviderMapper</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extra_config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity_provider_alias</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.UserTemplateImporterIdentityProviderMapper" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a UserTemplateImporterIdentityProviderMapper resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] identity_provider_alias: IDP Alias
:param pulumi.Input[str] name: IDP Mapper Name
:param pulumi.Input[str] realm: Realm Name
:param pulumi.Input[str] template: Username For Template Import</p>
<dl class="py method">
<dt id="pulumi_keycloak.UserTemplateImporterIdentityProviderMapper.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extra_config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identity_provider_alias</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.user_template_importer_identity_provider_mapper.UserTemplateImporterIdentityProviderMapper<a class="headerlink" href="#pulumi_keycloak.UserTemplateImporterIdentityProviderMapper.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserTemplateImporterIdentityProviderMapper resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>identity_provider_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IDP Alias</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IDP Mapper Name</p></li>
<li><p><strong>realm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Realm Name</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username For Template Import</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.UserTemplateImporterIdentityProviderMapper.identity_provider_alias">
<em class="property">property </em><code class="sig-name descname">identity_provider_alias</code><a class="headerlink" href="#pulumi_keycloak.UserTemplateImporterIdentityProviderMapper.identity_provider_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>IDP Alias</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.UserTemplateImporterIdentityProviderMapper.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_keycloak.UserTemplateImporterIdentityProviderMapper.name" title="Permalink to this definition">¶</a></dt>
<dd><p>IDP Mapper Name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.UserTemplateImporterIdentityProviderMapper.realm">
<em class="property">property </em><code class="sig-name descname">realm</code><a class="headerlink" href="#pulumi_keycloak.UserTemplateImporterIdentityProviderMapper.realm" title="Permalink to this definition">¶</a></dt>
<dd><p>Realm Name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.UserTemplateImporterIdentityProviderMapper.template">
<em class="property">property </em><code class="sig-name descname">template</code><a class="headerlink" href="#pulumi_keycloak.UserTemplateImporterIdentityProviderMapper.template" title="Permalink to this definition">¶</a></dt>
<dd><p>Username For Template Import</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.UserTemplateImporterIdentityProviderMapper.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.UserTemplateImporterIdentityProviderMapper.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.UserTemplateImporterIdentityProviderMapper.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.UserTemplateImporterIdentityProviderMapper.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.get_group">
<code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">get_group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.get_group.AwaitableGetGroupResult<a class="headerlink" href="#pulumi_keycloak.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch properties of a Keycloak group for
usage with other resources, such as <code class="docutils literal notranslate"><span class="pre">GroupRoles</span></code>.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this group exists within.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The name of the group</p></li>
</ul>
<p>In addition to the arguments listed above, the following computed attributes are exported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> - The unique ID of the group, which can be used as an argument to
other resources supported by this provider.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_keycloak.get_realm">
<code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">get_realm</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">attributes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name_html</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internationalizations</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetRealmInternationalizationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_defenses</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetRealmSecurityDefenseArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">smtp_servers</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>Union<span class="p">[</span>GetRealmSmtpServerArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.get_realm.AwaitableGetRealmResult<a class="headerlink" href="#pulumi_keycloak.get_realm" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch properties of a Keycloak realm for
usage with other resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">get_realm</span><span class="p">(</span><span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">)</span>
<span class="n">group</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;group&quot;</span><span class="p">,</span> <span class="n">realm_id</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;keycloak_realm&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm</span></code> - (Required) The realm name.</p></li>
</ul>
<p>See the docs for the <code class="docutils literal notranslate"><span class="pre">Realm</span></code> resource for details on the exported attributes.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_keycloak.get_realm_keys">
<code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">get_realm_keys</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">algorithms</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statuses</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.get_realm_keys.AwaitableGetRealmKeysResult<a class="headerlink" href="#pulumi_keycloak.get_realm_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the keys of a realm. Keys can be filtered by algorithm and status.</p>
<p>Remarks:</p>
<ul class="simple">
<li><p>A key must meet all filter criteria</p></li>
<li><p>This datasource may return more than one value.</p></li>
<li><p>If no key matches the filter criteria, then an error is returned.</p></li>
</ul>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm of which the keys are retrieved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">algorithms</span></code> - (Optional) When specified, keys are filtered by algorithm (values for algorithm: <code class="docutils literal notranslate"><span class="pre">HS256</span></code>, <code class="docutils literal notranslate"><span class="pre">RS256</span></code>,<code class="docutils literal notranslate"><span class="pre">AES</span></code>, …)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> - (Optional) When specified, keys are filtered by status (values for status: <code class="docutils literal notranslate"><span class="pre">ACTIVE</span></code>, <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code> and <code class="docutils literal notranslate"><span class="pre">PASSIVE</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_keycloak.get_role">
<code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">get_role</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.get_role.AwaitableGetRoleResult<a class="headerlink" href="#pulumi_keycloak.get_role" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch properties of a Keycloak role for
usage with other resources, such as <code class="docutils literal notranslate"><span class="pre">GroupRoles</span></code>.</p>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">realm_id</span></code> - (Required) The realm this role exists within.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> - (Optional) When specified, this role is assumed to be a
client role belonging to the client with the provided ID</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The name of the role</p></li>
</ul>
<p>In addition to the arguments listed above, the following computed attributes are exported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> - The unique ID of the role, which can be used as an argument to
other resources supported by this provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> - The description of the role.</p></li>
</ul>
</dd></dl>

</div>
