---
title: Package pulumi_kafka
title_tag: Package pulumi_kafka | Python SDK
linktitle: pulumi_kafka
notitle: true
---

<div class="section" id="module-pulumi_kafka">
<span id="pulumi-kafka"></span><h1>Pulumi Kafka<a class="headerlink" href="#module-pulumi_kafka" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_kafka.Acl">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kafka.</code><code class="sig-name descname">Acl</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acl_host=None</em>, <em class="sig-param">acl_operation=None</em>, <em class="sig-param">acl_permission_type=None</em>, <em class="sig-param">acl_principal=None</em>, <em class="sig-param">acl_resource_name=None</em>, <em class="sig-param">resource_pattern_type_filter=None</em>, <em class="sig-param">acl_resource_type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Acl" title="Permalink to this definition">¶</a></dt>
<dd><p>A resource for managing Kafka ACLs.</p>
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
<li><p><strong>resource_pattern_type_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pattern filter. Valid values
are <code class="docutils literal notranslate"><span class="pre">Prefixed</span></code>, <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">Match</span></code>, <code class="docutils literal notranslate"><span class="pre">Literal</span></code>.</p></li>
<li><p><strong>acl_resource_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of resource. Valid values are <code class="docutils literal notranslate"><span class="pre">Unknown</span></code>,
<code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">Topic</span></code>, <code class="docutils literal notranslate"><span class="pre">Group</span></code>, <code class="docutils literal notranslate"><span class="pre">Cluster</span></code>, <code class="docutils literal notranslate"><span class="pre">TransactionalID</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/Mongey/terraform-provider-kafka/blob/master/website/docs/r/acl.html.markdown">https://github.com/Mongey/terraform-provider-kafka/blob/master/website/docs/r/acl.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_kafka.Acl.acl_host">
<code class="sig-name descname">acl_host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kafka.Acl.acl_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Host from which principal listed in <code class="docutils literal notranslate"><span class="pre">acl_principal</span></code>
will have access.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kafka.Acl.acl_operation">
<code class="sig-name descname">acl_operation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kafka.Acl.acl_operation" title="Permalink to this definition">¶</a></dt>
<dd><p>Operation that is being allowed or denied. Valid
values are <code class="docutils literal notranslate"><span class="pre">Unknown</span></code>, <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">All</span></code>, <code class="docutils literal notranslate"><span class="pre">Read</span></code>, <code class="docutils literal notranslate"><span class="pre">Write</span></code>, <code class="docutils literal notranslate"><span class="pre">Create</span></code>, <code class="docutils literal notranslate"><span class="pre">Delete</span></code>, <code class="docutils literal notranslate"><span class="pre">Alter</span></code>,
<code class="docutils literal notranslate"><span class="pre">Describe</span></code>, <code class="docutils literal notranslate"><span class="pre">ClusterAction</span></code>, <code class="docutils literal notranslate"><span class="pre">DescribeConfigs</span></code>, <code class="docutils literal notranslate"><span class="pre">AlterConfigs</span></code>, <code class="docutils literal notranslate"><span class="pre">IdempotentWrite</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kafka.Acl.acl_permission_type">
<code class="sig-name descname">acl_permission_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kafka.Acl.acl_permission_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of permission. Valid values are <code class="docutils literal notranslate"><span class="pre">Unknown</span></code>,
<code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">Allow</span></code>, <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kafka.Acl.acl_principal">
<code class="sig-name descname">acl_principal</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kafka.Acl.acl_principal" title="Permalink to this definition">¶</a></dt>
<dd><p>Principal that is being allowed or denied.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kafka.Acl.acl_resource_name">
<code class="sig-name descname">acl_resource_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kafka.Acl.acl_resource_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kafka.Acl.resource_pattern_type_filter">
<code class="sig-name descname">resource_pattern_type_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kafka.Acl.resource_pattern_type_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The pattern filter. Valid values
are <code class="docutils literal notranslate"><span class="pre">Prefixed</span></code>, <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">Match</span></code>, <code class="docutils literal notranslate"><span class="pre">Literal</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kafka.Acl.acl_resource_type">
<code class="sig-name descname">acl_resource_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kafka.Acl.acl_resource_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of resource. Valid values are <code class="docutils literal notranslate"><span class="pre">Unknown</span></code>,
<code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">Topic</span></code>, <code class="docutils literal notranslate"><span class="pre">Group</span></code>, <code class="docutils literal notranslate"><span class="pre">Cluster</span></code>, <code class="docutils literal notranslate"><span class="pre">TransactionalID</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kafka.Acl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acl_host=None</em>, <em class="sig-param">acl_operation=None</em>, <em class="sig-param">acl_permission_type=None</em>, <em class="sig-param">acl_principal=None</em>, <em class="sig-param">acl_resource_name=None</em>, <em class="sig-param">resource_pattern_type_filter=None</em>, <em class="sig-param">acl_resource_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Acl.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Acl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<li><p><strong>resource_pattern_type_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pattern filter. Valid values
are <code class="docutils literal notranslate"><span class="pre">Prefixed</span></code>, <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">Match</span></code>, <code class="docutils literal notranslate"><span class="pre">Literal</span></code>.</p></li>
<li><p><strong>acl_resource_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of resource. Valid values are <code class="docutils literal notranslate"><span class="pre">Unknown</span></code>,
<code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">Topic</span></code>, <code class="docutils literal notranslate"><span class="pre">Group</span></code>, <code class="docutils literal notranslate"><span class="pre">Cluster</span></code>, <code class="docutils literal notranslate"><span class="pre">TransactionalID</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/Mongey/terraform-provider-kafka/blob/master/website/docs/r/acl.html.markdown">https://github.com/Mongey/terraform-provider-kafka/blob/master/website/docs/r/acl.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_kafka.Acl.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Acl.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kafka.Acl.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Acl.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kafka.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kafka.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bootstrap_servers=None</em>, <em class="sig-param">ca_cert=None</em>, <em class="sig-param">ca_cert_file=None</em>, <em class="sig-param">client_cert=None</em>, <em class="sig-param">client_cert_file=None</em>, <em class="sig-param">client_key=None</em>, <em class="sig-param">client_key_file=None</em>, <em class="sig-param">sasl_mechanism=None</em>, <em class="sig-param">sasl_password=None</em>, <em class="sig-param">sasl_username=None</em>, <em class="sig-param">skip_tls_verify=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">tls_enabled=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the kafka package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/Mongey/terraform-provider-kafka/blob/master/website/docs/index.html.markdown">https://github.com/Mongey/terraform-provider-kafka/blob/master/website/docs/index.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_kafka.Provider.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Provider.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Provider resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/Mongey/terraform-provider-kafka/blob/master/website/docs/index.html.markdown">https://github.com/Mongey/terraform-provider-kafka/blob/master/website/docs/index.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_kafka.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kafka.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kafka.Topic">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kafka.</code><code class="sig-name descname">Topic</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">partitions=None</em>, <em class="sig-param">replication_factor=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Topic" title="Permalink to this definition">¶</a></dt>
<dd><p>A resource for managing Kafka topics. Increases partition count without destroying the topic.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of string k/v attributes.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the topic.</p></li>
<li><p><strong>partitions</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of partitions the topic should have.</p></li>
<li><p><strong>replication_factor</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of replicas the topic should have.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/Mongey/terraform-provider-kafka/blob/master/website/docs/r/topic.html.markdown">https://github.com/Mongey/terraform-provider-kafka/blob/master/website/docs/r/topic.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_kafka.Topic.config">
<code class="sig-name descname">config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kafka.Topic.config" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of string k/v attributes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kafka.Topic.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kafka.Topic.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the topic.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kafka.Topic.partitions">
<code class="sig-name descname">partitions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kafka.Topic.partitions" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of partitions the topic should have.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kafka.Topic.replication_factor">
<code class="sig-name descname">replication_factor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kafka.Topic.replication_factor" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of replicas the topic should have.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kafka.Topic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">partitions=None</em>, <em class="sig-param">replication_factor=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Topic.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Topic resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of string k/v attributes.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the topic.</p></li>
<li><p><strong>partitions</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of partitions the topic should have.</p></li>
<li><p><strong>replication_factor</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of replicas the topic should have.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/Mongey/terraform-provider-kafka/blob/master/website/docs/r/topic.html.markdown">https://github.com/Mongey/terraform-provider-kafka/blob/master/website/docs/r/topic.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_kafka.Topic.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Topic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_kafka.Topic.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Topic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
