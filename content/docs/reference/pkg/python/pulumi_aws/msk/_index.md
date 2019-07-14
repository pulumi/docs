---
---

<div class="section" id="msk">
<h1>msk<a class="headerlink" href="#msk" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.msk"></span><dl class="class">
<dt id="pulumi_aws.msk.Cluster">
<em class="property">class </em><code class="descclassname">pulumi_aws.msk.</code><code class="descname">Cluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>broker_node_group_info=None</em>, <em>client_authentication=None</em>, <em>cluster_name=None</em>, <em>configuration_info=None</em>, <em>encryption_info=None</em>, <em>enhanced_monitoring=None</em>, <em>kafka_version=None</em>, <em>number_of_broker_nodes=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages AWS Managed Streaming for Kafka cluster</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>broker_node_group_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for the broker nodes of the Kafka cluster.</li>
<li><strong>client_authentication</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for specifying a client authentication. See below.</li>
<li><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the MSK cluster.</li>
<li><strong>configuration_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.</li>
<li><strong>encryption_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for specifying encryption. See below.</li>
<li><strong>enhanced_monitoring</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the desired enhanced MSK CloudWatch monitoring level.  See <a class="reference external" href="https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html">Monitoring Amazon MSK with Amazon CloudWatch</a></li>
<li><strong>kafka_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the desired Kafka software version.</li>
<li><strong>number_of_broker_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/msk_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/msk_cluster.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.bootstrap_brokers">
<code class="descname">bootstrap_brokers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.bootstrap_brokers" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of one or more hostname:port pairs of kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if <code class="docutils literal notranslate"><span class="pre">client_broker</span></code> encryption in transit is set to <code class="docutils literal notranslate"><span class="pre">PLAINTEXT</span></code> or <code class="docutils literal notranslate"><span class="pre">TLS_PLAINTEXT</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.bootstrap_brokers_tls">
<code class="descname">bootstrap_brokers_tls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.bootstrap_brokers_tls" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if <code class="docutils literal notranslate"><span class="pre">client_broker</span></code> encryption in transit is set to <code class="docutils literal notranslate"><span class="pre">TLS_PLAINTEXT</span></code> or <code class="docutils literal notranslate"><span class="pre">TLS</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.broker_node_group_info">
<code class="descname">broker_node_group_info</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.broker_node_group_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block for the broker nodes of the Kafka cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.client_authentication">
<code class="descname">client_authentication</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.client_authentication" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block for specifying a client authentication. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.cluster_name">
<code class="descname">cluster_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the MSK cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.configuration_info">
<code class="descname">configuration_info</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.configuration_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.current_version">
<code class="descname">current_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.current_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Current version of the MSK Cluster used for updates, e.g. <code class="docutils literal notranslate"><span class="pre">K13V1IB3VIYZZH</span></code></p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">encryption_info.0.encryption_at_rest_kms_key_arn</span></code> - The ARN of the KMS key used for encryption at rest of the broker data volumes.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.encryption_info">
<code class="descname">encryption_info</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.encryption_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block for specifying encryption. See below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.enhanced_monitoring">
<code class="descname">enhanced_monitoring</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.enhanced_monitoring" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the desired enhanced MSK CloudWatch monitoring level.  See <a class="reference external" href="https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html">Monitoring Amazon MSK with Amazon CloudWatch</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.kafka_version">
<code class="descname">kafka_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.kafka_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the desired Kafka software version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.number_of_broker_nodes">
<code class="descname">number_of_broker_nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.number_of_broker_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Cluster.zookeeper_connect_string">
<code class="descname">zookeeper_connect_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.zookeeper_connect_string" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of one or more IP:port pairs to use to connect to the Apache Zookeeper cluster.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.msk.Cluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.msk.Cluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.msk.Configuration">
<em class="property">class </em><code class="descclassname">pulumi_aws.msk.</code><code class="descname">Configuration</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>kafka_versions=None</em>, <em>name=None</em>, <em>server_properties=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Configuration resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the configuration.</li>
<li><strong>kafka_versions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Apache Kafka versions which can use this configuration.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the configuration.</li>
<li><strong>server_properties</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contents of the server.properties file. Supported properties are documented in the <a class="reference external" href="https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html">MSK Developer Guide</a>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/msk_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/msk_configuration.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.msk.Configuration.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Configuration.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Configuration.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Configuration.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Configuration.kafka_versions">
<code class="descname">kafka_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Configuration.kafka_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Apache Kafka versions which can use this configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Configuration.latest_revision">
<code class="descname">latest_revision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Configuration.latest_revision" title="Permalink to this definition">¶</a></dt>
<dd><p>Latest revision of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Configuration.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Configuration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.Configuration.server_properties">
<code class="descname">server_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Configuration.server_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>Contents of the server.properties file. Supported properties are documented in the <a class="reference external" href="https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html">MSK Developer Guide</a>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.msk.Configuration.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Configuration.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.msk.Configuration.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Configuration.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.msk.GetClusterResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.msk.</code><code class="descname">GetClusterResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>bootstrap_brokers=None</em>, <em>bootstrap_brokers_tls=None</em>, <em>cluster_name=None</em>, <em>kafka_version=None</em>, <em>number_of_broker_nodes=None</em>, <em>tags=None</em>, <em>zookeeper_connect_string=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="attribute">
<dt id="pulumi_aws.msk.GetClusterResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the MSK cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetClusterResult.bootstrap_brokers">
<code class="descname">bootstrap_brokers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.bootstrap_brokers" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of one or more hostname:port pairs of Kafka brokers suitable to boostrap connectivity to the Kafka cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetClusterResult.bootstrap_brokers_tls">
<code class="descname">bootstrap_brokers_tls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.bootstrap_brokers_tls" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetClusterResult.kafka_version">
<code class="descname">kafka_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.kafka_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Apache Kafka version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetClusterResult.number_of_broker_nodes">
<code class="descname">number_of_broker_nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.number_of_broker_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of broker nodes in the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetClusterResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of key-value pairs assigned to the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetClusterResult.zookeeper_connect_string">
<code class="descname">zookeeper_connect_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.zookeeper_connect_string" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of one or more IP:port pairs to use to connect to the Apache Zookeeper cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetClusterResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.msk.GetConfigurationResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.msk.</code><code class="descname">GetConfigurationResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>description=None</em>, <em>kafka_versions=None</em>, <em>latest_revision=None</em>, <em>name=None</em>, <em>server_properties=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getConfiguration.</p>
<dl class="attribute">
<dt id="pulumi_aws.msk.GetConfigurationResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetConfigurationResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetConfigurationResult.kafka_versions">
<code class="descname">kafka_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult.kafka_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Apache Kafka versions which can use this configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetConfigurationResult.latest_revision">
<code class="descname">latest_revision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult.latest_revision" title="Permalink to this definition">¶</a></dt>
<dd><p>Latest revision of the configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetConfigurationResult.server_properties">
<code class="descname">server_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult.server_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>Contents of the server.properties file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.msk.GetConfigurationResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.msk.get_cluster">
<code class="descclassname">pulumi_aws.msk.</code><code class="descname">get_cluster</code><span class="sig-paren">(</span><em>cluster_name=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on an Amazon MSK Cluster.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/msk_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/msk_cluster.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.msk.get_configuration">
<code class="descclassname">pulumi_aws.msk.</code><code class="descname">get_configuration</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.get_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on an Amazon MSK Configuration.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/msk_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/msk_configuration.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
