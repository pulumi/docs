---
title: Module msk
---

<div class="section" id="msk">
<h1>msk<a class="headerlink" href="#msk" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.msk"></span><dl class="class">
<dt id="pulumi_aws.msk.AwaitableGetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.msk.</code><code class="sig-name descname">AwaitableGetClusterResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">bootstrap_brokers=None</em>, <em class="sig-param">bootstrap_brokers_tls=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">kafka_version=None</em>, <em class="sig-param">number_of_broker_nodes=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zookeeper_connect_string=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.AwaitableGetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.msk.AwaitableGetConfigurationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.msk.</code><code class="sig-name descname">AwaitableGetConfigurationResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">kafka_versions=None</em>, <em class="sig-param">latest_revision=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">server_properties=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.AwaitableGetConfigurationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.msk.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.msk.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">broker_node_group_info=None</em>, <em class="sig-param">client_authentication=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">configuration_info=None</em>, <em class="sig-param">encryption_info=None</em>, <em class="sig-param">enhanced_monitoring=None</em>, <em class="sig-param">kafka_version=None</em>, <em class="sig-param">number_of_broker_nodes=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages AWS Managed Streaming for Kafka cluster</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>broker_node_group_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for the broker nodes of the Kafka cluster.</p></li>
<li><p><strong>client_authentication</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for specifying a client authentication. See below.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the MSK cluster.</p></li>
<li><p><strong>configuration_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.</p></li>
<li><p><strong>encryption_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for specifying encryption. See below.</p></li>
<li><p><strong>enhanced_monitoring</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the desired enhanced MSK CloudWatch monitoring level.  See <a class="reference external" href="https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html">Monitoring Amazon MSK with Amazon CloudWatch</a></p></li>
<li><p><strong>kafka_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the desired Kafka software version.</p></li>
<li><p><strong>number_of_broker_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/msk_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/msk_cluster.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.bootstrap_brokers">
<code class="sig-name descname">bootstrap_brokers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.bootstrap_brokers" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of one or more hostname:port pairs of kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if <code class="docutils literal notranslate"><span class="pre">client_broker</span></code> encryption in transit is set to <code class="docutils literal notranslate"><span class="pre">PLAINTEXT</span></code> or <code class="docutils literal notranslate"><span class="pre">TLS_PLAINTEXT</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.bootstrap_brokers_tls">
<code class="sig-name descname">bootstrap_brokers_tls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.bootstrap_brokers_tls" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if <code class="docutils literal notranslate"><span class="pre">client_broker</span></code> encryption in transit is set to <code class="docutils literal notranslate"><span class="pre">TLS_PLAINTEXT</span></code> or <code class="docutils literal notranslate"><span class="pre">TLS</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.broker_node_group_info">
<code class="sig-name descname">broker_node_group_info</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.broker_node_group_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block for the broker nodes of the Kafka cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.client_authentication">
<code class="sig-name descname">client_authentication</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.client_authentication" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block for specifying a client authentication. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.cluster_name">
<code class="sig-name descname">cluster_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the MSK cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.configuration_info">
<code class="sig-name descname">configuration_info</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.configuration_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.current_version">
<code class="sig-name descname">current_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.current_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Current version of the MSK Cluster used for updates, e.g. <code class="docutils literal notranslate"><span class="pre">K13V1IB3VIYZZH</span></code></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encryption_info.0.encryption_at_rest_kms_key_arn</span></code> - The ARN of the KMS key used for encryption at rest of the broker data volumes.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.encryption_info">
<code class="sig-name descname">encryption_info</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.encryption_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block for specifying encryption. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.enhanced_monitoring">
<code class="sig-name descname">enhanced_monitoring</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.enhanced_monitoring" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the desired enhanced MSK CloudWatch monitoring level.  See <a class="reference external" href="https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html">Monitoring Amazon MSK with Amazon CloudWatch</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.kafka_version">
<code class="sig-name descname">kafka_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.kafka_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the desired Kafka software version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.number_of_broker_nodes">
<code class="sig-name descname">number_of_broker_nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.number_of_broker_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.zookeeper_connect_string">
<code class="sig-name descname">zookeeper_connect_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.zookeeper_connect_string" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of one or more IP:port pairs to use to connect to the Apache Zookeeper cluster.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.msk.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">bootstrap_brokers=None</em>, <em class="sig-param">bootstrap_brokers_tls=None</em>, <em class="sig-param">broker_node_group_info=None</em>, <em class="sig-param">client_authentication=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">configuration_info=None</em>, <em class="sig-param">current_version=None</em>, <em class="sig-param">encryption_info=None</em>, <em class="sig-param">enhanced_monitoring=None</em>, <em class="sig-param">kafka_version=None</em>, <em class="sig-param">number_of_broker_nodes=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zookeeper_connect_string=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.
:param pulumi.Input[str] bootstrap_brokers: A comma separated list of one or more hostname:port pairs of kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if <code class="docutils literal notranslate"><span class="pre">client_broker</span></code> encryption in transit is set to <code class="docutils literal notranslate"><span class="pre">PLAINTEXT</span></code> or <code class="docutils literal notranslate"><span class="pre">TLS_PLAINTEXT</span></code>.
:param pulumi.Input[str] bootstrap_brokers_tls: A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if <code class="docutils literal notranslate"><span class="pre">client_broker</span></code> encryption in transit is set to <code class="docutils literal notranslate"><span class="pre">TLS_PLAINTEXT</span></code> or <code class="docutils literal notranslate"><span class="pre">TLS</span></code>.
:param pulumi.Input[dict] broker_node_group_info: Configuration block for the broker nodes of the Kafka cluster.
:param pulumi.Input[dict] client_authentication: Configuration block for specifying a client authentication. See below.
:param pulumi.Input[str] cluster_name: Name of the MSK cluster.
:param pulumi.Input[dict] configuration_info: Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.
:param pulumi.Input[str] current_version: Current version of the MSK Cluster used for updates, e.g. <code class="docutils literal notranslate"><span class="pre">K13V1IB3VIYZZH</span></code></p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `encryption_info.0.encryption_at_rest_kms_key_arn` - The ARN of the KMS key used for encryption at rest of the broker data volumes.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>encryption_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for specifying encryption. See below.</p></li>
<li><p><strong>enhanced_monitoring</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specify the desired enhanced MSK CloudWatch monitoring level.  See <a class="reference external" href="https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html">Monitoring Amazon MSK with Amazon CloudWatch</a></p>
</p></li>
<li><p><strong>kafka_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the desired Kafka software version.</p></li>
<li><p><strong>number_of_broker_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource</p></li>
<li><p><strong>zookeeper_connect_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma separated list of one or more IP:port pairs to use to connect to the Apache Zookeeper cluster.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/msk_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/msk_cluster.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.msk.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.msk.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.msk.Configuration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.msk.</code><code class="sig-name descname">Configuration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">kafka_versions=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">server_properties=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Amazon Managed Streaming for Kafka configuration. More information can be found on the <a class="reference external" href="https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration.html">MSK Developer Guide</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The API does not support deleting MSK configurations. Removing this resource will only remove the this provider state for it.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the configuration.</p></li>
<li><p><strong>kafka_versions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Apache Kafka versions which can use this configuration.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the configuration.</p></li>
<li><p><strong>server_properties</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Contents of the server.properties file. Supported properties are documented in the <a class="reference external" href="https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html">MSK Developer Guide</a>.</p>
</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/msk_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/msk_configuration.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.msk.Configuration.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Configuration.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Configuration.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Configuration.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Configuration.kafka_versions">
<code class="sig-name descname">kafka_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Configuration.kafka_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Apache Kafka versions which can use this configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Configuration.latest_revision">
<code class="sig-name descname">latest_revision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Configuration.latest_revision" title="Permalink to this definition">¶</a></dt>
<dd><p>Latest revision of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Configuration.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Configuration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Configuration.server_properties">
<code class="sig-name descname">server_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Configuration.server_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>Contents of the server.properties file. Supported properties are documented in the <a class="reference external" href="https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html">MSK Developer Guide</a>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.msk.Configuration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">kafka_versions=None</em>, <em class="sig-param">latest_revision=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">server_properties=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Configuration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Configuration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: Amazon Resource Name (ARN) of the configuration.
:param pulumi.Input[str] description: Description of the configuration.
:param pulumi.Input[list] kafka_versions: List of Apache Kafka versions which can use this configuration.
:param pulumi.Input[float] latest_revision: Latest revision of the configuration.
:param pulumi.Input[str] name: Name of the configuration.
:param pulumi.Input[str] server_properties: Contents of the server.properties file. Supported properties are documented in the <a class="reference external" href="https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html">MSK Developer Guide</a>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/msk_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/msk_configuration.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.msk.Configuration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Configuration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.msk.Configuration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Configuration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.msk.GetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.msk.</code><code class="sig-name descname">GetClusterResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">bootstrap_brokers=None</em>, <em class="sig-param">bootstrap_brokers_tls=None</em>, <em class="sig-param">cluster_name=None</em>, <em class="sig-param">kafka_version=None</em>, <em class="sig-param">number_of_broker_nodes=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zookeeper_connect_string=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="attribute">
<dt id="pulumi_aws.msk.GetClusterResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the MSK cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetClusterResult.bootstrap_brokers">
<code class="sig-name descname">bootstrap_brokers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.bootstrap_brokers" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of one or more hostname:port pairs of Kafka brokers suitable to boostrap connectivity to the Kafka cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetClusterResult.bootstrap_brokers_tls">
<code class="sig-name descname">bootstrap_brokers_tls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.bootstrap_brokers_tls" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetClusterResult.kafka_version">
<code class="sig-name descname">kafka_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.kafka_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Apache Kafka version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetClusterResult.number_of_broker_nodes">
<code class="sig-name descname">number_of_broker_nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.number_of_broker_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of broker nodes in the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetClusterResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of key-value pairs assigned to the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetClusterResult.zookeeper_connect_string">
<code class="sig-name descname">zookeeper_connect_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.zookeeper_connect_string" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of one or more IP:port pairs to use to connect to the Apache Zookeeper cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetClusterResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.msk.GetConfigurationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.msk.</code><code class="sig-name descname">GetConfigurationResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">kafka_versions=None</em>, <em class="sig-param">latest_revision=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">server_properties=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getConfiguration.</p>
<dl class="attribute">
<dt id="pulumi_aws.msk.GetConfigurationResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetConfigurationResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetConfigurationResult.kafka_versions">
<code class="sig-name descname">kafka_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult.kafka_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Apache Kafka versions which can use this configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetConfigurationResult.latest_revision">
<code class="sig-name descname">latest_revision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult.latest_revision" title="Permalink to this definition">¶</a></dt>
<dd><p>Latest revision of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetConfigurationResult.server_properties">
<code class="sig-name descname">server_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult.server_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>Contents of the server.properties file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetConfigurationResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.msk.get_cluster">
<code class="sig-prename descclassname">pulumi_aws.msk.</code><code class="sig-name descname">get_cluster</code><span class="sig-paren">(</span><em class="sig-param">cluster_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on an Amazon MSK Cluster.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/msk_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/msk_cluster.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.msk.get_configuration">
<code class="sig-prename descclassname">pulumi_aws.msk.</code><code class="sig-name descname">get_configuration</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.get_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on an Amazon MSK Configuration.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/msk_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/msk_configuration.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
