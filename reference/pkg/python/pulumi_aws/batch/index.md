<div class="section" id="module-pulumi_aws.batch">
<span id="batch"></span><h1>batch<a class="headerlink" href="#module-pulumi_aws.batch" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.batch.ComputeEnvironment">
<em class="property">class </em><code class="descclassname">pulumi_aws.batch.</code><code class="descname">ComputeEnvironment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>compute_environment_name=None</em>, <em>compute_resources=None</em>, <em>service_role=None</em>, <em>state=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a AWS Batch compute environment. Compute environments contain the Amazon ECS container instances that are used to run containerized batch jobs.</p>
<p>For information about AWS Batch, see [What is AWS Batch?][1] .
For information about compute environment, see [Compute Environments][2] .</p>
<blockquote>
<div><dl class="docutils">
<dt><strong>Note:</strong> To prevent a race condition during environment deletion, make sure to set <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> to the related <code class="docutils literal notranslate"><span class="pre">aws_iam_role_policy_attachment</span></code>;</dt>
<dd>otherwise, the policy may be destroyed too soon and the compute environment will then get stuck in the <code class="docutils literal notranslate"><span class="pre">DELETING</span></code> state, see [Troubleshooting AWS Batch][3] .</dd>
</dl>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>compute_environment_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, and underscores are allowed.</li>
<li><strong>compute_resources</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments. See details below.</li>
<li><strong>service_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.</li>
<li><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of the compute environment. If the state is <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>, then the compute environment accepts jobs from a queue and can scale out automatically based on queues. Valid items are <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of compute environment. Valid items are <code class="docutils literal notranslate"><span class="pre">EC2</span></code> or <code class="docutils literal notranslate"><span class="pre">SPOT</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the compute environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.compute_environment_name">
<code class="descname">compute_environment_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.compute_environment_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, and underscores are allowed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.compute_resources">
<code class="descname">compute_resources</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.compute_resources" title="Permalink to this definition">¶</a></dt>
<dd><p>Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments. See details below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.ecs_cluster_arn">
<code class="descname">ecs_cluster_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.ecs_cluster_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster used by the compute environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.service_role">
<code class="descname">service_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.service_role" title="Permalink to this definition">¶</a></dt>
<dd><p>The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the compute environment. If the state is <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>, then the compute environment accepts jobs from a queue and can scale out automatically based on queues. Valid items are <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the compute environment (for example, CREATING or VALID).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.status_reason">
<code class="descname">status_reason</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.status_reason" title="Permalink to this definition">¶</a></dt>
<dd><p>A short, human-readable string to provide additional details about the current status of the compute environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.ComputeEnvironment.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of compute environment. Valid items are <code class="docutils literal notranslate"><span class="pre">EC2</span></code> or <code class="docutils literal notranslate"><span class="pre">SPOT</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.batch.ComputeEnvironment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.batch.ComputeEnvironment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.ComputeEnvironment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.batch.</code><code class="descname">GetComputeEnvironmentResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>ecs_cluster_arn=None</em>, <em>service_role=None</em>, <em>state=None</em>, <em>status=None</em>, <em>status_reason=None</em>, <em>type=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getComputeEnvironment.</p>
<dl class="attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the compute environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.ecs_cluster_arn">
<code class="descname">ecs_cluster_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.ecs_cluster_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the underlying Amazon ECS cluster used by the compute environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.service_role">
<code class="descname">service_role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.service_role" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the compute environment (for example, <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>). If the state is <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>, then the compute environment accepts jobs from a queue and can scale out automatically based on queues.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the compute environment (for example, <code class="docutils literal notranslate"><span class="pre">CREATING</span></code> or <code class="docutils literal notranslate"><span class="pre">VALID</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.status_reason">
<code class="descname">status_reason</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.status_reason" title="Permalink to this definition">¶</a></dt>
<dd><p>A short, human-readable string to provide additional details about the current status of the compute environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the compute environment (for example, <code class="docutils literal notranslate"><span class="pre">MANAGED</span></code> or <code class="docutils literal notranslate"><span class="pre">UNMANAGED</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetComputeEnvironmentResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetComputeEnvironmentResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.batch.GetJobQueueResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.batch.</code><code class="descname">GetJobQueueResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>compute_environment_orders=None</em>, <em>priority=None</em>, <em>state=None</em>, <em>status=None</em>, <em>status_reason=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getJobQueue.</p>
<dl class="attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the job queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.compute_environment_orders">
<code class="descname">compute_environment_orders</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.compute_environment_orders" title="Permalink to this definition">¶</a></dt>
<dd><p>The compute environments that are attached to the job queue and the order in
which job placement is preferred. Compute environments are selected for job placement in ascending order.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">compute_environment_order.#.order</span></code> - The order of the compute environment.</li>
<li><code class="docutils literal notranslate"><span class="pre">compute_environment_order.#.compute_environment</span></code> - The ARN of the compute environment.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.priority">
<code class="descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the job queue. Job queues with a higher priority are evaluated first when
associated with the same compute environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes the ability of the queue to accept new jobs (for example, <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the job queue (for example, <code class="docutils literal notranslate"><span class="pre">CREATING</span></code> or <code class="docutils literal notranslate"><span class="pre">VALID</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.status_reason">
<code class="descname">status_reason</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.status_reason" title="Permalink to this definition">¶</a></dt>
<dd><p>A short, human-readable string to provide additional details about the current status
of the job queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.GetJobQueueResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.GetJobQueueResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.batch.JobDefinition">
<em class="property">class </em><code class="descclassname">pulumi_aws.batch.</code><code class="descname">JobDefinition</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>container_properties=None</em>, <em>name=None</em>, <em>parameters=None</em>, <em>retry_strategy=None</em>, <em>timeout=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobDefinition" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Batch Job Definition resource.</p>
<p><code class="docutils literal notranslate"><span class="pre">retry_strategy</span></code> supports the following:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">attempts</span></code> - (Optional) The number of times to move a job to the <code class="docutils literal notranslate"><span class="pre">RUNNABLE</span></code> status. You may specify between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">10</span></code> attempts.</li>
</ul>
<p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> supports the following:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">attempt_duration_seconds</span></code> - (Optional) The time duration in seconds after which AWS Batch terminates your jobs if they have not finished. The minimum value for the timeout is <code class="docutils literal notranslate"><span class="pre">60</span></code> seconds.</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>container_properties</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A valid <a class="reference external" href="http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html">container properties</a>
provided as a single valid JSON document. This parameter is required if the <code class="docutils literal notranslate"><span class="pre">type</span></code> parameter is <code class="docutils literal notranslate"><span class="pre">container</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the job definition.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the parameter substitution placeholders to set in the job definition.</li>
<li><strong>retry_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of <code class="docutils literal notranslate"><span class="pre">retry_strategy</span></code> is <code class="docutils literal notranslate"><span class="pre">1</span></code>.  Defined below.</li>
<li><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of <code class="docutils literal notranslate"><span class="pre">timeout</span></code> is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Defined below.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of job definition.  Must be <code class="docutils literal notranslate"><span class="pre">container</span></code></li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.batch.JobDefinition.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name of the job definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobDefinition.container_properties">
<code class="descname">container_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.container_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A valid <a class="reference external" href="http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html">container properties</a>
provided as a single valid JSON document. This parameter is required if the <code class="docutils literal notranslate"><span class="pre">type</span></code> parameter is <code class="docutils literal notranslate"><span class="pre">container</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobDefinition.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the job definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobDefinition.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the parameter substitution placeholders to set in the job definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobDefinition.retry_strategy">
<code class="descname">retry_strategy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.retry_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of <code class="docutils literal notranslate"><span class="pre">retry_strategy</span></code> is <code class="docutils literal notranslate"><span class="pre">1</span></code>.  Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobDefinition.revision">
<code class="descname">revision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.revision" title="Permalink to this definition">¶</a></dt>
<dd><p>The revision of the job definition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobDefinition.timeout">
<code class="descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of <code class="docutils literal notranslate"><span class="pre">timeout</span></code> is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobDefinition.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of job definition.  Must be <code class="docutils literal notranslate"><span class="pre">container</span></code></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.batch.JobDefinition.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.batch.JobDefinition.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobDefinition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.batch.JobQueue">
<em class="property">class </em><code class="descclassname">pulumi_aws.batch.</code><code class="descname">JobQueue</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>compute_environments=None</em>, <em>name=None</em>, <em>priority=None</em>, <em>state=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobQueue" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Batch Job Queue resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>compute_environments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the set of compute environments
mapped to a job queue and their order.  The position of the compute environments
in the list will dictate the order. You can associate up to 3 compute environments
with a job queue.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the job queue.</li>
<li><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the job queue. Job queues with a higher priority
are evaluated first when associated with the same compute environment.</li>
<li><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of the job queue. Must be one of: <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code></li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.batch.JobQueue.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobQueue.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name of the job queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobQueue.compute_environments">
<code class="descname">compute_environments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobQueue.compute_environments" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the set of compute environments
mapped to a job queue and their order.  The position of the compute environments
in the list will dictate the order. You can associate up to 3 compute environments
with a job queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobQueue.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobQueue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the job queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobQueue.priority">
<code class="descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobQueue.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the job queue. Job queues with a higher priority
are evaluated first when associated with the same compute environment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.batch.JobQueue.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.batch.JobQueue.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the job queue. Must be one of: <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.batch.JobQueue.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobQueue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.batch.JobQueue.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.JobQueue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.batch.get_compute_environment">
<code class="descclassname">pulumi_aws.batch.</code><code class="descname">get_compute_environment</code><span class="sig-paren">(</span><em>compute_environment_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.get_compute_environment" title="Permalink to this definition">¶</a></dt>
<dd><p>The Batch Compute Environment data source allows access to details of a specific
compute environment within AWS Batch.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.batch.get_job_queue">
<code class="descclassname">pulumi_aws.batch.</code><code class="descname">get_job_queue</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.batch.get_job_queue" title="Permalink to this definition">¶</a></dt>
<dd><p>The Batch Job Queue data source allows access to details of a specific
job queue within AWS Batch.</p>
</dd></dl>

</div>
