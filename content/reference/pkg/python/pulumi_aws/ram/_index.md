<div class="section" id="module-pulumi_aws.ram">
<span id="ram"></span><h1>ram<a class="headerlink" href="#module-pulumi_aws.ram" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.ram.PrincipalAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.ram.</code><code class="descname">PrincipalAssociation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>principal=None</em>, <em>resource_share_arn=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Resource Access Manager (RAM) principal association.</p>
<blockquote>
<div><em>NOTE:</em> For an AWS Account ID principal, the target account must accept the RAM association invitation after resource creation.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The principal to associate with the resource share. Possible values are an AWS account ID, an AWS Organizations Organization ARN, or an AWS Organizations Organization Unit ARN.</li>
<li><strong>resource_share_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the resource share.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.ram.PrincipalAssociation.principal">
<code class="descname">principal</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation.principal" title="Permalink to this definition">¶</a></dt>
<dd><p>The principal to associate with the resource share. Possible values are an AWS account ID, an AWS Organizations Organization ARN, or an AWS Organizations Organization Unit ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ram.PrincipalAssociation.resource_share_arn">
<code class="descname">resource_share_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation.resource_share_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the resource share.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ram.PrincipalAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ram.PrincipalAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ram.ResourceAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.ram.</code><code class="descname">ResourceAssociation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>resource_arn=None</em>, <em>resource_share_arn=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Resource Access Manager (RAM) Resource Association.</p>
<blockquote>
<div><em>NOTE:</em> Certain AWS resources (e.g. EC2 Subnets) can only be shared in an AWS account that is a member of an AWS Organizations organization with organization-wide Resource Access Manager functionality enabled. See the <a class="reference external" href="https://docs.aws.amazon.com/ram/latest/userguide/what-is.html">Resource Access Manager User Guide</a> and AWS service specific documentation for additional information.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>resource_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the resource to associate with the RAM Resource Share.</li>
<li><strong>resource_share_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the RAM Resource Share.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.ram.ResourceAssociation.resource_arn">
<code class="descname">resource_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation.resource_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the resource to associate with the RAM Resource Share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ram.ResourceAssociation.resource_share_arn">
<code class="descname">resource_share_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation.resource_share_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the RAM Resource Share.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ram.ResourceAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ram.ResourceAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ram.ResourceShare">
<em class="property">class </em><code class="descclassname">pulumi_aws.ram.</code><code class="descname">ResourceShare</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allow_external_principals=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceShare" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Resource Access Manager (RAM) Resource Share. To association principals with the share, see the <cite>``aws_ram_principal_association`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/ram_principal_association.html">https://www.terraform.io/docs/providers/aws/r/ram_principal_association.html</a>&gt;`_. To associate resources with the share, see the <cite>``aws_ram_resource_association`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/ram_resource_association.html">https://www.terraform.io/docs/providers/aws/r/ram_resource_association.html</a>&gt;`_.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allow_external_principals</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether principals outside your organization can be associated with a resource share.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource share.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource share.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.ram.ResourceShare.allow_external_principals">
<code class="descname">allow_external_principals</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.allow_external_principals" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether principals outside your organization can be associated with a resource share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ram.ResourceShare.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the resource share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ram.ResourceShare.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ram.ResourceShare.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource share.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ram.ResourceShare.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ram.ResourceShare.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
