<div class="section" id="module-pulumi_aws.cloudformation">
<span id="cloudformation"></span><h1>cloudformation<a class="headerlink" href="#module-pulumi_aws.cloudformation" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.cloudformation.GetExportResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.cloudformation.</code><code class="descname">GetExportResult</code><span class="sig-paren">(</span><em>exporting_stack_id=None</em>, <em>value=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.GetExportResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getExport.</p>
<dl class="attribute">
<dt id="pulumi_aws.cloudformation.GetExportResult.exporting_stack_id">
<code class="descname">exporting_stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.GetExportResult.exporting_stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The exporting_stack_id (AWS ARNs) equivalent <cite>ExportingStackId</cite> from [list-exports](<a class="reference external" href="http://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-exports.html">http://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-exports.html</a>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.GetExportResult.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.GetExportResult.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value from Cloudformation export identified by the export name found from [list-exports](<a class="reference external" href="http://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-exports.html">http://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-exports.html</a>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.GetExportResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.GetExportResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.cloudformation.GetStackResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.cloudformation.</code><code class="descname">GetStackResult</code><span class="sig-paren">(</span><em>capabilities=None</em>, <em>description=None</em>, <em>disable_rollback=None</em>, <em>iam_role_arn=None</em>, <em>notification_arns=None</em>, <em>outputs=None</em>, <em>parameters=None</em>, <em>tags=None</em>, <em>template_body=None</em>, <em>timeout_in_minutes=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.GetStackResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getStack.</p>
<dl class="attribute">
<dt id="pulumi_aws.cloudformation.GetStackResult.capabilities">
<code class="descname">capabilities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.GetStackResult.capabilities" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of capabilities</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.GetStackResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.GetStackResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the stack</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.GetStackResult.disable_rollback">
<code class="descname">disable_rollback</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.GetStackResult.disable_rollback" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the rollback of the stack is disabled when stack creation fails</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.GetStackResult.iam_role_arn">
<code class="descname">iam_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.GetStackResult.iam_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role used to create the stack.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.GetStackResult.notification_arns">
<code class="descname">notification_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.GetStackResult.notification_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SNS topic ARNs to publish stack related events</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.GetStackResult.outputs">
<code class="descname">outputs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.GetStackResult.outputs" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of outputs from the stack.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.GetStackResult.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.GetStackResult.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of parameters that specify input parameters for the stack.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.GetStackResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.GetStackResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags associated with this stack.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.GetStackResult.template_body">
<code class="descname">template_body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.GetStackResult.template_body" title="Permalink to this definition">¶</a></dt>
<dd><p>Structure containing the template body.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.GetStackResult.timeout_in_minutes">
<code class="descname">timeout_in_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.GetStackResult.timeout_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time that can pass before the stack status becomes <cite>CREATE_FAILED</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.GetStackResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.GetStackResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.cloudformation.Stack">
<em class="property">class </em><code class="descclassname">pulumi_aws.cloudformation.</code><code class="descname">Stack</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>capabilities=None</em>, <em>disable_rollback=None</em>, <em>iam_role_arn=None</em>, <em>name=None</em>, <em>notification_arns=None</em>, <em>on_failure=None</em>, <em>parameters=None</em>, <em>policy_body=None</em>, <em>policy_url=None</em>, <em>tags=None</em>, <em>template_body=None</em>, <em>template_url=None</em>, <em>timeout_in_minutes=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.Stack" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CloudFormation Stack resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of capabilities.
Valid values: <cite>CAPABILITY_IAM</cite> or <cite>CAPABILITY_NAMED_IAM</cite></li>
<li><strong>disable_rollback</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true to disable rollback of the stack if stack creation failed.
Conflicts with <cite>on_failure</cite>.</li>
<li><strong>iam_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don’t specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Stack name.</li>
<li><strong>notification_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of SNS topic ARNs to publish stack related events.</li>
<li><strong>on_failure</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action to be taken if stack creation fails. This must be
one of: <cite>DO_NOTHING</cite>, <cite>ROLLBACK</cite>, or <cite>DELETE</cite>. Conflicts with <cite>disable_rollback</cite>.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Parameter structures that specify input parameters for the stack.</li>
<li><strong>policy_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Structure containing the stack policy body.
Conflicts w/ <cite>policy_url</cite>.</li>
<li><strong>policy_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Location of a file containing the stack policy.
Conflicts w/ <cite>policy_body</cite>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of tags to associate with this stack.</li>
<li><strong>template_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Structure containing the template body (max size: 51,200 bytes).</li>
<li><strong>template_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Location of a file containing the template body (max size: 460,800 bytes).</li>
<li><strong>timeout_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The amount of time that can pass before the stack status becomes <cite>CREATE_FAILED</cite>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.cloudformation.Stack.capabilities">
<code class="descname">capabilities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.capabilities" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of capabilities.
Valid values: <cite>CAPABILITY_IAM</cite> or <cite>CAPABILITY_NAMED_IAM</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.Stack.disable_rollback">
<code class="descname">disable_rollback</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.disable_rollback" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to true to disable rollback of the stack if stack creation failed.
Conflicts with <cite>on_failure</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.Stack.iam_role_arn">
<code class="descname">iam_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.iam_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don’t specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.Stack.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Stack name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.Stack.notification_arns">
<code class="descname">notification_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.notification_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of SNS topic ARNs to publish stack related events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.Stack.on_failure">
<code class="descname">on_failure</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.on_failure" title="Permalink to this definition">¶</a></dt>
<dd><p>Action to be taken if stack creation fails. This must be
one of: <cite>DO_NOTHING</cite>, <cite>ROLLBACK</cite>, or <cite>DELETE</cite>. Conflicts with <cite>disable_rollback</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.Stack.outputs">
<code class="descname">outputs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.outputs" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of outputs from the stack.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.Stack.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Parameter structures that specify input parameters for the stack.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.Stack.policy_body">
<code class="descname">policy_body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.policy_body" title="Permalink to this definition">¶</a></dt>
<dd><p>Structure containing the stack policy body.
Conflicts w/ <cite>policy_url</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.Stack.policy_url">
<code class="descname">policy_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.policy_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Location of a file containing the stack policy.
Conflicts w/ <cite>policy_body</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.Stack.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to associate with this stack.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.Stack.template_body">
<code class="descname">template_body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.template_body" title="Permalink to this definition">¶</a></dt>
<dd><p>Structure containing the template body (max size: 51,200 bytes).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.Stack.template_url">
<code class="descname">template_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.template_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Location of a file containing the template body (max size: 460,800 bytes).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.Stack.timeout_in_minutes">
<code class="descname">timeout_in_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.timeout_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time that can pass before the stack status becomes <cite>CREATE_FAILED</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cloudformation.Stack.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cloudformation.Stack.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.cloudformation.get_export">
<code class="descclassname">pulumi_aws.cloudformation.</code><code class="descname">get_export</code><span class="sig-paren">(</span><em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.get_export" title="Permalink to this definition">¶</a></dt>
<dd><p>The CloudFormation Export data source allows access to stack
exports specified in the [Output](<a class="reference external" href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html">http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html</a>) section of the Cloudformation Template using the optional Export Property.</p>
<blockquote>
<div>-&gt; Note: If you are trying to use a value from a Cloudformation Stack in the same Terraform run please use normal interpolation or Cloudformation Outputs.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.cloudformation.get_stack">
<code class="descclassname">pulumi_aws.cloudformation.</code><code class="descname">get_stack</code><span class="sig-paren">(</span><em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.get_stack" title="Permalink to this definition">¶</a></dt>
<dd><p>The CloudFormation Stack data source allows access to stack
outputs and other useful data including the template body.</p>
</dd></dl>

</div>
