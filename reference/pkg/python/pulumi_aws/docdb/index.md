<div class="section" id="module-pulumi_aws.docdb">
<span id="docdb"></span><h1>docdb<a class="headerlink" href="#module-pulumi_aws.docdb" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.docdb.ClusterParameterGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.docdb.</code><code class="descname">ClusterParameterGroup</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>family=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>parameters=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a DocumentDB Cluster Parameter Group</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the documentDB cluster parameter group. Defaults to “Managed by Terraform”.</li>
<li><strong>family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The family of the documentDB cluster parameter group.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the documentDB parameter.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <cite>name</cite>.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of documentDB parameters to apply.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the documentDB cluster parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the documentDB cluster parameter group. Defaults to “Managed by Terraform”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.family">
<code class="descname">family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.family" title="Permalink to this definition">¶</a></dt>
<dd><p>The family of the documentDB cluster parameter group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the documentDB parameter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <cite>name</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of documentDB parameters to apply.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.docdb.ClusterParameterGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.docdb.ClusterParameterGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.ClusterParameterGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.docdb.SubnetGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.docdb.</code><code class="descname">SubnetGroup</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>subnet_ids=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an DocumentDB subnet group resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the docDB subnet group. Defaults to “Managed by Terraform”.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the docDB subnet group. If omitted, Terraform will assign a random, unique name.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <cite>name</cite>.</li>
<li><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of VPC subnet IDs.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.docdb.SubnetGroup.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the docDB subnet group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.SubnetGroup.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the docDB subnet group. Defaults to “Managed by Terraform”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.SubnetGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the docDB subnet group. If omitted, Terraform will assign a random, unique name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.SubnetGroup.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <cite>name</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.SubnetGroup.subnet_ids">
<code class="descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of VPC subnet IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.docdb.SubnetGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.docdb.SubnetGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.docdb.SubnetGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.docdb.SubnetGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
