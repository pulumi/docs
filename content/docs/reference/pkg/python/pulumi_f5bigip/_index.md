---
title: Package pulumi_f5bigip
title_tag: Package pulumi_f5bigip | Python SDK
linktitle: pulumi_f5bigip
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "f5bigip" >}}

<div class="section" id="pulumi-f5bigip">
<h1>Pulumi F5BigIP<a class="headerlink" href="#pulumi-f5bigip" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-f5bigip">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-f5bigip/issues">pulumi/pulumi-f5bigip repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-f5bigip/issues">terraform-providers/terraform-provider-f5bigip repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_f5bigip"></span><dl class="py class">
<dt id="pulumi_f5bigip.As3">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.</code><code class="sig-name descname">As3</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_list</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">as3_json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_filter</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_list</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.As3" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">As3</span></code> provides details about bigip as3 resource</p>
<p>This resource is helpful to configure as3 declarative JSON on BIG-IP.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_f5bigip</span> <span class="k">as</span> <span class="nn">f5bigip</span>

<span class="c1"># Example Usage for json file</span>
<span class="n">as3_example1_as3</span> <span class="o">=</span> <span class="n">f5bigip</span><span class="o">.</span><span class="n">As3</span><span class="p">(</span><span class="s2">&quot;as3-example1As3&quot;</span><span class="p">,</span> <span class="n">as3_json</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;example1.json&quot;</span><span class="p">))</span>
<span class="c1"># Example Usage for json file with tenant filter</span>
<span class="n">as3_example1_index_as3_as3</span> <span class="o">=</span> <span class="n">f5bigip</span><span class="o">.</span><span class="n">As3</span><span class="p">(</span><span class="s2">&quot;as3-example1Index/as3As3&quot;</span><span class="p">,</span>
    <span class="n">as3_json</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;example2.json&quot;</span><span class="p">),</span>
    <span class="n">tenant_filter</span><span class="o">=</span><span class="s2">&quot;Sample_03&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_list</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Application</p></li>
