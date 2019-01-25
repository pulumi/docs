<div class="section" id="module-pulumi_aws.dlm">
<span id="dlm"></span><h1>dlm<a class="headerlink" href="#module-pulumi_aws.dlm" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.dlm.LifecyclePolicy">
<em class="property">class </em><code class="descclassname">pulumi_aws.dlm.</code><code class="descname">LifecyclePolicy</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>execution_role_arn=None</em>, <em>policy_details=None</em>, <em>state=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a [Data Lifecycle Manager (DLM) lifecycle policy](<a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html">https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html</a>) for managing snapshots.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the DLM lifecycle policy.</li>
<li><strong>execution_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM role that is able to be assumed by the DLM service.</li>
<li><strong>policy_details</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – See the <cite>policy_details</cite> configuration block. Max of 1.</li>
<li><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the lifecycle policy should be enabled or disabled. <cite>ENABLED</cite> or <cite>DISABLED</cite> are valid values. Defaults to <cite>ENABLED</cite>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.dlm.LifecyclePolicy.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the DLM lifecycle policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dlm.LifecyclePolicy.execution_role_arn">
<code class="descname">execution_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.execution_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM role that is able to be assumed by the DLM service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dlm.LifecyclePolicy.policy_details">
<code class="descname">policy_details</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.policy_details" title="Permalink to this definition">¶</a></dt>
<dd><p>See the <cite>policy_details</cite> configuration block. Max of 1.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dlm.LifecyclePolicy.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the lifecycle policy should be enabled or disabled. <cite>ENABLED</cite> or <cite>DISABLED</cite> are valid values. Defaults to <cite>ENABLED</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dlm.LifecyclePolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dlm.LifecyclePolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
