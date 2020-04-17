---
title: Module operationalinsights
title_tag: Module operationalinsights | Package pulumi_azure | Python SDK
linktitle: operationalinsights
notitle: true
---

<div class="section" id="operationalinsights">
<h1>operationalinsights<a class="headerlink" href="#operationalinsights" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.operationalinsights"></span><dl class="class">
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.operationalinsights.</code><code class="sig-name descname">AnalyticsSolution</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">solution_name=None</em>, <em class="sig-param">workspace_name=None</em>, <em class="sig-param">workspace_resource_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Log Analytics (formally Operational Insights) Solution.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">plan</span></code> block as documented below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and it’s related workspace can only exist in the same resource group.</p></li>
<li><p><strong>solution_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the solution to be deployed. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-add-solutions">here for options</a>.Changing this forces a new resource to be created.</p></li>
<li><p><strong>workspace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full name of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.</p></li>
<li><p><strong>workspace_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>plan</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The product name of the solution. For example <code class="docutils literal notranslate"><span class="pre">OMSGallery/Containers</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">promotionCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A promotion code to be used with the solution.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The publisher of the solution. For example <code class="docutils literal notranslate"><span class="pre">Microsoft</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution.plan">
<code class="sig-name descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">plan</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The product name of the solution. For example <code class="docutils literal notranslate"><span class="pre">OMSGallery/Containers</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">promotionCode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A promotion code to be used with the solution.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The publisher of the solution. For example <code class="docutils literal notranslate"><span class="pre">Microsoft</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and it’s related workspace can only exist in the same resource group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution.solution_name">
<code class="sig-name descname">solution_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution.solution_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the solution to be deployed. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-add-solutions">here for options</a>.Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution.workspace_name">
<code class="sig-name descname">workspace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution.workspace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The full name of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution.workspace_resource_id">
<code class="sig-name descname">workspace_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution.workspace_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">solution_name=None</em>, <em class="sig-param">workspace_name=None</em>, <em class="sig-param">workspace_resource_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AnalyticsSolution resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">plan</span></code> block as documented below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Log Analytics solution is created. Changing this forces a new resource to be created. Note: The solution and it’s related workspace can only exist in the same resource group.</p></li>
<li><p><strong>solution_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the name of the solution to be deployed. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/log-analytics/log-analytics-add-solutions">here for options</a>.Changing this forces a new resource to be created.</p>
</p></li>
<li><p><strong>workspace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full name of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.</p></li>
<li><p><strong>workspace_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full resource ID of the Log Analytics workspace with which the solution will be linked. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>plan</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The product name of the solution. For example <code class="docutils literal notranslate"><span class="pre">OMSGallery/Containers</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">promotionCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A promotion code to be used with the solution.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The publisher of the solution. For example <code class="docutils literal notranslate"><span class="pre">Microsoft</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.operationalinsights.AnalyticsSolution.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsSolution.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.operationalinsights.</code><code class="sig-name descname">AnalyticsWorkspace</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">retention_in_days=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Log Analytics (formally Operational Insights) Workspace.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Log Analytics Workspace. Workspace name should include 4-63 letters, digits or ‘-‘. The ‘-‘ shouldn’t be the first or the last symbol. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Log Analytics workspace is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>retention_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The workspace data retention in days. Possible values range between 30 and 730.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Sku of the Log Analytics Workspace. Possible values are <code class="docutils literal notranslate"><span class="pre">Free</span></code>, <code class="docutils literal notranslate"><span class="pre">PerNode</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">Standalone</span></code>, <code class="docutils literal notranslate"><span class="pre">Unlimited</span></code>, and <code class="docutils literal notranslate"><span class="pre">PerGB2018</span></code> (new Sku as of <code class="docutils literal notranslate"><span class="pre">2018-04-03</span></code>).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Log Analytics Workspace. Workspace name should include 4-63 letters, digits or ‘-‘. The ‘-‘ shouldn’t be the first or the last symbol. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.portal_url">
<code class="sig-name descname">portal_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.portal_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The Portal URL for the Log Analytics Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.primary_shared_key">
<code class="sig-name descname">primary_shared_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.primary_shared_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary shared key for the Log Analytics Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Log Analytics workspace is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.retention_in_days">
<code class="sig-name descname">retention_in_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.retention_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>The workspace data retention in days. Possible values range between 30 and 730.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.secondary_shared_key">
<code class="sig-name descname">secondary_shared_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.secondary_shared_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary shared key for the Log Analytics Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Sku of the Log Analytics Workspace. Possible values are <code class="docutils literal notranslate"><span class="pre">Free</span></code>, <code class="docutils literal notranslate"><span class="pre">PerNode</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">Standalone</span></code>, <code class="docutils literal notranslate"><span class="pre">Unlimited</span></code>, and <code class="docutils literal notranslate"><span class="pre">PerGB2018</span></code> (new Sku as of <code class="docutils literal notranslate"><span class="pre">2018-04-03</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.workspace_id">
<code class="sig-name descname">workspace_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.workspace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Workspace (or Customer) ID for the Log Analytics Workspace.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">portal_url=None</em>, <em class="sig-param">primary_shared_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">retention_in_days=None</em>, <em class="sig-param">secondary_shared_key=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">workspace_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AnalyticsWorkspace resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Log Analytics Workspace. Workspace name should include 4-63 letters, digits or ‘-‘. The ‘-‘ shouldn’t be the first or the last symbol. Changing this forces a new resource to be created.</p></li>
<li><p><strong>portal_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Portal URL for the Log Analytics Workspace.</p></li>
<li><p><strong>primary_shared_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary shared key for the Log Analytics Workspace.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Log Analytics workspace is created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>retention_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The workspace data retention in days. Possible values range between 30 and 730.</p></li>
<li><p><strong>secondary_shared_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary shared key for the Log Analytics Workspace.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Sku of the Log Analytics Workspace. Possible values are <code class="docutils literal notranslate"><span class="pre">Free</span></code>, <code class="docutils literal notranslate"><span class="pre">PerNode</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">Standalone</span></code>, <code class="docutils literal notranslate"><span class="pre">Unlimited</span></code>, and <code class="docutils literal notranslate"><span class="pre">PerGB2018</span></code> (new Sku as of <code class="docutils literal notranslate"><span class="pre">2018-04-03</span></code>).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>workspace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Workspace (or Customer) ID for the Log Analytics Workspace.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.operationalinsights.AnalyticsWorkspace.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.AnalyticsWorkspace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.operationalinsights.AwaitableGetAnalyticsWorkspaceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.operationalinsights.</code><code class="sig-name descname">AwaitableGetAnalyticsWorkspaceResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">portal_url=None</em>, <em class="sig-param">primary_shared_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">retention_in_days=None</em>, <em class="sig-param">secondary_shared_key=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">workspace_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.AwaitableGetAnalyticsWorkspaceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.operationalinsights.</code><code class="sig-name descname">GetAnalyticsWorkspaceResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">portal_url=None</em>, <em class="sig-param">primary_shared_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">retention_in_days=None</em>, <em class="sig-param">secondary_shared_key=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">workspace_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAnalyticsWorkspace.</p>
<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.portal_url">
<code class="sig-name descname">portal_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.portal_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The Portal URL for the Log Analytics Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.primary_shared_key">
<code class="sig-name descname">primary_shared_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.primary_shared_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary shared key for the Log Analytics Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.retention_in_days">
<code class="sig-name descname">retention_in_days</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.retention_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>The workspace data retention in days.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.secondary_shared_key">
<code class="sig-name descname">secondary_shared_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.secondary_shared_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary shared key for the Log Analytics Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The Sku of the Log Analytics Workspace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.workspace_id">
<code class="sig-name descname">workspace_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.operationalinsights.GetAnalyticsWorkspaceResult.workspace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Workspace (or Customer) ID for the Log Analytics Workspace.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_azure.operationalinsights.get_analytics_workspace">
<code class="sig-prename descclassname">pulumi_azure.operationalinsights.</code><code class="sig-name descname">get_analytics_workspace</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.operationalinsights.get_analytics_workspace" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Log Analytics (formally Operational Insights) Workspace.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Log Analytics Workspace.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group in which the Log Analytics workspace is located in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