<li><p><strong>as3_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path/Filename of Declarative AS3 JSON which is a json file used with builtin <code class="docutils literal notranslate"><span class="pre">file</span></code> function</p></li>
<li><p><strong>tenant_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If there are muntiple tenants in a json this attribute helps the user to set a particular tenant to which he want to reflect the changes. Other tenants will neither be created nor be modified</p></li>
<li><p><strong>tenant_list</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Tenant</p></li>
<li><p><strong>tenant_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Tenant</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_f5bigip.As3.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">application_list</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">as3_json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_filter</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_list</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_f5bigip.as3.As3<a class="headerlink" href="#pulumi_f5bigip.As3.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing As3 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_list</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Application</p></li>
<li><p><strong>as3_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path/Filename of Declarative AS3 JSON which is a json file used with builtin <code class="docutils literal notranslate"><span class="pre">file</span></code> function</p></li>
<li><p><strong>tenant_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If there are muntiple tenants in a json this attribute helps the user to set a particular tenant to which he want to reflect the changes. Other tenants will neither be created nor be modified</p></li>
<li><p><strong>tenant_list</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Tenant</p></li>
<li><p><strong>tenant_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Tenant</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.As3.application_list">
<em class="property">property </em><code class="sig-name descname">application_list</code><a class="headerlink" href="#pulumi_f5bigip.As3.application_list" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Application</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.As3.as3_json">
<em class="property">property </em><code class="sig-name descname">as3_json</code><a class="headerlink" href="#pulumi_f5bigip.As3.as3_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Path/Filename of Declarative AS3 JSON which is a json file used with builtin <code class="docutils literal notranslate"><span class="pre">file</span></code> function</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.As3.tenant_filter">
<em class="property">property </em><code class="sig-name descname">tenant_filter</code><a class="headerlink" href="#pulumi_f5bigip.As3.tenant_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>If there are muntiple tenants in a json this attribute helps the user to set a particular tenant to which he want to reflect the changes. Other tenants will neither be created nor be modified</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.As3.tenant_list">
<em class="property">property </em><code class="sig-name descname">tenant_list</code><a class="headerlink" href="#pulumi_f5bigip.As3.tenant_list" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Tenant</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.As3.tenant_name">
<em class="property">property </em><code class="sig-name descname">tenant_name</code><a class="headerlink" href="#pulumi_f5bigip.As3.tenant_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Tenant</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.As3.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.As3.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.As3.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.As3.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.BigIqAs3">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.</code><code class="sig-name descname">BigIqAs3</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">as3_json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_login_ref</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_port</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_token_auth</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_user</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_list</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.BigIqAs3" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a BigIqAs3 resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] as3_json: AS3 json
:param pulumi.Input[str] bigiq_address: The registration key pool to use
:param pulumi.Input[str] bigiq_login_ref: Login reference for token authentication (see BIG-IQ REST docs for details)
:param pulumi.Input[str] bigiq_password: The registration key pool to use
:param pulumi.Input[str] bigiq_port: The registration key pool to use
:param pulumi.Input[bool] bigiq_token_auth: Enable to use an external authentication source (LDAP, TACACS, etc)
:param pulumi.Input[str] bigiq_user: The registration key pool to use
:param pulumi.Input[str] tenant_list: Name of Tenant</p>
<dl class="py method">
<dt id="pulumi_f5bigip.BigIqAs3.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">as3_json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_login_ref</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_port</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_token_auth</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_user</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_list</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_f5bigip.big_iq_as3.BigIqAs3<a class="headerlink" href="#pulumi_f5bigip.BigIqAs3.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BigIqAs3 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>as3_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AS3 json</p></li>
<li><p><strong>bigiq_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The registration key pool to use</p></li>
<li><p><strong>bigiq_login_ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login reference for token authentication (see BIG-IQ REST docs for details)</p></li>
<li><p><strong>bigiq_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The registration key pool to use</p></li>
<li><p><strong>bigiq_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The registration key pool to use</p></li>
<li><p><strong>bigiq_token_auth</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable to use an external authentication source (LDAP, TACACS, etc)</p></li>
<li><p><strong>bigiq_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The registration key pool to use</p></li>
<li><p><strong>tenant_list</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Tenant</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.BigIqAs3.as3_json">
<em class="property">property </em><code class="sig-name descname">as3_json</code><a class="headerlink" href="#pulumi_f5bigip.BigIqAs3.as3_json" title="Permalink to this definition">¶</a></dt>
<dd><p>AS3 json</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.BigIqAs3.bigiq_address">
<em class="property">property </em><code class="sig-name descname">bigiq_address</code><a class="headerlink" href="#pulumi_f5bigip.BigIqAs3.bigiq_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The registration key pool to use</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.BigIqAs3.bigiq_login_ref">
<em class="property">property </em><code class="sig-name descname">bigiq_login_ref</code><a class="headerlink" href="#pulumi_f5bigip.BigIqAs3.bigiq_login_ref" title="Permalink to this definition">¶</a></dt>
<dd><p>Login reference for token authentication (see BIG-IQ REST docs for details)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.BigIqAs3.bigiq_password">
<em class="property">property </em><code class="sig-name descname">bigiq_password</code><a class="headerlink" href="#pulumi_f5bigip.BigIqAs3.bigiq_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The registration key pool to use</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.BigIqAs3.bigiq_port">
<em class="property">property </em><code class="sig-name descname">bigiq_port</code><a class="headerlink" href="#pulumi_f5bigip.BigIqAs3.bigiq_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The registration key pool to use</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.BigIqAs3.bigiq_token_auth">
<em class="property">property </em><code class="sig-name descname">bigiq_token_auth</code><a class="headerlink" href="#pulumi_f5bigip.BigIqAs3.bigiq_token_auth" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable to use an external authentication source (LDAP, TACACS, etc)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.BigIqAs3.bigiq_user">
<em class="property">property </em><code class="sig-name descname">bigiq_user</code><a class="headerlink" href="#pulumi_f5bigip.BigIqAs3.bigiq_user" title="Permalink to this definition">¶</a></dt>
<dd><p>The registration key pool to use</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.BigIqAs3.tenant_list">
<em class="property">property </em><code class="sig-name descname">tenant_list</code><a class="headerlink" href="#pulumi_f5bigip.BigIqAs3.tenant_list" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Tenant</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.BigIqAs3.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.BigIqAs3.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.BigIqAs3.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.BigIqAs3.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.Command">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.</code><code class="sig-name descname">Command</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">command_results</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">commands</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">when</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.Command" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">Command</span></code> Run TMSH commands on F5 devices</p>
<p>This resource is helpful to send TMSH command to an BIG-IP node and returns the results read from the device</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_f5bigip</span> <span class="k">as</span> <span class="nn">f5bigip</span>

