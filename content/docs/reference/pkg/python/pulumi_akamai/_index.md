---
title: Package pulumi_akamai
title_tag: Package pulumi_akamai | Python SDK
linktitle: pulumi_akamai
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "akamai" >}}

<div class="section" id="pulumi-akamai">
<h1>Pulumi Akamai<a class="headerlink" href="#pulumi-akamai" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-akamai">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-akamai/issues">pulumi/pulumi-akamai repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-akamai/issues">terraform-providers/terraform-provider-akamai repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_akamai"></span><dl class="py class">
<dt id="pulumi_akamai.AppSecActivations">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AppSecActivations</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">activate</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_emails</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecActivations" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">AppSecActivations</span></code> resource allows you to activate or deactivate a given security configuration version.</p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">configuration</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_configuration</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Akamai Tools&quot;</span><span class="p">)</span>
<span class="n">activation</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">AppSecActivations</span><span class="p">(</span><span class="s2">&quot;activation&quot;</span><span class="p">,</span>
    <span class="n">config_id</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">config_id</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">latest_version</span><span class="p">,</span>
    <span class="n">network</span><span class="o">=</span><span class="s2">&quot;STAGING&quot;</span><span class="p">,</span>
    <span class="n">notes</span><span class="o">=</span><span class="s2">&quot;TEST Notes&quot;</span><span class="p">,</span>
    <span class="n">notification_emails</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;user@example.com&quot;</span><span class="p">])</span>
</pre></div>
</div>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">config_id</span></code> - (Required) The ID of the security configuration to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> - (Required) The version number of the security configuration to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notification_emails</span></code> - (Required) A bracketed, comma-separated list of email addresses that will be notified when the operation is complete.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> - The network in which the security configuration should be activated. If supplied, must be either STAGING or PRODUCTION. If not supplied, STAGING will be assumed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notes</span></code> - An optional text note describing this operation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">activate</span></code> - A boolean indicating whether to activate the specified configuration version. If not supplied, True is assumed.</p></li>
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
<dt id="pulumi_akamai.AppSecActivations.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">activate</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notes</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_emails</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.app_sec_activations.AppSecActivations<a class="headerlink" href="#pulumi_akamai.AppSecActivations.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AppSecActivations resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the operation. The following values are may be returned:</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecActivations.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_akamai.AppSecActivations.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the operation. The following values are may be returned:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecActivations.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecActivations.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.AppSecActivations.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecActivations.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.AppSecConfigurationVersionClone">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AppSecConfigurationVersionClone</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_from_version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_update</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecConfigurationVersionClone" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AppSecConfigurationVersionClone resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_akamai.AppSecConfigurationVersionClone.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_from_version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_update</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.app_sec_configuration_version_clone.AppSecConfigurationVersionClone<a class="headerlink" href="#pulumi_akamai.AppSecConfigurationVersionClone.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AppSecConfigurationVersionClone resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Version of cloned configuration</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecConfigurationVersionClone.version">
<em class="property">property </em><code class="sig-name descname">version</code><a class="headerlink" href="#pulumi_akamai.AppSecConfigurationVersionClone.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of cloned configuration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecConfigurationVersionClone.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecConfigurationVersionClone.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.AppSecConfigurationVersionClone.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecConfigurationVersionClone.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.AppSecCustomRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AppSecCustomRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecCustomRule" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">AppSecCustomRule</span></code> resource allows you to create or modify a custom rule associated with a given security configuration.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the security configuration to use.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a JSON file containing a custom rule definition (<a class="reference external" href="https://developer.akamai.com/api/cloud_security/application_security/v1.html#postcustomrules">format</a>).</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_akamai.AppSecCustomRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_rule_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.app_sec_custom_rule.AppSecCustomRule<a class="headerlink" href="#pulumi_akamai.AppSecCustomRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AppSecCustomRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the security configuration to use.</p></li>
<li><p><strong>custom_rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the custom rule.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of a JSON file containing a custom rule definition (<a class="reference external" href="https://developer.akamai.com/api/cloud_security/application_security/v1.html#postcustomrules">format</a>).</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecCustomRule.config_id">
<em class="property">property </em><code class="sig-name descname">config_id</code><a class="headerlink" href="#pulumi_akamai.AppSecCustomRule.config_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security configuration to use.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecCustomRule.custom_rule_id">
<em class="property">property </em><code class="sig-name descname">custom_rule_id</code><a class="headerlink" href="#pulumi_akamai.AppSecCustomRule.custom_rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the custom rule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecCustomRule.rules">
<em class="property">property </em><code class="sig-name descname">rules</code><a class="headerlink" href="#pulumi_akamai.AppSecCustomRule.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a JSON file containing a custom rule definition (<a class="reference external" href="https://developer.akamai.com/api/cloud_security/application_security/v1.html#postcustomrules">format</a>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecCustomRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecCustomRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.AppSecCustomRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecCustomRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.AppSecCustomRuleAction">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AppSecCustomRuleAction</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_rule_action</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_rule_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecCustomRuleAction" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">AppSecCustomRuleAction</span></code> resource allows you to associate an action to a custom rule.</p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">configuration</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_configuration</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Akamai Tools&quot;</span><span class="p">)</span>
<span class="n">create_custom_rule_action</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">AppSecCustomRuleAction</span><span class="p">(</span><span class="s2">&quot;createCustomRuleAction&quot;</span><span class="p">,</span>
    <span class="n">config_id</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">config_id</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">latest_version</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="s2">&quot;crAP_75829&quot;</span><span class="p">,</span>
    <span class="n">custom_rule_id</span><span class="o">=</span><span class="mi">12345</span><span class="p">,</span>
    <span class="n">custom_rule_action</span><span class="o">=</span><span class="s2">&quot;alert&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;customRuleId&quot;</span><span class="p">,</span> <span class="n">create_custom_rule_action</span><span class="o">.</span><span class="n">custom_rule_id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the security configuration to use.</p></li>
<li><p><strong>custom_rule_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action to be taken when the custom rule is invoked. Must be one of the following:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">alert</span>
<span class="o">*</span> <span class="n">deny</span>
<span class="o">*</span> <span class="n">none</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>custom_rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the custom rule.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The version number of the security configuration to use.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_akamai.AppSecCustomRuleAction.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_rule_action</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_rule_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.app_sec_custom_rule_action.AppSecCustomRuleAction<a class="headerlink" href="#pulumi_akamai.AppSecCustomRuleAction.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AppSecCustomRuleAction resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the security configuration to use.</p></li>
<li><p><strong>custom_rule_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The action to be taken when the custom rule is invoked. Must be one of the following:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">alert</span>
<span class="o">*</span> <span class="n">deny</span>
<span class="o">*</span> <span class="n">none</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>custom_rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the custom rule.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The version number of the security configuration to use.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecCustomRuleAction.config_id">
<em class="property">property </em><code class="sig-name descname">config_id</code><a class="headerlink" href="#pulumi_akamai.AppSecCustomRuleAction.config_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security configuration to use.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecCustomRuleAction.custom_rule_action">
<em class="property">property </em><code class="sig-name descname">custom_rule_action</code><a class="headerlink" href="#pulumi_akamai.AppSecCustomRuleAction.custom_rule_action" title="Permalink to this definition">¶</a></dt>
<dd><p>The action to be taken when the custom rule is invoked. Must be one of the following:</p>
<ul class="simple">
<li><p>alert</p></li>
<li><p>deny</p></li>
<li><p>none</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecCustomRuleAction.custom_rule_id">
<em class="property">property </em><code class="sig-name descname">custom_rule_id</code><a class="headerlink" href="#pulumi_akamai.AppSecCustomRuleAction.custom_rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the custom rule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecCustomRuleAction.policy_id">
<em class="property">property </em><code class="sig-name descname">policy_id</code><a class="headerlink" href="#pulumi_akamai.AppSecCustomRuleAction.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecCustomRuleAction.version">
<em class="property">property </em><code class="sig-name descname">version</code><a class="headerlink" href="#pulumi_akamai.AppSecCustomRuleAction.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version number of the security configuration to use.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecCustomRuleAction.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecCustomRuleAction.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.AppSecCustomRuleAction.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecCustomRuleAction.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.AppSecMatchTarget">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AppSecMatchTarget</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecMatchTarget" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">AppSecMatchTarget</span></code> resource allows you to create or modify a match target associated with a given security configuration version.</p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">configuration</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_configuration</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Akamai Tools&quot;</span><span class="p">)</span>
<span class="n">match_target</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">AppSecMatchTarget</span><span class="p">(</span><span class="s2">&quot;matchTarget&quot;</span><span class="p">,</span>
    <span class="n">config_id</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">config_id</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">latest_version</span><span class="p">,</span>
    <span class="n">json</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">path</span><span class="p">[</span><span class="s1">&#39;module&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">/match_targets.json&quot;</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the security configuration to use.</p></li>
