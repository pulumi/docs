---
title: Module machinelearning
title_tag: Module machinelearning | Package pulumi_azure | Python SDK
linktitle: machinelearning
notitle: true
---

<div class="section" id="machinelearning">
<h1>machinelearning<a class="headerlink" href="#machinelearning" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.machinelearning"></span><dl class="class">
<dt id="pulumi_azure.machinelearning.AwaitableGetWorkspaceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.machinelearning.</code><code class="sig-name descname">AwaitableGetWorkspaceResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.machinelearning.AwaitableGetWorkspaceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.machinelearning.GetWorkspaceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.machinelearning.</code><code class="sig-name descname">GetWorkspaceResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.machinelearning.GetWorkspaceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getWorkspace.</p>
<dl class="attribute">
<dt id="pulumi_azure.machinelearning.GetWorkspaceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.machinelearning.GetWorkspaceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.machinelearning.GetWorkspaceResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.machinelearning.GetWorkspaceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the Machine Learning Workspace exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.machinelearning.GetWorkspaceResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.machinelearning.GetWorkspaceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the Machine Learning Workspace.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.machinelearning.Workspace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.machinelearning.</code><code class="sig-name descname">Workspace</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_insights_id=None</em>, <em class="sig-param">container_registry_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">friendly_name=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">key_vault_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.machinelearning.Workspace" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Azure Machine Learning Workspace</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_insights_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Application Insights associated with this Machine Learning Workspace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>container_registry_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the container registry associated with this Machine Learning Workspace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this Machine Learning Workspace.</p></li>
<li><p><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name for this Machine Learning Workspace.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block defined below.</p></li>
<li><p><strong>key_vault_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of key vault associated with this Machine Learning Workspace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the Machine Learning Workspace should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Machine Learning Workspace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which the Machine Learning Workspace should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SKU/edition of the Machine Learning Workspace, possible values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> for a basic workspace or <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code> for a feature rich workspace. Defaults to <code class="docutils literal notranslate"><span class="pre">Basic</span></code>.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Storage Account associated with this Machine Learning Workspace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The (Client) ID of the Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Tenant the Service Principal is assigned in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Identity which should be used for this Disk Encryption Set. At this time the only possible value is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.machinelearning.Workspace.application_insights_id">
<code class="sig-name descname">application_insights_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.machinelearning.Workspace.application_insights_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Application Insights associated with this Machine Learning Workspace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.machinelearning.Workspace.container_registry_id">
<code class="sig-name descname">container_registry_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.machinelearning.Workspace.container_registry_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the container registry associated with this Machine Learning Workspace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.machinelearning.Workspace.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.machinelearning.Workspace.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this Machine Learning Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.machinelearning.Workspace.friendly_name">
<code class="sig-name descname">friendly_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.machinelearning.Workspace.friendly_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Friendly name for this Machine Learning Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.machinelearning.Workspace.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.machinelearning.Workspace.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The (Client) ID of the Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Tenant the Service Principal is assigned in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of Identity which should be used for this Disk Encryption Set. At this time the only possible value is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.machinelearning.Workspace.key_vault_id">
<code class="sig-name descname">key_vault_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.machinelearning.Workspace.key_vault_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of key vault associated with this Machine Learning Workspace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.machinelearning.Workspace.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.machinelearning.Workspace.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the Machine Learning Workspace should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.machinelearning.Workspace.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.machinelearning.Workspace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Machine Learning Workspace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.machinelearning.Workspace.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.machinelearning.Workspace.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which the Machine Learning Workspace should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.machinelearning.Workspace.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.machinelearning.Workspace.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>SKU/edition of the Machine Learning Workspace, possible values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> for a basic workspace or <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code> for a feature rich workspace. Defaults to <code class="docutils literal notranslate"><span class="pre">Basic</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.machinelearning.Workspace.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.machinelearning.Workspace.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Storage Account associated with this Machine Learning Workspace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.machinelearning.Workspace.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.machinelearning.Workspace.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.machinelearning.Workspace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_insights_id=None</em>, <em class="sig-param">container_registry_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">friendly_name=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">key_vault_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.machinelearning.Workspace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Workspace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_insights_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Application Insights associated with this Machine Learning Workspace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>container_registry_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the container registry associated with this Machine Learning Workspace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this Machine Learning Workspace.</p></li>
<li><p><strong>friendly_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Friendly name for this Machine Learning Workspace.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block defined below.</p></li>
<li><p><strong>key_vault_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of key vault associated with this Machine Learning Workspace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the Machine Learning Workspace should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Machine Learning Workspace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which the Machine Learning Workspace should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SKU/edition of the Machine Learning Workspace, possible values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> for a basic workspace or <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code> for a feature rich workspace. Defaults to <code class="docutils literal notranslate"><span class="pre">Basic</span></code>.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Storage Account associated with this Machine Learning Workspace. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The (Client) ID of the Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Tenant the Service Principal is assigned in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Identity which should be used for this Disk Encryption Set. At this time the only possible value is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.machinelearning.Workspace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.machinelearning.Workspace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.machinelearning.Workspace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.machinelearning.Workspace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.machinelearning.get_workspace">
<code class="sig-prename descclassname">pulumi_azure.machinelearning.</code><code class="sig-name descname">get_workspace</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.machinelearning.get_workspace" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Machine Learning Workspace.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Machine Learning Workspace exists.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group where the Machine Learning Workspace exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
