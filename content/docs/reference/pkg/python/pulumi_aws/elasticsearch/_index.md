---
title: Module elasticsearch
title_tag: Module elasticsearch | Package pulumi_aws | Python SDK
linktitle: elasticsearch
notitle: true
---

<div class="section" id="elasticsearch">
<h1>elasticsearch<a class="headerlink" href="#elasticsearch" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.elasticsearch"></span><dl class="class">
<dt id="pulumi_aws.elasticsearch.AwaitableGetDomainResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticsearch.</code><code class="sig-name descname">AwaitableGetDomainResult</code><span class="sig-paren">(</span><em class="sig-param">access_policies=None</em>, <em class="sig-param">advanced_options=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">cluster_configs=None</em>, <em class="sig-param">cognito_options=None</em>, <em class="sig-param">created=None</em>, <em class="sig-param">deleted=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">ebs_options=None</em>, <em class="sig-param">elasticsearch_version=None</em>, <em class="sig-param">encryption_at_rests=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">kibana_endpoint=None</em>, <em class="sig-param">log_publishing_options=None</em>, <em class="sig-param">node_to_node_encryptions=None</em>, <em class="sig-param">processing=None</em>, <em class="sig-param">snapshot_options=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpc_options=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticsearch.AwaitableGetDomainResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.elasticsearch.Domain">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticsearch.</code><code class="sig-name descname">Domain</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_policies=None</em>, <em class="sig-param">advanced_options=None</em>, <em class="sig-param">cluster_config=None</em>, <em class="sig-param">cognito_options=None</em>, <em class="sig-param">domain_endpoint_options=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">ebs_options=None</em>, <em class="sig-param">elasticsearch_version=None</em>, <em class="sig-param">encrypt_at_rest=None</em>, <em class="sig-param">log_publishing_options=None</em>, <em class="sig-param">node_to_node_encryption=None</em>, <em class="sig-param">snapshot_options=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpc_options=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS Elasticsearch Domain.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_policies</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – IAM policy document specifying the access policies for the domain</p></li>
<li><p><strong>advanced_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value string pairs to specify advanced configuration options.
Note that the values for these configuration options must be strings (wrapped in quotes) or they
may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
domain on every apply.</p></li>
<li><p><strong>cluster_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Cluster configuration of the domain, see below.</p></li>
<li><p><strong>domain_endpoint_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Domain endpoint HTTP(S) related options. See below.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the domain.</p></li>
<li><p><strong>ebs_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – EBS related options, may be required based on chosen <a class="reference external" href="https://aws.amazon.com/elasticsearch-service/pricing/">instance size</a>. See below.</p></li>
<li><p><strong>elasticsearch_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of Elasticsearch to deploy. Defaults to <code class="docutils literal notranslate"><span class="pre">1.5</span></code></p></li>
<li><p><strong>encrypt_at_rest</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Encrypt at rest options. Only available for <a class="reference external" href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html">certain instance types</a>. See below.</p></li>
<li><p><strong>log_publishing_options</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Options for publishing slow logs to CloudWatch Logs.</p></li>
<li><p><strong>node_to_node_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Node-to-node encryption options. See below.</p></li>
<li><p><strong>snapshot_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Snapshot related options, see below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource</p></li>
<li><p><strong>vpc_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – VPC related options, see below. Adding or removing this configuration forces a new resource (<a class="reference external" href="https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations">documentation</a>).</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cluster_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dedicatedMasterCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of dedicated master nodes in the cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dedicatedMasterEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether dedicated master nodes are enabled for the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dedicatedMasterType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Instance type of the dedicated master nodes in the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of instances in the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Instance type of data nodes in the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zoneAwarenessConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block containing zone awareness settings. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">availabilityZoneCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of Availability Zones for the domain to use with <code class="docutils literal notranslate"><span class="pre">zone_awareness_enabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">2</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">2</span></code> or <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zoneAwarenessEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether zone awareness is enabled, set to <code class="docutils literal notranslate"><span class="pre">true</span></code> for multi-az deployment. To enable awareness with three Availability Zones, the <code class="docutils literal notranslate"><span class="pre">availability_zone_count</span></code> within the <code class="docutils literal notranslate"><span class="pre">zone_awareness_config</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
</ul>
<p>The <strong>cognito_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether Amazon Cognito authentication with Kibana is enabled or not</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identity_pool_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the Cognito Identity Pool to use</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of the IAM role that has the AmazonESCognitoAccess policy attached</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_pool_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the Cognito User Pool to use</p></li>
</ul>
<p>The <strong>domain_endpoint_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enforceHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether or not to require HTTPS</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsSecurityPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the TLS security policy that needs to be applied to the HTTPS endpoint. Valid values:  <code class="docutils literal notranslate"><span class="pre">Policy-Min-TLS-1-0-2019-07</span></code> and <code class="docutils literal notranslate"><span class="pre">Policy-Min-TLS-1-2-2019-07</span></code>. This provider will only perform drift detection if a configuration value is provided.</p></li>
</ul>
<p>The <strong>ebs_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ebsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether EBS volumes are attached to data nodes in the domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The baseline input/output (I/O) performance of EBS volumes
attached to data nodes. Applicable only for the Provisioned IOPS EBS volume type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of EBS volumes attached to data nodes (in GB).
<strong>Required</strong> if <code class="docutils literal notranslate"><span class="pre">ebs_enabled</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of EBS volumes attached to data nodes.</p></li>
</ul>
<p>The <strong>encrypt_at_rest</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether Amazon Cognito authentication with Kibana is enabled or not</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The KMS key id to encrypt the Elasticsearch domain with. If not specified then it defaults to using the <code class="docutils literal notranslate"><span class="pre">aws/es</span></code> service KMS key.</p></li>
</ul>
<p>The <strong>log_publishing_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_log_group_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of the Cloudwatch log group to which log needs to be published.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether Amazon Cognito authentication with Kibana is enabled or not</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A type of Elasticsearch log. Valid values: INDEX_SLOW_LOGS, SEARCH_SLOW_LOGS, ES_APPLICATION_LOGS</p></li>
</ul>
<p>The <strong>node_to_node_encryption</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether Amazon Cognito authentication with Kibana is enabled or not</p></li>
</ul>
<p>The <strong>snapshot_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automatedSnapshotStartHour</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Hour during which the service takes an automated daily
snapshot of the indices in the domain.</p></li>
</ul>
<p>The <strong>vpc_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of VPC Security Group IDs to be applied to the Elasticsearch domain endpoints. If omitted, the default Security Group for the VPC will be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of VPC Subnet IDs for the Elasticsearch domain endpoints to be created in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.access_policies">
<code class="sig-name descname">access_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.access_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM policy document specifying the access policies for the domain</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.advanced_options">
<code class="sig-name descname">advanced_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.advanced_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value string pairs to specify advanced configuration options.
Note that the values for these configuration options must be strings (wrapped in quotes) or they
may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
domain on every apply.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.cluster_config">
<code class="sig-name descname">cluster_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.cluster_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Cluster configuration of the domain, see below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dedicatedMasterCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of dedicated master nodes in the cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dedicatedMasterEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether dedicated master nodes are enabled for the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dedicatedMasterType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Instance type of the dedicated master nodes in the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of instances in the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Instance type of data nodes in the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zoneAwarenessConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Configuration block containing zone awareness settings. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">availabilityZoneCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of Availability Zones for the domain to use with <code class="docutils literal notranslate"><span class="pre">zone_awareness_enabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">2</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">2</span></code> or <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zoneAwarenessEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether zone awareness is enabled, set to <code class="docutils literal notranslate"><span class="pre">true</span></code> for multi-az deployment. To enable awareness with three Availability Zones, the <code class="docutils literal notranslate"><span class="pre">availability_zone_count</span></code> within the <code class="docutils literal notranslate"><span class="pre">zone_awareness_config</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.domain_endpoint_options">
<code class="sig-name descname">domain_endpoint_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.domain_endpoint_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain endpoint HTTP(S) related options. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enforceHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether or not to require HTTPS</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsSecurityPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the TLS security policy that needs to be applied to the HTTPS endpoint. Valid values:  <code class="docutils literal notranslate"><span class="pre">Policy-Min-TLS-1-0-2019-07</span></code> and <code class="docutils literal notranslate"><span class="pre">Policy-Min-TLS-1-2-2019-07</span></code>. This provider will only perform drift detection if a configuration value is provided.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.domain_id">
<code class="sig-name descname">domain_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for the domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.domain_name">
<code class="sig-name descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.ebs_options">
<code class="sig-name descname">ebs_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.ebs_options" title="Permalink to this definition">¶</a></dt>
<dd><p>EBS related options, may be required based on chosen <a class="reference external" href="https://aws.amazon.com/elasticsearch-service/pricing/">instance size</a>. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ebsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether EBS volumes are attached to data nodes in the domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The baseline input/output (I/O) performance of EBS volumes
attached to data nodes. Applicable only for the Provisioned IOPS EBS volume type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of EBS volumes attached to data nodes (in GB).
<strong>Required</strong> if <code class="docutils literal notranslate"><span class="pre">ebs_enabled</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of EBS volumes attached to data nodes.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.elasticsearch_version">
<code class="sig-name descname">elasticsearch_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.elasticsearch_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of Elasticsearch to deploy. Defaults to <code class="docutils literal notranslate"><span class="pre">1.5</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.encrypt_at_rest">
<code class="sig-name descname">encrypt_at_rest</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.encrypt_at_rest" title="Permalink to this definition">¶</a></dt>
<dd><p>Encrypt at rest options. Only available for <a class="reference external" href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html">certain instance types</a>. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether Amazon Cognito authentication with Kibana is enabled or not</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The KMS key id to encrypt the Elasticsearch domain with. If not specified then it defaults to using the <code class="docutils literal notranslate"><span class="pre">aws/es</span></code> service KMS key.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain-specific endpoint used to submit index, search, and data upload requests.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.kibana_endpoint">
<code class="sig-name descname">kibana_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.kibana_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain-specific endpoint for kibana without https scheme.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_options.0.availability_zones</span></code> - If the domain was created inside a VPC, the names of the availability zones the configured <code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> were created inside.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_options.0.vpc_id</span></code> - If the domain was created inside a VPC, the ID of the VPC.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.log_publishing_options">
<code class="sig-name descname">log_publishing_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.log_publishing_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Options for publishing slow logs to CloudWatch Logs.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_log_group_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ARN of the Cloudwatch log group to which log needs to be published.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether Amazon Cognito authentication with Kibana is enabled or not</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A type of Elasticsearch log. Valid values: INDEX_SLOW_LOGS, SEARCH_SLOW_LOGS, ES_APPLICATION_LOGS</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.node_to_node_encryption">
<code class="sig-name descname">node_to_node_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.node_to_node_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Node-to-node encryption options. See below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether Amazon Cognito authentication with Kibana is enabled or not</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.snapshot_options">
<code class="sig-name descname">snapshot_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.snapshot_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Snapshot related options, see below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automatedSnapshotStartHour</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Hour during which the service takes an automated daily
snapshot of the indices in the domain.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.Domain.vpc_options">
<code class="sig-name descname">vpc_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.vpc_options" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC related options, see below. Adding or removing this configuration forces a new resource (<a class="reference external" href="https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations">documentation</a>).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of VPC Security Group IDs to be applied to the Elasticsearch domain endpoints. If omitted, the default Security Group for the VPC will be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of VPC Subnet IDs for the Elasticsearch domain endpoints to be created in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticsearch.Domain.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_policies=None</em>, <em class="sig-param">advanced_options=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">cluster_config=None</em>, <em class="sig-param">cognito_options=None</em>, <em class="sig-param">domain_endpoint_options=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">ebs_options=None</em>, <em class="sig-param">elasticsearch_version=None</em>, <em class="sig-param">encrypt_at_rest=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">kibana_endpoint=None</em>, <em class="sig-param">log_publishing_options=None</em>, <em class="sig-param">node_to_node_encryption=None</em>, <em class="sig-param">snapshot_options=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpc_options=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Domain resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_policies</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – IAM policy document specifying the access policies for the domain</p></li>
<li><p><strong>advanced_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value string pairs to specify advanced configuration options.
Note that the values for these configuration options must be strings (wrapped in quotes) or they
may be wrong and cause a perpetual diff, causing this provider to want to recreate your Elasticsearch
domain on every apply.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the domain.</p></li>
<li><p><strong>cluster_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Cluster configuration of the domain, see below.</p></li>
<li><p><strong>domain_endpoint_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Domain endpoint HTTP(S) related options. See below.</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for the domain.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the domain.</p></li>
<li><p><strong>ebs_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>EBS related options, may be required based on chosen <a class="reference external" href="https://aws.amazon.com/elasticsearch-service/pricing/">instance size</a>. See below.</p>
</p></li>
<li><p><strong>elasticsearch_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version of Elasticsearch to deploy. Defaults to <code class="docutils literal notranslate"><span class="pre">1.5</span></code></p></li>
<li><p><strong>encrypt_at_rest</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Encrypt at rest options. Only available for <a class="reference external" href="http://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/aes-supported-instance-types.html">certain instance types</a>. See below.</p>
</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain-specific endpoint used to submit index, search, and data upload requests.</p></li>
<li><p><strong>kibana_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain-specific endpoint for kibana without https scheme.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `vpc_options.0.availability_zones` - If the domain was created inside a VPC, the names of the availability zones the configured `subnet_ids` were created inside.
* `vpc_options.0.vpc_id` - If the domain was created inside a VPC, the ID of the VPC.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>log_publishing_options</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Options for publishing slow logs to CloudWatch Logs.</p></li>
<li><p><strong>node_to_node_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Node-to-node encryption options. See below.</p></li>
<li><p><strong>snapshot_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Snapshot related options, see below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource</p></li>
<li><p><strong>vpc_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>VPC related options, see below. Adding or removing this configuration forces a new resource (<a class="reference external" href="https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/es-vpc.html#es-vpc-limitations">documentation</a>).</p>
</p></li>
</ul>
</dd>
</dl>
<p>The <strong>cluster_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dedicatedMasterCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of dedicated master nodes in the cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dedicatedMasterEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether dedicated master nodes are enabled for the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dedicatedMasterType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Instance type of the dedicated master nodes in the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of instances in the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Instance type of data nodes in the cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zoneAwarenessConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Configuration block containing zone awareness settings. Documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">availabilityZoneCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of Availability Zones for the domain to use with <code class="docutils literal notranslate"><span class="pre">zone_awareness_enabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">2</span></code>. Valid values: <code class="docutils literal notranslate"><span class="pre">2</span></code> or <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">zoneAwarenessEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether zone awareness is enabled, set to <code class="docutils literal notranslate"><span class="pre">true</span></code> for multi-az deployment. To enable awareness with three Availability Zones, the <code class="docutils literal notranslate"><span class="pre">availability_zone_count</span></code> within the <code class="docutils literal notranslate"><span class="pre">zone_awareness_config</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
</ul>
<p>The <strong>cognito_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether Amazon Cognito authentication with Kibana is enabled or not</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">identity_pool_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the Cognito Identity Pool to use</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of the IAM role that has the AmazonESCognitoAccess policy attached</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_pool_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the Cognito User Pool to use</p></li>
</ul>
<p>The <strong>domain_endpoint_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enforceHttps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether or not to require HTTPS</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tlsSecurityPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the TLS security policy that needs to be applied to the HTTPS endpoint. Valid values:  <code class="docutils literal notranslate"><span class="pre">Policy-Min-TLS-1-0-2019-07</span></code> and <code class="docutils literal notranslate"><span class="pre">Policy-Min-TLS-1-2-2019-07</span></code>. This provider will only perform drift detection if a configuration value is provided.</p></li>
</ul>
<p>The <strong>ebs_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ebsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether EBS volumes are attached to data nodes in the domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The baseline input/output (I/O) performance of EBS volumes
attached to data nodes. Applicable only for the Provisioned IOPS EBS volume type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volume_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of EBS volumes attached to data nodes (in GB).
<strong>Required</strong> if <code class="docutils literal notranslate"><span class="pre">ebs_enabled</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of EBS volumes attached to data nodes.</p></li>
</ul>
<p>The <strong>encrypt_at_rest</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether Amazon Cognito authentication with Kibana is enabled or not</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The KMS key id to encrypt the Elasticsearch domain with. If not specified then it defaults to using the <code class="docutils literal notranslate"><span class="pre">aws/es</span></code> service KMS key.</p></li>
</ul>
<p>The <strong>log_publishing_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatch_log_group_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ARN of the Cloudwatch log group to which log needs to be published.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether Amazon Cognito authentication with Kibana is enabled or not</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A type of Elasticsearch log. Valid values: INDEX_SLOW_LOGS, SEARCH_SLOW_LOGS, ES_APPLICATION_LOGS</p></li>
</ul>
<p>The <strong>node_to_node_encryption</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether Amazon Cognito authentication with Kibana is enabled or not</p></li>
</ul>
<p>The <strong>snapshot_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">automatedSnapshotStartHour</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Hour during which the service takes an automated daily
snapshot of the indices in the domain.</p></li>
</ul>
<p>The <strong>vpc_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of VPC Security Group IDs to be applied to the Elasticsearch domain endpoints. If omitted, the default Security Group for the VPC will be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of VPC Subnet IDs for the Elasticsearch domain endpoints to be created in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticsearch.Domain.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.elasticsearch.Domain.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticsearch.Domain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.elasticsearch.DomainPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticsearch.</code><code class="sig-name descname">DomainPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_policies=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticsearch.DomainPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows setting policy to an Elasticsearch domain while referencing domain attributes (e.g. ARN)</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_policies</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – IAM policy document specifying the access policies for the domain</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the domain.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.DomainPolicy.access_policies">
<code class="sig-name descname">access_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.DomainPolicy.access_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM policy document specifying the access policies for the domain</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.DomainPolicy.domain_name">
<code class="sig-name descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.DomainPolicy.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the domain.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticsearch.DomainPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_policies=None</em>, <em class="sig-param">domain_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticsearch.DomainPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DomainPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_policies</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – IAM policy document specifying the access policies for the domain</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the domain.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.elasticsearch.DomainPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticsearch.DomainPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.elasticsearch.DomainPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticsearch.DomainPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.elasticsearch.GetDomainResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.elasticsearch.</code><code class="sig-name descname">GetDomainResult</code><span class="sig-paren">(</span><em class="sig-param">access_policies=None</em>, <em class="sig-param">advanced_options=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">cluster_configs=None</em>, <em class="sig-param">cognito_options=None</em>, <em class="sig-param">created=None</em>, <em class="sig-param">deleted=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">domain_name=None</em>, <em class="sig-param">ebs_options=None</em>, <em class="sig-param">elasticsearch_version=None</em>, <em class="sig-param">encryption_at_rests=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">kibana_endpoint=None</em>, <em class="sig-param">log_publishing_options=None</em>, <em class="sig-param">node_to_node_encryptions=None</em>, <em class="sig-param">processing=None</em>, <em class="sig-param">snapshot_options=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpc_options=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDomain.</p>
<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.access_policies">
<code class="sig-name descname">access_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.access_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy document attached to the domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.advanced_options">
<code class="sig-name descname">advanced_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.advanced_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value string pairs to specify advanced configuration options.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.cluster_configs">
<code class="sig-name descname">cluster_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.cluster_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>Cluster configuration of the domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.cognito_options">
<code class="sig-name descname">cognito_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.cognito_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain Amazon Cognito Authentication options for Kibana.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.created">
<code class="sig-name descname">created</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.created" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the creation of the domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.deleted">
<code class="sig-name descname">deleted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.deleted" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the deletion of the domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.domain_id">
<code class="sig-name descname">domain_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for the domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.ebs_options">
<code class="sig-name descname">ebs_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.ebs_options" title="Permalink to this definition">¶</a></dt>
<dd><p>EBS Options for the instances in the domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.elasticsearch_version">
<code class="sig-name descname">elasticsearch_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.elasticsearch_version" title="Permalink to this definition">¶</a></dt>
<dd><p>ElasticSearch version for the domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.encryption_at_rests">
<code class="sig-name descname">encryption_at_rests</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.encryption_at_rests" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain encryption at rest related options.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain-specific endpoint used to submit index, search, and data upload requests.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.kibana_endpoint">
<code class="sig-name descname">kibana_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.kibana_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain-specific endpoint used to access the Kibana application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.log_publishing_options">
<code class="sig-name descname">log_publishing_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.log_publishing_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain log publishing related options.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.node_to_node_encryptions">
<code class="sig-name descname">node_to_node_encryptions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.node_to_node_encryptions" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain in transit encryption related options.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.processing">
<code class="sig-name descname">processing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.processing" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of a configuration change in the domain.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_options</span></code> – Domain snapshot related options.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The tags assigned to the domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.elasticsearch.GetDomainResult.vpc_options">
<code class="sig-name descname">vpc_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.elasticsearch.GetDomainResult.vpc_options" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC Options for private Elasticsearch domains.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.elasticsearch.get_domain">
<code class="sig-prename descclassname">pulumi_aws.elasticsearch.</code><code class="sig-name descname">get_domain</code><span class="sig-paren">(</span><em class="sig-param">domain_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.elasticsearch.get_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about an Elasticsearch Domain</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain_name</strong> (<em>str</em>) – Name of the domain.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – The tags assigned to the domain.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
