---
title: Module databasemigration
title_tag: Module databasemigration | Package pulumi_azure | Python SDK
linktitle: databasemigration
notitle: true
---

<div class="section" id="databasemigration">
<h1>databasemigration<a class="headerlink" href="#databasemigration" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.databasemigration"></span><dl class="class">
<dt id="pulumi_azure.databasemigration.AwaitableGetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.databasemigration.</code><code class="sig-name descname">AwaitableGetProjectResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">source_platform=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_platform=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databasemigration.AwaitableGetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.databasemigration.AwaitableGetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.databasemigration.</code><code class="sig-name descname">AwaitableGetServiceResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databasemigration.AwaitableGetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.databasemigration.GetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.databasemigration.</code><code class="sig-name descname">GetProjectResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">source_platform=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_platform=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databasemigration.GetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProject.</p>
<dl class="attribute">
<dt id="pulumi_azure.databasemigration.GetProjectResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.GetProjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.GetProjectResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.GetProjectResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Azure location where the resource exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.GetProjectResult.source_platform">
<code class="sig-name descname">source_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.GetProjectResult.source_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The platform type of the migration source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.GetProjectResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.GetProjectResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.GetProjectResult.target_platform">
<code class="sig-name descname">target_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.GetProjectResult.target_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The platform type of the migration target.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.databasemigration.GetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.databasemigration.</code><code class="sig-name descname">GetServiceResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databasemigration.GetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getService.</p>
<dl class="attribute">
<dt id="pulumi_azure.databasemigration.GetServiceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.GetServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.GetServiceResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.GetServiceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Azure location where the resource exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.GetServiceResult.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.GetServiceResult.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The sku name of database migration service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.GetServiceResult.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.GetServiceResult.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the virtual subnet resource to which the database migration service exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.GetServiceResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.GetServiceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assigned to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.databasemigration.Project">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.databasemigration.</code><code class="sig-name descname">Project</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">source_platform=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_platform=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databasemigration.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Project resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] name: Specify the name of the database migration project. Changing this forces a new resource to be created.
:param pulumi.Input[str] resource_group_name: Name of the resource group in which to create the database migration project. Changing this forces a new resource to be created.
:param pulumi.Input[str] service_name: Name of the database migration service where resource belongs to. Changing this forces a new resource to be created.
:param pulumi.Input[str] source_platform: The platform type of the migration source. Currently only support: <code class="docutils literal notranslate"><span class="pre">SQL</span></code>(on-premises SQL Server). Changing this forces a new resource to be created.
:param pulumi.Input[dict] tags: A mapping of tags to assigned to the resource.
:param pulumi.Input[str] target_platform: The platform type of the migration target. Currently only support: <code class="docutils literal notranslate"><span class="pre">SQLDB</span></code>(Azure SQL Database). Changing this forces a new resource to be created.</p>
<dl class="attribute">
<dt id="pulumi_azure.databasemigration.Project.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.Project.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.Project.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the name of the database migration project. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.Project.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.Project.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the resource group in which to create the database migration project. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.Project.service_name">
<code class="sig-name descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.Project.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the database migration service where resource belongs to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.Project.source_platform">
<code class="sig-name descname">source_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.Project.source_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The platform type of the migration source. Currently only support: <code class="docutils literal notranslate"><span class="pre">SQL</span></code>(on-premises SQL Server). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.Project.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.Project.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.Project.target_platform">
<code class="sig-name descname">target_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.Project.target_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The platform type of the migration target. Currently only support: <code class="docutils literal notranslate"><span class="pre">SQLDB</span></code>(Azure SQL Database). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.databasemigration.Project.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">source_platform=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_platform=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databasemigration.Project.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Project resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the name of the database migration project. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the resource group in which to create the database migration project. Changing this forces a new resource to be created.</p></li>
<li><p><strong>service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the database migration service where resource belongs to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The platform type of the migration source. Currently only support: <code class="docutils literal notranslate"><span class="pre">SQL</span></code>(on-premises SQL Server). Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assigned to the resource.</p></li>
<li><p><strong>target_platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The platform type of the migration target. Currently only support: <code class="docutils literal notranslate"><span class="pre">SQLDB</span></code>(Azure SQL Database). Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.databasemigration.Project.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databasemigration.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.databasemigration.Project.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databasemigration.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.databasemigration.Service">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.databasemigration.</code><code class="sig-name descname">Service</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databasemigration.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Service resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] name: Specify the name of the database migration service. Changing this forces a new resource to be created.
:param pulumi.Input[str] resource_group_name: Name of the resource group in which to create the database migration service. Changing this forces a new resource to be created.
:param pulumi.Input[str] sku_name: The sku name of the database migration service. Possible values are <code class="docutils literal notranslate"><span class="pre">Premium_4vCores</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_1vCores</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_2vCores</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard_4vCores</span></code>. Changing this forces a new resource to be created.
:param pulumi.Input[str] subnet_id: The ID of the virtual subnet resource to which the database migration service should be joined. Changing this forces a new resource to be created.
:param pulumi.Input[dict] tags: A mapping of tags to assigned to the resource.</p>
<dl class="attribute">
<dt id="pulumi_azure.databasemigration.Service.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.Service.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.Service.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.Service.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the name of the database migration service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.Service.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.Service.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the resource group in which to create the database migration service. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.Service.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.Service.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The sku name of the database migration service. Possible values are <code class="docutils literal notranslate"><span class="pre">Premium_4vCores</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_1vCores</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_2vCores</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard_4vCores</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.Service.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.Service.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the virtual subnet resource to which the database migration service should be joined. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.databasemigration.Service.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.databasemigration.Service.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assigned to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.databasemigration.Service.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databasemigration.Service.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Service resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the name of the database migration service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the resource group in which to create the database migration service. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The sku name of the database migration service. Possible values are <code class="docutils literal notranslate"><span class="pre">Premium_4vCores</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_1vCores</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_2vCores</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard_4vCores</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the virtual subnet resource to which the database migration service should be joined. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assigned to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.databasemigration.Service.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databasemigration.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.databasemigration.Service.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databasemigration.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.databasemigration.get_project">
<code class="sig-prename descclassname">pulumi_azure.databasemigration.</code><code class="sig-name descname">get_project</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databasemigration.get_project" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Database Migration Project.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/database_migration_project.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/database_migration_project.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Name of the database migration project.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Name of the resource group where resource belongs to.</p></li>
<li><p><strong>service_name</strong> (<em>str</em>) – Name of the database migration service where resource belongs to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.databasemigration.get_service">
<code class="sig-prename descclassname">pulumi_azure.databasemigration.</code><code class="sig-name descname">get_service</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.databasemigration.get_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Database Migration Service.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/database_migration_service.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/database_migration_service.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specify the name of the database migration service.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the Name of the Resource Group within which the database migration service exists</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
