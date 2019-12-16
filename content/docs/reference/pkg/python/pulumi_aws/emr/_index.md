---
title: Module emr
title_tag: Module emr | Package pulumi_aws | Python SDK
linktitle: emr
notitle: true
---

<div class="section" id="emr">
<h1>emr<a class="headerlink" href="#emr" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.emr"></span><dl class="class">
<dt id="pulumi_aws.emr.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.emr.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_info=None</em>, <em class="sig-param">applications=None</em>, <em class="sig-param">autoscaling_role=None</em>, <em class="sig-param">bootstrap_actions=None</em>, <em class="sig-param">configurations=None</em>, <em class="sig-param">configurations_json=None</em>, <em class="sig-param">core_instance_count=None</em>, <em class="sig-param">core_instance_group=None</em>, <em class="sig-param">core_instance_type=None</em>, <em class="sig-param">custom_ami_id=None</em>, <em class="sig-param">ebs_root_volume_size=None</em>, <em class="sig-param">ec2_attributes=None</em>, <em class="sig-param">instance_groups=None</em>, <em class="sig-param">keep_job_flow_alive_when_no_steps=None</em>, <em class="sig-param">kerberos_attributes=None</em>, <em class="sig-param">log_uri=None</em>, <em class="sig-param">master_instance_group=None</em>, <em class="sig-param">master_instance_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">release_label=None</em>, <em class="sig-param">scale_down_behavior=None</em>, <em class="sig-param">security_configuration=None</em>, <em class="sig-param">service_role=None</em>, <em class="sig-param">steps=None</em>, <em class="sig-param">step_concurrency_level=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">termination_protection=None</em>, <em class="sig-param">visible_to_all_users=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic MapReduce Cluster, a web service that makes it easy to
process large amounts of data efficiently. See <a class="reference external" href="https://aws.amazon.com/documentation/elastic-mapreduce/">Amazon Elastic MapReduce Documentation</a>
for more information.</p>
<p>To configure <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups">Instance Groups</a> for <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-task">task nodes</a>, see the <cite>``emr.InstanceGroup`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html">https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html</a>&gt;`_.</p>
<blockquote>
<div><p>Support for <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-fleets">Instance Fleets</a> will be made available in an upcoming release.</p>
</div></blockquote>
<p>Supported arguments for the <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> - (Required) EC2 instance type for all instances in the instance group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling_policy</span></code> - (Optional) String containing the <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html">EMR Auto Scaling Policy</a> JSON.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> - (Optional) Bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_config</span></code> - (Optional) Configuration block(s) for EBS volumes attached to each instance in the instance group. Detailed below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> - (Optional) Target number of instances for the instance group. Must be at least 1. Defaults to 1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Optional) Friendly name given to the instance group.</p></li>
</ul>
<p>Attributes for the Amazon EC2 instances running the job flow</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key_name</span></code> - (Optional) Amazon EC2 key pair that can be used to ssh to the master node as the user called <code class="docutils literal notranslate"><span class="pre">hadoop</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> - (Optional) VPC subnet id where you want the job flow to launch. Cannot specify the <code class="docutils literal notranslate"><span class="pre">cc1.4xlarge</span></code> instance type for nodes of a job flow launched in a Amazon VPC</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">additional_master_security_groups</span></code> - (Optional) String containing a comma separated list of additional Amazon EC2 security group IDs for the master node</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">additional_slave_security_groups</span></code> - (Optional) String containing a comma separated list of additional Amazon EC2 security group IDs for the slave nodes as a comma separated string</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emr_managed_master_security_group</span></code> - (Optional) Identifier of the Amazon EC2 EMR-Managed security group for the master node</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emr_managed_slave_security_group</span></code> - (Optional) Identifier of the Amazon EC2 EMR-Managed security group for the slave nodes</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_access_security_group</span></code> - (Optional) Identifier of the Amazon EC2 service-access security group - required when the cluster runs on a private subnet</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_profile</span></code> - (Required) Instance Profile for EC2 instances of the cluster assume this role</p></li>
</ul>
<blockquote>
<div><p><strong>NOTE on EMR-Managed security groups:</strong> These security groups will have any
missing inbound or outbound access rules added and maintained by AWS, to ensure
proper communication between instances in a cluster. The EMR service will
maintain these rules for groups provided in <code class="docutils literal notranslate"><span class="pre">emr_managed_master_security_group</span></code>
and <code class="docutils literal notranslate"><span class="pre">emr_managed_slave_security_group</span></code>; attempts to remove the required rules
may succeed, only for the EMR service to re-add them in a matter of minutes.
This may cause this provider to fail to destroy an environment that contains an EMR
cluster, because the EMR service does not revoke rules added on deletion,
leaving a cyclic dependency between the security groups that prevents their
deletion. To avoid this, use the <code class="docutils literal notranslate"><span class="pre">revoke_rules_on_delete</span></code> optional attribute for
any Security Group used in <code class="docutils literal notranslate"><span class="pre">emr_managed_master_security_group</span></code> and
<code class="docutils literal notranslate"><span class="pre">emr_managed_slave_security_group</span></code>. See <a class="reference external" href="http://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-man-sec-groups.html">Amazon EMR-Managed Security
Groups</a>
for more information about the EMR-managed security group rules.</p>
</div></blockquote>
<p>Attributes for Kerberos configuration</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ad_domain_join_password</span></code> - (Optional) The Active Directory password for <code class="docutils literal notranslate"><span class="pre">ad_domain_join_user</span></code>. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ad_domain_join_user</span></code> - (Optional) Required only when establishing a cross-realm trust with an Active Directory domain. A user with sufficient privileges to join resources to the domain. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cross_realm_trust_principal_password</span></code> - (Optional) Required only when establishing a cross-realm trust with a KDC in a different realm. The cross-realm principal password, which must be identical across realms. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kdc_admin_password</span></code> - (Required) The password used within the cluster for the kadmin service on the cluster-dedicated KDC, which maintains Kerberos principals, password policies, and keytabs for the cluster. This provider cannot perform drift detection of this configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">realm</span></code> - (Required) The name of the Kerberos realm to which all nodes in a cluster belong. For example, <code class="docutils literal notranslate"><span class="pre">EC2.INTERNAL</span></code></p></li>
</ul>
<p>Attributes for each task instance group in the cluster</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance_role</span></code> - (Required) The role of the instance group in the cluster. Valid values are: <code class="docutils literal notranslate"><span class="pre">MASTER</span></code>, <code class="docutils literal notranslate"><span class="pre">CORE</span></code>, and <code class="docutils literal notranslate"><span class="pre">TASK</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> - (Required) The EC2 instance type for all instances in the instance group</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> - (Optional) Target number of instances for the instance group</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Optional) Friendly name given to the instance group</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> - (Optional) If set, the bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_config</span></code> - (Optional) A list of attributes for the EBS volumes attached to each instance in the instance group. Each <code class="docutils literal notranslate"><span class="pre">ebs_config</span></code> defined will result in additional EBS volumes being attached to <em>each</em> instance in the instance group. Defined below</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling_policy</span></code> - (Optional) The autoscaling policy document. This is a JSON formatted string. See <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html">EMR Auto Scaling</a></p></li>
</ul>
<p>Supported nested arguments for the <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> configuration block:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> - (Required) EC2 instance type for all instances in the instance group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> - (Optional) Bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_config</span></code> - (Optional) Configuration block(s) for EBS volumes attached to each instance in the instance group. Detailed below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> - (Optional) Target number of instances for the instance group. Must be 1 or 3. Defaults to 1. Launching with multiple master nodes is only supported in EMR version 5.23.0+, and requires this resource’s <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> to be configured. Public (Internet accessible) instances must be created in VPC subnets that have <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/subnet.html#map_public_ip_on_launch">map public IP on launch</a> enabled. Termination protection is automatically enabled when launched with multiple master nodes and this provider must have the <code class="docutils literal notranslate"><span class="pre">termination_protection</span> <span class="pre">=</span> <span class="pre">false</span></code> configuration applied before destroying this resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Optional) Friendly name given to the instance group.</p></li>
</ul>
<p>Attributes for the EBS volumes attached to each EC2 instance in the <code class="docutils literal notranslate"><span class="pre">instance_group</span></code></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> - (Required) The volume size, in gibibytes (GiB).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> - (Required) The volume type. Valid options are <code class="docutils literal notranslate"><span class="pre">gp2</span></code>, <code class="docutils literal notranslate"><span class="pre">io1</span></code>, <code class="docutils literal notranslate"><span class="pre">standard</span></code> and <code class="docutils literal notranslate"><span class="pre">st1</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html">EBS Volume Types</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> - (Optional) The number of I/O operations per second (IOPS) that the volume supports</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumes_per_instance</span></code> - (Optional) The number of EBS volumes with this configuration to attach to each EC2 instance in the instance group (default is 1)</p></li>
</ul>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) Name of the bootstrap action</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> - (Required) Location of the script to run during a bootstrap action. Can be either a location in Amazon S3 or on a local file system</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> - (Optional) List of command line arguments to pass to the bootstrap action script</p></li>
</ul>
<p>Attributes for step configuration</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action_on_failure</span></code> - (Required) The action to take if the step fails. Valid values: <code class="docutils literal notranslate"><span class="pre">TERMINATE_JOB_FLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">TERMINATE_CLUSTER</span></code>, <code class="docutils literal notranslate"><span class="pre">CANCEL_AND_WAIT</span></code>, and <code class="docutils literal notranslate"><span class="pre">CONTINUE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hadoop_jar_step</span></code> - (Required) The JAR file used for the step. Defined below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> - (Required) The name of the step.</p></li>
</ul>
<p>Attributes for Hadoop job step configuration</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> - (Optional) List of command line arguments passed to the JAR file’s main function when executed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jar</span></code> - (Required) Path to a JAR file run during the step.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">main_class</span></code> - (Optional) Name of the main class in the specified Java file. If not specified, the JAR file should specify a Main-Class in its manifest file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> - (Optional) Key-Value map of Java properties that are set when the step runs. You can use these properties to pass key value pairs to your main function.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_info</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore this provider cannot detect drift from the actual EMR cluster if its value is changed outside this provider.</p></li>
<li><p><strong>applications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of applications for the cluster. Valid values are: <code class="docutils literal notranslate"><span class="pre">Flink</span></code>, <code class="docutils literal notranslate"><span class="pre">Hadoop</span></code>, <code class="docutils literal notranslate"><span class="pre">Hive</span></code>, <code class="docutils literal notranslate"><span class="pre">Mahout</span></code>, <code class="docutils literal notranslate"><span class="pre">Pig</span></code>, <code class="docutils literal notranslate"><span class="pre">Spark</span></code>, and <code class="docutils literal notranslate"><span class="pre">JupyterHub</span></code> (as of EMR 5.14.0). Case insensitive</p></li>
<li><p><strong>autoscaling_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.</p></li>
<li><p><strong>bootstrap_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of bootstrap actions that will be run before Hadoop is started on the cluster nodes. Defined below</p></li>
<li><p><strong>configurations</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – List of configurations supplied for the EMR cluster you are creating</p></li>
<li><p><strong>configurations_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON string for supplying list of configurations for the EMR cluster.</p></li>
<li><p><strong>core_instance_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Use the <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">instance_count</span></code> argument instead. Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster’s master node and use the remainder of the nodes (<code class="docutils literal notranslate"><span class="pre">core_instance_count</span></code>-1) as core nodes. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set. Default <code class="docutils literal notranslate"><span class="pre">1</span></code></p></li>
<li><p><strong>core_instance_group</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block to use an <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups">Instance Group</a> for the <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-core">core node type</a>. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">core_instance_count</span></code> argument, <code class="docutils literal notranslate"><span class="pre">core_instance_type</span></code> argument, or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set. Detailed below.</p></li>
<li><p><strong>core_instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Use the <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">instance_type</span></code> argument instead. The EC2 instance type of the slave nodes. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set.</p></li>
<li><p><strong>custom_ami_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.</p></li>
<li><p><strong>ebs_root_volume_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.</p></li>
<li><p><strong>ec2_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Attributes for the EC2 instances running the job flow. Defined below</p></li>
<li><p><strong>instance_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Use the <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> configuration block, <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block and <cite>``emr.InstanceGroup`</cite> resource(s) &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html">https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html</a>&gt;`_ instead. A list of <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> objects for each instance group in the cluster. Exactly one of <code class="docutils literal notranslate"><span class="pre">master_instance_type</span></code> and <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> must be specified. If <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> is set, then it must contain a configuration block for at least the <code class="docutils literal notranslate"><span class="pre">MASTER</span></code> instance group type (as well as any additional instance groups). Cannot be specified if <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration blocks are set. Defined below</p></li>
<li><p><strong>keep_job_flow_alive_when_no_steps</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Switch on/off run cluster with no steps or when all steps are complete (default is on)</p></li>
<li><p><strong>kerberos_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Kerberos configuration for the cluster. Defined below</p></li>
<li><p><strong>log_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – S3 bucket to write the log files of the job flow. If a value is not provided, logs are not created</p></li>
<li><p><strong>master_instance_group</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Configuration block to use an <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups">Instance Group</a> for the <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-master">master node type</a>. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">master_instance_type</span></code> argument or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set. Detailed below.</p>
</p></li>
<li><p><strong>master_instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Use the <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">instance_type</span></code> argument instead. The EC2 instance type of the master node. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the job flow</p></li>
<li><p><strong>release_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The release label for the Amazon EMR release</p></li>
<li><p><strong>scale_down_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an <code class="docutils literal notranslate"><span class="pre">instance</span> <span class="pre">group</span></code> is resized.</p></li>
<li><p><strong>security_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with <code class="docutils literal notranslate"><span class="pre">release_label</span></code> 4.8.0 or greater</p></li>
<li><p><strong>service_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role that will be assumed by the Amazon EMR service to access AWS resources</p></li>
<li><p><strong>steps</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize the <a class="reference external" href="https://www.terraform.io/docs/configuration/resources.html">lifecycle configuration block</a> with <code class="docutils literal notranslate"><span class="pre">ignore_changes</span></code> if other steps are being managed outside of this provider. This argument is processed in <a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">attribute-as-blocks mode</a>.</p></li>
<li><p><strong>step_concurrency_level</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of steps that can be executed concurrently. You can specify a maximum of 256 steps. Only valid for EMR clusters with <code class="docutils literal notranslate"><span class="pre">release_label</span></code> 5.28.0 or greater. (default is 1)</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – list of tags to apply to the EMR Cluster</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Switch on/off termination protection (default is <code class="docutils literal notranslate"><span class="pre">false</span></code>, except when using multiple master nodes). Before attempting to destroy the resource when termination protection is enabled, this configuration must be applied with its value set to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>visible_to_all_users</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
</ul>
</dd>
</dl>
<p>The <strong>bootstrap_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the job flow</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>core_instance_group</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_configs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the EMR Cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the job flow</p></li>
</ul>
<p>The <strong>ec2_attributes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalMasterSecurityGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">additionalSlaveSecurityGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emrManagedMasterSecurityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emrManagedSlaveSecurityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceProfile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccessSecurityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>instance_groups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_configs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the EMR Cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceRole</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the job flow</p></li>
</ul>
<p>The <strong>kerberos_attributes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adDomainJoinPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adDomainJoinUser</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossRealmTrustPrincipalPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kdcAdminPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">realm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>master_instance_group</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_configs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the EMR Cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the job flow</p></li>
</ul>
<p>The <strong>steps</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionOnFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hadoopJarStep</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jar</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mainClass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the job flow</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/emr_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/emr_cluster.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.additional_info">
<code class="sig-name descname">additional_info</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.additional_info" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore this provider cannot detect drift from the actual EMR cluster if its value is changed outside this provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.applications">
<code class="sig-name descname">applications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.applications" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of applications for the cluster. Valid values are: <code class="docutils literal notranslate"><span class="pre">Flink</span></code>, <code class="docutils literal notranslate"><span class="pre">Hadoop</span></code>, <code class="docutils literal notranslate"><span class="pre">Hive</span></code>, <code class="docutils literal notranslate"><span class="pre">Mahout</span></code>, <code class="docutils literal notranslate"><span class="pre">Pig</span></code>, <code class="docutils literal notranslate"><span class="pre">Spark</span></code>, and <code class="docutils literal notranslate"><span class="pre">JupyterHub</span></code> (as of EMR 5.14.0). Case insensitive</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.autoscaling_role">
<code class="sig-name descname">autoscaling_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.autoscaling_role" title="Permalink to this definition">¶</a></dt>
<dd><p>An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.bootstrap_actions">
<code class="sig-name descname">bootstrap_actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.bootstrap_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of bootstrap actions that will be run before Hadoop is started on the cluster nodes. Defined below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the job flow</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.configurations">
<code class="sig-name descname">configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of configurations supplied for the EMR cluster you are creating</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.configurations_json">
<code class="sig-name descname">configurations_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.configurations_json" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON string for supplying list of configurations for the EMR cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.core_instance_count">
<code class="sig-name descname">core_instance_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.core_instance_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">instance_count</span></code> argument instead. Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster’s master node and use the remainder of the nodes (<code class="docutils literal notranslate"><span class="pre">core_instance_count</span></code>-1) as core nodes. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set. Default <code class="docutils literal notranslate"><span class="pre">1</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.core_instance_group">
<code class="sig-name descname">core_instance_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.core_instance_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block to use an <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups">Instance Group</a> for the <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-core">core node type</a>. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">core_instance_count</span></code> argument, <code class="docutils literal notranslate"><span class="pre">core_instance_type</span></code> argument, or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_configs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the EMR Cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the job flow</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.core_instance_type">
<code class="sig-name descname">core_instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.core_instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">instance_type</span></code> argument instead. The EC2 instance type of the slave nodes. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.custom_ami_id">
<code class="sig-name descname">custom_ami_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.custom_ami_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.ebs_root_volume_size">
<code class="sig-name descname">ebs_root_volume_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.ebs_root_volume_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.ec2_attributes">
<code class="sig-name descname">ec2_attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.ec2_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Attributes for the EC2 instances running the job flow. Defined below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalMasterSecurityGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">additionalSlaveSecurityGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emrManagedMasterSecurityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emrManagedSlaveSecurityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceProfile</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccessSecurityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.instance_groups">
<code class="sig-name descname">instance_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.instance_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> configuration block, <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block and <cite>``emr.InstanceGroup`</cite> resource(s) &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html">https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html</a>&gt;`_ instead. A list of <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> objects for each instance group in the cluster. Exactly one of <code class="docutils literal notranslate"><span class="pre">master_instance_type</span></code> and <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> must be specified. If <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> is set, then it must contain a configuration block for at least the <code class="docutils literal notranslate"><span class="pre">MASTER</span></code> instance group type (as well as any additional instance groups). Cannot be specified if <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration blocks are set. Defined below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_configs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the EMR Cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceRole</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the job flow</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.keep_job_flow_alive_when_no_steps">
<code class="sig-name descname">keep_job_flow_alive_when_no_steps</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.keep_job_flow_alive_when_no_steps" title="Permalink to this definition">¶</a></dt>
<dd><p>Switch on/off run cluster with no steps or when all steps are complete (default is on)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.kerberos_attributes">
<code class="sig-name descname">kerberos_attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.kerberos_attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>Kerberos configuration for the cluster. Defined below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adDomainJoinPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adDomainJoinUser</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossRealmTrustPrincipalPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kdcAdminPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">realm</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.log_uri">
<code class="sig-name descname">log_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.log_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>S3 bucket to write the log files of the job flow. If a value is not provided, logs are not created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.master_instance_group">
<code class="sig-name descname">master_instance_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.master_instance_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block to use an <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups">Instance Group</a> for the <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-master">master node type</a>. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">master_instance_type</span></code> argument or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set. Detailed below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_configs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the EMR Cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the job flow</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.master_instance_type">
<code class="sig-name descname">master_instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.master_instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">instance_type</span></code> argument instead. The EC2 instance type of the master node. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.master_public_dns">
<code class="sig-name descname">master_public_dns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.master_public_dns" title="Permalink to this definition">¶</a></dt>
<dd><p>The public DNS name of the master EC2 instance.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">core_instance_group.0.id</span></code> - Core node type Instance Group ID, if using Instance Group for this node type.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the job flow</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.release_label">
<code class="sig-name descname">release_label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.release_label" title="Permalink to this definition">¶</a></dt>
<dd><p>The release label for the Amazon EMR release</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.scale_down_behavior">
<code class="sig-name descname">scale_down_behavior</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.scale_down_behavior" title="Permalink to this definition">¶</a></dt>
<dd><p>The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an <code class="docutils literal notranslate"><span class="pre">instance</span> <span class="pre">group</span></code> is resized.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.security_configuration">
<code class="sig-name descname">security_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.security_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with <code class="docutils literal notranslate"><span class="pre">release_label</span></code> 4.8.0 or greater</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.service_role">
<code class="sig-name descname">service_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.service_role" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM role that will be assumed by the Amazon EMR service to access AWS resources</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.steps">
<code class="sig-name descname">steps</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.steps" title="Permalink to this definition">¶</a></dt>
<dd><p>List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize the <a class="reference external" href="https://www.terraform.io/docs/configuration/resources.html">lifecycle configuration block</a> with <code class="docutils literal notranslate"><span class="pre">ignore_changes</span></code> if other steps are being managed outside of this provider. This argument is processed in <a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">attribute-as-blocks mode</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionOnFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hadoopJarStep</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jar</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mainClass</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the job flow</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.step_concurrency_level">
<code class="sig-name descname">step_concurrency_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.step_concurrency_level" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of steps that can be executed concurrently. You can specify a maximum of 256 steps. Only valid for EMR clusters with <code class="docutils literal notranslate"><span class="pre">release_label</span></code> 5.28.0 or greater. (default is 1)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>list of tags to apply to the EMR Cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.termination_protection">
<code class="sig-name descname">termination_protection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.termination_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Switch on/off termination protection (default is <code class="docutils literal notranslate"><span class="pre">false</span></code>, except when using multiple master nodes). Before attempting to destroy the resource when termination protection is enabled, this configuration must be applied with its value set to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.Cluster.visible_to_all_users">
<code class="sig-name descname">visible_to_all_users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.Cluster.visible_to_all_users" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default <code class="docutils literal notranslate"><span class="pre">true</span></code></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.emr.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_info=None</em>, <em class="sig-param">applications=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">autoscaling_role=None</em>, <em class="sig-param">bootstrap_actions=None</em>, <em class="sig-param">cluster_state=None</em>, <em class="sig-param">configurations=None</em>, <em class="sig-param">configurations_json=None</em>, <em class="sig-param">core_instance_count=None</em>, <em class="sig-param">core_instance_group=None</em>, <em class="sig-param">core_instance_type=None</em>, <em class="sig-param">custom_ami_id=None</em>, <em class="sig-param">ebs_root_volume_size=None</em>, <em class="sig-param">ec2_attributes=None</em>, <em class="sig-param">instance_groups=None</em>, <em class="sig-param">keep_job_flow_alive_when_no_steps=None</em>, <em class="sig-param">kerberos_attributes=None</em>, <em class="sig-param">log_uri=None</em>, <em class="sig-param">master_instance_group=None</em>, <em class="sig-param">master_instance_type=None</em>, <em class="sig-param">master_public_dns=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">release_label=None</em>, <em class="sig-param">scale_down_behavior=None</em>, <em class="sig-param">security_configuration=None</em>, <em class="sig-param">service_role=None</em>, <em class="sig-param">steps=None</em>, <em class="sig-param">step_concurrency_level=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">termination_protection=None</em>, <em class="sig-param">visible_to_all_users=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_info</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore this provider cannot detect drift from the actual EMR cluster if its value is changed outside this provider.</p></li>
<li><p><strong>applications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of applications for the cluster. Valid values are: <code class="docutils literal notranslate"><span class="pre">Flink</span></code>, <code class="docutils literal notranslate"><span class="pre">Hadoop</span></code>, <code class="docutils literal notranslate"><span class="pre">Hive</span></code>, <code class="docutils literal notranslate"><span class="pre">Mahout</span></code>, <code class="docutils literal notranslate"><span class="pre">Pig</span></code>, <code class="docutils literal notranslate"><span class="pre">Spark</span></code>, and <code class="docutils literal notranslate"><span class="pre">JupyterHub</span></code> (as of EMR 5.14.0). Case insensitive</p></li>
<li><p><strong>autoscaling_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.</p></li>
<li><p><strong>bootstrap_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of bootstrap actions that will be run before Hadoop is started on the cluster nodes. Defined below</p></li>
<li><p><strong>configurations</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – List of configurations supplied for the EMR cluster you are creating</p></li>
<li><p><strong>configurations_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON string for supplying list of configurations for the EMR cluster.</p></li>
<li><p><strong>core_instance_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Use the <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">instance_count</span></code> argument instead. Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster’s master node and use the remainder of the nodes (<code class="docutils literal notranslate"><span class="pre">core_instance_count</span></code>-1) as core nodes. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set. Default <code class="docutils literal notranslate"><span class="pre">1</span></code></p></li>
<li><p><strong>core_instance_group</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Configuration block to use an <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups">Instance Group</a> for the <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-core">core node type</a>. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">core_instance_count</span></code> argument, <code class="docutils literal notranslate"><span class="pre">core_instance_type</span></code> argument, or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set. Detailed below.</p>
</p></li>
<li><p><strong>core_instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Use the <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">instance_type</span></code> argument instead. The EC2 instance type of the slave nodes. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set.</p></li>
<li><p><strong>custom_ami_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.</p></li>
<li><p><strong>ebs_root_volume_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.</p></li>
<li><p><strong>ec2_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Attributes for the EC2 instances running the job flow. Defined below</p></li>
<li><p><strong>instance_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Use the <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> configuration block, <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration block and <cite>``emr.InstanceGroup`</cite> resource(s) &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html">https://www.terraform.io/docs/providers/aws/r/emr_instance_group.html</a>&gt;`_ instead. A list of <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> objects for each instance group in the cluster. Exactly one of <code class="docutils literal notranslate"><span class="pre">master_instance_type</span></code> and <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> must be specified. If <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> is set, then it must contain a configuration block for at least the <code class="docutils literal notranslate"><span class="pre">MASTER</span></code> instance group type (as well as any additional instance groups). Cannot be specified if <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">core_instance_group</span></code> configuration blocks are set. Defined below</p></li>
<li><p><strong>keep_job_flow_alive_when_no_steps</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Switch on/off run cluster with no steps or when all steps are complete (default is on)</p></li>
<li><p><strong>kerberos_attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Kerberos configuration for the cluster. Defined below</p></li>
<li><p><strong>log_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – S3 bucket to write the log files of the job flow. If a value is not provided, logs are not created</p></li>
<li><p><strong>master_instance_group</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Configuration block to use an <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-group-configuration.html#emr-plan-instance-groups">Instance Group</a> for the <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html#emr-plan-master">master node type</a>. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">master_instance_type</span></code> argument or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set. Detailed below.</p>
</p></li>
<li><p><strong>master_instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Use the <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">instance_type</span></code> argument instead. The EC2 instance type of the master node. Cannot be specified if <code class="docutils literal notranslate"><span class="pre">master_instance_group</span></code> or <code class="docutils literal notranslate"><span class="pre">instance_group</span></code> configuration blocks are set.</p></li>
<li><p><strong>master_public_dns</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public DNS name of the master EC2 instance.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `core_instance_group.0.id` - Core node type Instance Group ID, if using Instance Group for this node type.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the job flow</p></li>
<li><p><strong>release_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The release label for the Amazon EMR release</p></li>
<li><p><strong>scale_down_behavior</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an <code class="docutils literal notranslate"><span class="pre">instance</span> <span class="pre">group</span></code> is resized.</p></li>
<li><p><strong>security_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with <code class="docutils literal notranslate"><span class="pre">release_label</span></code> 4.8.0 or greater</p></li>
<li><p><strong>service_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role that will be assumed by the Amazon EMR service to access AWS resources</p></li>
<li><p><strong>steps</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize the <a class="reference external" href="https://www.terraform.io/docs/configuration/resources.html">lifecycle configuration block</a> with <code class="docutils literal notranslate"><span class="pre">ignore_changes</span></code> if other steps are being managed outside of this provider. This argument is processed in <a class="reference external" href="https://www.terraform.io/docs/configuration/attr-as-blocks.html">attribute-as-blocks mode</a>.</p>
</p></li>
<li><p><strong>step_concurrency_level</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of steps that can be executed concurrently. You can specify a maximum of 256 steps. Only valid for EMR clusters with <code class="docutils literal notranslate"><span class="pre">release_label</span></code> 5.28.0 or greater. (default is 1)</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – list of tags to apply to the EMR Cluster</p></li>
<li><p><strong>termination_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Switch on/off termination protection (default is <code class="docutils literal notranslate"><span class="pre">false</span></code>, except when using multiple master nodes). Before attempting to destroy the resource when termination protection is enabled, this configuration must be applied with its value set to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>visible_to_all_users</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
</ul>
</dd>
</dl>
<p>The <strong>bootstrap_actions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the job flow</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>core_instance_group</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_configs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the EMR Cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the job flow</p></li>
</ul>
<p>The <strong>ec2_attributes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalMasterSecurityGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">additionalSlaveSecurityGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emrManagedMasterSecurityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emrManagedSlaveSecurityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceProfile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccessSecurityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>instance_groups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoscaling_policy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_configs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the EMR Cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceRole</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the job flow</p></li>
</ul>
<p>The <strong>kerberos_attributes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">adDomainJoinPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">adDomainJoinUser</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossRealmTrustPrincipalPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kdcAdminPassword</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">realm</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>master_instance_group</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bid_price</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ebs_configs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the EMR Cluster</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the job flow</p></li>
</ul>
<p>The <strong>steps</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionOnFailure</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hadoopJarStep</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">args</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jar</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mainClass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">properties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the job flow</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/emr_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/emr_cluster.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.emr.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.emr.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.emr.InstanceGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.emr.</code><code class="sig-name descname">InstanceGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">autoscaling_policy=None</em>, <em class="sig-param">bid_price=None</em>, <em class="sig-param">cluster_id=None</em>, <em class="sig-param">configurations_json=None</em>, <em class="sig-param">ebs_configs=None</em>, <em class="sig-param">ebs_optimized=None</em>, <em class="sig-param">instance_count=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Elastic MapReduce Cluster Instance Group configuration.
See <a class="reference external" href="https://aws.amazon.com/documentation/emr/">Amazon Elastic MapReduce Documentation</a> for more information.</p>
<blockquote>
<div><p><strong>NOTE:</strong> At this time, Instance Groups cannot be destroyed through the API nor
web interface. Instance Groups are destroyed when the EMR Cluster is destroyed.
this provider will resize any Instance Group to zero when destroying the resource.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>autoscaling_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The autoscaling policy document. This is a JSON formatted string. See <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html">EMR Auto Scaling</a></p>
</p></li>
<li><p><strong>bid_price</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set, the bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>configurations_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON string for supplying list of configurations specific to the EMR instance group. Note that this can only be changed when using EMR release 5.21 or later.</p></li>
<li><p><strong>ebs_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">ebs_config</span></code> blocks as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether an Amazon EBS volume is EBS-optimized. Changing this forces a new resource to be created.</p></li>
<li><p><strong>instance_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – target number of instances for the instance group. defaults to 0.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC2 instance type for all instances in the instance group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human friendly name given to the instance group. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of I/O operations per second (IOPS) that the volume supports.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The volume type. Valid options are ‘gp2’, ‘io1’ and ‘standard’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of EBS Volumes to attach per instance.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/emr_instance_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/emr_instance_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.emr.InstanceGroup.autoscaling_policy">
<code class="sig-name descname">autoscaling_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.autoscaling_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The autoscaling policy document. This is a JSON formatted string. See <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html">EMR Auto Scaling</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.InstanceGroup.bid_price">
<code class="sig-name descname">bid_price</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.bid_price" title="Permalink to this definition">¶</a></dt>
<dd><p>If set, the bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.InstanceGroup.cluster_id">
<code class="sig-name descname">cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.InstanceGroup.configurations_json">
<code class="sig-name descname">configurations_json</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.configurations_json" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON string for supplying list of configurations specific to the EMR instance group. Note that this can only be changed when using EMR release 5.21 or later.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.InstanceGroup.ebs_configs">
<code class="sig-name descname">ebs_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.ebs_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">ebs_config</span></code> blocks as defined below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of I/O operations per second (IOPS) that the volume supports.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The volume type. Valid options are ‘gp2’, ‘io1’ and ‘standard’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of EBS Volumes to attach per instance.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.InstanceGroup.ebs_optimized">
<code class="sig-name descname">ebs_optimized</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.ebs_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether an Amazon EBS volume is EBS-optimized. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.InstanceGroup.instance_count">
<code class="sig-name descname">instance_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.instance_count" title="Permalink to this definition">¶</a></dt>
<dd><p>target number of instances for the instance group. defaults to 0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.InstanceGroup.instance_type">
<code class="sig-name descname">instance_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The EC2 instance type for all instances in the instance group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.InstanceGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Human friendly name given to the instance group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.emr.InstanceGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">autoscaling_policy=None</em>, <em class="sig-param">bid_price=None</em>, <em class="sig-param">cluster_id=None</em>, <em class="sig-param">configurations_json=None</em>, <em class="sig-param">ebs_configs=None</em>, <em class="sig-param">ebs_optimized=None</em>, <em class="sig-param">instance_count=None</em>, <em class="sig-param">instance_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">running_instance_count=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InstanceGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>autoscaling_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The autoscaling policy document. This is a JSON formatted string. See <a class="reference external" href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-automatic-scaling.html">EMR Auto Scaling</a></p>
</p></li>
<li><p><strong>bid_price</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If set, the bid price for each EC2 instance in the instance group, expressed in USD. By setting this attribute, the instance group is being declared as a Spot Instance, and will implicitly create a Spot request. Leave this blank to use On-Demand Instances.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>configurations_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON string for supplying list of configurations specific to the EMR instance group. Note that this can only be changed when using EMR release 5.21 or later.</p></li>
<li><p><strong>ebs_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">ebs_config</span></code> blocks as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>ebs_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether an Amazon EBS volume is EBS-optimized. Changing this forces a new resource to be created.</p></li>
<li><p><strong>instance_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – target number of instances for the instance group. defaults to 0.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The EC2 instance type for all instances in the instance group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human friendly name given to the instance group. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ebs_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">iops</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of I/O operations per second (IOPS) that the volume supports.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The volume type. Valid options are ‘gp2’, ‘io1’ and ‘standard’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumesPerInstance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of EBS Volumes to attach per instance.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/emr_instance_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/emr_instance_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.emr.InstanceGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.emr.InstanceGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.InstanceGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.emr.SecurityConfiguration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.emr.</code><code class="sig-name descname">SecurityConfiguration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">configuration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage AWS EMR Security Configurations</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON formatted Security Configuration</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the EMR Security Configuration. By default generated by this provider.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/emr_security_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/emr_security_configuration.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.emr.SecurityConfiguration.configuration">
<code class="sig-name descname">configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON formatted Security Configuration</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.SecurityConfiguration.creation_date">
<code class="sig-name descname">creation_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.creation_date" title="Permalink to this definition">¶</a></dt>
<dd><p>Date the Security Configuration was created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.SecurityConfiguration.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the EMR Security Configuration. By default generated by this provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.emr.SecurityConfiguration.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.emr.SecurityConfiguration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">configuration=None</em>, <em class="sig-param">creation_date=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecurityConfiguration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON formatted Security Configuration</p></li>
<li><p><strong>creation_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Date the Security Configuration was created</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the EMR Security Configuration. By default generated by this provider.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/emr_security_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/emr_security_configuration.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.emr.SecurityConfiguration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.emr.SecurityConfiguration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.emr.SecurityConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
