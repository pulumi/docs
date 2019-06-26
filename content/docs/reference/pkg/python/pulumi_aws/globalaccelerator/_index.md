---
---

<div class="section" id="module-pulumi_aws.globalaccelerator">
<span id="globalaccelerator"></span><h1>globalaccelerator<a class="headerlink" href="#module-pulumi_aws.globalaccelerator" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.globalaccelerator.Accelerator">
<em class="property">class </em><code class="descclassname">pulumi_aws.globalaccelerator.</code><code class="descname">Accelerator</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>attributes=None</em>, <em>enabled=None</em>, <em>ip_address_type=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Global Accelerator accelerator.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>attributes</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The attributes of the accelerator. Fields documented below.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the accelerator is enabled. The value is true or false. The default value is true.</li>
<li><strong>ip_address_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value for the address type must be <code class="docutils literal notranslate"><span class="pre">IPV4</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the accelerator.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Accelerator.attributes">
<code class="descname">attributes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.attributes" title="Permalink to this definition">¶</a></dt>
<dd><p>The attributes of the accelerator. Fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Accelerator.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the accelerator is enabled. The value is true or false. The default value is true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Accelerator.ip_address_type">
<code class="descname">ip_address_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.ip_address_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The value for the address type must be <code class="docutils literal notranslate"><span class="pre">IPV4</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Accelerator.ip_sets">
<code class="descname">ip_sets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.ip_sets" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address set associated with the accelerator.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Accelerator.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the accelerator.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.globalaccelerator.Accelerator.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.globalaccelerator.Accelerator.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.Accelerator.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.globalaccelerator.EndpointGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.globalaccelerator.</code><code class="descname">EndpointGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>endpoint_configurations=None</em>, <em>endpoint_group_region=None</em>, <em>health_check_interval_seconds=None</em>, <em>health_check_path=None</em>, <em>health_check_port=None</em>, <em>health_check_protocol=None</em>, <em>listener_arn=None</em>, <em>threshold_count=None</em>, <em>traffic_dial_percentage=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Global Accelerator endpoint group.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>endpoint_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of endpoint objects. Fields documented below.</li>
<li><strong>health_check_interval_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time—10 seconds or 30 seconds—between each health check for an endpoint. The default value is 30.</li>
<li><strong>health_check_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If the protocol is HTTP/S, then this specifies the path that is the destination for health check targets. The default value is slash (/).</li>
<li><strong>health_check_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default port is the listener port that this endpoint group is associated with. If listener port is a list of ports, Global Accelerator uses the first port in the list.</li>
<li><strong>health_check_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default value is TCP.</li>
<li><strong>listener_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the listener.</li>
<li><strong>threshold_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.</li>
<li><strong>traffic_dial_percentage</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The percentage of traffic to send to an AWS Region. Additional traffic is distributed to other endpoint groups for this listener. The default value is 100.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.endpoint_configurations">
<code class="descname">endpoint_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.endpoint_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of endpoint objects. Fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.health_check_interval_seconds">
<code class="descname">health_check_interval_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.health_check_interval_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The time—10 seconds or 30 seconds—between each health check for an endpoint. The default value is 30.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.health_check_path">
<code class="descname">health_check_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.health_check_path" title="Permalink to this definition">¶</a></dt>
<dd><p>If the protocol is HTTP/S, then this specifies the path that is the destination for health check targets. The default value is slash (/).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.health_check_port">
<code class="descname">health_check_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.health_check_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default port is the listener port that this endpoint group is associated with. If listener port is a list of ports, Global Accelerator uses the first port in the list.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.health_check_protocol">
<code class="descname">health_check_protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.health_check_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol that AWS Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default value is TCP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.listener_arn">
<code class="descname">listener_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.listener_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the listener.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.threshold_count">
<code class="descname">threshold_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.threshold_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.traffic_dial_percentage">
<code class="descname">traffic_dial_percentage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.traffic_dial_percentage" title="Permalink to this definition">¶</a></dt>
<dd><p>The percentage of traffic to send to an AWS Region. Additional traffic is distributed to other endpoint groups for this listener. The default value is 100.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.globalaccelerator.EndpointGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.EndpointGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.globalaccelerator.Listener">
<em class="property">class </em><code class="descclassname">pulumi_aws.globalaccelerator.</code><code class="descname">Listener</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>accelerator_arn=None</em>, <em>client_affinity=None</em>, <em>port_ranges=None</em>, <em>protocol=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.Listener" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Global Accelerator listener.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>accelerator_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of your accelerator.</li>
<li><strong>client_affinity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Direct all requests from a user to the same endpoint. Valid values are <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">SOURCE_IP</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">NONE</span></code>. If <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, Global Accelerator uses the “five-tuple” properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If <code class="docutils literal notranslate"><span class="pre">SOURCE_IP</span></code>, Global Accelerator uses the “two-tuple” properties of source (client) IP address and destination IP address to select the hash value.</li>
<li><strong>port_ranges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of port ranges for the connections from clients to the accelerator. Fields documented below.</li>
<li><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol for the connections from clients to the accelerator. Valid values are <code class="docutils literal notranslate"><span class="pre">TCP</span></code>, <code class="docutils literal notranslate"><span class="pre">UDP</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Listener.accelerator_arn">
<code class="descname">accelerator_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Listener.accelerator_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of your accelerator.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Listener.client_affinity">
<code class="descname">client_affinity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Listener.client_affinity" title="Permalink to this definition">¶</a></dt>
<dd><p>Direct all requests from a user to the same endpoint. Valid values are <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">SOURCE_IP</span></code>. Default: <code class="docutils literal notranslate"><span class="pre">NONE</span></code>. If <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, Global Accelerator uses the “five-tuple” properties of source IP address, source port, destination IP address, destination port, and protocol to select the hash value. If <code class="docutils literal notranslate"><span class="pre">SOURCE_IP</span></code>, Global Accelerator uses the “two-tuple” properties of source (client) IP address and destination IP address to select the hash value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Listener.port_ranges">
<code class="descname">port_ranges</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Listener.port_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of port ranges for the connections from clients to the accelerator. Fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.globalaccelerator.Listener.protocol">
<code class="descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.globalaccelerator.Listener.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol for the connections from clients to the accelerator. Valid values are <code class="docutils literal notranslate"><span class="pre">TCP</span></code>, <code class="docutils literal notranslate"><span class="pre">UDP</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.globalaccelerator.Listener.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.Listener.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.globalaccelerator.Listener.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.globalaccelerator.Listener.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
