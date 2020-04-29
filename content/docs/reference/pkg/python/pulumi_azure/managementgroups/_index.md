---
title: Module managementgroups
title_tag: Module managementgroups | Package pulumi_azure | Python SDK
linktitle: managementgroups
notitle: true
---

<div class="section" id="managementgroups">
<h1>managementgroups<a class="headerlink" href="#managementgroups" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.managementgroups"></span><dl class="class">
<dt id="pulumi_azure.managementgroups.AwaitableGetManagementGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.managementgroups.</code><code class="sig-name descname">AwaitableGetManagementGroupResult</code><span class="sig-paren">(</span><em class="sig-param">display_name=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent_management_group_id=None</em>, <em class="sig-param">subscription_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managementgroups.AwaitableGetManagementGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.managementgroups.GetManagementGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.managementgroups.</code><code class="sig-name descname">GetManagementGroupResult</code><span class="sig-paren">(</span><em class="sig-param">display_name=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent_management_group_id=None</em>, <em class="sig-param">subscription_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managementgroups.GetManagementGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getManagementGroup.</p>
<dl class="attribute">
<dt id="pulumi_azure.managementgroups.GetManagementGroupResult.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementgroups.GetManagementGroupResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name for the Management Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managementgroups.GetManagementGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementgroups.GetManagementGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managementgroups.GetManagementGroupResult.parent_management_group_id">
<code class="sig-name descname">parent_management_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementgroups.GetManagementGroupResult.parent_management_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of any Parent Management Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managementgroups.GetManagementGroupResult.subscription_ids">
<code class="sig-name descname">subscription_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementgroups.GetManagementGroupResult.subscription_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Subscription ID’s which are assigned to the Management Group.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.managementgroups.ManagementGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.managementgroups.</code><code class="sig-name descname">ManagementGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent_management_group_id=None</em>, <em class="sig-param">subscription_ids=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managementgroups.ManagementGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Management Group.</p>
<p>Deprecated: azure.ManagementGroup has been deprecated in favour of azure.Group</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for this Management Group. If not specified, this’ll be the same as the <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or UUID for this Management Group, which needs to be unique across your tenant. A new UUID will be generated if not provided. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or UUID for this Management Group, which needs to be unique across your tenant. A new UUID will be generated if not provided. Changing this forces a new resource to be created.</p></li>
<li><p><strong>parent_management_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Parent Management Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subscription_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Subscription GUIDs which should be assigned to the Management Group.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.managementgroups.ManagementGroup.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementgroups.ManagementGroup.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name for this Management Group. If not specified, this’ll be the same as the <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managementgroups.ManagementGroup.group_id">
<code class="sig-name descname">group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementgroups.ManagementGroup.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or UUID for this Management Group, which needs to be unique across your tenant. A new UUID will be generated if not provided. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managementgroups.ManagementGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementgroups.ManagementGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or UUID for this Management Group, which needs to be unique across your tenant. A new UUID will be generated if not provided. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managementgroups.ManagementGroup.parent_management_group_id">
<code class="sig-name descname">parent_management_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementgroups.ManagementGroup.parent_management_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Parent Management Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.managementgroups.ManagementGroup.subscription_ids">
<code class="sig-name descname">subscription_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.managementgroups.ManagementGroup.subscription_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Subscription GUIDs which should be assigned to the Management Group.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.managementgroups.ManagementGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent_management_group_id=None</em>, <em class="sig-param">subscription_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managementgroups.ManagementGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ManagementGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for this Management Group. If not specified, this’ll be the same as the <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or UUID for this Management Group, which needs to be unique across your tenant. A new UUID will be generated if not provided. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or UUID for this Management Group, which needs to be unique across your tenant. A new UUID will be generated if not provided. Changing this forces a new resource to be created.</p></li>
<li><p><strong>parent_management_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Parent Management Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subscription_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Subscription GUIDs which should be assigned to the Management Group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.managementgroups.ManagementGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managementgroups.ManagementGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.managementgroups.ManagementGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managementgroups.ManagementGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.managementgroups.get_management_group">
<code class="sig-prename descclassname">pulumi_azure.managementgroups.</code><code class="sig-name descname">get_management_group</code><span class="sig-paren">(</span><em class="sig-param">group_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.managementgroups.get_management_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Management Group.</p>
<p>Deprecated: azure.getManagementGroup has been deprecated in favour of azure.getGroup</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>group_id</strong> (<em>str</em>) – Specifies the name or UUID of this Management Group.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name or UUID of this Management Group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
