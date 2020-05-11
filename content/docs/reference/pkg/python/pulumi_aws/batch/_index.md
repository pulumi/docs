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
<span class="target" id="module-pulumi_aws.batch"></span><dl class="py class">
<dt id="pulumi_aws.batch.AwaitableGetComputeEnvironmentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.batch.</code><code class="sig-name descname">AwaitableGetComputeEnvironmentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compute_environment_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecs_cluster_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status_reason</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.AwaitableGetComputeEnvironmentResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.batch.AwaitableGetJobQueueResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.batch.</code><code class="sig-name descname">AwaitableGetJobQueueResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compute_environment_orders</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status_reason</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.AwaitableGetJobQueueResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.batch.ComputeEnvironment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.batch.</code><code class="sig-name descname">ComputeEnvironment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compute_environment_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compute_environment_name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compute_resources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a AWS Batch compute environment. Compute environments contain the Amazon ECS container instances that are used to run containerized batch jobs.</p>
<p>For information about AWS Batch, see <a class="reference external" href="http://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html">What is AWS Batch?</a> .
For information about compute environment, see <a class="reference external" href="http://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html">Compute Environments</a> .</p>
<blockquote>
<div><p><strong>Note:</strong> To prevent a race condition during environment deletion, make sure to set <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> to the related <code class="docutils literal notranslate"><span class="pre">iam.RolePolicyAttachment</span></code>;
otherwise, the policy may be destroyed too soon and the compute environment will then get stuck in the <code class="docutils literal notranslate"><span class="pre">DELETING</span></code> state, see <a class="reference external" href="http://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html">Troubleshooting AWS Batch</a> .</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">ecs_instance_role_role</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;ecsInstanceRoleRole&quot;</span><span class="p">,</span> <span class="n">assume_role_policy</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">    &quot;Version&quot;: &quot;2012-10-17&quot;,</span>
<span class="s2">    &quot;Statement&quot;: [</span>
<span class="s2">        {</span>
<span class="s2">            &quot;Action&quot;: &quot;sts:AssumeRole&quot;,</span>
<span class="s2">            &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">            &quot;Principal&quot;: {</span>
<span class="s2">                &quot;Service&quot;: &quot;ec2.amazonaws.com&quot;</span>
<span class="s2">            }</span>
<span class="s2">        }</span>
<span class="s2">    ]</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
<span class="n">ecs_instance_role_role_policy_attachment</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">RolePolicyAttachment</span><span class="p">(</span><span class="s2">&quot;ecsInstanceRoleRolePolicyAttachment&quot;</span><span class="p">,</span>
    <span class="n">policy_arn</span><span class="o">=</span><span class="s2">&quot;arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="n">ecs_instance_role_role</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">ecs_instance_role_instance_profile</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">InstanceProfile</span><span class="p">(</span><span class="s2">&quot;ecsInstanceRoleInstanceProfile&quot;</span><span class="p">,</span> <span class="n">role</span><span class="o">=</span><span class="n">ecs_instance_role_role</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">aws_batch_service_role_role</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;awsBatchServiceRoleRole&quot;</span><span class="p">,</span> <span class="n">assume_role_policy</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">    &quot;Version&quot;: &quot;2012-10-17&quot;,</span>
<span class="s2">    &quot;Statement&quot;: [</span>
<span class="s2">        {</span>
<span class="s2">            &quot;Action&quot;: &quot;sts:AssumeRole&quot;,</span>
<span class="s2">            &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">            &quot;Principal&quot;: {</span>
<span class="s2">                &quot;Service&quot;: &quot;batch.amazonaws.com&quot;</span>
<span class="s2">            }</span>
<span class="s2">        }</span>
<span class="s2">    ]</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
<span class="n">aws_batch_service_role_role_policy_attachment</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">iam</span><span class="o">.</span><span class="n">RolePolicyAttachment</span><span class="p">(</span><span class="s2">&quot;awsBatchServiceRoleRolePolicyAttachment&quot;</span><span class="p">,</span>
    <span class="n">policy_arn</span><span class="o">=</span><span class="s2">&quot;arn:aws:iam::aws:policy/service-role/AWSBatchServiceRole&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="n">aws_batch_service_role_role</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">sample_security_group</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">SecurityGroup</span><span class="p">(</span><span class="s2">&quot;sampleSecurityGroup&quot;</span><span class="p">,</span> <span class="n">egress</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;cidrBlocks&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;0.0.0.0/0&quot;</span><span class="p">],</span>
    <span class="s2">&quot;fromPort&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
    <span class="s2">&quot;protocol&quot;</span><span class="p">:</span> <span class="s2">&quot;-1&quot;</span><span class="p">,</span>
    <span class="s2">&quot;toPort&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
