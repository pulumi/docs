---
title: Package pulumi_kafka
title_tag: Package pulumi_kafka | Python SDK
linktitle: pulumi_kafka
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "kafka" >}}

<div class="section" id="module-pulumi_kafka">
<span id="pulumi-kafka"></span><h1>Pulumi Kafka<a class="headerlink" href="#module-pulumi_kafka" title="Permalink to this headline">¶</a></h1>
<dl class="py class">
<dt id="pulumi_kafka.Acl">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kafka.</code><code class="sig-name descname">Acl</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_operation</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_permission_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_principal</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_resource_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_resource_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_pattern_type_filter</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Acl" title="Permalink to this definition">¶</a></dt>
<dd><p>A resource for managing Kafka ACLs.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_kafka</span> <span class="k">as</span> <span class="nn">kafka</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">kafka</span><span class="o">.</span><span class="n">Acl</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">acl_resource_name</span><span class="o">=</span><span class="s2">&quot;syslog&quot;</span><span class="p">,</span>
    <span class="n">acl_resource_type</span><span class="o">=</span><span class="s2">&quot;Topic&quot;</span><span class="p">,</span>
    <span class="n">acl_principal</span><span class="o">=</span><span class="s2">&quot;User:Alice&quot;</span><span class="p">,</span>
    <span class="n">acl_host</span><span class="o">=</span><span class="s2">&quot;*&quot;</span><span class="p">,</span>
    <span class="n">acl_operation</span><span class="o">=</span><span class="s2">&quot;Write&quot;</span><span class="p">,</span>
    <span class="n">acl_permission_type</span><span class="o">=</span><span class="s2">&quot;Deny&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Host from which principal listed in <code class="docutils literal notranslate"><span class="pre">acl_principal</span></code>
