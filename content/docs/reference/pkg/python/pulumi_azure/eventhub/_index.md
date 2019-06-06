---
---

<div class="section" id="module-pulumi_azure.eventhub">
<span id="eventhub"></span><h1>eventhub<a class="headerlink" href="#module-pulumi_azure.eventhub" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.eventhub.EventGridDomain">
<em class="property">class </em><code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">EventGridDomain</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>input_mapping_default_values=None</em>, <em>input_mapping_fields=None</em>, <em>input_schema=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventGridDomain" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EventGrid Domain</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>input_mapping_default_values</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">input_mapping_default_values</span></code> block as defined below.</li>
<li><strong>input_mapping_fields</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">input_mapping_fields</span></code> block as defined below.</li>
<li><strong>input_schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the schema in which incoming events will be published to this domain. Allowed values are <code class="docutils literal notranslate"><span class="pre">cloudeventv01schema</span></code>, <code class="docutils literal notranslate"><span class="pre">customeventschema</span></code>, or <code class="docutils literal notranslate"><span class="pre">eventgridschema</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">eventgridschema</span></code>. Changing this forces a new resource to be created.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventGrid Domain resource. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventGrid Domain exists. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridDomain.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridDomain.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Endpoint associated with the EventGrid Domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridDomain.input_mapping_default_values">
<code class="descname">input_mapping_default_values</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridDomain.input_mapping_default_values" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">input_mapping_default_values</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridDomain.input_mapping_fields">
<code class="descname">input_mapping_fields</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridDomain.input_mapping_fields" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">input_mapping_fields</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridDomain.input_schema">
<code class="descname">input_schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridDomain.input_schema" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the schema in which incoming events will be published to this domain. Allowed values are <code class="docutils literal notranslate"><span class="pre">cloudeventv01schema</span></code>, <code class="docutils literal notranslate"><span class="pre">customeventschema</span></code>, or <code class="docutils literal notranslate"><span class="pre">eventgridschema</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">eventgridschema</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridDomain.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridDomain.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridDomain.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridDomain.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventGrid Domain resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridDomain.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridDomain.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the EventGrid Domain exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridDomain.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridDomain.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventGridDomain.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventGridDomain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventGridDomain.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventGridDomain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventGridEventSubscription">
<em class="property">class </em><code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">EventGridEventSubscription</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>event_delivery_schema=None</em>, <em>eventhub_endpoint=None</em>, <em>hybrid_connection_endpoint=None</em>, <em>included_event_types=None</em>, <em>labels=None</em>, <em>name=None</em>, <em>retry_policy=None</em>, <em>scope=None</em>, <em>storage_blob_dead_letter_destination=None</em>, <em>storage_queue_endpoint=None</em>, <em>subject_filter=None</em>, <em>topic_name=None</em>, <em>webhook_endpoint=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventGridEventSubscription" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EventGrid Event Subscription</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>event_delivery_schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the event delivery schema for the event subscription. Possible values include: <code class="docutils literal notranslate"><span class="pre">EventGridSchema</span></code>, <code class="docutils literal notranslate"><span class="pre">CloudEventV01Schema</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomInputSchema</span></code>.</li>
<li><strong>eventhub_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">eventhub_endpoint</span></code> block as defined below.</li>
<li><strong>hybrid_connection_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">hybrid_connection_endpoint</span></code> block as defined below.</li>
<li><strong>included_event_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of applicable event types that need to be part of the event subscription.</li>
<li><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of labels to assign to the event subscription.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.</li>
<li><strong>retry_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">retry_policy</span></code> block as defined below.</li>
<li><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.</li>
<li><strong>storage_blob_dead_letter_destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_blob_dead_letter_destination</span></code> block as defined below.</li>
<li><strong>storage_queue_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_queue_endpoint</span></code> block as defined below.</li>
<li><strong>subject_filter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">subject_filter</span></code> block as defined below.</li>
<li><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the topic to associate with the event subscription.</li>
<li><strong>webhook_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">webhook_endpoint</span></code> block as defined below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridEventSubscription.event_delivery_schema">
<code class="descname">event_delivery_schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridEventSubscription.event_delivery_schema" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the event delivery schema for the event subscription. Possible values include: <code class="docutils literal notranslate"><span class="pre">EventGridSchema</span></code>, <code class="docutils literal notranslate"><span class="pre">CloudEventV01Schema</span></code>, <code class="docutils literal notranslate"><span class="pre">CustomInputSchema</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridEventSubscription.eventhub_endpoint">
<code class="descname">eventhub_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridEventSubscription.eventhub_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">eventhub_endpoint</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridEventSubscription.hybrid_connection_endpoint">
<code class="descname">hybrid_connection_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridEventSubscription.hybrid_connection_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">hybrid_connection_endpoint</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridEventSubscription.included_event_types">
<code class="descname">included_event_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridEventSubscription.included_event_types" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of applicable event types that need to be part of the event subscription.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridEventSubscription.labels">
<code class="descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridEventSubscription.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of labels to assign to the event subscription.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridEventSubscription.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridEventSubscription.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridEventSubscription.retry_policy">
<code class="descname">retry_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridEventSubscription.retry_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">retry_policy</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridEventSubscription.scope">
<code class="descname">scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridEventSubscription.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridEventSubscription.storage_blob_dead_letter_destination">
<code class="descname">storage_blob_dead_letter_destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridEventSubscription.storage_blob_dead_letter_destination" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_blob_dead_letter_destination</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridEventSubscription.storage_queue_endpoint">
<code class="descname">storage_queue_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridEventSubscription.storage_queue_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_queue_endpoint</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridEventSubscription.subject_filter">
<code class="descname">subject_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridEventSubscription.subject_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">subject_filter</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridEventSubscription.topic_name">
<code class="descname">topic_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridEventSubscription.topic_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the topic to associate with the event subscription.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridEventSubscription.webhook_endpoint">
<code class="descname">webhook_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridEventSubscription.webhook_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">webhook_endpoint</span></code> block as defined below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventGridEventSubscription.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventGridEventSubscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventGridEventSubscription.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventGridEventSubscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventGridTopic">
<em class="property">class </em><code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">EventGridTopic</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EventGrid Topic</p>
<blockquote>
<div><strong>Note:</strong> at this time EventGrid Topic’s are only available in a limited number of regions.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventGrid Topic resource. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventGrid Topic exists. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridTopic.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Endpoint associated with the EventGrid Topic.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridTopic.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridTopic.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventGrid Topic resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridTopic.primary_access_key">
<code class="descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Shared Access Key associated with the EventGrid Topic.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridTopic.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the EventGrid Topic exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridTopic.secondary_access_key">
<code class="descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Shared Access Key associated with the EventGrid Topic.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventGridTopic.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventGridTopic.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventGridTopic.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventGridTopic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHub">
<em class="property">class </em><code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">EventHub</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>capture_description=None</em>, <em>location=None</em>, <em>message_retention=None</em>, <em>name=None</em>, <em>namespace_name=None</em>, <em>partition_count=None</em>, <em>resource_group_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHub" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Event Hubs as a nested resource within a Event Hubs namespace.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>capture_description</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">capture_description</span></code> block as defined below.</li>
<li><strong>message_retention</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of days to retain the events for this Event Hub. Needs to be between 1 and 7 days; or 1 day when using a Basic SKU for the parent EventHub Namespace.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.</li>
<li><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.</li>
<li><strong>partition_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the current number of shards on the Event Hub. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventHub’s parent Namespace exists. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHub.capture_description">
<code class="descname">capture_description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.capture_description" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">capture_description</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHub.message_retention">
<code class="descname">message_retention</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.message_retention" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of days to retain the events for this Event Hub. Needs to be between 1 and 7 days; or 1 day when using a Basic SKU for the parent EventHub Namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHub.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHub.namespace_name">
<code class="descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHub.partition_count">
<code class="descname">partition_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.partition_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the current number of shards on the Event Hub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHub.partition_ids">
<code class="descname">partition_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.partition_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifiers for partitions created for Event Hubs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHub.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the EventHub’s parent Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventHub.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHub.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHub.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">EventHubAuthorizationRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>eventhub_name=None</em>, <em>listen=None</em>, <em>location=None</em>, <em>manage=None</em>, <em>name=None</em>, <em>namespace_name=None</em>, <em>resource_group_name=None</em>, <em>send=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Event Hubs authorization Rule within an Event Hub.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub. Changing this forces a new resource to be created.</li>
<li><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have permissions to Listen to the Event Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have permissions to Manage to the Event Hub? When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Authorization Rule resource. Changing this forces a new resource to be created.</li>
<li><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.</li>
<li><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have permissions to Send to the Event Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.eventhub_name">
<code class="descname">eventhub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.eventhub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.listen">
<code class="descname">listen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.listen" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have permissions to Listen to the Event Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.manage">
<code class="descname">manage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.manage" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have permissions to Manage to the Event Hub? When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub Authorization Rule resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.namespace_name">
<code class="descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.primary_connection_string">
<code class="descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Connection String for the Event Hubs authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.primary_key">
<code class="descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Key for the Event Hubs authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.secondary_connection_string">
<code class="descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Connection String for the Event Hubs authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.secondary_key">
<code class="descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Key for the Event Hubs authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.send">
<code class="descname">send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.send" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have permissions to Send to the Event Hub? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHubAuthorizationRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubAuthorizationRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHubConsumerGroup">
<em class="property">class </em><code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">EventHubConsumerGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>eventhub_name=None</em>, <em>location=None</em>, <em>name=None</em>, <em>namespace_name=None</em>, <em>resource_group_name=None</em>, <em>user_metadata=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubConsumerGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Event Hubs Consumer Group as a nested resource within an Event Hub.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Consumer Group resource. Changing this forces a new resource to be created.</li>
<li><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventHub Consumer Group’s grandparent Namespace exists. Changing this forces a new resource to be created.</li>
<li><strong>user_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the user metadata.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubConsumerGroup.eventhub_name">
<code class="descname">eventhub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubConsumerGroup.eventhub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubConsumerGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubConsumerGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub Consumer Group resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubConsumerGroup.namespace_name">
<code class="descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubConsumerGroup.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubConsumerGroup.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubConsumerGroup.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the EventHub Consumer Group’s grandparent Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubConsumerGroup.user_metadata">
<code class="descname">user_metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubConsumerGroup.user_metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the user metadata.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventHubConsumerGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubConsumerGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHubConsumerGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubConsumerGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHubNamespace">
<em class="property">class </em><code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">EventHubNamespace</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>auto_inflate_enabled=None</em>, <em>capacity=None</em>, <em>kafka_enabled=None</em>, <em>location=None</em>, <em>maximum_throughput_units=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage an EventHub Namespace.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>auto_inflate_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is Auto Inflate enabled for the EventHub Namespace?</li>
<li><strong>capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the Capacity / Throughput Units for a <code class="docutils literal notranslate"><span class="pre">Standard</span></code> SKU namespace. Valid values range from 1 - 20.</li>
<li><strong>kafka_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is Kafka enabled for the EventHub Namespace? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>maximum_throughput_units</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from 1 - 20.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines which tier to use. Valid options are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.auto_inflate_enabled">
<code class="descname">auto_inflate_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.auto_inflate_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is Auto Inflate enabled for the EventHub Namespace?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.capacity">
<code class="descname">capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Capacity / Throughput Units for a <code class="docutils literal notranslate"><span class="pre">Standard</span></code> SKU namespace. Valid values range from 1 - 20.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.default_primary_connection_string">
<code class="descname">default_primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.default_primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string for the authorization
rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.default_primary_key">
<code class="descname">default_primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.default_primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.default_secondary_connection_string">
<code class="descname">default_secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.default_secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string for the
authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.default_secondary_key">
<code class="descname">default_secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.default_secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.kafka_enabled">
<code class="descname">kafka_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.kafka_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is Kafka enabled for the EventHub Namespace? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.maximum_throughput_units">
<code class="descname">maximum_throughput_units</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.maximum_throughput_units" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum number of throughput units when Auto Inflate is Enabled. Valid values range from 1 - 20.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines which tier to use. Valid options are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespace.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventHubNamespace.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHubNamespace.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">EventHubNamespaceAuthorizationRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>listen=None</em>, <em>location=None</em>, <em>manage=None</em>, <em>name=None</em>, <em>namespace_name=None</em>, <em>resource_group_name=None</em>, <em>send=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Authorization Rule for an Event Hub Namespace.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants listen access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants manage access to this this Authorization Rule. When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.</li>
<li><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.</li>
<li><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants send access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.listen">
<code class="descname">listen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.listen" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants listen access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.manage">
<code class="descname">manage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.manage" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants manage access to this this Authorization Rule. When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.namespace_name">
<code class="descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.primary_connection_string">
<code class="descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Connection String for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.primary_key">
<code class="descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Key for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the EventHub Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.secondary_connection_string">
<code class="descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Connection String for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.secondary_key">
<code class="descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Key for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.send">
<code class="descname">send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.send" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants send access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.EventHubNamespaceAuthorizationRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">GetEventhubNamespaceResult</code><span class="sig-paren">(</span><em>auto_inflate_enabled=None</em>, <em>capacity=None</em>, <em>default_primary_connection_string=None</em>, <em>default_primary_key=None</em>, <em>default_secondary_connection_string=None</em>, <em>default_secondary_key=None</em>, <em>kafka_enabled=None</em>, <em>location=None</em>, <em>maximum_throughput_units=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEventhubNamespace.</p>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.auto_inflate_enabled">
<code class="descname">auto_inflate_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.auto_inflate_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is Auto Inflate enabled for the EventHub Namespace?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.capacity">
<code class="descname">capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The Capacity / Throughput Units for a <code class="docutils literal notranslate"><span class="pre">Standard</span></code> SKU namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.default_primary_connection_string">
<code class="descname">default_primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.default_primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string for the authorization
rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.default_primary_key">
<code class="descname">default_primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.default_primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.default_secondary_connection_string">
<code class="descname">default_secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.default_secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string for the
authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.default_secondary_key">
<code class="descname">default_secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.default_secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the EventHub Namespace exists</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.maximum_throughput_units">
<code class="descname">maximum_throughput_units</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.maximum_throughput_units" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum number of throughput units when Auto Inflate is Enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines which tier to use.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the EventHub Namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetEventhubNamespaceResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetEventhubNamespaceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">GetServiceBusNamespaceResult</code><span class="sig-paren">(</span><em>capacity=None</em>, <em>default_primary_connection_string=None</em>, <em>default_primary_key=None</em>, <em>default_secondary_connection_string=None</em>, <em>default_secondary_key=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServiceBusNamespace.</p>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.capacity">
<code class="descname">capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The capacity of the ServiceBus Namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.default_primary_connection_string">
<code class="descname">default_primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.default_primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string for the authorization
rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.default_primary_key">
<code class="descname">default_primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.default_primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.default_secondary_connection_string">
<code class="descname">default_secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.default_secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string for the
authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.default_secondary_key">
<code class="descname">default_secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.default_secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the Resource Group in which the ServiceBus Namespace exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The Tier used for the ServiceBus Namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.GetServiceBusNamespaceResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.GetServiceBusNamespaceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.eventhub.Namespace">
<em class="property">class </em><code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">Namespace</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>capacity=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a ServiceBus Namespace.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the capacity. When <code class="docutils literal notranslate"><span class="pre">sku</span></code> is <code class="docutils literal notranslate"><span class="pre">Premium</span></code> can be <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code> or <code class="docutils literal notranslate"><span class="pre">4</span></code>. When <code class="docutils literal notranslate"><span class="pre">sku</span></code> is <code class="docutils literal notranslate"><span class="pre">Basic</span></code> or <code class="docutils literal notranslate"><span class="pre">Standard</span></code> can be <code class="docutils literal notranslate"><span class="pre">0</span></code> only.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Namespace resource . Changing this forces a
new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the namespace.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines which tier to use. Options are basic, standard or premium.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.capacity">
<code class="descname">capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the capacity. When <code class="docutils literal notranslate"><span class="pre">sku</span></code> is <code class="docutils literal notranslate"><span class="pre">Premium</span></code> can be <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code> or <code class="docutils literal notranslate"><span class="pre">4</span></code>. When <code class="docutils literal notranslate"><span class="pre">sku</span></code> is <code class="docutils literal notranslate"><span class="pre">Basic</span></code> or <code class="docutils literal notranslate"><span class="pre">Standard</span></code> can be <code class="docutils literal notranslate"><span class="pre">0</span></code> only.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.default_primary_connection_string">
<code class="descname">default_primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.default_primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary connection string for the authorization
rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.default_primary_key">
<code class="descname">default_primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.default_primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The primary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.default_secondary_connection_string">
<code class="descname">default_secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.default_secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary connection string for the
authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.default_secondary_key">
<code class="descname">default_secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.default_secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secondary access key for the authorization rule <code class="docutils literal notranslate"><span class="pre">RootManageSharedAccessKey</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Namespace resource . Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the namespace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines which tier to use. Options are basic, standard or premium.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Namespace.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.Namespace.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.Namespace.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Namespace.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">NamespaceAuthorizationRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>listen=None</em>, <em>manage=None</em>, <em>name=None</em>, <em>namespace_name=None</em>, <em>resource_group_name=None</em>, <em>send=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a ServiceBus Namespace authorization Rule within a ServiceBus.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants listen access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants manage access to this this Authorization Rule. When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.</li>
<li><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.</li>
<li><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants send access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.listen">
<code class="descname">listen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.listen" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants listen access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.manage">
<code class="descname">manage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.manage" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants manage access to this this Authorization Rule. When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Namespace Authorization Rule resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.namespace_name">
<code class="descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.primary_connection_string">
<code class="descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Connection String for the ServiceBus Namespace authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.primary_key">
<code class="descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Key for the ServiceBus Namespace authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.secondary_connection_string">
<code class="descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Connection String for the ServiceBus Namespace authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.secondary_key">
<code class="descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Key for the ServiceBus Namespace authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.send">
<code class="descname">send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.send" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants send access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.NamespaceAuthorizationRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.NamespaceAuthorizationRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.Queue">
<em class="property">class </em><code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">Queue</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>auto_delete_on_idle=None</em>, <em>dead_lettering_on_message_expiration=None</em>, <em>default_message_ttl=None</em>, <em>duplicate_detection_history_time_window=None</em>, <em>enable_batched_operations=None</em>, <em>enable_express=None</em>, <em>enable_partitioning=None</em>, <em>location=None</em>, <em>lock_duration=None</em>, <em>max_delivery_count=None</em>, <em>max_size_in_megabytes=None</em>, <em>name=None</em>, <em>namespace_name=None</em>, <em>requires_duplicate_detection=None</em>, <em>requires_session=None</em>, <em>resource_group_name=None</em>, <em>support_ordering=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Queue" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a ServiceBus Queue.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>auto_delete_on_idle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.</li>
<li><strong>dead_lettering_on_message_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>default_message_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.</li>
<li><strong>duplicate_detection_history_time_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (<code class="docutils literal notranslate"><span class="pre">PT10M</span></code>)</li>
<li><strong>enable_express</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code> for Basic and Standard. For Premium, it MUST
be set to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>enable_partitioning</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code> for Basic and Standard. For Premium, it MUST
be set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.</li>
<li><strong>lock_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (<code class="docutils literal notranslate"><span class="pre">PT1M</span></code>)</li>
<li><strong>max_delivery_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer value which controls when a message is automatically deadlettered. Defaults to <code class="docutils literal notranslate"><span class="pre">10</span></code>.</li>
<li><strong>max_size_in_megabytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer value which controls the size of
memory allocated for the queue. For supported values see the “Queue/topic size”
section of <a class="reference external" href="https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas">this document</a>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.</li>
<li><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.</li>
<li><strong>requires_duplicate_detection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>requires_session</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.auto_delete_on_idle">
<code class="descname">auto_delete_on_idle</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.auto_delete_on_idle" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.dead_lettering_on_message_expiration">
<code class="descname">dead_lettering_on_message_expiration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.dead_lettering_on_message_expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.default_message_ttl">
<code class="descname">default_message_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.default_message_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.duplicate_detection_history_time_window">
<code class="descname">duplicate_detection_history_time_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.duplicate_detection_history_time_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (<code class="docutils literal notranslate"><span class="pre">PT10M</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.enable_express">
<code class="descname">enable_express</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.enable_express" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code> for Basic and Standard. For Premium, it MUST
be set to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.enable_partitioning">
<code class="descname">enable_partitioning</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.enable_partitioning" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code> for Basic and Standard. For Premium, it MUST
be set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.lock_duration">
<code class="descname">lock_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.lock_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (<code class="docutils literal notranslate"><span class="pre">PT1M</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.max_delivery_count">
<code class="descname">max_delivery_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.max_delivery_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer value which controls when a message is automatically deadlettered. Defaults to <code class="docutils literal notranslate"><span class="pre">10</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.max_size_in_megabytes">
<code class="descname">max_size_in_megabytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.max_size_in_megabytes" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer value which controls the size of
memory allocated for the queue. For supported values see the “Queue/topic size”
section of <a class="reference external" href="https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas">this document</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.namespace_name">
<code class="descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.requires_duplicate_detection">
<code class="descname">requires_duplicate_detection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.requires_duplicate_detection" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.requires_session">
<code class="descname">requires_session</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.requires_session" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Queue.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Queue.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.Queue.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Queue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.Queue.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Queue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">QueueAuthorizationRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>listen=None</em>, <em>manage=None</em>, <em>name=None</em>, <em>namespace_name=None</em>, <em>queue_name=None</em>, <em>resource_group_name=None</em>, <em>send=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Authorization Rule for a ServiceBus Queue.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have Listen permissions to the ServiceBus Queue? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have Manage permissions to the ServiceBus Queue? When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.</li>
<li><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Namespace in which the Queue exists. Changing this forces a new resource to be created.</li>
<li><strong>queue_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Queue. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.</li>
<li><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Does this Authorization Rule have Send permissions to the ServiceBus Queue? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.listen">
<code class="descname">listen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.listen" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have Listen permissions to the ServiceBus Queue? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.manage">
<code class="descname">manage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.manage" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have Manage permissions to the ServiceBus Queue? When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.namespace_name">
<code class="descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Namespace in which the Queue exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.primary_connection_string">
<code class="descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Connection String for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.primary_key">
<code class="descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Key for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.queue_name">
<code class="descname">queue_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.queue_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Queue. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.secondary_connection_string">
<code class="descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Connection String for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.secondary_key">
<code class="descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Key for the Authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.send">
<code class="descname">send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.send" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Authorization Rule have Send permissions to the ServiceBus Queue? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.QueueAuthorizationRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.QueueAuthorizationRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.Subscription">
<em class="property">class </em><code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">Subscription</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>auto_delete_on_idle=None</em>, <em>dead_lettering_on_filter_evaluation_exceptions=None</em>, <em>dead_lettering_on_message_expiration=None</em>, <em>default_message_ttl=None</em>, <em>enable_batched_operations=None</em>, <em>forward_to=None</em>, <em>location=None</em>, <em>lock_duration=None</em>, <em>max_delivery_count=None</em>, <em>name=None</em>, <em>namespace_name=None</em>, <em>requires_session=None</em>, <em>resource_group_name=None</em>, <em>topic_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Subscription" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a ServiceBus Subscription.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>auto_delete_on_idle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The idle interval after which the
Subscription is automatically deleted, minimum of 5 minutes. Provided in the
TimeSpan format.</li>
<li><strong>dead_lettering_on_message_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls
whether the Subscription has dead letter support when a message expires. Defaults
to false.</li>
<li><strong>default_message_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The TTL of messages sent to this Subscription
if no TTL value is set on the message itself. Provided in the TimeSpan
format.</li>
<li><strong>enable_batched_operations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether the
Subscription supports batched operations. Defaults to false.</li>
<li><strong>forward_to</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a Queue or Topic to automatically forward 
messages to.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.</li>
<li><strong>lock_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The lock duration for the subscription, maximum
supported value is 5 minutes. Defaults to 1 minute.</li>
<li><strong>max_delivery_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of deliveries.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Subscription resource.
Changing this forces a new resource to be created.</li>
<li><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Namespace to create
this Subscription in. Changing this forces a new resource to be created.</li>
<li><strong>requires_session</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether this Subscription
supports the concept of a session. Defaults to false. Changing this forces a
new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</li>
<li><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Topic to create
this Subscription in. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.auto_delete_on_idle">
<code class="descname">auto_delete_on_idle</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.auto_delete_on_idle" title="Permalink to this definition">¶</a></dt>
<dd><p>The idle interval after which the
Subscription is automatically deleted, minimum of 5 minutes. Provided in the
TimeSpan format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.dead_lettering_on_message_expiration">
<code class="descname">dead_lettering_on_message_expiration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.dead_lettering_on_message_expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls
whether the Subscription has dead letter support when a message expires. Defaults
to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.default_message_ttl">
<code class="descname">default_message_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.default_message_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The TTL of messages sent to this Subscription
if no TTL value is set on the message itself. Provided in the TimeSpan
format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.enable_batched_operations">
<code class="descname">enable_batched_operations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.enable_batched_operations" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether the
Subscription supports batched operations. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.forward_to">
<code class="descname">forward_to</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.forward_to" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a Queue or Topic to automatically forward 
messages to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.lock_duration">
<code class="descname">lock_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.lock_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The lock duration for the subscription, maximum
supported value is 5 minutes. Defaults to 1 minute.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.max_delivery_count">
<code class="descname">max_delivery_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.max_delivery_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of deliveries.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Subscription resource.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.namespace_name">
<code class="descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Namespace to create
this Subscription in. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.requires_session">
<code class="descname">requires_session</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.requires_session" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether this Subscription
supports the concept of a session. Defaults to false. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Subscription.topic_name">
<code class="descname">topic_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.topic_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Topic to create
this Subscription in. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.Subscription.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.Subscription.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Subscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.SubscriptionRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">SubscriptionRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>action=None</em>, <em>correlation_filter=None</em>, <em>filter_type=None</em>, <em>name=None</em>, <em>namespace_name=None</em>, <em>resource_group_name=None</em>, <em>sql_filter=None</em>, <em>subscription_name=None</em>, <em>topic_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a ServiceBus Subscription Rule.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Represents set of actions written in SQL language-based syntax that is performed against a BrokeredMessage.</li>
<li><strong>correlation_filter</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">correlation_filter</span></code> block as documented below to be evaluated against a BrokeredMessage. Required when <code class="docutils literal notranslate"><span class="pre">filter_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">CorrelationFilter</span></code>.</li>
<li><strong>filter_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of filter to be applied to a BrokeredMessage. Possible values are <code class="docutils literal notranslate"><span class="pre">SqlFilter</span></code> and <code class="docutils literal notranslate"><span class="pre">CorrelationFilter</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Subscription Rule. Changing this forces a new resource to be created.</li>
<li><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Namespace in which the ServiceBus Topic exists. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in the ServiceBus Namespace exists. Changing this forces a new resource to be created.</li>
<li><strong>sql_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Represents a filter written in SQL language-based syntax that to be evaluated against a BrokeredMessage. Required when <code class="docutils literal notranslate"><span class="pre">filter_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">SqlFilter</span></code>.</li>
<li><strong>subscription_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Subscription in which this Rule should be created. Changing this forces a new resource to be created.</li>
<li><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Topic in which the ServiceBus Subscription exists. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.SubscriptionRule.action">
<code class="descname">action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.action" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents set of actions written in SQL language-based syntax that is performed against a BrokeredMessage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.SubscriptionRule.correlation_filter">
<code class="descname">correlation_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.correlation_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">correlation_filter</span></code> block as documented below to be evaluated against a BrokeredMessage. Required when <code class="docutils literal notranslate"><span class="pre">filter_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">CorrelationFilter</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.SubscriptionRule.filter_type">
<code class="descname">filter_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.filter_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of filter to be applied to a BrokeredMessage. Possible values are <code class="docutils literal notranslate"><span class="pre">SqlFilter</span></code> and <code class="docutils literal notranslate"><span class="pre">CorrelationFilter</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.SubscriptionRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Subscription Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.SubscriptionRule.namespace_name">
<code class="descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Namespace in which the ServiceBus Topic exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.SubscriptionRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.SubscriptionRule.sql_filter">
<code class="descname">sql_filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.sql_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents a filter written in SQL language-based syntax that to be evaluated against a BrokeredMessage. Required when <code class="docutils literal notranslate"><span class="pre">filter_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">SqlFilter</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.SubscriptionRule.subscription_name">
<code class="descname">subscription_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.subscription_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Subscription in which this Rule should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.SubscriptionRule.topic_name">
<code class="descname">topic_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.topic_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Topic in which the ServiceBus Subscription exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.SubscriptionRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.SubscriptionRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.SubscriptionRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.Topic">
<em class="property">class </em><code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">Topic</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>auto_delete_on_idle=None</em>, <em>default_message_ttl=None</em>, <em>duplicate_detection_history_time_window=None</em>, <em>enable_batched_operations=None</em>, <em>enable_express=None</em>, <em>enable_filtering_messages_before_publishing=None</em>, <em>enable_partitioning=None</em>, <em>location=None</em>, <em>max_size_in_megabytes=None</em>, <em>name=None</em>, <em>namespace_name=None</em>, <em>requires_duplicate_detection=None</em>, <em>resource_group_name=None</em>, <em>status=None</em>, <em>support_ordering=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Topic" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a ServiceBus Topic.</p>
<p><strong>Note</strong> Topics can only be created in Namespaces with an SKU of <code class="docutils literal notranslate"><span class="pre">standard</span></code> or higher.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>auto_delete_on_idle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration of the idle interval after which the
Topic is automatically deleted, minimum of 5 minutes.</li>
<li><strong>default_message_ttl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration of TTL of messages sent to this topic if no
TTL value is set on the message itself.</li>
<li><strong>duplicate_detection_history_time_window</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration during which
duplicates can be detected. Defaults to 10 minutes. (<code class="docutils literal notranslate"><span class="pre">PT10M</span></code>)</li>
<li><strong>enable_batched_operations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls if server-side
batched operations are enabled. Defaults to false.</li>
<li><strong>enable_express</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether Express Entities
are enabled. An express topic holds a message in memory temporarily before writing
it to persistent storage. Defaults to false.</li>
<li><strong>enable_partitioning</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether to enable
the topic to be partitioned across multiple message brokers. Defaults to false.
Changing this forces a new resource to be created.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.</li>
<li><strong>max_size_in_megabytes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>Integer value which controls the size of
memory allocated for the topic. For supported values see the “Queue/topic size”
section of <a class="reference external" href="https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas">this document</a>.</p>
</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Topic resource. Changing this forces a
new resource to be created.</li>
<li><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ServiceBus Namespace to create
this topic in. Changing this forces a new resource to be created.</li>
<li><strong>requires_duplicate_detection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether
the Topic requires duplicate detection. Defaults to false. Changing this forces
a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</li>
<li><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Status of the Service Bus Topic. Acceptable values are <code class="docutils literal notranslate"><span class="pre">Active</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Active</span></code>.</li>
<li><strong>support_ordering</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls whether the Topic
supports ordering. Defaults to false.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.auto_delete_on_idle">
<code class="descname">auto_delete_on_idle</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.auto_delete_on_idle" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration of the idle interval after which the
Topic is automatically deleted, minimum of 5 minutes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.default_message_ttl">
<code class="descname">default_message_ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.default_message_ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration of TTL of messages sent to this topic if no
TTL value is set on the message itself.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.duplicate_detection_history_time_window">
<code class="descname">duplicate_detection_history_time_window</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.duplicate_detection_history_time_window" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration during which
duplicates can be detected. Defaults to 10 minutes. (<code class="docutils literal notranslate"><span class="pre">PT10M</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.enable_batched_operations">
<code class="descname">enable_batched_operations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.enable_batched_operations" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls if server-side
batched operations are enabled. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.enable_express">
<code class="descname">enable_express</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.enable_express" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether Express Entities
are enabled. An express topic holds a message in memory temporarily before writing
it to persistent storage. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.enable_partitioning">
<code class="descname">enable_partitioning</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.enable_partitioning" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether to enable
the topic to be partitioned across multiple message brokers. Defaults to false.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.max_size_in_megabytes">
<code class="descname">max_size_in_megabytes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.max_size_in_megabytes" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer value which controls the size of
memory allocated for the topic. For supported values see the “Queue/topic size”
section of <a class="reference external" href="https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas">this document</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Topic resource. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.namespace_name">
<code class="descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ServiceBus Namespace to create
this topic in. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.requires_duplicate_detection">
<code class="descname">requires_duplicate_detection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.requires_duplicate_detection" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether
the Topic requires duplicate detection. Defaults to false. Changing this forces
a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The Status of the Service Bus Topic. Acceptable values are <code class="docutils literal notranslate"><span class="pre">Active</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Active</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.Topic.support_ordering">
<code class="descname">support_ordering</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.Topic.support_ordering" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls whether the Topic
supports ordering. Defaults to false.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.Topic.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Topic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.Topic.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.Topic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">TopicAuthorizationRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>listen=None</em>, <em>manage=None</em>, <em>name=None</em>, <em>namespace_name=None</em>, <em>resource_group_name=None</em>, <em>send=None</em>, <em>topic_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a ServiceBus Topic authorization Rule within a ServiceBus Topic.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>listen</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants listen access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>manage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants manage access to this this Authorization Rule. When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Topic Authorization Rule resource. Changing this forces a new resource to be created.</li>
<li><strong>namespace_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.</li>
<li><strong>send</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Grants send access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the ServiceBus Topic. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.listen">
<code class="descname">listen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.listen" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants listen access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.manage">
<code class="descname">manage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.manage" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants manage access to this this Authorization Rule. When this property is <code class="docutils literal notranslate"><span class="pre">true</span></code> - both <code class="docutils literal notranslate"><span class="pre">listen</span></code> and <code class="docutils literal notranslate"><span class="pre">send</span></code> must be too. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Topic Authorization Rule resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.namespace_name">
<code class="descname">namespace_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.namespace_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Namespace. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.primary_connection_string">
<code class="descname">primary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.primary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Connection String for the ServiceBus Topic authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.primary_key">
<code class="descname">primary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.primary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Key for the ServiceBus Topic authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.secondary_connection_string">
<code class="descname">secondary_connection_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.secondary_connection_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Connection String for the ServiceBus Topic authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.secondary_key">
<code class="descname">secondary_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.secondary_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Key for the ServiceBus Topic authorization Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.send">
<code class="descname">send</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.send" title="Permalink to this definition">¶</a></dt>
<dd><p>Grants send access to this this Authorization Rule. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.topic_name">
<code class="descname">topic_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.topic_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the ServiceBus Topic. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.TopicAuthorizationRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.TopicAuthorizationRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.eventhub.get_eventhub_namespace">
<code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">get_eventhub_namespace</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.get_eventhub_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing EventHub Namespace.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.eventhub.get_service_bus_namespace">
<code class="descclassname">pulumi_azure.eventhub.</code><code class="descname">get_service_bus_namespace</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.eventhub.get_service_bus_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing ServiceBus Namespace.</p>
</dd></dl>

</div>
