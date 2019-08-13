---
title: Module inspector
---

<div class="section" id="inspector">
<h1>inspector<a class="headerlink" href="#inspector" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.inspector"></span><dl class="class">
<dt id="pulumi_aws.inspector.AssessmentTarget">
<em class="property">class </em><code class="descclassname">pulumi_aws.inspector.</code><code class="descname">AssessmentTarget</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>resource_group_arn=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTarget" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Inspector assessment target</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the assessment target.</li>
<li><strong>resource_group_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Inspector Resource Group Amazon Resource Name (ARN) stating tags for instance matching. If not specified, all EC2 instances in the current AWS account and region are included in the assessment target.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/inspector_assessment_target.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/inspector_assessment_target.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.inspector.AssessmentTarget.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTarget.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The target assessment ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.inspector.AssessmentTarget.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTarget.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the assessment target.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.inspector.AssessmentTarget.resource_group_arn">
<code class="descname">resource_group_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTarget.resource_group_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Inspector Resource Group Amazon Resource Name (ARN) stating tags for instance matching. If not specified, all EC2 instances in the current AWS account and region are included in the assessment target.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_aws.inspector.AssessmentTarget.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>arn=None</em>, <em>name=None</em>, <em>resource_group_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTarget.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AssessmentTarget resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: The target assessment ARN.
:param pulumi.Input[str] name: The name of the assessment target.
:param pulumi.Input[str] resource_group_arn: Inspector Resource Group Amazon Resource Name (ARN) stating tags for instance matching. If not specified, all EC2 instances in the current AWS account and region are included in the assessment target.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/inspector_assessment_target.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/inspector_assessment_target.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.inspector.AssessmentTarget.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTarget.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.inspector.AssessmentTarget.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTarget.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.inspector.AssessmentTemplate">
<em class="property">class </em><code class="descclassname">pulumi_aws.inspector.</code><code class="descname">AssessmentTemplate</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>duration=None</em>, <em>name=None</em>, <em>rules_package_arns=None</em>, <em>target_arn=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Inspector assessment template</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration of the inspector run.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the assessment template.</li>
<li><strong>rules_package_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The rules to be used during the run.</li>
<li><strong>target_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The assessment target ARN to attach the template to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/inspector_assessment_template.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/inspector_assessment_template.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.inspector.AssessmentTemplate.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The template assessment ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.inspector.AssessmentTemplate.duration">
<code class="descname">duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate.duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration of the inspector run.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.inspector.AssessmentTemplate.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the assessment template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.inspector.AssessmentTemplate.rules_package_arns">
<code class="descname">rules_package_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate.rules_package_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>The rules to be used during the run.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.inspector.AssessmentTemplate.target_arn">
<code class="descname">target_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate.target_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The assessment target ARN to attach the template to.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_aws.inspector.AssessmentTemplate.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>arn=None</em>, <em>duration=None</em>, <em>name=None</em>, <em>rules_package_arns=None</em>, <em>target_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AssessmentTemplate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: The template assessment ARN.
:param pulumi.Input[float] duration: The duration of the inspector run.
:param pulumi.Input[str] name: The name of the assessment template.
:param pulumi.Input[list] rules_package_arns: The rules to be used during the run.
:param pulumi.Input[str] target_arn: The assessment target ARN to attach the template to.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/inspector_assessment_template.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/inspector_assessment_template.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.inspector.AssessmentTemplate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.inspector.AssessmentTemplate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.inspector.AwaitableGetRulesPackagesResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.inspector.</code><code class="descname">AwaitableGetRulesPackagesResult</code><span class="sig-paren">(</span><em>arns=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.AwaitableGetRulesPackagesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.inspector.GetRulesPackagesResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.inspector.</code><code class="descname">GetRulesPackagesResult</code><span class="sig-paren">(</span><em>arns=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.GetRulesPackagesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRulesPackages.</p>
<dl class="attribute">
<dt id="pulumi_aws.inspector.GetRulesPackagesResult.arns">
<code class="descname">arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.GetRulesPackagesResult.arns" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the AWS Inspector Rules Packages arns available in the AWS region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.inspector.GetRulesPackagesResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.GetRulesPackagesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.inspector.ResourceGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.inspector.</code><code class="descname">ResourceGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>tags=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.ResourceGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Inspector resource group</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The tags on your EC2 Instance.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/inspector_resource_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/inspector_resource_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.inspector.ResourceGroup.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.ResourceGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource group ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.inspector.ResourceGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.ResourceGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The tags on your EC2 Instance.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_aws.inspector.ResourceGroup.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>arn=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.ResourceGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResourceGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: The resource group ARN.
:param pulumi.Input[dict] tags: The tags on your EC2 Instance.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/inspector_resource_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/inspector_resource_group.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.inspector.ResourceGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.ResourceGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.inspector.ResourceGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.ResourceGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.inspector.get_rules_packages">
<code class="descclassname">pulumi_aws.inspector.</code><code class="descname">get_rules_packages</code><span class="sig-paren">(</span><em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.get_rules_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Inspector Rules Packages data source allows access to the list of AWS
Inspector Rules Packages which can be used by AWS Inspector within the region
configured in the provider.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/inspector_rules_packages.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/inspector_rules_packages.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
