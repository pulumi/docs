---
title: Module mongodb
title_tag: Module mongodb | Package pulumi_alicloud | Python SDK
linktitle: mongodb
notitle: true
---

<div class="section" id="mongodb">
<h1>mongodb<a class="headerlink" href="#mongodb" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.mongodb"></span><dl class="class">
<dt id="pulumi_alicloud.mongodb.AwaitableGetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.mongodb.</code><code class="sig-name descname">AwaitableGetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param">availability_zone=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instance_class=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mongodb.AwaitableGetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.mongodb.AwaitableGetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.mongodb.</code><code class="sig-name descname">AwaitableGetZonesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">multi=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mongodb.AwaitableGetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.mongodb.GetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.mongodb.</code><code class="sig-name descname">GetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param">availability_zone=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instance_class=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mongodb.GetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstances.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.GetInstancesResult.availability_zone">
<code class="sig-name descname">availability_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.GetInstancesResult.availability_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance availability zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.GetInstancesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.GetInstancesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.GetInstancesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.GetInstancesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The ids list of MongoDB instances</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.GetInstancesResult.instance_class">
<code class="sig-name descname">instance_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.GetInstancesResult.instance_class" title="Permalink to this definition">¶</a></dt>
<dd><p>Sizing of the MongoDB instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.GetInstancesResult.instance_type">
<code class="sig-name descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.GetInstancesResult.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance type. Optional values <code class="docutils literal notranslate"><span class="pre">sharding</span></code> or <code class="docutils literal notranslate"><span class="pre">replicate</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.GetInstancesResult.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.GetInstancesResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of MongoDB instances. Its every element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.GetInstancesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.GetInstancesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>The names list of MongoDB instances</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.mongodb.GetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.mongodb.</code><code class="sig-name descname">GetZonesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">multi=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mongodb.GetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZones.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.GetZonesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.GetZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.GetZonesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.GetZonesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of zone IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.GetZonesResult.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.GetZonesResult.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of availability zones. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.mongodb.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.mongodb.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_password=None</em>, <em class="sig-param">backup_periods=None</em>, <em class="sig-param">backup_time=None</em>, <em class="sig-param">db_instance_class=None</em>, <em class="sig-param">db_instance_storage=None</em>, <em class="sig-param">engine_version=None</em>, <em class="sig-param">instance_charge_type=None</em>, <em class="sig-param">kms_encrypted_password=None</em>, <em class="sig-param">kms_encryption_context=None</em>, <em class="sig-param">maintain_end_time=None</em>, <em class="sig-param">maintain_start_time=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">replication_factor=None</em>, <em class="sig-param">security_group_id=None</em>, <em class="sig-param">security_ip_lists=None</em>, <em class="sig-param">ssl_action=None</em>, <em class="sig-param">storage_engine=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tde_status=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Instance resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] account_password: Password of the root account. It is a string of 6 to 32 characters and is composed of letters, numbers, and underlines.
:param pulumi.Input[list] backup_periods: MongoDB Instance backup period. It is required when <code class="docutils literal notranslate"><span class="pre">backup_time</span></code> was existed. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
:param pulumi.Input[str] backup_time: MongoDB instance backup time. It is required when <code class="docutils literal notranslate"><span class="pre">backup_period</span></code> was existed. In the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. If not set, the system will return a default, like “23:00Z-24:00Z”.
:param pulumi.Input[str] db_instance_class: Instance specification. see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/57141.htm">Instance specifications</a>.
:param pulumi.Input[float] db_instance_storage: User-defined DB instance storage space.Unit: GB. Value range:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Custom</span> <span class="n">storage</span> <span class="n">space</span><span class="p">;</span> <span class="n">value</span> <span class="nb">range</span><span class="p">:</span> <span class="p">[</span><span class="mi">10</span><span class="p">,</span><span class="mi">2000</span><span class="p">]</span>
<span class="o">-</span> <span class="mi">10</span><span class="o">-</span><span class="n">GB</span> <span class="n">increments</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database version. Value options can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/61763.htm">CreateDBInstance</a> <code class="docutils literal notranslate"><span class="pre">EngineVersion</span></code>.</p></li>
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, System default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. It can be modified from <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code> to <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> after version 1.63.0.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to a instance. If the <code class="docutils literal notranslate"><span class="pre">account_password</span></code> is filled in, this field will be ignored.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating instance with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p></li>
<li><p><strong>maintain_end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The end time of the operation and maintenance time period of the instance, in the format of HH:mmZ (UTC time).</p></li>
<li><p><strong>maintain_start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The start time of the operation and maintenance time period of the instance, in the format of HH:mmZ (UTC time).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of DB instance. It a string of 2 to 256 characters.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy DB instance (in month). It is valid when instance_charge_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid values: [1~9], 12, 24, 36. System default to 1.</p></li>
<li><p><strong>replication_factor</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of replica set nodes. Valid values: [3, 5, 7]</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `storage_engine` (Optional, ForceNew) Storage engine: WiredTiger or RocksDB. System Default value: WiredTiger.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Security Group ID of ECS.</p></li>
<li><p><strong>security_ip_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).</p></li>
<li><p><strong>ssl_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Actions performed on SSL functions, Valid values: <cite>Open</cite>: turn on SSL encryption; <cite>Close</cite>: turn off SSL encryption; <code class="docutils literal notranslate"><span class="pre">Update</span></code>: update SSL certificate.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>tde_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TDE(Transparent Data Encryption) status.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The virtual switch ID to launch DB instances in one VPC.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the DB instance. it supports multiple zone.
If it is a multi-zone and <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> is specified, the vswitch must in one of them.
The multiple zone ID can be retrieved by setting <code class="docutils literal notranslate"><span class="pre">multi</span></code> to “true” in the data source <code class="docutils literal notranslate"><span class="pre">.getZones</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.account_password">
<code class="sig-name descname">account_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.account_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password of the root account. It is a string of 6 to 32 characters and is composed of letters, numbers, and underlines.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.backup_periods">
<code class="sig-name descname">backup_periods</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.backup_periods" title="Permalink to this definition">¶</a></dt>
<dd><p>MongoDB Instance backup period. It is required when <code class="docutils literal notranslate"><span class="pre">backup_time</span></code> was existed. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.backup_time">
<code class="sig-name descname">backup_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.backup_time" title="Permalink to this definition">¶</a></dt>
<dd><p>MongoDB instance backup time. It is required when <code class="docutils literal notranslate"><span class="pre">backup_period</span></code> was existed. In the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. If not set, the system will return a default, like “23:00Z-24:00Z”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.db_instance_class">
<code class="sig-name descname">db_instance_class</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.db_instance_class" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance specification. see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/57141.htm">Instance specifications</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.db_instance_storage">
<code class="sig-name descname">db_instance_storage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.db_instance_storage" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined DB instance storage space.Unit: GB. Value range:</p>
<ul class="simple">
<li><p>Custom storage space; value range: [10,2000]</p></li>
<li><p>10-GB increments.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.engine_version">
<code class="sig-name descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Database version. Value options can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/61763.htm">CreateDBInstance</a> <code class="docutils literal notranslate"><span class="pre">EngineVersion</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.instance_charge_type">
<code class="sig-name descname">instance_charge_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.instance_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, System default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. It can be modified from <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code> to <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> after version 1.63.0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.kms_encrypted_password">
<code class="sig-name descname">kms_encrypted_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.kms_encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encrypts password used to a instance. If the <code class="docutils literal notranslate"><span class="pre">account_password</span></code> is filled in, this field will be ignored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.kms_encryption_context">
<code class="sig-name descname">kms_encryption_context</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.kms_encryption_context" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating instance with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.maintain_end_time">
<code class="sig-name descname">maintain_end_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.maintain_end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The end time of the operation and maintenance time period of the instance, in the format of HH:mmZ (UTC time).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.maintain_start_time">
<code class="sig-name descname">maintain_start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.maintain_start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The start time of the operation and maintenance time period of the instance, in the format of HH:mmZ (UTC time).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of DB instance. It a string of 2 to 256 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration that you will buy DB instance (in month). It is valid when instance_charge_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid values: [1~9], 12, 24, 36. System default to 1.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.replica_set_name">
<code class="sig-name descname">replica_set_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.replica_set_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the mongo replica set</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.replication_factor">
<code class="sig-name descname">replication_factor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.replication_factor" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of replica set nodes. Valid values: [3, 5, 7]</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storage_engine</span></code> (Optional, ForceNew) Storage engine: WiredTiger or RocksDB. System Default value: WiredTiger.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.retention_period">
<code class="sig-name descname">retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance log backup retention days. Available in 1.42.0+.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Security Group ID of ECS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.security_ip_lists">
<code class="sig-name descname">security_ip_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.security_ip_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.ssl_action">
<code class="sig-name descname">ssl_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.ssl_action" title="Permalink to this definition">¶</a></dt>
<dd><p>Actions performed on SSL functions, Valid values: <cite>Open</cite>: turn on SSL encryption; <cite>Close</cite>: turn off SSL encryption; <code class="docutils literal notranslate"><span class="pre">Update</span></code>: update SSL certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.ssl_status">
<code class="sig-name descname">ssl_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.ssl_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the SSL feature. <cite>Open</cite>: SSL is turned on; <cite>Closed</cite>: SSL is turned off.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.tde_status">
<code class="sig-name descname">tde_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.tde_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The TDE(Transparent Data Encryption) status.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual switch ID to launch DB instances in one VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.Instance.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Zone to launch the DB instance. it supports multiple zone.
If it is a multi-zone and <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> is specified, the vswitch must in one of them.
The multiple zone ID can be retrieved by setting <code class="docutils literal notranslate"><span class="pre">multi</span></code> to “true” in the data source <code class="docutils literal notranslate"><span class="pre">.getZones</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.mongodb.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_password=None</em>, <em class="sig-param">backup_periods=None</em>, <em class="sig-param">backup_time=None</em>, <em class="sig-param">db_instance_class=None</em>, <em class="sig-param">db_instance_storage=None</em>, <em class="sig-param">engine_version=None</em>, <em class="sig-param">instance_charge_type=None</em>, <em class="sig-param">kms_encrypted_password=None</em>, <em class="sig-param">kms_encryption_context=None</em>, <em class="sig-param">maintain_end_time=None</em>, <em class="sig-param">maintain_start_time=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">replica_set_name=None</em>, <em class="sig-param">replication_factor=None</em>, <em class="sig-param">retention_period=None</em>, <em class="sig-param">security_group_id=None</em>, <em class="sig-param">security_ip_lists=None</em>, <em class="sig-param">ssl_action=None</em>, <em class="sig-param">ssl_status=None</em>, <em class="sig-param">storage_engine=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tde_status=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password of the root account. It is a string of 6 to 32 characters and is composed of letters, numbers, and underlines.</p></li>
<li><p><strong>backup_periods</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – MongoDB Instance backup period. It is required when <code class="docutils literal notranslate"><span class="pre">backup_time</span></code> was existed. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]</p></li>
<li><p><strong>backup_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – MongoDB instance backup time. It is required when <code class="docutils literal notranslate"><span class="pre">backup_period</span></code> was existed. In the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. If not set, the system will return a default, like “23:00Z-24:00Z”.</p></li>
<li><p><strong>db_instance_class</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Instance specification. see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/57141.htm">Instance specifications</a>.</p>
</p></li>
<li><p><strong>db_instance_storage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – User-defined DB instance storage space.Unit: GB. Value range:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Custom</span> <span class="n">storage</span> <span class="n">space</span><span class="p">;</span> <span class="n">value</span> <span class="nb">range</span><span class="p">:</span> <span class="p">[</span><span class="mi">10</span><span class="p">,</span><span class="mi">2000</span><span class="p">]</span>
<span class="o">-</span> <span class="mi">10</span><span class="o">-</span><span class="n">GB</span> <span class="n">increments</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Database version. Value options can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/61763.htm">CreateDBInstance</a> <code class="docutils literal notranslate"><span class="pre">EngineVersion</span></code>.</p>
</p></li>
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, System default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. It can be modified from <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code> to <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> after version 1.63.0.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to a instance. If the <code class="docutils literal notranslate"><span class="pre">account_password</span></code> is filled in, this field will be ignored.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating instance with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</p></li>
<li><p><strong>maintain_end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The end time of the operation and maintenance time period of the instance, in the format of HH:mmZ (UTC time).</p></li>
<li><p><strong>maintain_start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The start time of the operation and maintenance time period of the instance, in the format of HH:mmZ (UTC time).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of DB instance. It a string of 2 to 256 characters.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy DB instance (in month). It is valid when instance_charge_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid values: [1~9], 12, 24, 36. System default to 1.</p></li>
<li><p><strong>replica_set_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the mongo replica set</p></li>
<li><p><strong>replication_factor</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of replica set nodes. Valid values: [3, 5, 7]</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `storage_engine` (Optional, ForceNew) Storage engine: WiredTiger or RocksDB. System Default value: WiredTiger.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance log backup retention days. Available in 1.42.0+.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Security Group ID of ECS.</p></li>
<li><p><strong>security_ip_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).</p></li>
<li><p><strong>ssl_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Actions performed on SSL functions, Valid values: <cite>Open</cite>: turn on SSL encryption; <cite>Close</cite>: turn off SSL encryption; <code class="docutils literal notranslate"><span class="pre">Update</span></code>: update SSL certificate.</p></li>
<li><p><strong>ssl_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the SSL feature. <cite>Open</cite>: SSL is turned on; <cite>Closed</cite>: SSL is turned off.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>tde_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TDE(Transparent Data Encryption) status.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The virtual switch ID to launch DB instances in one VPC.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the DB instance. it supports multiple zone.
If it is a multi-zone and <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> is specified, the vswitch must in one of them.
The multiple zone ID can be retrieved by setting <code class="docutils literal notranslate"><span class="pre">multi</span></code> to “true” in the data source <code class="docutils literal notranslate"><span class="pre">.getZones</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.mongodb.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.mongodb.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mongodb.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.mongodb.ShardingInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.mongodb.</code><code class="sig-name descname">ShardingInstance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_password=None</em>, <em class="sig-param">backup_periods=None</em>, <em class="sig-param">backup_time=None</em>, <em class="sig-param">engine_version=None</em>, <em class="sig-param">instance_charge_type=None</em>, <em class="sig-param">kms_encrypted_password=None</em>, <em class="sig-param">kms_encryption_context=None</em>, <em class="sig-param">mongo_lists=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">security_group_id=None</em>, <em class="sig-param">security_ip_lists=None</em>, <em class="sig-param">shard_lists=None</em>, <em class="sig-param">storage_engine=None</em>, <em class="sig-param">tde_status=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ShardingInstance resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] account_password: Password of the root account. It is a string of 6 to 32 characters and is composed of letters, numbers, and underlines.
:param pulumi.Input[list] backup_periods: MongoDB Instance backup period. It is required when <code class="docutils literal notranslate"><span class="pre">backup_time</span></code> was existed. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]
:param pulumi.Input[str] backup_time: MongoDB instance backup time. It is required when <code class="docutils literal notranslate"><span class="pre">backup_period</span></code> was existed. In the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. If not set, the system will return a default, like “23:00Z-24:00Z”.
:param pulumi.Input[str] engine_version: Database version. Value options can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/zh/doc-detail/61884.htm">CreateDBInstance</a> <code class="docutils literal notranslate"><span class="pre">EngineVersion</span></code>.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `storage_engine` (Optional, ForceNew) Storage engine: WiredTiger or RocksDB. System Default value: WiredTiger.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>,System default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to a instance. If the <code class="docutils literal notranslate"><span class="pre">account_password</span></code> is filled in, this field will be ignored.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating instance with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</p></li>
<li><p><strong>mongo_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The mongo-node count can be purchased is in range of [2, 32].</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `node_class` -(Required) Node specification. see [Instance specifications](https://www.alibabacloud.com/help/doc-detail/57141.htm).
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of DB instance. It a string of 2 to 256 characters.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy DB instance (in month). It is valid when instance_charge_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid values: [1~9], 12, 24, 36. System default to 1.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Security Group ID of ECS.</p></li>
<li><p><strong>security_ip_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]). System default to <code class="docutils literal notranslate"><span class="pre">[&quot;127.0.0.1&quot;]</span></code>.</p></li>
<li><p><strong>shard_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – the shard-node count can be purchased is in range of [2, 32].</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `node_class` -(Required) Node specification. see [Instance specifications](https://www.alibabacloud.com/help/doc-detail/57141.htm).
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>tde_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TDE(Transparent Data Encryption) status.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The virtual switch ID to launch DB instances in one VPC.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the DB instance. MongoDB sharding instance does not support multiple-zone.
If it is a multi-zone and <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> is specified, the vswitch must in one of them.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>mongo_lists</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Mongo node connection string</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeClass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the shard-node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Mongo node port</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">shard_list</span></code></p></li>
</ul>
</li>
</ul>
<p>The <strong>shard_lists</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">nodeClass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the shard-node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeStorage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) -</p>
<ul>
<li><p>Custom storage space; value range: [10, 1,000]</p></li>
<li><p>10-GB increments. Unit: GB.</p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.account_password">
<code class="sig-name descname">account_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.account_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password of the root account. It is a string of 6 to 32 characters and is composed of letters, numbers, and underlines.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.backup_periods">
<code class="sig-name descname">backup_periods</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.backup_periods" title="Permalink to this definition">¶</a></dt>
<dd><p>MongoDB Instance backup period. It is required when <code class="docutils literal notranslate"><span class="pre">backup_time</span></code> was existed. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.backup_time">
<code class="sig-name descname">backup_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.backup_time" title="Permalink to this definition">¶</a></dt>
<dd><p>MongoDB instance backup time. It is required when <code class="docutils literal notranslate"><span class="pre">backup_period</span></code> was existed. In the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. If not set, the system will return a default, like “23:00Z-24:00Z”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.engine_version">
<code class="sig-name descname">engine_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Database version. Value options can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/zh/doc-detail/61884.htm">CreateDBInstance</a> <code class="docutils literal notranslate"><span class="pre">EngineVersion</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storage_engine</span></code> (Optional, ForceNew) Storage engine: WiredTiger or RocksDB. System Default value: WiredTiger.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.instance_charge_type">
<code class="sig-name descname">instance_charge_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.instance_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>,System default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.kms_encrypted_password">
<code class="sig-name descname">kms_encrypted_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.kms_encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encrypts password used to a instance. If the <code class="docutils literal notranslate"><span class="pre">account_password</span></code> is filled in, this field will be ignored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.kms_encryption_context">
<code class="sig-name descname">kms_encryption_context</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.kms_encryption_context" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating instance with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.mongo_lists">
<code class="sig-name descname">mongo_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.mongo_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>The mongo-node count can be purchased is in range of [2, 32].</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">node_class</span></code> -(Required) Node specification. see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/57141.htm">Instance specifications</a>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">connectString</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Mongo node connection string</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeClass</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the shard-node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Mongo node port</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">shard_list</span></code></p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of DB instance. It a string of 2 to 256 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration that you will buy DB instance (in month). It is valid when instance_charge_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid values: [1~9], 12, 24, 36. System default to 1.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.retention_period">
<code class="sig-name descname">retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance log backup retention days. Available in 1.42.0+.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Security Group ID of ECS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.security_ip_lists">
<code class="sig-name descname">security_ip_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.security_ip_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]). System default to <code class="docutils literal notranslate"><span class="pre">[&quot;127.0.0.1&quot;]</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.shard_lists">
<code class="sig-name descname">shard_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.shard_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>the shard-node count can be purchased is in range of [2, 32].</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">node_class</span></code> -(Required) Node specification. see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/57141.htm">Instance specifications</a>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeClass</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the shard-node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeStorage</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) -</p>
<ul>
<li><p>Custom storage space; value range: [10, 1,000]</p></li>
<li><p>10-GB increments. Unit: GB.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.tde_status">
<code class="sig-name descname">tde_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.tde_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The TDE(Transparent Data Encryption) status.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual switch ID to launch DB instances in one VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Zone to launch the DB instance. MongoDB sharding instance does not support multiple-zone.
If it is a multi-zone and <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> is specified, the vswitch must in one of them.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_password=None</em>, <em class="sig-param">backup_periods=None</em>, <em class="sig-param">backup_time=None</em>, <em class="sig-param">engine_version=None</em>, <em class="sig-param">instance_charge_type=None</em>, <em class="sig-param">kms_encrypted_password=None</em>, <em class="sig-param">kms_encryption_context=None</em>, <em class="sig-param">mongo_lists=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">retention_period=None</em>, <em class="sig-param">security_group_id=None</em>, <em class="sig-param">security_ip_lists=None</em>, <em class="sig-param">shard_lists=None</em>, <em class="sig-param">storage_engine=None</em>, <em class="sig-param">tde_status=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ShardingInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password of the root account. It is a string of 6 to 32 characters and is composed of letters, numbers, and underlines.</p></li>
<li><p><strong>backup_periods</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – MongoDB Instance backup period. It is required when <code class="docutils literal notranslate"><span class="pre">backup_time</span></code> was existed. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]</p></li>
<li><p><strong>backup_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – MongoDB instance backup time. It is required when <code class="docutils literal notranslate"><span class="pre">backup_period</span></code> was existed. In the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. If not set, the system will return a default, like “23:00Z-24:00Z”.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Database version. Value options can refer to the latest docs <a class="reference external" href="https://www.alibabacloud.com/help/zh/doc-detail/61884.htm">CreateDBInstance</a> <code class="docutils literal notranslate"><span class="pre">EngineVersion</span></code>.</p>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `storage_engine` (Optional, ForceNew) Storage engine: WiredTiger or RocksDB. System Default value: WiredTiger.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>,System default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to a instance. If the <code class="docutils literal notranslate"><span class="pre">account_password</span></code> is filled in, this field will be ignored.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating instance with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</p></li>
<li><p><strong>mongo_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The mongo-node count can be purchased is in range of [2, 32].</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `node_class` -(Required) Node specification. see [Instance specifications](https://www.alibabacloud.com/help/doc-detail/57141.htm).
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of DB instance. It a string of 2 to 256 characters.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy DB instance (in month). It is valid when instance_charge_type is <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>. Valid values: [1~9], 12, 24, 36. System default to 1.</p></li>
<li><p><strong>retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance log backup retention days. Available in 1.42.0+.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Security Group ID of ECS.</p></li>
<li><p><strong>security_ip_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]). System default to <code class="docutils literal notranslate"><span class="pre">[&quot;127.0.0.1&quot;]</span></code>.</p></li>
<li><p><strong>shard_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – the shard-node count can be purchased is in range of [2, 32].</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `node_class` -(Required) Node specification. see [Instance specifications](https://www.alibabacloud.com/help/doc-detail/57141.htm).
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>tde_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TDE(Transparent Data Encryption) status.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The virtual switch ID to launch DB instances in one VPC.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the DB instance. MongoDB sharding instance does not support multiple-zone.
If it is a multi-zone and <code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> is specified, the vswitch must in one of them.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>mongo_lists</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connectString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Mongo node connection string</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeClass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the shard-node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Mongo node port</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">shard_list</span></code></p></li>
</ul>
</li>
</ul>
<p>The <strong>shard_lists</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">nodeClass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the shard-node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeStorage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) -</p>
<ul>
<li><p>Custom storage space; value range: [10, 1,000]</p></li>
<li><p>10-GB increments. Unit: GB.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.mongodb.ShardingInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.mongodb.ShardingInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mongodb.ShardingInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_alicloud.mongodb.get_instances">
<code class="sig-prename descclassname">pulumi_alicloud.mongodb.</code><code class="sig-name descname">get_instances</code><span class="sig-paren">(</span><em class="sig-param">availability_zone=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instance_class=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mongodb.get_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">mongodb.getInstances</span></code> data source provides a collection of MongoDB instances available in Alicloud account.
Filters support regular expression for the instance name, engine or instance type.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/mongodb_instances.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/mongodb_instances.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>availability_zone</strong> (<em>str</em>) – Instance availability zone.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – The ids list of MongoDB instances</p></li>
<li><p><strong>instance_class</strong> (<em>str</em>) – Sizing of the instance to be queried.</p></li>
<li><p><strong>instance_type</strong> (<em>str</em>) – Type of the instance to be queried. If it is set to <code class="docutils literal notranslate"><span class="pre">sharding</span></code>, the sharded cluster instances are listed. If it is set to <code class="docutils literal notranslate"><span class="pre">replicate</span></code>, replica set instances are listed. Default value <code class="docutils literal notranslate"><span class="pre">replicate</span></code>.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to apply to the instance name.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.mongodb.get_zones">
<code class="sig-prename descclassname">pulumi_alicloud.mongodb.</code><code class="sig-name descname">get_zones</code><span class="sig-paren">(</span><em class="sig-param">multi=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mongodb.get_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides availability zones for mongoDB that can be accessed by an Alibaba Cloud account within the region configured in the provider.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.73.0+.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/mongodb_zones.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/mongodb_zones.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>multi</strong> (<em>bool</em>) – Indicate whether the zones can be used in a multi AZ configuration. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Multi AZ is usually used to launch MongoDB instances.</p>
</dd>
</dl>
</dd></dl>

</div>