<li><p><strong>json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of a JSON file containing one or more match target definitions (<a class="reference external" href="https://developer.akamai.com/api/cloud_security/application_security/v1.html#postmatchtargets">format</a>).</p>
</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The version number of the security configuration to use.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_akamai.AppSecMatchTarget.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">match_target_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.app_sec_match_target.AppSecMatchTarget<a class="headerlink" href="#pulumi_akamai.AppSecMatchTarget.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AppSecMatchTarget resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the security configuration to use.</p></li>
<li><p><strong>json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of a JSON file containing one or more match target definitions (<a class="reference external" href="https://developer.akamai.com/api/cloud_security/application_security/v1.html#postmatchtargets">format</a>).</p>
</p></li>
<li><p><strong>match_target_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the match target.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The version number of the security configuration to use.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecMatchTarget.config_id">
<em class="property">property </em><code class="sig-name descname">config_id</code><a class="headerlink" href="#pulumi_akamai.AppSecMatchTarget.config_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security configuration to use.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecMatchTarget.json">
<em class="property">property </em><code class="sig-name descname">json</code><a class="headerlink" href="#pulumi_akamai.AppSecMatchTarget.json" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a JSON file containing one or more match target definitions (<a class="reference external" href="https://developer.akamai.com/api/cloud_security/application_security/v1.html#postmatchtargets">format</a>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecMatchTarget.match_target_id">
<em class="property">property </em><code class="sig-name descname">match_target_id</code><a class="headerlink" href="#pulumi_akamai.AppSecMatchTarget.match_target_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the match target.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecMatchTarget.version">
<em class="property">property </em><code class="sig-name descname">version</code><a class="headerlink" href="#pulumi_akamai.AppSecMatchTarget.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version number of the security configuration to use.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecMatchTarget.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecMatchTarget.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.AppSecMatchTarget.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecMatchTarget.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.AppSecMatchTargetSequence">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AppSecMatchTargetSequence</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sequence_map</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecMatchTargetSequence" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">AppSecMatchTargetSequence</span></code> resource allows you to specify the order in which match targets are applied within a given security configuration version.</p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">configuration</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_configuration</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Akamai Tools&quot;</span><span class="p">)</span>
<span class="n">match_target_sequence</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">AppSecMatchTargetSequence</span><span class="p">(</span><span class="s2">&quot;matchTargetSequence&quot;</span><span class="p">,</span>
    <span class="n">config_id</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">config_id</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">latest_version</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;website&quot;</span><span class="p">,</span>
    <span class="n">json</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">path</span><span class="p">[</span><span class="s1">&#39;module&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">/match_targets.json&quot;</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the security configuration to use.</p></li>
<li><p><strong>json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of a JSON file containing the sequence of all match targets defined for the specified security configuration version (<a class="reference external" href="https://developer.akamai.com/api/cloud_security/application_security/v1.html#putsequence">format</a>).</p>
</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The version number of the security configuration to use.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_akamai.AppSecMatchTargetSequence.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sequence_map</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.app_sec_match_target_sequence.AppSecMatchTargetSequence<a class="headerlink" href="#pulumi_akamai.AppSecMatchTargetSequence.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AppSecMatchTargetSequence resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the security configuration to use.</p></li>
<li><p><strong>json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of a JSON file containing the sequence of all match targets defined for the specified security configuration version (<a class="reference external" href="https://developer.akamai.com/api/cloud_security/application_security/v1.html#putsequence">format</a>).</p>
</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The version number of the security configuration to use.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecMatchTargetSequence.config_id">
<em class="property">property </em><code class="sig-name descname">config_id</code><a class="headerlink" href="#pulumi_akamai.AppSecMatchTargetSequence.config_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security configuration to use.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecMatchTargetSequence.json">
<em class="property">property </em><code class="sig-name descname">json</code><a class="headerlink" href="#pulumi_akamai.AppSecMatchTargetSequence.json" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a JSON file containing the sequence of all match targets defined for the specified security configuration version (<a class="reference external" href="https://developer.akamai.com/api/cloud_security/application_security/v1.html#putsequence">format</a>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecMatchTargetSequence.version">
<em class="property">property </em><code class="sig-name descname">version</code><a class="headerlink" href="#pulumi_akamai.AppSecMatchTargetSequence.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version number of the security configuration to use.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecMatchTargetSequence.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecMatchTargetSequence.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.AppSecMatchTargetSequence.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecMatchTargetSequence.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.AppSecSecurityPolicyClone">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AppSecSecurityPolicyClone</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_from_security_policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_prefix</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecSecurityPolicyClone" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">AppSecSecurityPolicyClone</span></code> resource allows you to create a new security policy by cloning an existing policy.</p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">configuration</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_configuration</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Akamai Tools&quot;</span><span class="p">)</span>
<span class="n">security_policy_clone_app_sec_security_policy_clone</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">AppSecSecurityPolicyClone</span><span class="p">(</span><span class="s2">&quot;securityPolicyCloneAppSecSecurityPolicyClone&quot;</span><span class="p">,</span>
    <span class="n">config_id</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">config_id</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">latest_version</span><span class="p">,</span>
    <span class="n">create_from_security_policy</span><span class="o">=</span><span class="s2">&quot;crAP_75829&quot;</span><span class="p">,</span>
    <span class="n">policy_name</span><span class="o">=</span><span class="s2">&quot;Test Policy 1&quot;</span><span class="p">,</span>
    <span class="n">policy_prefix</span><span class="o">=</span><span class="s2">&quot;TP1&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;securityPolicyClone&quot;</span><span class="p">,</span> <span class="n">security_policy_clone_app_sec_security_policy_clone</span><span class="o">.</span><span class="n">policy_id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the security configuration to use.</p></li>
<li><p><strong>create_from_security_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the security policy to clone.</p></li>
<li><p><strong>policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to be used for the new security policy. If not specified, the name will be autogenerated with the pattern ‘clone from ‘.</p></li>
<li><p><strong>policy_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The four-character policy prefix to be used for the new security policy. If not specified, the prefix will be autogenerated.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_akamai.AppSecSecurityPolicyClone.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_from_security_policy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_prefix</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.app_sec_security_policy_clone.AppSecSecurityPolicyClone<a class="headerlink" href="#pulumi_akamai.AppSecSecurityPolicyClone.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AppSecSecurityPolicyClone resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the security configuration to use.</p></li>
<li><p><strong>create_from_security_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the security policy to clone.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the new security policy.</p></li>
<li><p><strong>policy_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to be used for the new security policy. If not specified, the name will be autogenerated with the pattern ‘clone from ‘.</p></li>
<li><p><strong>policy_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The four-character policy prefix to be used for the new security policy. If not specified, the prefix will be autogenerated.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecSecurityPolicyClone.config_id">
<em class="property">property </em><code class="sig-name descname">config_id</code><a class="headerlink" href="#pulumi_akamai.AppSecSecurityPolicyClone.config_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security configuration to use.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecSecurityPolicyClone.create_from_security_policy">
<em class="property">property </em><code class="sig-name descname">create_from_security_policy</code><a class="headerlink" href="#pulumi_akamai.AppSecSecurityPolicyClone.create_from_security_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security policy to clone.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecSecurityPolicyClone.policy_id">
<em class="property">property </em><code class="sig-name descname">policy_id</code><a class="headerlink" href="#pulumi_akamai.AppSecSecurityPolicyClone.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the new security policy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecSecurityPolicyClone.policy_name">
<em class="property">property </em><code class="sig-name descname">policy_name</code><a class="headerlink" href="#pulumi_akamai.AppSecSecurityPolicyClone.policy_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to be used for the new security policy. If not specified, the name will be autogenerated with the pattern ‘clone from ‘.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecSecurityPolicyClone.policy_prefix">
<em class="property">property </em><code class="sig-name descname">policy_prefix</code><a class="headerlink" href="#pulumi_akamai.AppSecSecurityPolicyClone.policy_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The four-character policy prefix to be used for the new security policy. If not specified, the prefix will be autogenerated.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.AppSecSecurityPolicyClone.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecSecurityPolicyClone.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.AppSecSecurityPolicyClone.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecSecurityPolicyClone.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.AppSecSelectedHostnames">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AppSecSelectedHostnames</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostnames</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecSelectedHostnames" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AppSecSelectedHostnames resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_akamai.AppSecSelectedHostnames.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostnames</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.app_sec_selected_hostnames.AppSecSelectedHostnames<a class="headerlink" href="#pulumi_akamai.AppSecSelectedHostnames.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AppSecSelectedHostnames resource’s state with the given name, id, and optional extra
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
<dt id="pulumi_akamai.AppSecSelectedHostnames.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecSelectedHostnames.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.AppSecSelectedHostnames.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AppSecSelectedHostnames.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.AwaitableGetAppSecConfigurationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetAppSecConfigurationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latest_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">production_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">staging_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetAppSecConfigurationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetAppSecConfigurationVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetAppSecConfigurationVersionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latest_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">production_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">staging_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetAppSecConfigurationVersionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetAppSecCustomRuleActionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetAppSecCustomRuleActionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetAppSecCustomRuleActionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetAppSecCustomRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetAppSecCustomRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_text</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetAppSecCustomRulesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetAppSecExportConfigurationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetAppSecExportConfigurationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">searches</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetAppSecExportConfigurationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetAppSecMatchTargetsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetAppSecMatchTargetsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetAppSecMatchTargetsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetAppSecSecurityPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetAppSecSecurityPolicyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_lists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetAppSecSecurityPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetAppSecSelectableHostnamesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetAppSecSelectableHostnamesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">active_in_production</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active_in_staging</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostnames</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostnames_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetAppSecSelectableHostnamesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetAppSecSelectedHostnamesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetAppSecSelectedHostnamesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostnames</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostnames_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetAppSecSelectedHostnamesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetAuthoritiesSetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetAuthoritiesSetResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">authorities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetAuthoritiesSetResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetContractResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetContractResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetContractResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetContractsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetContractsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">contracts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetContractsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetCpCodeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetCpCodeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">contract</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetCpCodeResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetDnsRecordSetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetDnsRecordSetResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rdatas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">record_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetDnsRecordSetResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">contract</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetGtmDefaultDatacenterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetGtmDefaultDatacenterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nickname</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetGtmDefaultDatacenterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetPropertiesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetPropertiesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">contract_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">properties</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetPropertiesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetPropertyProductsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetPropertyProductsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">contract_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">products</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetPropertyProductsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetPropertyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetPropertyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetPropertyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetPropertyRuleFormatsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetPropertyRuleFormatsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_formats</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetPropertyRuleFormatsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetPropertyRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetPropertyRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">contract_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">errors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">property_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetPropertyRulesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.AwaitableGetPropertyRulesTemplateResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">AwaitableGetPropertyRulesTemplateResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">var_definition_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">var_values_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.AwaitableGetPropertyRulesTemplateResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.CpCode">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">CpCode</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.CpCode" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a CpCode resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_akamai.CpCode.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.cp_code.CpCode<a class="headerlink" href="#pulumi_akamai.CpCode.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CpCode resource’s state with the given name, id, and optional extra
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
<dt id="pulumi_akamai.CpCode.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.CpCode.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.CpCode.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.CpCode.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.DnsRecord">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">DnsRecord</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">algorithm</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">digest</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">digest_type</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiration</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fingerprint</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fingerprint_type</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">flags</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">flagsnaptr</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hardware</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">inception</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iterations</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keytag</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mailbox</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">match_type</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_server</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">next_hashed_owner_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nxdomain_ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">order</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">original_ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preference</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority_increment</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recordtype</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regexp</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replacement</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">salt</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signature</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signer</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">software</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subtype</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">targets</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">txt</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type_bitmaps</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type_covered</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type_mnemonic</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type_value</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usage</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.DnsRecord" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">DnsRecord</span></code> provides the resource for configuring a dns record to integrate easily with your existing DNS infrastructure to provide a secure, high performance, highly available and scalable solution for DNS hosting.</p>
<dl class="simple">
<dt>resource “akamai_dns_record” “origin” {</dt><dd><p>zone = “origin.org”
name = “origin.example.org”
recordtype =  “A”
active = true
ttl =  30
target = [“192.0.2.42”]</p>
</dd>
</dl>
<p>}</p>
<p>In addition to the fields listed in the prior section, type specific fields define the data makeup of each Record’s data. This section identfies required fields per type.</p>
<p>The following field is required:</p>
<ul class="simple">
<li><p>target - One or more IPv4 addresses, for example, 1.2.3.4.</p></li>
</ul>
<p>The following field is required:</p>
<ul class="simple">
<li><p>target - One or more IPv6 addresses, for example, 2001:0db8::ff00:0042:8329.</p></li>
</ul>
<p>The following fields are required:</p>
<ul class="simple">
<li><p>target - The domain name of the host having a server for the cell named by the owner name of the resource record.</p></li>
<li><p>subtype- An integer between 0 and 65535, indicating the type of service provided by the host.</p></li>
</ul>
<p>The following field is required:</p>
<ul class="simple">
<li><p>target - DNS name representing selected Edge Hostname name+domain.</p></li>
</ul>
<p>No additional fields are required. The following fields are Computed.</p>
<ul class="simple">
<li><p>dns_name - valid DNS name.</p></li>
<li><p>answer_type - answer type.</p></li>
</ul>
<p>The following field are required:</p>
<ul class="simple">
<li><p>target - One or more CA Authorizations. Each authorization contains three attributes: flags, property tag and property value.</p></li>
</ul>
<p>Example:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p>The following fields are required:</p>
<ul class="simple">
<li><p>type_value - numeric certificate type value</p></li>
<li><p>type_mnemonic - mnemonic certificate type value.</p></li>
<li><p>keytag - value computed for the key embedded in the certificate</p></li>
<li><p>algorithm - identifies the cryptographic algorithm used to create the signature.</p></li>
<li><p>certificate - certificate data</p></li>
</ul>
<p>Note: Type can be configured either a numeric OR menmonic value. If both set, type_mnemonic takes precedent.</p>
<p>The following field is required:</p>
<ul class="simple">
<li><p>target - A domain name that specifies the canonical or primary name for the owner. The owner name is an alias.</p></li>
</ul>
<p>The following fields are required:</p>
<ul class="simple">
<li><p>flags</p></li>
<li><p>protocol - Must have the value 3. The DNSKEY resource record must be treated as invalid during signature verification if it contains a value other than 3.</p></li>
<li><p>algorithm - The public key’s cryptographic algorithm and determine the format of the public key field.</p></li>
<li><p>key - Base 64 encoded value representing the public key, the format of which depends on the algorithm being used.</p></li>
</ul>
<p>The following fields are required:</p>
<ul class="simple">
<li><p>keytag - The key tag of the DNSKEY resource record referred to by the DS record, in network byte order.</p></li>
<li><p>algorithm - The algorithm number of the DNSKEY resource record referred to by the DS record.</p></li>
<li><p>digest_type - Identifies the algorithm used to construct the digest.</p></li>
<li><p>digest - The base 16 encoded DS record refers to a DNSKEY RR by including a digest of that DNSKEY RR. The digest is calculated by concatenating the canonical form of the fully qualified owner name of the DNSKEY RR with the DNSKEY RDATA, and then applying the digest algorithm.</p></li>
</ul>
<p>The following fields are required:</p>
<ul class="simple">
<li><p>hardware - Type of hardware the host uses. A machine name or CPU type may be up to 40 characters taken from the set of uppercase letters, digits, and the two punctuation characters hyphen and slash. It must start with a letter, and end with a letter.</p></li>
<li><p>software - Type of software the host uses. A system name may be up to 40 characters taken from the set of uppercase letters, digits, and the two punctuation characters hyphen and slash. It must start with a letter, and end with a letter or digit.</p></li>
</ul>
<p>The following field is required:</p>
<ul class="simple">
<li><p>target - A geographical location associated with a domain name.</p></li>
</ul>
<p>The following field is required:</p>
<ul class="simple">
<li><p>target - One or more domain names that specifies a host willing to act as a mail exchange for the owner name.</p></li>
</ul>
<p>The following fields are optional depending on configuration type. See DNS Getting Started Guide for more information.</p>
<ul class="simple">
<li><p>priority - The preference value given to the MX record among MX records. When a mailer needs to send mail to a certain DNS domain, it first contacts a DNS server for that domain and retrieves all the MX records. It then contacts the mailer with the lowest preference value. Ignored if embedded priority specified in target</p></li>
<li><p>priority_increment - auto priority increment when multiple targets are provided with no embedded priority.</p></li>
</ul>
<p>The following fields are required:</p>
<ul class="simple">
<li><p>order - A 16-bit unsigned integer specifying the order in which the NAPTR records MUST be processed to ensure the correct ordering ofrules. Low numbers are processed before high numbers, and once a NAPTR is found whose rule “matches” the target, the client MUST NOT consider any NAPTRs with a higher value for order (except as noted below for the Flags field).</p></li>
<li><p>preference - A 16-bit unsigned integer that specifies the order in which NAPTR records with equal order values should be processed, low numbers being processed before high numbers.</p></li>
<li><p>flagsnaptr - A <span class="raw-html-m2r"><character-string></span> containing flags to control aspects of the rewriting and interpretation of the fields in the record. Flags are single characters from the set [A-Z0-9]. The case of the alphabetic characters is not significant.</p></li>
<li><p>service - Specifies the services available down this rewrite path.</p></li>
<li><p>regexp - A String containing a substitution expression that is applied to the original string held by the client in order to construct the next domain name to lookup.</p></li>
<li><p>replacement - The next NAME to query for NAPTR, SRV, or address records depending on the value of the flags field. This MUST be a fully qualified domain-name.</p></li>
</ul>
<p>The following field is required:</p>
<ul class="simple">
<li><p>target - One or more domain names that specify authoritative hosts for the specified class and domain.</p></li>
</ul>
<p>The following fields are required:</p>
<ul class="simple">
<li><p>algorithm - The cryptographic hash algorithm used to construct the hash-value.</p></li>
<li><p>flags - The 8 one-bit flags that can be used to indicate different processing. All undefined flags must be zero.</p></li>
<li><p>iterations - The number of additional times the hash function has been performed.</p></li>
<li><p>salt - The base 16 encoded salt value, which is appended to the original owner name before hashing in order to defend against pre-calculated dictionary attacks.</p></li>
<li><p>next_hashed_owner_name - Base 32 encoded. The next hashed owner name in hash order. This value is in binary format. Given the ordered set of all hashed owner names, the Next Hashed Owner Name field contains the hash of an owner name that immediately follows the owner name of the given NSEC3 RR.</p></li>
<li><p>type_bitmaps - The resource record set types that exist at the original owner name of the NSEC3 RR.</p></li>
</ul>
<p>The following fields are required:</p>
<ul class="simple">
<li><p>algorithm - The cryptographic hash algorithm used to construct the hash-value.</p></li>
<li><p>flags - The 8 one-bit flags that can be used to indicate different processing. All undefined flags must be zero.</p></li>
<li><p>iterations - The number of additional times the hash function has been performed.</p></li>
<li><p>salt - The base 16 encoded salt value, which is appended to the original owner name before hashing in order to defend against pre-calculated dictionary attacks.</p></li>
</ul>
<p>The following field is required:</p>
<ul class="simple">
<li><p>target - A domain name that points to some location in the domain name space.</p></li>
</ul>
<p>The following fields are required:</p>
<ul class="simple">
<li><p>mailbox - A domain name that specifies the mailbox for the responsible person.</p></li>
<li><p>txt - A domain name for which TXT resource records exist.</p></li>
</ul>
<p>The following fields are required:</p>
<ul class="simple">
<li><p>type_covered - The resource record set type covered by this signature.</p></li>
<li><p>algorithm - The Algorithm Number field identifies the cryptographic algorithm used to create the signature.</p></li>
<li><p>original_ttl - The TTL of the covered record set as it appears in the authoritative zone.</p></li>
<li><p>expiration - The end point of this signature’s validity. The signature cannot be used for authentication past this point.</p></li>
<li><p>inception - The start point of this signature’s validity. The signature cannot be used for authentication prior to this point.</p></li>
<li><p>keytag - The Key Tag field contains the key tag value of the DNSKEY RR that validates this signature, in network byte order.</p></li>
<li><p>signer - The owner of the DSNKEY resource record who validates this signature.</p></li>
<li><p>signature - The base 64 encoded cryptographic signature that covers the RRSIG RDATA and covered record set. Format depends on the TSIG algorithm in use.</p></li>
<li><p>labels - The Labels field specifies the number of labels in the original RRSIG RR owner name. The significance of this field is that a validator uses it to determine whether the answer was synthesized from a wildcard. If so, it can be used to determine what owner name was used in generating the signature.</p></li>
</ul>
<p>The following field is required:</p>
<ul class="simple">
<li><p>target - Indicates which hosts are, and are not, authorized to use a domain name for the “HELO” and “MAIL FROM” identities.</p></li>
</ul>
<p>The following fields are required:</p>
<ul class="simple">
<li><p>target - The domain name of the target host.</p></li>
<li><p>priority - A 16-bit integer that specifies the preference given to this resource record among others at the same owner. Lower values are preferred.</p></li>
<li><p>weight - A server selection mechanism, specifying a relative weight for entries with the same priority. Larger weights should be given a proportionately higher probability of being selected. The range of this number is 0–65535, a 16-bit unsigned integer in network byte order. Domain administrators should use Weight 0 when there isn’t any server selection to do, to make the RR easier to read for humans. In the presence of records containing weights greater than 0, records with weight 0 should have a very small chance of being selected.</p></li>
<li><p>port - The port on this target of this service. The range of this number is 0–65535, a 16-bit unsigned integer in network byte order.</p></li>
</ul>
<p>The following fields are required:</p>
<ul class="simple">
<li><p>algorithm - Describes the algorithm of the public key. The following values are assigned: 0 = reserved; 1 = RSA; 2 = DSS, 3 = ECDSA</p></li>
<li><p>fingerprint_type - Describes the message-digest algorithm used to calculate the fingerprint of the public key. The following values are assigned: 0 = reserved, 1 = SHA-1, 2 = SHA-256</p></li>
<li><p>fingerprint - The base 16 encoded fingerprint as calculated over the public key blob. The message-digest algorithm is presumed to produce an opaque octet string output, which is placed as-is in the RDATA fingerprint field.</p></li>
</ul>
<p>The following fields are required:</p>
<ul class="simple">
<li><p>name_server - The domain name of the name server that was the original or primary source of data for this zone.</p></li>
<li><p>email_address - A domain name that specifies the mailbox of this person responsible for this zone.</p></li>
<li><p>serial - The unsigned version number between 0 and 214748364 of the original copy of the zone.</p></li>
<li><p>refresh - A time interval between 0 and 214748364 before the zone should be refreshed.</p></li>
<li><p>retry - A time interval between 0 and 214748364 that should elapse before a failed refresh should be retried.</p></li>
<li><p>expiry - A time value between 0 and 214748364 that specifies the upper limit on the time interval that can elapse before the zone is no longer authoritative.</p></li>
<li><p>nxdomain_ttl - The unsigned minimum TTL between 0 and 214748364 that should be exported with any resource record from this zone.</p></li>
</ul>
<p>The following fields are required:</p>
<ul class="simple">
<li><p>usage - specifies the provided association that will be used to match the certificate presented in the TLS handshake.</p></li>
<li><p>selector - specifies which part of the TLS certificate presented by the server will be matched against the association data.</p></li>
<li><p>match_type - specifies how the certificate association is presented.</p></li>
<li><p>certificate - specifies the “certificate association data” to be matched.</p></li>
</ul>
<p>The following field is required:</p>
<ul class="simple">
<li><p>target - One or more character strings. TXT RRs are used to hold descriptive text. The semantics of the text depends on the domain where it is found.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Maintained for backward compatibility</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the record. The name is an owner name, that is, the name of the node to which this resource record pertains.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The TTL is a 32-bit signed integer that specifies the time interval that the resource record may be cached before the source of the information should be consulted again. A value of zero means that the RR can only be used for the transaction in progress, and should not be cached. Zero values can also be used for extremely volatile data.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain zone, encapsulating any nested subdomains.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_akamai.DnsRecord.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">algorithm</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">answer_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">digest</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">digest_type</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiration</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expiry</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fingerprint</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fingerprint_type</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">flags</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">flagsnaptr</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hardware</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">inception</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iterations</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keytag</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mailbox</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">match_type</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_server</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">next_hashed_owner_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nxdomain_ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">order</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">original_ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">preference</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority_increment</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">record_sha</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recordtype</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">regexp</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replacement</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">salt</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selector</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">serial</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signature</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">signer</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">software</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subtype</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">targets</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">txt</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type_bitmaps</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type_covered</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type_mnemonic</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type_value</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usage</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.dns_record.DnsRecord<a class="headerlink" href="#pulumi_akamai.DnsRecord.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DnsRecord resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Maintained for backward compatibility</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the record. The name is an owner name, that is, the name of the node to which this resource record pertains.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The TTL is a 32-bit signed integer that specifies the time interval that the resource record may be cached before the source of the information should be consulted again. A value of zero means that the RR can only be used for the transaction in progress, and should not be cached. Zero values can also be used for extremely volatile data.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain zone, encapsulating any nested subdomains.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.DnsRecord.active">
<em class="property">property </em><code class="sig-name descname">active</code><a class="headerlink" href="#pulumi_akamai.DnsRecord.active" title="Permalink to this definition">¶</a></dt>
<dd><p>Maintained for backward compatibility</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.DnsRecord.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_akamai.DnsRecord.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the record. The name is an owner name, that is, the name of the node to which this resource record pertains.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.DnsRecord.ttl">
<em class="property">property </em><code class="sig-name descname">ttl</code><a class="headerlink" href="#pulumi_akamai.DnsRecord.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL is a 32-bit signed integer that specifies the time interval that the resource record may be cached before the source of the information should be consulted again. A value of zero means that the RR can only be used for the transaction in progress, and should not be cached. Zero values can also be used for extremely volatile data.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.DnsRecord.zone">
<em class="property">property </em><code class="sig-name descname">zone</code><a class="headerlink" href="#pulumi_akamai.DnsRecord.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain zone, encapsulating any nested subdomains.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.DnsRecord.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.DnsRecord.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.DnsRecord.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.DnsRecord.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.DnsZone">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">DnsZone</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_customer_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">masters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sign_and_serve</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sign_and_serve_algorithm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tsig_key</span><span class="p">:</span> <span class="n">Union[DnsZoneTsigKeyArgs, Mapping[str, Any], Awaitable[Union[DnsZoneTsigKeyArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.DnsZone" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">DnsZone</span></code> provides the resource for configuring a DNS zone to integrate easily with your existing DNS infrastructure to provide a secure, high performance, highly available and scalable solution for DNS hosting.</p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">demozone</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">DnsZone</span><span class="p">(</span><span class="s2">&quot;demozone&quot;</span><span class="p">,</span>
    <span class="n">comment</span><span class="o">=</span><span class="s2">&quot;some comment&quot;</span><span class="p">,</span>
    <span class="n">contract</span><span class="o">=</span><span class="s2">&quot;ctr_1-AB123&quot;</span><span class="p">,</span>
    <span class="n">group</span><span class="o">=</span><span class="s2">&quot;100&quot;</span><span class="p">,</span>
    <span class="n">masters</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;1.2.3.4&quot;</span><span class="p">,</span>
        <span class="s2">&quot;1.2.3.5&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">sign_and_serve</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;secondary&quot;</span><span class="p">,</span>
    <span class="n">zone</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive comment.</p></li>
<li><p><strong>contract</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contract ID.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The currently selected group ID.</p></li>
<li><p><strong>masters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The names or addresses of the customer’s nameservers from which the zone data should be retrieved.</p></li>
<li><p><strong>sign_and_serve</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether DNSSEC Sign&amp;Serve is enabled.</p></li>
<li><p><strong>sign_and_serve_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Algorithm used by Sign&amp;Serve.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the zone whose configuration this zone will copy.</p></li>
<li><p><strong>tsig_key</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DnsZoneTsigKeyArgs'</em><em>]</em><em>]</em>) – TSIG Key used in secure zone transfers</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the zone is <code class="docutils literal notranslate"><span class="pre">primary</span></code> or <code class="docutils literal notranslate"><span class="pre">secondary</span></code>.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain zone, encapsulating any nested subdomains.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_akamai.DnsZone.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">activation_state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alias_count</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_customer_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">masters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sign_and_serve</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sign_and_serve_algorithm</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tsig_key</span><span class="p">:</span> <span class="n">Union[DnsZoneTsigKeyArgs, Mapping[str, Any], Awaitable[Union[DnsZoneTsigKeyArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.dns_zone.DnsZone<a class="headerlink" href="#pulumi_akamai.DnsZone.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DnsZone resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive comment.</p></li>
<li><p><strong>contract</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contract ID.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The currently selected group ID.</p></li>
<li><p><strong>masters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The names or addresses of the customer’s nameservers from which the zone data should be retrieved.</p></li>
<li><p><strong>sign_and_serve</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether DNSSEC Sign&amp;Serve is enabled.</p></li>
<li><p><strong>sign_and_serve_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Algorithm used by Sign&amp;Serve.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the zone whose configuration this zone will copy.</p></li>
<li><p><strong>tsig_key</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DnsZoneTsigKeyArgs'</em><em>]</em><em>]</em>) – TSIG Key used in secure zone transfers</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the zone is <code class="docutils literal notranslate"><span class="pre">primary</span></code> or <code class="docutils literal notranslate"><span class="pre">secondary</span></code>.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain zone, encapsulating any nested subdomains.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.DnsZone.comment">
<em class="property">property </em><code class="sig-name descname">comment</code><a class="headerlink" href="#pulumi_akamai.DnsZone.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>A descriptive comment.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.DnsZone.contract">
<em class="property">property </em><code class="sig-name descname">contract</code><a class="headerlink" href="#pulumi_akamai.DnsZone.contract" title="Permalink to this definition">¶</a></dt>
<dd><p>The contract ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.DnsZone.group">
<em class="property">property </em><code class="sig-name descname">group</code><a class="headerlink" href="#pulumi_akamai.DnsZone.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The currently selected group ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.DnsZone.masters">
<em class="property">property </em><code class="sig-name descname">masters</code><a class="headerlink" href="#pulumi_akamai.DnsZone.masters" title="Permalink to this definition">¶</a></dt>
<dd><p>The names or addresses of the customer’s nameservers from which the zone data should be retrieved.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.DnsZone.sign_and_serve">
<em class="property">property </em><code class="sig-name descname">sign_and_serve</code><a class="headerlink" href="#pulumi_akamai.DnsZone.sign_and_serve" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether DNSSEC Sign&amp;Serve is enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.DnsZone.sign_and_serve_algorithm">
<em class="property">property </em><code class="sig-name descname">sign_and_serve_algorithm</code><a class="headerlink" href="#pulumi_akamai.DnsZone.sign_and_serve_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>Algorithm used by Sign&amp;Serve.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.DnsZone.target">
<em class="property">property </em><code class="sig-name descname">target</code><a class="headerlink" href="#pulumi_akamai.DnsZone.target" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the zone whose configuration this zone will copy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.DnsZone.tsig_key">
<em class="property">property </em><code class="sig-name descname">tsig_key</code><a class="headerlink" href="#pulumi_akamai.DnsZone.tsig_key" title="Permalink to this definition">¶</a></dt>
<dd><p>TSIG Key used in secure zone transfers</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.DnsZone.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_akamai.DnsZone.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the zone is <code class="docutils literal notranslate"><span class="pre">primary</span></code> or <code class="docutils literal notranslate"><span class="pre">secondary</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.DnsZone.zone">
<em class="property">property </em><code class="sig-name descname">zone</code><a class="headerlink" href="#pulumi_akamai.DnsZone.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain zone, encapsulating any nested subdomains.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.DnsZone.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.DnsZone.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.DnsZone.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.DnsZone.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.EdgeHostName">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">EdgeHostName</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edge_hostname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_behavior</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.EdgeHostName" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a EdgeHostName resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_akamai.EdgeHostName.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edge_hostname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_behavior</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.edge_host_name.EdgeHostName<a class="headerlink" href="#pulumi_akamai.EdgeHostName.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EdgeHostName resource’s state with the given name, id, and optional extra
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
<dt id="pulumi_akamai.EdgeHostName.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.EdgeHostName.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.EdgeHostName.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.EdgeHostName.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.GetAppSecConfigurationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetAppSecConfigurationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latest_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">production_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">staging_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetAppSecConfigurationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAppSecConfiguration.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetAppSecConfigurationResult.config_id">
<em class="property">property </em><code class="sig-name descname">config_id</code><a class="headerlink" href="#pulumi_akamai.GetAppSecConfigurationResult.config_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the specified security configuration. Returned only if <code class="docutils literal notranslate"><span class="pre">name</span></code> was specified.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecConfigurationResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetAppSecConfigurationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecConfigurationResult.latest_version">
<em class="property">property </em><code class="sig-name descname">latest_version</code><a class="headerlink" href="#pulumi_akamai.GetAppSecConfigurationResult.latest_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The last version of the specified security configuration created. Returned only if <code class="docutils literal notranslate"><span class="pre">name</span></code> was specified.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecConfigurationResult.output_text">
<em class="property">property </em><code class="sig-name descname">output_text</code><a class="headerlink" href="#pulumi_akamai.GetAppSecConfigurationResult.output_text" title="Permalink to this definition">¶</a></dt>
<dd><p>A tabular display showing the following information about all available security configurations: config_id, name, latest_version, version_active_in_staging, and version_active_in_production.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecConfigurationResult.production_version">
<em class="property">property </em><code class="sig-name descname">production_version</code><a class="headerlink" href="#pulumi_akamai.GetAppSecConfigurationResult.production_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the specified security configuration currently active in production. Returned only if <code class="docutils literal notranslate"><span class="pre">name</span></code> was specified.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecConfigurationResult.staging_version">
<em class="property">property </em><code class="sig-name descname">staging_version</code><a class="headerlink" href="#pulumi_akamai.GetAppSecConfigurationResult.staging_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the specified security configuration currently active in staging. Returned only if <code class="docutils literal notranslate"><span class="pre">name</span></code> was specified.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetAppSecConfigurationVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetAppSecConfigurationVersionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latest_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">production_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">staging_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetAppSecConfigurationVersionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAppSecConfigurationVersion.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetAppSecConfigurationVersionResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetAppSecConfigurationVersionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecConfigurationVersionResult.latest_version">
<em class="property">property </em><code class="sig-name descname">latest_version</code><a class="headerlink" href="#pulumi_akamai.GetAppSecConfigurationVersionResult.latest_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The last version of the security configuration created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecConfigurationVersionResult.output_text">
<em class="property">property </em><code class="sig-name descname">output_text</code><a class="headerlink" href="#pulumi_akamai.GetAppSecConfigurationVersionResult.output_text" title="Permalink to this definition">¶</a></dt>
<dd><p>A tabular display showing the following information about all versions of the security configuration: version number, staging status, and production status.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecConfigurationVersionResult.production_status">
<em class="property">property </em><code class="sig-name descname">production_status</code><a class="headerlink" href="#pulumi_akamai.GetAppSecConfigurationVersionResult.production_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the specified version in production: “Active”, “Inactive”, or “Deactivated”. Returned only if <code class="docutils literal notranslate"><span class="pre">version</span></code> was specified.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecConfigurationVersionResult.staging_status">
<em class="property">property </em><code class="sig-name descname">staging_status</code><a class="headerlink" href="#pulumi_akamai.GetAppSecConfigurationVersionResult.staging_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the specified version in staging: “Active”, “Inactive”, or “Deactivated”. Returned only if <code class="docutils literal notranslate"><span class="pre">version</span></code> was specified.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetAppSecCustomRuleActionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetAppSecCustomRuleActionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetAppSecCustomRuleActionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAppSecCustomRuleActions.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetAppSecCustomRuleActionsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetAppSecCustomRuleActionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecCustomRuleActionsResult.output_text">
<em class="property">property </em><code class="sig-name descname">output_text</code><a class="headerlink" href="#pulumi_akamai.GetAppSecCustomRuleActionsResult.output_text" title="Permalink to this definition">¶</a></dt>
<dd><p>A tabular display showing the ID, name, and action of all custom rules associated with the specified security configuration, version and security policy.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetAppSecCustomRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetAppSecCustomRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_text</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetAppSecCustomRulesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAppSecCustomRules.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetAppSecCustomRulesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetAppSecCustomRulesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecCustomRulesResult.output_text">
<em class="property">property </em><code class="sig-name descname">output_text</code><a class="headerlink" href="#pulumi_akamai.GetAppSecCustomRulesResult.output_text" title="Permalink to this definition">¶</a></dt>
<dd><p>A tabular display showing the ID and name of the custom rules defined for the security configuration.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetAppSecExportConfigurationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetAppSecExportConfigurationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">searches</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetAppSecExportConfigurationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAppSecExportConfiguration.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetAppSecExportConfigurationResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetAppSecExportConfigurationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecExportConfigurationResult.json">
<em class="property">property </em><code class="sig-name descname">json</code><a class="headerlink" href="#pulumi_akamai.GetAppSecExportConfigurationResult.json" title="Permalink to this definition">¶</a></dt>
<dd><p>The complete set of information about the specified security configuration version, in JSON format. This includes the types available for the <code class="docutils literal notranslate"><span class="pre">search</span></code> parameter, plus several additional fields such as createDate and createdBy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecExportConfigurationResult.output_text">
<em class="property">property </em><code class="sig-name descname">output_text</code><a class="headerlink" href="#pulumi_akamai.GetAppSecExportConfigurationResult.output_text" title="Permalink to this definition">¶</a></dt>
<dd><p>A tabular display showing the types of data specified in the <code class="docutils literal notranslate"><span class="pre">search</span></code> parameter. Included only if the <code class="docutils literal notranslate"><span class="pre">search</span></code> parameter specifies at least one type.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetAppSecMatchTargetsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetAppSecMatchTargetsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetAppSecMatchTargetsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAppSecMatchTargets.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetAppSecMatchTargetsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetAppSecMatchTargetsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecMatchTargetsResult.output_text">
<em class="property">property </em><code class="sig-name descname">output_text</code><a class="headerlink" href="#pulumi_akamai.GetAppSecMatchTargetsResult.output_text" title="Permalink to this definition">¶</a></dt>
<dd><p>A tabular display showing the ID and Policy ID of all match targets associated with the specified security configuration and version.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetAppSecSecurityPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetAppSecSecurityPolicyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_lists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetAppSecSecurityPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAppSecSecurityPolicy.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetAppSecSecurityPolicyResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetAppSecSecurityPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecSecurityPolicyResult.output_text">
<em class="property">property </em><code class="sig-name descname">output_text</code><a class="headerlink" href="#pulumi_akamai.GetAppSecSecurityPolicyResult.output_text" title="Permalink to this definition">¶</a></dt>
<dd><p>A tabular display showing the ID and name of all security policies.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecSecurityPolicyResult.policy_id">
<em class="property">property </em><code class="sig-name descname">policy_id</code><a class="headerlink" href="#pulumi_akamai.GetAppSecSecurityPolicyResult.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security policy. Included only if <code class="docutils literal notranslate"><span class="pre">name</span></code> was specified.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecSecurityPolicyResult.policy_lists">
<em class="property">property </em><code class="sig-name descname">policy_lists</code><a class="headerlink" href="#pulumi_akamai.GetAppSecSecurityPolicyResult.policy_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the IDs of all security policies.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetAppSecSelectableHostnamesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetAppSecSelectableHostnamesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">active_in_production</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active_in_staging</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostnames</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostnames_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetAppSecSelectableHostnamesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAppSecSelectableHostnames.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetAppSecSelectableHostnamesResult.hostnames">
<em class="property">property </em><code class="sig-name descname">hostnames</code><a class="headerlink" href="#pulumi_akamai.GetAppSecSelectableHostnamesResult.hostnames" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of selectable hostnames.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecSelectableHostnamesResult.hostnames_json">
<em class="property">property </em><code class="sig-name descname">hostnames_json</code><a class="headerlink" href="#pulumi_akamai.GetAppSecSelectableHostnamesResult.hostnames_json" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of selectable hostnames in json format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecSelectableHostnamesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetAppSecSelectableHostnamesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecSelectableHostnamesResult.output_text">
<em class="property">property </em><code class="sig-name descname">output_text</code><a class="headerlink" href="#pulumi_akamai.GetAppSecSelectableHostnamesResult.output_text" title="Permalink to this definition">¶</a></dt>
<dd><p>A tabular display of the selectable hostnames showing the name and config_id of the security configuration under which the host is protected in production, or ‘-‘ if the host is not protected in production.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetAppSecSelectedHostnamesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetAppSecSelectedHostnamesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostnames</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostnames_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_text</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetAppSecSelectedHostnamesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAppSecSelectedHostnames.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetAppSecSelectedHostnamesResult.hostnames">
<em class="property">property </em><code class="sig-name descname">hostnames</code><a class="headerlink" href="#pulumi_akamai.GetAppSecSelectedHostnamesResult.hostnames" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of selected hostnames.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecSelectedHostnamesResult.hostnames_json">
<em class="property">property </em><code class="sig-name descname">hostnames_json</code><a class="headerlink" href="#pulumi_akamai.GetAppSecSelectedHostnamesResult.hostnames_json" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of selected hostnames in JSON format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecSelectedHostnamesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetAppSecSelectedHostnamesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetAppSecSelectedHostnamesResult.output_text">
<em class="property">property </em><code class="sig-name descname">output_text</code><a class="headerlink" href="#pulumi_akamai.GetAppSecSelectedHostnamesResult.output_text" title="Permalink to this definition">¶</a></dt>
<dd><p>A tabular display of the selected hostnames.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetAuthoritiesSetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetAuthoritiesSetResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">authorities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetAuthoritiesSetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAuthoritiesSet.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetAuthoritiesSetResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetAuthoritiesSetResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetContractResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetContractResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetContractResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getContract.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetContractResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetContractResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetContractsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetContractsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">contracts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetContractsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getContracts.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetContractsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetContractsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetCpCodeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetCpCodeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">contract</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetCpCodeResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCpCode.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetCpCodeResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetCpCodeResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetDnsRecordSetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetDnsRecordSetResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rdatas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">record_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetDnsRecordSetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDnsRecordSet.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetDnsRecordSetResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetDnsRecordSetResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">contract</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetGroupResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroups.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetGroupsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetGtmDefaultDatacenterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetGtmDefaultDatacenterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nickname</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetGtmDefaultDatacenterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGtmDefaultDatacenter.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetGtmDefaultDatacenterResult.datacenter_id">
<em class="property">property </em><code class="sig-name descname">datacenter_id</code><a class="headerlink" href="#pulumi_akamai.GetGtmDefaultDatacenterResult.datacenter_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The default datacenter ID</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetGtmDefaultDatacenterResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetGtmDefaultDatacenterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GetGtmDefaultDatacenterResult.nickname">
<em class="property">property </em><code class="sig-name descname">nickname</code><a class="headerlink" href="#pulumi_akamai.GetGtmDefaultDatacenterResult.nickname" title="Permalink to this definition">¶</a></dt>
<dd><p>The default datacenter nickname</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetPropertiesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetPropertiesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">contract_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">properties</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetPropertiesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProperties.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetPropertiesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetPropertiesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetPropertyProductsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetPropertyProductsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">contract_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">products</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetPropertyProductsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPropertyProducts.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetPropertyProductsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetPropertyProductsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetPropertyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetPropertyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetPropertyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProperty.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetPropertyResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetPropertyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetPropertyRuleFormatsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetPropertyRuleFormatsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_formats</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetPropertyRuleFormatsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPropertyRuleFormats.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetPropertyRuleFormatsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetPropertyRuleFormatsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetPropertyRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetPropertyRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">contract_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">errors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">property_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetPropertyRulesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPropertyRules.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetPropertyRulesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetPropertyRulesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GetPropertyRulesTemplateResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GetPropertyRulesTemplateResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">var_definition_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">var_values_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GetPropertyRulesTemplateResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPropertyRulesTemplate.</p>
<dl class="py method">
<dt id="pulumi_akamai.GetPropertyRulesTemplateResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_akamai.GetPropertyRulesTemplateResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_akamai.GtmAsmap">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GtmAsmap</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assignments</span><span class="p">:</span> <span class="n">Union[Sequence[Union[GtmAsmapAssignmentArgs, Mapping[str, Any], Awaitable[Union[GtmAsmapAssignmentArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[GtmAsmapAssignmentArgs, Mapping[str, Any], Awaitable[Union[GtmAsmapAssignmentArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_datacenter</span><span class="p">:</span> <span class="n">Union[GtmAsmapDefaultDatacenterArgs, Mapping[str, Any], Awaitable[Union[GtmAsmapDefaultDatacenterArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_on_complete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmAsmap" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">GtmAsmap</span></code> provides the resource for creating, configuring and importing a gtm AS Map to integrate easily with your existing GTM infrastructure to provide a secure, high performance, highly available and scalable solution for Global Traffic Management. Note: Import requires an ID of the format: <cite>existing_domain_name</cite>:<cite>existing_map_name</cite></p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">demo_asmap</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">GtmAsmap</span><span class="p">(</span><span class="s2">&quot;demoAsmap&quot;</span><span class="p">,</span>
    <span class="n">default_datacenter</span><span class="o">=</span><span class="n">akamai</span><span class="o">.</span><span class="n">GtmAsmapDefaultDatacenterArgs</span><span class="p">(</span>
        <span class="n">datacenter_id</span><span class="o">=</span><span class="mi">5400</span><span class="p">,</span>
        <span class="n">nickname</span><span class="o">=</span><span class="s2">&quot;All Other AS numbers&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;demo_domain.akadns.net&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>assignments</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GtmAsmapAssignmentArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter_id</span></code></p></li>
</ul>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `nickname`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource name</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `default_datacenter`
* `datacenter_id`
* `nickname`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>wait_on_complete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wait for transaction to complete</p>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_akamai.GtmAsmap.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assignments</span><span class="p">:</span> <span class="n">Union[Sequence[Union[GtmAsmapAssignmentArgs, Mapping[str, Any], Awaitable[Union[GtmAsmapAssignmentArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[GtmAsmapAssignmentArgs, Mapping[str, Any], Awaitable[Union[GtmAsmapAssignmentArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_datacenter</span><span class="p">:</span> <span class="n">Union[GtmAsmapDefaultDatacenterArgs, Mapping[str, Any], Awaitable[Union[GtmAsmapDefaultDatacenterArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_on_complete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.gtm_asmap.GtmAsmap<a class="headerlink" href="#pulumi_akamai.GtmAsmap.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GtmAsmap resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>assignments</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GtmAsmapAssignmentArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter_id</span></code></p></li>
</ul>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `nickname`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource name</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `default_datacenter`
* `datacenter_id`
* `nickname`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>wait_on_complete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wait for transaction to complete</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmAsmap.assignments">
<em class="property">property </em><code class="sig-name descname">assignments</code><a class="headerlink" href="#pulumi_akamai.GtmAsmap.assignments" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter_id</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nickname</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmAsmap.domain">
<em class="property">property </em><code class="sig-name descname">domain</code><a class="headerlink" href="#pulumi_akamai.GtmAsmap.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmAsmap.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_akamai.GtmAsmap.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource name</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_datacenter</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter_id</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nickname</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmAsmap.wait_on_complete">
<em class="property">property </em><code class="sig-name descname">wait_on_complete</code><a class="headerlink" href="#pulumi_akamai.GtmAsmap.wait_on_complete" title="Permalink to this definition">¶</a></dt>
<dd><p>Wait for transaction to complete</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmAsmap.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmAsmap.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.GtmAsmap.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmAsmap.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.GtmCidrmap">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GtmCidrmap</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assignments</span><span class="p">:</span> <span class="n">Union[Sequence[Union[GtmCidrmapAssignmentArgs, Mapping[str, Any], Awaitable[Union[GtmCidrmapAssignmentArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[GtmCidrmapAssignmentArgs, Mapping[str, Any], Awaitable[Union[GtmCidrmapAssignmentArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_datacenter</span><span class="p">:</span> <span class="n">Union[GtmCidrmapDefaultDatacenterArgs, Mapping[str, Any], Awaitable[Union[GtmCidrmapDefaultDatacenterArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_on_complete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmCidrmap" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">GtmCidrmap</span></code> provides the resource for creating, configuring and importing a gtm Cidr Map to integrate easily with your existing GTM infrastructure to provide a secure, high performance, highly available and scalable solution for Global Traffic Management. Note: Import requires an ID of the format: <cite>existing_domain_name</cite>:<cite>existing_map_name</cite></p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">demo_cidrmap</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">GtmCidrmap</span><span class="p">(</span><span class="s2">&quot;demoCidrmap&quot;</span><span class="p">,</span>
    <span class="n">default_datacenter</span><span class="o">=</span><span class="n">akamai</span><span class="o">.</span><span class="n">GtmCidrmapDefaultDatacenterArgs</span><span class="p">(</span>
        <span class="n">datacenter_id</span><span class="o">=</span><span class="mi">5400</span><span class="p">,</span>
        <span class="n">nickname</span><span class="o">=</span><span class="s2">&quot;All Other CIDR Blocks&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;demo_domain.akadns.net&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>assignments</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GtmCidrmapAssignmentArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter_id</span></code></p></li>
</ul>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `nickname`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource name</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `default_datacenter`
* `datacenter_id`
* `nickname`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>wait_on_complete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wait for transaction to complete</p>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_akamai.GtmCidrmap.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assignments</span><span class="p">:</span> <span class="n">Union[Sequence[Union[GtmCidrmapAssignmentArgs, Mapping[str, Any], Awaitable[Union[GtmCidrmapAssignmentArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[GtmCidrmapAssignmentArgs, Mapping[str, Any], Awaitable[Union[GtmCidrmapAssignmentArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_datacenter</span><span class="p">:</span> <span class="n">Union[GtmCidrmapDefaultDatacenterArgs, Mapping[str, Any], Awaitable[Union[GtmCidrmapDefaultDatacenterArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_on_complete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.gtm_cidrmap.GtmCidrmap<a class="headerlink" href="#pulumi_akamai.GtmCidrmap.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GtmCidrmap resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>assignments</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GtmCidrmapAssignmentArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter_id</span></code></p></li>
</ul>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `nickname`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource name</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `default_datacenter`
* `datacenter_id`
* `nickname`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>wait_on_complete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wait for transaction to complete</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmCidrmap.assignments">
<em class="property">property </em><code class="sig-name descname">assignments</code><a class="headerlink" href="#pulumi_akamai.GtmCidrmap.assignments" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter_id</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nickname</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmCidrmap.domain">
<em class="property">property </em><code class="sig-name descname">domain</code><a class="headerlink" href="#pulumi_akamai.GtmCidrmap.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmCidrmap.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_akamai.GtmCidrmap.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource name</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_datacenter</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter_id</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nickname</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmCidrmap.wait_on_complete">
<em class="property">property </em><code class="sig-name descname">wait_on_complete</code><a class="headerlink" href="#pulumi_akamai.GtmCidrmap.wait_on_complete" title="Permalink to this definition">¶</a></dt>
<dd><p>Wait for transaction to complete</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmCidrmap.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmCidrmap.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.GtmCidrmap.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmCidrmap.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.GtmDatacenter">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GtmDatacenter</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">city</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clone_of</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_server_host_header_override</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_server_targeting</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">continent</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_load_object</span><span class="p">:</span> <span class="n">Union[GtmDatacenterDefaultLoadObjectArgs, Mapping[str, Any], Awaitable[Union[GtmDatacenterDefaultLoadObjectArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latitude</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">longitude</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nickname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state_or_province</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_on_complete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmDatacenter" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">GtmDatacenter</span></code> provides the resource for creating, configuring and importing a gtm datacenter to integrate easily with your existing GTM infrastructure to provide a secure, high performance, highly available and scalable solution for Global Traffic Management. Note: Import requires an ID of the format: <cite>existing_domain_name</cite>:<cite>existing_datacenter_id</cite></p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">demo_datacenter</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">GtmDatacenter</span><span class="p">(</span><span class="s2">&quot;demoDatacenter&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;demo_domain.akadns.net&quot;</span><span class="p">,</span>
    <span class="n">nickname</span><span class="o">=</span><span class="s2">&quot;demo_datacenter&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_server_host_header_override</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">continent</span></code></p></li>
</ul>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `country`
* `latitude`
* `longitude`
* `state_or_province`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name</p></li>
<li><p><strong>nickname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – datacenter nickname</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `default_load_object`
* `load_object`
* `load_object_port`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>wait_on_complete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wait for transaction to complete</p>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_akamai.GtmDatacenter.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">city</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">clone_of</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_server_host_header_override</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_server_targeting</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">continent</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">country</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">datacenter_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_load_object</span><span class="p">:</span> <span class="n">Union[GtmDatacenterDefaultLoadObjectArgs, Mapping[str, Any], Awaitable[Union[GtmDatacenterDefaultLoadObjectArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latitude</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">longitude</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nickname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ping_interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ping_packet_size</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">score_penalty</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">servermonitor_liveness_count</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">servermonitor_load_count</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">servermonitor_pool</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state_or_province</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtual</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_on_complete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.gtm_datacenter.GtmDatacenter<a class="headerlink" href="#pulumi_akamai.GtmDatacenter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GtmDatacenter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_server_host_header_override</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">continent</span></code></p></li>
</ul>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `country`
* `latitude`
* `longitude`
* `state_or_province`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name</p></li>
<li><p><strong>nickname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – datacenter nickname</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `default_load_object`
* `load_object`
* `load_object_port`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>wait_on_complete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wait for transaction to complete</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmDatacenter.cloud_server_host_header_override">
<em class="property">property </em><code class="sig-name descname">cloud_server_host_header_override</code><a class="headerlink" href="#pulumi_akamai.GtmDatacenter.cloud_server_host_header_override" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">continent</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">country</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">latitude</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">longitude</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">state_or_province</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmDatacenter.domain">
<em class="property">property </em><code class="sig-name descname">domain</code><a class="headerlink" href="#pulumi_akamai.GtmDatacenter.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmDatacenter.nickname">
<em class="property">property </em><code class="sig-name descname">nickname</code><a class="headerlink" href="#pulumi_akamai.GtmDatacenter.nickname" title="Permalink to this definition">¶</a></dt>
<dd><p>datacenter nickname</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_load_object</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">load_object</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">load_object_port</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmDatacenter.wait_on_complete">
<em class="property">property </em><code class="sig-name descname">wait_on_complete</code><a class="headerlink" href="#pulumi_akamai.GtmDatacenter.wait_on_complete" title="Permalink to this definition">¶</a></dt>
<dd><p>Wait for transaction to complete</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmDatacenter.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmDatacenter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.GtmDatacenter.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmDatacenter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.GtmDomain">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GtmDomain</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cname_coalescing_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_error_penalty</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_ssl_client_certificate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_ssl_client_private_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_timeout_penalty</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_notification_lists</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_user_mapping_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_feedback</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_imbalance_percentage</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_on_complete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmDomain" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">GtmDomain</span></code> provides the resource for creating, configuring and importing a gtm domain to integrate easily with your existing GTM infrastructure to provide a secure, high performance, highly available and scalable solution for Global Traffic Management. Note: Import requires an ID of the format: <code class="docutils literal notranslate"><span class="pre">existing_domain_name</span></code></p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">demodomain</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">GtmDomain</span><span class="p">(</span><span class="s2">&quot;demodomain&quot;</span><span class="p">,</span>
    <span class="n">comment</span><span class="o">=</span><span class="s2">&quot;some comment&quot;</span><span class="p">,</span>
    <span class="n">contract</span><span class="o">=</span><span class="s2">&quot;XXX&quot;</span><span class="p">,</span>
    <span class="n">group</span><span class="o">=</span><span class="s2">&quot;100&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;basic&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive comment</p></li>
<li><p><strong>contract</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contract ID (if creating domain)</p></li>
<li><p><strong>default_timeout_penalty</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">load_imbalance_percentage</span></code></p></li>
</ul>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `default_ssl_client_private_key`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The currently selected group ID (if creating domain)</p></li>
<li><p><strong>load_feedback</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">default_ssl_client_certificate</span></code></p></li>
</ul>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain type</p></li>
<li><p><strong>wait_on_complete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wait for transaction to complete</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_akamai.GtmDomain.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cname_coalescing_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_error_penalty</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_health_max</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_health_multiplier</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_health_threshold</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_max_unreachable_penalty</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_ssl_client_certificate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_ssl_client_private_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_timeout_penalty</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_unreachable_threshold</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_notification_lists</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_user_mapping_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_feedback</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_imbalance_percentage</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">map_update_interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_properties</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_resources</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_test_timeout</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_pingable_region_fraction</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_test_interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ping_interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ping_packet_size</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">round_robin_prefix</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">servermonitor_liveness_count</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">servermonitor_load_count</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">servermonitor_pool</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_on_complete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.gtm_domain.GtmDomain<a class="headerlink" href="#pulumi_akamai.GtmDomain.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GtmDomain resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive comment</p></li>
<li><p><strong>contract</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contract ID (if creating domain)</p></li>
<li><p><strong>default_timeout_penalty</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">load_imbalance_percentage</span></code></p></li>
</ul>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `default_ssl_client_private_key`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>default_unreachable_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">min_pingable_region_fraction</span></code></p></li>
</ul>
</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `servermonitor_liveness_count`
* `round_robin_prefix`
* `servermonitor_load_count`
* `ping_interval`
* `max_ttl`
* `default_health_max`
* `map_update_interval`
* `max_properties`
* `max_resources`
* `default_error_penalty`
* `max_test_timeout`
* `default_health_multiplier`
* `servermonitor_pool`
* `min_ttl`
* `default_max_unreachable_penalty`
* `default_health_threshold`
* `min_test_interval`
* `ping_packet_size`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The currently selected group ID (if creating domain)</p></li>
<li><p><strong>load_feedback</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">default_ssl_client_certificate</span></code></p></li>
</ul>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain type</p></li>
<li><p><strong>wait_on_complete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wait for transaction to complete</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmDomain.comment">
<em class="property">property </em><code class="sig-name descname">comment</code><a class="headerlink" href="#pulumi_akamai.GtmDomain.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>A descriptive comment</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmDomain.contract">
<em class="property">property </em><code class="sig-name descname">contract</code><a class="headerlink" href="#pulumi_akamai.GtmDomain.contract" title="Permalink to this definition">¶</a></dt>
<dd><p>The contract ID (if creating domain)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmDomain.default_timeout_penalty">
<em class="property">property </em><code class="sig-name descname">default_timeout_penalty</code><a class="headerlink" href="#pulumi_akamai.GtmDomain.default_timeout_penalty" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">load_imbalance_percentage</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_ssl_client_private_key</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmDomain.default_unreachable_threshold">
<em class="property">property </em><code class="sig-name descname">default_unreachable_threshold</code><a class="headerlink" href="#pulumi_akamai.GtmDomain.default_unreachable_threshold" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">min_pingable_region_fraction</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servermonitor_liveness_count</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">round_robin_prefix</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servermonitor_load_count</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ping_interval</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_ttl</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_health_max</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">map_update_interval</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_properties</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_resources</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_error_penalty</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_test_timeout</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_health_multiplier</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">servermonitor_pool</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_ttl</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_max_unreachable_penalty</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">default_health_threshold</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_test_interval</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ping_packet_size</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmDomain.group">
<em class="property">property </em><code class="sig-name descname">group</code><a class="headerlink" href="#pulumi_akamai.GtmDomain.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The currently selected group ID (if creating domain)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmDomain.load_feedback">
<em class="property">property </em><code class="sig-name descname">load_feedback</code><a class="headerlink" href="#pulumi_akamai.GtmDomain.load_feedback" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_ssl_client_certificate</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmDomain.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_akamai.GtmDomain.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmDomain.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_akamai.GtmDomain.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain type</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmDomain.wait_on_complete">
<em class="property">property </em><code class="sig-name descname">wait_on_complete</code><a class="headerlink" href="#pulumi_akamai.GtmDomain.wait_on_complete" title="Permalink to this definition">¶</a></dt>
<dd><p>Wait for transaction to complete</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmDomain.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmDomain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.GtmDomain.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmDomain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.GtmGeomap">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GtmGeomap</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assignments</span><span class="p">:</span> <span class="n">Union[Sequence[Union[GtmGeomapAssignmentArgs, Mapping[str, Any], Awaitable[Union[GtmGeomapAssignmentArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[GtmGeomapAssignmentArgs, Mapping[str, Any], Awaitable[Union[GtmGeomapAssignmentArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_datacenter</span><span class="p">:</span> <span class="n">Union[GtmGeomapDefaultDatacenterArgs, Mapping[str, Any], Awaitable[Union[GtmGeomapDefaultDatacenterArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_on_complete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmGeomap" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">GtmGeomap</span></code> provides the resource for creating, configuring and importing a gtm Geographic map to integrate easily with your existing GTM infrastructure to provide a secure, high performance, highly available and scalable solution for Global Traffic Management. Note: Import requires an ID of the format: <cite>existing_domain_name</cite>:<cite>existing_map_name</cite></p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">demo_geomap</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">GtmGeomap</span><span class="p">(</span><span class="s2">&quot;demoGeomap&quot;</span><span class="p">,</span>
    <span class="n">default_datacenter</span><span class="o">=</span><span class="n">akamai</span><span class="o">.</span><span class="n">GtmGeomapDefaultDatacenterArgs</span><span class="p">(</span>
        <span class="n">datacenter_id</span><span class="o">=</span><span class="mi">5400</span><span class="p">,</span>
        <span class="n">nickname</span><span class="o">=</span><span class="s2">&quot;All Others&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;demo_domain.akadns.net&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>assignments</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GtmGeomapAssignmentArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter_id</span></code></p></li>
</ul>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `nickname`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource name</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `default_datacenter`
* `datacenter_id`
* `nickname`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>wait_on_complete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wait for transaction to complete</p>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_akamai.GtmGeomap.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assignments</span><span class="p">:</span> <span class="n">Union[Sequence[Union[GtmGeomapAssignmentArgs, Mapping[str, Any], Awaitable[Union[GtmGeomapAssignmentArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[GtmGeomapAssignmentArgs, Mapping[str, Any], Awaitable[Union[GtmGeomapAssignmentArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_datacenter</span><span class="p">:</span> <span class="n">Union[GtmGeomapDefaultDatacenterArgs, Mapping[str, Any], Awaitable[Union[GtmGeomapDefaultDatacenterArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_on_complete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.gtm_geomap.GtmGeomap<a class="headerlink" href="#pulumi_akamai.GtmGeomap.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GtmGeomap resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>assignments</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GtmGeomapAssignmentArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter_id</span></code></p></li>
</ul>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `nickname`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource name</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `default_datacenter`
* `datacenter_id`
* `nickname`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>wait_on_complete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wait for transaction to complete</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmGeomap.assignments">
<em class="property">property </em><code class="sig-name descname">assignments</code><a class="headerlink" href="#pulumi_akamai.GtmGeomap.assignments" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter_id</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nickname</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmGeomap.domain">
<em class="property">property </em><code class="sig-name descname">domain</code><a class="headerlink" href="#pulumi_akamai.GtmGeomap.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmGeomap.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_akamai.GtmGeomap.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource name</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_datacenter</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter_id</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nickname</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmGeomap.wait_on_complete">
<em class="property">property </em><code class="sig-name descname">wait_on_complete</code><a class="headerlink" href="#pulumi_akamai.GtmGeomap.wait_on_complete" title="Permalink to this definition">¶</a></dt>
<dd><p>Wait for transaction to complete</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmGeomap.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmGeomap.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.GtmGeomap.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmGeomap.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.GtmProperty">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GtmProperty</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_cname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_ip</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">balance_by_download_score</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comments</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dynamic_ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">failback_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">failover_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ghost_demand_reporting</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">handout_limit</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">handout_mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_max</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_multiplier</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_threshold</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">liveness_tests</span><span class="p">:</span> <span class="n">Union[Sequence[Union[GtmPropertyLivenessTestArgs, Mapping[str, Any], Awaitable[Union[GtmPropertyLivenessTestArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[GtmPropertyLivenessTestArgs, Mapping[str, Any], Awaitable[Union[GtmPropertyLivenessTestArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_imbalance_percentage</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">map_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_unreachable_penalty</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_live_fraction</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">score_aggregation_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">static_rr_sets</span><span class="p">:</span> <span class="n">Union[Sequence[Union[GtmPropertyStaticRrSetArgs, Mapping[str, Any], Awaitable[Union[GtmPropertyStaticRrSetArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[GtmPropertyStaticRrSetArgs, Mapping[str, Any], Awaitable[Union[GtmPropertyStaticRrSetArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">static_ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stickiness_bonus_constant</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stickiness_bonus_percentage</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">traffic_targets</span><span class="p">:</span> <span class="n">Union[Sequence[Union[GtmPropertyTrafficTargetArgs, Mapping[str, Any], Awaitable[Union[GtmPropertyTrafficTargetArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[GtmPropertyTrafficTargetArgs, Mapping[str, Any], Awaitable[Union[GtmPropertyTrafficTargetArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unreachable_threshold</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_computed_targets</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_on_complete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmProperty" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">GtmProperty</span></code> provides the resource for creating, configuring and importing a gtm property to integrate easily with your existing GTM infrastructure to provide a secure, high performance, highly available and scalable solution for Global Traffic Management. Note: Import requires an ID of the format: <cite>existing_domain_name</cite>:<cite>existing_property_name</cite></p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">demo_property</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">GtmProperty</span><span class="p">(</span><span class="s2">&quot;demoProperty&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;demo_domain.akadns.net&quot;</span><span class="p">,</span>
    <span class="n">handout_limit</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">handout_mode</span><span class="o">=</span><span class="s2">&quot;normal&quot;</span><span class="p">,</span>
    <span class="n">score_aggregation_type</span><span class="o">=</span><span class="s2">&quot;median&quot;</span><span class="p">,</span>
    <span class="n">traffic_targets</span><span class="o">=</span><span class="p">[</span><span class="n">akamai</span><span class="o">.</span><span class="n">GtmPropertyTrafficTargetArgs</span><span class="p">(</span>
        <span class="n">datacenter_id</span><span class="o">=</span><span class="mi">3131</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;weighted-round-robin&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>balance_by_download_score</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">static_ttl</span></code></p></li>
</ul>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `unreachable_threshold`
* `health_multiplier`
* `dynamic_ttl`
* `max_unreachable_penalty`
* `map_name`
* `load_imbalance_percentage`
* `health_max`
* `cname`
* `comments`
* `ghost_demand_reporting`
* `min_live_fraction`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name</p></li>
<li><p><strong>ipv6</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">stickiness_bonus_percentage</span></code></p></li>
</ul>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `stickiness_bonus_constant`
* `health_threshold`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Liveness test name</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `test_interval`
* `test_object_protocol`
* `test_timeout`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>static_rr_sets</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GtmPropertyStaticRrSetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code></p></li>
</ul>
</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `ttl`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>traffic_targets</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GtmPropertyTrafficTargetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter_id</span></code></p></li>
</ul>
</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Property type</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `score_aggregation_type`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>use_computed_targets</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">backup_ip</span></code></p></li>
</ul>
</p></li>
<li><p><strong>wait_on_complete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wait for transaction to complete</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `failover_delay`
* `failback_delay`
</pre></div>
</div>
<dl class="py method">
<dt id="pulumi_akamai.GtmProperty.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_cname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_ip</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">balance_by_download_score</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comments</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dynamic_ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">failback_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">failover_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ghost_demand_reporting</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">handout_limit</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">handout_mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_max</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_multiplier</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">health_threshold</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">liveness_tests</span><span class="p">:</span> <span class="n">Union[Sequence[Union[GtmPropertyLivenessTestArgs, Mapping[str, Any], Awaitable[Union[GtmPropertyLivenessTestArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[GtmPropertyLivenessTestArgs, Mapping[str, Any], Awaitable[Union[GtmPropertyLivenessTestArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_imbalance_percentage</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">map_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_unreachable_penalty</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_live_fraction</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">score_aggregation_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">static_rr_sets</span><span class="p">:</span> <span class="n">Union[Sequence[Union[GtmPropertyStaticRrSetArgs, Mapping[str, Any], Awaitable[Union[GtmPropertyStaticRrSetArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[GtmPropertyStaticRrSetArgs, Mapping[str, Any], Awaitable[Union[GtmPropertyStaticRrSetArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">static_ttl</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stickiness_bonus_constant</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stickiness_bonus_percentage</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">traffic_targets</span><span class="p">:</span> <span class="n">Union[Sequence[Union[GtmPropertyTrafficTargetArgs, Mapping[str, Any], Awaitable[Union[GtmPropertyTrafficTargetArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[GtmPropertyTrafficTargetArgs, Mapping[str, Any], Awaitable[Union[GtmPropertyTrafficTargetArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unreachable_threshold</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_computed_targets</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_on_complete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weighted_hash_bits_for_ipv4</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weighted_hash_bits_for_ipv6</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.gtm_property.GtmProperty<a class="headerlink" href="#pulumi_akamai.GtmProperty.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GtmProperty resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>balance_by_download_score</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">static_ttl</span></code></p></li>
</ul>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `unreachable_threshold`
* `health_multiplier`
* `dynamic_ttl`
* `max_unreachable_penalty`
* `map_name`
* `load_imbalance_percentage`
* `health_max`
* `cname`
* `comments`
* `ghost_demand_reporting`
* `min_live_fraction`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name</p></li>
<li><p><strong>ipv6</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">stickiness_bonus_percentage</span></code></p></li>
</ul>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `stickiness_bonus_constant`
* `health_threshold`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Liveness test name</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `test_interval`
* `test_object_protocol`
* `test_timeout`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>static_rr_sets</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GtmPropertyStaticRrSetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code></p></li>
</ul>
</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `ttl`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>traffic_targets</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GtmPropertyTrafficTargetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter_id</span></code></p></li>
</ul>
</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Property type</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `score_aggregation_type`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>use_computed_targets</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <ul>
<li><p><code class="docutils literal notranslate"><span class="pre">backup_ip</span></code></p></li>
</ul>
</p></li>
<li><p><strong>wait_on_complete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wait for transaction to complete</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `failover_delay`
* `failback_delay`
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmProperty.balance_by_download_score">
<em class="property">property </em><code class="sig-name descname">balance_by_download_score</code><a class="headerlink" href="#pulumi_akamai.GtmProperty.balance_by_download_score" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">static_ttl</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unreachable_threshold</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">health_multiplier</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dynamic_ttl</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_unreachable_penalty</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">map_name</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">load_imbalance_percentage</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">health_max</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cname</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">comments</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ghost_demand_reporting</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_live_fraction</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmProperty.domain">
<em class="property">property </em><code class="sig-name descname">domain</code><a class="headerlink" href="#pulumi_akamai.GtmProperty.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmProperty.ipv6">
<em class="property">property </em><code class="sig-name descname">ipv6</code><a class="headerlink" href="#pulumi_akamai.GtmProperty.ipv6" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">stickiness_bonus_percentage</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stickiness_bonus_constant</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">health_threshold</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmProperty.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_akamai.GtmProperty.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Liveness test name</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">test_interval</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">test_object_protocol</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">test_timeout</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmProperty.static_rr_sets">
<em class="property">property </em><code class="sig-name descname">static_rr_sets</code><a class="headerlink" href="#pulumi_akamai.GtmProperty.static_rr_sets" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmProperty.traffic_targets">
<em class="property">property </em><code class="sig-name descname">traffic_targets</code><a class="headerlink" href="#pulumi_akamai.GtmProperty.traffic_targets" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter_id</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmProperty.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_akamai.GtmProperty.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Property type</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">score_aggregation_type</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmProperty.use_computed_targets">
<em class="property">property </em><code class="sig-name descname">use_computed_targets</code><a class="headerlink" href="#pulumi_akamai.GtmProperty.use_computed_targets" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">backup_ip</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmProperty.wait_on_complete">
<em class="property">property </em><code class="sig-name descname">wait_on_complete</code><a class="headerlink" href="#pulumi_akamai.GtmProperty.wait_on_complete" title="Permalink to this definition">¶</a></dt>
<dd><p>Wait for transaction to complete</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">failover_delay</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failback_delay</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmProperty.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmProperty.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.GtmProperty.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmProperty.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.GtmResource">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">GtmResource</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aggregation_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">constrained_property</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">decay_rate</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_header</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">leader_string</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">least_squares_decay</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_imbalance_percentage</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_u_multiplicative_increment</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_instances</span><span class="p">:</span> <span class="n">Union[Sequence[Union[GtmResourceResourceInstanceArgs, Mapping[str, Any], Awaitable[Union[GtmResourceResourceInstanceArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[GtmResourceResourceInstanceArgs, Mapping[str, Any], Awaitable[Union[GtmResourceResourceInstanceArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">upper_bound</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_on_complete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmResource" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">GtmResource</span></code> provides the resource for creating, configuring and importing a gtm resource to integrate easily with your existing GTM infrastructure to provide a secure, high performance, highly available and scalable solution for Global Traffic Management. Note: Import requires an ID of the format: <cite>existing_domain_name</cite>:<cite>existing_resource_name</cite></p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">demo_resource</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">GtmResource</span><span class="p">(</span><span class="s2">&quot;demoResource&quot;</span><span class="p">,</span>
    <span class="n">aggregation_type</span><span class="o">=</span><span class="s2">&quot;latest&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;demo_domain.akadns.net&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;XML load object via HTTP&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource name</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `aggregation_type`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>resource_instances</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GtmResourceResourceInstanceArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter_id</span></code></p></li>
</ul>
</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `load_object`
* `load_object_port`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource type</p></li>
<li><p><strong>wait_on_complete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wait for transaction to complete</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_akamai.GtmResource.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aggregation_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">constrained_property</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">decay_rate</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_header</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">leader_string</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">least_squares_decay</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_imbalance_percentage</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_u_multiplicative_increment</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_instances</span><span class="p">:</span> <span class="n">Union[Sequence[Union[GtmResourceResourceInstanceArgs, Mapping[str, Any], Awaitable[Union[GtmResourceResourceInstanceArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[GtmResourceResourceInstanceArgs, Mapping[str, Any], Awaitable[Union[GtmResourceResourceInstanceArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">upper_bound</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_on_complete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.gtm_resource.GtmResource<a class="headerlink" href="#pulumi_akamai.GtmResource.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GtmResource resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain name</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource name</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `aggregation_type`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>resource_instances</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GtmResourceResourceInstanceArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter_id</span></code></p></li>
</ul>
</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `load_object`
* `load_object_port`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource type</p></li>
<li><p><strong>wait_on_complete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Wait for transaction to complete</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmResource.domain">
<em class="property">property </em><code class="sig-name descname">domain</code><a class="headerlink" href="#pulumi_akamai.GtmResource.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmResource.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_akamai.GtmResource.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource name</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aggregation_type</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmResource.resource_instances">
<em class="property">property </em><code class="sig-name descname">resource_instances</code><a class="headerlink" href="#pulumi_akamai.GtmResource.resource_instances" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">datacenter_id</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">load_object</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">load_object_port</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmResource.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_akamai.GtmResource.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource type</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmResource.wait_on_complete">
<em class="property">property </em><code class="sig-name descname">wait_on_complete</code><a class="headerlink" href="#pulumi_akamai.GtmResource.wait_on_complete" title="Permalink to this definition">¶</a></dt>
<dd><p>Wait for transaction to complete</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.GtmResource.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmResource.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.GtmResource.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.GtmResource.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.Property">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">Property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contacts</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cp_code</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostnames</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_secure</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origins</span><span class="p">:</span> <span class="n">Union[Sequence[Union[PropertyOriginArgs, Mapping[str, Any], Awaitable[Union[PropertyOriginArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[PropertyOriginArgs, Mapping[str, Any], Awaitable[Union[PropertyOriginArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_format</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.Property" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">Property</span></code> resource represents an Akamai property configuration.
This resource lets you to create, update, and activate properties on the
Akamai platform.</p>
<p>Akamai’s edge network caches your web assets near to servers that request them.
A property provides the main way to control how edge servers respond to various
kinds of requests for those assets. Properties apply rules to a set of hostnames,
and you can only apply one property at a time to any given hostname. Each property
is assigned to a product, which determines which behaviors you can use. Each
property’s default rule needs a valid content provider (CP) code assigned to bill
and report for the service.</p>
<blockquote>
<div><p><strong>NOTE:</strong> In version 0.10 and earlier of this resource, it also controlled content provider (CP) codes, origin settings, rules, and hostname associations. Starting with version 1.0.0, this logic is broken out into individual resources.</p>
</div></blockquote>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">Property</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">contacts</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;user@example.org&quot;</span><span class="p">],</span>
    <span class="n">product_id</span><span class="o">=</span><span class="s2">&quot;prd_SPM&quot;</span><span class="p">,</span>
    <span class="n">contract_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;contractid&quot;</span><span class="p">],</span>
    <span class="n">group_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;groupid&quot;</span><span class="p">],</span>
    <span class="n">hostnames</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;example.org&quot;</span><span class="p">:</span> <span class="s2">&quot;example.org.edgesuite.net&quot;</span><span class="p">,</span>
        <span class="s2">&quot;www.example.org&quot;</span><span class="p">:</span> <span class="s2">&quot;example.org.edgesuite.net&quot;</span><span class="p">,</span>
        <span class="s2">&quot;sub.example.org&quot;</span><span class="p">:</span> <span class="s2">&quot;sub.example.org.edgesuite.net&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">rule_format</span><span class="o">=</span><span class="s2">&quot;v2020-03-04&quot;</span><span class="p">,</span>
    <span class="n">rules</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;akamai_property_rules_template&quot;</span><span class="p">][</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;json&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>This resource supports these arguments:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The property name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contact</span></code> - (Required) One or more email addresses to send activation status changes to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contract_id</span></code> - (Required) A contract’s unique ID, including the <code class="docutils literal notranslate"><span class="pre">ctr_</span></code> prefix.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group_id</span></code> - (Required) A group’s unique ID, including the <code class="docutils literal notranslate"><span class="pre">grp_</span></code> prefix.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product_id</span></code> - (Required to create, otherwise Optional) A product’s unique ID, including the <code class="docutils literal notranslate"><span class="pre">prd_</span></code> prefix.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostnames</span></code> - (Required) A mapping of public hostnames to edge hostnames. For example: <code class="docutils literal notranslate"><span class="pre">{&quot;example.org&quot;</span> <span class="pre">=</span> <span class="pre">&quot;example.org.edgesuite.net&quot;}</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> - (Required) A JSON-encoded rule tree for a given property. For this argument, you need to enter a complete JSON rule tree, unless you set up a series of JSON templates. See the <code class="docutils literal notranslate"><span class="pre">getPropertyRules</span></code> data source.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rule_format</span></code> - (Optional) The <a class="reference external" href="https://developer.akamai.com/api/core_features/property_manager/v1.html#getruleformats">rule format</a> to use. Uses the latest rule format by default.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contract</span></code> - (Deprecated) Replaced by <code class="docutils literal notranslate"><span class="pre">contract_id</span></code>. Maintained for legacy purposes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group</span></code> - (Deprecated) Replaced by <code class="docutils literal notranslate"><span class="pre">group_id</span></code>. Maintained for legacy purposes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> - (Deprecated) Optional argument replaced by the now required <code class="docutils literal notranslate"><span class="pre">product_id</span></code>. Maintained for legacy purposes.</p></li>
</ul>
<p>The resource returns these attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">warnings</span></code> - The contents of <code class="docutils literal notranslate"><span class="pre">warnings</span></code> field returned by the API. For more information see <a class="reference external" href="https://developer.akamai.com/api/core_features/property_manager/v1.html#errors">Errors</a> in the PAPI documentation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errors</span></code> - The contents of <code class="docutils literal notranslate"><span class="pre">errors</span></code> field returned by the API. For more information see <a class="reference external" href="https://developer.akamai.com/api/core_features/property_manager/v1.html#errors">Errors</a> in the PAPI documentation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">latest_version</span></code> - The version of the property you’ve created or updated rules for. The Akamai Provider always uses the latest version or creates a new version if latest is not editable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">production_version</span></code> - The current version of the property active on the Akamai production network.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">staging_version</span></code> - The current version of the property active on the Akamai staging network.</p></li>
</ul>
<p>Basic Usagehcl resource “akamai_property” “example” {</p>
<blockquote>
<div><p>} You can import Akamai properties using either the <code class="docutils literal notranslate"><span class="pre">property_id</span></code> or a comma-delimited</p>
</div></blockquote>
<p>string of the property, contract, and group IDs. You’ll need to enter the string of IDs if the property belongs to multiple groups or contracts. If using the string of IDs, you need to enter them in this order<code class="docutils literal notranslate"><span class="pre">property_id,contract_id,group_id</span></code> Here are some examples</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import akamai:index/property:Property example prp_123

Or
</pre></div>
</div>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import akamai:index/property:Property example prp_123,ctr_1-AB123,grp_123
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>contract_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contract ID to be assigned to the Property</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Group ID to be assigned to the Property</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>hostnames</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Mapping of edge hostname CNAMEs to other CNAMEs</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name to give to the Property (must be unique)</p></li>
<li><p><strong>product_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Product ID to be assigned to the Property</p></li>
<li><p><strong>rule_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the rule format version (defaults to latest version available when created)</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Property Rules as JSON</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_akamai.Property.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contacts</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cp_code</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostnames</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_secure</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latest_version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origins</span><span class="p">:</span> <span class="n">Union[Sequence[Union[PropertyOriginArgs, Mapping[str, Any], Awaitable[Union[PropertyOriginArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[PropertyOriginArgs, Mapping[str, Any], Awaitable[Union[PropertyOriginArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">production_version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_errors</span><span class="p">:</span> <span class="n">Union[Sequence[Union[PropertyRuleErrorArgs, Mapping[str, Any], Awaitable[Union[PropertyRuleErrorArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[PropertyRuleErrorArgs, Mapping[str, Any], Awaitable[Union[PropertyRuleErrorArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_format</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_warnings</span><span class="p">:</span> <span class="n">Union[Sequence[Union[PropertyRuleWarningArgs, Mapping[str, Any], Awaitable[Union[PropertyRuleWarningArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[PropertyRuleWarningArgs, Mapping[str, Any], Awaitable[Union[PropertyRuleWarningArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">staging_version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.property.Property<a class="headerlink" href="#pulumi_akamai.Property.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Property resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>contract_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contract ID to be assigned to the Property</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Group ID to be assigned to the Property</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>hostnames</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Mapping of edge hostname CNAMEs to other CNAMEs</p></li>
<li><p><strong>latest_version</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Property’s current latest version number</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name to give to the Property (must be unique)</p></li>
<li><p><strong>product_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Product ID to be assigned to the Property</p></li>
<li><p><strong>production_version</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Property’s version currently activated in production (zero when not active in production)</p></li>
<li><p><strong>rule_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the rule format version (defaults to latest version available when created)</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Property Rules as JSON</p></li>
<li><p><strong>staging_version</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Property’s version currently activated in staging (zero when not active in staging)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.Property.contract_id">
<em class="property">property </em><code class="sig-name descname">contract_id</code><a class="headerlink" href="#pulumi_akamai.Property.contract_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Contract ID to be assigned to the Property</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.Property.group_id">
<em class="property">property </em><code class="sig-name descname">group_id</code><a class="headerlink" href="#pulumi_akamai.Property.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Group ID to be assigned to the Property</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.Property.hostnames">
<em class="property">property </em><code class="sig-name descname">hostnames</code><a class="headerlink" href="#pulumi_akamai.Property.hostnames" title="Permalink to this definition">¶</a></dt>
<dd><p>Mapping of edge hostname CNAMEs to other CNAMEs</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.Property.latest_version">
<em class="property">property </em><code class="sig-name descname">latest_version</code><a class="headerlink" href="#pulumi_akamai.Property.latest_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Property’s current latest version number</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.Property.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_akamai.Property.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name to give to the Property (must be unique)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.Property.product_id">
<em class="property">property </em><code class="sig-name descname">product_id</code><a class="headerlink" href="#pulumi_akamai.Property.product_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Product ID to be assigned to the Property</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.Property.production_version">
<em class="property">property </em><code class="sig-name descname">production_version</code><a class="headerlink" href="#pulumi_akamai.Property.production_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Property’s version currently activated in production (zero when not active in production)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.Property.rule_format">
<em class="property">property </em><code class="sig-name descname">rule_format</code><a class="headerlink" href="#pulumi_akamai.Property.rule_format" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the rule format version (defaults to latest version available when created)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.Property.rules">
<em class="property">property </em><code class="sig-name descname">rules</code><a class="headerlink" href="#pulumi_akamai.Property.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Property Rules as JSON</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.Property.staging_version">
<em class="property">property </em><code class="sig-name descname">staging_version</code><a class="headerlink" href="#pulumi_akamai.Property.staging_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Property’s version currently activated in staging (zero when not active in staging)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.Property.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.Property.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.Property.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.Property.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.PropertyActivation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">PropertyActivation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">activation_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contacts</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">property</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">property_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.PropertyActivation" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">PropertyActivation</span></code> resource lets you activate a property version. An activation deploys the version to either the Akamai staging or production network. You can activate a specific version multiple times if you need to.</p>
<p>Before activating on production, activate on staging first. This way you can detect any problems in staging before your changes progress to production.</p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">email</span> <span class="o">=</span> <span class="s2">&quot;user@example.org&quot;</span>
<span class="n">rule_format</span> <span class="o">=</span> <span class="s2">&quot;v2020-03-04&quot;</span>
<span class="n">example</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">Property</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">contacts</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;user@example.org&quot;</span><span class="p">],</span>
    <span class="n">product_id</span><span class="o">=</span><span class="s2">&quot;prd_SPM&quot;</span><span class="p">,</span>
    <span class="n">contract_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;contractid&quot;</span><span class="p">],</span>
    <span class="n">group_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;groupid&quot;</span><span class="p">],</span>
    <span class="n">hostnames</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;example.org&quot;</span><span class="p">:</span> <span class="s2">&quot;example.org.edgesuite.net&quot;</span><span class="p">,</span>
        <span class="s2">&quot;www.example.org&quot;</span><span class="p">:</span> <span class="s2">&quot;example.org.edgesuite.net&quot;</span><span class="p">,</span>
        <span class="s2">&quot;sub.example.org&quot;</span><span class="p">:</span> <span class="s2">&quot;sub.example.org.edgesuite.net&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">rule_format</span><span class="o">=</span><span class="n">rule_format</span><span class="p">,</span>
    <span class="n">rules</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">path</span><span class="p">[</span><span class="s1">&#39;module&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">/main.json&quot;</span><span class="p">))</span>
<span class="n">example_staging</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">PropertyActivation</span><span class="p">(</span><span class="s2">&quot;exampleStaging&quot;</span><span class="p">,</span>
    <span class="n">property_id</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">contacts</span><span class="o">=</span><span class="p">[</span><span class="n">email</span><span class="p">],</span>
    <span class="n">version</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">latest_version</span><span class="p">)</span>
<span class="c1"># not specifying network will target STAGING</span>
<span class="n">example_prod</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">PropertyActivation</span><span class="p">(</span><span class="s2">&quot;exampleProd&quot;</span><span class="p">,</span>
    <span class="n">property_id</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">network</span><span class="o">=</span><span class="s2">&quot;PRODUCTION&quot;</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
    <span class="n">contacts</span><span class="o">=</span><span class="p">[</span><span class="n">email</span><span class="p">],</span>
    <span class="n">opts</span><span class="o">=</span><span class="n">pulumi</span><span class="o">.</span><span class="n">ResourceOptions</span><span class="p">(</span><span class="n">depends_on</span><span class="o">=</span><span class="p">[</span><span class="n">example_staging</span><span class="p">]))</span>
</pre></div>
</div>
<p>The following arguments are supported:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">property_id</span></code> - (Required) The property’s unique identifier, including the <code class="docutils literal notranslate"><span class="pre">prp_</span></code> prefix.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">contact</span></code> - (Required) One or more email addresses to send activation status changes to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> - (Required) The property version to activate. Previously this field was optional. It now depends on the <code class="docutils literal notranslate"><span class="pre">Property</span></code> resource to identify latest instead of calculating it locally.  This association helps keep the dependency tree properly aligned. To always use the latest version, enter this value <code class="docutils literal notranslate"><span class="pre">{resource}.{resource</span> <span class="pre">identifier}.{field</span> <span class="pre">name}</span></code>. Using the example code above, the entry would be <code class="docutils literal notranslate"><span class="pre">akamai_property.example.latest_version</span></code> since we want the value of the <code class="docutils literal notranslate"><span class="pre">latest_version</span></code> attribute in the <code class="docutils literal notranslate"><span class="pre">Property</span></code> resource labeled <code class="docutils literal notranslate"><span class="pre">example</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network</span></code> - (Optional) Akamai network to activate on, either <code class="docutils literal notranslate"><span class="pre">STAGING</span></code> or <code class="docutils literal notranslate"><span class="pre">PRODUCTION</span></code>. <code class="docutils literal notranslate"><span class="pre">STAGING</span></code> is the default.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">property</span></code> - (Deprecated) Replaced by <code class="docutils literal notranslate"><span class="pre">property_id</span></code>. Maintained for legacy purposes.</p></li>
</ul>
<p>The following attributes are returned:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> - The unique identifier for this activation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">warnings</span></code> - The contents of <code class="docutils literal notranslate"><span class="pre">warnings</span></code> field returned by the API. For more information see <a class="reference external" href="https://developer.akamai.com/api/core_features/property_manager/v1.html#errors">Errors</a> in the PAPI documentation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errors</span></code> - The contents of <code class="docutils literal notranslate"><span class="pre">errors</span></code> field returned by the API. For more information see <a class="reference external" href="https://developer.akamai.com/api/core_features/property_manager/v1.html#errors">Errors</a> in the PAPI documentation.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">activation_id</span></code> - The ID given to the activation event while it’s in progress.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> - The property version’s activation status on the selected network.</p></li>
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
<dt id="pulumi_akamai.PropertyActivation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">activation_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contacts</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">errors</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">property</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">property_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">warnings</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.property_activation.PropertyActivation<a class="headerlink" href="#pulumi_akamai.PropertyActivation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PropertyActivation resource’s state with the given name, id, and optional extra
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
<dt id="pulumi_akamai.PropertyActivation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.PropertyActivation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.PropertyActivation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.PropertyActivation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.PropertyVariables">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">PropertyVariables</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[PropertyVariablesVariableArgs, Mapping[str, Any], Awaitable[Union[PropertyVariablesVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[PropertyVariablesVariableArgs, Mapping[str, Any], Awaitable[Union[PropertyVariablesVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.PropertyVariables" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a PropertyVariables resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_akamai.PropertyVariables.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[PropertyVariablesVariableArgs, Mapping[str, Any], Awaitable[Union[PropertyVariablesVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[PropertyVariablesVariableArgs, Mapping[str, Any], Awaitable[Union[PropertyVariablesVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.property_variables.PropertyVariables<a class="headerlink" href="#pulumi_akamai.PropertyVariables.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PropertyVariables resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON variables representation</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.PropertyVariables.json">
<em class="property">property </em><code class="sig-name descname">json</code><a class="headerlink" href="#pulumi_akamai.PropertyVariables.json" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON variables representation</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_akamai.PropertyVariables.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.PropertyVariables.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.PropertyVariables.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.PropertyVariables.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">appsec_section</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">appsecs</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ProviderAppsecArgs, Mapping[str, Any], Awaitable[Union[ProviderAppsecArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ProviderAppsecArgs, Mapping[str, Any], Awaitable[Union[ProviderAppsecArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cache_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Union[ProviderConfigArgs, Mapping[str, Any], Awaitable[Union[ProviderConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_section</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns</span><span class="p">:</span> <span class="n">Union[ProviderDnsArgs, Mapping[str, Any], Awaitable[Union[ProviderDnsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_section</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">edgerc</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gtm</span><span class="p">:</span> <span class="n">Union[ProviderGtmArgs, Mapping[str, Any], Awaitable[Union[ProviderGtmArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gtm_section</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">papi_section</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">property</span><span class="p">:</span> <span class="n">Union[ProviderPropertyArgs, Mapping[str, Any], Awaitable[Union[ProviderPropertyArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">property_section</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the akamai package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config_section</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The section of the edgerc file to use for configuration</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_akamai.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_akamai.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_akamai.get_app_sec_configuration">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_app_sec_configuration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_app_sec_configuration.AwaitableGetAppSecConfigurationResult<a class="headerlink" href="#pulumi_akamai.get_app_sec_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">getAppSecConfiguration</span></code> data source to retrieve the list of security configurations, or information about a specific security configuration.</p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">configurations</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_configuration</span><span class="p">()</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;configurationList&quot;</span><span class="p">,</span> <span class="n">configurations</span><span class="o">.</span><span class="n">output_text</span><span class="p">)</span>
<span class="n">specific_configuration</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_configuration</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Akamai Tools&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;latest&quot;</span><span class="p">,</span> <span class="n">specific_configuration</span><span class="o">.</span><span class="n">latest_version</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;staging&quot;</span><span class="p">,</span> <span class="n">specific_configuration</span><span class="o">.</span><span class="n">staging_version</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;production&quot;</span><span class="p">,</span> <span class="n">specific_configuration</span><span class="o">.</span><span class="n">production_version</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;id&quot;</span><span class="p">,</span> <span class="n">specific_configuration</span><span class="o">.</span><span class="n">config_id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of a specific security configuration. If not supplied, information about all security configurations is returned.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_app_sec_configuration_version">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_app_sec_configuration_version</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_app_sec_configuration_version.AwaitableGetAppSecConfigurationVersionResult<a class="headerlink" href="#pulumi_akamai.get_app_sec_configuration_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">getAppSecConfigurationVersion</span></code> data source to retrieve information about the versions of a security configuration, or about a specific version.</p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">specific_configuration</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_configuration</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Akamai Tools&quot;</span><span class="p">)</span>
<span class="n">versions</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_configuration_version</span><span class="p">(</span><span class="n">config_id</span><span class="o">=</span><span class="n">specific_configuration</span><span class="o">.</span><span class="n">config_id</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;versionsOutputText&quot;</span><span class="p">,</span> <span class="n">versions</span><span class="o">.</span><span class="n">output_text</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;versionsLatest&quot;</span><span class="p">,</span> <span class="n">versions</span><span class="o">.</span><span class="n">latest_version</span><span class="p">)</span>
<span class="n">specific_version</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_configuration_version</span><span class="p">(</span><span class="n">config_id</span><span class="o">=</span><span class="n">specific_configuration</span><span class="o">.</span><span class="n">config_id</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="mi">42</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;specificVersionVersion&quot;</span><span class="p">,</span> <span class="n">specific_version</span><span class="o">.</span><span class="n">version</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;specificVersionStaging&quot;</span><span class="p">,</span> <span class="n">specific_version</span><span class="o">.</span><span class="n">staging_status</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;specificVersionProduction&quot;</span><span class="p">,</span> <span class="n">specific_version</span><span class="o">.</span><span class="n">production_status</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>config_id</strong> (<em>int</em>) – The ID of the security configuration to use.</p></li>
<li><p><strong>version</strong> (<em>int</em>) – The version number of the security configuration to use. If not supplied, information about all versions of the specified security configuration is returned.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_app_sec_custom_rule_actions">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_app_sec_custom_rule_actions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_app_sec_custom_rule_actions.AwaitableGetAppSecCustomRuleActionsResult<a class="headerlink" href="#pulumi_akamai.get_app_sec_custom_rule_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">getAppSecCustomRuleActions</span></code> data source to retrieve information about the actions defined for the custom rules associated with a specific security configuration, version and security policy.</p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">configuration</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_configuration</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Akamai Tools&quot;</span><span class="p">)</span>
<span class="n">custom_rule_actions_app_sec_custom_rule_actions</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_custom_rule_actions</span><span class="p">(</span><span class="n">config_id</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">config_id</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">latest_version</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="s2">&quot;crAP_75829&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;customRuleActions&quot;</span><span class="p">,</span> <span class="n">custom_rule_actions_app_sec_custom_rule_actions</span><span class="o">.</span><span class="n">output_text</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>config_id</strong> (<em>int</em>) – The ID of the security configuration to use.</p></li>
<li><p><strong>policy_id</strong> (<em>str</em>) – The ID of the security policy to use</p></li>
<li><p><strong>version</strong> (<em>int</em>) – The version number of the security configuration to use.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_app_sec_custom_rules">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_app_sec_custom_rules</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_app_sec_custom_rules.AwaitableGetAppSecCustomRulesResult<a class="headerlink" href="#pulumi_akamai.get_app_sec_custom_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">getAppSecCustomRules</span></code> data source to retrieve a list of the custom rules defined for a security configuration.</p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">configuration</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_configuration</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Akamai Tools&quot;</span><span class="p">)</span>
<span class="n">custom_rules</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_custom_rules</span><span class="p">(</span><span class="n">config_id</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">config_id</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;customRulesList&quot;</span><span class="p">,</span> <span class="n">custom_rules</span><span class="o">.</span><span class="n">output_text</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>config_id</strong> (<em>int</em>) – The ID of the security configuration to use.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_app_sec_export_configuration">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_app_sec_export_configuration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">searches</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_app_sec_export_configuration.AwaitableGetAppSecExportConfigurationResult<a class="headerlink" href="#pulumi_akamai.get_app_sec_export_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">getAppSecExportConfiguration</span></code> data source to retrieve comprehensive details about a security configuration version, including rate and security policies, rules, hostnames, and other settings. You can retrieve the entire set of information in JSON format, or a subset of the information in tabular format.</p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">configuration</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_configuration</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Akamai Tools&quot;</span><span class="p">)</span>
<span class="n">export</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_export_configuration</span><span class="p">(</span><span class="n">config_id</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">config_id</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">latest_version</span><span class="p">,</span>
    <span class="n">searches</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;securityPolicies&quot;</span><span class="p">,</span>
        <span class="s2">&quot;selectedHosts&quot;</span><span class="p">,</span>
    <span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;json&quot;</span><span class="p">,</span> <span class="n">export</span><span class="o">.</span><span class="n">json</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;text&quot;</span><span class="p">,</span> <span class="n">export</span><span class="o">.</span><span class="n">output_text</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>config_id</strong> (<em>int</em>) – The ID of the security configuration to use.</p></li>
<li><p><strong>searches</strong> (<em>Sequence</em><em>[</em><em>str</em><em>]</em>) – A bracket-delimited list of quoted strings specifying the types of information to be retrieved and made available for display in the <code class="docutils literal notranslate"><span class="pre">output_text</span></code> format. The following types are available:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">customRules</span>
<span class="o">*</span> <span class="n">matchTargets</span>
<span class="o">*</span> <span class="n">ratePolicies</span>
<span class="o">*</span> <span class="n">reputationProfiles</span>
<span class="o">*</span> <span class="n">rulesets</span>
<span class="o">*</span> <span class="n">securityPolicies</span>
<span class="o">*</span> <span class="n">selectableHosts</span>
<span class="o">*</span> <span class="n">selectedHosts</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>version</strong> (<em>int</em>) – The version number of the security configuration to use.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_app_sec_match_targets">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_app_sec_match_targets</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_app_sec_match_targets.AwaitableGetAppSecMatchTargetsResult<a class="headerlink" href="#pulumi_akamai.get_app_sec_match_targets" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">getAppSecMatchTargets</span></code> data source to retrieve information about the match targets associated with a given configuration version.</p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">configuration</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_configuration</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Akamai Tools&quot;</span><span class="p">)</span>
<span class="n">match_targets_app_sec_match_targets</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_match_targets</span><span class="p">(</span><span class="n">config_id</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">config_id</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">latest_version</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;matchTargets&quot;</span><span class="p">,</span> <span class="n">match_targets_app_sec_match_targets</span><span class="o">.</span><span class="n">output_text</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>config_id</strong> (<em>int</em>) – The ID of the security configuration to use.</p></li>
<li><p><strong>version</strong> (<em>int</em>) – The version number of the security configuration to use.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_app_sec_security_policy">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_app_sec_security_policy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_app_sec_security_policy.AwaitableGetAppSecSecurityPolicyResult<a class="headerlink" href="#pulumi_akamai.get_app_sec_security_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">getAppSecSecurityPolicy</span></code> data source to retrieve information about the security policies associated with a specific security configuration version, or about a specific security policy.</p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">configuration</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_configuration</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Akamai Tools&quot;</span><span class="p">)</span>
<span class="n">security_policies</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_security_policy</span><span class="p">(</span><span class="n">config_id</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">config_id</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">latest_version</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;securityPoliciesList&quot;</span><span class="p">,</span> <span class="n">security_policies</span><span class="o">.</span><span class="n">policy_lists</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;securityPoliciesText&quot;</span><span class="p">,</span> <span class="n">security_policies</span><span class="o">.</span><span class="n">output_text</span><span class="p">)</span>
<span class="n">specific_security_policy</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_security_policy</span><span class="p">(</span><span class="n">config_id</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">config_id</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">latest_version</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;APIs&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;specificSecurityPolicyId&quot;</span><span class="p">,</span> <span class="n">specific_security_policy</span><span class="o">.</span><span class="n">policy_id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>config_id</strong> (<em>int</em>) – The ID of the security configuration to use.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the security policy to use. If not supplied, information about all security policies is returned.</p></li>
<li><p><strong>version</strong> (<em>int</em>) – The version number of the security configuration to use.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_app_sec_selectable_hostnames">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_app_sec_selectable_hostnames</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">active_in_production</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active_in_staging</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_app_sec_selectable_hostnames.AwaitableGetAppSecSelectableHostnamesResult<a class="headerlink" href="#pulumi_akamai.get_app_sec_selectable_hostnames" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">getAppSecSelectableHostnames</span></code> data source to retrieve the list of hostnames that may be protected under a given security configuration version.</p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">configuration</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_configuration</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Akamai Tools&quot;</span><span class="p">)</span>
<span class="n">selectable_hostnames_app_sec_selectable_hostnames</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_selectable_hostnames</span><span class="p">(</span><span class="n">config_id</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">config_id</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">latest_version</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;selectableHostnames&quot;</span><span class="p">,</span> <span class="n">selectable_hostnames_app_sec_selectable_hostnames</span><span class="o">.</span><span class="n">hostnames</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;selectableHostnamesJson&quot;</span><span class="p">,</span> <span class="n">selectable_hostnames_app_sec_selectable_hostnames</span><span class="o">.</span><span class="n">hostnames_json</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;selectableHostnamesOutputText&quot;</span><span class="p">,</span> <span class="n">selectable_hostnames_app_sec_selectable_hostnames</span><span class="o">.</span><span class="n">output_text</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>config_id</strong> (<em>int</em>) – The ID of the security configuration to use.</p></li>
<li><p><strong>version</strong> (<em>int</em>) – The version number of the security configuration to use.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_app_sec_selected_hostnames">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_app_sec_selected_hostnames</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">config_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_app_sec_selected_hostnames.AwaitableGetAppSecSelectedHostnamesResult<a class="headerlink" href="#pulumi_akamai.get_app_sec_selected_hostnames" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">AppSecSelectedHostnames</span></code> data source to retrieve a list of the hostnames that are currently protected under a given security configuration version.</p>
<p>Basic usage:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_akamai</span> <span class="k">as</span> <span class="nn">akamai</span>

<span class="n">configuration</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_configuration</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Akamai Tools&quot;</span><span class="p">)</span>
<span class="n">selected_hostnames_app_sec_selected_hostnames</span> <span class="o">=</span> <span class="n">akamai</span><span class="o">.</span><span class="n">get_app_sec_selected_hostnames</span><span class="p">(</span><span class="n">config_id</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">config_id</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="n">configuration</span><span class="o">.</span><span class="n">latest_version</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;selectedHostnames&quot;</span><span class="p">,</span> <span class="n">selected_hostnames_app_sec_selected_hostnames</span><span class="o">.</span><span class="n">hostnames</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;selectedHostnamesJson&quot;</span><span class="p">,</span> <span class="n">selected_hostnames_app_sec_selected_hostnames</span><span class="o">.</span><span class="n">hostnames_json</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;selectedHostnamesOutputText&quot;</span><span class="p">,</span> <span class="n">selected_hostnames_app_sec_selected_hostnames</span><span class="o">.</span><span class="n">output_text</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>config_id</strong> (<em>int</em>) – The ID of the security configuration to use.</p></li>
<li><p><strong>version</strong> (<em>int</em>) – The version number of the security configuration to use.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_authorities_set">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_authorities_set</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">contract</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_authorities_set.AwaitableGetAuthoritiesSetResult<a class="headerlink" href="#pulumi_akamai.get_authorities_set" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_contract">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_contract</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_contract.AwaitableGetContractResult<a class="headerlink" href="#pulumi_akamai.get_contract" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_contracts">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_contracts</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_contracts.AwaitableGetContractsResult<a class="headerlink" href="#pulumi_akamai.get_contracts" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_cp_code">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_cp_code</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">contract</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_cp_code.AwaitableGetCpCodeResult<a class="headerlink" href="#pulumi_akamai.get_cp_code" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_dns_record_set">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_dns_record_set</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">record_type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_dns_record_set.AwaitableGetDnsRecordSetResult<a class="headerlink" href="#pulumi_akamai.get_dns_record_set" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_group">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">contract</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">contract_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_group.AwaitableGetGroupResult<a class="headerlink" href="#pulumi_akamai.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_groups">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_groups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_groups.AwaitableGetGroupsResult<a class="headerlink" href="#pulumi_akamai.get_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_gtm_default_datacenter">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_gtm_default_datacenter</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">datacenter</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_gtm_default_datacenter.AwaitableGetGtmDefaultDatacenterResult<a class="headerlink" href="#pulumi_akamai.get_gtm_default_datacenter" title="Permalink to this definition">¶</a></dt>
<dd><p>Use <code class="docutils literal notranslate"><span class="pre">getGtmDefaultDatacenter</span></code> data source to retrieve default datacenter id and nickname.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_properties">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_properties</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">contract_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_properties.AwaitableGetPropertiesResult<a class="headerlink" href="#pulumi_akamai.get_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">getProperties</span></code> data source to query and retrieve the list of properties for a group and contract
based on the <a class="reference external" href="https://developer.akamai.com/getting-started/edgegrid">EdgeGrid API client token</a> you’re using.</p>
<p>Return properties associated with the EdgeGrid API client token currently used for authentication:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>

<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;myPropertyList&quot;</span><span class="p">,</span> <span class="n">data</span><span class="p">[</span><span class="s2">&quot;akamai_properties&quot;</span><span class="p">][</span><span class="s2">&quot;example&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>This data source supports these arguments:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contract_id</span></code> - (Required) A contract’s unique ID, including the <code class="docutils literal notranslate"><span class="pre">ctr_</span></code> prefix.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group_id</span></code> - (Required) A group’s unique ID, including the <code class="docutils literal notranslate"><span class="pre">grp_</span></code> prefix.</p></li>
</ul>
<p>This data source returns this attribute:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> - A list of properties available for the contract and group IDs provided.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_property">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_property.AwaitableGetPropertyResult<a class="headerlink" href="#pulumi_akamai.get_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_property_products">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_property_products</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">contract_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_property_products.AwaitableGetPropertyProductsResult<a class="headerlink" href="#pulumi_akamai.get_property_products" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">getPropertyProducts</span></code> data source to list the products included on a contract.</p>
<p>This example returns products associated with the <a class="reference external" href="https://developer.akamai.com/getting-started/edgegrid">EdgeGrid client token</a> for a given contract:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>

<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;propertyMatch&quot;</span><span class="p">,</span> <span class="n">data</span><span class="p">[</span><span class="s2">&quot;akamai_property_products&quot;</span><span class="p">][</span><span class="s2">&quot;my-example&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>This data source supports this argument:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contract_id</span></code> - (Required) A contract’s unique ID, including the <code class="docutils literal notranslate"><span class="pre">ctr_</span></code> prefix.</p></li>
</ul>
<p>This data source returns these attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">products</span></code> - A list of supported products for the contract, including:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">product_id</span></code> - The product’s unique ID, including the <code class="docutils literal notranslate"><span class="pre">prd_</span></code> prefix.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product_name</span></code> - A string containing the product name.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_property_rule_formats">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_property_rule_formats</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_property_rule_formats.AwaitableGetPropertyRuleFormatsResult<a class="headerlink" href="#pulumi_akamai.get_property_rule_formats" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">getPropertyRuleFormats</span></code> data source to query the list of
known rule formats.
You use rule formats to <a class="reference external" href="https://developer.akamai.com/api/core_features/property_manager/v1.html#freezerf">freeze</a> or
<a class="reference external" href="https://developer.akamai.com/api/core_features/property_manager/v1.html#updaterf">update</a> the versioned set of behaviors
and criteria a rule tree invokes. Without this mechanism, behaviors and criteria
would update automatically and generate unexpected errors.</p>
<p>Use this example to list available property rule formats:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>

<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;propertyMatch&quot;</span><span class="p">,</span> <span class="n">data</span><span class="p">[</span><span class="s2">&quot;akamai_property_rule_formats&quot;</span><span class="p">][</span><span class="s2">&quot;my-example&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>There are no arguments available for this data source.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_property_rules">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_property_rules</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">contract_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">property_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_property_rules.AwaitableGetPropertyRulesResult<a class="headerlink" href="#pulumi_akamai.get_property_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">getPropertyRules</span></code> data source to query and retrieve the rule tree of
an existing property version. This data source lets you search across the contracts
and groups you have access to.</p>
<p>This example returns the rule tree for version 3 of a property based on the selected contract and group:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>

<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;propertyMatch&quot;</span><span class="p">,</span> <span class="n">data</span><span class="p">[</span><span class="s2">&quot;akamai_property_rules&quot;</span><span class="p">][</span><span class="s2">&quot;my-example&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>This data source supports these arguments:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contract_id</span></code> - (Required) A contract’s unique ID, including the <code class="docutils literal notranslate"><span class="pre">ctr_</span></code> prefix.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">group_id</span></code> - (Required) A group’s unique ID, including the <code class="docutils literal notranslate"><span class="pre">grp_</span></code> prefix.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">property_id</span></code> - (Required) A property’s unique ID, including the <code class="docutils literal notranslate"><span class="pre">prp_</span></code> prefix.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> - (Optional) The version to return. Returns the latest version by default.</p></li>
</ul>
<p>This data source returns these attributes:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> - A JSON-encoded rule tree for the property.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errors</span></code> - A list of validation errors for the rule tree object returned. For more information see <a class="reference external" href="https://developer.akamai.com/api/core_features/property_manager/v1.html#errors">Errors</a> in the Property Manager API documentation.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_akamai.get_property_rules_template">
<code class="sig-prename descclassname">pulumi_akamai.</code><code class="sig-name descname">get_property_rules_template</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">template_file</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">var_definition_file</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">var_values_file</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>GetPropertyRulesTemplateVariableArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_akamai.get_property_rules_template.AwaitableGetPropertyRulesTemplateResult<a class="headerlink" href="#pulumi_akamai.get_property_rules_template" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">getPropertyRulesTemplate</span></code> data source lets you configure a rule tree through the use of JSON template files. A rule tree is a nested block of property
rules in JSON format that include match criteria and behaviors.</p>
<p>With this data source you define the location of the JSON template files and provide information about any user-defined variables included within the templates.</p>
<p>The template format used in this data source matches those used in the <a class="reference external" href="https://learn.akamai.com/en-us/learn_akamai/getting_started_with_akamai_developers/developer_tools/getstartedpmcli.html#addanewsnippet">Property Manager CLI</a>.</p>
<p>You can pass user-defined variables by supplying either:</p>
<ul class="simple">
<li><p>paths to <code class="docutils literal notranslate"><span class="pre">variableDefinitions.json</span></code> and <code class="docutils literal notranslate"><span class="pre">variables.json</span></code> with syntax used in Property Manager CLI, or</p></li>
<li><p>a set of provider variables.</p></li>
</ul>
<p>You can split each template out into a series of smaller template files. To add
them to this data source, you need to include them in the currently loaded file,
which corresponds to the value in the <code class="docutils literal notranslate"><span class="pre">template_file</span></code> argument.  For example, to
include <code class="docutils literal notranslate"><span class="pre">example-file.json</span></code> from the <code class="docutils literal notranslate"><span class="pre">template</span></code> directory, use this syntax
including the quotes: <code class="docutils literal notranslate"><span class="pre">&quot;#include:example-file.json&quot;</span></code>.  All files are resolved in
relation to the directory that contains the starting template file.</p>
<p>You can also add variables to a template by using a string like <code class="docutils literal notranslate"><span class="pre">“${env.&lt;variableName&gt;}&quot;</span></code>. You’ll need the quotes here too.    These variables follow the format used in the <a class="reference external" href="https://github.com/akamai/cli-property-manager#update-the-variabledefinitions-file">Property Manager CLI</a>.  They differ from the provider variables which should resolve normally.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">template_file</span></code> - (Required) The absolute path to your top-level JSON template file. The top-level template combines smaller, nested JSON templates to form your property rule tree.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">variables</span></code> - (Optional) A definition of a variable. Variables aren’t required and you can use multiple ones if needed. This argument conflicts with the <code class="docutils literal notranslate"><span class="pre">variable_definition_file</span></code> and <code class="docutils literal notranslate"><span class="pre">variable_values_file</span></code> arguments. A <code class="docutils literal notranslate"><span class="pre">variables</span></code> block includes:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - The name of the variable used in template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - The type of variable: <code class="docutils literal notranslate"><span class="pre">string</span></code>, <code class="docutils literal notranslate"><span class="pre">number</span></code>, <code class="docutils literal notranslate"><span class="pre">bool</span></code>, or <code class="docutils literal notranslate"><span class="pre">jsonBlock</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> - The value of the variable passed as a string.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">variable_definition_file</span></code> - (Optional) The absolute path to the file containing variable definitions and defaults. This file follows the syntax used in the <a class="reference external" href="https://github.com/akamai/cli-property-manager">Property Manager CLI</a>. This argument is required if you set <code class="docutils literal notranslate"><span class="pre">variable_values_file</span></code> and conflicts with <code class="docutils literal notranslate"><span class="pre">variables</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">variable_values_file</span></code> - (Optional) The absolute path to the file containing variable values. This file follows the syntax used in the Property Manager CLI. This argument is required if you set <code class="docutils literal notranslate"><span class="pre">variable_definition_file</span></code> and conflicts with <code class="docutils literal notranslate"><span class="pre">variables</span></code>.</p></li>
</ul>
<p>This data source returns this attribute:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">json</span></code> - The fully expanded template with variables and all nested templates resolved.</p></li>
</ul>
</dd></dl>

</div>
