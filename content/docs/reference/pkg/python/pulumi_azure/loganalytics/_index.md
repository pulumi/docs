---
---

<div class="section" id="module-pulumi_azure.loganalytics">
<span id="loganalytics"></span><h1>loganalytics<a class="headerlink" href="#module-pulumi_azure.loganalytics" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.loganalytics.LinkedService">
<em class="property">class </em><code class="descclassname">pulumi_azure.loganalytics.</code><code class="descname">LinkedService</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>linked_service_name=None</em>, <em>linked_service_properties=None</em>, <em>resource_group_name=None</em>, <em>resource_id=None</em>, <em>tags=None</em>, <em>workspace_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService" title="Permalink to this definition">¶</a></dt>
<dd><p>Links a Log Analytics (formally Operational Insights) Workspace to another resource. The (currently) only linkable service is an Azure Automation Account.</p>
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
<dt id="pulumi_azure.loganalytics.LinkedService.linked_service_name">
<code class="descname">linked_service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.linked_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the type of linkedServices resource to connect to the Log Analytics Workspace specified in <code class="docutils literal notranslate"><span class="pre">workspace_name</span></code>. Currently it defaults to and only supports <code class="docutils literal notranslate"><span class="pre">automation</span></code> as a value. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.loganalytics.LinkedService.linked_service_properties">
<code class="descname">linked_service_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.linked_service_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">linked_service_properties</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.loganalytics.LinkedService.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The automatically generated name of the Linked Service. This cannot be specified. The format is always <code class="docutils literal notranslate"><span class="pre">&lt;workspace_name&gt;/&lt;linked_service_name&gt;</span></code> e.g. <code class="docutils literal notranslate"><span class="pre">workspace1/Automation</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.loganalytics.LinkedService.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Log Analytics Linked Service is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.loganalytics.LinkedService.resource_id">
<code class="descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource id of the resource that will be linked to the workspace. This field has been deprecated in favour of the top-level <code class="docutils literal notranslate"><span class="pre">resource_id</span></code> field and will be removed in v2.0 of the AzureRM Provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.loganalytics.LinkedService.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.loganalytics.LinkedService.workspace_name">
<code class="descname">workspace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.workspace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Log Analytics Workspace that will contain the linkedServices resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.loganalytics.LinkedService.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.loganalytics.LinkedService.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.loganalytics.LinkedService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