<span class="c1">#create ltm node</span>
<span class="n">test_command</span> <span class="o">=</span> <span class="n">f5bigip</span><span class="o">.</span><span class="n">Command</span><span class="p">(</span><span class="s2">&quot;test-command&quot;</span><span class="p">,</span>
    <span class="n">commands</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;delete ltm node 10.10.10.70&quot;</span><span class="p">],</span>
    <span class="n">when</span><span class="o">=</span><span class="s2">&quot;destroy&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>command_results</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The resulting output from the <code class="docutils literal notranslate"><span class="pre">commands</span></code> executed</p></li>
<li><p><strong>commands</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The commands to send to the remote BIG-IP device over the configured provider. The resulting output from the command is returned and added to <code class="docutils literal notranslate"><span class="pre">command_result</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_f5bigip.Command.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">command_results</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">commands</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">when</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_f5bigip.command.Command<a class="headerlink" href="#pulumi_f5bigip.Command.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Command resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>command_results</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The resulting output from the <code class="docutils literal notranslate"><span class="pre">commands</span></code> executed</p></li>
<li><p><strong>commands</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The commands to send to the remote BIG-IP device over the configured provider. The resulting output from the command is returned and added to <code class="docutils literal notranslate"><span class="pre">command_result</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.Command.command_results">
<em class="property">property </em><code class="sig-name descname">command_results</code><a class="headerlink" href="#pulumi_f5bigip.Command.command_results" title="Permalink to this definition">¶</a></dt>
<dd><p>The resulting output from the <code class="docutils literal notranslate"><span class="pre">commands</span></code> executed</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.Command.commands">
<em class="property">property </em><code class="sig-name descname">commands</code><a class="headerlink" href="#pulumi_f5bigip.Command.commands" title="Permalink to this definition">¶</a></dt>
<dd><p>The commands to send to the remote BIG-IP device over the configured provider. The resulting output from the command is returned and added to <code class="docutils literal notranslate"><span class="pre">command_result</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.Command.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.Command.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.Command.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.Command.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.</code><code class="sig-name descname">CommonLicenseManageBigIq</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assignment_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_login_ref</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_port</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_token_auth</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_user</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_license_status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hypervisor</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_poolname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mac_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skukeyword1</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skukeyword2</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unit_of_measure</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">CommonLicenseManageBigIq</span></code> This Resource is used for BIGIP/Provider License Management from BIGIQ</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_f5bigip</span> <span class="k">as</span> <span class="nn">f5bigip</span>

