---
---

<div class="section" id="cloudformation">
<h1>cloudformation<a class="headerlink" href="#cloudformation" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.cloudformation"></span><dl class="class">
<dt id="pulumi_aws.cloudformation.GetExportResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.cloudformation.</code><code class="descname">GetExportResult</code><span class="sig-paren">(</span><em>exporting_stack_id=None</em>, <em>name=None</em>, <em>value=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.GetExportResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getExport.</p>
<dl class="attribute">
<dt id="pulumi_aws.cloudformation.GetExportResult.exporting_stack_id">
<code class="descname">exporting_stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.GetExportResult.exporting_stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The exporting_stack_id (AWS ARNs) equivalent <code class="docutils literal notranslate"><span class="pre">ExportingStackId</span></code> from <a class="reference external" href="http://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-exports.html">list-exports</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.GetExportResult.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.GetExportResult.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value from Cloudformation export identified by the export name found from <a class="reference external" href="http://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-exports.html">list-exports</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.GetExportResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.GetExportResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.cloudformation.GetStackResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.cloudformation.</code><code class="descname">GetStackResult</code><span class="sig-paren">(</span><em>capabilities=None</em>, <em>description=None</em>, <em>disable_rollback=None</em>, <em>iam_role_arn=None</em>, <em>name=None</em>, <em>notification_arns=None</em>, <em>outputs=None</em>, <em>parameters=None</em>, <em>tags=None</em>, <em>template_body=None</em>, <em>timeout_in_minutes=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.GetStackResult" title="Permalink to this definition">¶</a></dt>
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
<dd><p>The amount of time that can pass before the stack status becomes <code class="docutils literal notranslate"><span class="pre">CREATE_FAILED</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.GetStackResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.GetStackResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.cloudformation.Stack">
<em class="property">class </em><code class="descclassname">pulumi_aws.cloudformation.</code><code class="descname">Stack</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>capabilities=None</em>, <em>disable_rollback=None</em>, <em>iam_role_arn=None</em>, <em>name=None</em>, <em>notification_arns=None</em>, <em>on_failure=None</em>, <em>parameters=None</em>, <em>policy_body=None</em>, <em>policy_url=None</em>, <em>tags=None</em>, <em>template_body=None</em>, <em>template_url=None</em>, <em>timeout_in_minutes=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.Stack" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CloudFormation Stack resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of capabilities.
Valid values: <code class="docutils literal notranslate"><span class="pre">CAPABILITY_IAM</span></code>, <code class="docutils literal notranslate"><span class="pre">CAPABILITY_NAMED_IAM</span></code>, or <code class="docutils literal notranslate"><span class="pre">CAPABILITY_AUTO_EXPAND</span></code></li>
<li><strong>disable_rollback</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true to disable rollback of the stack if stack creation failed.
Conflicts with <code class="docutils literal notranslate"><span class="pre">on_failure</span></code>.</li>
<li><strong>iam_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM role that AWS CloudFormation assumes to create the stack. If you don’t specify a value, AWS CloudFormation uses the role that was previously associated with the stack. If no role is available, AWS CloudFormation uses a temporary session that is generated from your user credentials.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Stack name.</li>
<li><strong>notification_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of SNS topic ARNs to publish stack related events.</li>
<li><strong>on_failure</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action to be taken if stack creation fails. This must be
one of: <code class="docutils literal notranslate"><span class="pre">DO_NOTHING</span></code>, <code class="docutils literal notranslate"><span class="pre">ROLLBACK</span></code>, or <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">disable_rollback</span></code>.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Parameter structures that specify input parameters for the stack.</li>
<li><strong>policy_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Structure containing the stack policy body.
Conflicts w/ <code class="docutils literal notranslate"><span class="pre">policy_url</span></code>.</li>
<li><strong>policy_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Location of a file containing the stack policy.
Conflicts w/ <code class="docutils literal notranslate"><span class="pre">policy_body</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of tags to associate with this stack.</li>
<li><strong>template_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Structure containing the template body (max size: 51,200 bytes).</li>
<li><strong>template_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Location of a file containing the template body (max size: 460,800 bytes).</li>
<li><strong>timeout_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time that can pass before the stack status becomes <code class="docutils literal notranslate"><span class="pre">CREATE_FAILED</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudformation_stack.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudformation_stack.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cloudformation.Stack.capabilities">
<code class="descname">capabilities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.capabilities" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of capabilities.
Valid values: <code class="docutils literal notranslate"><span class="pre">CAPABILITY_IAM</span></code>, <code class="docutils literal notranslate"><span class="pre">CAPABILITY_NAMED_IAM</span></code>, or <code class="docutils literal notranslate"><span class="pre">CAPABILITY_AUTO_EXPAND</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.Stack.disable_rollback">
<code class="descname">disable_rollback</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.disable_rollback" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to true to disable rollback of the stack if stack creation failed.
Conflicts with <code class="docutils literal notranslate"><span class="pre">on_failure</span></code>.</p>
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
one of: <code class="docutils literal notranslate"><span class="pre">DO_NOTHING</span></code>, <code class="docutils literal notranslate"><span class="pre">ROLLBACK</span></code>, or <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">disable_rollback</span></code>.</p>
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
Conflicts w/ <code class="docutils literal notranslate"><span class="pre">policy_url</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.Stack.policy_url">
<code class="descname">policy_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.policy_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Location of a file containing the stack policy.
Conflicts w/ <code class="docutils literal notranslate"><span class="pre">policy_body</span></code>.</p>
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
<dd><p>The amount of time that can pass before the stack status becomes <code class="docutils literal notranslate"><span class="pre">CREATE_FAILED</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cloudformation.Stack.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudformation.Stack.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.Stack.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudformation.StackSet">
<em class="property">class </em><code class="descclassname">pulumi_aws.cloudformation.</code><code class="descname">StackSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>administration_role_arn=None</em>, <em>capabilities=None</em>, <em>description=None</em>, <em>execution_role_name=None</em>, <em>name=None</em>, <em>parameters=None</em>, <em>tags=None</em>, <em>template_body=None</em>, <em>template_url=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.StackSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a CloudFormation Stack Set. Stack Sets allow CloudFormation templates to be easily deployed across multiple accounts and regions via Stack Set Instances (<cite>``aws_cloudformation_stack_set_instance`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set_instance.html">https://www.terraform.io/docs/providers/aws/r/cloudformation_stack_set_instance.html</a>&gt;`_). Additional information about Stack Sets can be found in the <a class="reference external" href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html">AWS CloudFormation User Guide</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> All template parameters, including those with a <code class="docutils literal notranslate"><span class="pre">Default</span></code>, must be configured or ignored with the <code class="docutils literal notranslate"><span class="pre">lifecycle</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">ignore_changes</span></code> argument.</p>
<p><strong>NOTE:</strong> All <code class="docutils literal notranslate"><span class="pre">NoEcho</span></code> template parameters must be ignored with the <code class="docutils literal notranslate"><span class="pre">lifecycle</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">ignore_changes</span></code> argument.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>administration_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Number (ARN) of the IAM Role in the administrator account.</li>
<li><strong>capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of capabilities. Valid values: <code class="docutils literal notranslate"><span class="pre">CAPABILITY_IAM</span></code>, <code class="docutils literal notranslate"><span class="pre">CAPABILITY_NAMED_IAM</span></code>, <code class="docutils literal notranslate"><span class="pre">CAPABILITY_AUTO_EXPAND</span></code>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the Stack Set.</li>
<li><strong>execution_role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the IAM Role in all target accounts for Stack Set operations. Defaults to <code class="docutils literal notranslate"><span class="pre">AWSCloudFormationStackSetExecutionRole</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Stack Set. The name must be unique in the region where you create your Stack Set. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value map of input parameters for the Stack Set template. All template parameters, including those with a <code class="docutils literal notranslate"><span class="pre">Default</span></code>, must be configured or ignored with <code class="docutils literal notranslate"><span class="pre">lifecycle</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">ignore_changes</span></code> argument. All <code class="docutils literal notranslate"><span class="pre">NoEcho</span></code> template parameters must be ignored with the <code class="docutils literal notranslate"><span class="pre">lifecycle</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">ignore_changes</span></code> argument.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value map of tags to associate with this Stack Set and the Stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the Stacks. A maximum number of 50 tags can be specified.</li>
<li><strong>template_body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String containing the CloudFormation template body. Maximum size: 51,200 bytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">template_url</span></code>.</li>
<li><strong>template_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String containing the location of a file containing the CloudFormation template body. The URL must point to a template that is located in an Amazon S3 bucket. Maximum location file size: 460,800 bytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">template_body</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudformation_stack_set.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudformation_stack_set.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cloudformation.StackSet.administration_role_arn">
<code class="descname">administration_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.StackSet.administration_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Number (ARN) of the IAM Role in the administrator account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.StackSet.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.StackSet.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the Stack Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.StackSet.capabilities">
<code class="descname">capabilities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.StackSet.capabilities" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of capabilities. Valid values: <code class="docutils literal notranslate"><span class="pre">CAPABILITY_IAM</span></code>, <code class="docutils literal notranslate"><span class="pre">CAPABILITY_NAMED_IAM</span></code>, <code class="docutils literal notranslate"><span class="pre">CAPABILITY_AUTO_EXPAND</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.StackSet.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.StackSet.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the Stack Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.StackSet.execution_role_name">
<code class="descname">execution_role_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.StackSet.execution_role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the IAM Role in all target accounts for Stack Set operations. Defaults to <code class="docutils literal notranslate"><span class="pre">AWSCloudFormationStackSetExecutionRole</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.StackSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.StackSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Stack Set. The name must be unique in the region where you create your Stack Set. The name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and cannot be longer than 128 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.StackSet.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.StackSet.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value map of input parameters for the Stack Set template. All template parameters, including those with a <code class="docutils literal notranslate"><span class="pre">Default</span></code>, must be configured or ignored with <code class="docutils literal notranslate"><span class="pre">lifecycle</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">ignore_changes</span></code> argument. All <code class="docutils literal notranslate"><span class="pre">NoEcho</span></code> template parameters must be ignored with the <code class="docutils literal notranslate"><span class="pre">lifecycle</span></code> configuration block <code class="docutils literal notranslate"><span class="pre">ignore_changes</span></code> argument.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.StackSet.stack_set_id">
<code class="descname">stack_set_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.StackSet.stack_set_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the Stack Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.StackSet.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.StackSet.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value map of tags to associate with this Stack Set and the Stacks created from it. AWS CloudFormation also propagates these tags to supported resources that are created in the Stacks. A maximum number of 50 tags can be specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.StackSet.template_body">
<code class="descname">template_body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.StackSet.template_body" title="Permalink to this definition">¶</a></dt>
<dd><p>String containing the CloudFormation template body. Maximum size: 51,200 bytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">template_url</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.StackSet.template_url">
<code class="descname">template_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.StackSet.template_url" title="Permalink to this definition">¶</a></dt>
<dd><p>String containing the location of a file containing the CloudFormation template body. The URL must point to a template that is located in an Amazon S3 bucket. Maximum location file size: 460,800 bytes. Conflicts with <code class="docutils literal notranslate"><span class="pre">template_body</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cloudformation.StackSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.StackSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudformation.StackSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.StackSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudformation.StackSetInstance">
<em class="property">class </em><code class="descclassname">pulumi_aws.cloudformation.</code><code class="descname">StackSetInstance</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_id=None</em>, <em>parameter_overrides=None</em>, <em>region=None</em>, <em>retain_stack=None</em>, <em>stack_set_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.StackSetInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a StackSetInstance resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target AWS Account ID to create a Stack based on the Stack Set. Defaults to current account.</li>
<li><strong>parameter_overrides</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value map of input parameters to override from the Stack Set for this Instance.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Target AWS Region to create a Stack based on the Stack Set. Defaults to current region.</li>
<li><strong>stack_set_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Stack Set.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudformation_stack_set_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudformation_stack_set_instance.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cloudformation.StackSetInstance.account_id">
<code class="descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.StackSetInstance.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Target AWS Account ID to create a Stack based on the Stack Set. Defaults to current account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.StackSetInstance.parameter_overrides">
<code class="descname">parameter_overrides</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.StackSetInstance.parameter_overrides" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value map of input parameters to override from the Stack Set for this Instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.StackSetInstance.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.StackSetInstance.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Target AWS Region to create a Stack based on the Stack Set. Defaults to current region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.StackSetInstance.stack_id">
<code class="descname">stack_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.StackSetInstance.stack_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Stack identifier</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudformation.StackSetInstance.stack_set_name">
<code class="descname">stack_set_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudformation.StackSetInstance.stack_set_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Stack Set.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cloudformation.StackSetInstance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.StackSetInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudformation.StackSetInstance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.StackSetInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudformation.get_export">
<code class="descclassname">pulumi_aws.cloudformation.</code><code class="descname">get_export</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.get_export" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/cloudformation_export.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/cloudformation_export.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.cloudformation.get_stack">
<code class="descclassname">pulumi_aws.cloudformation.</code><code class="descname">get_stack</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudformation.get_stack" title="Permalink to this definition">¶</a></dt>
<dd><p>The CloudFormation Stack data source allows access to stack
outputs and other useful data including the template body.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/cloudformation_stack.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/cloudformation_stack.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
