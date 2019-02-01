<div class="section" id="module-pulumi_aws.swf">
<span id="swf"></span><h1>swf<a class="headerlink" href="#module-pulumi_aws.swf" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.swf.Domain">
<em class="property">class </em><code class="descclassname">pulumi_aws.swf.</code><code class="descname">Domain</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>workflow_execution_retention_period_in_days=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.swf.Domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SWF Domain resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain description.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the domain. If omitted, Terraform will assign a random, unique name.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <cite>name</cite>.</li>
<li><strong>workflow_execution_retention_period_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Length of time that SWF will continue to retain information about the workflow execution after the workflow execution is complete, must be between 0 and 90 days.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.swf.Domain.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.swf.Domain.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.swf.Domain.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.swf.Domain.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the domain. If omitted, Terraform will assign a random, unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.swf.Domain.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.swf.Domain.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <cite>name</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.swf.Domain.workflow_execution_retention_period_in_days">
<code class="descname">workflow_execution_retention_period_in_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.swf.Domain.workflow_execution_retention_period_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Length of time that SWF will continue to retain information about the workflow execution after the workflow execution is complete, must be between 0 and 90 days.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.swf.Domain.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.swf.Domain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.swf.Domain.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.swf.Domain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