<span class="p">}])</span>
<span class="n">sample_vpc</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">Vpc</span><span class="p">(</span><span class="s2">&quot;sampleVpc&quot;</span><span class="p">,</span> <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;10.1.0.0/16&quot;</span><span class="p">)</span>
<span class="n">sample_subnet</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">Subnet</span><span class="p">(</span><span class="s2">&quot;sampleSubnet&quot;</span><span class="p">,</span>
    <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;10.1.1.0/24&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">sample_vpc</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">sample_compute_environment</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">batch</span><span class="o">.</span><span class="n">ComputeEnvironment</span><span class="p">(</span><span class="s2">&quot;sampleComputeEnvironment&quot;</span><span class="p">,</span>
    <span class="n">compute_environment_name</span><span class="o">=</span><span class="s2">&quot;sample&quot;</span><span class="p">,</span>
    <span class="n">compute_resources</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;instanceRole&quot;</span><span class="p">:</span> <span class="n">ecs_instance_role_instance_profile</span><span class="o">.</span><span class="n">arn</span><span class="p">,</span>
        <span class="s2">&quot;instanceType&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;c4.large&quot;</span><span class="p">],</span>
        <span class="s2">&quot;maxVcpus&quot;</span><span class="p">:</span> <span class="mi">16</span><span class="p">,</span>
        <span class="s2">&quot;minVcpus&quot;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
        <span class="s2">&quot;securityGroupIds&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">sample_security_group</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
        <span class="s2">&quot;subnets&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">sample_subnet</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;EC2&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">service_role</span><span class="o">=</span><span class="n">aws_batch_service_role_role</span><span class="o">.</span><span class="n">arn</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;MANAGED&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>compute_environment_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, and underscores are allowed. If omitted, this provider will assign a random, unique name.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">allocation_strategy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The allocation strategy to use for the compute resource in case not enough instances of the best fitting instance type can be allocated. Valid items are <code class="docutils literal notranslate"><span class="pre">BEST_FIT_PROGRESSIVE</span></code>, <code class="docutils literal notranslate"><span class="pre">SPOT_CAPACITY_OPTIMIZED</span></code> or <code class="docutils literal notranslate"><span class="pre">BEST_FIT</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">BEST_FIT</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html">AWS docs</a> for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bidPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer of minimum percentage that a Spot Instance price must be when compared with the On-Demand price for that instance type before instances are launched. For example, if your bid percentage is 20% (<code class="docutils literal notranslate"><span class="pre">20</span></code>), then the Spot price must be below 20% of the current On-Demand price for that EC2 instance. This parameter is required for SPOT compute environments.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">desiredVcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The desired number of EC2 vCPUS in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ec2KeyPair</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The EC2 key pair that is used for instances launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">image_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceRole</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon ECS instance role applied to Amazon EC2 instances in a compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_types</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of instance types that may be launched.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launch_template</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The launch template to use for your compute resources. See details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the launch template. You must specify either the launch template ID or launch template name in the request, but not both.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the launch template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version number of the launch template. Default: The default version of the launch template.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxVcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of EC2 vCPUs that an environment can reach.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minVcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of EC2 vCPUs that an environment should maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of EC2 security group that are associated with instances launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotIamFleetRole</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a SPOT compute environment. This parameter is required for SPOT compute environments.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of VPC subnets into which the compute resources are launched.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Key-value pair tags to be applied to resources that are launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of compute environment. Valid items are <code class="docutils literal notranslate"><span class="pre">EC2</span></code> or <code class="docutils literal notranslate"><span class="pre">SPOT</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the compute environment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.compute_environment_name">
