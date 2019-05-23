---
---

<div class="section" id="module-pulumi_azure.operationalinsights">
<span id="operationalinsights"></span><h1>operationalinsights<a class="headerlink" href="#module-pulumi_azure.operationalinsights" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution">
<em class="property">class </em><code class="descclassname">pulumi_azure.operationalinsights.</code><code class="descname">AnalyticsSolution</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>plan=None</em>, <em>resource_group_name=None</em>, <em>solution_name=None</em>, <em>workspace_name=None</em>, <em>workspace_resource_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Log Analytics (formally Operational Insights) Solution.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">plan</span></code> block as documented below.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and it’s related workspace can only exist in the same resource group.</li>
<li><strong>solution_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the solution to be deployed. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-add-solutions">here for options</a>.Changing this forces a new resource to be created.</li>
<li><strong>workspace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full name of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.</li>
<li><strong>workspace_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution.plan">
<code class="descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">plan</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and it’s related workspace can only exist in the same resource group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution.solution_name">
<code class="descname">solution_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution.solution_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the solution to be deployed. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-add-solutions">here for options</a>.Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution.workspace_name">
<code class="descname">workspace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution.workspace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The full name of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution.workspace_resource_id">
<code class="descname">workspace_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution.workspace_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace">
<em class="property">class </em><code class="descclassname">pulumi_azure.operationalinsights.</code><code class="descname">AnalyticsWorkspace</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>retention_in_days=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Log Analytics (formally Operational Insights) Workspace.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Log Analytics Workspace. Workspace name should include 4-63 letters, digits or ‘-‘. The ‘-‘ shouldn’t be the first or the last symbol. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Log Analytics workspace is created. Changing this forces a new resource to be created.</li>
<li><strong>retention_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The workspace data retention in days. Possible values range between 30 and 730.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Sku of the Log Analytics Workspace. Possible values are <code class="docutils literal notranslate"><span class="pre">Free</span></code>, <code class="docutils literal notranslate"><span class="pre">PerNode</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">Standalone</span></code>, <code class="docutils literal notranslate"><span class="pre">Unlimited</span></code>, and <code class="docutils literal notranslate"><span class="pre">PerGB2018</span></code> (new Sku as of <code class="docutils literal notranslate"><span class="pre">2018-04-03</span></code>).</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Log Analytics Workspace. Workspace name should include 4-63 letters, digits or ‘-‘. The ‘-‘ shouldn’t be the first or the last symbol. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.portal_url">
<code class="descname">portal_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.portal_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The Portal URL for the Log Analytics Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.primary_shared_key">
<code class="descname">primary_shared_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.primary_shared_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary shared key for the Log Analytics Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Log Analytics workspace is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.retention_in_days">
<code class="descname">retention_in_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.retention_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>The workspace data retention in days. Possible values range between 30 and 730.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.secondary_shared_key">
<code class="descname">secondary_shared_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.secondary_shared_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary shared key for the Log Analytics Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Sku of the Log Analytics Workspace. Possible values are <code class="docutils literal notranslate"><span class="pre">Free</span></code>, <code class="docutils literal notranslate"><span class="pre">PerNode</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">Standalone</span></code>, <code class="docutils literal notranslate"><span class="pre">Unlimited</span></code>, and <code class="docutils literal notranslate"><span class="pre">PerGB2018</span></code> (new Sku as of <code class="docutils literal notranslate"><span class="pre">2018-04-03</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.workspace_id">
<code class="descname">workspace_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.workspace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Workspace (or Customer) ID for the Log Analytics Workspace.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService">
<em class="property">class </em><code class="descclassname">pulumi_azure.operationalinsights.</code><code class="descname">AnalyticsWorkspaceLinkedService</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>linked_service_name=None</em>, <em>linked_service_properties=None</em>, <em>resource_group_name=None</em>, <em>resource_id=None</em>, <em>tags=None</em>, <em>workspace_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService" title="Permalink to this definition">¶</a></dt>
<dd><p>Links a Log Analytics (formally Operational Insights) Workspace to another resource. The (currently) only linkable service is an Azure Automation Account.</p>
<blockquote>
<div><strong>NOTE:</strong> This resource has been deprecated in favour of the <code class="docutils literal notranslate"><span class="pre">azurerm_log_analytics_linked_service</span></code> resource and will be removed in the next major version of the AzureRM Provider. The new resource shares the same fields as this one, and information on migrating across can be found in this guide.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>linked_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the type of linkedServices resource to connect to the Log Analytics Workspace specified in <code class="docutils literal notranslate"><span class="pre">workspace_name</span></code>. Currently it defaults to and only supports <code class="docutils literal notranslate"><span class="pre">automation</span></code> as a value. Changing this forces a new resource to be created.</li>
<li><strong>linked_service_properties</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">linked_service_properties</span></code> block as defined below.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Log Analytics Linked Service is created. Changing this forces a new resource to be created.</li>
<li><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource id of the resource that will be linked to the workspace. This field has been deprecated in favour of the top-level <code class="docutils literal notranslate"><span class="pre">resource_id</span></code> field and will be removed in v2.0 of the AzureRM Provider.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>workspace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Log Analytics Workspace that will contain the linkedServices resource. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService.linked_service_name">
<code class="descname">linked_service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService.linked_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the type of linkedServices resource to connect to the Log Analytics Workspace specified in <code class="docutils literal notranslate"><span class="pre">workspace_name</span></code>. Currently it defaults to and only supports <code class="docutils literal notranslate"><span class="pre">automation</span></code> as a value. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService.linked_service_properties">
<code class="descname">linked_service_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService.linked_service_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">linked_service_properties</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The automatically generated name of the Linked Service. This cannot be specified. The format is always <code class="docutils literal notranslate"><span class="pre">&lt;workspace_name&gt;/&lt;linked_service_name&gt;</span></code> e.g. <code class="docutils literal notranslate"><span class="pre">workspace1/Automation</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Log Analytics Linked Service is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService.resource_id">
<code class="descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource id of the resource that will be linked to the workspace. This field has been deprecated in favour of the top-level <code class="docutils literal notranslate"><span class="pre">resource_id</span></code> field and will be removed in v2.0 of the AzureRM Provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService.workspace_name">
<code class="descname">workspace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService.workspace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Log Analytics Workspace that will contain the linkedServices resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspaceLinkedService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.operationalinsights.</code><code class="descname">GetAnalyticsWorkspaceResult</code><span class="sig-paren">(</span><em>location=None</em>, <em>name=None</em>, <em>portal_url=None</em>, <em>primary_shared_key=None</em>, <em>resource_group_name=None</em>, <em>retention_in_days=None</em>, <em>secondary_shared_key=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>workspace_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAnalyticsWorkspace.</p>
<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.portal_url">
<code class="descname">portal_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.portal_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The Portal URL for the Log Analytics Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.primary_shared_key">
<code class="descname">primary_shared_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.primary_shared_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary shared key for the Log Analytics Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.retention_in_days">
<code class="descname">retention_in_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.retention_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>The workspace data retention in days.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.secondary_shared_key">
<code class="descname">secondary_shared_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.secondary_shared_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary shared key for the Log Analytics Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The Sku of the Log Analytics Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.workspace_id">
<code class="descname">workspace_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.workspace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Workspace (or Customer) ID for the Log Analytics Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_azure.operationalinsights.get_analytics_workspace">
<code class="descclassname">pulumi_azure.operationalinsights.</code><code class="descname">get_analytics_workspace</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.get_analytics_workspace" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Log Analytics (formally Operational Insights) Workspace.</p>
</dd></dl>

</div>
