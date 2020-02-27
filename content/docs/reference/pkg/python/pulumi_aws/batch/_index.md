---
title: Module batch
title_tag: Module batch | Package pulumi_aws | Python SDK
linktitle: batch
notitle: true
---

<div class="section" id="batch">
<h1>batch<a class="headerlink" href="#batch" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.batch"></span><dl class="class">
<dt id="pulumi_aws.batch.AwaitableGetComputeEnvironmentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.batch.</code><code class="sig-name descname">AwaitableGetComputeEnvironmentResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">compute_environment_name=None</em>, <em class="sig-param">ecs_cluster_arn=None</em>, <em class="sig-param">service_role=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">status_reason=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.AwaitableGetComputeEnvironmentResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.batch.AwaitableGetJobQueueResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.batch.</code><code class="sig-name descname">AwaitableGetJobQueueResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">compute_environment_orders=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">status_reason=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.AwaitableGetJobQueueResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.batch.ComputeEnvironment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.batch.</code><code class="sig-name descname">ComputeEnvironment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">compute_environment_name=None</em>, <em class="sig-param">compute_environment_name_prefix=None</em>, <em class="sig-param">compute_resources=None</em>, <em class="sig-param">service_role=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a AWS Batch compute environment. Compute environments contain the Amazon ECS container instances that are used to run containerized batch jobs.</p>
<p>For information about AWS Batch, see [What is AWS Batch?][1] .
For information about compute environment, see [Compute Environments][2] .</p>
<blockquote>
<div><p><strong>Note:</strong> To prevent a race condition during environment deletion, make sure to set <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> to the related <code class="docutils literal notranslate"><span class="pre">iam.RolePolicyAttachment</span></code>;
otherwise, the policy may be destroyed too soon and the compute environment will then get stuck in the <code class="docutils literal notranslate"><span class="pre">DELETING</span></code> state, see [Troubleshooting AWS Batch][3] .</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>compute_environment_name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique compute environment name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">compute_environment_name</span></code>.</p></li>
<li><p><strong>compute_resources</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments. See details below.</p></li>
<li><p><strong>service_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of the compute environment. If the state is <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>, then the compute environment accepts jobs from a queue and can scale out automatically based on queues. Valid items are <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of compute environment. Valid items are <code class="docutils literal notranslate"><span class="pre">EC2</span></code> or <code class="docutils literal notranslate"><span class="pre">SPOT</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>compute_resources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allocationStrategy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The allocation strategy to use for the compute resource in case not enough instances of the best fitting instance type can be allocated. Valid items are <code class="docutils literal notranslate"><span class="pre">BEST_FIT_PROGRESSIVE</span></code>, <code class="docutils literal notranslate"><span class="pre">SPOT_CAPACITY_OPTIMIZED</span></code> or <code class="docutils literal notranslate"><span class="pre">BEST_FIT</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">BEST_FIT</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html">AWS docs</a> for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bidPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer of minimum percentage that a Spot Instance price must be when compared with the On-Demand price for that instance type before instances are launched. For example, if your bid percentage is 20% (<code class="docutils literal notranslate"><span class="pre">20</span></code>), then the Spot price must be below 20% of the current On-Demand price for that EC2 instance. This parameter is required for SPOT compute environments.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">desiredVcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The desired number of EC2 vCPUS in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ec2KeyPair</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The EC2 key pair that is used for instances launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceRole</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon ECS instance role applied to Amazon EC2 instances in a compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of instance types that may be launched.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launch_template</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The launch template to use for your compute resources. See details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the launch template. You must specify either the launch template ID or launch template name in the request, but not both.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the launch template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version number of the launch template. Default: The default version of the launch template.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxVcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of EC2 vCPUs that an environment can reach.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minVcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of EC2 vCPUs that an environment should maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityGroupIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of EC2 security group that are associated with instances launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotIamFleetRole</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a SPOT compute environment. This parameter is required for SPOT compute environments.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of VPC subnets into which the compute resources are launched.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Key-value pair tags to be applied to resources that are launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of compute environment. Valid items are <code class="docutils literal notranslate"><span class="pre">EC2</span></code> or <code class="docutils literal notranslate"><span class="pre">SPOT</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/batch_compute_environment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/batch_compute_environment.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the compute environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.compute_environment_name_prefix">
<code class="sig-name descname">compute_environment_name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.compute_environment_name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique compute environment name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">compute_environment_name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.compute_resources">
<code class="sig-name descname">compute_resources</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.compute_resources" title="Permalink to this definition">¶</a></dt>
<dd><p>Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments. See details below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allocationStrategy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The allocation strategy to use for the compute resource in case not enough instances of the best fitting instance type can be allocated. Valid items are <code class="docutils literal notranslate"><span class="pre">BEST_FIT_PROGRESSIVE</span></code>, <code class="docutils literal notranslate"><span class="pre">SPOT_CAPACITY_OPTIMIZED</span></code> or <code class="docutils literal notranslate"><span class="pre">BEST_FIT</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">BEST_FIT</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html">AWS docs</a> for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bidPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Integer of minimum percentage that a Spot Instance price must be when compared with the On-Demand price for that instance type before instances are launched. For example, if your bid percentage is 20% (<code class="docutils literal notranslate"><span class="pre">20</span></code>), then the Spot price must be below 20% of the current On-Demand price for that EC2 instance. This parameter is required for SPOT compute environments.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">desiredVcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The desired number of EC2 vCPUS in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ec2KeyPair</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The EC2 key pair that is used for instances launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceRole</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Amazon ECS instance role applied to Amazon EC2 instances in a compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of instance types that may be launched.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launch_template</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The launch template to use for your compute resources. See details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the launch template. You must specify either the launch template ID or launch template name in the request, but not both.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the launch template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version number of the launch template. Default: The default version of the launch template.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxVcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of EC2 vCPUs that an environment can reach.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minVcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The minimum number of EC2 vCPUs that an environment should maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityGroupIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of EC2 security group that are associated with instances launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotIamFleetRole</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a SPOT compute environment. This parameter is required for SPOT compute environments.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnets</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of VPC subnets into which the compute resources are launched.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Key-value pair tags to be applied to resources that are launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of compute environment. Valid items are <code class="docutils literal notranslate"><span class="pre">EC2</span></code> or <code class="docutils literal notranslate"><span class="pre">SPOT</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.ecs_cluster_arn">
<code class="sig-name descname">ecs_cluster_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.ecs_cluster_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster used by the compute environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.service_role">
<code class="sig-name descname">service_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.service_role" title="Permalink to this definition">¶</a></dt>
<dd><p>The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the compute environment. If the state is <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>, then the compute environment accepts jobs from a queue and can scale out automatically based on queues. Valid items are <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the compute environment (for example, CREATING or VALID).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.status_reason">
<code class="sig-name descname">status_reason</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.status_reason" title="Permalink to this definition">¶</a></dt>
<dd><p>A short, human-readable string to provide additional details about the current status of the compute environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of compute environment. Valid items are <code class="docutils literal notranslate"><span class="pre">EC2</span></code> or <code class="docutils literal notranslate"><span class="pre">SPOT</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.batch.ComputeEnvironment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">compute_environment_name=None</em>, <em class="sig-param">compute_environment_name_prefix=None</em>, <em class="sig-param">compute_resources=None</em>, <em class="sig-param">ecs_cluster_arn=None</em>, <em class="sig-param">service_role=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">status_reason=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ComputeEnvironment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the compute environment.</p></li>
<li><p><strong>compute_environment_name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique compute environment name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">compute_environment_name</span></code>.</p></li>
<li><p><strong>compute_resources</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments. See details below.</p></li>
<li><p><strong>ecs_cluster_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster used by the compute environment.</p></li>
<li><p><strong>service_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of the compute environment. If the state is <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>, then the compute environment accepts jobs from a queue and can scale out automatically based on queues. Valid items are <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current status of the compute environment (for example, CREATING or VALID).</p></li>
<li><p><strong>status_reason</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short, human-readable string to provide additional details about the current status of the compute environment.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of compute environment. Valid items are <code class="docutils literal notranslate"><span class="pre">EC2</span></code> or <code class="docutils literal notranslate"><span class="pre">SPOT</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>compute_resources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allocationStrategy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The allocation strategy to use for the compute resource in case not enough instances of the best fitting instance type can be allocated. Valid items are <code class="docutils literal notranslate"><span class="pre">BEST_FIT_PROGRESSIVE</span></code>, <code class="docutils literal notranslate"><span class="pre">SPOT_CAPACITY_OPTIMIZED</span></code> or <code class="docutils literal notranslate"><span class="pre">BEST_FIT</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">BEST_FIT</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html">AWS docs</a> for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bidPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer of minimum percentage that a Spot Instance price must be when compared with the On-Demand price for that instance type before instances are launched. For example, if your bid percentage is 20% (<code class="docutils literal notranslate"><span class="pre">20</span></code>), then the Spot price must be below 20% of the current On-Demand price for that EC2 instance. This parameter is required for SPOT compute environments.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">desiredVcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The desired number of EC2 vCPUS in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ec2KeyPair</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The EC2 key pair that is used for instances launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceRole</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon ECS instance role applied to Amazon EC2 instances in a compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of instance types that may be launched.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launch_template</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The launch template to use for your compute resources. See details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the launch template. You must specify either the launch template ID or launch template name in the request, but not both.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the launch template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version number of the launch template. Default: The default version of the launch template.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxVcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of EC2 vCPUs that an environment can reach.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minVcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of EC2 vCPUs that an environment should maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityGroupIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of EC2 security group that are associated with instances launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotIamFleetRole</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a SPOT compute environment. This parameter is required for SPOT compute environments.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of VPC subnets into which the compute resources are launched.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Key-value pair tags to be applied to resources that are launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of compute environment. Valid items are <code class="docutils literal notranslate"><span class="pre">EC2</span></code> or <code class="docutils literal notranslate"><span class="pre">SPOT</span></code>.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/batch_compute_environment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/batch_compute_environment.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.batch.ComputeEnvironment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.batch.ComputeEnvironment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.batch.</code><code class="sig-name descname">GetComputeEnvironmentResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">compute_environment_name=None</em>, <em class="sig-param">ecs_cluster_arn=None</em>, <em class="sig-param">service_role=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">status_reason=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getComputeEnvironment.</p>
<dl class="attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the compute environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.ecs_cluster_arn">
<code class="sig-name descname">ecs_cluster_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.ecs_cluster_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the underlying Amazon ECS cluster used by the compute environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.service_role">
<code class="sig-name descname">service_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.service_role" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the compute environment (for example, <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>). If the state is <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>, then the compute environment accepts jobs from a queue and can scale out automatically based on queues.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the compute environment (for example, <code class="docutils literal notranslate"><span class="pre">CREATING</span></code> or <code class="docutils literal notranslate"><span class="pre">VALID</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.status_reason">
<code class="sig-name descname">status_reason</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.status_reason" title="Permalink to this definition">¶</a></dt>
<dd><p>A short, human-readable string to provide additional details about the current status of the compute environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the compute environment (for example, <code class="docutils literal notranslate"><span class="pre">MANAGED</span></code> or <code class="docutils literal notranslate"><span class="pre">UNMANAGED</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.batch.GetJobQueueResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.batch.</code><code class="sig-name descname">GetJobQueueResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">compute_environment_orders=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">status_reason=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getJobQueue.</p>
<dl class="attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the job queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.compute_environment_orders">
<code class="sig-name descname">compute_environment_orders</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.compute_environment_orders" title="Permalink to this definition">¶</a></dt>
<dd><p>The compute environments that are attached to the job queue and the order in
which job placement is preferred. Compute environments are selected for job placement in ascending order.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">compute_environment_order.#.order</span></code> - The order of the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compute_environment_order.#.compute_environment</span></code> - The ARN of the compute environment.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the job queue. Job queues with a higher priority are evaluated first when
associated with the same compute environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes the ability of the queue to accept new jobs (for example, <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the job queue (for example, <code class="docutils literal notranslate"><span class="pre">CREATING</span></code> or <code class="docutils literal notranslate"><span class="pre">VALID</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.status_reason">
<code class="sig-name descname">status_reason</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.status_reason" title="Permalink to this definition">¶</a></dt>
<dd><p>A short, human-readable string to provide additional details about the current status
of the job queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.batch.JobDefinition">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.batch.</code><code class="sig-name descname">JobDefinition</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">container_properties=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">retry_strategy=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobDefinition" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Batch Job Definition resource.</p>
<p><code class="docutils literal notranslate"><span class="pre">retry_strategy</span></code> supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attempts</span></code> - (Optional) The number of times to move a job to the <code class="docutils literal notranslate"><span class="pre">RUNNABLE</span></code> status. You may specify between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">10</span></code> attempts.</p></li>
</ul>
<p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attempt_duration_seconds</span></code> - (Optional) The time duration in seconds after which AWS Batch terminates your jobs if they have not finished. The minimum value for the timeout is <code class="docutils literal notranslate"><span class="pre">60</span></code> seconds.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>container_properties</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A valid <a class="reference external" href="http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html">container properties</a>
provided as a single valid JSON document. This parameter is required if the <code class="docutils literal notranslate"><span class="pre">type</span></code> parameter is <code class="docutils literal notranslate"><span class="pre">container</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the job definition.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the parameter substitution placeholders to set in the job definition.</p></li>
<li><p><strong>retry_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of <code class="docutils literal notranslate"><span class="pre">retry_strategy</span></code> is <code class="docutils literal notranslate"><span class="pre">1</span></code>.  Defined below.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of <code class="docutils literal notranslate"><span class="pre">timeout</span></code> is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Defined below.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of job definition.  Must be <code class="docutils literal notranslate"><span class="pre">container</span></code></p></li>
</ul>
</dd>
</dl>
<p>The <strong>retry_strategy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attempts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>timeout</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attemptDurationSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/batch_job_definition.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/batch_job_definition.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.batch.JobDefinition.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name of the job definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobDefinition.container_properties">
<code class="sig-name descname">container_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.container_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A valid <a class="reference external" href="http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html">container properties</a>
provided as a single valid JSON document. This parameter is required if the <code class="docutils literal notranslate"><span class="pre">type</span></code> parameter is <code class="docutils literal notranslate"><span class="pre">container</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobDefinition.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the job definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobDefinition.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the parameter substitution placeholders to set in the job definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobDefinition.retry_strategy">
<code class="sig-name descname">retry_strategy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.retry_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of <code class="docutils literal notranslate"><span class="pre">retry_strategy</span></code> is <code class="docutils literal notranslate"><span class="pre">1</span></code>.  Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attempts</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobDefinition.revision">
<code class="sig-name descname">revision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.revision" title="Permalink to this definition">¶</a></dt>
<dd><p>The revision of the job definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobDefinition.timeout">
<code class="sig-name descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of <code class="docutils literal notranslate"><span class="pre">timeout</span></code> is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attemptDurationSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobDefinition.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of job definition.  Must be <code class="docutils literal notranslate"><span class="pre">container</span></code></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.batch.JobDefinition.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">container_properties=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parameters=None</em>, <em class="sig-param">retry_strategy=None</em>, <em class="sig-param">revision=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing JobDefinition resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name of the job definition.</p></li>
<li><p><strong>container_properties</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>A valid <a class="reference external" href="http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html">container properties</a>
provided as a single valid JSON document. This parameter is required if the <code class="docutils literal notranslate"><span class="pre">type</span></code> parameter is <code class="docutils literal notranslate"><span class="pre">container</span></code>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the job definition.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the parameter substitution placeholders to set in the job definition.</p></li>
<li><p><strong>retry_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of <code class="docutils literal notranslate"><span class="pre">retry_strategy</span></code> is <code class="docutils literal notranslate"><span class="pre">1</span></code>.  Defined below.</p></li>
<li><p><strong>revision</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The revision of the job definition.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of <code class="docutils literal notranslate"><span class="pre">timeout</span></code> is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Defined below.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of job definition.  Must be <code class="docutils literal notranslate"><span class="pre">container</span></code></p></li>
</ul>
</dd>
</dl>
<p>The <strong>retry_strategy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attempts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>timeout</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attemptDurationSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/batch_job_definition.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/batch_job_definition.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.batch.JobDefinition.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.batch.JobDefinition.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.batch.JobQueue">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.batch.</code><code class="sig-name descname">JobQueue</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">compute_environments=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobQueue" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Batch Job Queue resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>compute_environments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the set of compute environments
mapped to a job queue and their order.  The position of the compute environments
in the list will dictate the order. You can associate up to 3 compute environments
with a job queue.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the job queue.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the job queue. Job queues with a higher priority
are evaluated first when associated with the same compute environment.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of the job queue. Must be one of: <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code></p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/batch_job_queue.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/batch_job_queue.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.batch.JobQueue.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobQueue.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name of the job queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobQueue.compute_environments">
<code class="sig-name descname">compute_environments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobQueue.compute_environments" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the set of compute environments
mapped to a job queue and their order.  The position of the compute environments
in the list will dictate the order. You can associate up to 3 compute environments
with a job queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobQueue.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobQueue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the job queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobQueue.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobQueue.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the job queue. Job queues with a higher priority
are evaluated first when associated with the same compute environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobQueue.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobQueue.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the job queue. Must be one of: <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.batch.JobQueue.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">compute_environments=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">state=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobQueue.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing JobQueue resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name of the job queue.</p></li>
<li><p><strong>compute_environments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the set of compute environments
mapped to a job queue and their order.  The position of the compute environments
in the list will dictate the order. You can associate up to 3 compute environments
with a job queue.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the job queue.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the job queue. Job queues with a higher priority
are evaluated first when associated with the same compute environment.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of the job queue. Must be one of: <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code></p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/batch_job_queue.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/batch_job_queue.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.batch.JobQueue.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobQueue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.batch.JobQueue.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobQueue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.batch.get_compute_environment">
<code class="sig-prename descclassname">pulumi_aws.batch.</code><code class="sig-name descname">get_compute_environment</code><span class="sig-paren">(</span><em class="sig-param">compute_environment_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.get_compute_environment" title="Permalink to this definition">¶</a></dt>
<dd><p>The Batch Compute Environment data source allows access to details of a specific
compute environment within AWS Batch.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>compute_environment_name</strong> (<em>str</em>) – The name of the Batch Compute Environment</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/batch_compute_environment.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/batch_compute_environment.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.batch.get_job_queue">
<code class="sig-prename descclassname">pulumi_aws.batch.</code><code class="sig-name descname">get_job_queue</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.get_job_queue" title="Permalink to this definition">¶</a></dt>
<dd><p>The Batch Job Queue data source allows access to details of a specific
job queue within AWS Batch.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the job queue.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/batch_job_queue.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/batch_job_queue.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
