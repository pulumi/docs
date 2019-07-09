---
---

<div class="section" id="managementgroups">
<h1>managementgroups<a class="headerlink" href="#managementgroups" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azure">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azure/issues">terraform-providers/terraform-provider-azure repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_azure.managementgroups"></span><dl class="class">
<dt id="pulumi_azure.managementgroups.GetManagementGroupResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.managementgroups.</code><code class="descname">GetManagementGroupResult</code><span class="sig-paren">(</span><em>display_name=None</em>, <em>group_id=None</em>, <em>parent_management_group_id=None</em>, <em>subscription_ids=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managementgroups.GetManagementGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getManagementGroup.</p>
<dl class="attribute">
<dt id="pulumi_azure.managementgroups.GetManagementGroupResult.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementgroups.GetManagementGroupResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name for the Management Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managementgroups.GetManagementGroupResult.parent_management_group_id">
<code class="descname">parent_management_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementgroups.GetManagementGroupResult.parent_management_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of any Parent Management Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managementgroups.GetManagementGroupResult.subscription_ids">
<code class="descname">subscription_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementgroups.GetManagementGroupResult.subscription_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Subscription ID’s which are assigned to the Management Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managementgroups.GetManagementGroupResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementgroups.GetManagementGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.managementgroups.ManagementGroup">
<em class="property">class </em><code class="descclassname">pulumi_azure.managementgroups.</code><code class="descname">ManagementGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>display_name=None</em>, <em>group_id=None</em>, <em>parent_management_group_id=None</em>, <em>subscription_ids=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managementgroups.ManagementGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Management Group.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for this Management Group. If not specified, this’ll be the same as the <code class="docutils literal notranslate"><span class="pre">group_id</span></code>.</li>
<li><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID for this Management Group, which needs to be unique across your tenant - which will be generated if not provided. Changing this forces a new resource to be created.</li>
<li><strong>parent_management_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Parent Management Group. Changing this forces a new resource to be created.</li>
<li><strong>subscription_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Subscription GUIDs which should be assigned to the Management Group.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/management_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/management_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.managementgroups.ManagementGroup.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementgroups.ManagementGroup.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name for this Management Group. If not specified, this’ll be the same as the <code class="docutils literal notranslate"><span class="pre">group_id</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managementgroups.ManagementGroup.group_id">
<code class="descname">group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementgroups.ManagementGroup.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID for this Management Group, which needs to be unique across your tenant - which will be generated if not provided. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managementgroups.ManagementGroup.parent_management_group_id">
<code class="descname">parent_management_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementgroups.ManagementGroup.parent_management_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Parent Management Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managementgroups.ManagementGroup.subscription_ids">
<code class="descname">subscription_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementgroups.ManagementGroup.subscription_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Subscription GUIDs which should be assigned to the Management Group.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.managementgroups.ManagementGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managementgroups.ManagementGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.managementgroups.ManagementGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managementgroups.ManagementGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.managementgroups.get_management_group">
<code class="descclassname">pulumi_azure.managementgroups.</code><code class="descname">get_management_group</code><span class="sig-paren">(</span><em>group_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managementgroups.get_management_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Management Group.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/management_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/management_group.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
