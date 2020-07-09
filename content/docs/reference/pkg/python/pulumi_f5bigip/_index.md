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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.</code><code class="sig-name descname">As3</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">as3_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_list</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.As3" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">As3</span></code> provides details about bigip as3 resource</p>
<p>This resource is helpful to configure as3 declarative JSON on BIG-IP.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_f5bigip</span> <span class="k">as</span> <span class="nn">f5bigip</span>

<span class="c1"># Example Usage for json file with tenant filter</span>
<span class="n">as3_example1</span> <span class="o">=</span> <span class="n">f5bigip</span><span class="o">.</span><span class="n">As3</span><span class="p">(</span><span class="s2">&quot;as3-example1&quot;</span><span class="p">,</span>
    <span class="n">as3_json</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;example2.json&quot;</span><span class="p">),</span>
    <span class="n">tenant_filter</span><span class="o">=</span><span class="s2">&quot;Sample_03&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>as3_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path/Filename of Declarative AS3 JSON which is a json file used with builtin <code class="docutils literal notranslate"><span class="pre">file</span></code> function</p></li>
<li><p><strong>tenant_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If there are muntiple tenants in a json this attribute helps the user to set a particular tenant to which he want to reflect the changes. Other tenants will neither be created nor be modified</p></li>
<li><p><strong>tenant_list</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Tenant</p></li>
<li><p><strong>tenant_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Tenant</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_f5bigip.As3.as3_json">
<code class="sig-name descname">as3_json</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.As3.as3_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Path/Filename of Declarative AS3 JSON which is a json file used with builtin <code class="docutils literal notranslate"><span class="pre">file</span></code> function</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_f5bigip.As3.tenant_filter">
<code class="sig-name descname">tenant_filter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.As3.tenant_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>If there are muntiple tenants in a json this attribute helps the user to set a particular tenant to which he want to reflect the changes. Other tenants will neither be created nor be modified</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_f5bigip.As3.tenant_list">
<code class="sig-name descname">tenant_list</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.As3.tenant_list" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Tenant</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_f5bigip.As3.tenant_name">
<code class="sig-name descname">tenant_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.As3.tenant_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Tenant</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.As3.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">as3_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_list</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.As3.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing As3 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>as3_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path/Filename of Declarative AS3 JSON which is a json file used with builtin <code class="docutils literal notranslate"><span class="pre">file</span></code> function</p></li>
<li><p><strong>tenant_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If there are muntiple tenants in a json this attribute helps the user to set a particular tenant to which he want to reflect the changes. Other tenants will neither be created nor be modified</p></li>
<li><p><strong>tenant_list</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Tenant</p></li>
<li><p><strong>tenant_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Tenant</p></li>
</ul>
</dd>
</dl>
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
<dt id="pulumi_f5bigip.Do">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.</code><code class="sig-name descname">Do</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">do_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.Do" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – DO json</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_f5bigip.Do.do_json">
<code class="sig-name descname">do_json</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.Do.do_json" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the of the Declarative DO JSON file</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_f5bigip.Do.tenant_name">
<code class="sig-name descname">tenant_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.Do.tenant_name" title="Permalink to this definition">¶</a></dt>
<dd><p>unique identifier for DO resource</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_f5bigip.Do.timeout">
<code class="sig-name descname">timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.Do.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>DO json</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.Do.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">do_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.Do.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Do resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>do_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the of the Declarative DO JSON file</p></li>
<li><p><strong>tenant_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – unique identifier for DO resource</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – DO json</p></li>
</ul>
</dd>
</dl>
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
<dt id="pulumi_f5bigip.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login_ref</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token_auth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.Provider" title="Permalink to this definition">¶</a></dt>
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