will have access.</p></li>
<li><p><strong>acl_operation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation that is being allowed or denied. Valid
values are <code class="docutils literal notranslate"><span class="pre">Unknown</span></code>, <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">All</span></code>, <code class="docutils literal notranslate"><span class="pre">Read</span></code>, <code class="docutils literal notranslate"><span class="pre">Write</span></code>, <code class="docutils literal notranslate"><span class="pre">Create</span></code>, <code class="docutils literal notranslate"><span class="pre">Delete</span></code>, <code class="docutils literal notranslate"><span class="pre">Alter</span></code>,
<code class="docutils literal notranslate"><span class="pre">Describe</span></code>, <code class="docutils literal notranslate"><span class="pre">ClusterAction</span></code>, <code class="docutils literal notranslate"><span class="pre">DescribeConfigs</span></code>, <code class="docutils literal notranslate"><span class="pre">AlterConfigs</span></code>, <code class="docutils literal notranslate"><span class="pre">IdempotentWrite</span></code>.</p></li>
<li><p><strong>acl_permission_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of permission. Valid values are <code class="docutils literal notranslate"><span class="pre">Unknown</span></code>,
<code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">Allow</span></code>, <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p></li>
<li><p><strong>acl_principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Principal that is being allowed or denied.</p></li>
<li><p><strong>acl_resource_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource.</p></li>
<li><p><strong>acl_resource_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of resource. Valid values are <code class="docutils literal notranslate"><span class="pre">Unknown</span></code>,
<code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">Topic</span></code>, <code class="docutils literal notranslate"><span class="pre">Group</span></code>, <code class="docutils literal notranslate"><span class="pre">Cluster</span></code>, <code class="docutils literal notranslate"><span class="pre">TransactionalID</span></code>.</p></li>
<li><p><strong>resource_pattern_type_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pattern filter. Valid values
are <code class="docutils literal notranslate"><span class="pre">Prefixed</span></code>, <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">Match</span></code>, <code class="docutils literal notranslate"><span class="pre">Literal</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_kafka.Acl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_operation</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_permission_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_principal</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_resource_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">acl_resource_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_pattern_type_filter</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_kafka.acl.Acl<a class="headerlink" href="#pulumi_kafka.Acl.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Acl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl_host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Host from which principal listed in <code class="docutils literal notranslate"><span class="pre">acl_principal</span></code>
will have access.</p></li>
<li><p><strong>acl_operation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Operation that is being allowed or denied. Valid
values are <code class="docutils literal notranslate"><span class="pre">Unknown</span></code>, <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">All</span></code>, <code class="docutils literal notranslate"><span class="pre">Read</span></code>, <code class="docutils literal notranslate"><span class="pre">Write</span></code>, <code class="docutils literal notranslate"><span class="pre">Create</span></code>, <code class="docutils literal notranslate"><span class="pre">Delete</span></code>, <code class="docutils literal notranslate"><span class="pre">Alter</span></code>,
<code class="docutils literal notranslate"><span class="pre">Describe</span></code>, <code class="docutils literal notranslate"><span class="pre">ClusterAction</span></code>, <code class="docutils literal notranslate"><span class="pre">DescribeConfigs</span></code>, <code class="docutils literal notranslate"><span class="pre">AlterConfigs</span></code>, <code class="docutils literal notranslate"><span class="pre">IdempotentWrite</span></code>.</p></li>
<li><p><strong>acl_permission_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of permission. Valid values are <code class="docutils literal notranslate"><span class="pre">Unknown</span></code>,
<code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">Allow</span></code>, <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p></li>
<li><p><strong>acl_principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Principal that is being allowed or denied.</p></li>
<li><p><strong>acl_resource_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource.</p></li>
<li><p><strong>acl_resource_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of resource. Valid values are <code class="docutils literal notranslate"><span class="pre">Unknown</span></code>,
<code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">Topic</span></code>, <code class="docutils literal notranslate"><span class="pre">Group</span></code>, <code class="docutils literal notranslate"><span class="pre">Cluster</span></code>, <code class="docutils literal notranslate"><span class="pre">TransactionalID</span></code>.</p></li>
<li><p><strong>resource_pattern_type_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pattern filter. Valid values
are <code class="docutils literal notranslate"><span class="pre">Prefixed</span></code>, <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">Match</span></code>, <code class="docutils literal notranslate"><span class="pre">Literal</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kafka.Acl.acl_host">
<em class="property">property </em><code class="sig-name descname">acl_host</code><a class="headerlink" href="#pulumi_kafka.Acl.acl_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Host from which principal listed in <code class="docutils literal notranslate"><span class="pre">acl_principal</span></code>
will have access.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kafka.Acl.acl_operation">
<em class="property">property </em><code class="sig-name descname">acl_operation</code><a class="headerlink" href="#pulumi_kafka.Acl.acl_operation" title="Permalink to this definition">¶</a></dt>
<dd><p>Operation that is being allowed or denied. Valid
values are <code class="docutils literal notranslate"><span class="pre">Unknown</span></code>, <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">All</span></code>, <code class="docutils literal notranslate"><span class="pre">Read</span></code>, <code class="docutils literal notranslate"><span class="pre">Write</span></code>, <code class="docutils literal notranslate"><span class="pre">Create</span></code>, <code class="docutils literal notranslate"><span class="pre">Delete</span></code>, <code class="docutils literal notranslate"><span class="pre">Alter</span></code>,
<code class="docutils literal notranslate"><span class="pre">Describe</span></code>, <code class="docutils literal notranslate"><span class="pre">ClusterAction</span></code>, <code class="docutils literal notranslate"><span class="pre">DescribeConfigs</span></code>, <code class="docutils literal notranslate"><span class="pre">AlterConfigs</span></code>, <code class="docutils literal notranslate"><span class="pre">IdempotentWrite</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kafka.Acl.acl_permission_type">
<em class="property">property </em><code class="sig-name descname">acl_permission_type</code><a class="headerlink" href="#pulumi_kafka.Acl.acl_permission_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of permission. Valid values are <code class="docutils literal notranslate"><span class="pre">Unknown</span></code>,
<code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">Allow</span></code>, <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kafka.Acl.acl_principal">
<em class="property">property </em><code class="sig-name descname">acl_principal</code><a class="headerlink" href="#pulumi_kafka.Acl.acl_principal" title="Permalink to this definition">¶</a></dt>
<dd><p>Principal that is being allowed or denied.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kafka.Acl.acl_resource_name">
<em class="property">property </em><code class="sig-name descname">acl_resource_name</code><a class="headerlink" href="#pulumi_kafka.Acl.acl_resource_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kafka.Acl.acl_resource_type">
<em class="property">property </em><code class="sig-name descname">acl_resource_type</code><a class="headerlink" href="#pulumi_kafka.Acl.acl_resource_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of resource. Valid values are <code class="docutils literal notranslate"><span class="pre">Unknown</span></code>,
<code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">Topic</span></code>, <code class="docutils literal notranslate"><span class="pre">Group</span></code>, <code class="docutils literal notranslate"><span class="pre">Cluster</span></code>, <code class="docutils literal notranslate"><span class="pre">TransactionalID</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kafka.Acl.resource_pattern_type_filter">
<em class="property">property </em><code class="sig-name descname">resource_pattern_type_filter</code><a class="headerlink" href="#pulumi_kafka.Acl.resource_pattern_type_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The pattern filter. Valid values
are <code class="docutils literal notranslate"><span class="pre">Prefixed</span></code>, <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">Match</span></code>, <code class="docutils literal notranslate"><span class="pre">Literal</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kafka.Acl.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Acl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kafka.Acl.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Acl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kafka.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kafka.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootstrap_servers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_cert</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_cert_file</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_cert</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_cert_file</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_key_file</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_key_passphrase</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sasl_mechanism</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sasl_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sasl_username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_tls_verify</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tls_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the kafka package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bootstrap_servers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of kafka brokers</p></li>
<li><p><strong>ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CA certificate file to validate the server’s certificate.</p></li>
<li><p><strong>ca_cert_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to a CA certificate file to validate the server’s certificate.</p></li>
<li><p><strong>client_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client certificate.</p></li>
<li><p><strong>client_cert_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to a file containing the client certificate.</p></li>
<li><p><strong>client_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key that the certificate was issued for.</p></li>
<li><p><strong>client_key_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to a file containing the private key that the certificate was issued for.</p></li>
<li><p><strong>client_key_passphrase</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The passphrase for the private key that the certificate was issued for.</p></li>
<li><p><strong>sasl_mechanism</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SASL mechanism, can be plain, scram-sha512, scram-sha256</p></li>
<li><p><strong>sasl_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password for SASL authentication.</p></li>
<li><p><strong>sasl_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username for SASL authentication.</p></li>
<li><p><strong>skip_tls_verify</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set this to true only if the target Kafka server is an insecure development instance.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Timeout in seconds</p></li>
<li><p><strong>tls_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable communication with the Kafka Cluster over TLS.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_kafka.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kafka.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kafka.Topic">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kafka.</code><code class="sig-name descname">Topic</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partitions</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_factor</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Topic" title="Permalink to this definition">¶</a></dt>
<dd><p>A resource for managing Kafka topics. Increases partition count without destroying the topic.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_kafka</span> <span class="k">as</span> <span class="nn">kafka</span>