<span class="c1"># MANAGED Regkey Pool</span>
<span class="n">test_example_common_license_manage_big_iq</span> <span class="o">=</span> <span class="n">f5bigip</span><span class="o">.</span><span class="n">CommonLicenseManageBigIq</span><span class="p">(</span><span class="s2">&quot;testExampleCommonLicenseManageBigIq&quot;</span><span class="p">,</span>
    <span class="n">bigiq_address</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;bigiq&quot;</span><span class="p">],</span>
    <span class="n">bigiq_user</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;bigiq_un&quot;</span><span class="p">],</span>
    <span class="n">bigiq_password</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;bigiq_pw&quot;</span><span class="p">],</span>
    <span class="n">license_poolname</span><span class="o">=</span><span class="s2">&quot;regkeypool_name&quot;</span><span class="p">,</span>
    <span class="n">assignment_type</span><span class="o">=</span><span class="s2">&quot;MANAGED&quot;</span><span class="p">)</span>
<span class="c1"># UNMANAGED Regkey Pool</span>
<span class="n">test_example_index_common_license_manage_big_iq_common_license_manage_big_iq</span> <span class="o">=</span> <span class="n">f5bigip</span><span class="o">.</span><span class="n">CommonLicenseManageBigIq</span><span class="p">(</span><span class="s2">&quot;testExampleIndex/commonLicenseManageBigIqCommonLicenseManageBigIq&quot;</span><span class="p">,</span>
    <span class="n">bigiq_address</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;bigiq&quot;</span><span class="p">],</span>
    <span class="n">bigiq_user</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;bigiq_un&quot;</span><span class="p">],</span>
    <span class="n">bigiq_password</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;bigiq_pw&quot;</span><span class="p">],</span>
    <span class="n">license_poolname</span><span class="o">=</span><span class="s2">&quot;regkeypool_name&quot;</span><span class="p">,</span>
    <span class="n">assignment_type</span><span class="o">=</span><span class="s2">&quot;UNMANAGED&quot;</span><span class="p">)</span>
<span class="c1"># UNMANAGED Utility Pool</span>
<span class="n">test_example_f5bigip_index_common_license_manage_big_iq_common_license_manage_big_iq</span> <span class="o">=</span> <span class="n">f5bigip</span><span class="o">.</span><span class="n">CommonLicenseManageBigIq</span><span class="p">(</span><span class="s2">&quot;testExampleF5bigipIndex/commonLicenseManageBigIqCommonLicenseManageBigIq&quot;</span><span class="p">,</span>
    <span class="n">bigiq_address</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;bigiq&quot;</span><span class="p">],</span>
    <span class="n">bigiq_user</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;bigiq_un&quot;</span><span class="p">],</span>
    <span class="n">bigiq_password</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;bigiq_pw&quot;</span><span class="p">],</span>
    <span class="n">license_poolname</span><span class="o">=</span><span class="s2">&quot;utilitypool_name&quot;</span><span class="p">,</span>
    <span class="n">assignment_type</span><span class="o">=</span><span class="s2">&quot;UNMANAGED&quot;</span><span class="p">,</span>
    <span class="n">unit_of_measure</span><span class="o">=</span><span class="s2">&quot;yearly&quot;</span><span class="p">,</span>
    <span class="n">skukeyword1</span><span class="o">=</span><span class="s2">&quot;BTHSM200M&quot;</span><span class="p">)</span>
<span class="c1"># UNREACHABLE Regkey Pool</span>
<span class="n">test_example_f5bigip_index_common_license_manage_big_iq_common_license_manage_big_iq1</span> <span class="o">=</span> <span class="n">f5bigip</span><span class="o">.</span><span class="n">CommonLicenseManageBigIq</span><span class="p">(</span><span class="s2">&quot;testExampleF5bigipIndex/commonLicenseManageBigIqCommonLicenseManageBigIq1&quot;</span><span class="p">,</span>
    <span class="n">bigiq_address</span><span class="o">=</span><span class="s2">&quot;xxx.xxx.xxx.xxx&quot;</span><span class="p">,</span>
    <span class="n">bigiq_user</span><span class="o">=</span><span class="s2">&quot;xxxx&quot;</span><span class="p">,</span>
    <span class="n">bigiq_password</span><span class="o">=</span><span class="s2">&quot;xxxxx&quot;</span><span class="p">,</span>
    <span class="n">license_poolname</span><span class="o">=</span><span class="s2">&quot;regkey_pool_name&quot;</span><span class="p">,</span>
    <span class="n">assignment_type</span><span class="o">=</span><span class="s2">&quot;UNREACHABLE&quot;</span><span class="p">,</span>
    <span class="n">mac_address</span><span class="o">=</span><span class="s2">&quot;FA:16:3E:1B:6D:32&quot;</span><span class="p">,</span>
    <span class="n">hypervisor</span><span class="o">=</span><span class="s2">&quot;azure&quot;</span><span class="p">)</span>
