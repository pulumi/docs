---
---

<div class="section" id="module-pulumi_azure.appinsights">
<span id="appinsights"></span><h1>appinsights<a class="headerlink" href="#module-pulumi_azure.appinsights" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.appinsights.ApiKey">
<em class="property">class </em><code class="descclassname">pulumi_azure.appinsights.</code><code class="descname">ApiKey</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application_insights_id=None</em>, <em>name=None</em>, <em>read_permissions=None</em>, <em>write_permissions=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appinsights.ApiKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Application Insights API key.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application_insights_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Application Insights component on which the API key operates. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Application Insights API key. Changing this forces a
new resource to be created.</li>
<li><strong>read_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the list of read permissions granted to the API key. Valid values are <code class="docutils literal notranslate"><span class="pre">agentconfig</span></code>, <code class="docutils literal notranslate"><span class="pre">aggregate</span></code>, <code class="docutils literal notranslate"><span class="pre">api</span></code>, <code class="docutils literal notranslate"><span class="pre">draft</span></code>, <code class="docutils literal notranslate"><span class="pre">extendqueries</span></code>, <code class="docutils literal notranslate"><span class="pre">search</span></code>. Please note these values are case sensitive. Changing this forces a new resource to be created.</li>
<li><strong>write_permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the list of write permissions granted to the API key. Valid values are <code class="docutils literal notranslate"><span class="pre">annotations</span></code>. Please note these values are case sensitive. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.appinsights.ApiKey.api_key">
<code class="descname">api_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.ApiKey.api_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The API Key secret (Sensitive).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.ApiKey.application_insights_id">
<code class="descname">application_insights_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.ApiKey.application_insights_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Application Insights component on which the API key operates. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.ApiKey.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.ApiKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Application Insights API key. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.ApiKey.read_permissions">
<code class="descname">read_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.ApiKey.read_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the list of read permissions granted to the API key. Valid values are <code class="docutils literal notranslate"><span class="pre">agentconfig</span></code>, <code class="docutils literal notranslate"><span class="pre">aggregate</span></code>, <code class="docutils literal notranslate"><span class="pre">api</span></code>, <code class="docutils literal notranslate"><span class="pre">draft</span></code>, <code class="docutils literal notranslate"><span class="pre">extendqueries</span></code>, <code class="docutils literal notranslate"><span class="pre">search</span></code>. Please note these values are case sensitive. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.ApiKey.write_permissions">
<code class="descname">write_permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.ApiKey.write_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the list of write permissions granted to the API key. Valid values are <code class="docutils literal notranslate"><span class="pre">annotations</span></code>. Please note these values are case sensitive. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appinsights.ApiKey.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appinsights.ApiKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appinsights.ApiKey.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appinsights.ApiKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appinsights.GetInsightsResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.appinsights.</code><code class="descname">GetInsightsResult</code><span class="sig-paren">(</span><em>app_id=None</em>, <em>application_type=None</em>, <em>instrumentation_key=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appinsights.GetInsightsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInsights.</p>
<dl class="attribute">
<dt id="pulumi_azure.appinsights.GetInsightsResult.app_id">
<code class="descname">app_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.GetInsightsResult.app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The App ID associated with this Application Insights component.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.GetInsightsResult.application_type">
<code class="descname">application_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.GetInsightsResult.application_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the component.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.GetInsightsResult.instrumentation_key">
<code class="descname">instrumentation_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.GetInsightsResult.instrumentation_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The instrumentation key of the Application Insights component.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.GetInsightsResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.GetInsightsResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the component exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.GetInsightsResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.GetInsightsResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tags applied to the component.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.GetInsightsResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.GetInsightsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.appinsights.Insights">
<em class="property">class </em><code class="descclassname">pulumi_azure.appinsights.</code><code class="descname">Insights</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application_type=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appinsights.Insights" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage an Application Insights component.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of Application Insights to create. Valid values are <code class="docutils literal notranslate"><span class="pre">ios</span></code> for <em>iOS</em>, <code class="docutils literal notranslate"><span class="pre">java</span></code> for <em>Java web</em>, <code class="docutils literal notranslate"><span class="pre">MobileCenter</span></code> for <em>App Center</em>, <code class="docutils literal notranslate"><span class="pre">Node.JS</span></code> for <em>Node.js</em>, <code class="docutils literal notranslate"><span class="pre">other</span></code> for <em>General</em>, <code class="docutils literal notranslate"><span class="pre">phone</span></code> for <em>Windows Phone</em>, <code class="docutils literal notranslate"><span class="pre">store</span></code> for <em>Windows Store</em> and <code class="docutils literal notranslate"><span class="pre">web</span></code> for <em>ASP.NET</em>. Please note these values are case sensitive; unmatched values are treated as <em>ASP.NET</em> by Azure. Changing this forces a new resource to be created.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Application Insights component. Changing this forces a
new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the Application Insights component.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.appinsights.Insights.app_id">
<code class="descname">app_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.Insights.app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The App ID associated with this Application Insights component.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.Insights.application_type">
<code class="descname">application_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.Insights.application_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of Application Insights to create. Valid values are <code class="docutils literal notranslate"><span class="pre">ios</span></code> for <em>iOS</em>, <code class="docutils literal notranslate"><span class="pre">java</span></code> for <em>Java web</em>, <code class="docutils literal notranslate"><span class="pre">MobileCenter</span></code> for <em>App Center</em>, <code class="docutils literal notranslate"><span class="pre">Node.JS</span></code> for <em>Node.js</em>, <code class="docutils literal notranslate"><span class="pre">other</span></code> for <em>General</em>, <code class="docutils literal notranslate"><span class="pre">phone</span></code> for <em>Windows Phone</em>, <code class="docutils literal notranslate"><span class="pre">store</span></code> for <em>Windows Store</em> and <code class="docutils literal notranslate"><span class="pre">web</span></code> for <em>ASP.NET</em>. Please note these values are case sensitive; unmatched values are treated as <em>ASP.NET</em> by Azure. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.Insights.instrumentation_key">
<code class="descname">instrumentation_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.Insights.instrumentation_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Instrumentation Key for this Application Insights component.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.Insights.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.Insights.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.Insights.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.Insights.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Application Insights component. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.Insights.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.Insights.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the Application Insights component.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.Insights.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.Insights.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appinsights.Insights.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appinsights.Insights.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appinsights.Insights.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appinsights.Insights.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appinsights.WebTest">
<em class="property">class </em><code class="descclassname">pulumi_azure.appinsights.</code><code class="descname">WebTest</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application_insights_id=None</em>, <em>configuration=None</em>, <em>description=None</em>, <em>enabled=None</em>, <em>frequency=None</em>, <em>geo_locations=None</em>, <em>kind=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>retry_enabled=None</em>, <em>tags=None</em>, <em>timeout=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appinsights.WebTest" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Application Insights WebTest.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application_insights_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Application Insights component on which the WebTest operates. Changing this forces a new resource to be created.</li>
<li><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An XML configuration specification for a WebTest.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Purpose/user defined descriptive test for this WebTest.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the test actively being monitored.</li>
<li><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Interval in seconds between test runs for this WebTest. Default is <code class="docutils literal notranslate"><span class="pre">300</span></code>.</li>
<li><strong>geo_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of where to physically run the tests from to give global coverage for accessibility of your application.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the resource group.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Application Insights WebTest. Changing this forces a
new resource to be created.</li>
<li><strong>retry_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow for retries should this WebTest fail.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Resource tags.</li>
<li><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Seconds until this WebTest will timeout and fail. Default is <code class="docutils literal notranslate"><span class="pre">30</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.appinsights.WebTest.application_insights_id">
<code class="descname">application_insights_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.WebTest.application_insights_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Application Insights component on which the WebTest operates. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.WebTest.configuration">
<code class="descname">configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.WebTest.configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>An XML configuration specification for a WebTest.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.WebTest.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.WebTest.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Purpose/user defined descriptive test for this WebTest.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.WebTest.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.WebTest.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the test actively being monitored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.WebTest.frequency">
<code class="descname">frequency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.WebTest.frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>Interval in seconds between test runs for this WebTest. Default is <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.WebTest.geo_locations">
<code class="descname">geo_locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.WebTest.geo_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of where to physically run the tests from to give global coverage for accessibility of your application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.WebTest.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.WebTest.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the resource group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.WebTest.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.WebTest.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Application Insights WebTest. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.WebTest.retry_enabled">
<code class="descname">retry_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.WebTest.retry_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow for retries should this WebTest fail.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.WebTest.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.WebTest.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource tags.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.appinsights.WebTest.timeout">
<code class="descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.appinsights.WebTest.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Seconds until this WebTest will timeout and fail. Default is <code class="docutils literal notranslate"><span class="pre">30</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.appinsights.WebTest.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appinsights.WebTest.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appinsights.WebTest.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appinsights.WebTest.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.appinsights.get_insights">
<code class="descclassname">pulumi_azure.appinsights.</code><code class="descname">get_insights</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.appinsights.get_insights" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Application Insights component.</p>
</dd></dl>

</div>
