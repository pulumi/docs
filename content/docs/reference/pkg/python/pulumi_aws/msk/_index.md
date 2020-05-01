---
title: Module msk
title_tag: Module msk | Package pulumi_aws | Python SDK
linktitle: msk
notitle: true
---

<div class="section" id="msk">
<h1>msk<a class="headerlink" href="#msk" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.msk"></span><dl class="py class">
<dt id="pulumi_aws.msk.AwaitableGetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.msk.</code><code class="sig-name descname">AwaitableGetClusterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootstrap_brokers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootstrap_brokers_tls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">number_of_broker_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zookeeper_connect_string</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.AwaitableGetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.msk.AwaitableGetConfigurationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.msk.</code><code class="sig-name descname">AwaitableGetConfigurationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_versions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latest_revision</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_properties</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.AwaitableGetConfigurationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.msk.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.msk.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">broker_node_group_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_authentication</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enhanced_monitoring</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">number_of_broker_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">open_monitoring</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Cluster" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>logging_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for streaming broker logs to Cloudwatch/S3/Kinesis Firehose. See below.</p></li>
<li><p><strong>number_of_broker_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.</p></li>
<li><p><strong>open_monitoring</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for JMX and Node monitoring for the MSK cluster. See below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource</p></li>
</ul>
</dd>
</dl>
<p>The <strong>broker_node_group_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">azDistribution</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The distribution of broker nodes across availability zones (<a class="reference external" href="https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#clusters-model-brokerazdistribution">documentation</a>). Currently the only valid value is <code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSubnets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of subnets to connect to in client VPC (<a class="reference external" href="https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#clusters-prop-brokernodegroupinfo-clientsubnets">documentation</a>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebsVolumeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size in GiB of the EBS volume for the data drive on each broker node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specify the instance type to use for the kafka brokers. e.g. kafka.m5.large. (<a class="reference external" href="https://aws.amazon.com/msk/pricing/">Pricing info</a>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of the security groups to associate with the elastic network interfaces to control who can communicate with the cluster.</p></li>
</ul>
<p>The <strong>client_authentication</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">tls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block for specifying TLS client authentication. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateAuthorityArns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of ACM Certificate Authority Amazon Resource Names (ARNs).</p></li>
</ul>
</li>
</ul>
<p>The <strong>configuration_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revision</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Revision of the MSK Configuration to use in the cluster.</p></li>
</ul>
<p>The <strong>encryption_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionAtRestKmsKeyArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - You may specify a KMS key short ID or ARN (it will always output an ARN) to use for encrypting your data at rest.  If no key is specified, an AWS managed KMS (‘aws/msk’ managed service) key will be used for encrypting the data at rest.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionInTransit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block to specify encryption in transit. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">clientBroker</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Encryption setting for data in transit between clients and brokers. Valid values: <code class="docutils literal notranslate"><span class="pre">TLS</span></code>, <code class="docutils literal notranslate"><span class="pre">TLS_PLAINTEXT</span></code>, and <code class="docutils literal notranslate"><span class="pre">PLAINTEXT</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">TLS_PLAINTEXT</span></code> when <code class="docutils literal notranslate"><span class="pre">encryption_in_transit</span></code> block defined, but <code class="docutils literal notranslate"><span class="pre">TLS</span></code> when <code class="docutils literal notranslate"><span class="pre">encryption_in_transit</span></code> block omitted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inCluster</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether data communication among broker nodes is encrypted. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>logging_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">brokerLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block for Broker Logs settings for logging info. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether you want to enable or disable streaming broker logs to Cloudwatch Logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the Cloudwatch Log Group to deliver logs to.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">firehose</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">deliveryStream</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the Kinesis Data Firehose delivery stream to deliver logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether you want to enable or disable streaming broker logs to Cloudwatch Logs.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the S3 bucket to deliver logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether you want to enable or disable streaming broker logs to Cloudwatch Logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Prefix to append to the folder name.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The <strong>open_monitoring</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block for Prometheus settings for open monitoring. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">jmxExporter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block for JMX Exporter. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabledInBroker</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether you want to enable or disable the JMX Exporter.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeExporter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block for Node Exporter. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabledInBroker</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether you want to enable or disable the JMX Exporter.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.msk.Cluster.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Cluster.bootstrap_brokers">
<code class="sig-name descname">bootstrap_brokers</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.bootstrap_brokers" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of one or more hostname:port pairs of kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if <code class="docutils literal notranslate"><span class="pre">client_broker</span></code> encryption in transit is set to <code class="docutils literal notranslate"><span class="pre">PLAINTEXT</span></code> or <code class="docutils literal notranslate"><span class="pre">TLS_PLAINTEXT</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Cluster.bootstrap_brokers_tls">
<code class="sig-name descname">bootstrap_brokers_tls</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.bootstrap_brokers_tls" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if <code class="docutils literal notranslate"><span class="pre">client_broker</span></code> encryption in transit is set to <code class="docutils literal notranslate"><span class="pre">TLS_PLAINTEXT</span></code> or <code class="docutils literal notranslate"><span class="pre">TLS</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Cluster.broker_node_group_info">
<code class="sig-name descname">broker_node_group_info</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.broker_node_group_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block for the broker nodes of the Kafka cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">azDistribution</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The distribution of broker nodes across availability zones (<a class="reference external" href="https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#clusters-model-brokerazdistribution">documentation</a>). Currently the only valid value is <code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSubnets</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of subnets to connect to in client VPC (<a class="reference external" href="https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#clusters-prop-brokernodegroupinfo-clientsubnets">documentation</a>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebsVolumeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size in GiB of the EBS volume for the data drive on each broker node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specify the instance type to use for the kafka brokers. e.g. kafka.m5.large. (<a class="reference external" href="https://aws.amazon.com/msk/pricing/">Pricing info</a>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_groups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of the security groups to associate with the elastic network interfaces to control who can communicate with the cluster.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Cluster.client_authentication">
<code class="sig-name descname">client_authentication</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.client_authentication" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block for specifying a client authentication. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">tls</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configuration block for specifying TLS client authentication. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateAuthorityArns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of ACM Certificate Authority Amazon Resource Names (ARNs).</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Cluster.cluster_name">
<code class="sig-name descname">cluster_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the MSK cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Cluster.configuration_info">
<code class="sig-name descname">configuration_info</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.configuration_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revision</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Revision of the MSK Configuration to use in the cluster.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Cluster.current_version">
<code class="sig-name descname">current_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.current_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Current version of the MSK Cluster used for updates, e.g. <code class="docutils literal notranslate"><span class="pre">K13V1IB3VIYZZH</span></code></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encryption_info.0.encryption_at_rest_kms_key_arn</span></code> - The ARN of the KMS key used for encryption at rest of the broker data volumes.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Cluster.encryption_info">
<code class="sig-name descname">encryption_info</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.encryption_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block for specifying encryption. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionAtRestKmsKeyArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - You may specify a KMS key short ID or ARN (it will always output an ARN) to use for encrypting your data at rest.  If no key is specified, an AWS managed KMS (‘aws/msk’ managed service) key will be used for encrypting the data at rest.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionInTransit</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configuration block to specify encryption in transit. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">clientBroker</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Encryption setting for data in transit between clients and brokers. Valid values: <code class="docutils literal notranslate"><span class="pre">TLS</span></code>, <code class="docutils literal notranslate"><span class="pre">TLS_PLAINTEXT</span></code>, and <code class="docutils literal notranslate"><span class="pre">PLAINTEXT</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">TLS_PLAINTEXT</span></code> when <code class="docutils literal notranslate"><span class="pre">encryption_in_transit</span></code> block defined, but <code class="docutils literal notranslate"><span class="pre">TLS</span></code> when <code class="docutils literal notranslate"><span class="pre">encryption_in_transit</span></code> block omitted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inCluster</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether data communication among broker nodes is encrypted. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Cluster.enhanced_monitoring">
<code class="sig-name descname">enhanced_monitoring</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.enhanced_monitoring" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the desired enhanced MSK CloudWatch monitoring level.  See <a class="reference external" href="https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html">Monitoring Amazon MSK with Amazon CloudWatch</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Cluster.kafka_version">
<code class="sig-name descname">kafka_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.kafka_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the desired Kafka software version.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Cluster.logging_info">
<code class="sig-name descname">logging_info</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.logging_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block for streaming broker logs to Cloudwatch/S3/Kinesis Firehose. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">brokerLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configuration block for Broker Logs settings for logging info. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether you want to enable or disable streaming broker logs to Cloudwatch Logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the Cloudwatch Log Group to deliver logs to.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">firehose</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">deliveryStream</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the Kinesis Data Firehose delivery stream to deliver logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether you want to enable or disable streaming broker logs to Cloudwatch Logs.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the S3 bucket to deliver logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether you want to enable or disable streaming broker logs to Cloudwatch Logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Prefix to append to the folder name.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Cluster.number_of_broker_nodes">
<code class="sig-name descname">number_of_broker_nodes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.number_of_broker_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Cluster.open_monitoring">
<code class="sig-name descname">open_monitoring</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.open_monitoring" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block for JMX and Node monitoring for the MSK cluster. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configuration block for Prometheus settings for open monitoring. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">jmxExporter</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configuration block for JMX Exporter. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabledInBroker</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether you want to enable or disable the JMX Exporter.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeExporter</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configuration block for Node Exporter. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabledInBroker</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether you want to enable or disable the JMX Exporter.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Cluster.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Cluster.zookeeper_connect_string">
<code class="sig-name descname">zookeeper_connect_string</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Cluster.zookeeper_connect_string" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of one or more hostname:port pairs to use to connect to the Apache Zookeeper cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.msk.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootstrap_brokers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootstrap_brokers_tls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">broker_node_group_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_authentication</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">current_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enhanced_monitoring</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logging_info</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">number_of_broker_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">open_monitoring</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zookeeper_connect_string</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.</p></li>
<li><p><strong>bootstrap_brokers</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma separated list of one or more hostname:port pairs of kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if <code class="docutils literal notranslate"><span class="pre">client_broker</span></code> encryption in transit is set to <code class="docutils literal notranslate"><span class="pre">PLAINTEXT</span></code> or <code class="docutils literal notranslate"><span class="pre">TLS_PLAINTEXT</span></code>.</p></li>
<li><p><strong>bootstrap_brokers_tls</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster. Only contains value if <code class="docutils literal notranslate"><span class="pre">client_broker</span></code> encryption in transit is set to <code class="docutils literal notranslate"><span class="pre">TLS_PLAINTEXT</span></code> or <code class="docutils literal notranslate"><span class="pre">TLS</span></code>.</p></li>
<li><p><strong>broker_node_group_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for the broker nodes of the Kafka cluster.</p></li>
<li><p><strong>client_authentication</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for specifying a client authentication. See below.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the MSK cluster.</p></li>
<li><p><strong>configuration_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for specifying a MSK Configuration to attach to Kafka brokers. See below.</p></li>
<li><p><strong>current_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Current version of the MSK Cluster used for updates, e.g. <code class="docutils literal notranslate"><span class="pre">K13V1IB3VIYZZH</span></code></p></li>
</ul>
</dd>
</dl>
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
<li><p><strong>logging_info</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for streaming broker logs to Cloudwatch/S3/Kinesis Firehose. See below.</p></li>
<li><p><strong>number_of_broker_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The desired total number of broker nodes in the kafka cluster.  It must be a multiple of the number of specified client subnets.</p></li>
<li><p><strong>open_monitoring</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block for JMX and Node monitoring for the MSK cluster. See below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource</p></li>
<li><p><strong>zookeeper_connect_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma separated list of one or more hostname:port pairs to use to connect to the Apache Zookeeper cluster.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>broker_node_group_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">azDistribution</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The distribution of broker nodes across availability zones (<a class="reference external" href="https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#clusters-model-brokerazdistribution">documentation</a>). Currently the only valid value is <code class="docutils literal notranslate"><span class="pre">DEFAULT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientSubnets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of subnets to connect to in client VPC (<a class="reference external" href="https://docs.aws.amazon.com/msk/1.0/apireference/clusters.html#clusters-prop-brokernodegroupinfo-clientsubnets">documentation</a>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebsVolumeSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size in GiB of the EBS volume for the data drive on each broker node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specify the instance type to use for the kafka brokers. e.g. kafka.m5.large. (<a class="reference external" href="https://aws.amazon.com/msk/pricing/">Pricing info</a>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_groups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of the security groups to associate with the elastic network interfaces to control who can communicate with the cluster.</p></li>
</ul>
<p>The <strong>client_authentication</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">tls</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block for specifying TLS client authentication. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateAuthorityArns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of ACM Certificate Authority Amazon Resource Names (ARNs).</p></li>
</ul>
</li>
</ul>
<p>The <strong>configuration_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amazon Resource Name (ARN) of the MSK Configuration to use in the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revision</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Revision of the MSK Configuration to use in the cluster.</p></li>
</ul>
<p>The <strong>encryption_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionAtRestKmsKeyArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - You may specify a KMS key short ID or ARN (it will always output an ARN) to use for encrypting your data at rest.  If no key is specified, an AWS managed KMS (‘aws/msk’ managed service) key will be used for encrypting the data at rest.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encryptionInTransit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block to specify encryption in transit. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">clientBroker</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Encryption setting for data in transit between clients and brokers. Valid values: <code class="docutils literal notranslate"><span class="pre">TLS</span></code>, <code class="docutils literal notranslate"><span class="pre">TLS_PLAINTEXT</span></code>, and <code class="docutils literal notranslate"><span class="pre">PLAINTEXT</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">TLS_PLAINTEXT</span></code> when <code class="docutils literal notranslate"><span class="pre">encryption_in_transit</span></code> block defined, but <code class="docutils literal notranslate"><span class="pre">TLS</span></code> when <code class="docutils literal notranslate"><span class="pre">encryption_in_transit</span></code> block omitted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inCluster</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether data communication among broker nodes is encrypted. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>logging_info</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">brokerLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block for Broker Logs settings for logging info. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchLogs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether you want to enable or disable streaming broker logs to Cloudwatch Logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_group</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the Cloudwatch Log Group to deliver logs to.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">firehose</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">deliveryStream</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the Kinesis Data Firehose delivery stream to deliver logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether you want to enable or disable streaming broker logs to Cloudwatch Logs.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">s3</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">bucket</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the S3 bucket to deliver logs to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether you want to enable or disable streaming broker logs to Cloudwatch Logs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Prefix to append to the folder name.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The <strong>open_monitoring</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">prometheus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block for Prometheus settings for open monitoring. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">jmxExporter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block for JMX Exporter. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabledInBroker</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether you want to enable or disable the JMX Exporter.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeExporter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block for Node Exporter. See below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabledInBroker</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether you want to enable or disable the JMX Exporter.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.msk.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.msk.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.msk.Configuration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.msk.</code><code class="sig-name descname">Configuration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_versions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Configuration" title="Permalink to this definition">¶</a></dt>
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
<dl class="py attribute">
<dt id="pulumi_aws.msk.Configuration.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Configuration.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Configuration.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Configuration.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Configuration.kafka_versions">
<code class="sig-name descname">kafka_versions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Configuration.kafka_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Apache Kafka versions which can use this configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Configuration.latest_revision">
<code class="sig-name descname">latest_revision</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Configuration.latest_revision" title="Permalink to this definition">¶</a></dt>
<dd><p>Latest revision of the configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Configuration.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Configuration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.Configuration.server_properties">
<code class="sig-name descname">server_properties</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.Configuration.server_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>Contents of the server.properties file. Supported properties are documented in the <a class="reference external" href="https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html">MSK Developer Guide</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.msk.Configuration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_versions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latest_revision</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_properties</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Configuration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Configuration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the configuration.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the configuration.</p></li>
<li><p><strong>kafka_versions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Apache Kafka versions which can use this configuration.</p></li>
<li><p><strong>latest_revision</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Latest revision of the configuration.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the configuration.</p></li>
<li><p><strong>server_properties</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Contents of the server.properties file. Supported properties are documented in the <a class="reference external" href="https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html">MSK Developer Guide</a>.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.msk.Configuration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Configuration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.msk.Configuration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.Configuration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.msk.GetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.msk.</code><code class="sig-name descname">GetClusterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootstrap_brokers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bootstrap_brokers_tls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">number_of_broker_nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zookeeper_connect_string</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="py attribute">
<dt id="pulumi_aws.msk.GetClusterResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the MSK cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.GetClusterResult.bootstrap_brokers">
<code class="sig-name descname">bootstrap_brokers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.bootstrap_brokers" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of one or more hostname:port pairs of Kafka brokers suitable to boostrap connectivity to the Kafka cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.GetClusterResult.bootstrap_brokers_tls">
<code class="sig-name descname">bootstrap_brokers_tls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.bootstrap_brokers_tls" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of one or more DNS names (or IPs) and TLS port pairs kafka brokers suitable to boostrap connectivity to the kafka cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.GetClusterResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.GetClusterResult.kafka_version">
<code class="sig-name descname">kafka_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.kafka_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Apache Kafka version.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.GetClusterResult.number_of_broker_nodes">
<code class="sig-name descname">number_of_broker_nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.number_of_broker_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of broker nodes in the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.GetClusterResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of key-value pairs assigned to the cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.GetClusterResult.zookeeper_connect_string">
<code class="sig-name descname">zookeeper_connect_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetClusterResult.zookeeper_connect_string" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma separated list of one or more hostname:port pairs to use to connect to the Apache Zookeeper cluster.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.msk.GetConfigurationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.msk.</code><code class="sig-name descname">GetConfigurationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kafka_versions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">latest_revision</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_properties</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getConfiguration.</p>
<dl class="py attribute">
<dt id="pulumi_aws.msk.GetConfigurationResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.GetConfigurationResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.GetConfigurationResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.GetConfigurationResult.kafka_versions">
<code class="sig-name descname">kafka_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult.kafka_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Apache Kafka versions which can use this configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.GetConfigurationResult.latest_revision">
<code class="sig-name descname">latest_revision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult.latest_revision" title="Permalink to this definition">¶</a></dt>
<dd><p>Latest revision of the configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.msk.GetConfigurationResult.server_properties">
<code class="sig-name descname">server_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.msk.GetConfigurationResult.server_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>Contents of the server.properties file.</p>
</dd></dl>

</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.msk.get_cluster">
<code class="sig-prename descclassname">pulumi_aws.msk.</code><code class="sig-name descname">get_cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on an Amazon MSK Cluster.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_name</strong> (<em>str</em>) – Name of the cluster.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – Map of key-value pairs assigned to the cluster.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.msk.get_configuration">
<code class="sig-prename descclassname">pulumi_aws.msk.</code><code class="sig-name descname">get_configuration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.msk.get_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on an Amazon MSK Configuration.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – Name of the configuration.</p>
</dd>
</dl>
</dd></dl>

</div>