<span class="c1"># MANAGED Purchased Pool</span>
<span class="n">test_example_f5bigip_index_common_license_manage_big_iq_common_license_manage_big_iq2</span> <span class="o">=</span> <span class="n">f5bigip</span><span class="o">.</span><span class="n">CommonLicenseManageBigIq</span><span class="p">(</span><span class="s2">&quot;testExampleF5bigipIndex/commonLicenseManageBigIqCommonLicenseManageBigIq2&quot;</span><span class="p">,</span>
    <span class="n">bigiq_address</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;bigiq&quot;</span><span class="p">],</span>
    <span class="n">bigiq_user</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;bigiq_un&quot;</span><span class="p">],</span>
    <span class="n">bigiq_password</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;bigiq_pw&quot;</span><span class="p">],</span>
    <span class="n">license_poolname</span><span class="o">=</span><span class="s2">&quot;purchased_pool_name&quot;</span><span class="p">,</span>
    <span class="n">assignment_type</span><span class="o">=</span><span class="s2">&quot;MANAGED&quot;</span><span class="p">)</span>
<span class="c1"># UNMANAGED Purchased Pool</span>
<span class="n">test_example_f5bigip_index_common_license_manage_big_iq_common_license_manage_big_iq3</span> <span class="o">=</span> <span class="n">f5bigip</span><span class="o">.</span><span class="n">CommonLicenseManageBigIq</span><span class="p">(</span><span class="s2">&quot;testExampleF5bigipIndex/commonLicenseManageBigIqCommonLicenseManageBigIq3&quot;</span><span class="p">,</span>
    <span class="n">bigiq_address</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;bigiq&quot;</span><span class="p">],</span>
    <span class="n">bigiq_user</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;bigiq_un&quot;</span><span class="p">],</span>
    <span class="n">bigiq_password</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;bigiq_pw&quot;</span><span class="p">],</span>
    <span class="n">license_poolname</span><span class="o">=</span><span class="s2">&quot;purchased_pool_name&quot;</span><span class="p">,</span>
    <span class="n">assignment_type</span><span class="o">=</span><span class="s2">&quot;UNMANAGED&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>assignment_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of assignment, which is determined by whether the BIG-IP is unreachable, unmanaged, or managed by BIG-IQ. Possible values: “UNREACHABLE”, “UNMANAGED”, or “MANAGED”.</p></li>
