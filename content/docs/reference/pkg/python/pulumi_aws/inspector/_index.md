---
title: Module inspector
title_tag: Module inspector | Package pulumi_aws | Python SDK
linktitle: inspector
notitle: true
---

<div class="section" id="inspector">
<h1>inspector<a class="headerlink" href="#inspector" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.inspector"></span><dl class="class">
<dt id="pulumi_aws.inspector.AssessmentTarget">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.inspector.</code><code class="sig-name descname">AssessmentTarget</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTarget" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Inspector assessment target</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the assessment target.</p></li>
<li><p><strong>resource_group_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Inspector Resource Group Amazon Resource Name (ARN) stating tags for instance matching. If not specified, all EC2 instances in the current AWS account and region are included in the assessment target.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.inspector.AssessmentTarget.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTarget.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The target assessment ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.inspector.AssessmentTarget.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTarget.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the assessment target.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.inspector.AssessmentTarget.resource_group_arn">
<code class="sig-name descname">resource_group_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTarget.resource_group_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Inspector Resource Group Amazon Resource Name (ARN) stating tags for instance matching. If not specified, all EC2 instances in the current AWS account and region are included in the assessment target.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.inspector.AssessmentTarget.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTarget.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AssessmentTarget resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target assessment ARN.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the assessment target.</p></li>
<li><p><strong>resource_group_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Inspector Resource Group Amazon Resource Name (ARN) stating tags for instance matching. If not specified, all EC2 instances in the current AWS account and region are included in the assessment target.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.inspector.AssessmentTarget.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTarget.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.inspector.AssessmentTarget.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTarget.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.inspector.AssessmentTemplate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.inspector.</code><code class="sig-name descname">AssessmentTemplate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">duration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rules_package_arns=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Inspector assessment template</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration of the inspector run.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the assessment template.</p></li>
<li><p><strong>rules_package_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The rules to be used during the run.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of tags for the Inspector assessment template.</p></li>
<li><p><strong>target_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The assessment target ARN to attach the template to.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.inspector.AssessmentTemplate.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The template assessment ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.inspector.AssessmentTemplate.duration">
<code class="sig-name descname">duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate.duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration of the inspector run.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.inspector.AssessmentTemplate.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the assessment template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.inspector.AssessmentTemplate.rules_package_arns">
<code class="sig-name descname">rules_package_arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate.rules_package_arns" title="Permalink to this definition">¶</a></dt>
<dd><p>The rules to be used during the run.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.inspector.AssessmentTemplate.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of tags for the Inspector assessment template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.inspector.AssessmentTemplate.target_arn">
<code class="sig-name descname">target_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate.target_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The assessment target ARN to attach the template to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.inspector.AssessmentTemplate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">duration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">rules_package_arns=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AssessmentTemplate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The template assessment ARN.</p></li>
<li><p><strong>duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration of the inspector run.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the assessment template.</p></li>
<li><p><strong>rules_package_arns</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The rules to be used during the run.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of tags for the Inspector assessment template.</p></li>
<li><p><strong>target_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The assessment target ARN to attach the template to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.inspector.AssessmentTemplate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.inspector.AssessmentTemplate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.AssessmentTemplate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.inspector.AwaitableGetRulesPackagesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.inspector.</code><code class="sig-name descname">AwaitableGetRulesPackagesResult</code><span class="sig-paren">(</span><em class="sig-param">arns=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.AwaitableGetRulesPackagesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.inspector.GetRulesPackagesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.inspector.</code><code class="sig-name descname">GetRulesPackagesResult</code><span class="sig-paren">(</span><em class="sig-param">arns=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.GetRulesPackagesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRulesPackages.</p>
<dl class="attribute">
<dt id="pulumi_aws.inspector.GetRulesPackagesResult.arns">
<code class="sig-name descname">arns</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.GetRulesPackagesResult.arns" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the AWS Inspector Rules Packages arns available in the AWS region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.inspector.GetRulesPackagesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.GetRulesPackagesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.inspector.ResourceGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.inspector.</code><code class="sig-name descname">ResourceGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.ResourceGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Amazon Inspector resource group resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value map of tags that are used to select the EC2 instances to be included in an <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/inspector_assessment_target.html">Amazon Inspector assessment target</a>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.inspector.ResourceGroup.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.ResourceGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource group ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.inspector.ResourceGroup.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.inspector.ResourceGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value map of tags that are used to select the EC2 instances to be included in an <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/inspector_assessment_target.html">Amazon Inspector assessment target</a>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.inspector.ResourceGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.ResourceGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResourceGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource group ARN.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Key-value map of tags that are used to select the EC2 instances to be included in an <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/inspector_assessment_target.html">Amazon Inspector assessment target</a>.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.inspector.ResourceGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.ResourceGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.inspector.ResourceGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.ResourceGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.inspector.get_rules_packages">
<code class="sig-prename descclassname">pulumi_aws.inspector.</code><code class="sig-name descname">get_rules_packages</code><span class="sig-paren">(</span><em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.inspector.get_rules_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Inspector Rules Packages data source allows access to the list of AWS
Inspector Rules Packages which can be used by AWS Inspector within the region
configured in the provider.</p>
</dd></dl>

</div>
