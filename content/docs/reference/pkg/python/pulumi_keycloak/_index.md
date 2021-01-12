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
<dd><p>Allows for creating and managing an attribute importer identity provider mapper within Keycloak.</p>
<p>The attribute importer mapper can be used to map attributes from externally defined users to attributes or properties of the imported Keycloak user:</p>
<ul class="simple">
<li><p>For the OIDC identity provider, this will map a claim on the ID or access token to an attribute for the imported Keycloak user.</p></li>
<li><p>For the SAML identity provider, this will map a SAML attribute found within the assertion to an attribute for the imported Keycloak user.</p></li>
<li><p>For social identity providers, this will map a JSON field from the user profile to an attribute for the imported Keycloak user.</p></li>
</ul>
<blockquote>
<div><p>If you are using Keycloak 10 or higher, you will need to specify the <code class="docutils literal notranslate"><span class="pre">extra_config</span></code> argument in order to define a <code class="docutils literal notranslate"><span class="pre">syncMode</span></code> for the mapper.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">oidc_identity_provider</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">oidc</span><span class="o">.</span><span class="n">IdentityProvider</span><span class="p">(</span><span class="s2">&quot;oidcIdentityProvider&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">alias</span><span class="o">=</span><span class="s2">&quot;oidc&quot;</span><span class="p">,</span>
    <span class="n">authorization_url</span><span class="o">=</span><span class="s2">&quot;https://example.com/auth&quot;</span><span class="p">,</span>
    <span class="n">token_url</span><span class="o">=</span><span class="s2">&quot;https://example.com/token&quot;</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="s2">&quot;example_id&quot;</span><span class="p">,</span>
    <span class="n">client_secret</span><span class="o">=</span><span class="s2">&quot;example_token&quot;</span><span class="p">,</span>
    <span class="n">default_scopes</span><span class="o">=</span><span class="s2">&quot;openid random profile&quot;</span><span class="p">)</span>
<span class="n">oidc_attribute_importer_identity_provider_mapper</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">AttributeImporterIdentityProviderMapper</span><span class="p">(</span><span class="s2">&quot;oidcAttributeImporterIdentityProviderMapper&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">claim_name</span><span class="o">=</span><span class="s2">&quot;my-email-claim&quot;</span><span class="p">,</span>
    <span class="n">identity_provider_alias</span><span class="o">=</span><span class="n">oidc_identity_provider</span><span class="o">.</span><span class="n">alias</span><span class="p">,</span>
    <span class="n">user_attribute</span><span class="o">=</span><span class="s2">&quot;email&quot;</span><span class="p">,</span>
    <span class="n">extra_config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;syncMode&quot;</span><span class="p">:</span> <span class="s2">&quot;INHERIT&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<p>Identity provider mappers can be imported using the format <code class="docutils literal notranslate"><span class="pre">{{realm_id}}/{{idp_alias}}/{{idp_mapper_id}}</span></code>, where <code class="docutils literal notranslate"><span class="pre">idp_alias</span></code> is the identity provider alias, and <code class="docutils literal notranslate"><span class="pre">idp_mapper_id</span></code> is the unique ID that Keycloak assigns to the mapper upon creation. This value can be found in the URI when editing this mapper in the GUI, and is typically a GUID. Examplebash</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import keycloak:index/attributeImporterIdentityProviderMapper:AttributeImporterIdentityProviderMapper test_mapper my-realm/my-mapper/f446db98-7133-4e30-b18a-3d28fde7ca1b
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attribute_friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For SAML based providers, this is the friendly name of the attribute to search for in the assertion. Conflicts with <code class="docutils literal notranslate"><span class="pre">attribute_name</span></code>.</p></li>
<li><p><strong>attribute_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For SAML based providers, this is the name of the attribute to search for in the assertion. Conflicts with <code class="docutils literal notranslate"><span class="pre">attribute_friendly_name</span></code>.</p></li>
<li><p><strong>claim_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For OIDC based providers, this is the name of the claim to use.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>extra_config</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Key/value attributes to add to the identity provider mapper model that is persisted to Keycloak. This can be used to extend the base model with new Keycloak features.</p></li>
<li><p><strong>identity_provider_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alias of the associated identity provider.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the mapper.</p></li>
<li><p><strong>realm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the realm.</p></li>
<li><p><strong>user_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user attribute or property name to store the mapped result.</p></li>
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
<li><p><strong>attribute_friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For SAML based providers, this is the friendly name of the attribute to search for in the assertion. Conflicts with <code class="docutils literal notranslate"><span class="pre">attribute_name</span></code>.</p></li>
<li><p><strong>attribute_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For SAML based providers, this is the name of the attribute to search for in the assertion. Conflicts with <code class="docutils literal notranslate"><span class="pre">attribute_friendly_name</span></code>.</p></li>
<li><p><strong>claim_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For OIDC based providers, this is the name of the claim to use.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>extra_config</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Key/value attributes to add to the identity provider mapper model that is persisted to Keycloak. This can be used to extend the base model with new Keycloak features.</p></li>
<li><p><strong>identity_provider_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alias of the associated identity provider.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the mapper.</p></li>
<li><p><strong>realm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the realm.</p></li>
<li><p><strong>user_attribute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user attribute or property name to store the mapped result.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper.attribute_friendly_name">
<em class="property">property </em><code class="sig-name descname">attribute_friendly_name</code><a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper.attribute_friendly_name" title="Permalink to this definition">¶</a></dt>
<dd><p>For SAML based providers, this is the friendly name of the attribute to search for in the assertion. Conflicts with <code class="docutils literal notranslate"><span class="pre">attribute_name</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper.attribute_name">
<em class="property">property </em><code class="sig-name descname">attribute_name</code><a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper.attribute_name" title="Permalink to this definition">¶</a></dt>
<dd><p>For SAML based providers, this is the name of the attribute to search for in the assertion. Conflicts with <code class="docutils literal notranslate"><span class="pre">attribute_friendly_name</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper.claim_name">
<em class="property">property </em><code class="sig-name descname">claim_name</code><a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper.claim_name" title="Permalink to this definition">¶</a></dt>
<dd><p>For OIDC based providers, this is the name of the claim to use.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper.extra_config">
<em class="property">property </em><code class="sig-name descname">extra_config</code><a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper.extra_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Key/value attributes to add to the identity provider mapper model that is persisted to Keycloak. This can be used to extend the base model with new Keycloak features.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper.identity_provider_alias">
<em class="property">property </em><code class="sig-name descname">identity_provider_alias</code><a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper.identity_provider_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>The alias of the associated identity provider.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the mapper.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper.realm">
<em class="property">property </em><code class="sig-name descname">realm</code><a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper.realm" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the realm.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.AttributeImporterIdentityProviderMapper.user_attribute">
<em class="property">property </em><code class="sig-name descname">user_attribute</code><a class="headerlink" href="#pulumi_keycloak.AttributeImporterIdentityProviderMapper.user_attribute" title="Permalink to this definition">¶</a></dt>
<dd><p>The user attribute or property name to store the mapped result.</p>
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
<dt id="pulumi_keycloak.AwaitableGetAuthenticationExecutionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">AwaitableGetAuthenticationExecutionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_flow_alias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.AwaitableGetAuthenticationExecutionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_keycloak.AwaitableGetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">AwaitableGetGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.AwaitableGetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_keycloak.AwaitableGetRealmKeysResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">AwaitableGetRealmKeysResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">algorithms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statuses</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.AwaitableGetRealmKeysResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_keycloak.AwaitableGetRealmResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">AwaitableGetRealmResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_code_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan_login</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan_user_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_token_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_token_lifespan_for_implicit_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_theme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_token_generated_by_admin_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_token_generated_by_user_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_theme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">browser_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_authentication_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_signature_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">direct_grant_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name_html</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_authentication_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">duplicate_emails_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edit_username_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_theme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internal_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internationalizations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_theme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_with_email_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_idle_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_max_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_max_lifespan_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_token_max_reuse</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_email_as_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remember_me</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_credentials_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_password_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">revoke_refresh_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_defenses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">smtp_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_required</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_idle_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_idle_timeout_remember_me</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_max_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_max_lifespan_remember_me</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_managed_access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verify_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_authn_passwordless_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_authn_policy</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.AwaitableGetRealmResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_keycloak.AwaitableGetRoleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">AwaitableGetRoleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.AwaitableGetRoleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_keycloak.AwaitableGetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">AwaitableGetUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_verified</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">federated_identities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">first_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.AwaitableGetUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_keycloak.CustomUserFederation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">CustomUserFederation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cache_policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.CustomUserFederation" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom user federation providers can be imported using the format <code class="docutils literal notranslate"><span class="pre">{{realm_id}}/{{custom_user_federation_id}}</span></code>. The ID of the custom user federation provider can be found within the Keycloak GUI and is typically a GUIDbash</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import keycloak:index/customUserFederation:CustomUserFederation custom_user_federation my-realm/af2a6ca3-e4d7-49c3-b08b-1b3c70b4b860
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cache_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Can be one of <code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code>, <code class="docutils literal notranslate"><span class="pre">EVICT_DAILY</span></code>, <code class="docutils literal notranslate"><span class="pre">EVICT_WEEKLY</span></code>, <code class="docutils literal notranslate"><span class="pre">MAX_LIFESPAN</span></code>, or <code class="docutils literal notranslate"><span class="pre">NO_CACHE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code>.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – The provider configuration handed over to your custom user federation provider.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">false</span></code>, this provider will not be used when performing queries for users. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the provider when displayed in the console.</p></li>
<li><p><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be set to the realms’ <code class="docutils literal notranslate"><span class="pre">internal_id</span></code>  when it differs from the realm. This can happen when existing resources are imported into the state.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Priority of this provider when looking up users. Lower values are first. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><strong>provider_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID of the custom provider, specified in the <code class="docutils literal notranslate"><span class="pre">getId</span></code> implementation for the <code class="docutils literal notranslate"><span class="pre">UserStorageProviderFactory</span></code> interface.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm that this provider will provide user federation for.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.CustomUserFederation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cache_policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.custom_user_federation.CustomUserFederation<a class="headerlink" href="#pulumi_keycloak.CustomUserFederation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CustomUserFederation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cache_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Can be one of <code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code>, <code class="docutils literal notranslate"><span class="pre">EVICT_DAILY</span></code>, <code class="docutils literal notranslate"><span class="pre">EVICT_WEEKLY</span></code>, <code class="docutils literal notranslate"><span class="pre">MAX_LIFESPAN</span></code>, or <code class="docutils literal notranslate"><span class="pre">NO_CACHE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code>.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – The provider configuration handed over to your custom user federation provider.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">false</span></code>, this provider will not be used when performing queries for users. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the provider when displayed in the console.</p></li>
<li><p><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be set to the realms’ <code class="docutils literal notranslate"><span class="pre">internal_id</span></code>  when it differs from the realm. This can happen when existing resources are imported into the state.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Priority of this provider when looking up users. Lower values are first. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><strong>provider_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID of the custom provider, specified in the <code class="docutils literal notranslate"><span class="pre">getId</span></code> implementation for the <code class="docutils literal notranslate"><span class="pre">UserStorageProviderFactory</span></code> interface.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm that this provider will provide user federation for.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.CustomUserFederation.cache_policy">
<em class="property">property </em><code class="sig-name descname">cache_policy</code><a class="headerlink" href="#pulumi_keycloak.CustomUserFederation.cache_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be one of <code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code>, <code class="docutils literal notranslate"><span class="pre">EVICT_DAILY</span></code>, <code class="docutils literal notranslate"><span class="pre">EVICT_WEEKLY</span></code>, <code class="docutils literal notranslate"><span class="pre">MAX_LIFESPAN</span></code>, or <code class="docutils literal notranslate"><span class="pre">NO_CACHE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.CustomUserFederation.config">
<em class="property">property </em><code class="sig-name descname">config</code><a class="headerlink" href="#pulumi_keycloak.CustomUserFederation.config" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider configuration handed over to your custom user federation provider.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.CustomUserFederation.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_keycloak.CustomUserFederation.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">false</span></code>, this provider will not be used when performing queries for users. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.CustomUserFederation.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_keycloak.CustomUserFederation.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name of the provider when displayed in the console.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.CustomUserFederation.parent_id">
<em class="property">property </em><code class="sig-name descname">parent_id</code><a class="headerlink" href="#pulumi_keycloak.CustomUserFederation.parent_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Must be set to the realms’ <code class="docutils literal notranslate"><span class="pre">internal_id</span></code>  when it differs from the realm. This can happen when existing resources are imported into the state.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.CustomUserFederation.priority">
<em class="property">property </em><code class="sig-name descname">priority</code><a class="headerlink" href="#pulumi_keycloak.CustomUserFederation.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Priority of this provider when looking up users. Lower values are first. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.CustomUserFederation.provider_id">
<em class="property">property </em><code class="sig-name descname">provider_id</code><a class="headerlink" href="#pulumi_keycloak.CustomUserFederation.provider_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID of the custom provider, specified in the <code class="docutils literal notranslate"><span class="pre">getId</span></code> implementation for the <code class="docutils literal notranslate"><span class="pre">UserStorageProviderFactory</span></code> interface.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.CustomUserFederation.realm_id">
<em class="property">property </em><code class="sig-name descname">realm_id</code><a class="headerlink" href="#pulumi_keycloak.CustomUserFederation.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm that this provider will provide user federation for.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">DefaultGroups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.DefaultGroups" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for managing a realm’s default groups.</p>
<blockquote>
<div><p>You should not use <code class="docutils literal notranslate"><span class="pre">DefaultGroups</span></code> with a group whose members are managed by <code class="docutils literal notranslate"><span class="pre">GroupMemberships</span></code>.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">group</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;group&quot;</span><span class="p">,</span> <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">default</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">DefaultGroups</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">group_ids</span><span class="o">=</span><span class="p">[</span><span class="n">group</span><span class="o">.</span><span class="n">id</span><span class="p">])</span>
</pre></div>
</div>
<p>Default groups can be imported using the format <code class="docutils literal notranslate"><span class="pre">{{realm_id}}</span></code> where <code class="docutils literal notranslate"><span class="pre">realm_id</span></code> is the realm the group exists in. Examplebash</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import keycloak:index/defaultGroups:DefaultGroups default my-realm
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A set of group ids that should be default groups on the realm referenced by <code class="docutils literal notranslate"><span class="pre">realm_id</span></code>.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this group exists in.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.DefaultGroups.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.default_groups.DefaultGroups<a class="headerlink" href="#pulumi_keycloak.DefaultGroups.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DefaultGroups resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A set of group ids that should be default groups on the realm referenced by <code class="docutils literal notranslate"><span class="pre">realm_id</span></code>.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this group exists in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.DefaultGroups.group_ids">
<em class="property">property </em><code class="sig-name descname">group_ids</code><a class="headerlink" href="#pulumi_keycloak.DefaultGroups.group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of group ids that should be default groups on the realm referenced by <code class="docutils literal notranslate"><span class="pre">realm_id</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.DefaultGroups.realm_id">
<em class="property">property </em><code class="sig-name descname">realm_id</code><a class="headerlink" href="#pulumi_keycloak.DefaultGroups.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm this group exists in.</p>
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
<dd><p>Allows for creating and managing protocol mappers for both types of clients (openid-connect and saml) within Keycloak.</p>
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
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">saml_client</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">saml</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="s2">&quot;samlClient&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="s2">&quot;test-client&quot;</span><span class="p">)</span>
<span class="n">saml_hardcode_attribute_mapper</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">GenericClientProtocolMapper</span><span class="p">(</span><span class="s2">&quot;samlHardcodeAttributeMapper&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="n">saml_client</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">protocol</span><span class="o">=</span><span class="s2">&quot;saml&quot;</span><span class="p">,</span>
    <span class="n">protocol_mapper</span><span class="o">=</span><span class="s2">&quot;saml-hardcode-attribute-mapper&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;attribute.name&quot;</span><span class="p">:</span> <span class="s2">&quot;name&quot;</span><span class="p">,</span>
        <span class="s2">&quot;attribute.nameformat&quot;</span><span class="p">:</span> <span class="s2">&quot;Basic&quot;</span><span class="p">,</span>
        <span class="s2">&quot;attribute.value&quot;</span><span class="p">:</span> <span class="s2">&quot;value&quot;</span><span class="p">,</span>
        <span class="s2">&quot;friendly.name&quot;</span><span class="p">:</span> <span class="s2">&quot;display name&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<p>Protocol mappers can be imported using the following format<code class="docutils literal notranslate"><span class="pre">{{realm_id}}/client/{{client_keycloak_id}}/{{protocol_mapper_id}}</span></code> Examplebash</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import keycloak:index/genericClientProtocolMapper:GenericClientProtocolMapper saml_hardcode_attribute_mapper my-realm/client/a7202154-8793-4656-b655-1dd18c181e14/71602afa-f7d1-4788-8c49-ef8fd00af0f4
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client this protocol mapper is attached to.</p></li>
<li><p><strong>client_scope_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mapper’s associated client scope. Cannot be used at the same time as client_id.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map with key / value pairs for configuring the protocol mapper. The supported keys depends on the protocol mapper.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of this protocol mapper in the GUI.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of client (either <code class="docutils literal notranslate"><span class="pre">openid-connect</span></code> or <code class="docutils literal notranslate"><span class="pre">saml</span></code>). The type must match the type of the client.</p></li>
<li><p><strong>protocol_mapper</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the protocol mapper. The protocol mapper must be compatible with the specified client.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this protocol mapper exists within.</p></li>
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
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client this protocol mapper is attached to.</p></li>
<li><p><strong>client_scope_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mapper’s associated client scope. Cannot be used at the same time as client_id.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map with key / value pairs for configuring the protocol mapper. The supported keys depends on the protocol mapper.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name of this protocol mapper in the GUI.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of client (either <code class="docutils literal notranslate"><span class="pre">openid-connect</span></code> or <code class="docutils literal notranslate"><span class="pre">saml</span></code>). The type must match the type of the client.</p></li>
<li><p><strong>protocol_mapper</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the protocol mapper. The protocol mapper must be compatible with the specified client.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this protocol mapper exists within.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientProtocolMapper.client_id">
<em class="property">property </em><code class="sig-name descname">client_id</code><a class="headerlink" href="#pulumi_keycloak.GenericClientProtocolMapper.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The client this protocol mapper is attached to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientProtocolMapper.client_scope_id">
<em class="property">property </em><code class="sig-name descname">client_scope_id</code><a class="headerlink" href="#pulumi_keycloak.GenericClientProtocolMapper.client_scope_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The mapper’s associated client scope. Cannot be used at the same time as client_id.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientProtocolMapper.config">
<em class="property">property </em><code class="sig-name descname">config</code><a class="headerlink" href="#pulumi_keycloak.GenericClientProtocolMapper.config" title="Permalink to this definition">¶</a></dt>
<dd><p>A map with key / value pairs for configuring the protocol mapper. The supported keys depends on the protocol mapper.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientProtocolMapper.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_keycloak.GenericClientProtocolMapper.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name of this protocol mapper in the GUI.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientProtocolMapper.protocol">
<em class="property">property </em><code class="sig-name descname">protocol</code><a class="headerlink" href="#pulumi_keycloak.GenericClientProtocolMapper.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of client (either <code class="docutils literal notranslate"><span class="pre">openid-connect</span></code> or <code class="docutils literal notranslate"><span class="pre">saml</span></code>). The type must match the type of the client.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientProtocolMapper.protocol_mapper">
<em class="property">property </em><code class="sig-name descname">protocol_mapper</code><a class="headerlink" href="#pulumi_keycloak.GenericClientProtocolMapper.protocol_mapper" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the protocol mapper. The protocol mapper must be compatible with the specified client.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientProtocolMapper.realm_id">
<em class="property">property </em><code class="sig-name descname">realm_id</code><a class="headerlink" href="#pulumi_keycloak.GenericClientProtocolMapper.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm this protocol mapper exists within.</p>
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
<dd><p>Allow for creating and managing a client’s scope mappings within Keycloak.</p>
<p>By default, all the user role mappings of the user are added as claims within the token (OIDC) or assertion (SAML). When
<code class="docutils literal notranslate"><span class="pre">full_scope_allowed</span></code> is set to <code class="docutils literal notranslate"><span class="pre">false</span></code> for a client, role scope mapping allows you to limit the roles that get declared
inside an access token for a client.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">client</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">openid</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="s2">&quot;client&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="s2">&quot;client&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">access_type</span><span class="o">=</span><span class="s2">&quot;BEARER-ONLY&quot;</span><span class="p">)</span>
<span class="n">realm_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;realmRole&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;My Realm Role&quot;</span><span class="p">)</span>
<span class="n">client_role_mapper</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">GenericClientRoleMapper</span><span class="p">(</span><span class="s2">&quot;clientRoleMapper&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="n">client</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">role_id</span><span class="o">=</span><span class="n">realm_role</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">client_a</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">openid</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="s2">&quot;clientA&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="s2">&quot;client-a&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">access_type</span><span class="o">=</span><span class="s2">&quot;BEARER-ONLY&quot;</span><span class="p">,</span>
    <span class="n">full_scope_allowed</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">client_role_a</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;clientRoleA&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="n">client_a</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;My Client Role&quot;</span><span class="p">)</span>
