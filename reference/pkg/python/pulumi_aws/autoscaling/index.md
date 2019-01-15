<div class="section" id="module-pulumi_aws.autoscaling">
<span id="autoscaling"></span><h1>autoscaling<a class="headerlink" href="#module-pulumi_aws.autoscaling" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.autoscaling.Attachment">
<em class="property">class </em><code class="descclassname">pulumi_aws.autoscaling.</code><code class="descname">Attachment</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>alb_target_group_arn=None</em>, <em>autoscaling_group_name=None</em>, <em>elb=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Attachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AutoScaling Attachment resource.</p>
<p>&gt; <strong>NOTE on AutoScaling Groups and ASG Attachments:</strong> Terraform currently provides
both a standalone ASG Attachment resource (describing an ASG attached to
an ELB), and an AutoScaling Group resource with
<cite>load_balancers</cite> defined in-line. At this time you cannot use an ASG with in-line
load balancers in conjunction with an ASG Attachment resource. Doing so will cause a
conflict and will overwrite attachments.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>alb_target_group_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an ALB Target Group.</li>
<li><strong>autoscaling_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of ASG to associate with the ELB.</li>
<li><strong>elb</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ELB.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Attachment.alb_target_group_arn">
<code class="descname">alb_target_group_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Attachment.alb_target_group_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an ALB Target Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Attachment.autoscaling_group_name">
<code class="descname">autoscaling_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Attachment.autoscaling_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of ASG to associate with the ELB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Attachment.elb">
<code class="descname">elb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Attachment.elb" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ELB.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Attachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Attachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Attachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Attachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.autoscaling.GetGroupResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.autoscaling.</code><code class="descname">GetGroupResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>availability_zones=None</em>, <em>default_cooldown=None</em>, <em>desired_capacity=None</em>, <em>health_check_grace_period=None</em>, <em>health_check_type=None</em>, <em>launch_configuration=None</em>, <em>load_balancers=None</em>, <em>max_size=None</em>, <em>min_size=None</em>, <em>new_instances_protected_from_scale_in=None</em>, <em>placement_group=None</em>, <em>service_linked_role_arn=None</em>, <em>status=None</em>, <em>target_group_arns=None</em>, <em>termination_policies=None</em>, <em>vpc_zone_identifier=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the Auto Scaling group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.availability_zones">
<code class="descname">availability_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more Availability Zones for the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.desired_capacity">
<code class="descname">desired_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.desired_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired size of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.health_check_grace_period">
<code class="descname">health_check_grace_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.health_check_grace_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.health_check_type">
<code class="descname">health_check_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.health_check_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The service to use for the health checks. The valid values are EC2 and ELB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.launch_configuration">
<code class="descname">launch_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.launch_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the associated launch configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.load_balancers">
<code class="descname">load_balancers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.load_balancers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more load balancers associated with the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.max_size">
<code class="descname">max_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.max_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum size of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.min_size">
<code class="descname">min_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.min_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum size of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.placement_group">
<code class="descname">placement_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.placement_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the placement group into which to launch your instances, if any. For more information, see Placement Groups (<a class="reference external" href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html">http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html</a>) in the Amazon Elastic Compute Cloud User Guide.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.service_linked_role_arn">
<code class="descname">service_linked_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.service_linked_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other AWS services on your behalf.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current state of the group when DeleteAutoScalingGroup is in progress.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.target_group_arns">
<code class="descname">target_group_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.target_group_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Names (ARN) of the target groups for your load balancer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.termination_policies">
<code class="descname">termination_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.termination_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>The termination policies for the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.vpc_zone_identifier">
<code class="descname">vpc_zone_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.vpc_zone_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC ID for the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.autoscaling.Group">
<em class="property">class </em><code class="descclassname">pulumi_aws.autoscaling.</code><code class="descname">Group</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>availability_zones=None</em>, <em>default_cooldown=None</em>, <em>desired_capacity=None</em>, <em>enabled_metrics=None</em>, <em>force_delete=None</em>, <em>health_check_grace_period=None</em>, <em>health_check_type=None</em>, <em>initial_lifecycle_hooks=None</em>, <em>launch_configuration=None</em>, <em>launch_template=None</em>, <em>load_balancers=None</em>, <em>max_size=None</em>, <em>metrics_granularity=None</em>, <em>min_elb_capacity=None</em>, <em>min_size=None</em>, <em>mixed_instances_policy=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>placement_group=None</em>, <em>protect_from_scale_in=None</em>, <em>service_linked_role_arn=None</em>, <em>suspended_processes=None</em>, <em>tags=None</em>, <em>tags_collection=None</em>, <em>target_group_arns=None</em>, <em>termination_policies=None</em>, <em>vpc_zone_identifiers=None</em>, <em>wait_for_capacity_timeout=None</em>, <em>wait_for_elb_capacity=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AutoScaling Group resource.</p>
<p>-&gt; <strong>Note:</strong> You must specify either <cite>launch_configuration</cite>, <cite>launch_template</cite>, or <cite>mixed_instances_policy</cite>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of one or more availability zones for the group. This parameter should not be specified when using <cite>vpc_zone_identifier</cite>.</li>
<li><strong>default_cooldown</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.</li>
<li><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of Amazon EC2 instances that
should be running in the group. (See also Waiting for
Capacity below.)</li>
<li><strong>enabled_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of metrics to collect. The allowed values are <cite>GroupMinSize</cite>, <cite>GroupMaxSize</cite>, <cite>GroupDesiredCapacity</cite>, <cite>GroupInServiceInstances</cite>, <cite>GroupPendingInstances</cite>, <cite>GroupStandbyInstances</cite>, <cite>GroupTerminatingInstances</cite>, <cite>GroupTotalInstances</cite>.
* <cite>wait_for_capacity_timeout</cite> (Default: “10m”) A maximum
[duration](<a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">https://golang.org/pkg/time/#ParseDuration</a>) that Terraform should
wait for ASG instances to be healthy before timing out.  (See also Waiting
for Capacity below.) Setting this to “0” causes
Terraform to skip all Capacity Waiting behavior.</li>
<li><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it’s in the process of scaling a resource. Normally, Terraform
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.</li>
<li><strong>health_check_grace_period</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Time (in seconds) after instance comes into service before checking health.</li>
<li><strong>health_check_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – “EC2” or “ELB”. Controls how health checking is done.</li>
<li><strong>initial_lifecycle_hooks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more
[Lifecycle Hooks](<a class="reference external" href="http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html">http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html</a>)
to attach to the autoscaling group <strong>before</strong> instances are launched. The
syntax is exactly the same as the separate
[<cite>aws_autoscaling_lifecycle_hook</cite>](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hooks.html">https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hooks.html</a>)
resource, without the <cite>autoscaling_group_name</cite> attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use <cite>aws_autoscaling_lifecycle_hook</cite> resource.</li>
<li><strong>launch_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the launch configuration to use.</li>
<li><strong>launch_template</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument with Launch template specification to use to launch instances. Defined below.</li>
<li><strong>load_balancers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use <cite>target_group_arns</cite> instead.</li>
<li><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum size of the auto scale group.</li>
<li><strong>metrics_granularity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The granularity to associate with the metrics to collect. The only valid value is <cite>1Minute</cite>. Default is <cite>1Minute</cite>.</li>
<li><strong>min_elb_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Setting this causes Terraform to wait for
this number of instances to show up healthy in the ELB only on creation.
Updates will not wait on ELB instance number changes.
(See also Waiting for Capacity below.)</li>
<li><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The minimum size of the auto scale group.
(See also Waiting for Capacity below.)</li>
<li><strong>mixed_instances_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the auto scaling group. By default generated by Terraform.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <cite>name</cite>.</li>
<li><strong>placement_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the placement group into which you’ll launch your instances, if any.</li>
<li><strong>protect_from_scale_in</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.</li>
<li><strong>service_linked_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the service-linked role that the ASG will use to call other AWS services</li>
<li><strong>suspended_processes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of processes to suspend for the AutoScaling Group. The allowed values are <cite>Launch</cite>, <cite>Terminate</cite>, <cite>HealthCheck</cite>, <cite>ReplaceUnhealthy</cite>, <cite>AZRebalance</cite>, <cite>AlarmNotification</cite>, <cite>ScheduledActions</cite>, <cite>AddToLoadBalancer</cite>.
Note that if you suspend either the <cite>Launch</cite> or <cite>Terminate</cite> process types, it can prevent your autoscaling group from functioning properly.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tag blocks. Tags documented below.</li>
<li><strong>tags_collection</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tag blocks (maps). Tags documented below.</li>
<li><strong>target_group_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of <cite>aws_alb_target_group</cite> ARNs, for use with Application Load Balancing.</li>
<li><strong>termination_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are <cite>OldestInstance</cite>, <cite>NewestInstance</cite>, <cite>OldestLaunchConfiguration</cite>, <cite>ClosestToNextInstanceHour</cite>, <cite>Default</cite>.</li>
<li><strong>vpc_zone_identifiers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of subnet IDs to launch resources in.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] wait_for_capacity_timeout
:param pulumi.Input[int] wait_for_elb_capacity: Setting this will cause Terraform to wait</p>
<blockquote>
<div>for exactly this number of healthy instances in all attached load balancers
on both create and update operations. (Takes precedence over
<cite>min_elb_capacity</cite> behavior.)
(See also Waiting for Capacity below.)</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for this AutoScaling Group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.availability_zones">
<code class="descname">availability_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of one or more availability zones for the group. This parameter should not be specified when using <cite>vpc_zone_identifier</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.default_cooldown">
<code class="descname">default_cooldown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.default_cooldown" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.desired_capacity">
<code class="descname">desired_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.desired_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of Amazon EC2 instances that
should be running in the group. (See also Waiting for
Capacity below.)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.enabled_metrics">
<code class="descname">enabled_metrics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.enabled_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of metrics to collect. The allowed values are <cite>GroupMinSize</cite>, <cite>GroupMaxSize</cite>, <cite>GroupDesiredCapacity</cite>, <cite>GroupInServiceInstances</cite>, <cite>GroupPendingInstances</cite>, <cite>GroupStandbyInstances</cite>, <cite>GroupTerminatingInstances</cite>, <cite>GroupTotalInstances</cite>.
* <cite>wait_for_capacity_timeout</cite> (Default: “10m”) A maximum
[duration](<a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">https://golang.org/pkg/time/#ParseDuration</a>) that Terraform should
wait for ASG instances to be healthy before timing out.  (See also Waiting
for Capacity below.) Setting this to “0” causes
Terraform to skip all Capacity Waiting behavior.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.force_delete">
<code class="descname">force_delete</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.force_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it’s in the process of scaling a resource. Normally, Terraform
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.health_check_grace_period">
<code class="descname">health_check_grace_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.health_check_grace_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Time (in seconds) after instance comes into service before checking health.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.health_check_type">
<code class="descname">health_check_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.health_check_type" title="Permalink to this definition">¶</a></dt>
<dd><p>“EC2” or “ELB”. Controls how health checking is done.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.initial_lifecycle_hooks">
<code class="descname">initial_lifecycle_hooks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.initial_lifecycle_hooks" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more
[Lifecycle Hooks](<a class="reference external" href="http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html">http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html</a>)
to attach to the autoscaling group <strong>before</strong> instances are launched. The
syntax is exactly the same as the separate
[<cite>aws_autoscaling_lifecycle_hook</cite>](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hooks.html">https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hooks.html</a>)
resource, without the <cite>autoscaling_group_name</cite> attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use <cite>aws_autoscaling_lifecycle_hook</cite> resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.launch_configuration">
<code class="descname">launch_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.launch_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the launch configuration to use.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.launch_template">
<code class="descname">launch_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.launch_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument with Launch template specification to use to launch instances. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.load_balancers">
<code class="descname">load_balancers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.load_balancers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use <cite>target_group_arns</cite> instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.max_size">
<code class="descname">max_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.max_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum size of the auto scale group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.metrics_granularity">
<code class="descname">metrics_granularity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.metrics_granularity" title="Permalink to this definition">¶</a></dt>
<dd><p>The granularity to associate with the metrics to collect. The only valid value is <cite>1Minute</cite>. Default is <cite>1Minute</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.min_elb_capacity">
<code class="descname">min_elb_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.min_elb_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>Setting this causes Terraform to wait for
this number of instances to show up healthy in the ELB only on creation.
Updates will not wait on ELB instance number changes.
(See also Waiting for Capacity below.)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.min_size">
<code class="descname">min_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.min_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum size of the auto scale group.
(See also Waiting for Capacity below.)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.mixed_instances_policy">
<code class="descname">mixed_instances_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.mixed_instances_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the auto scaling group. By default generated by Terraform.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified
prefix. Conflicts with <cite>name</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.placement_group">
<code class="descname">placement_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.placement_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the placement group into which you’ll launch your instances, if any.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.protect_from_scale_in">
<code class="descname">protect_from_scale_in</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.protect_from_scale_in" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.service_linked_role_arn">
<code class="descname">service_linked_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.service_linked_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the service-linked role that the ASG will use to call other AWS services</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.suspended_processes">
<code class="descname">suspended_processes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.suspended_processes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of processes to suspend for the AutoScaling Group. The allowed values are <cite>Launch</cite>, <cite>Terminate</cite>, <cite>HealthCheck</cite>, <cite>ReplaceUnhealthy</cite>, <cite>AZRebalance</cite>, <cite>AlarmNotification</cite>, <cite>ScheduledActions</cite>, <cite>AddToLoadBalancer</cite>.
Note that if you suspend either the <cite>Launch</cite> or <cite>Terminate</cite> process types, it can prevent your autoscaling group from functioning properly.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tag blocks. Tags documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.tags_collection">
<code class="descname">tags_collection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.tags_collection" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tag blocks (maps). Tags documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.target_group_arns">
<code class="descname">target_group_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.target_group_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of <cite>aws_alb_target_group</cite> ARNs, for use with Application Load Balancing.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.termination_policies">
<code class="descname">termination_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.termination_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are <cite>OldestInstance</cite>, <cite>NewestInstance</cite>, <cite>OldestLaunchConfiguration</cite>, <cite>ClosestToNextInstanceHour</cite>, <cite>Default</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.vpc_zone_identifiers">
<code class="descname">vpc_zone_identifiers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.vpc_zone_identifiers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of subnet IDs to launch resources in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.wait_for_elb_capacity">
<code class="descname">wait_for_elb_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.wait_for_elb_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>Setting this will cause Terraform to wait
for exactly this number of healthy instances in all attached load balancers
on both create and update operations. (Takes precedence over
<cite>min_elb_capacity</cite> behavior.)
(See also Waiting for Capacity below.)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Group.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Group.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.autoscaling.LifecycleHook">
<em class="property">class </em><code class="descclassname">pulumi_aws.autoscaling.</code><code class="descname">LifecycleHook</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>autoscaling_group_name=None</em>, <em>default_result=None</em>, <em>heartbeat_timeout=None</em>, <em>lifecycle_transition=None</em>, <em>name=None</em>, <em>notification_metadata=None</em>, <em>notification_target_arn=None</em>, <em>role_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AutoScaling Lifecycle Hook resource.</p>
<p>&gt; <strong>NOTE:</strong> Terraform has two types of ways you can add lifecycle hooks - via
the <cite>initial_lifecycle_hook</cite> attribute from the
[<cite>aws_autoscaling_group</cite>](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/autoscaling_group.html">https://www.terraform.io/docs/providers/aws/r/autoscaling_group.html</a>)
resource, or via this one. Hooks added via this resource will not be added
until the autoscaling group has been created, and depending on your
[capacity](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/autoscaling_group.html#waiting-for-capacity">https://www.terraform.io/docs/providers/aws/r/autoscaling_group.html#waiting-for-capacity</a>)
settings, after the initial instances have been launched, creating unintended
behavior. If you need hooks to run on all instances, add them with
<cite>initial_lifecycle_hook</cite> in
[<cite>aws_autoscaling_group</cite>](<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/autoscaling_group.html">https://www.terraform.io/docs/providers/aws/r/autoscaling_group.html</a>),
but take care to not duplicate those hooks with this resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>autoscaling_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Auto Scaling group to which you want to assign the lifecycle hook</li>
<li><strong>default_result</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The value for this parameter can be either CONTINUE or ABANDON. The default value for this parameter is ABANDON.</li>
<li><strong>heartbeat_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Defines the amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the action defined in the DefaultResult parameter</li>
<li><strong>lifecycle_transition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance state to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see [describe-lifecycle-hook-types](<a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/autoscaling/describe-lifecycle-hook-types.html#examples">https://docs.aws.amazon.com/cli/latest/reference/autoscaling/describe-lifecycle-hook-types.html#examples</a>)</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the lifecycle hook.</li>
<li><strong>notification_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains additional information that you want to include any time Auto Scaling sends a message to the notification target.</li>
<li><strong>notification_target_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook. This ARN target can be either an SQS queue or an SNS topic.</li>
<li><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.autoscaling.LifecycleHook.autoscaling_group_name">
<code class="descname">autoscaling_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.autoscaling_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Auto Scaling group to which you want to assign the lifecycle hook</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.LifecycleHook.default_result">
<code class="descname">default_result</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.default_result" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The value for this parameter can be either CONTINUE or ABANDON. The default value for this parameter is ABANDON.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.LifecycleHook.heartbeat_timeout">
<code class="descname">heartbeat_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.heartbeat_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the action defined in the DefaultResult parameter</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.LifecycleHook.lifecycle_transition">
<code class="descname">lifecycle_transition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.lifecycle_transition" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance state to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see [describe-lifecycle-hook-types](<a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/autoscaling/describe-lifecycle-hook-types.html#examples">https://docs.aws.amazon.com/cli/latest/reference/autoscaling/describe-lifecycle-hook-types.html#examples</a>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.LifecycleHook.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the lifecycle hook.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.LifecycleHook.notification_metadata">
<code class="descname">notification_metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.notification_metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains additional information that you want to include any time Auto Scaling sends a message to the notification target.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.LifecycleHook.notification_target_arn">
<code class="descname">notification_target_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.notification_target_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook. This ARN target can be either an SQS queue or an SNS topic.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.LifecycleHook.role_arn">
<code class="descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.LifecycleHook.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.LifecycleHook.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.autoscaling.Notification">
<em class="property">class </em><code class="descclassname">pulumi_aws.autoscaling.</code><code class="descname">Notification</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>group_names=None</em>, <em>notifications=None</em>, <em>topic_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Notification" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AutoScaling Group with Notification support, via SNS Topics. Each of
the <cite>notifications</cite> map to a [Notification Configuration][2] inside Amazon Web
Services, and are applied to each AutoScaling Group you supply.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>group_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of AutoScaling Group Names</li>
<li><strong>notifications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Notification Types that trigger
notifications. Acceptable values are documented [in the AWS documentation here][1]</li>
<li><strong>topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Topic ARN for notifications to be sent through</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Notification.group_names">
<code class="descname">group_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Notification.group_names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of AutoScaling Group Names</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Notification.notifications">
<code class="descname">notifications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Notification.notifications" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Notification Types that trigger
notifications. Acceptable values are documented [in the AWS documentation here][1]</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Notification.topic_arn">
<code class="descname">topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Notification.topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Topic ARN for notifications to be sent through</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Notification.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Notification.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Notification.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Notification.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.autoscaling.Policy">
<em class="property">class </em><code class="descclassname">pulumi_aws.autoscaling.</code><code class="descname">Policy</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>adjustment_type=None</em>, <em>autoscaling_group_name=None</em>, <em>cooldown=None</em>, <em>estimated_instance_warmup=None</em>, <em>metric_aggregation_type=None</em>, <em>min_adjustment_magnitude=None</em>, <em>min_adjustment_step=None</em>, <em>name=None</em>, <em>policy_type=None</em>, <em>scaling_adjustment=None</em>, <em>step_adjustments=None</em>, <em>target_tracking_configuration=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AutoScaling Scaling Policy resource.</p>
<p>&gt; <strong>NOTE:</strong> You may want to omit <cite>desired_capacity</cite> attribute from attached <cite>aws_autoscaling_group</cite>
when using autoscaling policies. It’s good practice to pick either
[manual](<a class="reference external" href="https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-manual-scaling.html">https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-manual-scaling.html</a>)
or [dynamic](<a class="reference external" href="https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-scale-based-on-demand.html">https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-scale-based-on-demand.html</a>)
(policy-based) scaling.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>adjustment_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are <cite>ChangeInCapacity</cite>, <cite>ExactCapacity</cite>, and <cite>PercentChangeInCapacity</cite>.</li>
<li><strong>autoscaling_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the autoscaling group.</li>
<li><strong>cooldown</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.</li>
<li><strong>estimated_instance_warmup</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group’s specified cooldown period.</li>
<li><strong>metric_aggregation_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The aggregation type for the policy’s metrics. Valid values are “Minimum”, “Maximum”, and “Average”. Without a value, AWS will treat the aggregation type as “Average”.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[int] min_adjustment_magnitude
:param pulumi.Input[int] min_adjustment_step: Use <cite>min_adjustment_magnitude</cite> instead.
:param pulumi.Input[str] name: The name of the dimension.
:param pulumi.Input[str] policy_type: The policy type, either “SimpleScaling”, “StepScaling” or “TargetTrackingScaling”. If this value isn’t provided, AWS will default to “SimpleScaling.”
:param pulumi.Input[int] scaling_adjustment: The number of members by which to</p>
<blockquote>
<div>scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.</div></blockquote>
<p>:param pulumi.Input[list] step_adjustments
:param pulumi.Input[dict] target_tracking_configuration: A target tracking policy. These have the following structure:</p>
<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.adjustment_type">
<code class="descname">adjustment_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.adjustment_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are <cite>ChangeInCapacity</cite>, <cite>ExactCapacity</cite>, and <cite>PercentChangeInCapacity</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS to the scaling policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.autoscaling_group_name">
<code class="descname">autoscaling_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.autoscaling_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the autoscaling group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.cooldown">
<code class="descname">cooldown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.cooldown" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.estimated_instance_warmup">
<code class="descname">estimated_instance_warmup</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.estimated_instance_warmup" title="Permalink to this definition">¶</a></dt>
<dd><p>The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group’s specified cooldown period.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.metric_aggregation_type">
<code class="descname">metric_aggregation_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.metric_aggregation_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The aggregation type for the policy’s metrics. Valid values are “Minimum”, “Maximum”, and “Average”. Without a value, AWS will treat the aggregation type as “Average”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.min_adjustment_step">
<code class="descname">min_adjustment_step</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.min_adjustment_step" title="Permalink to this definition">¶</a></dt>
<dd><p>Use <cite>min_adjustment_magnitude</cite> instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the dimension.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.policy_type">
<code class="descname">policy_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.policy_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy type, either “SimpleScaling”, “StepScaling” or “TargetTrackingScaling”. If this value isn’t provided, AWS will default to “SimpleScaling.”</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.scaling_adjustment">
<code class="descname">scaling_adjustment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.scaling_adjustment" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.target_tracking_configuration">
<code class="descname">target_tracking_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.target_tracking_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A target tracking policy. These have the following structure:</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Policy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Policy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.autoscaling.Schedule">
<em class="property">class </em><code class="descclassname">pulumi_aws.autoscaling.</code><code class="descname">Schedule</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>autoscaling_group_name=None</em>, <em>desired_capacity=None</em>, <em>end_time=None</em>, <em>max_size=None</em>, <em>min_size=None</em>, <em>recurrence=None</em>, <em>scheduled_action_name=None</em>, <em>start_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AutoScaling Schedule resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>autoscaling_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or Amazon Resource Name (ARN) of the Auto Scaling group.</li>
<li><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don’t want to change the desired capacity at the scheduled time.</li>
<li><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time for this action to end, in “YYYY-MM-DDThh:mm:ssZ” format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.</li>
<li><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don’t want to change the maximum size at the scheduled time.</li>
<li><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don’t want to change the minimum size at the scheduled time.</li>
<li><strong>recurrence</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.</li>
<li><strong>scheduled_action_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this scaling action.</li>
<li><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time for this action to start, in “YYYY-MM-DDThh:mm:ssZ” format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Schedule.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS to the autoscaling schedule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Schedule.autoscaling_group_name">
<code class="descname">autoscaling_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.autoscaling_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or Amazon Resource Name (ARN) of the Auto Scaling group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Schedule.desired_capacity">
<code class="descname">desired_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.desired_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don’t want to change the desired capacity at the scheduled time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Schedule.end_time">
<code class="descname">end_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time for this action to end, in “YYYY-MM-DDThh:mm:ssZ” format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Schedule.max_size">
<code class="descname">max_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.max_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don’t want to change the maximum size at the scheduled time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Schedule.min_size">
<code class="descname">min_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.min_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don’t want to change the minimum size at the scheduled time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Schedule.recurrence">
<code class="descname">recurrence</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.recurrence" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Schedule.scheduled_action_name">
<code class="descname">scheduled_action_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.scheduled_action_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this scaling action.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Schedule.start_time">
<code class="descname">start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time for this action to start, in “YYYY-MM-DDThh:mm:ssZ” format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Schedule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Schedule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.autoscaling.get_group">
<code class="descclassname">pulumi_aws.autoscaling.</code><code class="descname">get_group</code><span class="sig-paren">(</span><em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information on an existing autoscaling group.</p>
</dd></dl>

</div>
