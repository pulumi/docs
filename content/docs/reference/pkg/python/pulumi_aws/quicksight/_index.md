---
---

<div class="section" id="quicksight">
<h1>quicksight<a class="headerlink" href="#quicksight" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.quicksight"></span><dl class="class">
<dt id="pulumi_aws.quicksight.Group">
<em class="property">class </em><code class="descclassname">pulumi_aws.quicksight.</code><code class="descname">Group</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>aws_account_id=None</em>, <em>description=None</em>, <em>group_name=None</em>, <em>namespace=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.quicksight.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource for managing Quick Sight Group</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>aws_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the group.</li>
<li><strong>group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name for the group.</li>
<li><strong>namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The namespace. Currently, you should set this to <code class="docutils literal notranslate"><span class="pre">default</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/quicksight_group.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/quicksight_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.quicksight.Group.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.Group.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.quicksight.Group.aws_account_id">
<code class="descname">aws_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.Group.aws_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID for the AWS account that the group is in. Currently, you use the ID for the AWS account that contains your Amazon QuickSight account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.quicksight.Group.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.Group.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.quicksight.Group.group_name">
<code class="descname">group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.Group.group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name for the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.quicksight.Group.namespace">
<code class="descname">namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.quicksight.Group.namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace. Currently, you should set this to <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.quicksight.Group.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.quicksight.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.quicksight.Group.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.quicksight.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
