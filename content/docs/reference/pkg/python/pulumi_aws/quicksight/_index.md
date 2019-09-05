---
title: Module quicksight
linktitle: quicksight
notitle: true
---

<div class="section" id="quicksight">
<h1>quicksight<a class="headerlink" href="#quicksight" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.quicksight"></span><dl class="class">
<dt id="pulumi_aws.quicksight.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.quicksight.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">aws_account_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">group_name=None</em>, <em class="sig-param">namespace=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.quicksight.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource for managing Quick Sight Group</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the group.</p></li>
<li><p><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the group.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace. Currently, you should set this to <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/quicksight_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/quicksight_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.quicksight.Group.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.Group.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.quicksight.Group.aws_account_id">
<code class="sig-name descname">aws_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.Group.aws_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.quicksight.Group.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.Group.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.quicksight.Group.group_name">
<code class="sig-name descname">group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.Group.group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.quicksight.Group.namespace">
<code class="sig-name descname">namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.Group.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace. Currently, you should set this to <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.quicksight.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">aws_account_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">group_name=None</em>, <em class="sig-param">namespace=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.quicksight.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of group</p></li>
<li><p><strong>aws_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the group.</p></li>
<li><p><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the group.</p></li>
<li><p><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace. Currently, you should set this to <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/quicksight_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/quicksight_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.quicksight.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.quicksight.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.quicksight.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.quicksight.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
