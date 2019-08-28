---
title: Module ram
---

<div class="section" id="ram">
<h1>ram<a class="headerlink" href="#ram" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.ram"></span><dl class="class">
<dt id="pulumi_aws.ram.AwaitableGetResourceShareResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ram.</code><code class="sig-name descname">AwaitableGetResourceShareResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">filters=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_owner=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.AwaitableGetResourceShareResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.ram.GetResourceShareResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ram.</code><code class="sig-name descname">GetResourceShareResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">filters=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_owner=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.GetResourceShareResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getResourceShare.</p>
<dl class="attribute">
<dt id="pulumi_aws.ram.GetResourceShareResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.GetResourceShareResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the resource share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ram.GetResourceShareResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.GetResourceShareResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the resource share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ram.GetResourceShareResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.GetResourceShareResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The Status of the RAM share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ram.GetResourceShareResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.GetResourceShareResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The Tags attached to the RAM share</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ram.PrincipalAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ram.</code><code class="sig-name descname">PrincipalAssociation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">principal=None</em>, <em class="sig-param">resource_share_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Resource Access Manager (RAM) principal association.</p>
<blockquote>
<div><p><em>NOTE:</em> For an AWS Account ID principal, the target account must accept the RAM association invitation after resource creation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The principal to associate with the resource share. Possible values are an AWS account ID, an AWS Organizations Organization ARN, or an AWS Organizations Organization Unit ARN.</p></li>
<li><p><strong>resource_share_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the resource share.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_principal_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_principal_association.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ram.PrincipalAssociation.principal">
<code class="sig-name descname">principal</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation.principal" title="Permalink to this definition">¶</a></dt>
<dd><p>The principal to associate with the resource share. Possible values are an AWS account ID, an AWS Organizations Organization ARN, or an AWS Organizations Organization Unit ARN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ram.PrincipalAssociation.resource_share_arn">
<code class="sig-name descname">resource_share_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation.resource_share_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the resource share.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ram.PrincipalAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">principal=None</em>, <em class="sig-param">resource_share_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PrincipalAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] principal: The principal to associate with the resource share. Possible values are an AWS account ID, an AWS Organizations Organization ARN, or an AWS Organizations Organization Unit ARN.
:param pulumi.Input[str] resource_share_arn: The Amazon Resource Name (ARN) of the resource share.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_principal_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_principal_association.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ram.PrincipalAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ram.PrincipalAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ram.ResourceAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ram.</code><code class="sig-name descname">ResourceAssociation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">resource_arn=None</em>, <em class="sig-param">resource_share_arn=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Resource Access Manager (RAM) Resource Association.</p>
<blockquote>
<div><p><em>NOTE:</em> Certain AWS resources (e.g. EC2 Subnets) can only be shared in an AWS account that is a member of an AWS Organizations organization with organization-wide Resource Access Manager functionality enabled. See the <a class="reference external" href="https://docs.aws.amazon.com/ram/latest/userguide/what-is.html">Resource Access Manager User Guide</a> and AWS service specific documentation for additional information.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>resource_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the resource to associate with the RAM Resource Share.</p></li>
<li><p><strong>resource_share_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the RAM Resource Share.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_resource_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_resource_association.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ram.ResourceAssociation.resource_arn">
<code class="sig-name descname">resource_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation.resource_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the resource to associate with the RAM Resource Share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ram.ResourceAssociation.resource_share_arn">
<code class="sig-name descname">resource_share_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation.resource_share_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the RAM Resource Share.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ram.ResourceAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">resource_arn=None</em>, <em class="sig-param">resource_share_arn=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResourceAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] resource_arn: Amazon Resource Name (ARN) of the resource to associate with the RAM Resource Share.
:param pulumi.Input[str] resource_share_arn: Amazon Resource Name (ARN) of the RAM Resource Share.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_resource_association.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_resource_association.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ram.ResourceAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ram.ResourceAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ram.ResourceShare">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ram.</code><code class="sig-name descname">ResourceShare</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_external_principals=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceShare" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Resource Access Manager (RAM) Resource Share. To association principals with the share, see the <cite>``ram.PrincipalAssociation`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/ram_principal_association.html">https://www.terraform.io/docs/providers/aws/r/ram_principal_association.html</a>&gt;`_. To associate resources with the share, see the <cite>``ram.ResourceAssociation`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/ram_resource_association.html">https://www.terraform.io/docs/providers/aws/r/ram_resource_association.html</a>&gt;`_.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_external_principals</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether principals outside your organization can be associated with a resource share.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource share.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource share.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_resource_share.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_resource_share.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.ram.ResourceShare.allow_external_principals">
<code class="sig-name descname">allow_external_principals</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.allow_external_principals" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether principals outside your organization can be associated with a resource share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ram.ResourceShare.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the resource share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ram.ResourceShare.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource share.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ram.ResourceShare.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource share.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ram.ResourceShare.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_external_principals=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.get" title="Permalink to this definition">¶</a></dt>
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
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_resource_share.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ram_resource_share.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ram.ResourceShare.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ram.ResourceShare.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ram.get_resource_share">
<code class="sig-prename descclassname">pulumi_aws.ram.</code><code class="sig-name descname">get_resource_share</code><span class="sig-paren">(</span><em class="sig-param">filters=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_owner=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.get_resource_share" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ram.ResourceShare</span></code> Retrieve information about a RAM Resource Share.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ram_resource_share.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ram_resource_share.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
