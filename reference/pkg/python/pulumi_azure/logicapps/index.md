<div class="section" id="module-pulumi_azure.logicapps">
<span id="logicapps"></span><h1>logicapps<a class="headerlink" href="#module-pulumi_azure.logicapps" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.logicapps.ActionCustom">
<em class="property">class </em><code class="descclassname">pulumi_azure.logicapps.</code><code class="descname">ActionCustom</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>body=None</em>, <em>logic_app_id=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.ActionCustom" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Custom Action within a Logic App Workflow</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the JSON Blob defining the Body of this Custom Action.</li>
<li><strong>logic_app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.logicapps.ActionCustom.body">
<code class="descname">body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionCustom.body" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the JSON Blob defining the Body of this Custom Action.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.ActionCustom.logic_app_id">
<code class="descname">logic_app_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionCustom.logic_app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.ActionCustom.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionCustom.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.logicapps.ActionCustom.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.ActionCustom.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.ActionCustom.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.ActionCustom.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.ActionHttp">
<em class="property">class </em><code class="descclassname">pulumi_azure.logicapps.</code><code class="descname">ActionHttp</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>body=None</em>, <em>headers=None</em>, <em>logic_app_id=None</em>, <em>method=None</em>, <em>name=None</em>, <em>uri=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an HTTP Action within a Logic App Workflow</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the HTTP Body that should be sent to the <code class="docutils literal notranslate"><span class="pre">uri</span></code> when this HTTP Action is triggered.</li>
<li><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a Map of Key-Value Pairs that should be sent to the <code class="docutils literal notranslate"><span class="pre">uri</span></code> when this HTTP Action is triggered.</li>
<li><strong>logic_app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</li>
<li><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the HTTP Method which should be used for this HTTP Action. Possible values include <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code> and <code class="docutils literal notranslate"><span class="pre">PUT</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.</li>
<li><strong>uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the URI which will be called when this HTTP Action is triggered.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.logicapps.ActionHttp.body">
<code class="descname">body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp.body" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the HTTP Body that should be sent to the <code class="docutils literal notranslate"><span class="pre">uri</span></code> when this HTTP Action is triggered.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.ActionHttp.headers">
<code class="descname">headers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp.headers" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a Map of Key-Value Pairs that should be sent to the <code class="docutils literal notranslate"><span class="pre">uri</span></code> when this HTTP Action is triggered.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.ActionHttp.logic_app_id">
<code class="descname">logic_app_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp.logic_app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.ActionHttp.method">
<code class="descname">method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp.method" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the HTTP Method which should be used for this HTTP Action. Possible values include <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code> and <code class="docutils literal notranslate"><span class="pre">PUT</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.ActionHttp.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.ActionHttp.uri">
<code class="descname">uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp.uri" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the URI which will be called when this HTTP Action is triggered.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.logicapps.ActionHttp.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.ActionHttp.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.GetWorkflowResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.logicapps.</code><code class="descname">GetWorkflowResult</code><span class="sig-paren">(</span><em>access_endpoint=None</em>, <em>location=None</em>, <em>parameters=None</em>, <em>tags=None</em>, <em>workflow_schema=None</em>, <em>workflow_version=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getWorkflow.</p>
<dl class="attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.access_endpoint">
<code class="descname">access_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.access_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Access Endpoint for the Logic App Workflow</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the Logic App Workflow exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Key-Value pairs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.workflow_schema">
<code class="descname">workflow_schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.workflow_schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The Schema used for this Logic App Workflow.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.workflow_version">
<code class="descname">workflow_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.workflow_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the Schema used for this Logic App Workflow. Defaults to <code class="docutils literal notranslate"><span class="pre">1.0.0.0</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.logicapps.TriggerCustom">
<em class="property">class </em><code class="descclassname">pulumi_azure.logicapps.</code><code class="descname">TriggerCustom</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>body=None</em>, <em>logic_app_id=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerCustom" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Custom Trigger within a Logic App Workflow</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the JSON Blob defining the Body of this Custom Trigger.</li>
<li><strong>logic_app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the HTTP Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.logicapps.TriggerCustom.body">
<code class="descname">body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerCustom.body" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the JSON Blob defining the Body of this Custom Trigger.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.TriggerCustom.logic_app_id">
<code class="descname">logic_app_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerCustom.logic_app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.TriggerCustom.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerCustom.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the HTTP Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.logicapps.TriggerCustom.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerCustom.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.TriggerCustom.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerCustom.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.TriggerHttpRequest">
<em class="property">class </em><code class="descclassname">pulumi_azure.logicapps.</code><code class="descname">TriggerHttpRequest</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>logic_app_id=None</em>, <em>method=None</em>, <em>name=None</em>, <em>relative_path=None</em>, <em>schema=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerHttpRequest" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HTTP Request Trigger within a Logic App Workflow</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>logic_app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</li>
<li><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the HTTP Method which the request be using. Possible values include <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code> or <code class="docutils literal notranslate"><span class="pre">PUT</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the HTTP Request Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.</li>
<li><strong>relative_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Relative Path used for this Request.</li>
<li><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON Blob defining the Schema of the incoming request. This needs to be valid JSON.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.logicapps.TriggerHttpRequest.logic_app_id">
<code class="descname">logic_app_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerHttpRequest.logic_app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.TriggerHttpRequest.method">
<code class="descname">method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerHttpRequest.method" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the HTTP Method which the request be using. Possible values include <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code> or <code class="docutils literal notranslate"><span class="pre">PUT</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.TriggerHttpRequest.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerHttpRequest.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the HTTP Request Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.TriggerHttpRequest.relative_path">
<code class="descname">relative_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerHttpRequest.relative_path" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Relative Path used for this Request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.TriggerHttpRequest.schema">
<code class="descname">schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerHttpRequest.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON Blob defining the Schema of the incoming request. This needs to be valid JSON.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.logicapps.TriggerHttpRequest.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerHttpRequest.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.TriggerHttpRequest.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerHttpRequest.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.TriggerRecurrence">
<em class="property">class </em><code class="descclassname">pulumi_azure.logicapps.</code><code class="descname">TriggerRecurrence</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>frequency=None</em>, <em>interval=None</em>, <em>logic_app_id=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerRecurrence" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Recurrence Trigger within a Logic App Workflow</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Frequency at which this Trigger should be run. Possible values include <code class="docutils literal notranslate"><span class="pre">Month</span></code>, <code class="docutils literal notranslate"><span class="pre">Week</span></code>, <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Minute</span></code> and <code class="docutils literal notranslate"><span class="pre">Second</span></code>.</li>
<li><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies interval used for the Frequency, for example a value of <code class="docutils literal notranslate"><span class="pre">4</span></code> for <code class="docutils literal notranslate"><span class="pre">interval</span></code> and <code class="docutils literal notranslate"><span class="pre">hour</span></code> for <code class="docutils literal notranslate"><span class="pre">frequency</span></code> would run the Trigger every 4 hours.</li>
<li><strong>logic_app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recurrence Triggers to be created within the Logic App Workflow. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.logicapps.TriggerRecurrence.frequency">
<code class="descname">frequency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerRecurrence.frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Frequency at which this Trigger should be run. Possible values include <code class="docutils literal notranslate"><span class="pre">Month</span></code>, <code class="docutils literal notranslate"><span class="pre">Week</span></code>, <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Minute</span></code> and <code class="docutils literal notranslate"><span class="pre">Second</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.TriggerRecurrence.interval">
<code class="descname">interval</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerRecurrence.interval" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies interval used for the Frequency, for example a value of <code class="docutils literal notranslate"><span class="pre">4</span></code> for <code class="docutils literal notranslate"><span class="pre">interval</span></code> and <code class="docutils literal notranslate"><span class="pre">hour</span></code> for <code class="docutils literal notranslate"><span class="pre">frequency</span></code> would run the Trigger every 4 hours.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.TriggerRecurrence.logic_app_id">
<code class="descname">logic_app_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerRecurrence.logic_app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.TriggerRecurrence.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerRecurrence.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Recurrence Triggers to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.logicapps.TriggerRecurrence.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerRecurrence.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.TriggerRecurrence.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerRecurrence.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.Workflow">
<em class="property">class </em><code class="descclassname">pulumi_azure.logicapps.</code><code class="descname">Workflow</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>name=None</em>, <em>parameters=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>workflow_schema=None</em>, <em>workflow_version=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.Workflow" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Logic App Workflow.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the Logic App Workflow exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Logic App Workflow. Changing this forces a new resource to be created.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Key-Value pairs.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Logic App Workflow should be created. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>workflow_schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Schema to use for this Logic App Workflow. Defaults to <code class="docutils literal notranslate"><span class="pre">https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#</span></code>. Changing this forces a new resource to be created.</li>
<li><strong>workflow_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version of the Schema used for this Logic App Workflow. Defaults to <code class="docutils literal notranslate"><span class="pre">1.0.0.0</span></code>. Changing this forces a new resource to be create.d</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.logicapps.Workflow.access_endpoint">
<code class="descname">access_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.access_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Access Endpoint for the Logic App Workflow</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.Workflow.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the Logic App Workflow exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.Workflow.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.Workflow.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Key-Value pairs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.Workflow.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Logic App Workflow should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.Workflow.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.Workflow.workflow_schema">
<code class="descname">workflow_schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.workflow_schema" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Schema to use for this Logic App Workflow. Defaults to <code class="docutils literal notranslate"><span class="pre">https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.logicapps.Workflow.workflow_version">
<code class="descname">workflow_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.workflow_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the version of the Schema used for this Logic App Workflow. Defaults to <code class="docutils literal notranslate"><span class="pre">1.0.0.0</span></code>. Changing this forces a new resource to be create.d</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.logicapps.Workflow.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.Workflow.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.get_workflow">
<code class="descclassname">pulumi_azure.logicapps.</code><code class="descname">get_workflow</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.get_workflow" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Logic App Workflow.</p>
</dd></dl>

</div>