<span class="n">logs</span> <span class="o">=</span> <span class="n">kafka</span><span class="o">.</span><span class="n">Topic</span><span class="p">(</span><span class="s2">&quot;logs&quot;</span><span class="p">,</span>
    <span class="n">config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;cleanup.policy&quot;</span><span class="p">:</span> <span class="s2">&quot;compact&quot;</span><span class="p">,</span>
        <span class="s2">&quot;segment.ms&quot;</span><span class="p">:</span> <span class="s2">&quot;20000&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">partitions</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span>
    <span class="n">replication_factor</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</pre></div>
</div>
<p>Topics can be imported using their ARN, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import kafka:index/topic:Topic logs systemd_logs
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map of string k/v attributes.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the topic.</p></li>
<li><p><strong>partitions</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of partitions the topic should have.</p></li>
<li><p><strong>replication_factor</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of replicas the topic should have.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_kafka.Topic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partitions</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_factor</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_kafka.topic.Topic<a class="headerlink" href="#pulumi_kafka.Topic.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Topic resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map of string k/v attributes.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the topic.</p></li>
<li><p><strong>partitions</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of partitions the topic should have.</p></li>
<li><p><strong>replication_factor</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of replicas the topic should have.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kafka.Topic.config">
<em class="property">property </em><code class="sig-name descname">config</code><a class="headerlink" href="#pulumi_kafka.Topic.config" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of string k/v attributes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kafka.Topic.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_kafka.Topic.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the topic.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kafka.Topic.partitions">
<em class="property">property </em><code class="sig-name descname">partitions</code><a class="headerlink" href="#pulumi_kafka.Topic.partitions" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of partitions the topic should have.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kafka.Topic.replication_factor">
<em class="property">property </em><code class="sig-name descname">replication_factor</code><a class="headerlink" href="#pulumi_kafka.Topic.replication_factor" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of replicas the topic should have.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_kafka.Topic.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Topic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kafka.Topic.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Topic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
