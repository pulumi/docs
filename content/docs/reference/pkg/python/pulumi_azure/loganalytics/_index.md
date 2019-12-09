---
title: Module loganalytics
title_tag: Module loganalytics | Package pulumi_azure | Python SDK
linktitle: loganalytics
notitle: true
---

<div class="section" id="loganalytics">
<h1>loganalytics<a class="headerlink" href="#loganalytics" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.loganalytics"></span><dl class="class">
<dt id="pulumi_azure.loganalytics.LinkedService">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.loganalytics.</code><code class="sig-name descname">LinkedService</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">linked_service_name=None</em>, <em class="sig-param">linked_service_properties=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">workspace_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService" title="Permalink to this definition">¶</a></dt>
<dd><p>Links a Log Analytics (formally Operational Insights) Workspace to another resource. The (currently) only linkable service is an Azure Automation Account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>linked_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the type of linkedServices resource to connect to the Log Analytics Workspace specified in <code class="docutils literal notranslate"><span class="pre">workspace_name</span></code>. Currently it defaults to and only supports <code class="docutils literal notranslate"><span class="pre">automation</span></code> as a value. Changing this forces a new resource to be created.</p></li>
<li><p><strong>linked_service_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">linked_service_properties</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Log Analytics Linked Service is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource id of the resource that will be linked to the workspace. This field has been deprecated in favour of the top-level <code class="docutils literal notranslate"><span class="pre">resource_id</span></code> field and will be removed in v2.0 of the AzureRM Provider.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>workspace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Log Analytics Workspace that will contain the linkedServices resource. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>linked_service_properties</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource id of the resource that will be linked to the workspace. This field has been deprecated in favour of the top-level <code class="docutils literal notranslate"><span class="pre">resource_id</span></code> field and will be removed in v2.0 of the AzureRM Provider.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/log_analytics_linked_service.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/log_analytics_linked_service.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.loganalytics.LinkedService.linked_service_name">
<code class="sig-name descname">linked_service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.linked_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the type of linkedServices resource to connect to the Log Analytics Workspace specified in <code class="docutils literal notranslate"><span class="pre">workspace_name</span></code>. Currently it defaults to and only supports <code class="docutils literal notranslate"><span class="pre">automation</span></code> as a value. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.loganalytics.LinkedService.linked_service_properties">
<code class="sig-name descname">linked_service_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.linked_service_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">linked_service_properties</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The resource id of the resource that will be linked to the workspace. This field has been deprecated in favour of the top-level <code class="docutils literal notranslate"><span class="pre">resource_id</span></code> field and will be removed in v2.0 of the AzureRM Provider.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.loganalytics.LinkedService.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The automatically generated name of the Linked Service. This cannot be specified. The format is always <code class="docutils literal notranslate"><span class="pre">&lt;workspace_name&gt;/&lt;linked_service_name&gt;</span></code> e.g. <code class="docutils literal notranslate"><span class="pre">workspace1/Automation</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.loganalytics.LinkedService.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Log Analytics Linked Service is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.loganalytics.LinkedService.resource_id">
<code class="sig-name descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource id of the resource that will be linked to the workspace. This field has been deprecated in favour of the top-level <code class="docutils literal notranslate"><span class="pre">resource_id</span></code> field and will be removed in v2.0 of the AzureRM Provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.loganalytics.LinkedService.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.loganalytics.LinkedService.workspace_name">
<code class="sig-name descname">workspace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.workspace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Log Analytics Workspace that will contain the linkedServices resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.loganalytics.LinkedService.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">linked_service_name=None</em>, <em class="sig-param">linked_service_properties=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">workspace_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LinkedService resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>linked_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the type of linkedServices resource to connect to the Log Analytics Workspace specified in <code class="docutils literal notranslate"><span class="pre">workspace_name</span></code>. Currently it defaults to and only supports <code class="docutils literal notranslate"><span class="pre">automation</span></code> as a value. Changing this forces a new resource to be created.</p></li>
<li><p><strong>linked_service_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">linked_service_properties</span></code> block as defined below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The automatically generated name of the Linked Service. This cannot be specified. The format is always <code class="docutils literal notranslate"><span class="pre">&lt;workspace_name&gt;/&lt;linked_service_name&gt;</span></code> e.g. <code class="docutils literal notranslate"><span class="pre">workspace1/Automation</span></code></p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Log Analytics Linked Service is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource id of the resource that will be linked to the workspace. This field has been deprecated in favour of the top-level <code class="docutils literal notranslate"><span class="pre">resource_id</span></code> field and will be removed in v2.0 of the AzureRM Provider.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>workspace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Log Analytics Workspace that will contain the linkedServices resource. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>linked_service_properties</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource id of the resource that will be linked to the workspace. This field has been deprecated in favour of the top-level <code class="docutils literal notranslate"><span class="pre">resource_id</span></code> field and will be removed in v2.0 of the AzureRM Provider.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/log_analytics_linked_service.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/log_analytics_linked_service.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.loganalytics.LinkedService.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.loganalytics.LinkedService.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
