---
title: Module emr
title_tag: Module emr | Package pulumi_alicloud | Python SDK
linktitle: emr
notitle: true
---

<div class="section" id="emr">
<h1>emr<a class="headerlink" href="#emr" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.emr"></span><dl class="class">
<dt id="pulumi_alicloud.emr.AwaitableGetDiskTypesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">AwaitableGetDiskTypesResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_type=None</em>, <em class="sig-param">destination_resource=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instance_charge_type=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">types=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.AwaitableGetDiskTypesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.emr.AwaitableGetInstanceTypesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">AwaitableGetInstanceTypesResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_type=None</em>, <em class="sig-param">destination_resource=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instance_charge_type=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">support_local_storage=None</em>, <em class="sig-param">support_node_types=None</em>, <em class="sig-param">types=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.AwaitableGetInstanceTypesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.emr.AwaitableGetMainVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">AwaitableGetMainVersionsResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_types=None</em>, <em class="sig-param">emr_version=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">main_versions=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.AwaitableGetMainVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.emr.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">charge_type=None</em>, <em class="sig-param">cluster_type=None</em>, <em class="sig-param">deposit_type=None</em>, <em class="sig-param">eas_enable=None</em>, <em class="sig-param">emr_ver=None</em>, <em class="sig-param">high_availability_enable=None</em>, <em class="sig-param">host_groups=None</em>, <em class="sig-param">is_open_public_ip=None</em>, <em class="sig-param">key_pair_name=None</em>, <em class="sig-param">master_pwd=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">option_software_lists=None</em>, <em class="sig-param">related_cluster_id=None</em>, <em class="sig-param">security_group_id=None</em>, <em class="sig-param">ssh_enable=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">use_local_metadb=None</em>, <em class="sig-param">user_defined_emr_ecs_role=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a EMR Cluster resource. With this you can create, read, and release  EMR Cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.57.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Charge Type for this group of hosts: PostPaid or PrePaid. If this is not specified, charge type will follow global charge_type value.</p></li>
<li><p><strong>cluster_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – EMR Cluster Type, e.g. HADOOP, KAFKA, DRUID, GATEWAY etc. You can find all valid EMR cluster type in emr web console. Supported ‘GATEWAY’ available in 1.61.0+.</p></li>
<li><p><strong>emr_ver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – EMR Version, e.g. EMR-3.22.0. You can find the all valid EMR Version in emr web console.</p></li>
<li><p><strong>host*groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Groups of Host, You can specify MASTER as a group, CORE as a group (just like the above example).</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of emr cluster. The name length must be less than 64. Supported characters: chinese character, english character, number, “-“, “<a href="#id3"><span class="problematic" id="id4">*</span></a>”.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Zone ID, e.g. cn-huhehaote-a</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `security_group_id` (Optional, ForceNew) Security Group ID for Cluster, you can also specify this key for each host group.
* `vswitch_id` (Optional, ForceNew) Global vswitch id, you can also specify it in host group.
* `option_software_list` (Optional, ForceNew) Optional software list.
* `high_availability_enable` (Optional, ForceNew) High Available for HDFS and YARN. If this is set true, MASTER group must have two nodes.
* `use_local_metadb` (Optional, ForceNew) Use local metadb. Default is false.
* `ssh_enable` (Optional, ForceNew) If this is set true, we can ssh into cluster. Default value is false.
* `master_pwd` (Optional, ForceNew) Master ssh password.
* `eas_enable` (Optional, ForceNew) High security cluster (true) or not. Default value is false.
* `user_defined_emr_ecs_role` (Optional, ForceNew) Alicloud EMR uses roles to perform actions on your behalf when provisioning cluster resources, running applications, dynamically scaling resources. EMR uses the following roles when interacting with other Alicloud services. Default value is AliyunEmrEcsDefaultRole.
* `key_pair_name` (Optional, ForceNew) Ssh key pair.
* `deposit_type` (Optional, ForceNew) Cluster deposit type, HALF_MANAGED or FULL_MANAGED.
* `related_cluster_id` (Optional, ForceNew) This specify the related cluster id, if this cluster is a Gateway.
</pre></div>
</div>
<p>The <strong>host_groups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoRenew</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Auto renew for prepaid, true of false. Default is false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">charge_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Charge Type for this group of hosts: PostPaid or PrePaid. If this is not specified, charge type will follow global charge_type value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Data disk capacity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Data disk count.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Data disk type. Supported value: cloud,cloud_efficiency,cloud_ssd,local_disk,cloud_essd.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpuDriver</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostGroupName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - host group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostGroupType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - host group type, supported value: MASTER, CORE or TASK, supported ‘GATEWAY’ available in 1.61.0+.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceList</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Instance list for cluster scale down. This value follows the json format, e.g. [“instance_id1”,”instance_id2”]. escape character for ” is “.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Host Ecs instance type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Host number in this group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - If charge type is PrePaid, this should be specified, unit is month. Supported value: 1、2、3、4、5、6、7、8、9、12、24、36.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sysDiskCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System disk capacity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sysDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System disk type. Supported value: cloud,cloud_efficiency,cloud_ssd,cloud_essd.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/emr_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/emr_cluster.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_alicloud.emr.Cluster.charge_type">
<code class="sig-name descname">charge_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Charge Type for this group of hosts: PostPaid or PrePaid. If this is not specified, charge type will follow global charge_type value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.emr.Cluster.cluster_type">
<code class="sig-name descname">cluster_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.cluster_type" title="Permalink to this definition">¶</a></dt>
<dd><p>EMR Cluster Type, e.g. HADOOP, KAFKA, DRUID, GATEWAY etc. You can find all valid EMR cluster type in emr web console. Supported ‘GATEWAY’ available in 1.61.0+.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.emr.Cluster.emr_ver">
<code class="sig-name descname">emr_ver</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.emr_ver" title="Permalink to this definition">¶</a></dt>
<dd><p>EMR Version, e.g. EMR-3.22.0. You can find the all valid EMR Version in emr web console.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.emr.Cluster.host_groups">
<code class="sig-name descname">host_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.host_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Groups of Host, You can specify MASTER as a group, CORE as a group (just like the above example).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoRenew</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Auto renew for prepaid, true of false. Default is false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">charge_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Charge Type for this group of hosts: PostPaid or PrePaid. If this is not specified, charge type will follow global charge_type value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Data disk capacity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskCount</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Data disk count.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Data disk type. Supported value: cloud,cloud_efficiency,cloud_ssd,local_disk,cloud_essd.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpuDriver</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostGroupName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - host group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostGroupType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - host group type, supported value: MASTER, CORE or TASK, supported ‘GATEWAY’ available in 1.61.0+.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceList</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Instance list for cluster scale down. This value follows the json format, e.g. [“instance_id1”,”instance_id2”]. escape character for ” is “.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Host Ecs instance type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Host number in this group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - If charge type is PrePaid, this should be specified, unit is month. Supported value: 1、2、3、4、5、6、7、8、9、12、24、36.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sysDiskCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - System disk capacity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sysDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - System disk type. Supported value: cloud,cloud_efficiency,cloud_ssd,cloud_essd.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.emr.Cluster.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of emr cluster. The name length must be less than 64. Supported characters: chinese character, english character, number, “-“, “_”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.emr.Cluster.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.emr.Cluster.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Zone ID, e.g. cn-huhehaote-a</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_id</span></code> (Optional, ForceNew) Security Group ID for Cluster, you can also specify this key for each host group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vswitch_id</span></code> (Optional, ForceNew) Global vswitch id, you can also specify it in host group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">option_software_list</span></code> (Optional, ForceNew) Optional software list.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">high_availability_enable</span></code> (Optional, ForceNew) High Available for HDFS and YARN. If this is set true, MASTER group must have two nodes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">use_local_metadb</span></code> (Optional, ForceNew) Use local metadb. Default is false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssh_enable</span></code> (Optional, ForceNew) If this is set true, we can ssh into cluster. Default value is false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">master_pwd</span></code> (Optional, ForceNew) Master ssh password.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eas_enable</span></code> (Optional, ForceNew) High security cluster (true) or not. Default value is false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_defined_emr_ecs_role</span></code> (Optional, ForceNew) Alicloud EMR uses roles to perform actions on your behalf when provisioning cluster resources, running applications, dynamically scaling resources. EMR uses the following roles when interacting with other Alicloud services. Default value is AliyunEmrEcsDefaultRole.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_pair_name</span></code> (Optional, ForceNew) Ssh key pair.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deposit_type</span></code> (Optional, ForceNew) Cluster deposit type, HALF_MANAGED or FULL_MANAGED.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">related_cluster_id</span></code> (Optional, ForceNew) This specify the related cluster id, if this cluster is a Gateway.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.emr.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">charge_type=None</em>, <em class="sig-param">cluster_type=None</em>, <em class="sig-param">deposit_type=None</em>, <em class="sig-param">eas_enable=None</em>, <em class="sig-param">emr_ver=None</em>, <em class="sig-param">high_availability_enable=None</em>, <em class="sig-param">host_groups=None</em>, <em class="sig-param">is_open_public_ip=None</em>, <em class="sig-param">key_pair_name=None</em>, <em class="sig-param">master_pwd=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">option_software_lists=None</em>, <em class="sig-param">related_cluster_id=None</em>, <em class="sig-param">security_group_id=None</em>, <em class="sig-param">ssh_enable=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">use_local_metadb=None</em>, <em class="sig-param">user_defined_emr_ecs_role=None</em>, <em class="sig-param">vswitch_id=None</em>, <em class="sig-param">zone_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Charge Type for this group of hosts: PostPaid or PrePaid. If this is not specified, charge type will follow global charge_type value.</p></li>
<li><p><strong>cluster_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – EMR Cluster Type, e.g. HADOOP, KAFKA, DRUID, GATEWAY etc. You can find all valid EMR cluster type in emr web console. Supported ‘GATEWAY’ available in 1.61.0+.</p></li>
<li><p><strong>emr_ver</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – EMR Version, e.g. EMR-3.22.0. You can find the all valid EMR Version in emr web console.</p></li>
<li><p><strong>host*groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Groups of Host, You can specify MASTER as a group, CORE as a group (just like the above example).</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of emr cluster. The name length must be less than 64. Supported characters: chinese character, english character, number, “-“, “<a href="#id7"><span class="problematic" id="id8">*</span></a>”.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Zone ID, e.g. cn-huhehaote-a</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `security_group_id` (Optional, ForceNew) Security Group ID for Cluster, you can also specify this key for each host group.
* `vswitch_id` (Optional, ForceNew) Global vswitch id, you can also specify it in host group.
* `option_software_list` (Optional, ForceNew) Optional software list.
* `high_availability_enable` (Optional, ForceNew) High Available for HDFS and YARN. If this is set true, MASTER group must have two nodes.
* `use_local_metadb` (Optional, ForceNew) Use local metadb. Default is false.
* `ssh_enable` (Optional, ForceNew) If this is set true, we can ssh into cluster. Default value is false.
* `master_pwd` (Optional, ForceNew) Master ssh password.
* `eas_enable` (Optional, ForceNew) High security cluster (true) or not. Default value is false.
* `user_defined_emr_ecs_role` (Optional, ForceNew) Alicloud EMR uses roles to perform actions on your behalf when provisioning cluster resources, running applications, dynamically scaling resources. EMR uses the following roles when interacting with other Alicloud services. Default value is AliyunEmrEcsDefaultRole.
* `key_pair_name` (Optional, ForceNew) Ssh key pair.
* `deposit_type` (Optional, ForceNew) Cluster deposit type, HALF_MANAGED or FULL_MANAGED.
* `related_cluster_id` (Optional, ForceNew) This specify the related cluster id, if this cluster is a Gateway.
</pre></div>
</div>
<p>The <strong>host_groups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoRenew</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Auto renew for prepaid, true of false. Default is false.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">charge_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Charge Type for this group of hosts: PostPaid or PrePaid. If this is not specified, charge type will follow global charge_type value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Data disk capacity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diskCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Data disk count.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Data disk type. Supported value: cloud,cloud_efficiency,cloud_ssd,local_disk,cloud_essd.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpuDriver</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostGroupName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - host group name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostGroupType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - host group type, supported value: MASTER, CORE or TASK, supported ‘GATEWAY’ available in 1.61.0+.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceList</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Instance list for cluster scale down. This value follows the json format, e.g. [“instance_id1”,”instance_id2”]. escape character for ” is “.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Host Ecs instance type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Host number in this group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">period</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - If charge type is PrePaid, this should be specified, unit is month. Supported value: 1、2、3、4、5、6、7、8、9、12、24、36.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sysDiskCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System disk capacity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sysDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - System disk type. Supported value: cloud,cloud_efficiency,cloud_ssd,cloud_essd.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/emr_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/emr_cluster.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.emr.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.emr.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.emr.GetDiskTypesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">GetDiskTypesResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_type=None</em>, <em class="sig-param">destination_resource=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instance_charge_type=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">types=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.GetDiskTypesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDiskTypes.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.emr.GetDiskTypesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetDiskTypesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of data disk and system disk type IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.emr.GetDiskTypesResult.types">
<code class="sig-name descname">types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetDiskTypesResult.types" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of emr instance types. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.emr.GetDiskTypesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetDiskTypesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.emr.GetInstanceTypesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">GetInstanceTypesResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_type=None</em>, <em class="sig-param">destination_resource=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instance_charge_type=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">support_local_storage=None</em>, <em class="sig-param">support_node_types=None</em>, <em class="sig-param">types=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.GetInstanceTypesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstanceTypes.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.emr.GetInstanceTypesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetInstanceTypesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of emr instance types IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.emr.GetInstanceTypesResult.types">
<code class="sig-name descname">types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetInstanceTypesResult.types" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of emr instance types. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.emr.GetInstanceTypesResult.zone_id">
<code class="sig-name descname">zone_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetInstanceTypesResult.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The available zone id in Alibaba Cloud account</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.emr.GetInstanceTypesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetInstanceTypesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.emr.GetMainVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">GetMainVersionsResult</code><span class="sig-paren">(</span><em class="sig-param">cluster_types=None</em>, <em class="sig-param">emr_version=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">main_versions=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.GetMainVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getMainVersions.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.emr.GetMainVersionsResult.emr_version">
<code class="sig-name descname">emr_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetMainVersionsResult.emr_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the emr cluster instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.emr.GetMainVersionsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetMainVersionsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of emr instance types IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.emr.GetMainVersionsResult.main_versions">
<code class="sig-name descname">main_versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetMainVersionsResult.main_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of versions of the emr cluster instance. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.emr.GetMainVersionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.emr.GetMainVersionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.emr.get_disk_types">
<code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">get_disk_types</code><span class="sig-paren">(</span><em class="sig-param">cluster_type=None</em>, <em class="sig-param">destination_resource=None</em>, <em class="sig-param">instance_charge_type=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.get_disk_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">emr.getDiskTypes</span></code> data source provides a collection of data disk and 
system disk types available in Alibaba Cloud account when create a emr cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.60.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_type</strong> (<em>str</em>) – The cluster type of the emr cluster instance. Possible values: <code class="docutils literal notranslate"><span class="pre">HADOOP</span></code>, <code class="docutils literal notranslate"><span class="pre">KAFKA</span></code>, <code class="docutils literal notranslate"><span class="pre">ZOOKEEPER</span></code>, <code class="docutils literal notranslate"><span class="pre">DRUID</span></code>.</p></li>
<li><p><strong>destination_resource</strong> (<em>str</em>) – The destination resource of emr cluster instance</p></li>
<li><p><strong>instance_charge_type</strong> (<em>str</em>) – Filter the results by charge type. Valid values: <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> and <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>instance_type</strong> (<em>str</em>) – The ecs instance type of create emr cluster instance.</p></li>
<li><p><strong>zone_id</strong> (<em>str</em>) – The Zone to create emr cluster instance.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/emr_disk_types.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/emr_disk_types.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.emr.get_instance_types">
<code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">get_instance_types</code><span class="sig-paren">(</span><em class="sig-param">cluster_type=None</em>, <em class="sig-param">destination_resource=None</em>, <em class="sig-param">instance_charge_type=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">support_local_storage=None</em>, <em class="sig-param">support_node_types=None</em>, <em class="sig-param">zone_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.get_instance_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">emr.getInstanceTypes</span></code> data source provides a collection of ecs
instance types available in Alibaba Cloud account when create a emr cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.59.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_type</strong> (<em>str</em>) – The cluster type of the emr cluster instance. Possible values: <code class="docutils literal notranslate"><span class="pre">HADOOP</span></code>, <code class="docutils literal notranslate"><span class="pre">KAFKA</span></code>, <code class="docutils literal notranslate"><span class="pre">ZOOKEEPER</span></code>, <code class="docutils literal notranslate"><span class="pre">DRUID</span></code>.</p></li>
<li><p><strong>destination_resource</strong> (<em>str</em>) – The destination resource of emr cluster instance</p></li>
<li><p><strong>instance_charge_type</strong> (<em>str</em>) – Filter the results by charge type. Valid values: <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code> and <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>. Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>support_local_storage</strong> (<em>bool</em>) – Whether the current storage disk is local or not.</p></li>
<li><p><strong>support_node_types</strong> (<em>list</em>) – The specific supported node type list. 
Possible values may be any one or combination of these: [“MASTER”, “CORE”, “TASK”, “GATEWAY”]</p></li>
<li><p><strong>zone_id</strong> (<em>str</em>) – The supported resources of specific zoneId.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/emr_instance_types.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/emr_instance_types.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.emr.get_main_versions">
<code class="sig-prename descclassname">pulumi_alicloud.emr.</code><code class="sig-name descname">get_main_versions</code><span class="sig-paren">(</span><em class="sig-param">cluster_types=None</em>, <em class="sig-param">emr_version=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.emr.get_main_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">emr.getMainVersions</span></code> data source provides a collection of emr 
main versions available in Alibaba Cloud account when create a emr cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.59.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_types</strong> (<em>list</em>) – The supported clusterType of this emr version.
Possible values may be any one or combination of these: [“HADOOP”, “DRUID”, “KAFKA”, “ZOOKEEPER”, “FLINK”, “CLICKHOUSE”]</p></li>
<li><p><strong>emr_version</strong> (<em>str</em>) – The version of the emr cluster instance. Possible values: <code class="docutils literal notranslate"><span class="pre">EMR-4.0.0</span></code>, <code class="docutils literal notranslate"><span class="pre">EMR-3.23.0</span></code>, <code class="docutils literal notranslate"><span class="pre">EMR-3.22.0</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/emr_main_versions.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/emr_main_versions.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
