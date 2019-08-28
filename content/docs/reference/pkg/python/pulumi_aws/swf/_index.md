---
title: Module swf
---

<div class="section" id="swf">
<h1>swf<a class="headerlink" href="#swf" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.swf"></span><dl class="class">
<dt id="pulumi_aws.swf.Domain">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.swf.</code><code class="sig-name descname">Domain</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">workflow_execution_retention_period_in_days=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.swf.Domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SWF Domain resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain description.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the domain. If omitted, this provider will assign a random, unique name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>workflow_execution_retention_period_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Length of time that SWF will continue to retain information about the workflow execution after the workflow execution is complete, must be between 0 and 90 days.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/swf_domain.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/swf_domain.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.swf.Domain.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.swf.Domain.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.swf.Domain.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.swf.Domain.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the domain. If omitted, this provider will assign a random, unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.swf.Domain.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.swf.Domain.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.swf.Domain.workflow_execution_retention_period_in_days">
<code class="sig-name descname">workflow_execution_retention_period_in_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.swf.Domain.workflow_execution_retention_period_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Length of time that SWF will continue to retain information about the workflow execution after the workflow execution is complete, must be between 0 and 90 days.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.swf.Domain.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">workflow_execution_retention_period_in_days=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.swf.Domain.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Domain resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: The domain description.
:param pulumi.Input[str] name: The name of the domain. If omitted, this provider will assign a random, unique name.
:param pulumi.Input[str] name_prefix: Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.
:param pulumi.Input[str] workflow_execution_retention_period_in_days: Length of time that SWF will continue to retain information about the workflow execution after the workflow execution is complete, must be between 0 and 90 days.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/swf_domain.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/swf_domain.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.swf.Domain.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.swf.Domain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.swf.Domain.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.swf.Domain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