<span class="n">client_b</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">openid</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="s2">&quot;clientB&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="s2">&quot;client-b&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">access_type</span><span class="o">=</span><span class="s2">&quot;BEARER-ONLY&quot;</span><span class="p">)</span>
<span class="n">client_role_b</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;clientRoleB&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="n">client_b</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;My Client Role&quot;</span><span class="p">)</span>
<span class="n">client_b_role_mapper</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">GenericClientRoleMapper</span><span class="p">(</span><span class="s2">&quot;clientBRoleMapper&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="n">keycloak_client</span><span class="p">[</span><span class="s2">&quot;client_b&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">role_id</span><span class="o">=</span><span class="n">client_role_a</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">client_scope</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">openid</span><span class="o">.</span><span class="n">ClientScope</span><span class="p">(</span><span class="s2">&quot;clientScope&quot;</span><span class="p">,</span> <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">realm_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;realmRole&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;My Realm Role&quot;</span><span class="p">)</span>
<span class="n">client_role_mapper</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">GenericClientRoleMapper</span><span class="p">(</span><span class="s2">&quot;clientRoleMapper&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">client_scope_id</span><span class="o">=</span><span class="n">client_scope</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">role_id</span><span class="o">=</span><span class="n">realm_role</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">client</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">openid</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="s2">&quot;client&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="s2">&quot;client&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">access_type</span><span class="o">=</span><span class="s2">&quot;BEARER-ONLY&quot;</span><span class="p">)</span>
<span class="n">client_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;clientRole&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="n">client</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;My Client Role&quot;</span><span class="p">)</span>
<span class="n">client_scope</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">openid</span><span class="o">.</span><span class="n">ClientScope</span><span class="p">(</span><span class="s2">&quot;clientScope&quot;</span><span class="p">,</span> <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">client_b_role_mapper</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">GenericClientRoleMapper</span><span class="p">(</span><span class="s2">&quot;clientBRoleMapper&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">client_scope_id</span><span class="o">=</span><span class="n">keycloak_client_scope</span><span class="p">[</span><span class="s2">&quot;client_scope&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">role_id</span><span class="o">=</span><span class="n">client_role</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<p>Generic client role mappers can be imported using one of the following two formats- When mapping a role to a client, use the format <code class="docutils literal notranslate"><span class="pre">{{realmId}}/client/{{clientId}}/scope-mappings/{{roleClientId}}/{{roleId}}</span></code> - When mapping a role to a client scope, use the format <code class="docutils literal notranslate"><span class="pre">{{realmId}}/client-scope/{{clientScopeId}}/scope-mappings/{{roleClientId}}/{{roleId}}</span></code> Examplebash</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import keycloak:index/genericClientRoleMapper:GenericClientRoleMapper client_role_mapper my-realm/client/23888550-5dcd-41f6-85ba-554233021e9c/scope-mappings/ce51f004-bdfb-4dd5-a963-c4487d2dec5b/ff3aa49f-bc07-4030-8783-41918c3614a3
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the client this role mapper should be added to. Conflicts with <code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code>. This argument is required if <code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> is not set.</p></li>
<li><p><strong>client_scope_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the client scope this role mapper should be added to. Conflicts with <code class="docutils literal notranslate"><span class="pre">client_id</span></code>. This argument is required if <code class="docutils literal notranslate"><span class="pre">client_id</span></code> is not set.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this role mapper exists within.</p></li>
<li><p><strong>role_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the role to be added to this role mapper.</p></li>
</ul>
</dd>
</dl>
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
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the client this role mapper should be added to. Conflicts with <code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code>. This argument is required if <code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> is not set.</p></li>
<li><p><strong>client_scope_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the client scope this role mapper should be added to. Conflicts with <code class="docutils literal notranslate"><span class="pre">client_id</span></code>. This argument is required if <code class="docutils literal notranslate"><span class="pre">client_id</span></code> is not set.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this role mapper exists within.</p></li>
<li><p><strong>role_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the role to be added to this role mapper.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientRoleMapper.client_id">
<em class="property">property </em><code class="sig-name descname">client_id</code><a class="headerlink" href="#pulumi_keycloak.GenericClientRoleMapper.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the client this role mapper should be added to. Conflicts with <code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code>. This argument is required if <code class="docutils literal notranslate"><span class="pre">client_scope_id</span></code> is not set.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientRoleMapper.client_scope_id">
<em class="property">property </em><code class="sig-name descname">client_scope_id</code><a class="headerlink" href="#pulumi_keycloak.GenericClientRoleMapper.client_scope_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the client scope this role mapper should be added to. Conflicts with <code class="docutils literal notranslate"><span class="pre">client_id</span></code>. This argument is required if <code class="docutils literal notranslate"><span class="pre">client_id</span></code> is not set.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientRoleMapper.realm_id">
<em class="property">property </em><code class="sig-name descname">realm_id</code><a class="headerlink" href="#pulumi_keycloak.GenericClientRoleMapper.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm this role mapper exists within.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GenericClientRoleMapper.role_id">
<em class="property">property </em><code class="sig-name descname">role_id</code><a class="headerlink" href="#pulumi_keycloak.GenericClientRoleMapper.role_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the role to be added to this role mapper.</p>
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
<dt id="pulumi_keycloak.GetAuthenticationExecutionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">GetAuthenticationExecutionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_flow_alias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GetAuthenticationExecutionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAuthenticationExecution.</p>
<dl class="py method">
<dt id="pulumi_keycloak.GetAuthenticationExecutionResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_keycloak.GetAuthenticationExecutionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_keycloak.GetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">GetGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GetGroupResult" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_keycloak.GetRealmKeysResult.keys">
<em class="property">property </em><code class="sig-name descname">keys</code><a class="headerlink" href="#pulumi_keycloak.GetRealmKeysResult.keys" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) A list of keys that match the filter criteria. Each key has the following attributes:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GetRealmKeysResult.statuses">
<em class="property">property </em><code class="sig-name descname">statuses</code><a class="headerlink" href="#pulumi_keycloak.GetRealmKeysResult.statuses" title="Permalink to this definition">¶</a></dt>
<dd><p>Key status (string)</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_keycloak.GetRealmResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">GetRealmResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_code_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan_login</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan_user_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_token_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_token_lifespan_for_implicit_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_theme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_token_generated_by_admin_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_token_generated_by_user_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_theme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">browser_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_authentication_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_signature_algorithm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">direct_grant_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name_html</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_authentication_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">duplicate_emails_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edit_username_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_theme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internal_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internationalizations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_theme</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_with_email_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_idle_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_max_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_max_lifespan_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_token_max_reuse</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_email_as_username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remember_me</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_credentials_flow</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_password_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">revoke_refresh_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_defenses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">smtp_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_required</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_idle_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_idle_timeout_remember_me</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_max_lifespan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_max_lifespan_remember_me</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_managed_access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verify_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_authn_passwordless_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_authn_policy</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GetRealmResult" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.GetRoleResult.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_keycloak.GetRoleResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The description of the role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GetRoleResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_keycloak.GetRoleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_keycloak.GetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">GetUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_verified</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">federated_identities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">first_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GetUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUser.</p>
<dl class="py method">
<dt id="pulumi_keycloak.GetUserResult.attributes">
<em class="property">property </em><code class="sig-name descname">attributes</code><a class="headerlink" href="#pulumi_keycloak.GetUserResult.attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) A map representing attributes for the user</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GetUserResult.email">
<em class="property">property </em><code class="sig-name descname">email</code><a class="headerlink" href="#pulumi_keycloak.GetUserResult.email" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The user’s email.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GetUserResult.email_verified">
<em class="property">property </em><code class="sig-name descname">email_verified</code><a class="headerlink" href="#pulumi_keycloak.GetUserResult.email_verified" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) Whether the email address was validated or not. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GetUserResult.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_keycloak.GetUserResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) When false, this user cannot log in. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GetUserResult.federated_identities">
<em class="property">property </em><code class="sig-name descname">federated_identities</code><a class="headerlink" href="#pulumi_keycloak.GetUserResult.federated_identities" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The user’s federated identities, if applicable. This block has the following schema:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GetUserResult.first_name">
<em class="property">property </em><code class="sig-name descname">first_name</code><a class="headerlink" href="#pulumi_keycloak.GetUserResult.first_name" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The user’s first name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GetUserResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_keycloak.GetUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GetUserResult.last_name">
<em class="property">property </em><code class="sig-name descname">last_name</code><a class="headerlink" href="#pulumi_keycloak.GetUserResult.last_name" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The user’s last name.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_keycloak.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing Groups within Keycloak.</p>
<p>Groups provide a logical wrapping for users within Keycloak. Users within a group can share attributes and roles, and
group membership can be mapped to a claim.</p>
<p>Attributes can also be defined on Groups.</p>
<p>Groups can also be federated from external data sources, such as LDAP or Active Directory. This resource <strong>should not</strong>
be used to manage groups that were created this way.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">parent_group</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;parentGroup&quot;</span><span class="p">,</span> <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">child_group</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;childGroup&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">parent_id</span><span class="o">=</span><span class="n">parent_group</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">child_group_with_optional_attributes</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;childGroupWithOptionalAttributes&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">parent_id</span><span class="o">=</span><span class="n">parent_group</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">attributes</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;key1&quot;</span><span class="p">:</span> <span class="s2">&quot;value1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;key2&quot;</span><span class="p">:</span> <span class="s2">&quot;value2&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<p>Groups can be imported using the format <code class="docutils literal notranslate"><span class="pre">{{realm_id}}/{{group_id}}</span></code>, where <code class="docutils literal notranslate"><span class="pre">group_id</span></code> is the unique ID that Keycloak assigns to the group upon creation. This value can be found in the URI when editing this group in the GUI, and is typically a GUID. Examplebash</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import keycloak:index/group:Group child_group my-realm/934a4a4e-28bd-4703-a0fa-332df153aabd
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map of key/value pairs to set as custom attributes for the group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the group.</p></li>
<li><p><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of this group’s parent. If omitted, this group will be defined at the root level.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this group exists in.</p></li>
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
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map of key/value pairs to set as custom attributes for the group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the group.</p></li>
<li><p><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of this group’s parent. If omitted, this group will be defined at the root level.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The complete path of the group. For example, the child group’s path in the example configuration would be <code class="docutils literal notranslate"><span class="pre">/parent-group/child-group</span></code>.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this group exists in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Group.attributes">
<em class="property">property </em><code class="sig-name descname">attributes</code><a class="headerlink" href="#pulumi_keycloak.Group.attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of key/value pairs to set as custom attributes for the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Group.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_keycloak.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Group.parent_id">
<em class="property">property </em><code class="sig-name descname">parent_id</code><a class="headerlink" href="#pulumi_keycloak.Group.parent_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of this group’s parent. If omitted, this group will be defined at the root level.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Group.path">
<em class="property">property </em><code class="sig-name descname">path</code><a class="headerlink" href="#pulumi_keycloak.Group.path" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The complete path of the group. For example, the child group’s path in the example configuration would be <code class="docutils literal notranslate"><span class="pre">/parent-group/child-group</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Group.realm_id">
<em class="property">property </em><code class="sig-name descname">realm_id</code><a class="headerlink" href="#pulumi_keycloak.Group.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm this group exists in.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">GroupMemberships</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GroupMemberships" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource does not support import. Instead of importing, feel free to create this resource as if it did not already exist on the server.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the group this resource should manage memberships for.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of usernames that belong to this group.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this group exists in.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.GroupMemberships.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.group_memberships.GroupMemberships<a class="headerlink" href="#pulumi_keycloak.GroupMemberships.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupMemberships resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the group this resource should manage memberships for.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of usernames that belong to this group.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this group exists in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GroupMemberships.group_id">
<em class="property">property </em><code class="sig-name descname">group_id</code><a class="headerlink" href="#pulumi_keycloak.GroupMemberships.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the group this resource should manage memberships for.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GroupMemberships.members">
<em class="property">property </em><code class="sig-name descname">members</code><a class="headerlink" href="#pulumi_keycloak.GroupMemberships.members" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of usernames that belong to this group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GroupMemberships.realm_id">
<em class="property">property </em><code class="sig-name descname">realm_id</code><a class="headerlink" href="#pulumi_keycloak.GroupMemberships.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm this group exists in.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">GroupRoles</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.GroupRoles" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource can be imported using the format <code class="docutils literal notranslate"><span class="pre">{{realm_id}}/{{group_id}}</span></code>, where <code class="docutils literal notranslate"><span class="pre">group_id</span></code> is the unique ID that Keycloak assigns to the group upon creation. This value can be found in the URI when editing this group in the GUI, and is typically a GUID. Examplebash</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import keycloak:index/groupRoles:GroupRoles group_roles my-realm/18cc6b87-2ce7-4e59-bdc8-b9d49ec98a94
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the group this resource should manage roles for.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this group exists in.</p></li>
<li><p><strong>role_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of role IDs to map to the group</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.GroupRoles.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.group_roles.GroupRoles<a class="headerlink" href="#pulumi_keycloak.GroupRoles.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupRoles resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the group this resource should manage roles for.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this group exists in.</p></li>
<li><p><strong>role_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of role IDs to map to the group</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GroupRoles.group_id">
<em class="property">property </em><code class="sig-name descname">group_id</code><a class="headerlink" href="#pulumi_keycloak.GroupRoles.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the group this resource should manage roles for.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GroupRoles.realm_id">
<em class="property">property </em><code class="sig-name descname">realm_id</code><a class="headerlink" href="#pulumi_keycloak.GroupRoles.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm this group exists in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.GroupRoles.role_ids">
<em class="property">property </em><code class="sig-name descname">role_ids</code><a class="headerlink" href="#pulumi_keycloak.GroupRoles.role_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of role IDs to map to the group</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">IdentityProviderTokenExchangeScopePermission</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clients</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_alias</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource can be imported using the format <code class="docutils literal notranslate"><span class="pre">{{realm_id}}/{{provider_alias}}</span></code>, where <code class="docutils literal notranslate"><span class="pre">provider_alias</span></code> is the alias that you assign to the identity provider upon creation. Examplebash</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import keycloak:index/identityProviderTokenExchangeScopePermission:IdentityProviderTokenExchangeScopePermission oidc_idp_permission my-realm/myIdp
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>clients</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of IDs of the clients for which a policy will be created and set on scope based token exchange permission.</p></li>
<li><p><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defaults to “client” This is also the only value policy type supported by this provider.</p></li>
<li><p><strong>provider_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias of the identity provider.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm that the identity provider exists in.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_idp_resource_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_resource_server_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_token_exchange_scope_permission_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clients</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_alias</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.identity_provider_token_exchange_scope_permission.IdentityProviderTokenExchangeScopePermission<a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IdentityProviderTokenExchangeScopePermission resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorization_idp_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) Resource ID representing the identity provider, this automatically created by keycloak.</p></li>
<li><p><strong>authorization_resource_server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) Resource server ID representing the realm management client on which this permission is managed.</p></li>
<li><p><strong>authorization_token_exchange_scope_permission_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) Permission ID representing the Permission with scope ‘Token Exchange’ and the resource ‘authorization_idp_resource_id’, this automatically created by keycloak, the policy ID will be set on this permission.</p></li>
<li><p><strong>clients</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of IDs of the clients for which a policy will be created and set on scope based token exchange permission.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) Policy ID that will be set on the scope based token exchange permission automatically created by enabling permissions on the reference identity provider.</p></li>
<li><p><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defaults to “client” This is also the only value policy type supported by this provider.</p></li>
<li><p><strong>provider_alias</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alias of the identity provider.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm that the identity provider exists in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.authorization_idp_resource_id">
<em class="property">property </em><code class="sig-name descname">authorization_idp_resource_id</code><a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.authorization_idp_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) Resource ID representing the identity provider, this automatically created by keycloak.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.authorization_resource_server_id">
<em class="property">property </em><code class="sig-name descname">authorization_resource_server_id</code><a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.authorization_resource_server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) Resource server ID representing the realm management client on which this permission is managed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.authorization_token_exchange_scope_permission_id">
<em class="property">property </em><code class="sig-name descname">authorization_token_exchange_scope_permission_id</code><a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.authorization_token_exchange_scope_permission_id" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) Permission ID representing the Permission with scope ‘Token Exchange’ and the resource ‘authorization_idp_resource_id’, this automatically created by keycloak, the policy ID will be set on this permission.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.clients">
<em class="property">property </em><code class="sig-name descname">clients</code><a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.clients" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IDs of the clients for which a policy will be created and set on scope based token exchange permission.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.policy_id">
<em class="property">property </em><code class="sig-name descname">policy_id</code><a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) Policy ID that will be set on the scope based token exchange permission automatically created by enabling permissions on the reference identity provider.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.policy_type">
<em class="property">property </em><code class="sig-name descname">policy_type</code><a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.policy_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Defaults to “client” This is also the only value policy type supported by this provider.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.provider_alias">
<em class="property">property </em><code class="sig-name descname">provider_alias</code><a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.provider_alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Alias of the identity provider.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.realm_id">
<em class="property">property </em><code class="sig-name descname">realm_id</code><a class="headerlink" href="#pulumi_keycloak.IdentityProviderTokenExchangeScopePermission.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm that the identity provider exists in.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">base_path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_timeout</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_login</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_ca_certificate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_insecure_skip_verify</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the keycloak package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Timeout (in seconds) of the Keycloak client</p></li>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">Realm</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan_login</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan_user_action</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_token_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_token_lifespan_for_implicit_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_theme</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_token_generated_by_admin_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_token_generated_by_user_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_theme</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">browser_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_authentication_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_signature_algorithm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">direct_grant_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name_html</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_authentication_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">duplicate_emails_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edit_username_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_theme</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internationalization</span><span class="p">:</span> <span class="n">Union[RealmInternationalizationArgs, Mapping[str, Any], Awaitable[Union[RealmInternationalizationArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_theme</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_with_email_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_idle_timeout</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_max_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_max_lifespan_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_token_max_reuse</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_email_as_username</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remember_me</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_credentials_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_password_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">revoke_refresh_token</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_defenses</span><span class="p">:</span> <span class="n">Union[RealmSecurityDefensesArgs, Mapping[str, Any], Awaitable[Union[RealmSecurityDefensesArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">smtp_server</span><span class="p">:</span> <span class="n">Union[RealmSmtpServerArgs, Mapping[str, Any], Awaitable[Union[RealmSmtpServerArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_required</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_idle_timeout</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_idle_timeout_remember_me</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_max_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_max_lifespan_remember_me</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_managed_access</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verify_email</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_authn_passwordless_policy</span><span class="p">:</span> <span class="n">Union[RealmWebAuthnPasswordlessPolicyArgs, Mapping[str, Any], Awaitable[Union[RealmWebAuthnPasswordlessPolicyArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_authn_policy</span><span class="p">:</span> <span class="n">Union[RealmWebAuthnPolicyArgs, Mapping[str, Any], Awaitable[Union[RealmWebAuthnPolicyArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.Realm" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing Realms within Keycloak.</p>
<p>A realm manages a logical collection of users, credentials, roles, and groups. Users log in to realms and can be federated
from multiple sources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">access_code_lifespan</span><span class="o">=</span><span class="s2">&quot;1h&quot;</span><span class="p">,</span>
    <span class="n">attributes</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;mycustomAttribute&quot;</span><span class="p">:</span> <span class="s2">&quot;myCustomValue&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;my realm&quot;</span><span class="p">,</span>
    <span class="n">display_name_html</span><span class="o">=</span><span class="s2">&quot;&lt;b&gt;my realm&lt;/b&gt;&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">internationalization</span><span class="o">=</span><span class="n">keycloak</span><span class="o">.</span><span class="n">RealmInternationalizationArgs</span><span class="p">(</span>
        <span class="n">default_locale</span><span class="o">=</span><span class="s2">&quot;en&quot;</span><span class="p">,</span>
        <span class="n">supported_locales</span><span class="o">=</span><span class="p">[</span>
            <span class="s2">&quot;en&quot;</span><span class="p">,</span>
            <span class="s2">&quot;de&quot;</span><span class="p">,</span>
            <span class="s2">&quot;es&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">),</span>
    <span class="n">login_theme</span><span class="o">=</span><span class="s2">&quot;base&quot;</span><span class="p">,</span>
    <span class="n">password_policy</span><span class="o">=</span><span class="s2">&quot;upperCase(1) and length(8) and forceExpiredPasswordChange(365) and notUsername&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">,</span>
    <span class="n">security_defenses</span><span class="o">=</span><span class="n">keycloak</span><span class="o">.</span><span class="n">RealmSecurityDefensesArgs</span><span class="p">(</span>
        <span class="n">brute_force_detection</span><span class="o">=</span><span class="n">keycloak</span><span class="o">.</span><span class="n">RealmSecurityDefensesBruteForceDetectionArgs</span><span class="p">(</span>
            <span class="n">failure_reset_time_seconds</span><span class="o">=</span><span class="mi">43200</span><span class="p">,</span>
            <span class="n">max_failure_wait_seconds</span><span class="o">=</span><span class="mi">900</span><span class="p">,</span>
            <span class="n">max_login_failures</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span>
            <span class="n">minimum_quick_login_wait_seconds</span><span class="o">=</span><span class="mi">60</span><span class="p">,</span>
            <span class="n">permanent_lockout</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="n">quick_login_check_milli_seconds</span><span class="o">=</span><span class="mi">1000</span><span class="p">,</span>
            <span class="n">wait_increment_seconds</span><span class="o">=</span><span class="mi">60</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">headers</span><span class="o">=</span><span class="n">keycloak</span><span class="o">.</span><span class="n">RealmSecurityDefensesHeadersArgs</span><span class="p">(</span>
            <span class="n">content_security_policy</span><span class="o">=</span><span class="s2">&quot;frame-src &#39;self&#39;; frame-ancestors &#39;self&#39;; object-src &#39;none&#39;;&quot;</span><span class="p">,</span>
            <span class="n">content_security_policy_report_only</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
            <span class="n">strict_transport_security</span><span class="o">=</span><span class="s2">&quot;max-age=31536000; includeSubDomains&quot;</span><span class="p">,</span>
            <span class="n">x_content_type_options</span><span class="o">=</span><span class="s2">&quot;nosniff&quot;</span><span class="p">,</span>
            <span class="n">x_frame_options</span><span class="o">=</span><span class="s2">&quot;DENY&quot;</span><span class="p">,</span>
            <span class="n">x_robots_tag</span><span class="o">=</span><span class="s2">&quot;none&quot;</span><span class="p">,</span>
            <span class="n">x_xss_protection</span><span class="o">=</span><span class="s2">&quot;1; mode=block&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">),</span>
    <span class="n">smtp_server</span><span class="o">=</span><span class="n">keycloak</span><span class="o">.</span><span class="n">RealmSmtpServerArgs</span><span class="p">(</span>
        <span class="n">auth</span><span class="o">=</span><span class="n">keycloak</span><span class="o">.</span><span class="n">RealmSmtpServerAuthArgs</span><span class="p">(</span>
            <span class="n">password</span><span class="o">=</span><span class="s2">&quot;password&quot;</span><span class="p">,</span>
            <span class="n">username</span><span class="o">=</span><span class="s2">&quot;tom&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">from_</span><span class="o">=</span><span class="s2">&quot;example@example.com&quot;</span><span class="p">,</span>
        <span class="n">host</span><span class="o">=</span><span class="s2">&quot;smtp.example.com&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">ssl_required</span><span class="o">=</span><span class="s2">&quot;external&quot;</span><span class="p">,</span>
    <span class="n">web_authn_policy</span><span class="o">=</span><span class="n">keycloak</span><span class="o">.</span><span class="n">RealmWebAuthnPolicyArgs</span><span class="p">(</span>
        <span class="n">relying_party_entity_name</span><span class="o">=</span><span class="s2">&quot;Example&quot;</span><span class="p">,</span>
        <span class="n">relying_party_id</span><span class="o">=</span><span class="s2">&quot;keycloak.example.com&quot;</span><span class="p">,</span>
        <span class="n">signature_algorithms</span><span class="o">=</span><span class="p">[</span>
            <span class="s2">&quot;ES256&quot;</span><span class="p">,</span>
            <span class="s2">&quot;RS256&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">))</span>
</pre></div>
</div>
<p>Realms can be imported using their name. Examplebash</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import keycloak:index/realm:Realm realm my-realm
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_code_lifespan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum amount of time a client has to finish the authorization code flow.</p></li>
<li><p><strong>access_code_lifespan_login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum amount of time a user is permitted to stay on the login page before the authentication process must be restarted.</p></li>
<li><p><strong>access_code_lifespan_user_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum amount of time a user has to complete login related actions, such as updating a password.</p></li>
<li><p><strong>access_token_lifespan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The amount of time an access token can be used before it expires.</p></li>
<li><p><strong>access_token_lifespan_for_implicit_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The amount of time an access token issued with the OpenID Connect Implicit Flow can be used before it expires.</p></li>
<li><p><strong>account_theme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used for account management pages.</p></li>
<li><p><strong>action_token_generated_by_admin_lifespan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum time a user has to use an admin-generated permit before it expires.</p></li>
<li><p><strong>action_token_generated_by_user_lifespan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum time a user has to use a user-generated permit before it expires.</p></li>
<li><p><strong>admin_theme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used for the admin console.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map of custom attributes to add to the realm.</p></li>
<li><p><strong>browser_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired flow for browser authentication. Defaults to <code class="docutils literal notranslate"><span class="pre">browser</span></code>.</p></li>
<li><p><strong>client_authentication_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired flow for client authentication. Defaults to <code class="docutils literal notranslate"><span class="pre">clients</span></code>.</p></li>
<li><p><strong>default_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default algorithm used to sign tokens for the realm.</p></li>
<li><p><strong>direct_grant_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired flow for direct access authentication. Defaults to <code class="docutils literal notranslate"><span class="pre">direct</span> <span class="pre">grant</span></code>.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the realm that is shown when logging in to the admin console.</p></li>
<li><p><strong>display_name_html</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the realm that is rendered as HTML on the screen when logging in to the admin console.</p></li>
<li><p><strong>docker_authentication_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired flow for Docker authentication. Defaults to <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">auth</span></code>.</p></li>
<li><p><strong>duplicate_emails_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, multiple users will be allowed to have the same email address. This argument must be set to <code class="docutils literal notranslate"><span class="pre">false</span></code> if <code class="docutils literal notranslate"><span class="pre">login_with_email_allowed</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>edit_username_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, the username field is editable.</p></li>
<li><p><strong>email_theme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used for emails that are sent by Keycloak.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">false</span></code>, users and clients will not be able to access this realm. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>login_theme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used for the login, forgot password, and registration pages.</p></li>
<li><p><strong>login_with_email_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, users may log in with their email address.</p></li>
<li><p><strong>offline_session_idle_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The amount of time an offline session can be idle before it expires.</p></li>
<li><p><strong>offline_session_max_lifespan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum amount of time before an offline session expires regardless of activity.</p></li>
<li><p><strong>offline_session_max_lifespan_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable <code class="docutils literal notranslate"><span class="pre">offline_session_max_lifespan</span></code>.</p></li>
<li><p><strong>password_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password policy for users within the realm.</p></li>
<li><p><strong>realm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the realm. This is unique across Keycloak. This will also be used as the realm’s internal ID within Keycloak.</p></li>
<li><p><strong>refresh_token_max_reuse</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum number of times a refresh token can be reused before they are revoked. If unspecified and ‘revoke_refresh_token’ is enabled the default value is 0 and refresh tokens can not be reused.</p></li>
<li><p><strong>registration_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, user registration will be enabled, and a link for registration will be displayed on the login page.</p></li>
<li><p><strong>registration_email_as_username</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, the user’s email will be used as their username during registration.</p></li>
<li><p><strong>registration_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired flow for user registration. Defaults to <code class="docutils literal notranslate"><span class="pre">registration</span></code>.</p></li>
<li><p><strong>remember_me</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, a “remember me” checkbox will be displayed on the login page, and the user’s session will not expire between browser restarts.</p></li>
<li><p><strong>reset_credentials_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired flow to use when a user attempts to reset their credentials. Defaults to <code class="docutils literal notranslate"><span class="pre">reset</span> <span class="pre">credentials</span></code>.</p></li>
<li><p><strong>reset_password_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, a “forgot password” link will be displayed on the login page.</p></li>
<li><p><strong>revoke_refresh_token</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled a refresh token can only be used number of times specified in ‘refresh_token_max_reuse’ before they are revoked. If unspecified, refresh tokens can be reused.</p></li>
<li><p><strong>ssl_required</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Can be one of following values: ‘none, ‘external’ or ‘all’</p></li>
<li><p><strong>sso_session_idle_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The amount of time a session can be idle before it expires.</p></li>
<li><p><strong>sso_session_max_lifespan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum amount of time before a session expires regardless of activity.</p></li>
<li><p><strong>user_managed_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code>, users are allowed to manage their own resources. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>verify_email</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, users are required to verify their email address after registration and after email address changes.</p></li>
<li><p><strong>web_authn_passwordless_policy</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RealmWebAuthnPasswordlessPolicyArgs'</em><em>]</em><em>]</em>) – Configuration for WebAuthn Passwordless Policy authentication.</p></li>
<li><p><strong>web_authn_policy</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RealmWebAuthnPolicyArgs'</em><em>]</em><em>]</em>) – Configuration for WebAuthn Policy authentication.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.Realm.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan_login</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_code_lifespan_user_action</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_token_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_token_lifespan_for_implicit_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_theme</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_token_generated_by_admin_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">action_token_generated_by_user_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_theme</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">browser_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_authentication_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_signature_algorithm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">direct_grant_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name_html</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_authentication_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">duplicate_emails_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edit_username_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_theme</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internal_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internationalization</span><span class="p">:</span> <span class="n">Union[RealmInternationalizationArgs, Mapping[str, Any], Awaitable[Union[RealmInternationalizationArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_theme</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_with_email_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_idle_timeout</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_max_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">offline_session_max_lifespan_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_token_max_reuse</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_email_as_username</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registration_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remember_me</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_credentials_flow</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_password_allowed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">revoke_refresh_token</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_defenses</span><span class="p">:</span> <span class="n">Union[RealmSecurityDefensesArgs, Mapping[str, Any], Awaitable[Union[RealmSecurityDefensesArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">smtp_server</span><span class="p">:</span> <span class="n">Union[RealmSmtpServerArgs, Mapping[str, Any], Awaitable[Union[RealmSmtpServerArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_required</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_idle_timeout</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_idle_timeout_remember_me</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_max_lifespan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sso_session_max_lifespan_remember_me</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_managed_access</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verify_email</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_authn_passwordless_policy</span><span class="p">:</span> <span class="n">Union[RealmWebAuthnPasswordlessPolicyArgs, Mapping[str, Any], Awaitable[Union[RealmWebAuthnPasswordlessPolicyArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_authn_policy</span><span class="p">:</span> <span class="n">Union[RealmWebAuthnPolicyArgs, Mapping[str, Any], Awaitable[Union[RealmWebAuthnPolicyArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.realm.Realm<a class="headerlink" href="#pulumi_keycloak.Realm.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Realm resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_code_lifespan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum amount of time a client has to finish the authorization code flow.</p></li>
<li><p><strong>access_code_lifespan_login</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum amount of time a user is permitted to stay on the login page before the authentication process must be restarted.</p></li>
<li><p><strong>access_code_lifespan_user_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum amount of time a user has to complete login related actions, such as updating a password.</p></li>
<li><p><strong>access_token_lifespan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The amount of time an access token can be used before it expires.</p></li>
<li><p><strong>access_token_lifespan_for_implicit_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The amount of time an access token issued with the OpenID Connect Implicit Flow can be used before it expires.</p></li>
<li><p><strong>account_theme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used for account management pages.</p></li>
<li><p><strong>action_token_generated_by_admin_lifespan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum time a user has to use an admin-generated permit before it expires.</p></li>
<li><p><strong>action_token_generated_by_user_lifespan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum time a user has to use a user-generated permit before it expires.</p></li>
<li><p><strong>admin_theme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used for the admin console.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map of custom attributes to add to the realm.</p></li>
<li><p><strong>browser_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired flow for browser authentication. Defaults to <code class="docutils literal notranslate"><span class="pre">browser</span></code>.</p></li>
<li><p><strong>client_authentication_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired flow for client authentication. Defaults to <code class="docutils literal notranslate"><span class="pre">clients</span></code>.</p></li>
<li><p><strong>default_signature_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default algorithm used to sign tokens for the realm.</p></li>
<li><p><strong>direct_grant_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired flow for direct access authentication. Defaults to <code class="docutils literal notranslate"><span class="pre">direct</span> <span class="pre">grant</span></code>.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the realm that is shown when logging in to the admin console.</p></li>
<li><p><strong>display_name_html</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the realm that is rendered as HTML on the screen when logging in to the admin console.</p></li>
<li><p><strong>docker_authentication_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired flow for Docker authentication. Defaults to <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">auth</span></code>.</p></li>
<li><p><strong>duplicate_emails_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, multiple users will be allowed to have the same email address. This argument must be set to <code class="docutils literal notranslate"><span class="pre">false</span></code> if <code class="docutils literal notranslate"><span class="pre">login_with_email_allowed</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>edit_username_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, the username field is editable.</p></li>
<li><p><strong>email_theme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used for emails that are sent by Keycloak.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">false</span></code>, users and clients will not be able to access this realm. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>login_theme</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used for the login, forgot password, and registration pages.</p></li>
<li><p><strong>login_with_email_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, users may log in with their email address.</p></li>
<li><p><strong>offline_session_idle_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The amount of time an offline session can be idle before it expires.</p></li>
<li><p><strong>offline_session_max_lifespan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum amount of time before an offline session expires regardless of activity.</p></li>
<li><p><strong>offline_session_max_lifespan_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable <code class="docutils literal notranslate"><span class="pre">offline_session_max_lifespan</span></code>.</p></li>
<li><p><strong>password_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password policy for users within the realm.</p></li>
<li><p><strong>realm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the realm. This is unique across Keycloak. This will also be used as the realm’s internal ID within Keycloak.</p></li>
<li><p><strong>refresh_token_max_reuse</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum number of times a refresh token can be reused before they are revoked. If unspecified and ‘revoke_refresh_token’ is enabled the default value is 0 and refresh tokens can not be reused.</p></li>
<li><p><strong>registration_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, user registration will be enabled, and a link for registration will be displayed on the login page.</p></li>
<li><p><strong>registration_email_as_username</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, the user’s email will be used as their username during registration.</p></li>
<li><p><strong>registration_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired flow for user registration. Defaults to <code class="docutils literal notranslate"><span class="pre">registration</span></code>.</p></li>
<li><p><strong>remember_me</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, a “remember me” checkbox will be displayed on the login page, and the user’s session will not expire between browser restarts.</p></li>
<li><p><strong>reset_credentials_flow</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The desired flow to use when a user attempts to reset their credentials. Defaults to <code class="docutils literal notranslate"><span class="pre">reset</span> <span class="pre">credentials</span></code>.</p></li>
<li><p><strong>reset_password_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, a “forgot password” link will be displayed on the login page.</p></li>
<li><p><strong>revoke_refresh_token</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If enabled a refresh token can only be used number of times specified in ‘refresh_token_max_reuse’ before they are revoked. If unspecified, refresh tokens can be reused.</p></li>
<li><p><strong>ssl_required</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Can be one of following values: ‘none, ‘external’ or ‘all’</p></li>
<li><p><strong>sso_session_idle_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The amount of time a session can be idle before it expires.</p></li>
<li><p><strong>sso_session_max_lifespan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum amount of time before a session expires regardless of activity.</p></li>
<li><p><strong>user_managed_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code>, users are allowed to manage their own resources. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>verify_email</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true, users are required to verify their email address after registration and after email address changes.</p></li>
<li><p><strong>web_authn_passwordless_policy</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RealmWebAuthnPasswordlessPolicyArgs'</em><em>]</em><em>]</em>) – Configuration for WebAuthn Passwordless Policy authentication.</p></li>
<li><p><strong>web_authn_policy</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RealmWebAuthnPolicyArgs'</em><em>]</em><em>]</em>) – Configuration for WebAuthn Policy authentication.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.access_code_lifespan">
<em class="property">property </em><code class="sig-name descname">access_code_lifespan</code><a class="headerlink" href="#pulumi_keycloak.Realm.access_code_lifespan" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum amount of time a client has to finish the authorization code flow.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.access_code_lifespan_login">
<em class="property">property </em><code class="sig-name descname">access_code_lifespan_login</code><a class="headerlink" href="#pulumi_keycloak.Realm.access_code_lifespan_login" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum amount of time a user is permitted to stay on the login page before the authentication process must be restarted.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.access_code_lifespan_user_action">
<em class="property">property </em><code class="sig-name descname">access_code_lifespan_user_action</code><a class="headerlink" href="#pulumi_keycloak.Realm.access_code_lifespan_user_action" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum amount of time a user has to complete login related actions, such as updating a password.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.access_token_lifespan">
<em class="property">property </em><code class="sig-name descname">access_token_lifespan</code><a class="headerlink" href="#pulumi_keycloak.Realm.access_token_lifespan" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time an access token can be used before it expires.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.access_token_lifespan_for_implicit_flow">
<em class="property">property </em><code class="sig-name descname">access_token_lifespan_for_implicit_flow</code><a class="headerlink" href="#pulumi_keycloak.Realm.access_token_lifespan_for_implicit_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time an access token issued with the OpenID Connect Implicit Flow can be used before it expires.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.account_theme">
<em class="property">property </em><code class="sig-name descname">account_theme</code><a class="headerlink" href="#pulumi_keycloak.Realm.account_theme" title="Permalink to this definition">¶</a></dt>
<dd><p>Used for account management pages.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.action_token_generated_by_admin_lifespan">
<em class="property">property </em><code class="sig-name descname">action_token_generated_by_admin_lifespan</code><a class="headerlink" href="#pulumi_keycloak.Realm.action_token_generated_by_admin_lifespan" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum time a user has to use an admin-generated permit before it expires.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.action_token_generated_by_user_lifespan">
<em class="property">property </em><code class="sig-name descname">action_token_generated_by_user_lifespan</code><a class="headerlink" href="#pulumi_keycloak.Realm.action_token_generated_by_user_lifespan" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum time a user has to use a user-generated permit before it expires.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.admin_theme">
<em class="property">property </em><code class="sig-name descname">admin_theme</code><a class="headerlink" href="#pulumi_keycloak.Realm.admin_theme" title="Permalink to this definition">¶</a></dt>
<dd><p>Used for the admin console.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.attributes">
<em class="property">property </em><code class="sig-name descname">attributes</code><a class="headerlink" href="#pulumi_keycloak.Realm.attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of custom attributes to add to the realm.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.browser_flow">
<em class="property">property </em><code class="sig-name descname">browser_flow</code><a class="headerlink" href="#pulumi_keycloak.Realm.browser_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired flow for browser authentication. Defaults to <code class="docutils literal notranslate"><span class="pre">browser</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.client_authentication_flow">
<em class="property">property </em><code class="sig-name descname">client_authentication_flow</code><a class="headerlink" href="#pulumi_keycloak.Realm.client_authentication_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired flow for client authentication. Defaults to <code class="docutils literal notranslate"><span class="pre">clients</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.default_signature_algorithm">
<em class="property">property </em><code class="sig-name descname">default_signature_algorithm</code><a class="headerlink" href="#pulumi_keycloak.Realm.default_signature_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Default algorithm used to sign tokens for the realm.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.direct_grant_flow">
<em class="property">property </em><code class="sig-name descname">direct_grant_flow</code><a class="headerlink" href="#pulumi_keycloak.Realm.direct_grant_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired flow for direct access authentication. Defaults to <code class="docutils literal notranslate"><span class="pre">direct</span> <span class="pre">grant</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.display_name">
<em class="property">property </em><code class="sig-name descname">display_name</code><a class="headerlink" href="#pulumi_keycloak.Realm.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name for the realm that is shown when logging in to the admin console.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.display_name_html">
<em class="property">property </em><code class="sig-name descname">display_name_html</code><a class="headerlink" href="#pulumi_keycloak.Realm.display_name_html" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name for the realm that is rendered as HTML on the screen when logging in to the admin console.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.docker_authentication_flow">
<em class="property">property </em><code class="sig-name descname">docker_authentication_flow</code><a class="headerlink" href="#pulumi_keycloak.Realm.docker_authentication_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired flow for Docker authentication. Defaults to <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">auth</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.duplicate_emails_allowed">
<em class="property">property </em><code class="sig-name descname">duplicate_emails_allowed</code><a class="headerlink" href="#pulumi_keycloak.Realm.duplicate_emails_allowed" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, multiple users will be allowed to have the same email address. This argument must be set to <code class="docutils literal notranslate"><span class="pre">false</span></code> if <code class="docutils literal notranslate"><span class="pre">login_with_email_allowed</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.edit_username_allowed">
<em class="property">property </em><code class="sig-name descname">edit_username_allowed</code><a class="headerlink" href="#pulumi_keycloak.Realm.edit_username_allowed" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, the username field is editable.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.email_theme">
<em class="property">property </em><code class="sig-name descname">email_theme</code><a class="headerlink" href="#pulumi_keycloak.Realm.email_theme" title="Permalink to this definition">¶</a></dt>
<dd><p>Used for emails that are sent by Keycloak.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_keycloak.Realm.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">false</span></code>, users and clients will not be able to access this realm. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.login_theme">
<em class="property">property </em><code class="sig-name descname">login_theme</code><a class="headerlink" href="#pulumi_keycloak.Realm.login_theme" title="Permalink to this definition">¶</a></dt>
<dd><p>Used for the login, forgot password, and registration pages.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.login_with_email_allowed">
<em class="property">property </em><code class="sig-name descname">login_with_email_allowed</code><a class="headerlink" href="#pulumi_keycloak.Realm.login_with_email_allowed" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, users may log in with their email address.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.offline_session_idle_timeout">
<em class="property">property </em><code class="sig-name descname">offline_session_idle_timeout</code><a class="headerlink" href="#pulumi_keycloak.Realm.offline_session_idle_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time an offline session can be idle before it expires.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.offline_session_max_lifespan">
<em class="property">property </em><code class="sig-name descname">offline_session_max_lifespan</code><a class="headerlink" href="#pulumi_keycloak.Realm.offline_session_max_lifespan" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum amount of time before an offline session expires regardless of activity.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.offline_session_max_lifespan_enabled">
<em class="property">property </em><code class="sig-name descname">offline_session_max_lifespan_enabled</code><a class="headerlink" href="#pulumi_keycloak.Realm.offline_session_max_lifespan_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable <code class="docutils literal notranslate"><span class="pre">offline_session_max_lifespan</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.password_policy">
<em class="property">property </em><code class="sig-name descname">password_policy</code><a class="headerlink" href="#pulumi_keycloak.Realm.password_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The password policy for users within the realm.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.realm">
<em class="property">property </em><code class="sig-name descname">realm</code><a class="headerlink" href="#pulumi_keycloak.Realm.realm" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the realm. This is unique across Keycloak. This will also be used as the realm’s internal ID within Keycloak.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.refresh_token_max_reuse">
<em class="property">property </em><code class="sig-name descname">refresh_token_max_reuse</code><a class="headerlink" href="#pulumi_keycloak.Realm.refresh_token_max_reuse" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum number of times a refresh token can be reused before they are revoked. If unspecified and ‘revoke_refresh_token’ is enabled the default value is 0 and refresh tokens can not be reused.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.registration_allowed">
<em class="property">property </em><code class="sig-name descname">registration_allowed</code><a class="headerlink" href="#pulumi_keycloak.Realm.registration_allowed" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, user registration will be enabled, and a link for registration will be displayed on the login page.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.registration_email_as_username">
<em class="property">property </em><code class="sig-name descname">registration_email_as_username</code><a class="headerlink" href="#pulumi_keycloak.Realm.registration_email_as_username" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, the user’s email will be used as their username during registration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.registration_flow">
<em class="property">property </em><code class="sig-name descname">registration_flow</code><a class="headerlink" href="#pulumi_keycloak.Realm.registration_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired flow for user registration. Defaults to <code class="docutils literal notranslate"><span class="pre">registration</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.remember_me">
<em class="property">property </em><code class="sig-name descname">remember_me</code><a class="headerlink" href="#pulumi_keycloak.Realm.remember_me" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, a “remember me” checkbox will be displayed on the login page, and the user’s session will not expire between browser restarts.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.reset_credentials_flow">
<em class="property">property </em><code class="sig-name descname">reset_credentials_flow</code><a class="headerlink" href="#pulumi_keycloak.Realm.reset_credentials_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired flow to use when a user attempts to reset their credentials. Defaults to <code class="docutils literal notranslate"><span class="pre">reset</span> <span class="pre">credentials</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.reset_password_allowed">
<em class="property">property </em><code class="sig-name descname">reset_password_allowed</code><a class="headerlink" href="#pulumi_keycloak.Realm.reset_password_allowed" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, a “forgot password” link will be displayed on the login page.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.revoke_refresh_token">
<em class="property">property </em><code class="sig-name descname">revoke_refresh_token</code><a class="headerlink" href="#pulumi_keycloak.Realm.revoke_refresh_token" title="Permalink to this definition">¶</a></dt>
<dd><p>If enabled a refresh token can only be used number of times specified in ‘refresh_token_max_reuse’ before they are revoked. If unspecified, refresh tokens can be reused.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.ssl_required">
<em class="property">property </em><code class="sig-name descname">ssl_required</code><a class="headerlink" href="#pulumi_keycloak.Realm.ssl_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be one of following values: ‘none, ‘external’ or ‘all’</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.sso_session_idle_timeout">
<em class="property">property </em><code class="sig-name descname">sso_session_idle_timeout</code><a class="headerlink" href="#pulumi_keycloak.Realm.sso_session_idle_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time a session can be idle before it expires.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.sso_session_max_lifespan">
<em class="property">property </em><code class="sig-name descname">sso_session_max_lifespan</code><a class="headerlink" href="#pulumi_keycloak.Realm.sso_session_max_lifespan" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum amount of time before a session expires regardless of activity.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.user_managed_access">
<em class="property">property </em><code class="sig-name descname">user_managed_access</code><a class="headerlink" href="#pulumi_keycloak.Realm.user_managed_access" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">true</span></code>, users are allowed to manage their own resources. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.verify_email">
<em class="property">property </em><code class="sig-name descname">verify_email</code><a class="headerlink" href="#pulumi_keycloak.Realm.verify_email" title="Permalink to this definition">¶</a></dt>
<dd><p>When true, users are required to verify their email address after registration and after email address changes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.web_authn_passwordless_policy">
<em class="property">property </em><code class="sig-name descname">web_authn_passwordless_policy</code><a class="headerlink" href="#pulumi_keycloak.Realm.web_authn_passwordless_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for WebAuthn Passwordless Policy authentication.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Realm.web_authn_policy">
<em class="property">property </em><code class="sig-name descname">web_authn_policy</code><a class="headerlink" href="#pulumi_keycloak.Realm.web_authn_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for WebAuthn Policy authentication.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">RealmEvents</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_events_details_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_events_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled_event_types</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events_expiration</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events_listeners</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.RealmEvents" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for managing Realm Events settings within Keycloak.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">realm_events</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">RealmEvents</span><span class="p">(</span><span class="s2">&quot;realmEvents&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">events_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">events_expiration</span><span class="o">=</span><span class="mi">3600</span><span class="p">,</span>
    <span class="n">admin_events_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">admin_events_details_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">enabled_event_types</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;LOGIN&quot;</span><span class="p">,</span>
        <span class="s2">&quot;LOGOUT&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">events_listeners</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;jboss-logging&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>This resource currently does not support importing.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_events_details_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code>, saved admin events will included detailed information for create/update requests. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>admin_events_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code>, admin events are saved to the database, making them available through the admin console. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enabled_event_types</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The event types that will be saved to the database. Omitting this field enables all event types. Defaults to <code class="docutils literal notranslate"><span class="pre">[]</span></code> or all event types.</p></li>
<li><p><strong>events_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code>, events from <code class="docutils literal notranslate"><span class="pre">enabled_event_types</span></code> are saved to the database, making them available through the admin console. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>events_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The amount of time in seconds events will be saved in the database. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> or never.</p></li>
<li><p><strong>events_listeners</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The event listeners that events should be sent to. Defaults to <code class="docutils literal notranslate"><span class="pre">[]</span></code> or none. Note that new realms enable the <code class="docutils literal notranslate"><span class="pre">jboss-logging</span></code> listener by default, and this resource will remove that unless it is specified.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the realm the event settings apply to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.RealmEvents.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_events_details_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">admin_events_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled_event_types</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events_expiration</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events_listeners</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.realm_events.RealmEvents<a class="headerlink" href="#pulumi_keycloak.RealmEvents.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RealmEvents resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_events_details_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code>, saved admin events will included detailed information for create/update requests. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>admin_events_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code>, admin events are saved to the database, making them available through the admin console. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enabled_event_types</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The event types that will be saved to the database. Omitting this field enables all event types. Defaults to <code class="docutils literal notranslate"><span class="pre">[]</span></code> or all event types.</p></li>
<li><p><strong>events_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code>, events from <code class="docutils literal notranslate"><span class="pre">enabled_event_types</span></code> are saved to the database, making them available through the admin console. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>events_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The amount of time in seconds events will be saved in the database. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> or never.</p></li>
<li><p><strong>events_listeners</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The event listeners that events should be sent to. Defaults to <code class="docutils literal notranslate"><span class="pre">[]</span></code> or none. Note that new realms enable the <code class="docutils literal notranslate"><span class="pre">jboss-logging</span></code> listener by default, and this resource will remove that unless it is specified.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the realm the event settings apply to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.RealmEvents.admin_events_details_enabled">
<em class="property">property </em><code class="sig-name descname">admin_events_details_enabled</code><a class="headerlink" href="#pulumi_keycloak.RealmEvents.admin_events_details_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">true</span></code>, saved admin events will included detailed information for create/update requests. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.RealmEvents.admin_events_enabled">
<em class="property">property </em><code class="sig-name descname">admin_events_enabled</code><a class="headerlink" href="#pulumi_keycloak.RealmEvents.admin_events_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">true</span></code>, admin events are saved to the database, making them available through the admin console. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.RealmEvents.enabled_event_types">
<em class="property">property </em><code class="sig-name descname">enabled_event_types</code><a class="headerlink" href="#pulumi_keycloak.RealmEvents.enabled_event_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The event types that will be saved to the database. Omitting this field enables all event types. Defaults to <code class="docutils literal notranslate"><span class="pre">[]</span></code> or all event types.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.RealmEvents.events_enabled">
<em class="property">property </em><code class="sig-name descname">events_enabled</code><a class="headerlink" href="#pulumi_keycloak.RealmEvents.events_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">true</span></code>, events from <code class="docutils literal notranslate"><span class="pre">enabled_event_types</span></code> are saved to the database, making them available through the admin console. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.RealmEvents.events_expiration">
<em class="property">property </em><code class="sig-name descname">events_expiration</code><a class="headerlink" href="#pulumi_keycloak.RealmEvents.events_expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time in seconds events will be saved in the database. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> or never.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.RealmEvents.events_listeners">
<em class="property">property </em><code class="sig-name descname">events_listeners</code><a class="headerlink" href="#pulumi_keycloak.RealmEvents.events_listeners" title="Permalink to this definition">¶</a></dt>
<dd><p>The event listeners that events should be sent to. Defaults to <code class="docutils literal notranslate"><span class="pre">[]</span></code> or none. Note that new realms enable the <code class="docutils literal notranslate"><span class="pre">jboss-logging</span></code> listener by default, and this resource will remove that unless it is specified.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.RealmEvents.realm_id">
<em class="property">property </em><code class="sig-name descname">realm_id</code><a class="headerlink" href="#pulumi_keycloak.RealmEvents.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the realm the event settings apply to.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">RequiredAction</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alias</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_action</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.RequiredAction" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a RequiredAction resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_keycloak.RequiredAction.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alias</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_action</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.required_action.RequiredAction<a class="headerlink" href="#pulumi_keycloak.RequiredAction.get" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">Role</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">composite_roles</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.Role" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing roles within Keycloak.</p>
<p>Roles allow you define privileges within Keycloak and map them to users and groups.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">realm_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;realmRole&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;My Realm Role&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">openid_client</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">openid</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="s2">&quot;openidClient&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="s2">&quot;client&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">access_type</span><span class="o">=</span><span class="s2">&quot;CONFIDENTIAL&quot;</span><span class="p">,</span>
    <span class="n">valid_redirect_uris</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;http://localhost:8080/openid-callback&quot;</span><span class="p">])</span>
<span class="n">client_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;clientRole&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="n">keycloak_client</span><span class="p">[</span><span class="s2">&quot;openid_client&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;My Client Role&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="c1"># realm roles</span>
<span class="n">create_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;createRole&quot;</span><span class="p">,</span> <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">read_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;readRole&quot;</span><span class="p">,</span> <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">update_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;updateRole&quot;</span><span class="p">,</span> <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">delete_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;deleteRole&quot;</span><span class="p">,</span> <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="c1"># client role</span>
<span class="n">openid_client</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">openid</span><span class="o">.</span><span class="n">Client</span><span class="p">(</span><span class="s2">&quot;openidClient&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="s2">&quot;client&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">access_type</span><span class="o">=</span><span class="s2">&quot;CONFIDENTIAL&quot;</span><span class="p">,</span>
    <span class="n">valid_redirect_uris</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;http://localhost:8080/openid-callback&quot;</span><span class="p">])</span>
<span class="n">client_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;clientRole&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="n">keycloak_client</span><span class="p">[</span><span class="s2">&quot;openid_client&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;My Client Role&quot;</span><span class="p">)</span>
<span class="n">admin_role</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;adminRole&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">composite_roles</span><span class="o">=</span><span class="p">[</span>
        <span class="n">create_role</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="n">read_role</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="n">update_role</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="n">delete_role</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="n">client_role</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>Roles can be imported using the format <code class="docutils literal notranslate"><span class="pre">{{realm_id}}/{{role_id}}</span></code>, where <code class="docutils literal notranslate"><span class="pre">role_id</span></code> is the unique ID that Keycloak assigns to the role. The ID is not easy to find in the GUI, but it appears in the URL when editing the role. Examplebash</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import keycloak:index/role:Role role my-realm/7e8cf32a-8acb-4d34-89c4-04fb1d10ccad
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When specified, this role will be created as a client role attached to the client with the provided ID</p></li>
<li><p><strong>composite_roles</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – When specified, this role will be a composite role, composed of all roles that have an ID present within this list.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the role</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this role exists within.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.Role.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">composite_roles</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.role.Role<a class="headerlink" href="#pulumi_keycloak.Role.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Role resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When specified, this role will be created as a client role attached to the client with the provided ID</p></li>
<li><p><strong>composite_roles</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – When specified, this role will be a composite role, composed of all roles that have an ID present within this list.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the role</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the role</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this role exists within.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Role.client_id">
<em class="property">property </em><code class="sig-name descname">client_id</code><a class="headerlink" href="#pulumi_keycloak.Role.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>When specified, this role will be created as a client role attached to the client with the provided ID</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Role.composite_roles">
<em class="property">property </em><code class="sig-name descname">composite_roles</code><a class="headerlink" href="#pulumi_keycloak.Role.composite_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>When specified, this role will be a composite role, composed of all roles that have an ID present within this list.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Role.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_keycloak.Role.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the role</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Role.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_keycloak.Role.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the role</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.Role.realm_id">
<em class="property">property </em><code class="sig-name descname">realm_id</code><a class="headerlink" href="#pulumi_keycloak.Role.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm this role exists within.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_verified</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">federated_identities</span><span class="p">:</span> <span class="n">Union[Sequence[Union[UserFederatedIdentityArgs, Mapping[str, Any], Awaitable[Union[UserFederatedIdentityArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[UserFederatedIdentityArgs, Mapping[str, Any], Awaitable[Union[UserFederatedIdentityArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">first_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_password</span><span class="p">:</span> <span class="n">Union[UserInitialPasswordArgs, Mapping[str, Any], Awaitable[Union[UserInitialPasswordArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows for creating and managing Users within Keycloak.</p>
<p>This resource was created primarily to enable the acceptance tests for the <code class="docutils literal notranslate"><span class="pre">Group</span></code> resource. Creating users within
Keycloak is not recommended. Instead, users should be federated from external sources by configuring user federation providers
or identity providers.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">user</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;bob&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;bob@domain.com&quot;</span><span class="p">,</span>
    <span class="n">first_name</span><span class="o">=</span><span class="s2">&quot;Bob&quot;</span><span class="p">,</span>
    <span class="n">last_name</span><span class="o">=</span><span class="s2">&quot;Bobson&quot;</span><span class="p">)</span>
<span class="n">user_with_initial_password</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;userWithInitialPassword&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;alice&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;alice@domain.com&quot;</span><span class="p">,</span>
    <span class="n">first_name</span><span class="o">=</span><span class="s2">&quot;Alice&quot;</span><span class="p">,</span>
    <span class="n">last_name</span><span class="o">=</span><span class="s2">&quot;Aliceberg&quot;</span><span class="p">,</span>
    <span class="n">attributes</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;foo&quot;</span><span class="p">:</span> <span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">initial_password</span><span class="o">=</span><span class="n">keycloak</span><span class="o">.</span><span class="n">UserInitialPasswordArgs</span><span class="p">(</span>
        <span class="n">value</span><span class="o">=</span><span class="s2">&quot;some password&quot;</span><span class="p">,</span>
        <span class="n">temporary</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="p">))</span>
</pre></div>
</div>
<p>Users can be imported using the format <code class="docutils literal notranslate"><span class="pre">{{realm_id}}/{{user_id}}</span></code>, where <code class="docutils literal notranslate"><span class="pre">user_id</span></code> is the unique ID that Keycloak assigns to the user upon creation. This value can be found in the GUI when editing the user. Examplebash</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import keycloak:index/user:User user my-realm/60c3f971-b1d3-4b3a-9035-d16d7540a5e4
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map representing attributes for the user</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s email.</p></li>
<li><p><strong>email_verified</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the email address was validated or not. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When false, this user cannot log in. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>first_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s first name.</p></li>
<li><p><strong>initial_password</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'UserInitialPasswordArgs'</em><em>]</em><em>]</em>) – When given, the user’s initial password will be set. This attribute is only respected during initial user creation.</p></li>
<li><p><strong>last_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s last name.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this user belongs to.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique username of this user.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attributes</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_verified</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">federated_identities</span><span class="p">:</span> <span class="n">Union[Sequence[Union[UserFederatedIdentityArgs, Mapping[str, Any], Awaitable[Union[UserFederatedIdentityArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[UserFederatedIdentityArgs, Mapping[str, Any], Awaitable[Union[UserFederatedIdentityArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">first_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initial_password</span><span class="p">:</span> <span class="n">Union[UserInitialPasswordArgs, Mapping[str, Any], Awaitable[Union[UserInitialPasswordArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.user.User<a class="headerlink" href="#pulumi_keycloak.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map representing attributes for the user</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s email.</p></li>
<li><p><strong>email_verified</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the email address was validated or not. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When false, this user cannot log in. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>first_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s first name.</p></li>
<li><p><strong>initial_password</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'UserInitialPasswordArgs'</em><em>]</em><em>]</em>) – When given, the user’s initial password will be set. This attribute is only respected during initial user creation.</p></li>
<li><p><strong>last_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s last name.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this user belongs to.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique username of this user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.User.attributes">
<em class="property">property </em><code class="sig-name descname">attributes</code><a class="headerlink" href="#pulumi_keycloak.User.attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>A map representing attributes for the user</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.User.email">
<em class="property">property </em><code class="sig-name descname">email</code><a class="headerlink" href="#pulumi_keycloak.User.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The user’s email.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.User.email_verified">
<em class="property">property </em><code class="sig-name descname">email_verified</code><a class="headerlink" href="#pulumi_keycloak.User.email_verified" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the email address was validated or not. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.User.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_keycloak.User.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>When false, this user cannot log in. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.User.first_name">
<em class="property">property </em><code class="sig-name descname">first_name</code><a class="headerlink" href="#pulumi_keycloak.User.first_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The user’s first name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.User.initial_password">
<em class="property">property </em><code class="sig-name descname">initial_password</code><a class="headerlink" href="#pulumi_keycloak.User.initial_password" title="Permalink to this definition">¶</a></dt>
<dd><p>When given, the user’s initial password will be set. This attribute is only respected during initial user creation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.User.last_name">
<em class="property">property </em><code class="sig-name descname">last_name</code><a class="headerlink" href="#pulumi_keycloak.User.last_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The user’s last name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.User.realm_id">
<em class="property">property </em><code class="sig-name descname">realm_id</code><a class="headerlink" href="#pulumi_keycloak.User.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm this user belongs to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.User.username">
<em class="property">property </em><code class="sig-name descname">username</code><a class="headerlink" href="#pulumi_keycloak.User.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique username of this user.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">UserRoles</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.UserRoles" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource can be imported using the format <code class="docutils literal notranslate"><span class="pre">{{realm_id}}/{{user_id}}</span></code>, where <code class="docutils literal notranslate"><span class="pre">user_id</span></code> is the unique ID that Keycloak assigns to the user upon creation. This value can be found in the GUI when editing the user, and is typically a GUID. Examplebash</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import keycloak:index/userRoles:UserRoles user_roles my-realm/b0ae6924-1bd5-4655-9e38-dae7c5e42924
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this user exists in.</p></li>
<li><p><strong>role_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of role IDs to map to the user</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the user this resource should manage roles for.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_keycloak.UserRoles.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.user_roles.UserRoles<a class="headerlink" href="#pulumi_keycloak.UserRoles.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserRoles resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>realm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The realm this user exists in.</p></li>
<li><p><strong>role_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of role IDs to map to the user</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the user this resource should manage roles for.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.UserRoles.realm_id">
<em class="property">property </em><code class="sig-name descname">realm_id</code><a class="headerlink" href="#pulumi_keycloak.UserRoles.realm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The realm this user exists in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.UserRoles.role_ids">
<em class="property">property </em><code class="sig-name descname">role_ids</code><a class="headerlink" href="#pulumi_keycloak.UserRoles.role_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of role IDs to map to the user</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.UserRoles.user_id">
<em class="property">property </em><code class="sig-name descname">user_id</code><a class="headerlink" href="#pulumi_keycloak.UserRoles.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the user this resource should manage roles for.</p>
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

<dl class="py class">
<dt id="pulumi_keycloak.UsersPermissions">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">UsersPermissions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">impersonate_scope</span><span class="p">:</span> <span class="n">Union[UsersPermissionsImpersonateScopeArgs, Mapping[str, Any], Awaitable[Union[UsersPermissionsImpersonateScopeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">manage_group_membership_scope</span><span class="p">:</span> <span class="n">Union[UsersPermissionsManageGroupMembershipScopeArgs, Mapping[str, Any], Awaitable[Union[UsersPermissionsManageGroupMembershipScopeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">manage_scope</span><span class="p">:</span> <span class="n">Union[UsersPermissionsManageScopeArgs, Mapping[str, Any], Awaitable[Union[UsersPermissionsManageScopeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">map_roles_scope</span><span class="p">:</span> <span class="n">Union[UsersPermissionsMapRolesScopeArgs, Mapping[str, Any], Awaitable[Union[UsersPermissionsMapRolesScopeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_impersonated_scope</span><span class="p">:</span> <span class="n">Union[UsersPermissionsUserImpersonatedScopeArgs, Mapping[str, Any], Awaitable[Union[UsersPermissionsUserImpersonatedScopeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">view_scope</span><span class="p">:</span> <span class="n">Union[UsersPermissionsViewScopeArgs, Mapping[str, Any], Awaitable[Union[UsersPermissionsViewScopeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.UsersPermissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a UsersPermissions resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_keycloak.UsersPermissions.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_resource_server_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">impersonate_scope</span><span class="p">:</span> <span class="n">Union[UsersPermissionsImpersonateScopeArgs, Mapping[str, Any], Awaitable[Union[UsersPermissionsImpersonateScopeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">manage_group_membership_scope</span><span class="p">:</span> <span class="n">Union[UsersPermissionsManageGroupMembershipScopeArgs, Mapping[str, Any], Awaitable[Union[UsersPermissionsManageGroupMembershipScopeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">manage_scope</span><span class="p">:</span> <span class="n">Union[UsersPermissionsManageScopeArgs, Mapping[str, Any], Awaitable[Union[UsersPermissionsManageScopeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">map_roles_scope</span><span class="p">:</span> <span class="n">Union[UsersPermissionsMapRolesScopeArgs, Mapping[str, Any], Awaitable[Union[UsersPermissionsMapRolesScopeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_impersonated_scope</span><span class="p">:</span> <span class="n">Union[UsersPermissionsUserImpersonatedScopeArgs, Mapping[str, Any], Awaitable[Union[UsersPermissionsUserImpersonatedScopeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">view_scope</span><span class="p">:</span> <span class="n">Union[UsersPermissionsViewScopeArgs, Mapping[str, Any], Awaitable[Union[UsersPermissionsViewScopeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.users_permissions.UsersPermissions<a class="headerlink" href="#pulumi_keycloak.UsersPermissions.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UsersPermissions resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorization_resource_server_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource server id representing the realm management client on which this permission is managed</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.UsersPermissions.authorization_resource_server_id">
<em class="property">property </em><code class="sig-name descname">authorization_resource_server_id</code><a class="headerlink" href="#pulumi_keycloak.UsersPermissions.authorization_resource_server_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource server id representing the realm management client on which this permission is managed</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_keycloak.UsersPermissions.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.UsersPermissions.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.UsersPermissions.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_keycloak.UsersPermissions.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_keycloak.get_authentication_execution">
<code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">get_authentication_execution</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">parent_flow_alias</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.get_authentication_execution.AwaitableGetAuthenticationExecutionResult<a class="headerlink" href="#pulumi_keycloak.get_authentication_execution" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch the ID of an authentication execution within Keycloak.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">browser_auth_cookie</span> <span class="o">=</span> <span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">get_authentication_execution</span><span class="p">(</span><span class="n">realm_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">parent_flow_alias</span><span class="o">=</span><span class="s2">&quot;browser&quot;</span><span class="p">,</span>
    <span class="n">provider_id</span><span class="o">=</span><span class="s2">&quot;auth-cookie&quot;</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>parent_flow_alias</strong> (<em>str</em>) – The alias of the flow this execution is attached to.</p></li>
<li><p><strong>provider_id</strong> (<em>str</em>) – The name of the provider. This can be found by experimenting with the GUI and looking at HTTP requests within the network tab of your browser’s development tools. This was previously known as the “authenticator”.</p></li>
<li><p><strong>realm_id</strong> (<em>str</em>) – The realm the authentication execution exists in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_keycloak.get_group">
<code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">get_group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.get_group.AwaitableGetGroupResult<a class="headerlink" href="#pulumi_keycloak.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch properties of a Keycloak group for
usage with other resources, such as <code class="docutils literal notranslate"><span class="pre">GroupRoles</span></code>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">offline_access</span> <span class="o">=</span> <span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">get_role</span><span class="p">(</span><span class="n">realm_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;offline_access&quot;</span><span class="p">))</span>
<span class="n">group</span> <span class="o">=</span> <span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">realm_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;group&quot;</span><span class="p">))</span>
<span class="n">group_roles</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">GroupRoles</span><span class="p">(</span><span class="s2">&quot;groupRoles&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">group_id</span><span class="o">=</span><span class="n">group</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">role_ids</span><span class="o">=</span><span class="p">[</span><span class="n">offline_access</span><span class="o">.</span><span class="n">id</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the group. If there are multiple groups match <code class="docutils literal notranslate"><span class="pre">name</span></code>, the first result will be returned.</p></li>
<li><p><strong>realm_id</strong> (<em>str</em>) – The realm this group exists within.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_keycloak.get_realm">
<code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">get_realm</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">attributes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name_html</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internationalizations</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>GetRealmInternationalizationArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_defenses</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>GetRealmSecurityDefenseArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">smtp_servers</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>GetRealmSmtpServerArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_authn_passwordless_policy</span><span class="p">:</span> <span class="n">Union[GetRealmWebAuthnPasswordlessPolicyArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_authn_policy</span><span class="p">:</span> <span class="n">Union[GetRealmWebAuthnPolicyArgs, Mapping[str, Any], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.get_realm.AwaitableGetRealmResult<a class="headerlink" href="#pulumi_keycloak.get_realm" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch properties of a Keycloak realm for
usage with other resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">get_realm</span><span class="p">(</span><span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">)</span>
<span class="n">group</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;group&quot;</span><span class="p">,</span> <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>realm</strong> (<em>str</em>) – The realm name.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_keycloak.get_realm_keys">
<code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">get_realm_keys</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">algorithms</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statuses</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.get_realm_keys.AwaitableGetRealmKeysResult<a class="headerlink" href="#pulumi_keycloak.get_realm_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the keys of a realm. Keys can be filtered by algorithm and status.</p>
<p>Remarks:</p>
<ul class="simple">
<li><p>A key must meet all filter criteria</p></li>
<li><p>This data source may return more than one value.</p></li>
<li><p>If no key matches the filter criteria, then an error will be returned.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>algorithms</strong> (<em>Sequence</em><em>[</em><em>str</em><em>]</em>) – When specified, keys will be filtered by algorithm. The algorithms can be any of <code class="docutils literal notranslate"><span class="pre">HS256</span></code>, <code class="docutils literal notranslate"><span class="pre">RS256</span></code>,<code class="docutils literal notranslate"><span class="pre">AES</span></code>, etc.</p></li>
<li><p><strong>realm_id</strong> (<em>str</em>) – The realm from which the keys will be retrieved.</p></li>
<li><p><strong>statuses</strong> (<em>Sequence</em><em>[</em><em>str</em><em>]</em>) – When specified, keys will be filtered by status. The statuses can be any of <code class="docutils literal notranslate"><span class="pre">ACTIVE</span></code>, <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code> and <code class="docutils literal notranslate"><span class="pre">PASSIVE</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_keycloak.get_role">
<code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">get_role</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.get_role.AwaitableGetRoleResult<a class="headerlink" href="#pulumi_keycloak.get_role" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch properties of a Keycloak role for
usage with other resources, such as <code class="docutils literal notranslate"><span class="pre">GroupRoles</span></code>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_keycloak</span> <span class="k">as</span> <span class="nn">keycloak</span>

<span class="n">realm</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Realm</span><span class="p">(</span><span class="s2">&quot;realm&quot;</span><span class="p">,</span>
    <span class="n">realm</span><span class="o">=</span><span class="s2">&quot;my-realm&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">offline_access</span> <span class="o">=</span> <span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">get_role</span><span class="p">(</span><span class="n">realm_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;offline_access&quot;</span><span class="p">))</span>
<span class="n">group</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;group&quot;</span><span class="p">,</span> <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">group_roles</span> <span class="o">=</span> <span class="n">keycloak</span><span class="o">.</span><span class="n">GroupRoles</span><span class="p">(</span><span class="s2">&quot;groupRoles&quot;</span><span class="p">,</span>
    <span class="n">realm_id</span><span class="o">=</span><span class="n">realm</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">group_id</span><span class="o">=</span><span class="n">group</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">role_ids</span><span class="o">=</span><span class="p">[</span><span class="n">offline_access</span><span class="o">.</span><span class="n">id</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>client_id</strong> (<em>str</em>) – When specified, this role is assumed to be a client role belonging to the client with the provided ID. The <code class="docutils literal notranslate"><span class="pre">id</span></code> attribute of a <code class="docutils literal notranslate"><span class="pre">keycloak_client</span></code> resource should be used here.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the role.</p></li>
<li><p><strong>realm_id</strong> (<em>str</em>) – The realm this role exists within.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_keycloak.get_user">
<code class="sig-prename descclassname">pulumi_keycloak.</code><code class="sig-name descname">get_user</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">realm_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_keycloak.get_user.AwaitableGetUserResult<a class="headerlink" href="#pulumi_keycloak.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source can be used to fetch properties of a user within Keycloak.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>realm_id</strong> (<em>str</em>) – The realm this user belongs to.</p></li>
<li><p><strong>username</strong> (<em>str</em>) – The unique username of this user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
