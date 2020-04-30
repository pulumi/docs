---
title: Module dlm
title_tag: Module dlm | Package pulumi_aws | Python SDK
linktitle: dlm
notitle: true
---

<div class="section" id="dlm">
<h1>dlm<a class="headerlink" href="#dlm" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.dlm"></span><dl class="py class">
<dt id="pulumi_aws.dlm.LifecyclePolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.dlm.</code><code class="sig-name descname">LifecyclePolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">execution_role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html">Data Lifecycle Manager (DLM) lifecycle policy</a> for managing snapshots.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the DLM lifecycle policy.</p></li>
<li><p><strong>execution_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM role that is able to be assumed by the DLM service.</p></li>
<li><p><strong>policy_details</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – See the <code class="docutils literal notranslate"><span class="pre">policy_details</span></code> configuration block. Max of 1.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the lifecycle policy should be enabled or disabled. <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code> are valid values. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>policy_details</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resourceTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of resource types that should be targeted by the lifecycle policy. <code class="docutils literal notranslate"><span class="pre">VOLUME</span></code> is currently the only allowed value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schedules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - See the <code class="docutils literal notranslate"><span class="pre">schedule</span></code> configuration block.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">copyTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Copy all user-defined tags on a source volume to snapshots of the volume created by this policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">createRule</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See the <code class="docutils literal notranslate"><span class="pre">create_rule</span></code> block. Max of 1 per schedule.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How often this lifecycle policy should be evaluated. <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>,<code class="docutils literal notranslate"><span class="pre">3</span></code>,<code class="docutils literal notranslate"><span class="pre">4</span></code>,<code class="docutils literal notranslate"><span class="pre">6</span></code>,<code class="docutils literal notranslate"><span class="pre">8</span></code>,<code class="docutils literal notranslate"><span class="pre">12</span></code> or <code class="docutils literal notranslate"><span class="pre">24</span></code> are valid values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">intervalUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unit for how often the lifecycle policy should be evaluated. <code class="docutils literal notranslate"><span class="pre">HOURS</span></code> is currently the only allowed value and also the default value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">times</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A list of times in 24 hour clock format that sets when the lifecycle policy should be evaluated. Max of 1.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A name for the schedule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retainRule</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See the <code class="docutils literal notranslate"><span class="pre">retain_rule</span></code> block. Max of 1 per schedule.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How many snapshots to keep. Must be an integer between 1 and 1000.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tagsToAdd</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of tag keys and their values. DLM lifecycle policies will already tag the snapshot with the tags on the volume. This configuration adds extra tags on top of these.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of tag keys and their values. Any resources that match the <code class="docutils literal notranslate"><span class="pre">resource_types</span></code> and are tagged with <em>any</em> of these tags will be targeted.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.dlm.LifecyclePolicy.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the DLM Lifecycle Policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dlm.LifecyclePolicy.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the DLM lifecycle policy.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dlm.LifecyclePolicy.execution_role_arn">
<code class="sig-name descname">execution_role_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.execution_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM role that is able to be assumed by the DLM service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dlm.LifecyclePolicy.policy_details">
<code class="sig-name descname">policy_details</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.policy_details" title="Permalink to this definition">¶</a></dt>
<dd><p>See the <code class="docutils literal notranslate"><span class="pre">policy_details</span></code> configuration block. Max of 1.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resourceTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of resource types that should be targeted by the lifecycle policy. <code class="docutils literal notranslate"><span class="pre">VOLUME</span></code> is currently the only allowed value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schedules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - See the <code class="docutils literal notranslate"><span class="pre">schedule</span></code> configuration block.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">copyTags</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Copy all user-defined tags on a source volume to snapshots of the volume created by this policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">createRule</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - See the <code class="docutils literal notranslate"><span class="pre">create_rule</span></code> block. Max of 1 per schedule.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How often this lifecycle policy should be evaluated. <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>,<code class="docutils literal notranslate"><span class="pre">3</span></code>,<code class="docutils literal notranslate"><span class="pre">4</span></code>,<code class="docutils literal notranslate"><span class="pre">6</span></code>,<code class="docutils literal notranslate"><span class="pre">8</span></code>,<code class="docutils literal notranslate"><span class="pre">12</span></code> or <code class="docutils literal notranslate"><span class="pre">24</span></code> are valid values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">intervalUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The unit for how often the lifecycle policy should be evaluated. <code class="docutils literal notranslate"><span class="pre">HOURS</span></code> is currently the only allowed value and also the default value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">times</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A list of times in 24 hour clock format that sets when the lifecycle policy should be evaluated. Max of 1.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A name for the schedule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retainRule</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - See the <code class="docutils literal notranslate"><span class="pre">retain_rule</span></code> block. Max of 1 per schedule.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How many snapshots to keep. Must be an integer between 1 and 1000.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tagsToAdd</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A mapping of tag keys and their values. DLM lifecycle policies will already tag the snapshot with the tags on the volume. This configuration adds extra tags on top of these.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetTags</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A mapping of tag keys and their values. Any resources that match the <code class="docutils literal notranslate"><span class="pre">resource_types</span></code> and are tagged with <em>any</em> of these tags will be targeted.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dlm.LifecyclePolicy.state">
<code class="sig-name descname">state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the lifecycle policy should be enabled or disabled. <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code> are valid values. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.dlm.LifecyclePolicy.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.dlm.LifecyclePolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">execution_role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LifecyclePolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the DLM Lifecycle Policy.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the DLM lifecycle policy.</p></li>
<li><p><strong>execution_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of an IAM role that is able to be assumed by the DLM service.</p></li>
<li><p><strong>policy_details</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – See the <code class="docutils literal notranslate"><span class="pre">policy_details</span></code> configuration block. Max of 1.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether the lifecycle policy should be enabled or disabled. <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code> are valid values. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>policy_details</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resourceTypes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of resource types that should be targeted by the lifecycle policy. <code class="docutils literal notranslate"><span class="pre">VOLUME</span></code> is currently the only allowed value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">schedules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - See the <code class="docutils literal notranslate"><span class="pre">schedule</span></code> configuration block.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">copyTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Copy all user-defined tags on a source volume to snapshots of the volume created by this policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">createRule</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See the <code class="docutils literal notranslate"><span class="pre">create_rule</span></code> block. Max of 1 per schedule.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How often this lifecycle policy should be evaluated. <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>,<code class="docutils literal notranslate"><span class="pre">3</span></code>,<code class="docutils literal notranslate"><span class="pre">4</span></code>,<code class="docutils literal notranslate"><span class="pre">6</span></code>,<code class="docutils literal notranslate"><span class="pre">8</span></code>,<code class="docutils literal notranslate"><span class="pre">12</span></code> or <code class="docutils literal notranslate"><span class="pre">24</span></code> are valid values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">intervalUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The unit for how often the lifecycle policy should be evaluated. <code class="docutils literal notranslate"><span class="pre">HOURS</span></code> is currently the only allowed value and also the default value.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">times</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A list of times in 24 hour clock format that sets when the lifecycle policy should be evaluated. Max of 1.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A name for the schedule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retainRule</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - See the <code class="docutils literal notranslate"><span class="pre">retain_rule</span></code> block. Max of 1 per schedule.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How many snapshots to keep. Must be an integer between 1 and 1000.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">tagsToAdd</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of tag keys and their values. DLM lifecycle policies will already tag the snapshot with the tags on the volume. This configuration adds extra tags on top of these.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of tag keys and their values. Any resources that match the <code class="docutils literal notranslate"><span class="pre">resource_types</span></code> and are tagged with <em>any</em> of these tags will be targeted.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.dlm.LifecyclePolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dlm.LifecyclePolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
