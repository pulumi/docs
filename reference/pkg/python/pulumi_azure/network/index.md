<div class="section" id="module-pulumi_azure.network">
<span id="network"></span><h1>network<a class="headerlink" href="#module-pulumi_azure.network" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.network.ApplicationGateway">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">ApplicationGateway</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>authentication_certificates=None</em>, <em>backend_address_pools=None</em>, <em>backend_http_settings=None</em>, <em>disabled_ssl_protocols=None</em>, <em>frontend_ip_configurations=None</em>, <em>frontend_ports=None</em>, <em>gateway_ip_configurations=None</em>, <em>http_listeners=None</em>, <em>location=None</em>, <em>name=None</em>, <em>probes=None</em>, <em>request_routing_rules=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>ssl_certificates=None</em>, <em>tags=None</em>, <em>url_path_maps=None</em>, <em>waf_configuration=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ApplicationGateway resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] authentication_certificates
:param pulumi.Input[list] backend_address_pools
:param pulumi.Input[list] backend_http_settings
:param pulumi.Input[list] disabled_ssl_protocols
:param pulumi.Input[list] frontend_ip_configurations
:param pulumi.Input[list] frontend_ports
:param pulumi.Input[list] gateway_ip_configurations
:param pulumi.Input[list] http_listeners
:param pulumi.Input[str] location
:param pulumi.Input[str] name
:param pulumi.Input[list] probes
:param pulumi.Input[list] request_routing_rules
:param pulumi.Input[str] resource_group_name
:param pulumi.Input[dict] sku
:param pulumi.Input[list] ssl_certificates
:param pulumi.Input[dict] tags
:param pulumi.Input[list] url_path_maps
:param pulumi.Input[dict] waf_configuration</p>
<dl class="method">
<dt id="pulumi_azure.network.ApplicationGateway.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ApplicationGateway.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ApplicationSecurityGroup">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">ApplicationSecurityGroup</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ApplicationSecurityGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage an Application Security Group.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Application Security Group. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Application Security Group.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationSecurityGroup.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationSecurityGroup.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationSecurityGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationSecurityGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Application Security Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationSecurityGroup.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationSecurityGroup.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Application Security Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationSecurityGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationSecurityGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.ApplicationSecurityGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ApplicationSecurityGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ApplicationSecurityGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ApplicationSecurityGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ExpressRouteCircuit">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">ExpressRouteCircuit</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>allow_classic_operations=None</em>, <em>bandwidth_in_mbps=None</em>, <em>location=None</em>, <em>name=None</em>, <em>peering_location=None</em>, <em>resource_group_name=None</em>, <em>service_provider_name=None</em>, <em>sku=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an ExpressRoute circuit.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allow_classic_operations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow the circuit to interact with classic (RDFE) resources. The default value is <cite>false</cite>.</li>
<li><strong>bandwidth_in_mbps</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The bandwidth in Mbps of the circuit being created.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ExpressRoute circuit. Changing this forces a new resource to be created.</li>
<li><strong>peering_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the peering location and <strong>not</strong> the Azure resource location.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the ExpressRoute circuit. Changing this forces a new resource to be created.</li>
<li><strong>service_provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ExpressRoute Service Provider.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>sku</cite> block for the ExpressRoute circuit as documented below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.allow_classic_operations">
<code class="descname">allow_classic_operations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.allow_classic_operations" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow the circuit to interact with classic (RDFE) resources. The default value is <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.bandwidth_in_mbps">
<code class="descname">bandwidth_in_mbps</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.bandwidth_in_mbps" title="Permalink to this definition">¶</a></dt>
<dd><p>The bandwidth in Mbps of the circuit being created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ExpressRoute circuit. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.peering_location">
<code class="descname">peering_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.peering_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the peering location and <strong>not</strong> the Azure resource location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the ExpressRoute circuit. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.service_key">
<code class="descname">service_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.service_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The string needed by the service provider to provision the ExpressRoute circuit.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.service_provider_name">
<code class="descname">service_provider_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.service_provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ExpressRoute Service Provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.service_provider_provisioning_state">
<code class="descname">service_provider_provisioning_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.service_provider_provisioning_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The ExpressRoute circuit provisioning state from your chosen service provider. Possible values are “NotProvisioned”, “Provisioning”, “Provisioned”, and “Deprovisioning”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>sku</cite> block for the ExpressRoute circuit as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.ExpressRouteCircuit.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ExpressRouteCircuit.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ExpressRouteCircuitAuthorization">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">ExpressRouteCircuitAuthorization</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>express_route_circuit_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitAuthorization" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an ExpressRoute Circuit Authorization.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>express_route_circuit_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Express Route Circuit in which to create the Authorization.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ExpressRoute circuit. Changing this forces a
new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the ExpressRoute circuit. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitAuthorization.authorization_key">
<code class="descname">authorization_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitAuthorization.authorization_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Authorization Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitAuthorization.authorization_use_status">
<code class="descname">authorization_use_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitAuthorization.authorization_use_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The authorization use status.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitAuthorization.express_route_circuit_name">
<code class="descname">express_route_circuit_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitAuthorization.express_route_circuit_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Express Route Circuit in which to create the Authorization.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitAuthorization.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitAuthorization.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ExpressRoute circuit. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitAuthorization.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitAuthorization.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the ExpressRoute circuit. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.ExpressRouteCircuitAuthorization.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitAuthorization.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ExpressRouteCircuitAuthorization.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitAuthorization.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">ExpressRouteCircuitPeering</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>express_route_circuit_name=None</em>, <em>microsoft_peering_config=None</em>, <em>peer_asn=None</em>, <em>peering_type=None</em>, <em>primary_peer_address_prefix=None</em>, <em>resource_group_name=None</em>, <em>secondary_peer_address_prefix=None</em>, <em>shared_key=None</em>, <em>vlan_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an ExpressRoute Circuit Peering.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>express_route_circuit_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ExpressRoute Circuit in which to create the Peering.</li>
<li><strong>microsoft_peering_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>microsoft_peering_config</cite> block as defined below. Required when <cite>peering_type</cite> is set to <cite>MicrosoftPeering</cite>.</li>
<li><strong>peer_asn</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The Either a 16-bit or a 32-bit ASN. Can either be public or private..</li>
<li><strong>peering_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the ExpressRoute Circuit Peering. Acceptable values include <cite>AzurePrivatePeering</cite>, <cite>AzurePublicPeering</cite> and <cite>MicrosoftPeering</cite>. Changing this forces a new resource to be created.</li>
<li><strong>primary_peer_address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A <cite>/30</cite> subnet for the primary link.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the Express Route Circuit Peering. Changing this forces a new resource to be created.</li>
<li><strong>secondary_peer_address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A <cite>/30</cite> subnet for the secondary link.</li>
<li><strong>shared_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared key. Can be a maximum of 25 characters.</li>
<li><strong>vlan_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – A valid VLAN ID to establish this peering on.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.azure_asn">
<code class="descname">azure_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.azure_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ASN used by Azure.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.express_route_circuit_name">
<code class="descname">express_route_circuit_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.express_route_circuit_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ExpressRoute Circuit in which to create the Peering.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.microsoft_peering_config">
<code class="descname">microsoft_peering_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.microsoft_peering_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>microsoft_peering_config</cite> block as defined below. Required when <cite>peering_type</cite> is set to <cite>MicrosoftPeering</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.peer_asn">
<code class="descname">peer_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.peer_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Either a 16-bit or a 32-bit ASN. Can either be public or private..</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.peering_type">
<code class="descname">peering_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.peering_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the ExpressRoute Circuit Peering. Acceptable values include <cite>AzurePrivatePeering</cite>, <cite>AzurePublicPeering</cite> and <cite>MicrosoftPeering</cite>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.primary_azure_port">
<code class="descname">primary_azure_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.primary_azure_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Port used by Azure for this Peering.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.primary_peer_address_prefix">
<code class="descname">primary_peer_address_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.primary_peer_address_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>/30</cite> subnet for the primary link.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the Express Route Circuit Peering. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.secondary_azure_port">
<code class="descname">secondary_azure_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.secondary_azure_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Port used by Azure for this Peering.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.secondary_peer_address_prefix">
<code class="descname">secondary_peer_address_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.secondary_peer_address_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>/30</cite> subnet for the secondary link.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.shared_key">
<code class="descname">shared_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.shared_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared key. Can be a maximum of 25 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.vlan_id">
<code class="descname">vlan_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.vlan_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A valid VLAN ID to establish this peering on.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.Firewall">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">Firewall</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>ip_configuration=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Firewall" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Firewall.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>ip_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>ip_configuration</cite> block as documented below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Firewall. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.Firewall.ip_configuration">
<code class="descname">ip_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Firewall.ip_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>ip_configuration</cite> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Firewall.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Firewall.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Firewall.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Firewall.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Firewall. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Firewall.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Firewall.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Firewall.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Firewall.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.Firewall.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Firewall.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.Firewall.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Firewall.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">FirewallApplicationRuleCollection</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>action=None</em>, <em>azure_firewall_name=None</em>, <em>name=None</em>, <em>priority=None</em>, <em>resource_group_name=None</em>, <em>rules=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Application Rule Collection within an Azure Firewall.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the action the rule will apply to matching traffic. Possible values are <cite>Allow</cite> and <cite>Deny</cite>.</li>
<li><strong>azure_firewall_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Firewall in which the Application Rule Collection should be created. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Application Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</li>
<li><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies the priority of the rule collection. Possible values are between <cite>100</cite> - <cite>65000</cite>.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.</li>
<li><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <cite>rule</cite> blocks as defined below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection.action">
<code class="descname">action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection.action" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the action the rule will apply to matching traffic. Possible values are <cite>Allow</cite> and <cite>Deny</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection.azure_firewall_name">
<code class="descname">azure_firewall_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection.azure_firewall_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Firewall in which the Application Rule Collection should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Application Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection.priority">
<code class="descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the priority of the rule collection. Possible values are between <cite>100</cite> - <cite>65000</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection.rules">
<code class="descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>rule</cite> blocks as defined below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">FirewallNetworkRuleCollection</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>action=None</em>, <em>azure_firewall_name=None</em>, <em>name=None</em>, <em>priority=None</em>, <em>resource_group_name=None</em>, <em>rules=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Network Rule Collection within an Azure Firewall.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the action the rule will apply to matching traffic. Possible values are <cite>Allow</cite> and <cite>Deny</cite>.</li>
<li><strong>azure_firewall_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Firewall in which the Network Rule Collection should be created. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Network Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</li>
<li><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies the priority of the rule collection. Possible values are between <cite>100</cite> - <cite>65000</cite>.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.</li>
<li><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <cite>rule</cite> blocks as defined below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection.action">
<code class="descname">action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection.action" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the action the rule will apply to matching traffic. Possible values are <cite>Allow</cite> and <cite>Deny</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection.azure_firewall_name">
<code class="descname">azure_firewall_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection.azure_firewall_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Firewall in which the Network Rule Collection should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Network Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection.priority">
<code class="descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the priority of the rule collection. Possible values are between <cite>100</cite> - <cite>65000</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection.rules">
<code class="descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>rule</cite> blocks as defined below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.GetApplicationSecurityGroupResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">GetApplicationSecurityGroupResult</code><span class="sig-paren">(</span><em>location=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetApplicationSecurityGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getApplicationSecurityGroup.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetApplicationSecurityGroupResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetApplicationSecurityGroupResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The supported Azure location where the Application Security Group exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetApplicationSecurityGroupResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetApplicationSecurityGroupResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetApplicationSecurityGroupResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetApplicationSecurityGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">GetNetworkInterfaceResult</code><span class="sig-paren">(</span><em>applied_dns_servers=None</em>, <em>dns_servers=None</em>, <em>enable_accelerated_networking=None</em>, <em>enable_ip_forwarding=None</em>, <em>internal_dns_name_label=None</em>, <em>internal_fqdn=None</em>, <em>ip_configurations=None</em>, <em>location=None</em>, <em>mac_address=None</em>, <em>network_security_group_id=None</em>, <em>private_ip_address=None</em>, <em>private_ip_addresses=None</em>, <em>tags=None</em>, <em>virtual_machine_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkInterface.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.applied_dns_servers">
<code class="descname">applied_dns_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.applied_dns_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of DNS servers applied to the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.dns_servers">
<code class="descname">dns_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.dns_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of DNS servers used by the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.enable_accelerated_networking">
<code class="descname">enable_accelerated_networking</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.enable_accelerated_networking" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates if accelerated networking is set on the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.enable_ip_forwarding">
<code class="descname">enable_ip_forwarding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.enable_ip_forwarding" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicate if IP forwarding is set on the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.internal_dns_name_label">
<code class="descname">internal_dns_name_label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.internal_dns_name_label" title="Permalink to this definition">¶</a></dt>
<dd><p>The internal dns name label of the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.ip_configurations">
<code class="descname">ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>ip_configuration</cite> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.mac_address">
<code class="descname">mac_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.mac_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The MAC address used by the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.network_security_group_id">
<code class="descname">network_security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.network_security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the network security group associated to the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.private_ip_address">
<code class="descname">private_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.private_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Private IP Address assigned to this Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.private_ip_addresses">
<code class="descname">private_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.private_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of private ip addresses associates to the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>List the tags associated to the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.virtual_machine_id">
<code class="descname">virtual_machine_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.virtual_machine_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the virtual machine that the specified Network Interface is attached to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetNetworkSecurityGroupResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">GetNetworkSecurityGroupResult</code><span class="sig-paren">(</span><em>location=None</em>, <em>security_rules=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetNetworkSecurityGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkSecurityGroup.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkSecurityGroupResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkSecurityGroupResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The supported Azure location where the resource exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkSecurityGroupResult.security_rules">
<code class="descname">security_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkSecurityGroupResult.security_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>security_rule</cite> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkSecurityGroupResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkSecurityGroupResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkSecurityGroupResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkSecurityGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetPublicIPResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">GetPublicIPResult</code><span class="sig-paren">(</span><em>allocation_method=None</em>, <em>domain_name_label=None</em>, <em>fqdn=None</em>, <em>idle_timeout_in_minutes=None</em>, <em>ip_address=None</em>, <em>ip_version=None</em>, <em>location=None</em>, <em>reverse_fqdn=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>zones=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetPublicIPResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPublicIP.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIPResult.domain_name_label">
<code class="descname">domain_name_label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIPResult.domain_name_label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label for the Domain Name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIPResult.fqdn">
<code class="descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIPResult.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>Fully qualified domain name of the A DNS record associated with the public IP. This is the concatenation of the domainNameLabel and the regionalized DNS zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIPResult.idle_timeout_in_minutes">
<code class="descname">idle_timeout_in_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIPResult.idle_timeout_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the timeout for the TCP idle connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIPResult.ip_address">
<code class="descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIPResult.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address value that was allocated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIPResult.ip_version">
<code class="descname">ip_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIPResult.ip_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP version being used, for example <cite>IPv4</cite> or <cite>IPv6</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIPResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIPResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIPResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIPResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetPublicIPsResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">GetPublicIPsResult</code><span class="sig-paren">(</span><em>public_ips=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetPublicIPsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPublicIPs.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIPsResult.public_ips">
<code class="descname">public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIPsResult.public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>A List of <cite>public_ips</cite> blocks as defined below filtered by the criteria above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIPsResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIPsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetRouteTableResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">GetRouteTableResult</code><span class="sig-paren">(</span><em>location=None</em>, <em>routes=None</em>, <em>subnets=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetRouteTableResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRouteTable.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetRouteTableResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetRouteTableResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which the Route Table exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetRouteTableResult.routes">
<code class="descname">routes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetRouteTableResult.routes" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>route</cite> blocks as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetRouteTableResult.subnets">
<code class="descname">subnets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetRouteTableResult.subnets" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of Subnets associated with this route table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetRouteTableResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetRouteTableResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the Route Table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetRouteTableResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetRouteTableResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetSubnetResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">GetSubnetResult</code><span class="sig-paren">(</span><em>address_prefix=None</em>, <em>ip_configurations=None</em>, <em>network_security_group_id=None</em>, <em>route_table_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetSubnetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSubnet.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetSubnetResult.address_prefix">
<code class="descname">address_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetSubnetResult.address_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The address prefix used for the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetSubnetResult.ip_configurations">
<code class="descname">ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetSubnetResult.ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of IP Configurations with IPs within this subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetSubnetResult.network_security_group_id">
<code class="descname">network_security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetSubnetResult.network_security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Security Group associated with the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetSubnetResult.route_table_id">
<code class="descname">route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetSubnetResult.route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Route Table associated with this subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetSubnetResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetSubnetResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">GetVirtualNetworkGatewayResult</code><span class="sig-paren">(</span><em>active_active=None</em>, <em>bgp_settings=None</em>, <em>default_local_network_gateway_id=None</em>, <em>enable_bgp=None</em>, <em>ip_configurations=None</em>, <em>location=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>type=None</em>, <em>vpn_client_configurations=None</em>, <em>vpn_type=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVirtualNetworkGateway.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.active_active">
<code class="descname">active_active</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.active_active" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) Is this an Active-Active Gateway?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.default_local_network_gateway_id">
<code class="descname">default_local_network_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.default_local_network_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (<em>forced tunneling</em>). Refer to the
[Azure documentation on forced tunneling](<a class="reference external" href="https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm">https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm</a>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.enable_bgp">
<code class="descname">enable_bgp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.enable_bgp" title="Permalink to this definition">¶</a></dt>
<dd><p>Will BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.ip_configurations">
<code class="descname">ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or two <cite>ip_configuration</cite> blocks documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location/region where the Virtual Network Gateway is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration of the size and capacity of the Virtual Network Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the Virtual Network Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.vpn_client_configurations">
<code class="descname">vpn_client_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.vpn_client_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>vpn_client_configuration</cite> block which is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.vpn_type">
<code class="descname">vpn_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.vpn_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The routing type of the Virtual Network Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetVirtualNetworkResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">GetVirtualNetworkResult</code><span class="sig-paren">(</span><em>address_spaces=None</em>, <em>dns_servers=None</em>, <em>subnets=None</em>, <em>vnet_peerings=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVirtualNetwork.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkResult.address_spaces">
<code class="descname">address_spaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkResult.address_spaces" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of address spaces used by the virtual network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkResult.dns_servers">
<code class="descname">dns_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkResult.dns_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of DNS servers used by the virtual network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkResult.subnets">
<code class="descname">subnets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkResult.subnets" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of name of the subnets that are attached to this virtual network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkResult.vnet_peerings">
<code class="descname">vnet_peerings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkResult.vnet_peerings" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of name - virtual network id of the virtual network peerings.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.LocalNetworkGateway">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">LocalNetworkGateway</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>address_spaces=None</em>, <em>bgp_settings=None</em>, <em>gateway_address=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a local network gateway connection over which specific connections can be configured.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>address_spaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of string CIDRs representing the
address spaces the gateway exposes.</li>
<li><strong>bgp_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>bgp_settings</cite> block as defined below containing the
Local Network Gateway’s BGP speaker settings.</li>
<li><strong>gateway_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the gateway to which to
connect.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location/region where the local network gateway is
created. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the local network gateway. Changing this
forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the local network gateway.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.LocalNetworkGateway.address_spaces">
<code class="descname">address_spaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.address_spaces" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of string CIDRs representing the
address spaces the gateway exposes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.LocalNetworkGateway.bgp_settings">
<code class="descname">bgp_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.bgp_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>bgp_settings</cite> block as defined below containing the
Local Network Gateway’s BGP speaker settings.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.LocalNetworkGateway.gateway_address">
<code class="descname">gateway_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.gateway_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of the gateway to which to
connect.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.LocalNetworkGateway.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location/region where the local network gateway is
created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.LocalNetworkGateway.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the local network gateway. Changing this
forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.LocalNetworkGateway.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the local network gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.LocalNetworkGateway.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.LocalNetworkGateway.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.LocalNetworkGateway.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterface">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">NetworkInterface</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>applied_dns_servers=None</em>, <em>dns_servers=None</em>, <em>enable_accelerated_networking=None</em>, <em>enable_ip_forwarding=None</em>, <em>internal_dns_name_label=None</em>, <em>internal_fqdn=None</em>, <em>ip_configurations=None</em>, <em>location=None</em>, <em>mac_address=None</em>, <em>name=None</em>, <em>network_security_group_id=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>virtual_machine_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Network Interface located in a Virtual Network, usually attached to a Virtual Machine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>applied_dns_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If the VM that uses this NIC is part of an Availability Set, then this list will have the union of all DNS servers from all NICs that are part of the Availability Set</li>
<li><strong>dns_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of DNS servers IP addresses to use for this NIC, overrides the VNet-level server list</li>
<li><strong>enable_accelerated_networking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables Azure Accelerated Networking using SR-IOV. Only certain VM instance sizes are supported. Refer to [Create a Virtual Machine with Accelerated Networking](<a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-network/create-vm-accelerated-networking-cli">https://docs.microsoft.com/en-us/azure/virtual-network/create-vm-accelerated-networking-cli</a>). Defaults to <cite>false</cite>.</li>
<li><strong>enable_ip_forwarding</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables IP Forwarding on the NIC. Defaults to <cite>false</cite>.</li>
<li><strong>internal_dns_name_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Relative DNS name for this NIC used for internal communications between VMs in the same VNet</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] internal_fqdn
:param pulumi.Input[list] ip_configurations: One or more <cite>ip_configuration</cite> associated with this NIC as documented below.
:param pulumi.Input[str] location: The location/region where the network interface is created. Changing this forces a new resource to be created.
:param pulumi.Input[str] mac_address: The media access control (MAC) address of the network interface.
:param pulumi.Input[str] name: The name of the network interface. Changing this forces a new resource to be created.
:param pulumi.Input[str] network_security_group_id: The ID of the Network Security Group to associate with the network interface.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the network interface. Changing this forces a new resource to be created.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
:param pulumi.Input[str] virtual_machine_id: Reference to a VM with which this NIC has been associated.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.applied_dns_servers">
<code class="descname">applied_dns_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.applied_dns_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>If the VM that uses this NIC is part of an Availability Set, then this list will have the union of all DNS servers from all NICs that are part of the Availability Set</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.dns_servers">
<code class="descname">dns_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.dns_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of DNS servers IP addresses to use for this NIC, overrides the VNet-level server list</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.enable_accelerated_networking">
<code class="descname">enable_accelerated_networking</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.enable_accelerated_networking" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables Azure Accelerated Networking using SR-IOV. Only certain VM instance sizes are supported. Refer to [Create a Virtual Machine with Accelerated Networking](<a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-network/create-vm-accelerated-networking-cli">https://docs.microsoft.com/en-us/azure/virtual-network/create-vm-accelerated-networking-cli</a>). Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.enable_ip_forwarding">
<code class="descname">enable_ip_forwarding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.enable_ip_forwarding" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables IP Forwarding on the NIC. Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.internal_dns_name_label">
<code class="descname">internal_dns_name_label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.internal_dns_name_label" title="Permalink to this definition">¶</a></dt>
<dd><p>Relative DNS name for this NIC used for internal communications between VMs in the same VNet</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.ip_configurations">
<code class="descname">ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>ip_configuration</cite> associated with this NIC as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location/region where the network interface is created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.mac_address">
<code class="descname">mac_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.mac_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The media access control (MAC) address of the network interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the network interface. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.network_security_group_id">
<code class="descname">network_security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.network_security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Security Group to associate with the network interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.private_ip_address">
<code class="descname">private_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.private_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The first private IP address of the network interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.private_ip_addresses">
<code class="descname">private_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.private_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The private IP addresses of the network interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the network interface. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.virtual_machine_id">
<code class="descname">virtual_machine_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.virtual_machine_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Reference to a VM with which this NIC has been associated.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkInterface.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterface.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>backend_address_pool_id=None</em>, <em>ip_configuration_name=None</em>, <em>network_interface_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the association between a Network Interface and a Application Gateway’s Backend Address Pool.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>backend_address_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Application Gateway’s Backend Address Pool which this Network Interface which should be connected to. Changing this forces a new resource to be created.</li>
<li><strong>ip_configuration_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the IP Configuration within the Network Interface which should be connected to the Backend Address Pool. Changing this forces a new resource to be created.</li>
<li><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Interface. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.backend_address_pool_id">
<code class="descname">backend_address_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.backend_address_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Application Gateway’s Backend Address Pool which this Network Interface which should be connected to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.ip_configuration_name">
<code class="descname">ip_configuration_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.ip_configuration_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the IP Configuration within the Network Interface which should be connected to the Backend Address Pool. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.network_interface_id">
<code class="descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Interface. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">NetworkInterfaceBackendAddressPoolAssociation</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>backend_address_pool_id=None</em>, <em>ip_configuration_name=None</em>, <em>network_interface_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the association between a Network Interface and a Load Balancer’s Backend Address Pool.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>backend_address_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer Backend Address Pool which this Network Interface which should be connected to. Changing this forces a new resource to be created.</li>
<li><strong>ip_configuration_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the IP Configuration within the Network Interface which should be connected to the Backend Address Pool. Changing this forces a new resource to be created.</li>
<li><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Interface. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.backend_address_pool_id">
<code class="descname">backend_address_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.backend_address_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Load Balancer Backend Address Pool which this Network Interface which should be connected to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.ip_configuration_name">
<code class="descname">ip_configuration_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.ip_configuration_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the IP Configuration within the Network Interface which should be connected to the Backend Address Pool. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.network_interface_id">
<code class="descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Interface. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterfaceNatRuleAssociation">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">NetworkInterfaceNatRuleAssociation</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>ip_configuration_name=None</em>, <em>nat_rule_id=None</em>, <em>network_interface_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceNatRuleAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the association between a Network Interface and a Load Balancer’s NAT Rule.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>ip_configuration_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.</li>
<li><strong>nat_rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.</li>
<li><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Interface. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceNatRuleAssociation.ip_configuration_name">
<code class="descname">ip_configuration_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceNatRuleAssociation.ip_configuration_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceNatRuleAssociation.nat_rule_id">
<code class="descname">nat_rule_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceNatRuleAssociation.nat_rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceNatRuleAssociation.network_interface_id">
<code class="descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceNatRuleAssociation.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Interface. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkInterfaceNatRuleAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceNatRuleAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterfaceNatRuleAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceNatRuleAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkSecurityGroup">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">NetworkSecurityGroup</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>security_rules=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a network security group that contains a list of network security rules.  Network security groups enable inbound or outbound traffic to be enabled or denied.</p>
<p>&gt; <strong>NOTE on Network Security Groups and Network Security Rules:</strong> Terraform currently
provides both a standalone Network Security Rule resource, and allows for Network Security Rules to be defined in-line within the Network Security Group resource.
At this time you cannot use a Network Security Group with in-line Network Security Rules in conjunction with any Network Security Rule resources. Doing so will cause a conflict of rule settings and will overwrite rules.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the network security group. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the network security group. Changing this forces a new resource to be created.</li>
<li><strong>security_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <cite>security_rule</cite> blocks as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityGroup.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityGroup.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the network security group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityGroup.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityGroup.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the network security group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityGroup.security_rules">
<code class="descname">security_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityGroup.security_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>security_rule</cite> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkSecurityGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkSecurityGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkSecurityRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">NetworkSecurityRule</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>access=None</em>, <em>description=None</em>, <em>destination_address_prefix=None</em>, <em>destination_address_prefixes=None</em>, <em>destination_application_security_group_ids=None</em>, <em>destination_port_range=None</em>, <em>destination_port_ranges=None</em>, <em>direction=None</em>, <em>name=None</em>, <em>network_security_group_name=None</em>, <em>priority=None</em>, <em>protocol=None</em>, <em>resource_group_name=None</em>, <em>source_address_prefix=None</em>, <em>source_address_prefixes=None</em>, <em>source_application_security_group_ids=None</em>, <em>source_port_range=None</em>, <em>source_port_ranges=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Network Security Rule.</p>
<p>&gt; <strong>NOTE on Network Security Groups and Network Security Rules:</strong> Terraform currently
provides both a standalone Network Security Rule resource, and allows for Network Security Rules to be defined in-line within the Network Security Group resource.
At this time you cannot use a Network Security Group with in-line Network Security Rules in conjunction with any Network Security Rule resources. Doing so will cause a conflict of rule settings and will overwrite rules.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>access</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether network traffic is allowed or denied. Possible values are <cite>Allow</cite> and <cite>Deny</cite>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this rule. Restricted to 140 characters.</li>
<li><strong>destination_address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CIDR or destination IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if <cite>destination_address_prefixes</cite> is not specified.</li>
<li><strong>destination_address_prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of destination address prefixes. Tags may not be used. This is required if <cite>destination_address_prefix</cite> is not specified.</li>
<li><strong>destination_application_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A List of destination Application Security Group ID’s</li>
<li><strong>destination_port_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination Port or Range. Integer or range between <cite>0</cite> and <cite>65535</cite> or <cite>*</cite> to match any. This is required if <cite>destination_port_ranges</cite> is not specified.</li>
<li><strong>destination_port_ranges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of destination ports or port ranges. This is required if <cite>destination_port_range</cite> is not specified.</li>
<li><strong>direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The direction specifies if rule will be evaluated on incoming or outgoing traffic. Possible values are <cite>Inbound</cite> and <cite>Outbound</cite>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the security rule. This needs to be unique across all Rules in the Network Security Group. Changing this forces a new resource to be created.</li>
<li><strong>network_security_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Security Group that we want to attach the rule to. Changing this forces a new resource to be created.</li>
<li><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies the priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.</li>
<li><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network protocol this rule applies to. Possible values include <cite>Tcp</cite>, <cite>Udp</cite> or <cite>*</cite> (which matches both).</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Network Security Rule. Changing this forces a new resource to be created.</li>
<li><strong>source_address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CIDR or source IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if <cite>source_address_prefixes</cite> is not specified.</li>
<li><strong>source_address_prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of source address prefixes. Tags may not be used. This is required if <cite>source_address_prefix</cite> is not specified.</li>
<li><strong>source_application_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A List of source Application Security Group ID’s</li>
<li><strong>source_port_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Source Port or Range. Integer or range between <cite>0</cite> and <cite>65535</cite> or <cite>*</cite> to match any. This is required if <cite>source_port_ranges</cite> is not specified.</li>
<li><strong>source_port_ranges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of source ports or port ranges. This is required if <cite>source_port_range</cite> is not specified.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.access">
<code class="descname">access</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.access" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether network traffic is allowed or denied. Possible values are <cite>Allow</cite> and <cite>Deny</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for this rule. Restricted to 140 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.destination_address_prefix">
<code class="descname">destination_address_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.destination_address_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR or destination IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if <cite>destination_address_prefixes</cite> is not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.destination_address_prefixes">
<code class="descname">destination_address_prefixes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.destination_address_prefixes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of destination address prefixes. Tags may not be used. This is required if <cite>destination_address_prefix</cite> is not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.destination_application_security_group_ids">
<code class="descname">destination_application_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.destination_application_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A List of destination Application Security Group ID’s</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.destination_port_range">
<code class="descname">destination_port_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.destination_port_range" title="Permalink to this definition">¶</a></dt>
<dd><p>Destination Port or Range. Integer or range between <cite>0</cite> and <cite>65535</cite> or <cite>*</cite> to match any. This is required if <cite>destination_port_ranges</cite> is not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.destination_port_ranges">
<code class="descname">destination_port_ranges</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.destination_port_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>List of destination ports or port ranges. This is required if <cite>destination_port_range</cite> is not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.direction">
<code class="descname">direction</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.direction" title="Permalink to this definition">¶</a></dt>
<dd><p>The direction specifies if rule will be evaluated on incoming or outgoing traffic. Possible values are <cite>Inbound</cite> and <cite>Outbound</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the security rule. This needs to be unique across all Rules in the Network Security Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.network_security_group_name">
<code class="descname">network_security_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.network_security_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Network Security Group that we want to attach the rule to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.priority">
<code class="descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.protocol">
<code class="descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>Network protocol this rule applies to. Possible values include <cite>Tcp</cite>, <cite>Udp</cite> or <cite>*</cite> (which matches both).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Network Security Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.source_address_prefix">
<code class="descname">source_address_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.source_address_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR or source IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if <cite>source_address_prefixes</cite> is not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.source_address_prefixes">
<code class="descname">source_address_prefixes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.source_address_prefixes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of source address prefixes. Tags may not be used. This is required if <cite>source_address_prefix</cite> is not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.source_application_security_group_ids">
<code class="descname">source_application_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.source_application_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A List of source Application Security Group ID’s</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.source_port_range">
<code class="descname">source_port_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.source_port_range" title="Permalink to this definition">¶</a></dt>
<dd><p>Source Port or Range. Integer or range between <cite>0</cite> and <cite>65535</cite> or <cite>*</cite> to match any. This is required if <cite>source_port_ranges</cite> is not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.source_port_ranges">
<code class="descname">source_port_ranges</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.source_port_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>List of source ports or port ranges. This is required if <cite>source_port_range</cite> is not specified.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkSecurityRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkSecurityRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkWatcher">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">NetworkWatcher</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkWatcher" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Network Watcher.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Watcher. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Network Watcher. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkWatcher.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkWatcher.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkWatcher.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkWatcher.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Network Watcher. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkWatcher.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkWatcher.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Network Watcher. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkWatcher.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkWatcher.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkWatcher.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkWatcher.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkWatcher.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkWatcher.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.PacketCapture">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">PacketCapture</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>filters=None</em>, <em>maximum_bytes_per_packet=None</em>, <em>maximum_bytes_per_session=None</em>, <em>maximum_capture_duration=None</em>, <em>name=None</em>, <em>network_watcher_name=None</em>, <em>resource_group_name=None</em>, <em>storage_location=None</em>, <em>target_resource_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PacketCapture" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures Packet Capturing against a Virtual Machine using a Network Watcher.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <cite>filter</cite> blocks as defined below. Changing this forces a new resource to be created.</li>
<li><strong>maximum_bytes_per_packet</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of bytes captured per packet. The remaining bytes are truncated. Defaults to <cite>0</cite> (Entire Packet Captured). Changing this forces a new resource to be created.</li>
<li><strong>maximum_bytes_per_session</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum size of the capture in Bytes. Defaults to <cite>1073741824</cite> (1GB). Changing this forces a new resource to be created.</li>
<li><strong>maximum_capture_duration</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum duration of the capture session in seconds. Defaults to <cite>18000</cite> (5 hours). Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for this Packet Capture. Changing this forces a new resource to be created.</li>
<li><strong>network_watcher_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Watcher. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Network Watcher exists. Changing this forces a new resource to be created.</li>
<li><strong>storage_location</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>storage_location</cite> block as defined below. Changing this forces a new resource to be created.</li>
<li><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Resource to capture packets from. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.PacketCapture.filters">
<code class="descname">filters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PacketCapture.filters" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>filter</cite> blocks as defined below. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PacketCapture.maximum_bytes_per_packet">
<code class="descname">maximum_bytes_per_packet</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PacketCapture.maximum_bytes_per_packet" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of bytes captured per packet. The remaining bytes are truncated. Defaults to <cite>0</cite> (Entire Packet Captured). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PacketCapture.maximum_bytes_per_session">
<code class="descname">maximum_bytes_per_session</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PacketCapture.maximum_bytes_per_session" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum size of the capture in Bytes. Defaults to <cite>1073741824</cite> (1GB). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PacketCapture.maximum_capture_duration">
<code class="descname">maximum_capture_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PacketCapture.maximum_capture_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum duration of the capture session in seconds. Defaults to <cite>18000</cite> (5 hours). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PacketCapture.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PacketCapture.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for this Packet Capture. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PacketCapture.network_watcher_name">
<code class="descname">network_watcher_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PacketCapture.network_watcher_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Network Watcher. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PacketCapture.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PacketCapture.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Network Watcher exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PacketCapture.storage_location">
<code class="descname">storage_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PacketCapture.storage_location" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>storage_location</cite> block as defined below. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PacketCapture.target_resource_id">
<code class="descname">target_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PacketCapture.target_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Resource to capture packets from. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.PacketCapture.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PacketCapture.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.PacketCapture.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PacketCapture.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.PublicIp">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">PublicIp</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>allocation_method=None</em>, <em>domain_name_label=None</em>, <em>idle_timeout_in_minutes=None</em>, <em>ip_version=None</em>, <em>location=None</em>, <em>name=None</em>, <em>public_ip_address_allocation=None</em>, <em>resource_group_name=None</em>, <em>reverse_fqdn=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PublicIp" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a Public IP Address.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allocation_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the allocation method for this IP address. Possible values are <cite>Static</cite> or <cite>Dynamic</cite>.</li>
<li><strong>domain_name_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Label for the Domain Name. Will be used to make up the FQDN.  If a domain name label is specified, an A DNS record is created for the public IP in the Microsoft Azure DNS system.</li>
<li><strong>idle_timeout_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies the timeout for the TCP idle connection. The value can be set between 4 and 30 minutes.</li>
<li><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP Version to use, IPv6 or IPv4.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Public IP resource . Changing this forces a
new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] public_ip_address_allocation
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to</p>
<blockquote>
<div>create the public ip.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>reverse_fqdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A fully qualified domain name that resolves to this public IP address. If the reverseFqdn is specified, then a PTR DNS record is created pointing from the IP address in the in-addr.arpa domain to the reverse FQDN.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU of the Public IP. Accepted values are <cite>Basic</cite> and <cite>Standard</cite>. Defaults to <cite>Basic</cite>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A collection containing the availability zone to allocate the Public IP in.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.allocation_method">
<code class="descname">allocation_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.allocation_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the allocation method for this IP address. Possible values are <cite>Static</cite> or <cite>Dynamic</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.domain_name_label">
<code class="descname">domain_name_label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.domain_name_label" title="Permalink to this definition">¶</a></dt>
<dd><p>Label for the Domain Name. Will be used to make up the FQDN.  If a domain name label is specified, an A DNS record is created for the public IP in the Microsoft Azure DNS system.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.fqdn">
<code class="descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>Fully qualified domain name of the A DNS record associated with the public IP. This is the concatenation of the domainNameLabel and the regionalized DNS zone</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.idle_timeout_in_minutes">
<code class="descname">idle_timeout_in_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.idle_timeout_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the timeout for the TCP idle connection. The value can be set between 4 and 30 minutes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.ip_address">
<code class="descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address value that was allocated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.ip_version">
<code class="descname">ip_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.ip_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP Version to use, IPv6 or IPv4.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Public IP resource . Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the public ip.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.reverse_fqdn">
<code class="descname">reverse_fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.reverse_fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>A fully qualified domain name that resolves to this public IP address. If the reverseFqdn is specified, then a PTR DNS record is created pointing from the IP address in the in-addr.arpa domain to the reverse FQDN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU of the Public IP. Accepted values are <cite>Basic</cite> and <cite>Standard</cite>. Defaults to <cite>Basic</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.zones">
<code class="descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection containing the availability zone to allocate the Public IP in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.PublicIp.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PublicIp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.PublicIp.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PublicIp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.Route">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">Route</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>address_prefix=None</em>, <em>name=None</em>, <em>next_hop_in_ip_address=None</em>, <em>next_hop_type=None</em>, <em>resource_group_name=None</em>, <em>route_table_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Route" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Route within a Route Table.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination CIDR to which the route applies, such as <cite>10.1.0.0/16</cite></li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the route. Changing this forces a new resource to be created.</li>
<li><strong>next_hop_in_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains the IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is <cite>VirtualAppliance</cite>.</li>
<li><strong>next_hop_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of Azure hop the packet should be sent to. Possible values are <cite>VirtualNetworkGateway</cite>, <cite>VnetLocal</cite>, <cite>Internet</cite>, <cite>VirtualAppliance</cite> and <cite>None</cite></li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the route. Changing this forces a new resource to be created.</li>
<li><strong>route_table_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the route table within which create the route. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.Route.address_prefix">
<code class="descname">address_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Route.address_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination CIDR to which the route applies, such as <cite>10.1.0.0/16</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Route.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Route.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the route. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Route.next_hop_in_ip_address">
<code class="descname">next_hop_in_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Route.next_hop_in_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is <cite>VirtualAppliance</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Route.next_hop_type">
<code class="descname">next_hop_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Route.next_hop_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of Azure hop the packet should be sent to. Possible values are <cite>VirtualNetworkGateway</cite>, <cite>VnetLocal</cite>, <cite>Internet</cite>, <cite>VirtualAppliance</cite> and <cite>None</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Route.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Route.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the route. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Route.route_table_name">
<code class="descname">route_table_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Route.route_table_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the route table within which create the route. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.Route.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Route.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.Route.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Route.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.RouteTable">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">RouteTable</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>disable_bgp_route_propagation=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>routes=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.RouteTable" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Route Table</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>disable_bgp_route_propagation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls propagation of routes learned by BGP on that route table. True means disable.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the route table. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the route table. Changing this forces a new resource to be created.</li>
<li><strong>routes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Can be specified multiple times to define multiple routes. Each <cite>route</cite> block supports fields documented below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.RouteTable.disable_bgp_route_propagation">
<code class="descname">disable_bgp_route_propagation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.RouteTable.disable_bgp_route_propagation" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls propagation of routes learned by BGP on that route table. True means disable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.RouteTable.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.RouteTable.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.RouteTable.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.RouteTable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the route table. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.RouteTable.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.RouteTable.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the route table. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.RouteTable.routes">
<code class="descname">routes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.RouteTable.routes" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be specified multiple times to define multiple routes. Each <cite>route</cite> block supports fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.RouteTable.subnets">
<code class="descname">subnets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.RouteTable.subnets" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of Subnets associated with this route table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.RouteTable.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.RouteTable.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.RouteTable.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.RouteTable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.RouteTable.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.RouteTable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.Subnet">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">Subnet</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>address_prefix=None</em>, <em>delegations=None</em>, <em>ip_configurations=None</em>, <em>name=None</em>, <em>network_security_group_id=None</em>, <em>resource_group_name=None</em>, <em>route_table_id=None</em>, <em>service_endpoints=None</em>, <em>virtual_network_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a subnet. Subnets represent network segments within the IP space defined by the virtual network.</p>
<p>&gt; <strong>NOTE on Virtual Networks and Subnet’s:</strong> Terraform currently
provides both a standalone Subnet resource, and allows for Subnets to be defined in-line within the Virtual Network resource.
At this time you cannot use a Virtual Network with in-line Subnets in conjunction with any Subnet resources. Doing so will cause a conflict of Subnet configurations and will overwrite Subnet’s.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address prefix to use for the subnet.</li>
<li><strong>delegations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <cite>delegation</cite> blocks as defined below.</li>
<li><strong>ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The collection of IP Configurations with IPs within this subnet.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnet. Changing this forces a new resource to be created.</li>
<li><strong>network_security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Security Group to associate with the subnet.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the subnet. Changing this forces a new resource to be created.</li>
<li><strong>route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Route Table to associate with the subnet.</li>
<li><strong>service_endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of Service endpoints to associate with the subnet. Possible values include: <cite>Microsoft.AzureActiveDirectory</cite>, <cite>Microsoft.AzureCosmosDB</cite>, <cite>Microsoft.EventHub</cite>, <cite>Microsoft.KeyVault</cite>, <cite>Microsoft.ServiceBus</cite>, <cite>Microsoft.Sql</cite> and <cite>Microsoft.Storage</cite>.</li>
<li><strong>virtual_network_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual network to which to attach the subnet. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.Subnet.address_prefix">
<code class="descname">address_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Subnet.address_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The address prefix to use for the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Subnet.delegations">
<code class="descname">delegations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Subnet.delegations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>delegation</cite> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Subnet.ip_configurations">
<code class="descname">ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Subnet.ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of IP Configurations with IPs within this subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Subnet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Subnet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the subnet. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Subnet.network_security_group_id">
<code class="descname">network_security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Subnet.network_security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Security Group to associate with the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Subnet.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Subnet.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the subnet. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Subnet.route_table_id">
<code class="descname">route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Subnet.route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Route Table to associate with the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Subnet.service_endpoints">
<code class="descname">service_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Subnet.service_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of Service endpoints to associate with the subnet. Possible values include: <cite>Microsoft.AzureActiveDirectory</cite>, <cite>Microsoft.AzureCosmosDB</cite>, <cite>Microsoft.EventHub</cite>, <cite>Microsoft.KeyVault</cite>, <cite>Microsoft.ServiceBus</cite>, <cite>Microsoft.Sql</cite> and <cite>Microsoft.Storage</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Subnet.virtual_network_name">
<code class="descname">virtual_network_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Subnet.virtual_network_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the virtual network to which to attach the subnet. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.Subnet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Subnet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.Subnet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Subnet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.SubnetNetworkSecurityGroupAssociation">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">SubnetNetworkSecurityGroupAssociation</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>network_security_group_id=None</em>, <em>subnet_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.SubnetNetworkSecurityGroupAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates a Network Security Group with a Subnet within a Virtual Network.</p>
<p>-&gt; <strong>NOTE:</strong> Subnet <cite>&lt;-&gt;</cite> Network Security Group associations currently need to be configured on both this resource and using the <cite>network_security_group_id</cite> field on the <cite>azurerm_subnet</cite> resource. The next major version of the AzureRM Provider (2.0) will remove the <cite>network_security_group_id</cite> field from the <cite>azurerm_subnet</cite> resource such that this resource is used to link resources in future.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>network_security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Security Group which should be associated with the Subnet. Changing this forces a new resource to be created.</li>
<li><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.SubnetNetworkSecurityGroupAssociation.network_security_group_id">
<code class="descname">network_security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.SubnetNetworkSecurityGroupAssociation.network_security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Security Group which should be associated with the Subnet. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.SubnetNetworkSecurityGroupAssociation.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.SubnetNetworkSecurityGroupAssociation.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Subnet. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.SubnetNetworkSecurityGroupAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.SubnetNetworkSecurityGroupAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.SubnetNetworkSecurityGroupAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.SubnetNetworkSecurityGroupAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.SubnetRouteTableAssociation">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">SubnetRouteTableAssociation</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>route_table_id=None</em>, <em>subnet_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.SubnetRouteTableAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates a Route Table with a Subnet within a Virtual Network.</p>
<p>-&gt; <strong>NOTE:</strong> Subnet <cite>&lt;-&gt;</cite> Route Table associations currently need to be configured on both this resource and using the <cite>route_table_id</cite> field on the <cite>azurerm_subnet</cite> resource. The next major version of the AzureRM Provider (2.0) will remove the <cite>route_table_id</cite> field from the <cite>azurerm_subnet</cite> resource such that this resource is used to link resources in future.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Route Table which should be associated with the Subnet. Changing this forces a new resource to be created.</li>
<li><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.SubnetRouteTableAssociation.route_table_id">
<code class="descname">route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.SubnetRouteTableAssociation.route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Route Table which should be associated with the Subnet. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.SubnetRouteTableAssociation.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.SubnetRouteTableAssociation.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Subnet. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.SubnetRouteTableAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.SubnetRouteTableAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.SubnetRouteTableAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.SubnetRouteTableAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualNetwork">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">VirtualNetwork</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>address_spaces=None</em>, <em>dns_servers=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>subnets=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a virtual network including any configured subnets. Each subnet can
optionally be configured with a security group to be associated with the subnet.</p>
<p>&gt; <strong>NOTE on Virtual Networks and Subnet’s:</strong> Terraform currently
provides both a standalone Subnet resource, and allows for Subnets to be defined in-line within the Virtual Network resource.
At this time you cannot use a Virtual Network with in-line Subnets in conjunction with any Subnet resources. Doing so will cause a conflict of Subnet configurations and will overwrite Subnet’s.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>address_spaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The address space that is used the virtual
network. You can supply more than one address space. Changing this forces
a new resource to be created.</li>
<li><strong>dns_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IP addresses of DNS servers</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location/region where the virtual network is
created. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual network. Changing this forces a
new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the virtual network.</li>
<li><strong>subnets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Can be specified multiple times to define multiple
subnets. Each <cite>subnet</cite> block supports fields documented below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetwork.address_spaces">
<code class="descname">address_spaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.address_spaces" title="Permalink to this definition">¶</a></dt>
<dd><p>The address space that is used the virtual
network. You can supply more than one address space. Changing this forces
a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetwork.dns_servers">
<code class="descname">dns_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.dns_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IP addresses of DNS servers</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetwork.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location/region where the virtual network is
created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetwork.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the virtual network. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetwork.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the virtual network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetwork.subnets">
<code class="descname">subnets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.subnets" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be specified multiple times to define multiple
subnets. Each <cite>subnet</cite> block supports fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetwork.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VirtualNetwork.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualNetwork.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualNetworkGateway">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">VirtualNetworkGateway</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>active_active=None</em>, <em>bgp_settings=None</em>, <em>default_local_network_gateway_id=None</em>, <em>enable_bgp=None</em>, <em>ip_configurations=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>type=None</em>, <em>vpn_client_configuration=None</em>, <em>vpn_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Virtual Network Gateway to establish secure, cross-premises connectivity.</p>
<p>-&gt; <strong>Note:</strong> Please be aware that provisioning a Virtual Network Gateway takes a long time (between 30 minutes and 1 hour)</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>active_active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <cite>true</cite>, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a <cite>HighPerformance</cite> or an
<cite>UltraPerformance</cite> sku. If <cite>false</cite>, an active-standby gateway will be created.
Defaults to <cite>false</cite>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[dict] bgp_settings
:param pulumi.Input[str] default_local_network_gateway_id: The ID of the local network gateway</p>
<blockquote>
<div>through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (<em>forced tunneling</em>). Refer to the
[Azure documentation on forced tunneling](<a class="reference external" href="https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm">https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm</a>).
If not specified, forced tunneling is disabled.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>enable_bgp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <cite>true</cite>, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to <cite>false</cite>.</li>
<li><strong>ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or two <cite>ip_configuration</cite> blocks documented below.
An active-standby gateway requires exactly one <cite>ip_configuration</cite> block whereas
an active-active gateway requires exactly two <cite>ip_configuration</cite> blocks.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Configuration of the size and capacity of the virtual network
gateway. Valid options are <cite>Basic</cite>, <cite>Standard</cite>, <cite>HighPerformance</cite>, <cite>UltraPerformance</cite>,
<cite>ErGw1AZ</cite>, <cite>ErGw2AZ</cite>, <cite>ErGw3AZ</cite>, <cite>VpnGw1</cite>, <cite>VpnGw2</cite> and <cite>VpnGw3</cite>
and depend on the <cite>type</cite> and <cite>vpn_type</cite> arguments.
A <cite>PolicyBased</cite> gateway only supports the <cite>Basic</cite> sku. Further, the <cite>UltraPerformance</cite>
sku is only supported by an <cite>ExpressRoute</cite> gateway.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the Virtual Network Gateway. Valid options are
<cite>Vpn</cite> or <cite>ExpressRoute</cite>. Changing the type forces a new resource to be created.</li>
<li><strong>vpn_client_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>vpn_client_configuration</cite> block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.</li>
<li><strong>vpn_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The routing type of the Virtual Network Gateway. Valid
options are <cite>RouteBased</cite> or <cite>PolicyBased</cite>. Defaults to <cite>RouteBased</cite>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.active_active">
<code class="descname">active_active</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.active_active" title="Permalink to this definition">¶</a></dt>
<dd><p>If <cite>true</cite>, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a <cite>HighPerformance</cite> or an
<cite>UltraPerformance</cite> sku. If <cite>false</cite>, an active-standby gateway will be created.
Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.default_local_network_gateway_id">
<code class="descname">default_local_network_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.default_local_network_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (<em>forced tunneling</em>). Refer to the
[Azure documentation on forced tunneling](<a class="reference external" href="https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm">https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm</a>).
If not specified, forced tunneling is disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.enable_bgp">
<code class="descname">enable_bgp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.enable_bgp" title="Permalink to this definition">¶</a></dt>
<dd><p>If <cite>true</cite>, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.ip_configurations">
<code class="descname">ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or two <cite>ip_configuration</cite> blocks documented below.
An active-standby gateway requires exactly one <cite>ip_configuration</cite> block whereas
an active-active gateway requires exactly two <cite>ip_configuration</cite> blocks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration of the size and capacity of the virtual network
gateway. Valid options are <cite>Basic</cite>, <cite>Standard</cite>, <cite>HighPerformance</cite>, <cite>UltraPerformance</cite>,
<cite>ErGw1AZ</cite>, <cite>ErGw2AZ</cite>, <cite>ErGw3AZ</cite>, <cite>VpnGw1</cite>, <cite>VpnGw2</cite> and <cite>VpnGw3</cite>
and depend on the <cite>type</cite> and <cite>vpn_type</cite> arguments.
A <cite>PolicyBased</cite> gateway only supports the <cite>Basic</cite> sku. Further, the <cite>UltraPerformance</cite>
sku is only supported by an <cite>ExpressRoute</cite> gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the Virtual Network Gateway. Valid options are
<cite>Vpn</cite> or <cite>ExpressRoute</cite>. Changing the type forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.vpn_client_configuration">
<code class="descname">vpn_client_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.vpn_client_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>vpn_client_configuration</cite> block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.vpn_type">
<code class="descname">vpn_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.vpn_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The routing type of the Virtual Network Gateway. Valid
options are <cite>RouteBased</cite> or <cite>PolicyBased</cite>. Defaults to <cite>RouteBased</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VirtualNetworkGateway.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualNetworkGateway.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">VirtualNetworkGatewayConnection</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>authorization_key=None</em>, <em>enable_bgp=None</em>, <em>express_route_circuit_id=None</em>, <em>ipsec_policy=None</em>, <em>local_network_gateway_id=None</em>, <em>location=None</em>, <em>name=None</em>, <em>peer_virtual_network_gateway_id=None</em>, <em>resource_group_name=None</em>, <em>routing_weight=None</em>, <em>shared_key=None</em>, <em>tags=None</em>, <em>type=None</em>, <em>use_policy_based_traffic_selectors=None</em>, <em>virtual_network_gateway_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a connection in an existing Virtual Network Gateway.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>authorization_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.</li>
<li><strong>enable_bgp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <cite>true</cite>, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to <cite>false</cite>.</li>
<li><strong>express_route_circuit_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when <cite>type</cite> is <cite>ExpressRoute</cite>).
The Express Route Circuit can be in the same or in a different subscription.</li>
<li><strong>ipsec_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>ipsec_policy</cite> block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](<a class="reference external" href="https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell">https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell</a>).</li>
<li><strong>local_network_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the local network gateway
when creating Site-to-Site connection (i.e. when <cite>type</cite> is <cite>IPsec</cite>).</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location/region where the connection is
located. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the connection. Changing the name forces a
new resource to be created.</li>
<li><strong>peer_virtual_network_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when <cite>type</cite>
is <cite>Vnet2Vnet</cite>). The peer Virtual Network Gateway can be in the same or
in a different subscription.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.</li>
<li><strong>routing_weight</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The routing weight. Defaults to <cite>10</cite>.</li>
<li><strong>shared_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of connection. Valid options are <cite>IPsec</cite>
(Site-to-Site), <cite>ExpressRoute</cite> (ExpressRoute), and <cite>Vnet2Vnet</cite> (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.</li>
<li><strong>use_policy_based_traffic_selectors</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <cite>true</cite>, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an <cite>ipsec_policy</cite> block. Defaults to <cite>false</cite>.</li>
<li><strong>virtual_network_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.authorization_key">
<code class="descname">authorization_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.authorization_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.enable_bgp">
<code class="descname">enable_bgp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.enable_bgp" title="Permalink to this definition">¶</a></dt>
<dd><p>If <cite>true</cite>, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.express_route_circuit_id">
<code class="descname">express_route_circuit_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.express_route_circuit_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when <cite>type</cite> is <cite>ExpressRoute</cite>).
The Express Route Circuit can be in the same or in a different subscription.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.ipsec_policy">
<code class="descname">ipsec_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.ipsec_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>ipsec_policy</cite> block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to [the relevant section in the Azure documentation](<a class="reference external" href="https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell">https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell</a>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.local_network_gateway_id">
<code class="descname">local_network_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.local_network_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the local network gateway
when creating Site-to-Site connection (i.e. when <cite>type</cite> is <cite>IPsec</cite>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location/region where the connection is
located. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the connection. Changing the name forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.peer_virtual_network_gateway_id">
<code class="descname">peer_virtual_network_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.peer_virtual_network_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when <cite>type</cite>
is <cite>Vnet2Vnet</cite>). The peer Virtual Network Gateway can be in the same or
in a different subscription.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.routing_weight">
<code class="descname">routing_weight</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.routing_weight" title="Permalink to this definition">¶</a></dt>
<dd><p>The routing weight. Defaults to <cite>10</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.shared_key">
<code class="descname">shared_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.shared_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of connection. Valid options are <cite>IPsec</cite>
(Site-to-Site), <cite>ExpressRoute</cite> (ExpressRoute), and <cite>Vnet2Vnet</cite> (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.use_policy_based_traffic_selectors">
<code class="descname">use_policy_based_traffic_selectors</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.use_policy_based_traffic_selectors" title="Permalink to this definition">¶</a></dt>
<dd><p>If <cite>true</cite>, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an <cite>ipsec_policy</cite> block. Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.virtual_network_gateway_id">
<code class="descname">virtual_network_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.virtual_network_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualNetworkPeering">
<em class="property">class </em><code class="descclassname">pulumi_azure.network.</code><code class="descname">VirtualNetworkPeering</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>allow_forwarded_traffic=None</em>, <em>allow_gateway_transit=None</em>, <em>allow_virtual_network_access=None</em>, <em>name=None</em>, <em>remote_virtual_network_id=None</em>, <em>resource_group_name=None</em>, <em>use_remote_gateways=None</em>, <em>virtual_network_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a virtual network peering which allows resources to access other
resources in the linked virtual network.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allow_forwarded_traffic</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls if forwarded traffic from  VMs
in the remote virtual network is allowed. Defaults to false.</li>
<li><strong>allow_gateway_transit</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls gatewayLinks can be used in the
remote virtual network’s link to the local virtual network.</li>
<li><strong>allow_virtual_network_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls if the VMs in the remote
virtual network can access VMs in the local virtual network. Defaults to
false.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual network peering. Changing this
forces a new resource to be created.</li>
<li><strong>remote_virtual_network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full Azure resource ID of the
remote virtual network.  Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.</li>
<li><strong>use_remote_gateways</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls if remote gateways can be used on
the local virtual network. If the flag is set to <cite>true</cite>, and
<cite>allow_gateway_transit</cite> on the remote peering is also <cite>true</cite>, virtual network will
use gateways of remote virtual network for transit. Only one peering can
have this flag set to <cite>true</cite>. This flag cannot be set if virtual network
already has a gateway. Defaults to <cite>false</cite>.</li>
<li><strong>virtual_network_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual network. Changing
this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkPeering.allow_forwarded_traffic">
<code class="descname">allow_forwarded_traffic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.allow_forwarded_traffic" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls if forwarded traffic from  VMs
in the remote virtual network is allowed. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkPeering.allow_gateway_transit">
<code class="descname">allow_gateway_transit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.allow_gateway_transit" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls gatewayLinks can be used in the
remote virtual network’s link to the local virtual network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkPeering.allow_virtual_network_access">
<code class="descname">allow_virtual_network_access</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.allow_virtual_network_access" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls if the VMs in the remote
virtual network can access VMs in the local virtual network. Defaults to
false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkPeering.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the virtual network peering. Changing this
forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkPeering.remote_virtual_network_id">
<code class="descname">remote_virtual_network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.remote_virtual_network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The full Azure resource ID of the
remote virtual network.  Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkPeering.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkPeering.use_remote_gateways">
<code class="descname">use_remote_gateways</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.use_remote_gateways" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls if remote gateways can be used on
the local virtual network. If the flag is set to <cite>true</cite>, and
<cite>allow_gateway_transit</cite> on the remote peering is also <cite>true</cite>, virtual network will
use gateways of remote virtual network for transit. Only one peering can
have this flag set to <cite>true</cite>. This flag cannot be set if virtual network
already has a gateway. Defaults to <cite>false</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkPeering.virtual_network_name">
<code class="descname">virtual_network_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.virtual_network_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the virtual network. Changing
this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VirtualNetworkPeering.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualNetworkPeering.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.get_application_security_group">
<code class="descclassname">pulumi_azure.network.</code><code class="descname">get_application_security_group</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_application_security_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Application Security Group.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_network_interface">
<code class="descclassname">pulumi_azure.network.</code><code class="descname">get_network_interface</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_network_interface" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Network Interface.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_network_security_group">
<code class="descclassname">pulumi_azure.network.</code><code class="descname">get_network_security_group</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_network_security_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Network Security Group.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_public_i_ps">
<code class="descclassname">pulumi_azure.network.</code><code class="descname">get_public_i_ps</code><span class="sig-paren">(</span><em>allocation_type=None</em>, <em>attached=None</em>, <em>name_prefix=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_public_i_ps" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about a set of existing Public IP Addresses.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_public_ip">
<code class="descclassname">pulumi_azure.network.</code><code class="descname">get_public_ip</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_public_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Public IP Address.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_route_table">
<code class="descclassname">pulumi_azure.network.</code><code class="descname">get_route_table</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_route_table" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Route Table.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_subnet">
<code class="descclassname">pulumi_azure.network.</code><code class="descname">get_subnet</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>virtual_network_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Subnet within a Virtual Network.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_virtual_network">
<code class="descclassname">pulumi_azure.network.</code><code class="descname">get_virtual_network</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_virtual_network" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Virtual Network.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_virtual_network_gateway">
<code class="descclassname">pulumi_azure.network.</code><code class="descname">get_virtual_network_gateway</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_virtual_network_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Virtual Network Gateway.</p>
</dd></dl>

</div>
