---
title: Module ram
---

<div class="section" id="ram">
<h1>ram<a class="headerlink" href="#ram" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.ram"></span><dl class="class">
<dt id="pulumi_aws.ram.AwaitableGetResourceShareResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ram.</code><code class="descname">AwaitableGetResourceShareResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>filters=None</em>, <em>id=None</em>, <em>name=None</em>, <em>resource_owner=None</em>, <em>status=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.AwaitableGetResourceShareResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.ram.GetResourceShareResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ram.</code><code class="descname">GetResourceShareResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>filters=None</em>, <em>id=None</em>, <em>name=None</em>, <em>resource_owner=None</em>, <em>status=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.GetResourceShareResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getResourceShare.</p>
<dl class="attribute">
<dt id="pulumi_aws.ram.GetResourceShareResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.GetResourceShareResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the resource share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ram.GetResourceShareResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.GetResourceShareResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the resource share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ram.GetResourceShareResult.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.GetResourceShareResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The Status of the RAM share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ram.GetResourceShareResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.GetResourceShareResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The Tags attached to the RAM share</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ram.PrincipalAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.ram.</code><code class="descname">PrincipalAssociation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>principal=None</em>, <em>resource_share_arn=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation" title="Permalink to this definition">¶</a></dt>
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
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_principal_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_principal_association.html.markdown</a>.</div></blockquote>
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

<dl class="staticmethod">
<dt id="pulumi_aws.ram.PrincipalAssociation.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>principal=None</em>, <em>resource_share_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PrincipalAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] principal: The principal to associate with the resource share. Possible values are an AWS account ID, an AWS Organizations Organization ARN, or an AWS Organizations Organization Unit ARN.
:param pulumi.Input[str] resource_share_arn: The Amazon Resource Name (ARN) of the resource share.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_principal_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_principal_association.html.markdown</a>.</div></blockquote>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.ram.</code><code class="descname">ResourceAssociation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>resource_arn=None</em>, <em>resource_share_arn=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation" title="Permalink to this definition">¶</a></dt>
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
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_resource_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_resource_association.html.markdown</a>.</div></blockquote>
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

<dl class="staticmethod">
<dt id="pulumi_aws.ram.ResourceAssociation.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>resource_arn=None</em>, <em>resource_share_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResourceAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] resource_arn: Amazon Resource Name (ARN) of the resource to associate with the RAM Resource Share.
:param pulumi.Input[str] resource_share_arn: Amazon Resource Name (ARN) of the RAM Resource Share.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_resource_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_resource_association.html.markdown</a>.</div></blockquote>
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
<em class="property">class </em><code class="descclassname">pulumi_aws.ram.</code><code class="descname">ResourceShare</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allow_external_principals=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceShare" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Resource Access Manager (RAM) Resource Share. To association principals with the share, see the <cite>``ram.PrincipalAssociation`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/ram_principal_association.html">https://www.terraform.io/docs/providers/aws/r/ram_principal_association.html</a>&gt;`_. To associate resources with the share, see the <cite>``ram.ResourceAssociation`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/ram_resource_association.html">https://www.terraform.io/docs/providers/aws/r/ram_resource_association.html</a>&gt;`_.</p>
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
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_resource_share.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_resource_share.html.markdown</a>.</div></blockquote>
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

<dl class="staticmethod">
<dt id="pulumi_aws.ram.ResourceShare.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>allow_external_principals=None</em>, <em>arn=None</em>, <em>name=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResourceShare resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] allow_external_principals: Indicates whether principals outside your organization can be associated with a resource share.
:param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the resource share.
:param pulumi.Input[str] name: The name of the resource share.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource share.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_resource_share.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_resource_share.html.markdown</a>.</div></blockquote>
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

<dl class="function">
<dt id="pulumi_aws.ram.get_resource_share">
<code class="descclassname">pulumi_aws.ram.</code><code class="descname">get_resource_share</code><span class="sig-paren">(</span><em>filters=None</em>, <em>name=None</em>, <em>resource_owner=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.get_resource_share" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ram.ResourceShare</span></code> Retrieve information about a RAM Resource Share.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ram_resource_share.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ram_resource_share.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
