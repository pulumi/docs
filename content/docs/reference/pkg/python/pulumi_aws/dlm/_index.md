---
title: Module dlm
---

<div class="section" id="dlm">
<h1>dlm<a class="headerlink" href="#dlm" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.dlm"></span><dl class="class">
<dt id="pulumi_aws.dlm.LifecyclePolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.dlm.</code><code class="sig-name descname">LifecyclePolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">execution_role_arn=None</em>, <em class="sig-param">policy_details=None</em>, <em class="sig-param">state=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy" title="Permalink to this definition">¶</a></dt>
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
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dlm_lifecycle_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dlm_lifecycle_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.dlm.LifecyclePolicy.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the DLM lifecycle policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dlm.LifecyclePolicy.execution_role_arn">
<code class="sig-name descname">execution_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.execution_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of an IAM role that is able to be assumed by the DLM service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dlm.LifecyclePolicy.policy_details">
<code class="sig-name descname">policy_details</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.policy_details" title="Permalink to this definition">¶</a></dt>
<dd><p>See the <code class="docutils literal notranslate"><span class="pre">policy_details</span></code> configuration block. Max of 1.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.dlm.LifecyclePolicy.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the lifecycle policy should be enabled or disabled. <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code> are valid values. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dlm.LifecyclePolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">execution_role_arn=None</em>, <em class="sig-param">policy_details=None</em>, <em class="sig-param">state=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LifecyclePolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: A description for the DLM lifecycle policy.
:param pulumi.Input[str] execution_role_arn: The ARN of an IAM role that is able to be assumed by the DLM service.
:param pulumi.Input[dict] policy_details: See the <code class="docutils literal notranslate"><span class="pre">policy_details</span></code> configuration block. Max of 1.
:param pulumi.Input[str] state: Whether the lifecycle policy should be enabled or disabled. <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code> are valid values. Defaults to <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dlm_lifecycle_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dlm_lifecycle_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.dlm.LifecyclePolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.dlm.LifecyclePolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.dlm.LifecyclePolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
