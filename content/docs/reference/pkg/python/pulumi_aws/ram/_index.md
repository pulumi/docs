---
title: Module ram
title_tag: Module ram | Package pulumi_aws | Python SDK
linktitle: ram
notitle: true
---

<div class="section" id="ram">
<h1>ram<a class="headerlink" href="#ram" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.ram"></span><dl class="py class">
<dt id="pulumi_aws.ram.AwaitableGetResourceShareResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ram.</code><code class="sig-name descname">AwaitableGetResourceShareResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_owner</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.AwaitableGetResourceShareResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ram.GetResourceShareResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ram.</code><code class="sig-name descname">GetResourceShareResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_owner</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.GetResourceShareResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getResourceShare.</p>
<dl class="py attribute">
<dt id="pulumi_aws.ram.GetResourceShareResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.GetResourceShareResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the resource share.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ram.GetResourceShareResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.GetResourceShareResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the resource share.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ram.GetResourceShareResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.GetResourceShareResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The Status of the RAM share.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ram.GetResourceShareResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.GetResourceShareResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The Tags attached to the RAM share</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ram.PrincipalAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ram.</code><code class="sig-name descname">PrincipalAssociation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_share_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Resource Access Manager (RAM) principal association. Depending if <a class="reference external" href="https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs">RAM Sharing with AWS Organizations is enabled</a>, the RAM behavior with different principal types changes.</p>
<p>When RAM Sharing with AWS Organizations is enabled:</p>
<ul class="simple">
<li><p>For AWS Account ID, Organization, and Organizational Unit principals within the same AWS Organization, no resource share invitation is sent and resources become available automatically after creating the association.</p></li>
<li><p>For AWS Account ID principals outside the AWS Organization, a resource share invitation is sent and must be accepted before resources become available. See the <cite>``ram.ResourceShareAccepter`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/ram_resource_share_accepter.html">https://www.terraform.io/docs/providers/aws/r/ram_resource_share_accepter.html</a>&gt;`_ to accept these invitations.</p></li>
</ul>
<p>When RAM Sharing with AWS Organizations is not enabled:</p>
<ul class="simple">
<li><p>Organization and Organizational Unit principals cannot be used.</p></li>
<li><p>For AWS Account ID principals, a resource share invitation is sent and must be accepted before resources become available. See the <cite>``ram.ResourceShareAccepter`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/ram_resource_share_accepter.html">https://www.terraform.io/docs/providers/aws/r/ram_resource_share_accepter.html</a>&gt;`_ to accept these invitations.</p></li>
</ul>
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
<dl class="py attribute">
<dt id="pulumi_aws.ram.PrincipalAssociation.principal">
<code class="sig-name descname">principal</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation.principal" title="Permalink to this definition">¶</a></dt>
<dd><p>The principal to associate with the resource share. Possible values are an AWS account ID, an AWS Organizations Organization ARN, or an AWS Organizations Organization Unit ARN.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ram.PrincipalAssociation.resource_share_arn">
<code class="sig-name descname">resource_share_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation.resource_share_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the resource share.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ram.PrincipalAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_share_arn</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PrincipalAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The principal to associate with the resource share. Possible values are an AWS account ID, an AWS Organizations Organization ARN, or an AWS Organizations Organization Unit ARN.</p></li>
<li><p><strong>resource_share_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the resource share.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ram.PrincipalAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ram.PrincipalAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.PrincipalAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.ram.ResourceAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ram.</code><code class="sig-name descname">ResourceAssociation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_share_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation" title="Permalink to this definition">¶</a></dt>
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
<dl class="py attribute">
<dt id="pulumi_aws.ram.ResourceAssociation.resource_arn">
<code class="sig-name descname">resource_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation.resource_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the resource to associate with the RAM Resource Share.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ram.ResourceAssociation.resource_share_arn">
<code class="sig-name descname">resource_share_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation.resource_share_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the RAM Resource Share.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ram.ResourceAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_share_arn</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResourceAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>resource_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the resource to associate with the RAM Resource Share.</p></li>
<li><p><strong>resource_share_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the RAM Resource Share.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ram.ResourceAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ram.ResourceAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.ram.ResourceShare">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ram.</code><code class="sig-name descname">ResourceShare</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_external_principals</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceShare" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Resource Access Manager (RAM) Resource Share. To associate principals with the share, see the <cite>``ram.PrincipalAssociation`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/ram_principal_association.html">https://www.terraform.io/docs/providers/aws/r/ram_principal_association.html</a>&gt;`_. To associate resources with the share, see the <cite>``ram.ResourceAssociation`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/ram_resource_association.html">https://www.terraform.io/docs/providers/aws/r/ram_resource_association.html</a>&gt;`_.</p>
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
<dl class="py attribute">
<dt id="pulumi_aws.ram.ResourceShare.allow_external_principals">
<code class="sig-name descname">allow_external_principals</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.allow_external_principals" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether principals outside your organization can be associated with a resource share.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ram.ResourceShare.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the resource share.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ram.ResourceShare.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource share.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ram.ResourceShare.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource share.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ram.ResourceShare.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_external_principals</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResourceShare resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_external_principals</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether principals outside your organization can be associated with a resource share.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the resource share.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource share.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource share.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ram.ResourceShare.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ram.ResourceShare.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceShare.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.ram.ResourceShareAccepter">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ram.</code><code class="sig-name descname">ResourceShareAccepter</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">share_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceShareAccepter" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage accepting a Resource Access Manager (RAM) Resource Share invitation. From a <em>receiver</em> AWS account, accept an invitation to share resources that were shared by a <em>sender</em> AWS account. To create a resource share in the <em>sender</em>, see the <cite>``ram.ResourceShare`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/ram_resource_share.html">https://www.terraform.io/docs/providers/aws/r/ram_resource_share.html</a>&gt;`_.</p>
<blockquote>
<div><p><strong>Note:</strong> If both AWS accounts are in the same Organization and <a class="reference external" href="https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs">RAM Sharing with AWS Organizations is enabled</a>, this resource is not necessary as RAM Resource Share invitations are not used.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>share_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the resource share.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.ram.ResourceShareAccepter.invitation_arn">
<code class="sig-name descname">invitation_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShareAccepter.invitation_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the resource share invitation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ram.ResourceShareAccepter.receiver_account_id">
<code class="sig-name descname">receiver_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShareAccepter.receiver_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The account ID of the receiver account which accepts the invitation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ram.ResourceShareAccepter.resources">
<code class="sig-name descname">resources</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShareAccepter.resources" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the resource ARNs shared via the resource share.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ram.ResourceShareAccepter.sender_account_id">
<code class="sig-name descname">sender_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShareAccepter.sender_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The account ID of the sender account which submits the invitation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ram.ResourceShareAccepter.share_arn">
<code class="sig-name descname">share_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShareAccepter.share_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the resource share.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ram.ResourceShareAccepter.share_id">
<code class="sig-name descname">share_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShareAccepter.share_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the resource share as displayed in the console.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ram.ResourceShareAccepter.share_name">
<code class="sig-name descname">share_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShareAccepter.share_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource share.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ram.ResourceShareAccepter.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ram.ResourceShareAccepter.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the resource share (ACTIVE, PENDING, FAILED, DELETING, DELETED).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ram.ResourceShareAccepter.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">invitation_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">receiver_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sender_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">share_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">share_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">share_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceShareAccepter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResourceShareAccepter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>invitation_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the resource share invitation.</p></li>
<li><p><strong>receiver_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account ID of the receiver account which accepts the invitation.</p></li>
<li><p><strong>resources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the resource ARNs shared via the resource share.</p></li>
<li><p><strong>sender_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account ID of the sender account which submits the invitation.</p></li>
<li><p><strong>share_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the resource share.</p></li>
<li><p><strong>share_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resource share as displayed in the console.</p></li>
<li><p><strong>share_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource share.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the resource share (ACTIVE, PENDING, FAILED, DELETING, DELETED).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ram.ResourceShareAccepter.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceShareAccepter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ram.ResourceShareAccepter.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.ResourceShareAccepter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_aws.ram.get_resource_share">
<code class="sig-prename descclassname">pulumi_aws.ram.</code><code class="sig-name descname">get_resource_share</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_owner</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ram.get_resource_share" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ram.ResourceShare</span></code> Retrieve information about a RAM Resource Share.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filters</strong> (<em>list</em>) – A filter used to scope the list e.g. by tags. See [related docs] (<a class="reference external" href="https://docs.aws.amazon.com/ram/latest/APIReference/API_TagFilter.html">https://docs.aws.amazon.com/ram/latest/APIReference/API_TagFilter.html</a>).</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the tag key to filter on.</p></li>
<li><p><strong>resource_owner</strong> (<em>str</em>) – The owner of the resource share. Valid values are SELF or OTHER-ACCOUNTS</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – The Tags attached to the RAM share</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the tag key to filter on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The value of the tag key.</p></li>
</ul>
</dd></dl>

</div>
