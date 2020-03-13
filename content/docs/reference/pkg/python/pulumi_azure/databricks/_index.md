---
title: Module databricks
title_tag: Module databricks | Package pulumi_azure | Python SDK
linktitle: databricks
notitle: true
---

<div class="section" id="databricks">
<h1>databricks<a class="headerlink" href="#databricks" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.databricks"></span><dl class="class">
<dt id="pulumi_azure.databricks.Workspace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.databricks.</code><code class="sig-name descname">Workspace</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">custom_parameters=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">managed_resource_group_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databricks.Workspace" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Databricks Workspace</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/databricks_workspace.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/databricks_workspace.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">custom_parameters</span></code> block as documented below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource has to be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>managed_resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group where Azure should place the managed Databricks resources. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Databricks Workspace resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Databricks Workspace should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">sku</span></code> to use for the Databricks Workspace. Possible values are <code class="docutils literal notranslate"><span class="pre">standard</span></code>, <code class="docutils literal notranslate"><span class="pre">premium</span></code>, or <code class="docutils literal notranslate"><span class="pre">trial</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">noPublicIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Are public IP Addresses not allowed?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateSubnetName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Private Subnet within the Virtual Network. Required if <code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> is set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicSubnetName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Public Subnet within the Virtual Network. Required if <code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> is set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of a Virtual Network where this Databricks Cluster should be created.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.databricks.Workspace.custom_parameters">
<code class="sig-name descname">custom_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databricks.Workspace.custom_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">custom_parameters</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">noPublicIp</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Are public IP Addresses not allowed?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateSubnetName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Private Subnet within the Virtual Network. Required if <code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> is set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicSubnetName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Public Subnet within the Virtual Network. Required if <code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> is set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of a Virtual Network where this Databricks Cluster should be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databricks.Workspace.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databricks.Workspace.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource has to be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databricks.Workspace.managed_resource_group_id">
<code class="sig-name descname">managed_resource_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databricks.Workspace.managed_resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Managed Resource Group created by the Databricks Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databricks.Workspace.managed_resource_group_name">
<code class="sig-name descname">managed_resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databricks.Workspace.managed_resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group where Azure should place the managed Databricks resources. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databricks.Workspace.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databricks.Workspace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Databricks Workspace resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databricks.Workspace.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databricks.Workspace.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Databricks Workspace should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databricks.Workspace.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databricks.Workspace.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">sku</span></code> to use for the Databricks Workspace. Possible values are <code class="docutils literal notranslate"><span class="pre">standard</span></code>, <code class="docutils literal notranslate"><span class="pre">premium</span></code>, or <code class="docutils literal notranslate"><span class="pre">trial</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databricks.Workspace.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databricks.Workspace.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.databricks.Workspace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">custom_parameters=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">managed_resource_group_id=None</em>, <em class="sig-param">managed_resource_group_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databricks.Workspace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Workspace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">custom_parameters</span></code> block as documented below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource has to be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>managed_resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Managed Resource Group created by the Databricks Workspace.</p></li>
<li><p><strong>managed_resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group where Azure should place the managed Databricks resources. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Databricks Workspace resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Databricks Workspace should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">sku</span></code> to use for the Databricks Workspace. Possible values are <code class="docutils literal notranslate"><span class="pre">standard</span></code>, <code class="docutils literal notranslate"><span class="pre">premium</span></code>, or <code class="docutils literal notranslate"><span class="pre">trial</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">noPublicIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Are public IP Addresses not allowed?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateSubnetName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Private Subnet within the Virtual Network. Required if <code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> is set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicSubnetName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Public Subnet within the Virtual Network. Required if <code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> is set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_network_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of a Virtual Network where this Databricks Cluster should be created.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.databricks.Workspace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databricks.Workspace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.databricks.Workspace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databricks.Workspace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