<code class="sig-name descname">compute_environment_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.compute_environment_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, and underscores are allowed. If omitted, this provider will assign a random, unique name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.compute_environment_name_prefix">
<code class="sig-name descname">compute_environment_name_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.compute_environment_name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique compute environment name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">compute_environment_name</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.compute_resources">
<code class="sig-name descname">compute_resources</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.compute_resources" title="Permalink to this definition">¶</a></dt>
<dd><p>Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments. See details below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allocation_strategy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The allocation strategy to use for the compute resource in case not enough instances of the best fitting instance type can be allocated. Valid items are <code class="docutils literal notranslate"><span class="pre">BEST_FIT_PROGRESSIVE</span></code>, <code class="docutils literal notranslate"><span class="pre">SPOT_CAPACITY_OPTIMIZED</span></code> or <code class="docutils literal notranslate"><span class="pre">BEST_FIT</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">BEST_FIT</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html">AWS docs</a> for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bidPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Integer of minimum percentage that a Spot Instance price must be when compared with the On-Demand price for that instance type before instances are launched. For example, if your bid percentage is 20% (<code class="docutils literal notranslate"><span class="pre">20</span></code>), then the Spot price must be below 20% of the current On-Demand price for that EC2 instance. This parameter is required for SPOT compute environments.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">desiredVcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The desired number of EC2 vCPUS in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ec2KeyPair</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The EC2 key pair that is used for instances launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">image_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceRole</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Amazon ECS instance role applied to Amazon EC2 instances in a compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_types</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of instance types that may be launched.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launch_template</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The launch template to use for your compute resources. See details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the launch template. You must specify either the launch template ID or launch template name in the request, but not both.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the launch template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version number of the launch template. Default: The default version of the launch template.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxVcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of EC2 vCPUs that an environment can reach.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minVcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The minimum number of EC2 vCPUs that an environment should maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of EC2 security group that are associated with instances launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotIamFleetRole</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a SPOT compute environment. This parameter is required for SPOT compute environments.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnets</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of VPC subnets into which the compute resources are launched.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Key-value pair tags to be applied to resources that are launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of compute environment. Valid items are <code class="docutils literal notranslate"><span class="pre">EC2</span></code> or <code class="docutils literal notranslate"><span class="pre">SPOT</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.ecs_cluster_arn">
<code class="sig-name descname">ecs_cluster_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.ecs_cluster_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster used by the compute environment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.service_role">
<code class="sig-name descname">service_role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.service_role" title="Permalink to this definition">¶</a></dt>
<dd><p>The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.state">
<code class="sig-name descname">state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the compute environment. If the state is <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>, then the compute environment accepts jobs from a queue and can scale out automatically based on queues. Valid items are <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the compute environment (for example, CREATING or VALID).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.status_reason">
<code class="sig-name descname">status_reason</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.status_reason" title="Permalink to this definition">¶</a></dt>
<dd><p>A short, human-readable string to provide additional details about the current status of the compute environment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of compute environment. Valid items are <code class="docutils literal notranslate"><span class="pre">EC2</span></code> or <code class="docutils literal notranslate"><span class="pre">SPOT</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.batch.ComputeEnvironment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compute_environment_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compute_environment_name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compute_resources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecs_cluster_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status_reason</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ComputeEnvironment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the compute environment.</p></li>
<li><p><strong>compute_environment_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, and underscores are allowed. If omitted, this provider will assign a random, unique name.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">allocation_strategy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The allocation strategy to use for the compute resource in case not enough instances of the best fitting instance type can be allocated. Valid items are <code class="docutils literal notranslate"><span class="pre">BEST_FIT_PROGRESSIVE</span></code>, <code class="docutils literal notranslate"><span class="pre">SPOT_CAPACITY_OPTIMIZED</span></code> or <code class="docutils literal notranslate"><span class="pre">BEST_FIT</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">BEST_FIT</span></code>. See <a class="reference external" href="https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html">AWS docs</a> for details.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bidPercentage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Integer of minimum percentage that a Spot Instance price must be when compared with the On-Demand price for that instance type before instances are launched. For example, if your bid percentage is 20% (<code class="docutils literal notranslate"><span class="pre">20</span></code>), then the Spot price must be below 20% of the current On-Demand price for that EC2 instance. This parameter is required for SPOT compute environments.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">desiredVcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The desired number of EC2 vCPUS in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ec2KeyPair</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The EC2 key pair that is used for instances launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">image_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon Machine Image (AMI) ID used for instances launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceRole</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon ECS instance role applied to Amazon EC2 instances in a compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance_types</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of instance types that may be launched.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launch_template</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The launch template to use for your compute resources. See details below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the launch template. You must specify either the launch template ID or launch template name in the request, but not both.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">launchTemplateName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the launch template.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version number of the launch template. Default: The default version of the launch template.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxVcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of EC2 vCPUs that an environment can reach.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minVcpus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of EC2 vCPUs that an environment should maintain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of EC2 security group that are associated with instances launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">spotIamFleetRole</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a SPOT compute environment. This parameter is required for SPOT compute environments.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of VPC subnets into which the compute resources are launched.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Key-value pair tags to be applied to resources that are launched in the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of compute environment. Valid items are <code class="docutils literal notranslate"><span class="pre">EC2</span></code> or <code class="docutils literal notranslate"><span class="pre">SPOT</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.batch.ComputeEnvironment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.batch.ComputeEnvironment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.batch.</code><code class="sig-name descname">GetComputeEnvironmentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compute_environment_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ecs_cluster_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status_reason</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getComputeEnvironment.</p>
<dl class="py attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the compute environment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.ecs_cluster_arn">
<code class="sig-name descname">ecs_cluster_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.ecs_cluster_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the underlying Amazon ECS cluster used by the compute environment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.service_role">
<code class="sig-name descname">service_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.service_role" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the compute environment (for example, <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>). If the state is <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>, then the compute environment accepts jobs from a queue and can scale out automatically based on queues.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the compute environment (for example, <code class="docutils literal notranslate"><span class="pre">CREATING</span></code> or <code class="docutils literal notranslate"><span class="pre">VALID</span></code>).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.status_reason">
<code class="sig-name descname">status_reason</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.status_reason" title="Permalink to this definition">¶</a></dt>
<dd><p>A short, human-readable string to provide additional details about the current status of the compute environment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the compute environment (for example, <code class="docutils literal notranslate"><span class="pre">MANAGED</span></code> or <code class="docutils literal notranslate"><span class="pre">UNMANAGED</span></code>).</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.batch.GetJobQueueResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.batch.</code><code class="sig-name descname">GetJobQueueResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compute_environment_orders</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status_reason</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getJobQueue.</p>
<dl class="py attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the job queue.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.compute_environment_orders">
<code class="sig-name descname">compute_environment_orders</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.compute_environment_orders" title="Permalink to this definition">¶</a></dt>
<dd><p>The compute environments that are attached to the job queue and the order in
which job placement is preferred. Compute environments are selected for job placement in ascending order.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">compute_environment_order.#.order</span></code> - The order of the compute environment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">compute_environment_order.#.compute_environment</span></code> - The ARN of the compute environment.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the job queue. Job queues with a higher priority are evaluated first when
associated with the same compute environment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes the ability of the queue to accept new jobs (for example, <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the job queue (for example, <code class="docutils literal notranslate"><span class="pre">CREATING</span></code> or <code class="docutils literal notranslate"><span class="pre">VALID</span></code>).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.status_reason">
<code class="sig-name descname">status_reason</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.status_reason" title="Permalink to this definition">¶</a></dt>
<dd><p>A short, human-readable string to provide additional details about the current status
of the job queue.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.batch.JobDefinition">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.batch.</code><code class="sig-name descname">JobDefinition</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobDefinition" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Batch Job Definition resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">batch</span><span class="o">.</span><span class="n">JobDefinition</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">container_properties</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">        &quot;command&quot;: [&quot;ls&quot;, &quot;-la&quot;],</span>
<span class="s2">        &quot;image&quot;: &quot;busybox&quot;,</span>
<span class="s2">        &quot;memory&quot;: 1024,</span>
<span class="s2">        &quot;vcpus&quot;: 1,</span>
<span class="s2">        &quot;volumes&quot;: [</span>
<span class="s2">      {</span>
<span class="s2">        &quot;host&quot;: {</span>
<span class="s2">          &quot;sourcePath&quot;: &quot;/tmp&quot;</span>
<span class="s2">        },</span>
<span class="s2">        &quot;name&quot;: &quot;tmp&quot;</span>
<span class="s2">      }</span>
<span class="s2">    ],</span>
<span class="s2">        &quot;environment&quot;: [</span>
<span class="s2">                {&quot;name&quot;: &quot;VARNAME&quot;, &quot;value&quot;: &quot;VARVAL&quot;}</span>
<span class="s2">        ],</span>
<span class="s2">        &quot;mountPoints&quot;: [</span>
<span class="s2">                {</span>
<span class="s2">          &quot;sourceVolume&quot;: &quot;tmp&quot;,</span>
<span class="s2">          &quot;containerPath&quot;: &quot;/tmp&quot;,</span>
<span class="s2">          &quot;readOnly&quot;: false</span>
<span class="s2">        }</span>
<span class="s2">        ],</span>
<span class="s2">    &quot;ulimits&quot;: [</span>
<span class="s2">      {</span>
<span class="s2">        &quot;hardLimit&quot;: 1024,</span>
<span class="s2">        &quot;name&quot;: &quot;nofile&quot;,</span>
<span class="s2">        &quot;softLimit&quot;: 1024</span>
<span class="s2">      }</span>
<span class="s2">    ]</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;container&quot;</span><span class="p">)</span>
</pre></div>
</div>
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
<li><p><code class="docutils literal notranslate"><span class="pre">attempts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of times to move a job to the <code class="docutils literal notranslate"><span class="pre">RUNNABLE</span></code> status. You may specify between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">10</span></code> attempts.</p></li>
</ul>
<p>The <strong>timeout</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attemptDurationSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time duration in seconds after which AWS Batch terminates your jobs if they have not finished. The minimum value for the timeout is <code class="docutils literal notranslate"><span class="pre">60</span></code> seconds.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.batch.JobDefinition.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name of the job definition.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.JobDefinition.container_properties">
<code class="sig-name descname">container_properties</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.container_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A valid <a class="reference external" href="http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html">container properties</a>
provided as a single valid JSON document. This parameter is required if the <code class="docutils literal notranslate"><span class="pre">type</span></code> parameter is <code class="docutils literal notranslate"><span class="pre">container</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.JobDefinition.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the job definition.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.JobDefinition.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the parameter substitution placeholders to set in the job definition.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.JobDefinition.retry_strategy">
<code class="sig-name descname">retry_strategy</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.retry_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of <code class="docutils literal notranslate"><span class="pre">retry_strategy</span></code> is <code class="docutils literal notranslate"><span class="pre">1</span></code>.  Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attempts</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of times to move a job to the <code class="docutils literal notranslate"><span class="pre">RUNNABLE</span></code> status. You may specify between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">10</span></code> attempts.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.JobDefinition.revision">
<code class="sig-name descname">revision</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.revision" title="Permalink to this definition">¶</a></dt>
<dd><p>The revision of the job definition.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.JobDefinition.timeout">
<code class="sig-name descname">timeout</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of <code class="docutils literal notranslate"><span class="pre">timeout</span></code> is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attemptDurationSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The time duration in seconds after which AWS Batch terminates your jobs if they have not finished. The minimum value for the timeout is <code class="docutils literal notranslate"><span class="pre">60</span></code> seconds.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.JobDefinition.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of job definition.  Must be <code class="docutils literal notranslate"><span class="pre">container</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.batch.JobDefinition.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_properties</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_strategy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">revision</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><code class="docutils literal notranslate"><span class="pre">attempts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of times to move a job to the <code class="docutils literal notranslate"><span class="pre">RUNNABLE</span></code> status. You may specify between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">10</span></code> attempts.</p></li>
</ul>
<p>The <strong>timeout</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attemptDurationSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time duration in seconds after which AWS Batch terminates your jobs if they have not finished. The minimum value for the timeout is <code class="docutils literal notranslate"><span class="pre">60</span></code> seconds.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.batch.JobDefinition.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.batch.JobDefinition.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.batch.JobQueue">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.batch.</code><code class="sig-name descname">JobQueue</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compute_environments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobQueue" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Batch Job Queue resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">test_queue</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">batch</span><span class="o">.</span><span class="n">JobQueue</span><span class="p">(</span><span class="s2">&quot;testQueue&quot;</span><span class="p">,</span>
    <span class="n">compute_environments</span><span class="o">=</span><span class="p">[</span>
        <span class="n">aws_batch_compute_environment</span><span class="p">[</span><span class="s2">&quot;test_environment_1&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">],</span>
        <span class="n">aws_batch_compute_environment</span><span class="p">[</span><span class="s2">&quot;test_environment_2&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">],</span>
    <span class="p">],</span>
    <span class="n">priority</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">state</span><span class="o">=</span><span class="s2">&quot;ENABLED&quot;</span><span class="p">)</span>
</pre></div>
</div>
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
<dl class="py attribute">
<dt id="pulumi_aws.batch.JobQueue.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobQueue.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name of the job queue.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.JobQueue.compute_environments">
<code class="sig-name descname">compute_environments</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobQueue.compute_environments" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the set of compute environments
mapped to a job queue and their order.  The position of the compute environments
in the list will dictate the order. You can associate up to 3 compute environments
with a job queue.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.JobQueue.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobQueue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the job queue.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.JobQueue.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobQueue.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the job queue. Job queues with a higher priority
are evaluated first when associated with the same compute environment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.batch.JobQueue.state">
<code class="sig-name descname">state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobQueue.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the job queue. Must be one of: <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.batch.JobQueue.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compute_environments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobQueue.get" title="Permalink to this definition">¶</a></dt>
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
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.batch.JobQueue.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobQueue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.batch.JobQueue.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobQueue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_aws.batch.get_compute_environment">
<code class="sig-prename descclassname">pulumi_aws.batch.</code><code class="sig-name descname">get_compute_environment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">compute_environment_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.get_compute_environment" title="Permalink to this definition">¶</a></dt>
<dd><p>The Batch Compute Environment data source allows access to details of a specific
compute environment within AWS Batch.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">batch_mongo</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">batch</span><span class="o">.</span><span class="n">get_compute_environment</span><span class="p">(</span><span class="n">compute_environment_name</span><span class="o">=</span><span class="s2">&quot;batch-mongo-production&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>compute_environment_name</strong> (<em>str</em>) – The name of the Batch Compute Environment</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.batch.get_job_queue">
<code class="sig-prename descclassname">pulumi_aws.batch.</code><code class="sig-name descname">get_job_queue</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.get_job_queue" title="Permalink to this definition">¶</a></dt>
<dd><p>The Batch Job Queue data source allows access to details of a specific
job queue within AWS Batch.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">test_queue</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">batch</span><span class="o">.</span><span class="n">get_job_queue</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;tf-test-batch-job-queue&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the job queue.</p>
</dd>
</dl>
</dd></dl>

</div>
