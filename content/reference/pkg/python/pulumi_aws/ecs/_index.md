---
---

<div class="section" id="module-pulumi_aws.ecs">
<span id="ecs"></span><h1>ecs<a class="headerlink" href="#module-pulumi_aws.ecs" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.ecs.Cluster">
<em class="property">class </em><code class="descclassname">pulumi_aws.ecs.</code><code class="descname">Cluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecs.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an ECS cluster.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.ecs.Cluster.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Cluster.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) that identifies the cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Cluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Cluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ecs.Cluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecs.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ecs.Cluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecs.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ecs.GetClusterResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ecs.</code><code class="descname">GetClusterResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>cluster_name=None</em>, <em>pending_tasks_count=None</em>, <em>registered_container_instances_count=None</em>, <em>running_tasks_count=None</em>, <em>status=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecs.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="attribute">
<dt id="pulumi_aws.ecs.GetClusterResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetClusterResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the ECS Cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetClusterResult.pending_tasks_count">
<code class="descname">pending_tasks_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetClusterResult.pending_tasks_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of pending tasks for the ECS Cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetClusterResult.registered_container_instances_count">
<code class="descname">registered_container_instances_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetClusterResult.registered_container_instances_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of registered container instances for the ECS Cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetClusterResult.running_tasks_count">
<code class="descname">running_tasks_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetClusterResult.running_tasks_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of running tasks for the ECS Cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetClusterResult.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetClusterResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the ECS Cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetClusterResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ecs.GetContainerDefinitionResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ecs.</code><code class="descname">GetContainerDefinitionResult</code><span class="sig-paren">(</span><em>container_name=None</em>, <em>cpu=None</em>, <em>disable_networking=None</em>, <em>docker_labels=None</em>, <em>environment=None</em>, <em>image=None</em>, <em>image_digest=None</em>, <em>memory=None</em>, <em>memory_reservation=None</em>, <em>task_definition=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecs.GetContainerDefinitionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getContainerDefinition.</p>
<dl class="attribute">
<dt id="pulumi_aws.ecs.GetContainerDefinitionResult.cpu">
<code class="descname">cpu</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetContainerDefinitionResult.cpu" title="Permalink to this definition">¶</a></dt>
<dd><p>The CPU limit for this container definition</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetContainerDefinitionResult.disable_networking">
<code class="descname">disable_networking</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetContainerDefinitionResult.disable_networking" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicator if networking is disabled</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetContainerDefinitionResult.docker_labels">
<code class="descname">docker_labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetContainerDefinitionResult.docker_labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Set docker labels</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetContainerDefinitionResult.environment">
<code class="descname">environment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetContainerDefinitionResult.environment" title="Permalink to this definition">¶</a></dt>
<dd><p>The environment in use</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetContainerDefinitionResult.image">
<code class="descname">image</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetContainerDefinitionResult.image" title="Permalink to this definition">¶</a></dt>
<dd><p>The docker image in use, including the digest</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetContainerDefinitionResult.image_digest">
<code class="descname">image_digest</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetContainerDefinitionResult.image_digest" title="Permalink to this definition">¶</a></dt>
<dd><p>The digest of the docker image in use</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetContainerDefinitionResult.memory">
<code class="descname">memory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetContainerDefinitionResult.memory" title="Permalink to this definition">¶</a></dt>
<dd><p>The memory limit for this container definition</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetContainerDefinitionResult.memory_reservation">
<code class="descname">memory_reservation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetContainerDefinitionResult.memory_reservation" title="Permalink to this definition">¶</a></dt>
<dd><p>The soft limit (in MiB) of memory to reserve for the container. When system memory is under contention, Docker attempts to keep the container memory to this soft limit</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetContainerDefinitionResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetContainerDefinitionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ecs.GetServiceResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ecs.</code><code class="descname">GetServiceResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>cluster_arn=None</em>, <em>desired_count=None</em>, <em>launch_type=None</em>, <em>scheduling_strategy=None</em>, <em>service_name=None</em>, <em>task_definition=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecs.GetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getService.</p>
<dl class="attribute">
<dt id="pulumi_aws.ecs.GetServiceResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetServiceResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the ECS Service</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetServiceResult.desired_count">
<code class="descname">desired_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetServiceResult.desired_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of tasks for the ECS Service</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetServiceResult.launch_type">
<code class="descname">launch_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetServiceResult.launch_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The launch type for the ECS Service</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetServiceResult.scheduling_strategy">
<code class="descname">scheduling_strategy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetServiceResult.scheduling_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>The scheduling strategy for the ECS Service</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetServiceResult.task_definition">
<code class="descname">task_definition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetServiceResult.task_definition" title="Permalink to this definition">¶</a></dt>
<dd><p>The family for the latest ACTIVE revision</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetServiceResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ecs.GetTaskDefinitionResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ecs.</code><code class="descname">GetTaskDefinitionResult</code><span class="sig-paren">(</span><em>family=None</em>, <em>network_mode=None</em>, <em>revision=None</em>, <em>status=None</em>, <em>task_definition=None</em>, <em>task_role_arn=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecs.GetTaskDefinitionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTaskDefinition.</p>
<dl class="attribute">
<dt id="pulumi_aws.ecs.GetTaskDefinitionResult.family">
<code class="descname">family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetTaskDefinitionResult.family" title="Permalink to this definition">¶</a></dt>
<dd><p>The family of this task definition</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetTaskDefinitionResult.network_mode">
<code class="descname">network_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetTaskDefinitionResult.network_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The Docker networking mode to use for the containers in this task.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetTaskDefinitionResult.revision">
<code class="descname">revision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetTaskDefinitionResult.revision" title="Permalink to this definition">¶</a></dt>
<dd><p>The revision of this task definition</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetTaskDefinitionResult.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetTaskDefinitionResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of this task definition</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetTaskDefinitionResult.task_role_arn">
<code class="descname">task_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetTaskDefinitionResult.task_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role that containers in this task can assume</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.GetTaskDefinitionResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.GetTaskDefinitionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ecs.Service">
<em class="property">class </em><code class="descclassname">pulumi_aws.ecs.</code><code class="descname">Service</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cluster=None</em>, <em>deployment_controller=None</em>, <em>deployment_maximum_percent=None</em>, <em>deployment_minimum_healthy_percent=None</em>, <em>desired_count=None</em>, <em>enable_ecs_managed_tags=None</em>, <em>health_check_grace_period_seconds=None</em>, <em>iam_role=None</em>, <em>launch_type=None</em>, <em>load_balancers=None</em>, <em>name=None</em>, <em>network_configuration=None</em>, <em>ordered_placement_strategies=None</em>, <em>placement_constraints=None</em>, <em>platform_version=None</em>, <em>propagate_tags=None</em>, <em>scheduling_strategy=None</em>, <em>service_registries=None</em>, <em>tags=None</em>, <em>task_definition=None</em>, <em>wait_for_steady_state=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecs.Service" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><strong>Note:</strong> To prevent a race condition during service deletion, make sure to set <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> to the related <code class="docutils literal notranslate"><span class="pre">aws_iam_role_policy</span></code>; otherwise, the policy may be destroyed too soon and the ECS service will then get stuck in the <code class="docutils literal notranslate"><span class="pre">DRAINING</span></code> state.</div></blockquote>
<p>Provides an ECS service - effectively a task that is expected to run until an error occurs or a user terminates it (typically a webserver or a database).</p>
<p>See <a class="reference external" href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html">ECS Services section in AWS developer guide</a>.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">deployment_controller</span></code> configuration block supports the following:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">type</span></code> - (Optional) Type of deployment controller. Valid values: <code class="docutils literal notranslate"><span class="pre">CODE_DEPLOY</span></code>, <code class="docutils literal notranslate"><span class="pre">ECS</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">ECS</span></code>.</li>
</ul>
<p><code class="docutils literal notranslate"><span class="pre">load_balancer</span></code> supports the following:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">elb_name</span></code> - (Required for ELB Classic) The name of the ELB (Classic) to associate with the service.</li>
<li><code class="docutils literal notranslate"><span class="pre">target_group_arn</span></code> - (Required for ALB/NLB) The ARN of the Load Balancer target group to associate with the service.</li>
<li><code class="docutils literal notranslate"><span class="pre">container_name</span></code> - (Required) The name of the container to associate with the load balancer (as it appears in a container definition).</li>
<li><code class="docutils literal notranslate"><span class="pre">container_port</span></code> - (Required) The port on the container to associate with the load balancer.</li>
</ul>
<blockquote>
<div><strong>Note:</strong> As a result of an AWS limitation, a single <code class="docutils literal notranslate"><span class="pre">load_balancer</span></code> can be attached to the ECS service at most. See <a class="reference external" href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html#load-balancing-concepts">related docs</a>.</div></blockquote>
<p><code class="docutils literal notranslate"><span class="pre">ordered_placement_strategy</span></code> supports the following:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">type</span></code> - (Required) The type of placement strategy. Must be one of: <code class="docutils literal notranslate"><span class="pre">binpack</span></code>, <code class="docutils literal notranslate"><span class="pre">random</span></code>, or <code class="docutils literal notranslate"><span class="pre">spread</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">field</span></code> - (Optional) For the <code class="docutils literal notranslate"><span class="pre">spread</span></code> placement strategy, valid values are <code class="docutils literal notranslate"><span class="pre">instanceId</span></code> (or <code class="docutils literal notranslate"><span class="pre">host</span></code>,
which has the same effect), or any platform or custom attribute that is applied to a container instance.
For the <code class="docutils literal notranslate"><span class="pre">binpack</span></code> type, valid values are <code class="docutils literal notranslate"><span class="pre">memory</span></code> and <code class="docutils literal notranslate"><span class="pre">cpu</span></code>. For the <code class="docutils literal notranslate"><span class="pre">random</span></code> type, this attribute is not
needed. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_PlacementStrategy.html">Placement Strategy</a>.</li>
</ul>
<blockquote>
<div><strong>Note:</strong> for <code class="docutils literal notranslate"><span class="pre">spread</span></code>, <code class="docutils literal notranslate"><span class="pre">host</span></code> and <code class="docutils literal notranslate"><span class="pre">instanceId</span></code> will be normalized, by AWS, to be <code class="docutils literal notranslate"><span class="pre">instanceId</span></code>. This means the statefile will show <code class="docutils literal notranslate"><span class="pre">instanceId</span></code> but your config will differ if you use <code class="docutils literal notranslate"><span class="pre">host</span></code>.</div></blockquote>
<p><code class="docutils literal notranslate"><span class="pre">placement_constraints</span></code> support the following:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">type</span></code> - (Required) The type of constraint. The only valid values at this time are <code class="docutils literal notranslate"><span class="pre">memberOf</span></code> and <code class="docutils literal notranslate"><span class="pre">distinctInstance</span></code>.</li>
<li><code class="docutils literal notranslate"><span class="pre">expression</span></code> -  (Optional) Cluster Query Language expression to apply to the constraint. Does not need to be specified
for the <code class="docutils literal notranslate"><span class="pre">distinctInstance</span></code> type.
For more information, see <a class="reference external" href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html">Cluster Query Language in the Amazon EC2 Container
Service Developer
Guide</a>.</li>
</ul>
<p><code class="docutils literal notranslate"><span class="pre">network_configuration</span></code> support the following:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">subnets</span></code> - (Required) The subnets associated with the task or service.</li>
<li><code class="docutils literal notranslate"><span class="pre">security_groups</span></code> - (Optional) The security groups associated with the task or service. If you do not specify a security group, the default security group for the VPC is used.</li>
<li><code class="docutils literal notranslate"><span class="pre">assign_public_ip</span></code> - (Optional) Assign a public IP address to the ENI (Fargate launch type only). Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
</ul>
<p>For more information, see <a class="reference external" href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html">Task Networking</a></p>
<p><code class="docutils literal notranslate"><span class="pre">service_registries</span></code> support the following:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">registry_arn</span></code> - (Required) The ARN of the Service Registry. The currently supported service registry is Amazon Route 53 Auto Naming Service(<code class="docutils literal notranslate"><span class="pre">aws_service_discovery_service</span></code>). For more information, see <a class="reference external" href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_autonaming_Service.html">Service</a></li>
<li><code class="docutils literal notranslate"><span class="pre">port</span></code> - (Optional) The port value used if your Service Discovery service specified an SRV record.</li>
<li><code class="docutils literal notranslate"><span class="pre">container_port</span></code> - (Optional) The port value, already specified in the task definition, to be used for your service discovery service.</li>
<li><code class="docutils literal notranslate"><span class="pre">container_name</span></code> - (Optional) The container name value, already specified in the task definition, to be used for your service discovery service.</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cluster</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of an ECS cluster</li>
<li><strong>deployment_controller</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration block containing deployment controller configuration. Defined below.</li>
<li><strong>deployment_maximum_percent</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The upper limit (as a percentage of the service’s desiredCount) of the number of running tasks that can be running in a service during a deployment. Not valid when using the <code class="docutils literal notranslate"><span class="pre">DAEMON</span></code> scheduling strategy.</li>
<li><strong>deployment_minimum_healthy_percent</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The lower limit (as a percentage of the service’s desiredCount) of the number of running tasks that must remain running and healthy in a service during a deployment.</li>
<li><strong>desired_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of instances of the task definition to place and keep running. Defaults to 0. Do not specify if using the <code class="docutils literal notranslate"><span class="pre">DAEMON</span></code> scheduling strategy.</li>
<li><strong>enable_ecs_managed_tags</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to enable Amazon ECS managed tags for the tasks within the service.</li>
<li><strong>health_check_grace_period_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Seconds to ignore failing load balancer health checks on newly instantiated tasks to prevent premature shutdown, up to 2147483647. Only valid for services configured to use load balancers.</li>
<li><strong>iam_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is required if you are using a load balancer with your service, but only if your task definition does not use the <code class="docutils literal notranslate"><span class="pre">awsvpc</span></code> network mode. If using <code class="docutils literal notranslate"><span class="pre">awsvpc</span></code> network mode, do not specify this role. If your account has already created the Amazon ECS service-linked role, that role is used by default for your service unless you specify a role here.</li>
<li><strong>launch_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The launch type on which to run your service. The valid values are <code class="docutils literal notranslate"><span class="pre">EC2</span></code> and <code class="docutils literal notranslate"><span class="pre">FARGATE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">EC2</span></code>.</li>
<li><strong>load_balancers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A load balancer block. Load balancers documented below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the service (up to 255 letters, numbers, hyphens, and underscores)</li>
<li><strong>network_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The network configuration for the service. This parameter is required for task definitions that use the <code class="docutils literal notranslate"><span class="pre">awsvpc</span></code> network mode to receive their own Elastic Network Interface, and it is not supported for other network modes.</li>
<li><strong>ordered_placement_strategies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Service level strategy rules that are taken into consideration during task placement. List from top to bottom in order of precedence. The maximum number of <code class="docutils literal notranslate"><span class="pre">ordered_placement_strategy</span></code> blocks is <code class="docutils literal notranslate"><span class="pre">5</span></code>. Defined below.</li>
<li><strong>placement_constraints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – rules that are taken into consideration during task placement. Maximum number of
<code class="docutils literal notranslate"><span class="pre">placement_constraints</span></code> is <code class="docutils literal notranslate"><span class="pre">10</span></code>. Defined below.</li>
<li><strong>platform_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The platform version on which to run your service. Only applicable for <code class="docutils literal notranslate"><span class="pre">launch_type</span></code> set to <code class="docutils literal notranslate"><span class="pre">FARGATE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">LATEST</span></code>. More information about Fargate platform versions can be found in the <a class="reference external" href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">AWS ECS User Guide</a>.</li>
<li><strong>propagate_tags</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to propagate the tags from the task definition or the service to the tasks. The valid values are <code class="docutils literal notranslate"><span class="pre">SERVICE</span></code> and <code class="docutils literal notranslate"><span class="pre">TASK_DEFINITION</span></code>.</li>
<li><strong>scheduling_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scheduling strategy to use for the service. The valid values are <code class="docutils literal notranslate"><span class="pre">REPLICA</span></code> and <code class="docutils literal notranslate"><span class="pre">DAEMON</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">REPLICA</span></code>. Note that <cite>*Fargate tasks do not support the ``DAEMON`</cite> scheduling strategy* &lt;<a class="reference external" href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html">https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html</a>&gt;`_.</li>
<li><strong>service_registries</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The service discovery registries for the service. The maximum number of <code class="docutils literal notranslate"><span class="pre">service_registries</span></code> blocks is <code class="docutils literal notranslate"><span class="pre">1</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</li>
<li><strong>task_definition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The family and revision (<code class="docutils literal notranslate"><span class="pre">family:revision</span></code>) or full ARN of the task definition that you want to run in your service.</li>
<li><strong>wait_for_steady_state</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, Terraform will wait for the service to reach a steady state (like <cite>``aws ecs wait services-stable`</cite> &lt;<a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/ecs/wait/services-stable.html">https://docs.aws.amazon.com/cli/latest/reference/ecs/wait/services-stable.html</a>&gt;`_) before continuing. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.cluster">
<code class="descname">cluster</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of an ECS cluster</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.deployment_controller">
<code class="descname">deployment_controller</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.deployment_controller" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration block containing deployment controller configuration. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.deployment_maximum_percent">
<code class="descname">deployment_maximum_percent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.deployment_maximum_percent" title="Permalink to this definition">¶</a></dt>
<dd><p>The upper limit (as a percentage of the service’s desiredCount) of the number of running tasks that can be running in a service during a deployment. Not valid when using the <code class="docutils literal notranslate"><span class="pre">DAEMON</span></code> scheduling strategy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.deployment_minimum_healthy_percent">
<code class="descname">deployment_minimum_healthy_percent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.deployment_minimum_healthy_percent" title="Permalink to this definition">¶</a></dt>
<dd><p>The lower limit (as a percentage of the service’s desiredCount) of the number of running tasks that must remain running and healthy in a service during a deployment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.desired_count">
<code class="descname">desired_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.desired_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of instances of the task definition to place and keep running. Defaults to 0. Do not specify if using the <code class="docutils literal notranslate"><span class="pre">DAEMON</span></code> scheduling strategy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.enable_ecs_managed_tags">
<code class="descname">enable_ecs_managed_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.enable_ecs_managed_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to enable Amazon ECS managed tags for the tasks within the service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.health_check_grace_period_seconds">
<code class="descname">health_check_grace_period_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.health_check_grace_period_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>Seconds to ignore failing load balancer health checks on newly instantiated tasks to prevent premature shutdown, up to 2147483647. Only valid for services configured to use load balancers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.iam_role">
<code class="descname">iam_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.iam_role" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is required if you are using a load balancer with your service, but only if your task definition does not use the <code class="docutils literal notranslate"><span class="pre">awsvpc</span></code> network mode. If using <code class="docutils literal notranslate"><span class="pre">awsvpc</span></code> network mode, do not specify this role. If your account has already created the Amazon ECS service-linked role, that role is used by default for your service unless you specify a role here.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.launch_type">
<code class="descname">launch_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.launch_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The launch type on which to run your service. The valid values are <code class="docutils literal notranslate"><span class="pre">EC2</span></code> and <code class="docutils literal notranslate"><span class="pre">FARGATE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">EC2</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.load_balancers">
<code class="descname">load_balancers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.load_balancers" title="Permalink to this definition">¶</a></dt>
<dd><p>A load balancer block. Load balancers documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the service (up to 255 letters, numbers, hyphens, and underscores)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.network_configuration">
<code class="descname">network_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.network_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The network configuration for the service. This parameter is required for task definitions that use the <code class="docutils literal notranslate"><span class="pre">awsvpc</span></code> network mode to receive their own Elastic Network Interface, and it is not supported for other network modes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.ordered_placement_strategies">
<code class="descname">ordered_placement_strategies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.ordered_placement_strategies" title="Permalink to this definition">¶</a></dt>
<dd><p>Service level strategy rules that are taken into consideration during task placement. List from top to bottom in order of precedence. The maximum number of <code class="docutils literal notranslate"><span class="pre">ordered_placement_strategy</span></code> blocks is <code class="docutils literal notranslate"><span class="pre">5</span></code>. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.placement_constraints">
<code class="descname">placement_constraints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.placement_constraints" title="Permalink to this definition">¶</a></dt>
<dd><p>rules that are taken into consideration during task placement. Maximum number of
<code class="docutils literal notranslate"><span class="pre">placement_constraints</span></code> is <code class="docutils literal notranslate"><span class="pre">10</span></code>. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.platform_version">
<code class="descname">platform_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.platform_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The platform version on which to run your service. Only applicable for <code class="docutils literal notranslate"><span class="pre">launch_type</span></code> set to <code class="docutils literal notranslate"><span class="pre">FARGATE</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">LATEST</span></code>. More information about Fargate platform versions can be found in the <a class="reference external" href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html">AWS ECS User Guide</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.propagate_tags">
<code class="descname">propagate_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.propagate_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to propagate the tags from the task definition or the service to the tasks. The valid values are <code class="docutils literal notranslate"><span class="pre">SERVICE</span></code> and <code class="docutils literal notranslate"><span class="pre">TASK_DEFINITION</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.scheduling_strategy">
<code class="descname">scheduling_strategy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.scheduling_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>The scheduling strategy to use for the service. The valid values are <code class="docutils literal notranslate"><span class="pre">REPLICA</span></code> and <code class="docutils literal notranslate"><span class="pre">DAEMON</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">REPLICA</span></code>. Note that <cite>*Fargate tasks do not support the ``DAEMON`</cite> scheduling strategy* &lt;<a class="reference external" href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html">https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduling_tasks.html</a>&gt;`_.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.service_registries">
<code class="descname">service_registries</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.service_registries" title="Permalink to this definition">¶</a></dt>
<dd><p>The service discovery registries for the service. The maximum number of <code class="docutils literal notranslate"><span class="pre">service_registries</span></code> blocks is <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.task_definition">
<code class="descname">task_definition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.task_definition" title="Permalink to this definition">¶</a></dt>
<dd><p>The family and revision (<code class="docutils literal notranslate"><span class="pre">family:revision</span></code>) or full ARN of the task definition that you want to run in your service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.Service.wait_for_steady_state">
<code class="descname">wait_for_steady_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.Service.wait_for_steady_state" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, Terraform will wait for the service to reach a steady state (like <cite>``aws ecs wait services-stable`</cite> &lt;<a class="reference external" href="https://docs.aws.amazon.com/cli/latest/reference/ecs/wait/services-stable.html">https://docs.aws.amazon.com/cli/latest/reference/ecs/wait/services-stable.html</a>&gt;`_) before continuing. Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ecs.Service.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecs.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ecs.Service.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecs.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ecs.TaskDefinition">
<em class="property">class </em><code class="descclassname">pulumi_aws.ecs.</code><code class="descname">TaskDefinition</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>container_definitions=None</em>, <em>cpu=None</em>, <em>execution_role_arn=None</em>, <em>family=None</em>, <em>ipc_mode=None</em>, <em>memory=None</em>, <em>network_mode=None</em>, <em>pid_mode=None</em>, <em>placement_constraints=None</em>, <em>proxy_configuration=None</em>, <em>requires_compatibilities=None</em>, <em>tags=None</em>, <em>task_role_arn=None</em>, <em>volumes=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a revision of an ECS task definition to be used in <code class="docutils literal notranslate"><span class="pre">aws_ecs_service</span></code>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>container_definitions</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A list of valid [container definitions]
(<a class="reference external" href="http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html">http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html</a>) provided as a
single valid JSON document. Please note that you should only provide values that are part of the container
definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters]
(<a class="reference external" href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html">https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html</a>) section from the
official <a class="reference external" href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide">Developer Guide</a>.</li>
<li><strong>cpu</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The number of cpu units used by the task. If the <code class="docutils literal notranslate"><span class="pre">requires_compatibilities</span></code> is <code class="docutils literal notranslate"><span class="pre">FARGATE</span></code> this field is required.</li>
<li><strong>execution_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.</li>
<li><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for your task definition.</li>
<li><strong>ipc_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPC resource namespace to be used for the containers in the task The valid values are <code class="docutils literal notranslate"><span class="pre">host</span></code>, <code class="docutils literal notranslate"><span class="pre">task</span></code>, and <code class="docutils literal notranslate"><span class="pre">none</span></code>.</li>
<li><strong>memory</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The amount (in MiB) of memory used by the task. If the <code class="docutils literal notranslate"><span class="pre">requires_compatibilities</span></code> is <code class="docutils literal notranslate"><span class="pre">FARGATE</span></code> this field is required.</li>
<li><strong>network_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Docker networking mode to use for the containers in the task. The valid values are <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">bridge</span></code>, <code class="docutils literal notranslate"><span class="pre">awsvpc</span></code>, and <code class="docutils literal notranslate"><span class="pre">host</span></code>.</li>
<li><strong>pid_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The process namespace to use for the containers in the task. The valid values are <code class="docutils literal notranslate"><span class="pre">host</span></code> and <code class="docutils literal notranslate"><span class="pre">task</span></code>.</li>
<li><strong>placement_constraints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of placement constraints rules that are taken into consideration during task placement. Maximum number of <code class="docutils literal notranslate"><span class="pre">placement_constraints</span></code> is <code class="docutils literal notranslate"><span class="pre">10</span></code>.</li>
<li><strong>proxy_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The proxy configuration details for the App Mesh proxy.</li>
<li><strong>requires_compatibilities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of launch types required by the task. The valid values are <code class="docutils literal notranslate"><span class="pre">EC2</span></code> and <code class="docutils literal notranslate"><span class="pre">FARGATE</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</li>
<li><strong>task_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.</li>
<li><strong>volumes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of volume blocks that containers in your task may use.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.ecs.TaskDefinition.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Full ARN of the Task Definition (including both <code class="docutils literal notranslate"><span class="pre">family</span></code> and <code class="docutils literal notranslate"><span class="pre">revision</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.TaskDefinition.container_definitions">
<code class="descname">container_definitions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition.container_definitions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of valid [container definitions]
(<a class="reference external" href="http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html">http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html</a>) provided as a
single valid JSON document. Please note that you should only provide values that are part of the container
definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters]
(<a class="reference external" href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html">https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html</a>) section from the
official <a class="reference external" href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide">Developer Guide</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.TaskDefinition.cpu">
<code class="descname">cpu</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition.cpu" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of cpu units used by the task. If the <code class="docutils literal notranslate"><span class="pre">requires_compatibilities</span></code> is <code class="docutils literal notranslate"><span class="pre">FARGATE</span></code> this field is required.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.TaskDefinition.execution_role_arn">
<code class="descname">execution_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition.execution_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.TaskDefinition.family">
<code class="descname">family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition.family" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for your task definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.TaskDefinition.ipc_mode">
<code class="descname">ipc_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition.ipc_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPC resource namespace to be used for the containers in the task The valid values are <code class="docutils literal notranslate"><span class="pre">host</span></code>, <code class="docutils literal notranslate"><span class="pre">task</span></code>, and <code class="docutils literal notranslate"><span class="pre">none</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.TaskDefinition.memory">
<code class="descname">memory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition.memory" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount (in MiB) of memory used by the task. If the <code class="docutils literal notranslate"><span class="pre">requires_compatibilities</span></code> is <code class="docutils literal notranslate"><span class="pre">FARGATE</span></code> this field is required.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.TaskDefinition.network_mode">
<code class="descname">network_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition.network_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The Docker networking mode to use for the containers in the task. The valid values are <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">bridge</span></code>, <code class="docutils literal notranslate"><span class="pre">awsvpc</span></code>, and <code class="docutils literal notranslate"><span class="pre">host</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.TaskDefinition.pid_mode">
<code class="descname">pid_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition.pid_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The process namespace to use for the containers in the task. The valid values are <code class="docutils literal notranslate"><span class="pre">host</span></code> and <code class="docutils literal notranslate"><span class="pre">task</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.TaskDefinition.placement_constraints">
<code class="descname">placement_constraints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition.placement_constraints" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of placement constraints rules that are taken into consideration during task placement. Maximum number of <code class="docutils literal notranslate"><span class="pre">placement_constraints</span></code> is <code class="docutils literal notranslate"><span class="pre">10</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.TaskDefinition.proxy_configuration">
<code class="descname">proxy_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition.proxy_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The proxy configuration details for the App Mesh proxy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.TaskDefinition.requires_compatibilities">
<code class="descname">requires_compatibilities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition.requires_compatibilities" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of launch types required by the task. The valid values are <code class="docutils literal notranslate"><span class="pre">EC2</span></code> and <code class="docutils literal notranslate"><span class="pre">FARGATE</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.TaskDefinition.revision">
<code class="descname">revision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition.revision" title="Permalink to this definition">¶</a></dt>
<dd><p>The revision of the task in a particular family.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.TaskDefinition.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.TaskDefinition.task_role_arn">
<code class="descname">task_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition.task_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ecs.TaskDefinition.volumes">
<code class="descname">volumes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition.volumes" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of volume blocks that containers in your task may use.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ecs.TaskDefinition.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ecs.TaskDefinition.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecs.TaskDefinition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_aws.ecs.get_cluster">
<code class="descclassname">pulumi_aws.ecs.</code><code class="descname">get_cluster</code><span class="sig-paren">(</span><em>cluster_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecs.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>The ECS Cluster data source allows access to details of a specific
cluster within an AWS ECS service.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ecs.get_container_definition">
<code class="descclassname">pulumi_aws.ecs.</code><code class="descname">get_container_definition</code><span class="sig-paren">(</span><em>container_name=None</em>, <em>task_definition=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecs.get_container_definition" title="Permalink to this definition">¶</a></dt>
<dd><p>The ECS container definition data source allows access to details of
a specific container within an AWS ECS service.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ecs.get_service">
<code class="descclassname">pulumi_aws.ecs.</code><code class="descname">get_service</code><span class="sig-paren">(</span><em>cluster_arn=None</em>, <em>service_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecs.get_service" title="Permalink to this definition">¶</a></dt>
<dd><p>The ECS Service data source allows access to details of a specific
Service within a AWS ECS Cluster.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ecs.get_task_definition">
<code class="descclassname">pulumi_aws.ecs.</code><code class="descname">get_task_definition</code><span class="sig-paren">(</span><em>task_definition=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ecs.get_task_definition" title="Permalink to this definition">¶</a></dt>
<dd><p>The ECS task definition data source allows access to details of
a specific AWS ECS task definition.</p>
</dd></dl>

</div>