<li><p><strong>bigiq_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIGIQ License Manager IP Address, variable type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
<li><p><strong>bigiq_login_ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIGIQ Login reference for token authentication</p></li>
<li><p><strong>bigiq_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIGIQ License Manager password.  variable type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
<li><p><strong>bigiq_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – type <code class="docutils literal notranslate"><span class="pre">int</span></code>, BIGIQ License Manager Port number, specify if port is other than <code class="docutils literal notranslate"><span class="pre">443</span></code></p></li>
<li><p><strong>bigiq_token_auth</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – type <code class="docutils literal notranslate"><span class="pre">bool</span></code>, if set to <code class="docutils literal notranslate"><span class="pre">true</span></code> enables Token based Authentication,default is <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><strong>bigiq_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIGIQ License Manager username, variable type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
<li><p><strong>device_license_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of Licence Assignment</p></li>
<li><p><strong>hypervisor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies the platform running the BIG-IP VE. Possible values: “aws”, “azure”, “gce”, “vmware”, “hyperv”, “kvm”, or “xen”. type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – License Assignment is done with specified <code class="docutils literal notranslate"><span class="pre">key</span></code>, supported only with RegKeypool type License assignement. type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
<li><p><strong>license_poolname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name given to the license pool. type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
<li><p><strong>mac_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – MAC address of the BIG-IP. type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
<li><p><strong>skukeyword1</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional offering name. type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
<li><p><strong>skukeyword2</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional offering name. type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
<li><p><strong>tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For an unreachable BIG-IP, you can provide an optional description for the assignment in this field.</p></li>
<li><p><strong>unit_of_measure</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The units used to measure billing. For example, “hourly” or “daily”. Type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assignment_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_login_ref</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_port</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_token_auth</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bigiq_user</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_license_status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hypervisor</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_poolname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mac_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skukeyword1</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skukeyword2</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unit_of_measure</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_f5bigip.common_license_manage_big_iq.CommonLicenseManageBigIq<a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CommonLicenseManageBigIq resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>assignment_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of assignment, which is determined by whether the BIG-IP is unreachable, unmanaged, or managed by BIG-IQ. Possible values: “UNREACHABLE”, “UNMANAGED”, or “MANAGED”.</p></li>
<li><p><strong>bigiq_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIGIQ License Manager IP Address, variable type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
<li><p><strong>bigiq_login_ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIGIQ Login reference for token authentication</p></li>
<li><p><strong>bigiq_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIGIQ License Manager password.  variable type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
<li><p><strong>bigiq_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – type <code class="docutils literal notranslate"><span class="pre">int</span></code>, BIGIQ License Manager Port number, specify if port is other than <code class="docutils literal notranslate"><span class="pre">443</span></code></p></li>
<li><p><strong>bigiq_token_auth</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – type <code class="docutils literal notranslate"><span class="pre">bool</span></code>, if set to <code class="docutils literal notranslate"><span class="pre">true</span></code> enables Token based Authentication,default is <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><strong>bigiq_user</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – BIGIQ License Manager username, variable type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
<li><p><strong>device_license_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of Licence Assignment</p></li>
<li><p><strong>hypervisor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifies the platform running the BIG-IP VE. Possible values: “aws”, “azure”, “gce”, “vmware”, “hyperv”, “kvm”, or “xen”. type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – License Assignment is done with specified <code class="docutils literal notranslate"><span class="pre">key</span></code>, supported only with RegKeypool type License assignement. type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
<li><p><strong>license_poolname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name given to the license pool. type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
<li><p><strong>mac_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – MAC address of the BIG-IP. type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
<li><p><strong>skukeyword1</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional offering name. type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
<li><p><strong>skukeyword2</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional offering name. type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
<li><p><strong>tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For an unreachable BIG-IP, you can provide an optional description for the assignment in this field.</p></li>
<li><p><strong>unit_of_measure</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The units used to measure billing. For example, “hourly” or “daily”. Type <code class="docutils literal notranslate"><span class="pre">string</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.assignment_type">
<em class="property">property </em><code class="sig-name descname">assignment_type</code><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.assignment_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of assignment, which is determined by whether the BIG-IP is unreachable, unmanaged, or managed by BIG-IQ. Possible values: “UNREACHABLE”, “UNMANAGED”, or “MANAGED”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.bigiq_address">
<em class="property">property </em><code class="sig-name descname">bigiq_address</code><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.bigiq_address" title="Permalink to this definition">¶</a></dt>
<dd><p>BIGIQ License Manager IP Address, variable type <code class="docutils literal notranslate"><span class="pre">string</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.bigiq_login_ref">
<em class="property">property </em><code class="sig-name descname">bigiq_login_ref</code><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.bigiq_login_ref" title="Permalink to this definition">¶</a></dt>
<dd><p>BIGIQ Login reference for token authentication</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.bigiq_password">
<em class="property">property </em><code class="sig-name descname">bigiq_password</code><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.bigiq_password" title="Permalink to this definition">¶</a></dt>
<dd><p>BIGIQ License Manager password.  variable type <code class="docutils literal notranslate"><span class="pre">string</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.bigiq_port">
<em class="property">property </em><code class="sig-name descname">bigiq_port</code><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.bigiq_port" title="Permalink to this definition">¶</a></dt>
<dd><p>type <code class="docutils literal notranslate"><span class="pre">int</span></code>, BIGIQ License Manager Port number, specify if port is other than <code class="docutils literal notranslate"><span class="pre">443</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.bigiq_token_auth">
<em class="property">property </em><code class="sig-name descname">bigiq_token_auth</code><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.bigiq_token_auth" title="Permalink to this definition">¶</a></dt>
<dd><p>type <code class="docutils literal notranslate"><span class="pre">bool</span></code>, if set to <code class="docutils literal notranslate"><span class="pre">true</span></code> enables Token based Authentication,default is <code class="docutils literal notranslate"><span class="pre">false</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.bigiq_user">
<em class="property">property </em><code class="sig-name descname">bigiq_user</code><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.bigiq_user" title="Permalink to this definition">¶</a></dt>
<dd><p>BIGIQ License Manager username, variable type <code class="docutils literal notranslate"><span class="pre">string</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.device_license_status">
<em class="property">property </em><code class="sig-name descname">device_license_status</code><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.device_license_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of Licence Assignment</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.hypervisor">
<em class="property">property </em><code class="sig-name descname">hypervisor</code><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.hypervisor" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the platform running the BIG-IP VE. Possible values: “aws”, “azure”, “gce”, “vmware”, “hyperv”, “kvm”, or “xen”. type <code class="docutils literal notranslate"><span class="pre">string</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.key">
<em class="property">property </em><code class="sig-name descname">key</code><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.key" title="Permalink to this definition">¶</a></dt>
<dd><p>License Assignment is done with specified <code class="docutils literal notranslate"><span class="pre">key</span></code>, supported only with RegKeypool type License assignement. type <code class="docutils literal notranslate"><span class="pre">string</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.license_poolname">
<em class="property">property </em><code class="sig-name descname">license_poolname</code><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.license_poolname" title="Permalink to this definition">¶</a></dt>
<dd><p>A name given to the license pool. type <code class="docutils literal notranslate"><span class="pre">string</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.mac_address">
<em class="property">property </em><code class="sig-name descname">mac_address</code><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.mac_address" title="Permalink to this definition">¶</a></dt>
<dd><p>MAC address of the BIG-IP. type <code class="docutils literal notranslate"><span class="pre">string</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.skukeyword1">
<em class="property">property </em><code class="sig-name descname">skukeyword1</code><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.skukeyword1" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional offering name. type <code class="docutils literal notranslate"><span class="pre">string</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.skukeyword2">
<em class="property">property </em><code class="sig-name descname">skukeyword2</code><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.skukeyword2" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional offering name. type <code class="docutils literal notranslate"><span class="pre">string</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.tenant">
<em class="property">property </em><code class="sig-name descname">tenant</code><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.tenant" title="Permalink to this definition">¶</a></dt>
<dd><p>For an unreachable BIG-IP, you can provide an optional description for the assignment in this field.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.unit_of_measure">
<em class="property">property </em><code class="sig-name descname">unit_of_measure</code><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.unit_of_measure" title="Permalink to this definition">¶</a></dt>
<dd><p>The units used to measure billing. For example, “hourly” or “daily”. Type <code class="docutils literal notranslate"><span class="pre">string</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.CommonLicenseManageBigIq.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.CommonLicenseManageBigIq.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.Do">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.</code><code class="sig-name descname">Do</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">do_json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.Do" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">Do</span></code> provides details about bigip do resource</p>
<p>This resource is helpful to configure do declarative JSON on BIG-IP.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_f5bigip</span> <span class="k">as</span> <span class="nn">f5bigip</span>

