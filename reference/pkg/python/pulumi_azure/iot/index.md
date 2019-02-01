<div class="section" id="module-pulumi_azure.iot">
<span id="iot"></span><h1>iot<a class="headerlink" href="#module-pulumi_azure.iot" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.iot.ConsumerGroup">
<em class="property">class </em><code class="descclassname">pulumi_azure.iot.</code><code class="descname">ConsumerGroup</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>eventhub_endpoint_name=None</em>, <em>iothub_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.ConsumerGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Consumer Group within an IotHub</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>eventhub_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Event Hub-compatible endpoint in the IoT hub. Changing this forces a new resource to be created.</li>
<li><strong>iothub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IoT Hub. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this Consumer Group. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group that contains the IoT hub. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.iot.ConsumerGroup.eventhub_endpoint_name">
<code class="descname">eventhub_endpoint_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.ConsumerGroup.eventhub_endpoint_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Event Hub-compatible endpoint in the IoT hub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.ConsumerGroup.iothub_name">
<code class="descname">iothub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.ConsumerGroup.iothub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IoT Hub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.ConsumerGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.ConsumerGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this Consumer Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.ConsumerGroup.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.ConsumerGroup.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group that contains the IoT hub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.ConsumerGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.ConsumerGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.ConsumerGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.ConsumerGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.IoTHub">
<em class="property">class </em><code class="descclassname">pulumi_azure.iot.</code><code class="descname">IoTHub</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>endpoints=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>routes=None</em>, <em>sku=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.IoTHub" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an IotHub</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An <cite>endpoint</cite> block as defined below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.</li>
<li><strong>routes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <cite>route</cite> block as defined below.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>sku</cite> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.endpoints">
<code class="descname">endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>An <cite>endpoint</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.event_hub_events_endpoint">
<code class="descname">event_hub_events_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.event_hub_events_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The EventHub compatible endpoint for events data</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.event_hub_events_path">
<code class="descname">event_hub_events_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.event_hub_events_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The EventHub compatible path for events data</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.event_hub_operations_endpoint">
<code class="descname">event_hub_operations_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.event_hub_operations_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The EventHub compatible endpoint for operational data</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.event_hub_operations_path">
<code class="descname">event_hub_operations_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.event_hub_operations_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The EventHub compatible path for operational data</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.hostname">
<code class="descname">hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname of the IotHub Resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.routes">
<code class="descname">routes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.routes" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>route</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.shared_access_policies">
<code class="descname">shared_access_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.shared_access_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>shared_access_policy</cite> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>sku</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.IoTHub.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.IoTHub.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.IoTHub.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.IoTHub.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
