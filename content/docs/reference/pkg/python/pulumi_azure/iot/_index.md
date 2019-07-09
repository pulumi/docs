---
---

<div class="section" id="iot">
<h1>iot<a class="headerlink" href="#iot" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azure">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azure/issues">terraform-providers/terraform-provider-azure repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_azure.iot"></span><dl class="class">
<dt id="pulumi_azure.iot.Certificate">
<em class="property">class </em><code class="descclassname">pulumi_azure.iot.</code><code class="descname">Certificate</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>certificate_content=None</em>, <em>iot_dps_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.Certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an IoT Device Provisioning Service Certificate.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>certificate_content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Base-64 representation of the X509 leaf certificate .cer file or just a .pem file content.</li>
<li><strong>iot_dps_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IoT Device Provisioning Service that this certificate will be attached to. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Iot Device Provisioning Service Certificate resource. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the Iot Device Provisioning Service Certificate resource has to be created. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iot_dps_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iot_dps_certificate.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.iot.Certificate.certificate_content">
<code class="descname">certificate_content</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.Certificate.certificate_content" title="Permalink to this definition">¶</a></dt>
<dd><p>The Base-64 representation of the X509 leaf certificate .cer file or just a .pem file content.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.Certificate.iot_dps_name">
<code class="descname">iot_dps_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.Certificate.iot_dps_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IoT Device Provisioning Service that this certificate will be attached to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.Certificate.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.Certificate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Iot Device Provisioning Service Certificate resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.Certificate.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.Certificate.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group under which the Iot Device Provisioning Service Certificate resource has to be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.Certificate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.Certificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.Certificate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.Certificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.ConsumerGroup">
<em class="property">class </em><code class="descclassname">pulumi_azure.iot.</code><code class="descname">ConsumerGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>eventhub_endpoint_name=None</em>, <em>iothub_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.ConsumerGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Consumer Group within an IotHub</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>eventhub_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Event Hub-compatible endpoint in the IoT hub. Changing this forces a new resource to be created.</li>
<li><strong>iothub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IoT Hub. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this Consumer Group. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group that contains the IoT hub. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_consumer_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_consumer_group.html.markdown</a>.</div></blockquote>
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
<dt id="pulumi_azure.iot.Dps">
<em class="property">class </em><code class="descclassname">pulumi_azure.iot.</code><code class="descname">Dps</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.Dps" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an IoT Device Provisioning Service.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Iot Device Provisioning Service resource. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the Iot Device Provisioning Service resource has to be created. Changing this forces a new resource to be created.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iot_dps.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iot_dps.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.iot.Dps.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.Dps.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.Dps.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.Dps.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Iot Device Provisioning Service resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.Dps.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.Dps.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group under which the Iot Device Provisioning Service resource has to be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.Dps.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.Dps.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.Dps.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.Dps.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.Dps.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.Dps.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.Dps.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.Dps.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="descclassname">pulumi_azure.iot.</code><code class="descname">IoTHub</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>endpoints=None</em>, <em>fallback_route=None</em>, <em>ip_filter_rules=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>routes=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.IoTHub" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an IotHub</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">endpoint</span></code> block as defined below.</li>
<li><strong>fallback_route</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">fallback_route</span></code> block as defined below. If the fallback route is enabled, messages that don’t match any of the supplied routes are automatically sent to this route. Defaults to messages/events.</li>
<li><strong>ip_filter_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">ip_filter_rule</span></code> blocks as defined below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the IotHub resource. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.</li>
<li><strong>routes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">route</span></code> block as defined below.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.endpoints">
<code class="descname">endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">endpoint</span></code> block as defined below.</p>
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
<dt id="pulumi_azure.iot.IoTHub.fallback_route">
<code class="descname">fallback_route</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.fallback_route" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">fallback_route</span></code> block as defined below. If the fallback route is enabled, messages that don’t match any of the supplied routes are automatically sent to this route. Defaults to messages/events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.hostname">
<code class="descname">hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The hostname of the IotHub Resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.ip_filter_rules">
<code class="descname">ip_filter_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.ip_filter_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">ip_filter_rule</span></code> blocks as defined below.</p>
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
<dd><p>A <code class="docutils literal notranslate"><span class="pre">route</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.shared_access_policies">
<code class="descname">shared_access_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.shared_access_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">shared_access_policy</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.IoTHub.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.IoTHub.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p>
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

<dl class="class">
<dt id="pulumi_azure.iot.SharedAccessPolicy">
<em class="property">class </em><code class="descclassname">pulumi_azure.iot.</code><code class="descname">SharedAccessPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>device_connect=None</em>, <em>iothub_name=None</em>, <em>name=None</em>, <em>registry_read=None</em>, <em>registry_write=None</em>, <em>resource_group_name=None</em>, <em>service_connect=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an IotHub Shared Access Policy</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>device_connect</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">DeviceConnect</span></code> permission to this Shared Access Account. It allows sending and receiving on the device-side endpoints.</li>
<li><strong>iothub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IoTHub to which this Shared Access Policy belongs. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the IotHub Shared Access Policy resource. Changing this forces a new resource to be created.</li>
<li><strong>registry_read</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">RegistryRead</span></code> permission to this Shared Access Account. It allows read access to the identity registry.</li>
<li><strong>registry_write</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">RegistryWrite</span></code> permission to this Shared Access Account. It allows write access to the identity registry.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the IotHub Shared Access Policy resource has to be created. Changing this forces a new resource to be created.</li>
<li><strong>service_connect</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Adds <code class="docutils literal notranslate"><span class="pre">ServiceConnect</span></code> permission to this Shared Access Account. It allows sending and receiving on the cloud-side endpoints.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_shared_access_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/iothub_shared_access_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.device_connect">
<code class="descname">device_connect</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.device_connect" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds <code class="docutils literal notranslate"><span class="pre">DeviceConnect</span></code> permission to this Shared Access Account. It allows sending and receiving on the device-side endpoints.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.iothub_name">
<code class="descname">iothub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.iothub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IoTHub to which this Shared Access Policy belongs. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the IotHub Shared Access Policy resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.primary_connection_string">
<code class="descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string of the Shared Access Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.primary_key">
<code class="descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary key used to create the authentication token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.registry_read">
<code class="descname">registry_read</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.registry_read" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds <code class="docutils literal notranslate"><span class="pre">RegistryRead</span></code> permission to this Shared Access Account. It allows read access to the identity registry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.registry_write">
<code class="descname">registry_write</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.registry_write" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds <code class="docutils literal notranslate"><span class="pre">RegistryWrite</span></code> permission to this Shared Access Account. It allows write access to the identity registry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group under which the IotHub Shared Access Policy resource has to be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.secondary_connection_string">
<code class="descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string of the Shared Access Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.secondary_key">
<code class="descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary key used to create the authentication token.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.iot.SharedAccessPolicy.service_connect">
<code class="descname">service_connect</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.service_connect" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds <code class="docutils literal notranslate"><span class="pre">ServiceConnect</span></code> permission to this Shared Access Account. It allows sending and receiving on the cloud-side endpoints.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.iot.SharedAccessPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.iot.SharedAccessPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.iot.SharedAccessPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