<span class="n">do_example</span> <span class="o">=</span> <span class="n">f5bigip</span><span class="o">.</span><span class="n">Do</span><span class="p">(</span><span class="s2">&quot;do-example&quot;</span><span class="p">,</span>
    <span class="n">do_json</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;example.json&quot;</span><span class="p">),</span>
    <span class="n">timeout</span><span class="o">=</span><span class="mi">15</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>do_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the of the Declarative DO JSON file</p></li>
<li><p><strong>tenant_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – unique identifier for DO resource</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – DO json</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_f5bigip.Do.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">do_json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_f5bigip.do.Do<a class="headerlink" href="#pulumi_f5bigip.Do.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Do resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>do_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the of the Declarative DO JSON file</p></li>
<li><p><strong>tenant_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – unique identifier for DO resource</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – DO json</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.Do.do_json">
<em class="property">property </em><code class="sig-name descname">do_json</code><a class="headerlink" href="#pulumi_f5bigip.Do.do_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the of the Declarative DO JSON file</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.Do.tenant_name">
<em class="property">property </em><code class="sig-name descname">tenant_name</code><a class="headerlink" href="#pulumi_f5bigip.Do.tenant_name" title="Permalink to this definition">¶</a></dt>
<dd><p>unique identifier for DO resource</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.Do.timeout">
<em class="property">property </em><code class="sig-name descname">timeout</code><a class="headerlink" href="#pulumi_f5bigip.Do.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>DO json</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.Do.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.Do.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.Do.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.Do.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.EventServiceDiscovery">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.</code><code class="sig-name descname">EventServiceDiscovery</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[EventServiceDiscoveryNodeArgs, Mapping[str, Any], Awaitable[Union[EventServiceDiscoveryNodeArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[EventServiceDiscoveryNodeArgs, Mapping[str, Any], Awaitable[Union[EventServiceDiscoveryNodeArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">taskid</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.EventServiceDiscovery" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a EventServiceDiscovery resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] taskid: Name of the partition/tenant</p>
<dl class="py method">
<dt id="pulumi_f5bigip.EventServiceDiscovery.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[EventServiceDiscoveryNodeArgs, Mapping[str, Any], Awaitable[Union[EventServiceDiscoveryNodeArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[EventServiceDiscoveryNodeArgs, Mapping[str, Any], Awaitable[Union[EventServiceDiscoveryNodeArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">taskid</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_f5bigip.event_service_discovery.EventServiceDiscovery<a class="headerlink" href="#pulumi_f5bigip.EventServiceDiscovery.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventServiceDiscovery resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>taskid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the partition/tenant</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.EventServiceDiscovery.taskid">
<em class="property">property </em><code class="sig-name descname">taskid</code><a class="headerlink" href="#pulumi_f5bigip.EventServiceDiscovery.taskid" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the partition/tenant</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.EventServiceDiscovery.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.EventServiceDiscovery.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.EventServiceDiscovery.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.EventServiceDiscovery.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_ref</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teem_disable</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_auth</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the bigip package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name/IP of the BigIP</p></li>
<li><p><strong>login_ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Login reference for token authentication (see BIG-IP REST docs for details)</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user’s password</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Management Port to connect to Bigip</p></li>
<li><p><strong>teem_disable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If this flag set to true,sending telemetry data to TEEM will be disabled</p></li>
<li><p><strong>token_auth</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable to use an external authentication source (LDAP, TACACS, etc)</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username with API access to the BigIP</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_f5bigip.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
