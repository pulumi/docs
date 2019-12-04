---
title: Module autoscaling
linktitle: autoscaling
notitle: true
---

<div class="section" id="autoscaling">
<h1>autoscaling<a class="headerlink" href="#autoscaling" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.autoscaling"></span><dl class="class">
<dt id="pulumi_aws.autoscaling.Attachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.autoscaling.</code><code class="sig-name descname">Attachment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alb_target_group_arn=None</em>, <em class="sig-param">autoscaling_group_name=None</em>, <em class="sig-param">elb=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Attachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AutoScaling Attachment resource.</p>
<blockquote>
<div><p><strong>NOTE on AutoScaling Groups and ASG Attachments:</strong> This provider currently provides
both a standalone ASG Attachment resource (describing an ASG attached to
an ELB), and an AutoScaling Group resource with
<code class="docutils literal notranslate"><span class="pre">load_balancers</span></code> defined in-line. At this time you cannot use an ASG with in-line
load balancers in conjunction with an ASG Attachment resource. Doing so will cause a
conflict and will overwrite attachments.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alb_target_group_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an ALB Target Group.</p></li>
<li><p><strong>autoscaling_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of ASG to associate with the ELB.</p></li>
<li><p><strong>elb</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ELB.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_attachment.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Attachment.alb_target_group_arn">
<code class="sig-name descname">alb_target_group_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Attachment.alb_target_group_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an ALB Target Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Attachment.autoscaling_group_name">
<code class="sig-name descname">autoscaling_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Attachment.autoscaling_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of ASG to associate with the ELB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Attachment.elb">
<code class="sig-name descname">elb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Attachment.elb" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ELB.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Attachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alb_target_group_arn=None</em>, <em class="sig-param">autoscaling_group_name=None</em>, <em class="sig-param">elb=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Attachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Attachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alb_target_group_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an ALB Target Group.</p></li>
<li><p><strong>autoscaling_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of ASG to associate with the ELB.</p></li>
<li><p><strong>elb</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ELB.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_attachment.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Attachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Attachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.autoscaling.Attachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Attachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.autoscaling.AwaitableGetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.autoscaling.</code><code class="sig-name descname">AwaitableGetGroupResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">availability_zones=None</em>, <em class="sig-param">default_cooldown=None</em>, <em class="sig-param">desired_capacity=None</em>, <em class="sig-param">health_check_grace_period=None</em>, <em class="sig-param">health_check_type=None</em>, <em class="sig-param">launch_configuration=None</em>, <em class="sig-param">load_balancers=None</em>, <em class="sig-param">max_size=None</em>, <em class="sig-param">min_size=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">new_instances_protected_from_scale_in=None</em>, <em class="sig-param">placement_group=None</em>, <em class="sig-param">service_linked_role_arn=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">target_group_arns=None</em>, <em class="sig-param">termination_policies=None</em>, <em class="sig-param">vpc_zone_identifier=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.AwaitableGetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.autoscaling.GetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.autoscaling.</code><code class="sig-name descname">GetGroupResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">availability_zones=None</em>, <em class="sig-param">default_cooldown=None</em>, <em class="sig-param">desired_capacity=None</em>, <em class="sig-param">health_check_grace_period=None</em>, <em class="sig-param">health_check_type=None</em>, <em class="sig-param">launch_configuration=None</em>, <em class="sig-param">load_balancers=None</em>, <em class="sig-param">max_size=None</em>, <em class="sig-param">min_size=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">new_instances_protected_from_scale_in=None</em>, <em class="sig-param">placement_group=None</em>, <em class="sig-param">service_linked_role_arn=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">target_group_arns=None</em>, <em class="sig-param">termination_policies=None</em>, <em class="sig-param">vpc_zone_identifier=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the Auto Scaling group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.availability_zones">
<code class="sig-name descname">availability_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more Availability Zones for the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.desired_capacity">
<code class="sig-name descname">desired_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.desired_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The desired size of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.health_check_grace_period">
<code class="sig-name descname">health_check_grace_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.health_check_grace_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time, in seconds, that Amazon EC2 Auto Scaling waits before checking the health status of an EC2 instance that has come into service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.health_check_type">
<code class="sig-name descname">health_check_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.health_check_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The service to use for the health checks. The valid values are EC2 and ELB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.launch_configuration">
<code class="sig-name descname">launch_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.launch_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the associated launch configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.load_balancers">
<code class="sig-name descname">load_balancers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.load_balancers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more load balancers associated with the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.max_size">
<code class="sig-name descname">max_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.max_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum size of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.min_size">
<code class="sig-name descname">min_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.min_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum size of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Auto Scaling group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.placement_group">
<code class="sig-name descname">placement_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.placement_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the placement group into which to launch your instances, if any. For more information, see Placement Groups (<a class="reference external" href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html">http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html</a>) in the Amazon Elastic Compute Cloud User Guide.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.service_linked_role_arn">
<code class="sig-name descname">service_linked_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.service_linked_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other AWS services on your behalf.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current state of the group when DeleteAutoScalingGroup is in progress.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.target_group_arns">
<code class="sig-name descname">target_group_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.target_group_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Names (ARN) of the target groups for your load balancer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.termination_policies">
<code class="sig-name descname">termination_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.termination_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>The termination policies for the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.vpc_zone_identifier">
<code class="sig-name descname">vpc_zone_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.vpc_zone_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC ID for the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.GetGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.autoscaling.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.autoscaling.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">availability_zones=None</em>, <em class="sig-param">default_cooldown=None</em>, <em class="sig-param">desired_capacity=None</em>, <em class="sig-param">enabled_metrics=None</em>, <em class="sig-param">force_delete=None</em>, <em class="sig-param">health_check_grace_period=None</em>, <em class="sig-param">health_check_type=None</em>, <em class="sig-param">initial_lifecycle_hooks=None</em>, <em class="sig-param">launch_configuration=None</em>, <em class="sig-param">launch_template=None</em>, <em class="sig-param">load_balancers=None</em>, <em class="sig-param">max_instance_lifetime=None</em>, <em class="sig-param">max_size=None</em>, <em class="sig-param">metrics_granularity=None</em>, <em class="sig-param">min_elb_capacity=None</em>, <em class="sig-param">min_size=None</em>, <em class="sig-param">mixed_instances_policy=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">placement_group=None</em>, <em class="sig-param">protect_from_scale_in=None</em>, <em class="sig-param">service_linked_role_arn=None</em>, <em class="sig-param">suspended_processes=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tags_collection=None</em>, <em class="sig-param">target_group_arns=None</em>, <em class="sig-param">termination_policies=None</em>, <em class="sig-param">vpc_zone_identifiers=None</em>, <em class="sig-param">wait_for_capacity_timeout=None</em>, <em class="sig-param">wait_for_elb_capacity=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AutoScaling Group resource.</p>
<blockquote>
<div><p><strong>Note:</strong> You must specify either <code class="docutils literal notranslate"><span class="pre">launch_configuration</span></code>, <code class="docutils literal notranslate"><span class="pre">launch_template</span></code>, or <code class="docutils literal notranslate"><span class="pre">mixed_instances_policy</span></code>.</p>
</div></blockquote>
<p>A newly-created ASG is initially empty and begins to scale to <code class="docutils literal notranslate"><span class="pre">min_size</span></code> (or
<code class="docutils literal notranslate"><span class="pre">desired_capacity</span></code>, if specified) by launching instances using the provided
Launch Configuration. These instances take time to launch and boot.</p>
<p>On ASG Update, changes to these values also take time to result in the target
number of instances providing service.</p>
<p>This provider provides two mechanisms to help consistently manage ASG scale up
time across dependent resources.</p>
<p>The first is default behavior. This provider waits after ASG creation for
<code class="docutils literal notranslate"><span class="pre">min_size</span></code> (or <code class="docutils literal notranslate"><span class="pre">desired_capacity</span></code>, if specified) healthy instances to show up
in the ASG before continuing.</p>
<p>If <code class="docutils literal notranslate"><span class="pre">min_size</span></code> or <code class="docutils literal notranslate"><span class="pre">desired_capacity</span></code> are changed in a subsequent update,
this provider will also wait for the correct number of healthy instances before
continuing.</p>
<p>This provider considers an instance “healthy” when the ASG reports <code class="docutils literal notranslate"><span class="pre">HealthStatus:</span>
<span class="pre">&quot;Healthy&quot;</span></code> and <code class="docutils literal notranslate"><span class="pre">LifecycleState:</span> <span class="pre">&quot;InService&quot;</span></code>. See the <a class="reference external" href="https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/AutoScalingGroupLifecycle.html">AWS AutoScaling
Docs</a>
for more information on an ASG’s lifecycle.</p>
<p>This provider will wait for healthy instances for up to
<code class="docutils literal notranslate"><span class="pre">wait_for_capacity_timeout</span></code>. If ASG creation is taking more than a few minutes,
it’s worth investigating for scaling activity errors, which can be caused by
problems with the selected Launch Configuration.</p>
<p>Setting <code class="docutils literal notranslate"><span class="pre">wait_for_capacity_timeout</span></code> to <code class="docutils literal notranslate"><span class="pre">&quot;0&quot;</span></code> disables ASG Capacity waiting.</p>
<p>The second mechanism is optional, and affects ASGs with attached ELBs specified
via the <code class="docutils literal notranslate"><span class="pre">load_balancers</span></code> attribute or with ALBs specified with <code class="docutils literal notranslate"><span class="pre">target_group_arns</span></code>.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">min_elb_capacity</span></code> parameter causes this provider to wait for at least the
requested number of instances to show up <code class="docutils literal notranslate"><span class="pre">&quot;InService&quot;</span></code> in all attached ELBs
during ASG creation.  It has no effect on ASG updates.</p>
<p>If <code class="docutils literal notranslate"><span class="pre">wait_for_elb_capacity</span></code> is set, this provider will wait for exactly that number
of Instances to be <code class="docutils literal notranslate"><span class="pre">&quot;InService&quot;</span></code> in all attached ELBs on both creation and
updates.</p>
<p>These parameters can be used to ensure that service is being provided before
this provider moves on. If new instances don’t pass the ELB’s health checks for any
reason, the deployment will time out, and the ASG will be marked as
tainted (i.e. marked to be destroyed in a follow up run).</p>
<p>As with ASG Capacity, this provider will wait for up to <code class="docutils literal notranslate"><span class="pre">wait_for_capacity_timeout</span></code>
for the proper number of instances to be healthy.</p>
<p>If ASG creation takes more than a few minutes, this could indicate one of a
number of configuration problems. See the <a class="reference external" href="https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/elb-troubleshooting.html">AWS Docs on Load Balancer
Troubleshooting</a>
for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of one or more availability zones for the group. This parameter should not be specified when using <code class="docutils literal notranslate"><span class="pre">vpc_zone_identifier</span></code>.</p></li>
<li><p><strong>default_cooldown</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.</p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of Amazon EC2 instances that
should be running in the group. (See also Waiting for
Capacity below.)</p></li>
<li><p><strong>enabled_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of metrics to collect. The allowed values are <code class="docutils literal notranslate"><span class="pre">GroupMinSize</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupMaxSize</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupDesiredCapacity</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupInServiceInstances</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupPendingInstances</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupStandbyInstances</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupTerminatingInstances</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupTotalInstances</span></code>.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `wait_for_capacity_timeout` (Default: &quot;10m&quot;) A maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for ASG instances to be healthy before timing out.  (See also Waiting
for Capacity below.) Setting this to &quot;0&quot; causes
this provider to skip all Capacity Waiting behavior.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it’s in the process of scaling a resource. Normally, this provider
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.</p></li>
<li><p><strong>health_check_grace_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time (in seconds) after instance comes into service before checking health.</p></li>
<li><p><strong>health_check_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – “EC2” or “ELB”. Controls how health checking is done.</p></li>
<li><p><strong>initial_lifecycle_hooks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more
<a class="reference external" href="http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html">Lifecycle Hooks</a>
to attach to the autoscaling group <strong>before</strong> instances are launched. The
syntax is exactly the same as the separate
<cite>``autoscaling.LifecycleHook`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hooks.html">https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hooks.html</a>&gt;`_
resource, without the <code class="docutils literal notranslate"><span class="pre">autoscaling_group_name</span></code> attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use <code class="docutils literal notranslate"><span class="pre">autoscaling.LifecycleHook</span></code> resource.</p></li>
<li><p><strong>launch_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the launch configuration to use.</p></li>
<li><p><strong>launch_template</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.</p></li>
<li><p><strong>load_balancers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use <code class="docutils literal notranslate"><span class="pre">target_group_arns</span></code> instead.</p></li>
<li><p><strong>max_instance_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum amount of time, in seconds, that an instance can be in service</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum size of the auto scale group.</p></li>
<li><p><strong>metrics_granularity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The granularity to associate with the metrics to collect. The only valid value is <code class="docutils literal notranslate"><span class="pre">1Minute</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">1Minute</span></code>.</p></li>
<li><p><strong>min_elb_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Setting this causes this provider to wait for
this number of instances from this autoscaling group to show up healthy in the
ELB only on creation. Updates will not wait on ELB instance number changes.
(See also Waiting for Capacity below.)</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum size of the auto scale group.
(See also Waiting for Capacity below.)</p></li>
<li><p><strong>mixed_instances_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the auto scaling group. By default generated by this provider.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>placement_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the placement group into which you’ll launch your instances, if any.</p></li>
<li><p><strong>protect_from_scale_in</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.</p></li>
<li><p><strong>service_linked_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the service-linked role that the ASG will use to call other AWS services</p></li>
<li><p><strong>suspended_processes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of processes to suspend for the AutoScaling Group. The allowed values are <code class="docutils literal notranslate"><span class="pre">Launch</span></code>, <code class="docutils literal notranslate"><span class="pre">Terminate</span></code>, <code class="docutils literal notranslate"><span class="pre">HealthCheck</span></code>, <code class="docutils literal notranslate"><span class="pre">ReplaceUnhealthy</span></code>, <code class="docutils literal notranslate"><span class="pre">AZRebalance</span></code>, <code class="docutils literal notranslate"><span class="pre">AlarmNotification</span></code>, <code class="docutils literal notranslate"><span class="pre">ScheduledActions</span></code>, <code class="docutils literal notranslate"><span class="pre">AddToLoadBalancer</span></code>.
Note that if you suspend either the <code class="docutils literal notranslate"><span class="pre">Launch</span></code> or <code class="docutils literal notranslate"><span class="pre">Terminate</span></code> process types, it can prevent your autoscaling group from functioning properly.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tag blocks. Tags documented below.</p></li>
<li><p><strong>tags_collection</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tag blocks (maps). Tags documented below.</p></li>
<li><p><strong>target_group_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of <code class="docutils literal notranslate"><span class="pre">alb.TargetGroup</span></code> ARNs, for use with Application or Network Load Balancing.</p></li>
<li><p><strong>termination_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are <code class="docutils literal notranslate"><span class="pre">OldestInstance</span></code>, <code class="docutils literal notranslate"><span class="pre">NewestInstance</span></code>, <code class="docutils literal notranslate"><span class="pre">OldestLaunchConfiguration</span></code>, <code class="docutils literal notranslate"><span class="pre">ClosestToNextInstanceHour</span></code>, <code class="docutils literal notranslate"><span class="pre">OldestLaunchTemplate</span></code>, <code class="docutils literal notranslate"><span class="pre">AllocationStrategy</span></code>, <code class="docutils literal notranslate"><span class="pre">Default</span></code>.</p></li>
<li><p><strong>vpc_zone_identifiers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of subnet IDs to launch resources in.</p></li>
<li><p><strong>wait_for_elb_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Setting this will cause this provider to wait
for exactly this number of healthy instances from this autoscaling group in
all attached load balancers on both create and update operations. (Takes
precedence over <code class="docutils literal notranslate"><span class="pre">min_elb_capacity</span></code> behavior.)
(See also Waiting for Capacity below.)</p></li>
</ul>
</dd>
</dl>
<p>The <strong>initial_lifecycle_hooks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_result</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">heartbeat_timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifecycle_transition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the auto scaling group. By default generated by this provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notification_metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notification_target_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>launch_template</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The autoscaling group id.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the auto scaling group. By default generated by this provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Template version. Can be version number, <code class="docutils literal notranslate"><span class="pre">$Latest</span></code>, or <code class="docutils literal notranslate"><span class="pre">$Default</span></code>. (Default: <code class="docutils literal notranslate"><span class="pre">$Default</span></code>).</p></li>
</ul>
<p>The <strong>mixed_instances_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instancesDistribution</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument containing settings on how to mix on-demand and Spot instances in the Auto Scaling group. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">onDemandAllocationStrategy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Strategy to use when launching on-demand instances. Valid values: <code class="docutils literal notranslate"><span class="pre">prioritized</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">prioritized</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onDemandBaseCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Absolute minimum amount of desired capacity that must be fulfilled by on-demand instances. Default: <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onDemandPercentageAboveBaseCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Percentage split between on-demand and Spot instances above the base on-demand capacity. Default: <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotAllocationStrategy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How to allocate capacity across the Spot pools. Valid values: <code class="docutils literal notranslate"><span class="pre">lowest-price</span></code>, <code class="docutils literal notranslate"><span class="pre">capacity-optimized</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">lowest-price</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotInstancePools</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of Spot pools per availability zone to allocate capacity. EC2 Auto Scaling selects the cheapest Spot pools and evenly allocates Spot capacity across the number of Spot pools that you specify. Default: <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotMaxPrice</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Maximum price per unit hour that the user is willing to pay for the Spot instances. Default: an empty string which means the on-demand price.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">launch_template</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateSpecification</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument defines the Launch Template. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the launch template. Conflicts with <code class="docutils literal notranslate"><span class="pre">launch_template_name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the launch template. Conflicts with <code class="docutils literal notranslate"><span class="pre">launch_template_id</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Template version. Can be version number, <code class="docutils literal notranslate"><span class="pre">$Latest</span></code>, or <code class="docutils literal notranslate"><span class="pre">$Default</span></code>. (Default: <code class="docutils literal notranslate"><span class="pre">$Default</span></code>).</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrides</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of nested arguments provides the ability to specify multiple instance types. This will override the same parameter in the launch template. For on-demand instances, Auto Scaling considers the order of preference of instance types to launch based on the order specified in the overrides list. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Override the instance type in the Launch Template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weightedCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The number of capacity units, which gives the instance type a proportional weight to other instance types.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Key</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">propagateAtLaunch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables propagation of the tag to
Amazon EC2 instances launched via this ASG</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for this AutoScaling Group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.availability_zones">
<code class="sig-name descname">availability_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of one or more availability zones for the group. This parameter should not be specified when using <code class="docutils literal notranslate"><span class="pre">vpc_zone_identifier</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.default_cooldown">
<code class="sig-name descname">default_cooldown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.default_cooldown" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.desired_capacity">
<code class="sig-name descname">desired_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.desired_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of Amazon EC2 instances that
should be running in the group. (See also Waiting for
Capacity below.)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.enabled_metrics">
<code class="sig-name descname">enabled_metrics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.enabled_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of metrics to collect. The allowed values are <code class="docutils literal notranslate"><span class="pre">GroupMinSize</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupMaxSize</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupDesiredCapacity</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupInServiceInstances</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupPendingInstances</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupStandbyInstances</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupTerminatingInstances</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupTotalInstances</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">wait_for_capacity_timeout</span></code> (Default: “10m”) A maximum
<a class="reference external" href="https://golang.org/pkg/time/#ParseDuration">duration</a> that this provider should
wait for ASG instances to be healthy before timing out.  (See also Waiting
for Capacity below.) Setting this to “0” causes
this provider to skip all Capacity Waiting behavior.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.force_delete">
<code class="sig-name descname">force_delete</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.force_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it’s in the process of scaling a resource. Normally, this provider
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.health_check_grace_period">
<code class="sig-name descname">health_check_grace_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.health_check_grace_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Time (in seconds) after instance comes into service before checking health.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.health_check_type">
<code class="sig-name descname">health_check_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.health_check_type" title="Permalink to this definition">¶</a></dt>
<dd><p>“EC2” or “ELB”. Controls how health checking is done.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.initial_lifecycle_hooks">
<code class="sig-name descname">initial_lifecycle_hooks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.initial_lifecycle_hooks" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more
<a class="reference external" href="http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html">Lifecycle Hooks</a>
to attach to the autoscaling group <strong>before</strong> instances are launched. The
syntax is exactly the same as the separate
<cite>``autoscaling.LifecycleHook`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hooks.html">https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hooks.html</a>&gt;`_
resource, without the <code class="docutils literal notranslate"><span class="pre">autoscaling_group_name</span></code> attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use <code class="docutils literal notranslate"><span class="pre">autoscaling.LifecycleHook</span></code> resource.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_result</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">heartbeat_timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifecycle_transition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the auto scaling group. By default generated by this provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notification_metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notification_target_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.launch_configuration">
<code class="sig-name descname">launch_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.launch_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the launch configuration to use.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.launch_template">
<code class="sig-name descname">launch_template</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.launch_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The autoscaling group id.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the auto scaling group. By default generated by this provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Template version. Can be version number, <code class="docutils literal notranslate"><span class="pre">$Latest</span></code>, or <code class="docutils literal notranslate"><span class="pre">$Default</span></code>. (Default: <code class="docutils literal notranslate"><span class="pre">$Default</span></code>).</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.load_balancers">
<code class="sig-name descname">load_balancers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.load_balancers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use <code class="docutils literal notranslate"><span class="pre">target_group_arns</span></code> instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.max_instance_lifetime">
<code class="sig-name descname">max_instance_lifetime</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.max_instance_lifetime" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum amount of time, in seconds, that an instance can be in service</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.max_size">
<code class="sig-name descname">max_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.max_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum size of the auto scale group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.metrics_granularity">
<code class="sig-name descname">metrics_granularity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.metrics_granularity" title="Permalink to this definition">¶</a></dt>
<dd><p>The granularity to associate with the metrics to collect. The only valid value is <code class="docutils literal notranslate"><span class="pre">1Minute</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">1Minute</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.min_elb_capacity">
<code class="sig-name descname">min_elb_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.min_elb_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>Setting this causes this provider to wait for
this number of instances from this autoscaling group to show up healthy in the
ELB only on creation. Updates will not wait on ELB instance number changes.
(See also Waiting for Capacity below.)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.min_size">
<code class="sig-name descname">min_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.min_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum size of the auto scale group.
(See also Waiting for Capacity below.)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.mixed_instances_policy">
<code class="sig-name descname">mixed_instances_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.mixed_instances_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instancesDistribution</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Nested argument containing settings on how to mix on-demand and Spot instances in the Auto Scaling group. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">onDemandAllocationStrategy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Strategy to use when launching on-demand instances. Valid values: <code class="docutils literal notranslate"><span class="pre">prioritized</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">prioritized</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onDemandBaseCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Absolute minimum amount of desired capacity that must be fulfilled by on-demand instances. Default: <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onDemandPercentageAboveBaseCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Percentage split between on-demand and Spot instances above the base on-demand capacity. Default: <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotAllocationStrategy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - How to allocate capacity across the Spot pools. Valid values: <code class="docutils literal notranslate"><span class="pre">lowest-price</span></code>, <code class="docutils literal notranslate"><span class="pre">capacity-optimized</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">lowest-price</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotInstancePools</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of Spot pools per availability zone to allocate capacity. EC2 Auto Scaling selects the cheapest Spot pools and evenly allocates Spot capacity across the number of Spot pools that you specify. Default: <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotMaxPrice</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Maximum price per unit hour that the user is willing to pay for the Spot instances. Default: an empty string which means the on-demand price.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">launch_template</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateSpecification</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Nested argument defines the Launch Template. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the launch template. Conflicts with <code class="docutils literal notranslate"><span class="pre">launch_template_name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the launch template. Conflicts with <code class="docutils literal notranslate"><span class="pre">launch_template_id</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Template version. Can be version number, <code class="docutils literal notranslate"><span class="pre">$Latest</span></code>, or <code class="docutils literal notranslate"><span class="pre">$Default</span></code>. (Default: <code class="docutils literal notranslate"><span class="pre">$Default</span></code>).</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrides</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of nested arguments provides the ability to specify multiple instance types. This will override the same parameter in the launch template. For on-demand instances, Auto Scaling considers the order of preference of instance types to launch based on the order specified in the overrides list. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Override the instance type in the Launch Template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weightedCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The number of capacity units, which gives the instance type a proportional weight to other instance types.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the auto scaling group. By default generated by this provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.placement_group">
<code class="sig-name descname">placement_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.placement_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the placement group into which you’ll launch your instances, if any.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.protect_from_scale_in">
<code class="sig-name descname">protect_from_scale_in</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.protect_from_scale_in" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.service_linked_role_arn">
<code class="sig-name descname">service_linked_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.service_linked_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the service-linked role that the ASG will use to call other AWS services</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.suspended_processes">
<code class="sig-name descname">suspended_processes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.suspended_processes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of processes to suspend for the AutoScaling Group. The allowed values are <code class="docutils literal notranslate"><span class="pre">Launch</span></code>, <code class="docutils literal notranslate"><span class="pre">Terminate</span></code>, <code class="docutils literal notranslate"><span class="pre">HealthCheck</span></code>, <code class="docutils literal notranslate"><span class="pre">ReplaceUnhealthy</span></code>, <code class="docutils literal notranslate"><span class="pre">AZRebalance</span></code>, <code class="docutils literal notranslate"><span class="pre">AlarmNotification</span></code>, <code class="docutils literal notranslate"><span class="pre">ScheduledActions</span></code>, <code class="docutils literal notranslate"><span class="pre">AddToLoadBalancer</span></code>.
Note that if you suspend either the <code class="docutils literal notranslate"><span class="pre">Launch</span></code> or <code class="docutils literal notranslate"><span class="pre">Terminate</span></code> process types, it can prevent your autoscaling group from functioning properly.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tag blocks. Tags documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Key</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">propagateAtLaunch</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Enables propagation of the tag to
Amazon EC2 instances launched via this ASG</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.tags_collection">
<code class="sig-name descname">tags_collection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.tags_collection" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tag blocks (maps). Tags documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.target_group_arns">
<code class="sig-name descname">target_group_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.target_group_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of <code class="docutils literal notranslate"><span class="pre">alb.TargetGroup</span></code> ARNs, for use with Application or Network Load Balancing.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.termination_policies">
<code class="sig-name descname">termination_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.termination_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are <code class="docutils literal notranslate"><span class="pre">OldestInstance</span></code>, <code class="docutils literal notranslate"><span class="pre">NewestInstance</span></code>, <code class="docutils literal notranslate"><span class="pre">OldestLaunchConfiguration</span></code>, <code class="docutils literal notranslate"><span class="pre">ClosestToNextInstanceHour</span></code>, <code class="docutils literal notranslate"><span class="pre">OldestLaunchTemplate</span></code>, <code class="docutils literal notranslate"><span class="pre">AllocationStrategy</span></code>, <code class="docutils literal notranslate"><span class="pre">Default</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.vpc_zone_identifiers">
<code class="sig-name descname">vpc_zone_identifiers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.vpc_zone_identifiers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of subnet IDs to launch resources in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Group.wait_for_elb_capacity">
<code class="sig-name descname">wait_for_elb_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Group.wait_for_elb_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>Setting this will cause this provider to wait
for exactly this number of healthy instances from this autoscaling group in
all attached load balancers on both create and update operations. (Takes
precedence over <code class="docutils literal notranslate"><span class="pre">min_elb_capacity</span></code> behavior.)
(See also Waiting for Capacity below.)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">availability_zones=None</em>, <em class="sig-param">default_cooldown=None</em>, <em class="sig-param">desired_capacity=None</em>, <em class="sig-param">enabled_metrics=None</em>, <em class="sig-param">force_delete=None</em>, <em class="sig-param">health_check_grace_period=None</em>, <em class="sig-param">health_check_type=None</em>, <em class="sig-param">initial_lifecycle_hooks=None</em>, <em class="sig-param">launch_configuration=None</em>, <em class="sig-param">launch_template=None</em>, <em class="sig-param">load_balancers=None</em>, <em class="sig-param">max_instance_lifetime=None</em>, <em class="sig-param">max_size=None</em>, <em class="sig-param">metrics_granularity=None</em>, <em class="sig-param">min_elb_capacity=None</em>, <em class="sig-param">min_size=None</em>, <em class="sig-param">mixed_instances_policy=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">placement_group=None</em>, <em class="sig-param">protect_from_scale_in=None</em>, <em class="sig-param">service_linked_role_arn=None</em>, <em class="sig-param">suspended_processes=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tags_collection=None</em>, <em class="sig-param">target_group_arns=None</em>, <em class="sig-param">termination_policies=None</em>, <em class="sig-param">vpc_zone_identifiers=None</em>, <em class="sig-param">wait_for_capacity_timeout=None</em>, <em class="sig-param">wait_for_elb_capacity=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for this AutoScaling Group</p></li>
<li><p><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of one or more availability zones for the group. This parameter should not be specified when using <code class="docutils literal notranslate"><span class="pre">vpc_zone_identifier</span></code>.</p></li>
<li><p><strong>default_cooldown</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time, in seconds, after a scaling activity completes before another scaling activity can start.</p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of Amazon EC2 instances that
should be running in the group. (See also Waiting for
Capacity below.)</p></li>
<li><p><strong>enabled_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of metrics to collect. The allowed values are <code class="docutils literal notranslate"><span class="pre">GroupMinSize</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupMaxSize</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupDesiredCapacity</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupInServiceInstances</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupPendingInstances</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupStandbyInstances</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupTerminatingInstances</span></code>, <code class="docutils literal notranslate"><span class="pre">GroupTotalInstances</span></code>.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `wait_for_capacity_timeout` (Default: &quot;10m&quot;) A maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for ASG instances to be healthy before timing out.  (See also Waiting
for Capacity below.) Setting this to &quot;0&quot; causes
this provider to skip all Capacity Waiting behavior.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allows deleting the autoscaling group without waiting
for all instances in the pool to terminate.  You can force an autoscaling group to delete
even if it’s in the process of scaling a resource. Normally, this provider
drains all the instances before deleting the group.  This bypasses that
behavior and potentially leaves resources dangling.</p></li>
<li><p><strong>health_check_grace_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time (in seconds) after instance comes into service before checking health.</p></li>
<li><p><strong>health_check_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – “EC2” or “ELB”. Controls how health checking is done.</p></li>
<li><p><strong>initial_lifecycle_hooks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>One or more
<a class="reference external" href="http://docs.aws.amazon.com/autoscaling/latest/userguide/lifecycle-hooks.html">Lifecycle Hooks</a>
to attach to the autoscaling group <strong>before</strong> instances are launched. The
syntax is exactly the same as the separate
<cite>``autoscaling.LifecycleHook`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hooks.html">https://www.terraform.io/docs/providers/aws/r/autoscaling_lifecycle_hooks.html</a>&gt;`_
resource, without the <code class="docutils literal notranslate"><span class="pre">autoscaling_group_name</span></code> attribute. Please note that this will only work when creating
a new autoscaling group. For all other use-cases, please use <code class="docutils literal notranslate"><span class="pre">autoscaling.LifecycleHook</span></code> resource.</p>
</p></li>
<li><p><strong>launch_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the launch configuration to use.</p></li>
<li><p><strong>launch_template</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.</p></li>
<li><p><strong>load_balancers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of elastic load balancer names to add to the autoscaling
group names. Only valid for classic load balancers. For ALBs, use <code class="docutils literal notranslate"><span class="pre">target_group_arns</span></code> instead.</p></li>
<li><p><strong>max_instance_lifetime</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum amount of time, in seconds, that an instance can be in service</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum size of the auto scale group.</p></li>
<li><p><strong>metrics_granularity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The granularity to associate with the metrics to collect. The only valid value is <code class="docutils literal notranslate"><span class="pre">1Minute</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">1Minute</span></code>.</p></li>
<li><p><strong>min_elb_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Setting this causes this provider to wait for
this number of instances from this autoscaling group to show up healthy in the
ELB only on creation. Updates will not wait on ELB instance number changes.
(See also Waiting for Capacity below.)</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum size of the auto scale group.
(See also Waiting for Capacity below.)</p></li>
<li><p><strong>mixed_instances_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing settings to define launch targets for Auto Scaling groups. Defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the auto scaling group. By default generated by this provider.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified
prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>placement_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the placement group into which you’ll launch your instances, if any.</p></li>
<li><p><strong>protect_from_scale_in</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allows setting instance protection. The
autoscaling group will not select instances with this setting for terminination
during scale in events.</p></li>
<li><p><strong>service_linked_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the service-linked role that the ASG will use to call other AWS services</p></li>
<li><p><strong>suspended_processes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of processes to suspend for the AutoScaling Group. The allowed values are <code class="docutils literal notranslate"><span class="pre">Launch</span></code>, <code class="docutils literal notranslate"><span class="pre">Terminate</span></code>, <code class="docutils literal notranslate"><span class="pre">HealthCheck</span></code>, <code class="docutils literal notranslate"><span class="pre">ReplaceUnhealthy</span></code>, <code class="docutils literal notranslate"><span class="pre">AZRebalance</span></code>, <code class="docutils literal notranslate"><span class="pre">AlarmNotification</span></code>, <code class="docutils literal notranslate"><span class="pre">ScheduledActions</span></code>, <code class="docutils literal notranslate"><span class="pre">AddToLoadBalancer</span></code>.
Note that if you suspend either the <code class="docutils literal notranslate"><span class="pre">Launch</span></code> or <code class="docutils literal notranslate"><span class="pre">Terminate</span></code> process types, it can prevent your autoscaling group from functioning properly.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tag blocks. Tags documented below.</p></li>
<li><p><strong>tags_collection</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of tag blocks (maps). Tags documented below.</p></li>
<li><p><strong>target_group_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of <code class="docutils literal notranslate"><span class="pre">alb.TargetGroup</span></code> ARNs, for use with Application or Network Load Balancing.</p></li>
<li><p><strong>termination_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of policies to decide how the instances in the auto scale group should be terminated. The allowed values are <code class="docutils literal notranslate"><span class="pre">OldestInstance</span></code>, <code class="docutils literal notranslate"><span class="pre">NewestInstance</span></code>, <code class="docutils literal notranslate"><span class="pre">OldestLaunchConfiguration</span></code>, <code class="docutils literal notranslate"><span class="pre">ClosestToNextInstanceHour</span></code>, <code class="docutils literal notranslate"><span class="pre">OldestLaunchTemplate</span></code>, <code class="docutils literal notranslate"><span class="pre">AllocationStrategy</span></code>, <code class="docutils literal notranslate"><span class="pre">Default</span></code>.</p></li>
<li><p><strong>vpc_zone_identifiers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of subnet IDs to launch resources in.</p></li>
<li><p><strong>wait_for_elb_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Setting this will cause this provider to wait
for exactly this number of healthy instances from this autoscaling group in
all attached load balancers on both create and update operations. (Takes
precedence over <code class="docutils literal notranslate"><span class="pre">min_elb_capacity</span></code> behavior.)
(See also Waiting for Capacity below.)</p></li>
</ul>
</dd>
</dl>
<p>The <strong>initial_lifecycle_hooks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_result</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">heartbeat_timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lifecycle_transition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the auto scaling group. By default generated by this provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notification_metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">notification_target_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">role_arn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>launch_template</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The autoscaling group id.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the auto scaling group. By default generated by this provider.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Template version. Can be version number, <code class="docutils literal notranslate"><span class="pre">$Latest</span></code>, or <code class="docutils literal notranslate"><span class="pre">$Default</span></code>. (Default: <code class="docutils literal notranslate"><span class="pre">$Default</span></code>).</p></li>
</ul>
<p>The <strong>mixed_instances_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instancesDistribution</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument containing settings on how to mix on-demand and Spot instances in the Auto Scaling group. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">onDemandAllocationStrategy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Strategy to use when launching on-demand instances. Valid values: <code class="docutils literal notranslate"><span class="pre">prioritized</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">prioritized</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onDemandBaseCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Absolute minimum amount of desired capacity that must be fulfilled by on-demand instances. Default: <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">onDemandPercentageAboveBaseCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Percentage split between on-demand and Spot instances above the base on-demand capacity. Default: <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotAllocationStrategy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - How to allocate capacity across the Spot pools. Valid values: <code class="docutils literal notranslate"><span class="pre">lowest-price</span></code>, <code class="docutils literal notranslate"><span class="pre">capacity-optimized</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">lowest-price</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotInstancePools</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of Spot pools per availability zone to allocate capacity. EC2 Auto Scaling selects the cheapest Spot pools and evenly allocates Spot capacity across the number of Spot pools that you specify. Default: <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotMaxPrice</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Maximum price per unit hour that the user is willing to pay for the Spot instances. Default: an empty string which means the on-demand price.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">launch_template</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument containing launch template settings along with the overrides to specify multiple instance types and weights. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateSpecification</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Nested argument defines the Launch Template. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the launch template. Conflicts with <code class="docutils literal notranslate"><span class="pre">launch_template_name</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the launch template. Conflicts with <code class="docutils literal notranslate"><span class="pre">launch_template_id</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Template version. Can be version number, <code class="docutils literal notranslate"><span class="pre">$Latest</span></code>, or <code class="docutils literal notranslate"><span class="pre">$Default</span></code>. (Default: <code class="docutils literal notranslate"><span class="pre">$Default</span></code>).</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">overrides</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of nested arguments provides the ability to specify multiple instance types. This will override the same parameter in the launch template. For on-demand instances, Auto Scaling considers the order of preference of instance types to launch based on the order specified in the overrides list. Defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Override the instance type in the Launch Template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weightedCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The number of capacity units, which gives the instance type a proportional weight to other instance types.</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<p>The <strong>tags</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Key</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">propagateAtLaunch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Enables propagation of the tag to
Amazon EC2 instances launched via this ASG</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.autoscaling.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.autoscaling.LifecycleHook">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.autoscaling.</code><code class="sig-name descname">LifecycleHook</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">autoscaling_group_name=None</em>, <em class="sig-param">default_result=None</em>, <em class="sig-param">heartbeat_timeout=None</em>, <em class="sig-param">lifecycle_transition=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">notification_metadata=None</em>, <em class="sig-param">notification_target_arn=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AutoScaling Lifecycle Hook resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> This provider has two types of ways you can add lifecycle hooks - via
the <code class="docutils literal notranslate"><span class="pre">initial_lifecycle_hook</span></code> attribute from the
<cite>``autoscaling.Group`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/autoscaling_group.html">https://www.terraform.io/docs/providers/aws/r/autoscaling_group.html</a>&gt;`_
resource, or via this one. Hooks added via this resource will not be added
until the autoscaling group has been created, and depending on your
<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/autoscaling_group.html#waiting-for-capacity">capacity</a>
settings, after the initial instances have been launched, creating unintended
behavior. If you need hooks to run on all instances, add them with
<code class="docutils literal notranslate"><span class="pre">initial_lifecycle_hook</span></code> in
<cite>``autoscaling.Group`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/autoscaling_group.html">https://www.terraform.io/docs/providers/aws/r/autoscaling_group.html</a>&gt;`_,
but take care to not duplicate those hooks with this resource.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>autoscaling_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Auto Scaling group to which you want to assign the lifecycle hook</p></li>
<li><p><strong>default_result</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The value for this parameter can be either CONTINUE or ABANDON. The default value for this parameter is ABANDON.</p></li>
<li><p><strong>heartbeat_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Defines the amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the action defined in the DefaultResult parameter</p></li>
<li><p><strong>lifecycle_transition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance state to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/autoscaling/describe-lifecycle-hook-types.html#examples">describe-lifecycle-hook-types</a></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the lifecycle hook.</p></li>
<li><p><strong>notification_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains additional information that you want to include any time Auto Scaling sends a message to the notification target.</p></li>
<li><p><strong>notification_target_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook. This ARN target can be either an SQS queue or an SNS topic.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_lifecycle_hook.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_lifecycle_hook.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.autoscaling.LifecycleHook.autoscaling_group_name">
<code class="sig-name descname">autoscaling_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.autoscaling_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Auto Scaling group to which you want to assign the lifecycle hook</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.LifecycleHook.default_result">
<code class="sig-name descname">default_result</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.default_result" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The value for this parameter can be either CONTINUE or ABANDON. The default value for this parameter is ABANDON.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.LifecycleHook.heartbeat_timeout">
<code class="sig-name descname">heartbeat_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.heartbeat_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the action defined in the DefaultResult parameter</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.LifecycleHook.lifecycle_transition">
<code class="sig-name descname">lifecycle_transition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.lifecycle_transition" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance state to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/autoscaling/describe-lifecycle-hook-types.html#examples">describe-lifecycle-hook-types</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.LifecycleHook.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the lifecycle hook.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.LifecycleHook.notification_metadata">
<code class="sig-name descname">notification_metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.notification_metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains additional information that you want to include any time Auto Scaling sends a message to the notification target.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.LifecycleHook.notification_target_arn">
<code class="sig-name descname">notification_target_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.notification_target_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook. This ARN target can be either an SQS queue or an SNS topic.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.LifecycleHook.role_arn">
<code class="sig-name descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.LifecycleHook.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">autoscaling_group_name=None</em>, <em class="sig-param">default_result=None</em>, <em class="sig-param">heartbeat_timeout=None</em>, <em class="sig-param">lifecycle_transition=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">notification_metadata=None</em>, <em class="sig-param">notification_target_arn=None</em>, <em class="sig-param">role_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LifecycleHook resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>autoscaling_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Auto Scaling group to which you want to assign the lifecycle hook</p></li>
<li><p><strong>default_result</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses or if an unexpected failure occurs. The value for this parameter can be either CONTINUE or ABANDON. The default value for this parameter is ABANDON.</p></li>
<li><p><strong>heartbeat_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Defines the amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the action defined in the DefaultResult parameter</p></li>
<li><p><strong>lifecycle_transition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The instance state to which you want to attach the lifecycle hook. For a list of lifecycle hook types, see <a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/autoscaling/describe-lifecycle-hook-types.html#examples">describe-lifecycle-hook-types</a></p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the lifecycle hook.</p></li>
<li><p><strong>notification_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains additional information that you want to include any time Auto Scaling sends a message to the notification target.</p></li>
<li><p><strong>notification_target_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the notification target that Auto Scaling will use to notify you when an instance is in the transition state for the lifecycle hook. This ARN target can be either an SQS queue or an SNS topic.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_lifecycle_hook.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_lifecycle_hook.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.LifecycleHook.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.autoscaling.LifecycleHook.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.LifecycleHook.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.autoscaling.Notification">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.autoscaling.</code><code class="sig-name descname">Notification</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">group_names=None</em>, <em class="sig-param">notifications=None</em>, <em class="sig-param">topic_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Notification" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AutoScaling Group with Notification support, via SNS Topics. Each of
the <code class="docutils literal notranslate"><span class="pre">notifications</span></code> map to a [Notification Configuration][2] inside Amazon Web
Services, and are applied to each AutoScaling Group you supply.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of AutoScaling Group Names</p></li>
<li><p><strong>notifications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Notification Types that trigger
notifications. Acceptable values are documented [in the AWS documentation here][1]</p></li>
<li><p><strong>topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Topic ARN for notifications to be sent through</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_notification.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_notification.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Notification.group_names">
<code class="sig-name descname">group_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Notification.group_names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of AutoScaling Group Names</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Notification.notifications">
<code class="sig-name descname">notifications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Notification.notifications" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Notification Types that trigger
notifications. Acceptable values are documented [in the AWS documentation here][1]</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Notification.topic_arn">
<code class="sig-name descname">topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Notification.topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Topic ARN for notifications to be sent through</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Notification.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">group_names=None</em>, <em class="sig-param">notifications=None</em>, <em class="sig-param">topic_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Notification.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Notification resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_names</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of AutoScaling Group Names</p></li>
<li><p><strong>notifications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Notification Types that trigger
notifications. Acceptable values are documented [in the AWS documentation here][1]</p></li>
<li><p><strong>topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Topic ARN for notifications to be sent through</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_notification.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_notification.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Notification.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Notification.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.autoscaling.Notification.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Notification.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.autoscaling.Policy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.autoscaling.</code><code class="sig-name descname">Policy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">adjustment_type=None</em>, <em class="sig-param">autoscaling_group_name=None</em>, <em class="sig-param">cooldown=None</em>, <em class="sig-param">estimated_instance_warmup=None</em>, <em class="sig-param">metric_aggregation_type=None</em>, <em class="sig-param">min_adjustment_magnitude=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy_type=None</em>, <em class="sig-param">scaling_adjustment=None</em>, <em class="sig-param">step_adjustments=None</em>, <em class="sig-param">target_tracking_configuration=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AutoScaling Scaling Policy resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> You may want to omit <code class="docutils literal notranslate"><span class="pre">desired_capacity</span></code> attribute from attached <code class="docutils literal notranslate"><span class="pre">autoscaling.Group</span></code>
when using autoscaling policies. It’s good practice to pick either
<a class="reference external" href="https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-manual-scaling.html">manual</a>
or <a class="reference external" href="https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/as-scale-based-on-demand.html">dynamic</a>
(policy-based) scaling.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>adjustment_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are <code class="docutils literal notranslate"><span class="pre">ChangeInCapacity</span></code>, <code class="docutils literal notranslate"><span class="pre">ExactCapacity</span></code>, and <code class="docutils literal notranslate"><span class="pre">PercentChangeInCapacity</span></code>.</p></li>
<li><p><strong>autoscaling_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the autoscaling group.</p></li>
<li><p><strong>cooldown</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.</p></li>
<li><p><strong>estimated_instance_warmup</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group’s specified cooldown period.</p></li>
<li><p><strong>metric_aggregation_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The aggregation type for the policy’s metrics. Valid values are “Minimum”, “Maximum”, and “Average”. Without a value, AWS will treat the aggregation type as “Average”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the dimension.</p></li>
<li><p><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy type, either “SimpleScaling”, “StepScaling” or “TargetTrackingScaling”. If this value isn’t provided, AWS will default to “SimpleScaling.”</p></li>
<li><p><strong>scaling_adjustment</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.</p></li>
<li><p><strong>step_adjustments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of adjustments that manage
group scaling. These have the following structure:</p></li>
<li><p><strong>target_tracking_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A target tracking policy. These have the following structure:</p></li>
</ul>
</dd>
</dl>
<p>The <strong>step_adjustments</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">metricIntervalLowerBound</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The lower bound for the
difference between the alarm threshold and the CloudWatch metric.
Without a value, AWS will treat this bound as infinity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricIntervalUpperBound</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The upper bound for the
difference between the alarm threshold and the CloudWatch metric.
Without a value, AWS will treat this bound as infinity. The upper bound
must be greater than the lower bound.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaling_adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.</p></li>
</ul>
<p>The <strong>target_tracking_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customizedMetricSpecification</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A customized metric. Conflicts with <code class="docutils literal notranslate"><span class="pre">predefined_metric_specification</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">metricDimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The dimensions of the metric.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the dimension.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the dimension.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the metric.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The namespace of the metric.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The statistic of the metric.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unit of the metric.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableScaleIn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether scale in by the target tracking policy is disabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">predefinedMetricSpecification</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A predefined metric. Conflicts with <code class="docutils literal notranslate"><span class="pre">customized_metric_specification</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">predefinedMetricType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The metric type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifies the resource associated with the metric type.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The target value for the metric.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.adjustment_type">
<code class="sig-name descname">adjustment_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.adjustment_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are <code class="docutils literal notranslate"><span class="pre">ChangeInCapacity</span></code>, <code class="docutils literal notranslate"><span class="pre">ExactCapacity</span></code>, and <code class="docutils literal notranslate"><span class="pre">PercentChangeInCapacity</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS to the scaling policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.autoscaling_group_name">
<code class="sig-name descname">autoscaling_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.autoscaling_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the autoscaling group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.cooldown">
<code class="sig-name descname">cooldown</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.cooldown" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.estimated_instance_warmup">
<code class="sig-name descname">estimated_instance_warmup</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.estimated_instance_warmup" title="Permalink to this definition">¶</a></dt>
<dd><p>The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group’s specified cooldown period.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.metric_aggregation_type">
<code class="sig-name descname">metric_aggregation_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.metric_aggregation_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The aggregation type for the policy’s metrics. Valid values are “Minimum”, “Maximum”, and “Average”. Without a value, AWS will treat the aggregation type as “Average”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the dimension.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.policy_type">
<code class="sig-name descname">policy_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.policy_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy type, either “SimpleScaling”, “StepScaling” or “TargetTrackingScaling”. If this value isn’t provided, AWS will default to “SimpleScaling.”</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.scaling_adjustment">
<code class="sig-name descname">scaling_adjustment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.scaling_adjustment" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.step_adjustments">
<code class="sig-name descname">step_adjustments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.step_adjustments" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of adjustments that manage
group scaling. These have the following structure:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">metricIntervalLowerBound</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The lower bound for the
difference between the alarm threshold and the CloudWatch metric.
Without a value, AWS will treat this bound as infinity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricIntervalUpperBound</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The upper bound for the
difference between the alarm threshold and the CloudWatch metric.
Without a value, AWS will treat this bound as infinity. The upper bound
must be greater than the lower bound.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaling_adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Policy.target_tracking_configuration">
<code class="sig-name descname">target_tracking_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.target_tracking_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A target tracking policy. These have the following structure:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customizedMetricSpecification</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A customized metric. Conflicts with <code class="docutils literal notranslate"><span class="pre">predefined_metric_specification</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">metricDimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The dimensions of the metric.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the dimension.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of the dimension.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the metric.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The namespace of the metric.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The statistic of the metric.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unit of the metric.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableScaleIn</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether scale in by the target tracking policy is disabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">predefinedMetricSpecification</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A predefined metric. Conflicts with <code class="docutils literal notranslate"><span class="pre">customized_metric_specification</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">predefinedMetricType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The metric type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Identifies the resource associated with the metric type.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetValue</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The target value for the metric.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Policy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">adjustment_type=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">autoscaling_group_name=None</em>, <em class="sig-param">cooldown=None</em>, <em class="sig-param">estimated_instance_warmup=None</em>, <em class="sig-param">metric_aggregation_type=None</em>, <em class="sig-param">min_adjustment_magnitude=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy_type=None</em>, <em class="sig-param">scaling_adjustment=None</em>, <em class="sig-param">step_adjustments=None</em>, <em class="sig-param">target_tracking_configuration=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Policy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>adjustment_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the adjustment is an absolute number or a percentage of the current capacity. Valid values are <code class="docutils literal notranslate"><span class="pre">ChangeInCapacity</span></code>, <code class="docutils literal notranslate"><span class="pre">ExactCapacity</span></code>, and <code class="docutils literal notranslate"><span class="pre">PercentChangeInCapacity</span></code>.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN assigned by AWS to the scaling policy.</p></li>
<li><p><strong>autoscaling_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the autoscaling group.</p></li>
<li><p><strong>cooldown</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time, in seconds, after a scaling activity completes and before the next scaling activity can start.</p></li>
<li><p><strong>estimated_instance_warmup</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The estimated time, in seconds, until a newly launched instance will contribute CloudWatch metrics. Without a value, AWS will default to the group’s specified cooldown period.</p></li>
<li><p><strong>metric_aggregation_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The aggregation type for the policy’s metrics. Valid values are “Minimum”, “Maximum”, and “Average”. Without a value, AWS will treat the aggregation type as “Average”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the dimension.</p></li>
<li><p><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy type, either “SimpleScaling”, “StepScaling” or “TargetTrackingScaling”. If this value isn’t provided, AWS will default to “SimpleScaling.”</p></li>
<li><p><strong>scaling_adjustment</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.</p></li>
<li><p><strong>step_adjustments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of adjustments that manage
group scaling. These have the following structure:</p></li>
<li><p><strong>target_tracking_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A target tracking policy. These have the following structure:</p></li>
</ul>
</dd>
</dl>
<p>The <strong>step_adjustments</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">metricIntervalLowerBound</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The lower bound for the
difference between the alarm threshold and the CloudWatch metric.
Without a value, AWS will treat this bound as infinity.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricIntervalUpperBound</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The upper bound for the
difference between the alarm threshold and the CloudWatch metric.
Without a value, AWS will treat this bound as infinity. The upper bound
must be greater than the lower bound.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scaling_adjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of members by which to
scale, when the adjustment bounds are breached. A positive value scales
up. A negative value scales down.</p></li>
</ul>
<p>The <strong>target_tracking_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customizedMetricSpecification</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A customized metric. Conflicts with <code class="docutils literal notranslate"><span class="pre">predefined_metric_specification</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">metricDimensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The dimensions of the metric.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the dimension.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the dimension.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the metric.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The namespace of the metric.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The statistic of the metric.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unit of the metric.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">disableScaleIn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether scale in by the target tracking policy is disabled.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">predefinedMetricSpecification</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A predefined metric. Conflicts with <code class="docutils literal notranslate"><span class="pre">customized_metric_specification</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">predefinedMetricType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The metric type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Identifies the resource associated with the metric type.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The target value for the metric.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Policy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.autoscaling.Policy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.autoscaling.Schedule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.autoscaling.</code><code class="sig-name descname">Schedule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">autoscaling_group_name=None</em>, <em class="sig-param">desired_capacity=None</em>, <em class="sig-param">end_time=None</em>, <em class="sig-param">max_size=None</em>, <em class="sig-param">min_size=None</em>, <em class="sig-param">recurrence=None</em>, <em class="sig-param">scheduled_action_name=None</em>, <em class="sig-param">start_time=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AutoScaling Schedule resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>autoscaling_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or Amazon Resource Name (ARN) of the Auto Scaling group.</p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don’t want to change the desired capacity at the scheduled time.</p></li>
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time for this action to end, in “YYYY-MM-DDThh:mm:ssZ” format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don’t want to change the maximum size at the scheduled time.</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don’t want to change the minimum size at the scheduled time.</p></li>
<li><p><strong>recurrence</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.</p></li>
<li><p><strong>scheduled_action_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this scaling action.</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time for this action to start, in “YYYY-MM-DDThh:mm:ssZ” format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_schedule.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_schedule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Schedule.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS to the autoscaling schedule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Schedule.autoscaling_group_name">
<code class="sig-name descname">autoscaling_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.autoscaling_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or Amazon Resource Name (ARN) of the Auto Scaling group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Schedule.desired_capacity">
<code class="sig-name descname">desired_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.desired_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don’t want to change the desired capacity at the scheduled time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Schedule.end_time">
<code class="sig-name descname">end_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time for this action to end, in “YYYY-MM-DDThh:mm:ssZ” format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Schedule.max_size">
<code class="sig-name descname">max_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.max_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don’t want to change the maximum size at the scheduled time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Schedule.min_size">
<code class="sig-name descname">min_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.min_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don’t want to change the minimum size at the scheduled time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Schedule.recurrence">
<code class="sig-name descname">recurrence</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.recurrence" title="Permalink to this definition">¶</a></dt>
<dd><p>The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Schedule.scheduled_action_name">
<code class="sig-name descname">scheduled_action_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.scheduled_action_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this scaling action.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.autoscaling.Schedule.start_time">
<code class="sig-name descname">start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time for this action to start, in “YYYY-MM-DDThh:mm:ssZ” format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Schedule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">autoscaling_group_name=None</em>, <em class="sig-param">desired_capacity=None</em>, <em class="sig-param">end_time=None</em>, <em class="sig-param">max_size=None</em>, <em class="sig-param">min_size=None</em>, <em class="sig-param">recurrence=None</em>, <em class="sig-param">scheduled_action_name=None</em>, <em class="sig-param">start_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Schedule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN assigned by AWS to the autoscaling schedule.</p></li>
<li><p><strong>autoscaling_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or Amazon Resource Name (ARN) of the Auto Scaling group.</p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of EC2 instances that should be running in the group. Default 0.  Set to -1 if you don’t want to change the desired capacity at the scheduled time.</p></li>
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time for this action to end, in “YYYY-MM-DDThh:mm:ssZ” format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.</p></li>
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum size for the Auto Scaling group. Default 0.
Set to -1 if you don’t want to change the maximum size at the scheduled time.</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum size for the Auto Scaling group. Default 0.
Set to -1 if you don’t want to change the minimum size at the scheduled time.</p></li>
<li><p><strong>recurrence</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time when recurring future actions will start. Start time is specified by the user following the Unix cron syntax format.</p></li>
<li><p><strong>scheduled_action_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this scaling action.</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time for this action to start, in “YYYY-MM-DDThh:mm:ssZ” format in UTC/GMT only (for example, 2014-06-01T00:00:00Z ).
If you try to schedule your action in the past, Auto Scaling returns an error message.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_schedule.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/autoscaling_schedule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.autoscaling.Schedule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.autoscaling.Schedule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.Schedule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.autoscaling.get_group">
<code class="sig-prename descclassname">pulumi_aws.autoscaling.</code><code class="sig-name descname">get_group</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.autoscaling.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information on an existing autoscaling group.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – Specify the exact name of the desired autoscaling group.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/autoscaling_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/autoscaling_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
