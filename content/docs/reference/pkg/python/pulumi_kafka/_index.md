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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_kafka.</code><code class="sig-name descname">Acl</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acl_host=None</em>, <em class="sig-param">acl_operation=None</em>, <em class="sig-param">acl_permission_type=None</em>, <em class="sig-param">acl_principal=None</em>, <em class="sig-param">acl_resource_name=None</em>, <em class="sig-param">acl_resource_type=None</em>, <em class="sig-param">resource_pattern_type_filter=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Acl" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Acl resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] acl_resource_name: The name of the resouce</p>
<dl class="attribute">
<dt id="pulumi_kafka.Acl.acl_resource_name">
<code class="sig-name descname">acl_resource_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kafka.Acl.acl_resource_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resouce</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_kafka.Acl.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">acl_host=None</em>, <em class="sig-param">acl_operation=None</em>, <em class="sig-param">acl_permission_type=None</em>, <em class="sig-param">acl_principal=None</em>, <em class="sig-param">acl_resource_name=None</em>, <em class="sig-param">acl_resource_type=None</em>, <em class="sig-param">resource_pattern_type_filter=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_kafka.Acl.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Acl resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>acl_resource_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resouce</p></li>
</ul>
</dd>
</dl>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/Mongey/terraform-provider-kafka/blob/master/website/docs/index.html.markdown">https://github.com/Mongey/terraform-provider-kafka/blob/master/website/docs/index.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bootstrap_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of kafka brokers</p></li>
<li><p><strong>ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CA certificate file to validate the server’s certificate.</p></li>
<li><p><strong>ca_cert_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to a CA certificate file to validate the server’s certificate.</p></li>
<li><p><strong>client_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client certificate.</p></li>
<li><p><strong>client_cert_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to a file containing the client certificate.</p></li>
<li><p><strong>client_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key that the certificate was issued for.</p></li>
<li><p><strong>client_key_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to a file containing the private key that the certificate was issued for.</p></li>
<li><p><strong>sasl_mechanism</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SASL mechanism, can be plain, scram-sha512, scram-sha256</p></li>
<li><p><strong>sasl_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password for SASL authentication.</p></li>
<li><p><strong>sasl_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username for SASL authentication.</p></li>
<li><p><strong>skip_tls_verify</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set this to true only if the target Kafka server is an insecure development instance.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout in seconds</p></li>
<li><p><strong>tls_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable communication with the Kafka Cluster over TLS.</p></li>
</ul>
</dd>
</dl>
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
<dd><p>Create a Topic resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] config: A map of string k/v attributes.
:param pulumi.Input[str] name: The name of the topic.
:param pulumi.Input[float] partitions: Number of partitions.
:param pulumi.Input[float] replication_factor: Number of replicas.</p>
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
<dd><p>Number of partitions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_kafka.Topic.replication_factor">
<code class="sig-name descname">replication_factor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_kafka.Topic.replication_factor" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of replicas.</p>
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
<li><p><strong>partitions</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of partitions.</p></li>
<li><p><strong>replication_factor</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of replicas.</p></li>
</ul>
</dd>
</dl>
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
