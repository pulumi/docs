---
---

<div class="section" id="sfn">
<h1>sfn<a class="headerlink" href="#sfn" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.sfn"></span><dl class="class">
<dt id="pulumi_aws.sfn.Activity">
<em class="property">class </em><code class="descclassname">pulumi_aws.sfn.</code><code class="descname">Activity</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sfn.Activity" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Step Function Activity resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the activity to create.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sfn_activity.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sfn_activity.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.sfn.Activity.creation_date">
<code class="descname">creation_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sfn.Activity.creation_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the activity was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sfn.Activity.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sfn.Activity.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the activity to create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sfn.Activity.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sfn.Activity.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sfn.Activity.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sfn.Activity.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sfn.Activity.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sfn.Activity.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sfn.StateMachine">
<em class="property">class </em><code class="descclassname">pulumi_aws.sfn.</code><code class="descname">StateMachine</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>definition=None</em>, <em>name=None</em>, <em>role_arn=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sfn.StateMachine" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Step Function State Machine resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>definition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon States Language definition of the state machine.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the state machine.</li>
<li><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the IAM role to use for this state machine.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sfn_state_machine.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sfn_state_machine.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.sfn.StateMachine.creation_date">
<code class="descname">creation_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sfn.StateMachine.creation_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date the state machine was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sfn.StateMachine.definition">
<code class="descname">definition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sfn.StateMachine.definition" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon States Language definition of the state machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sfn.StateMachine.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sfn.StateMachine.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the state machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sfn.StateMachine.role_arn">
<code class="descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sfn.StateMachine.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the IAM role to use for this state machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sfn.StateMachine.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sfn.StateMachine.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current status of the state machine. Either “ACTIVE” or “DELETING”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sfn.StateMachine.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sfn.StateMachine.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sfn.StateMachine.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sfn.StateMachine.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sfn.StateMachine.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sfn.StateMachine.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
