<div class="section" id="module-pulumi_aws.emr">
<span id="emr"></span><h1>emr<a class="headerlink" href="#module-pulumi_aws.emr" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.emr.Cluster">
<em class="property">class </em><code class="descclassname">pulumi_aws.emr.</code><code class="descname">Cluster</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>additional_info=None</em>, <em>applications=None</em>, <em>autoscaling_role=None</em>, <em>bootstrap_actions=None</em>, <em>configurations=None</em>, <em>configurations_json=None</em>, <em>core_instance_count=None</em>, <em>core_instance_type=None</em>, <em>custom_ami_id=None</em>, <em>ebs_root_volume_size=None</em>, <em>ec2_attributes=None</em>, <em>instance_groups=None</em>, <em>keep_job_flow_alive_when_no_steps=None</em>, <em>kerberos_attributes=None</em>, <em>log_uri=None</em>, <em>master_instance_type=None</em>, <em>name=None</em>, <em>release_label=None</em>, <em>scale_down_behavior=None</em>, <em>security_configuration=None</em>, <em>service_role=None</em>, <em>steps=None</em>, <em>tags=None</em>, <em>termination_protection=None</em>, <em>visible_to_all_users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic MapReduce Cluster, a web service that makes it easy to
process large amounts of data efficiently. See [Amazon Elastic MapReduce Documentation](<a class="reference external" href="https://aws.amazon.com/documentation/elastic-mapreduce/">https://aws.amazon.com/documentation/elastic-mapreduce/</a>)
for more information.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>additional_info</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore Terraform cannot detect drift from the actual EMR cluster if its value is changed outside Terraform.</li>
<li><strong>applications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of applications for the cluster. Valid values are: <cite>Flink</cite>, <cite>Hadoop</cite>, <cite>Hive</cite>, <cite>Mahout</cite>, <cite>Pig</cite>, <cite>Spark</cite>, and <cite>JupyterHub</cite> (as of EMR 5.14.0). Case insensitive</li>
<li><strong>autoscaling_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.</li>
<li><strong>bootstrap_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of bootstrap actions that will be run before Hadoop is started on the cluster nodes. Defined below</li>
<li><strong>configurations</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – List of configurations supplied for the EMR cluster you are creating</li>
<li><strong>configurations_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON string for supplying list of configurations for the EMR cluster.</li>
<li><strong>core_instance_count</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster’s master node and use the remainder of the nodes (<cite>core_instance_count</cite>-1) as core nodes. Cannot be specified if <cite>instance_groups</cite> is set. Default <cite>1</cite></li>
<li><strong>core_instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC2 instance type of the slave nodes. Cannot be specified if <cite>instance_groups</cite> is set</li>
<li><strong>custom_ami_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.</li>
<li><strong>ebs_root_volume_size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.</li>
<li><strong>ec2_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Attributes for the EC2 instances running the job flow. Defined below</li>
<li><strong>instance_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of <cite>instance_group</cite> objects for each instance group in the cluster. Exactly one of <cite>master_instance_type</cite> and <cite>instance_group</cite> must be specified. If <cite>instance_group</cite> is set, then it must contain a configuration block for at least the <cite>MASTER</cite> instance group type (as well as any additional instance groups). Defined below</li>
<li><strong>keep_job_flow_alive_when_no_steps</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Switch on/off run cluster with no steps or when all steps are complete (default is on)</li>
<li><strong>kerberos_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Kerberos configuration for the cluster. Defined below</li>
<li><strong>log_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – S3 bucket to write the log files of the job flow. If a value is not provided, logs are not created</li>
<li><strong>master_instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC2 instance type of the master node. Exactly one of <cite>master_instance_type</cite> and <cite>instance_group</cite> must be specified.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the job flow</li>
<li><strong>release_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The release label for the Amazon EMR release</li>
<li><strong>scale_down_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an <cite>instance group</cite> is resized.</li>
<li><strong>security_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with <cite>release_label</cite> 4.8.0 or greater</li>
<li><strong>service_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role that will be assumed by the Amazon EMR service to access AWS resources</li>
<li><strong>steps</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize the [lifecycle configuration block](<a class="reference external" href="https://www.terraform.io/docs/configuration/resources.html">https://www.terraform.io/docs/configuration/resources.html</a>) with <cite>ignore_changes</cite> if other steps are being managed outside of Terraform.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – list of tags to apply to the EMR Cluster</li>
<li><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Switch on/off termination protection (default is off)</li>
<li><strong>visible_to_all_users</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default <cite>true</cite></li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.additional_info">
<code class="descname">additional_info</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.additional_info" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore Terraform cannot detect drift from the actual EMR cluster if its value is changed outside Terraform.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.applications">
<code class="descname">applications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.applications" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of applications for the cluster. Valid values are: <cite>Flink</cite>, <cite>Hadoop</cite>, <cite>Hive</cite>, <cite>Mahout</cite>, <cite>Pig</cite>, <cite>Spark</cite>, and <cite>JupyterHub</cite> (as of EMR 5.14.0). Case insensitive</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.autoscaling_role">
<code class="descname">autoscaling_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.autoscaling_role" title="Permalink to this definition">¶</a></dt>
<dd><p>An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.bootstrap_actions">
<code class="descname">bootstrap_actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.bootstrap_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of bootstrap actions that will be run before Hadoop is started on the cluster nodes. Defined below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.configurations">
<code class="descname">configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of configurations supplied for the EMR cluster you are creating</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.configurations_json">
<code class="descname">configurations_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.configurations_json" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON string for supplying list of configurations for the EMR cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.core_instance_count">
<code class="descname">core_instance_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.core_instance_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster’s master node and use the remainder of the nodes (<cite>core_instance_count</cite>-1) as core nodes. Cannot be specified if <cite>instance_groups</cite> is set. Default <cite>1</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.core_instance_type">
<code class="descname">core_instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.core_instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The EC2 instance type of the slave nodes. Cannot be specified if <cite>instance_groups</cite> is set</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.custom_ami_id">
<code class="descname">custom_ami_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.custom_ami_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.ebs_root_volume_size">
<code class="descname">ebs_root_volume_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.ebs_root_volume_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.ec2_attributes">
<code class="descname">ec2_attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.ec2_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Attributes for the EC2 instances running the job flow. Defined below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.instance_groups">
<code class="descname">instance_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.instance_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of <cite>instance_group</cite> objects for each instance group in the cluster. Exactly one of <cite>master_instance_type</cite> and <cite>instance_group</cite> must be specified. If <cite>instance_group</cite> is set, then it must contain a configuration block for at least the <cite>MASTER</cite> instance group type (as well as any additional instance groups). Defined below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.keep_job_flow_alive_when_no_steps">
<code class="descname">keep_job_flow_alive_when_no_steps</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.keep_job_flow_alive_when_no_steps" title="Permalink to this definition">¶</a></dt>
<dd><p>Switch on/off run cluster with no steps or when all steps are complete (default is on)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.kerberos_attributes">
<code class="descname">kerberos_attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.kerberos_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Kerberos configuration for the cluster. Defined below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.log_uri">
<code class="descname">log_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.log_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>S3 bucket to write the log files of the job flow. If a value is not provided, logs are not created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.master_instance_type">
<code class="descname">master_instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.master_instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The EC2 instance type of the master node. Exactly one of <cite>master_instance_type</cite> and <cite>instance_group</cite> must be specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.master_public_dns">
<code class="descname">master_public_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.master_public_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The public DNS name of the master EC2 instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the job flow</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.release_label">
<code class="descname">release_label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.release_label" title="Permalink to this definition">¶</a></dt>
<dd><p>The release label for the Amazon EMR release</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.scale_down_behavior">
<code class="descname">scale_down_behavior</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.scale_down_behavior" title="Permalink to this definition">¶</a></dt>
<dd><p>The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an <cite>instance group</cite> is resized.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.security_configuration">
<code class="descname">security_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.security_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with <cite>release_label</cite> 4.8.0 or greater</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.service_role">
<code class="descname">service_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.service_role" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM role that will be assumed by the Amazon EMR service to access AWS resources</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.steps">
<code class="descname">steps</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.steps" title="Permalink to this definition">¶</a></dt>
<dd><p>List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize the [lifecycle configuration block](<a class="reference external" href="https://www.terraform.io/docs/configuration/resources.html">https://www.terraform.io/docs/configuration/resources.html</a>) with <cite>ignore_changes</cite> if other steps are being managed outside of Terraform.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>list of tags to apply to the EMR Cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.termination_protection">
<code class="descname">termination_protection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Switch on/off termination protection (default is off)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.visible_to_all_users">
<code class="descname">visible_to_all_users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.visible_to_all_users" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default <cite>true</cite></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.emr.Cluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.emr.Cluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.emr.InstanceGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.emr.</code><code class="descname">InstanceGroup</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>cluster_id=None</em>, <em>ebs_configs=None</em>, <em>ebs_optimized=None</em>, <em>instance_count=None</em>, <em>instance_type=None</em>, <em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic MapReduce Cluster Instance Group configuration.
See [Amazon Elastic MapReduce Documentation](<a class="reference external" href="https://aws.amazon.com/documentation/emr/">https://aws.amazon.com/documentation/emr/</a>) for more information.</p>
<p>&gt; <strong>NOTE:</strong> At this time, Instance Groups cannot be destroyed through the API nor
web interface. Instance Groups are destroyed when the EMR Cluster is destroyed.
Terraform will resize any Instance Group to zero when destroying the resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.</li>
<li><strong>ebs_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <cite>ebs_config</cite> blocks as defined below. Changing this forces a new resource to be created.</li>
<li><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether an Amazon EBS volume is EBS-optimized. Changing this forces a new resource to be created.</li>
<li><strong>instance_count</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Target number of instances for the instance group. Defaults to 0.</li>
<li><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC2 instance type for all instances in the instance group. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human friendly name given to the instance group. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.emr.InstanceGroup.cluster_id">
<code class="descname">cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.InstanceGroup.ebs_configs">
<code class="descname">ebs_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.ebs_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>ebs_config</cite> blocks as defined below. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.InstanceGroup.ebs_optimized">
<code class="descname">ebs_optimized</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.ebs_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether an Amazon EBS volume is EBS-optimized. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.InstanceGroup.instance_count">
<code class="descname">instance_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.instance_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Target number of instances for the instance group. Defaults to 0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.InstanceGroup.instance_type">
<code class="descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The EC2 instance type for all instances in the instance group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.InstanceGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Human friendly name given to the instance group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.emr.InstanceGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.emr.InstanceGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.emr.SecurityConfiguration">
<em class="property">class </em><code class="descclassname">pulumi_aws.emr.</code><code class="descname">SecurityConfiguration</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>configuration=None</em>, <em>name=None</em>, <em>name_prefix=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage AWS EMR Security Configurations</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON formatted Security Configuration</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the EMR Security Configuration. By default generated by Terraform.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <cite>name</cite>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.emr.SecurityConfiguration.configuration">
<code class="descname">configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON formatted Security Configuration</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.SecurityConfiguration.creation_date">
<code class="descname">creation_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.creation_date" title="Permalink to this definition">¶</a></dt>
<dd><p>Date the Security Configuration was created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.SecurityConfiguration.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the EMR Security Configuration. By default generated by Terraform.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.SecurityConfiguration.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified
prefix. Conflicts with <cite>name</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.emr.SecurityConfiguration.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.emr.SecurityConfiguration.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
