<div class="section" id="module-pulumi_azure.lb">
<span id="lb"></span><h1>lb<a class="headerlink" href="#module-pulumi_azure.lb" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.lb.BackendAddressPool">
<em class="property">class </em><code class="descclassname">pulumi_azure.lb.</code><code class="descname">BackendAddressPool</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>loadbalancer_id=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.BackendAddressPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a Load Balancer Backend Address Pool.</p>
<p>&gt; <strong>NOTE:</strong> When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer in which to create the Backend Address Pool.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] location
:param pulumi.Input[str] name: Specifies the name of the Backend Address Pool.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the resource.</p>
<dl class="attribute">
<dt id="pulumi_azure.lb.BackendAddressPool.backend_ip_configurations">
<code class="descname">backend_ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.BackendAddressPool.backend_ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>The Backend IP Configurations associated with this Backend Address Pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.BackendAddressPool.load_balancing_rules">
<code class="descname">load_balancing_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.BackendAddressPool.load_balancing_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>The Load Balancing Rules associated with this Backend Address Pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.BackendAddressPool.loadbalancer_id">
<code class="descname">loadbalancer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.BackendAddressPool.loadbalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Load Balancer in which to create the Backend Address Pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.BackendAddressPool.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.BackendAddressPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Backend Address Pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.BackendAddressPool.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.BackendAddressPool.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.BackendAddressPool.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.BackendAddressPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.BackendAddressPool.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.BackendAddressPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.lb.GetBackendAddressPoolResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.lb.</code><code class="descname">GetBackendAddressPoolResult</code><span class="sig-paren">(</span><em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.GetBackendAddressPoolResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBackendAddressPool.</p>
<dl class="attribute">
<dt id="pulumi_azure.lb.GetBackendAddressPoolResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetBackendAddressPoolResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.lb.GetLBResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.lb.</code><code class="descname">GetLBResult</code><span class="sig-paren">(</span><em>frontend_ip_configurations=None</em>, <em>location=None</em>, <em>private_ip_address=None</em>, <em>private_ip_addresses=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.GetLBResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLB.</p>
<dl class="attribute">
<dt id="pulumi_azure.lb.GetLBResult.frontend_ip_configurations">
<code class="descname">frontend_ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetLBResult.frontend_ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) A <cite>frontend_ip_configuration</cite> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.GetLBResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetLBResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the Load Balancer exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.GetLBResult.private_ip_address">
<code class="descname">private_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetLBResult.private_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Private IP Address to assign to the Load Balancer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.GetLBResult.private_ip_addresses">
<code class="descname">private_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetLBResult.private_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of private IP address assigned to the load balancer in <cite>frontend_ip_configuration</cite> blocks, if any.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.GetLBResult.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetLBResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU of the Load Balancer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.GetLBResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetLBResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.GetLBResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetLBResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.lb.LoadBalancer">
<em class="property">class </em><code class="descclassname">pulumi_azure.lb.</code><code class="descname">LoadBalancer</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>frontend_ip_configurations=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a Load Balancer Resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>frontend_ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <cite>frontend_ip_configuration</cite> block as documented below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure Region where the Load Balancer should be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the frontend ip configuration.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which to create the Load Balancer.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU of the Azure Load Balancer. Accepted values are <cite>Basic</cite> and <cite>Standard</cite>. Defaults to <cite>Basic</cite>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.lb.LoadBalancer.frontend_ip_configurations">
<code class="descname">frontend_ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.frontend_ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>frontend_ip_configuration</cite> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.LoadBalancer.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure Region where the Load Balancer should be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.LoadBalancer.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the frontend ip configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.LoadBalancer.private_ip_address">
<code class="descname">private_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.private_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Private IP Address to assign to the Load Balancer. The last one and first four IPs in any range are reserved and cannot be manually assigned.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.LoadBalancer.private_ip_addresses">
<code class="descname">private_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.private_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of private IP address assigned to the load balancer in <cite>frontend_ip_configuration</cite> blocks, if any.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.LoadBalancer.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which to create the Load Balancer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.LoadBalancer.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU of the Azure Load Balancer. Accepted values are <cite>Basic</cite> and <cite>Standard</cite>. Defaults to <cite>Basic</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.LoadBalancer.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.LoadBalancer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.LoadBalancer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.lb.NatPool">
<em class="property">class </em><code class="descclassname">pulumi_azure.lb.</code><code class="descname">NatPool</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>backend_port=None</em>, <em>frontend_ip_configuration_name=None</em>, <em>frontend_port_end=None</em>, <em>frontend_port_start=None</em>, <em>loadbalancer_id=None</em>, <em>location=None</em>, <em>name=None</em>, <em>protocol=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.NatPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Load Balancer NAT pool.</p>
<p>&gt; <strong>NOTE</strong> When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>backend_port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The port used for the internal endpoint. Possible values range between 1 and 65535, inclusive.</li>
<li><strong>frontend_ip_configuration_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the frontend IP configuration exposing this rule.</li>
<li><strong>frontend_port_end</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The last port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.</li>
<li><strong>frontend_port_start</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The first port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.</li>
<li><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer in which to create the NAT pool.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] location
:param pulumi.Input[str] name: Specifies the name of the NAT pool.
:param pulumi.Input[str] protocol: The transport protocol for the external endpoint. Possible values are <cite>Udp</cite> or <cite>Tcp</cite>.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the resource.</p>
<dl class="attribute">
<dt id="pulumi_azure.lb.NatPool.backend_port">
<code class="descname">backend_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatPool.backend_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port used for the internal endpoint. Possible values range between 1 and 65535, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatPool.frontend_ip_configuration_name">
<code class="descname">frontend_ip_configuration_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatPool.frontend_ip_configuration_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the frontend IP configuration exposing this rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatPool.frontend_port_end">
<code class="descname">frontend_port_end</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatPool.frontend_port_end" title="Permalink to this definition">¶</a></dt>
<dd><p>The last port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatPool.frontend_port_start">
<code class="descname">frontend_port_start</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatPool.frontend_port_start" title="Permalink to this definition">¶</a></dt>
<dd><p>The first port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatPool.loadbalancer_id">
<code class="descname">loadbalancer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatPool.loadbalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Load Balancer in which to create the NAT pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatPool.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the NAT pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatPool.protocol">
<code class="descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatPool.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The transport protocol for the external endpoint. Possible values are <cite>Udp</cite> or <cite>Tcp</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatPool.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatPool.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.NatPool.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.NatPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.NatPool.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.NatPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.lb.NatRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.lb.</code><code class="descname">NatRule</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>backend_port=None</em>, <em>enable_floating_ip=None</em>, <em>frontend_ip_configuration_name=None</em>, <em>frontend_port=None</em>, <em>loadbalancer_id=None</em>, <em>location=None</em>, <em>name=None</em>, <em>protocol=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.NatRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Load Balancer NAT Rule.</p>
<p>&gt; <strong>NOTE</strong> When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>backend_port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The port used for internal connections on the endpoint. Possible values range between 1 and 65535, inclusive.</li>
<li><strong>enable_floating_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables the Floating IP Capacity, required to configure a SQL AlwaysOn Availability Group.</li>
<li><strong>frontend_ip_configuration_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the frontend IP configuration exposing this rule.</li>
<li><strong>frontend_port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 1 and 65534, inclusive.</li>
<li><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer in which to create the NAT Rule.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] location
:param pulumi.Input[str] name: Specifies the name of the NAT Rule.
:param pulumi.Input[str] protocol: The transport protocol for the external endpoint. Possible values are <cite>Udp</cite>, <cite>Tcp</cite> or <cite>All</cite>.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the resource.</p>
<dl class="attribute">
<dt id="pulumi_azure.lb.NatRule.backend_port">
<code class="descname">backend_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatRule.backend_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port used for internal connections on the endpoint. Possible values range between 1 and 65535, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatRule.enable_floating_ip">
<code class="descname">enable_floating_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatRule.enable_floating_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables the Floating IP Capacity, required to configure a SQL AlwaysOn Availability Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatRule.frontend_ip_configuration_name">
<code class="descname">frontend_ip_configuration_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatRule.frontend_ip_configuration_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the frontend IP configuration exposing this rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatRule.frontend_port">
<code class="descname">frontend_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatRule.frontend_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 1 and 65534, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatRule.loadbalancer_id">
<code class="descname">loadbalancer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatRule.loadbalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Load Balancer in which to create the NAT Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the NAT Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatRule.protocol">
<code class="descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatRule.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The transport protocol for the external endpoint. Possible values are <cite>Udp</cite>, <cite>Tcp</cite> or <cite>All</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.NatRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.NatRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.NatRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.NatRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.lb.Probe">
<em class="property">class </em><code class="descclassname">pulumi_azure.lb.</code><code class="descname">Probe</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>interval_in_seconds=None</em>, <em>loadbalancer_id=None</em>, <em>location=None</em>, <em>name=None</em>, <em>number_of_probes=None</em>, <em>port=None</em>, <em>protocol=None</em>, <em>request_path=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.Probe" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a LoadBalancer Probe Resource.</p>
<p>&gt; <strong>NOTE</strong> When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>interval_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The interval, in seconds between probes to the backend endpoint for health status. The default value is 15, the minimum value is 5.</li>
<li><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the LoadBalancer in which to create the NAT Rule.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] location
:param pulumi.Input[str] name: Specifies the name of the Probe.
:param pulumi.Input[int] number_of_probes: The number of failed probe attempts after which the backend endpoint is removed from rotation. The default value is 2. NumberOfProbes multiplied by intervalInSeconds value must be greater or equal to 10.Endpoints are returned to rotation when at least one probe is successful.
:param pulumi.Input[int] port: Port on which the Probe queries the backend endpoint. Possible values range from 1 to 65535, inclusive.
:param pulumi.Input[str] protocol: Specifies the protocol of the end point. Possible values are <cite>Http</cite>, <cite>Https</cite> or <cite>Tcp</cite>. If Tcp is specified, a received ACK is required for the probe to be successful. If Http is specified, a 200 OK response from the specified URI is required for the probe to be successful.
:param pulumi.Input[str] request_path: The URI used for requesting health status from the backend endpoint. Required if protocol is set to Http. Otherwise, it is not allowed.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the resource.</p>
<dl class="attribute">
<dt id="pulumi_azure.lb.Probe.interval_in_seconds">
<code class="descname">interval_in_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Probe.interval_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The interval, in seconds between probes to the backend endpoint for health status. The default value is 15, the minimum value is 5.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Probe.loadbalancer_id">
<code class="descname">loadbalancer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Probe.loadbalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the LoadBalancer in which to create the NAT Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Probe.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Probe.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Probe.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Probe.number_of_probes">
<code class="descname">number_of_probes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Probe.number_of_probes" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of failed probe attempts after which the backend endpoint is removed from rotation. The default value is 2. NumberOfProbes multiplied by intervalInSeconds value must be greater or equal to 10.Endpoints are returned to rotation when at least one probe is successful.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Probe.port">
<code class="descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Probe.port" title="Permalink to this definition">¶</a></dt>
<dd><p>Port on which the Probe queries the backend endpoint. Possible values range from 1 to 65535, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Probe.protocol">
<code class="descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Probe.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the protocol of the end point. Possible values are <cite>Http</cite>, <cite>Https</cite> or <cite>Tcp</cite>. If Tcp is specified, a received ACK is required for the probe to be successful. If Http is specified, a 200 OK response from the specified URI is required for the probe to be successful.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Probe.request_path">
<code class="descname">request_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Probe.request_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI used for requesting health status from the backend endpoint. Required if protocol is set to Http. Otherwise, it is not allowed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Probe.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Probe.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.Probe.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.Probe.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.Probe.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.Probe.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.lb.Rule">
<em class="property">class </em><code class="descclassname">pulumi_azure.lb.</code><code class="descname">Rule</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>backend_address_pool_id=None</em>, <em>backend_port=None</em>, <em>enable_floating_ip=None</em>, <em>frontend_ip_configuration_name=None</em>, <em>frontend_port=None</em>, <em>idle_timeout_in_minutes=None</em>, <em>load_distribution=None</em>, <em>loadbalancer_id=None</em>, <em>location=None</em>, <em>name=None</em>, <em>probe_id=None</em>, <em>protocol=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.Rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Load Balancer Rule.</p>
<p>&gt; <strong>NOTE</strong> When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>backend_address_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A reference to a Backend Address Pool over which this Load Balancing Rule operates.</li>
<li><strong>backend_port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The port used for internal connections on the endpoint. Possible values range between 0 and 65535, inclusive.</li>
<li><strong>enable_floating_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Floating IP is pertinent to failover scenarios: a “floating” IP is reassigned to a secondary server in case the primary server fails. Floating IP is required for SQL AlwaysOn.</li>
<li><strong>frontend_ip_configuration_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the frontend IP configuration to which the rule is associated.</li>
<li><strong>frontend_port</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 0 and 65534, inclusive.</li>
<li><strong>idle_timeout_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies the timeout for the Tcp idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to Tcp.</li>
<li><strong>load_distribution</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the load balancing distribution type to be used by the Load Balancer. Possible values are: <cite>Default</cite> – The load balancer is configured to use a 5 tuple hash to map traffic to available servers. <cite>SourceIP</cite> – The load balancer is configured to use a 2 tuple hash to map traffic to available servers. <cite>SourceIPProtocol</cite> – The load balancer is configured to use a 3 tuple hash to map traffic to available servers. Also known as Session Persistence, where  the options are called <cite>None</cite>, <cite>Client IP</cite> and <cite>Client IP and Protocol</cite> respectively.</li>
<li><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer in which to create the Rule.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] location
:param pulumi.Input[str] name: Specifies the name of the LB Rule.
:param pulumi.Input[str] probe_id: A reference to a Probe used by this Load Balancing Rule.
:param pulumi.Input[str] protocol: The transport protocol for the external endpoint. Possible values are <cite>Tcp</cite>, <cite>Udp</cite> or <cite>All</cite>.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the resource.</p>
<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.backend_address_pool_id">
<code class="descname">backend_address_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.backend_address_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A reference to a Backend Address Pool over which this Load Balancing Rule operates.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.backend_port">
<code class="descname">backend_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.backend_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port used for internal connections on the endpoint. Possible values range between 0 and 65535, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.enable_floating_ip">
<code class="descname">enable_floating_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.enable_floating_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Floating IP is pertinent to failover scenarios: a “floating” IP is reassigned to a secondary server in case the primary server fails. Floating IP is required for SQL AlwaysOn.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.frontend_ip_configuration_name">
<code class="descname">frontend_ip_configuration_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.frontend_ip_configuration_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the frontend IP configuration to which the rule is associated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.frontend_port">
<code class="descname">frontend_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.frontend_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 0 and 65534, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.idle_timeout_in_minutes">
<code class="descname">idle_timeout_in_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.idle_timeout_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the timeout for the Tcp idle connection. The value can be set between 4 and 30 minutes. The default value is 4 minutes. This element is only used when the protocol is set to Tcp.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.load_distribution">
<code class="descname">load_distribution</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.load_distribution" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the load balancing distribution type to be used by the Load Balancer. Possible values are: <cite>Default</cite> – The load balancer is configured to use a 5 tuple hash to map traffic to available servers. <cite>SourceIP</cite> – The load balancer is configured to use a 2 tuple hash to map traffic to available servers. <cite>SourceIPProtocol</cite> – The load balancer is configured to use a 3 tuple hash to map traffic to available servers. Also known as Session Persistence, where  the options are called <cite>None</cite>, <cite>Client IP</cite> and <cite>Client IP and Protocol</cite> respectively.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.loadbalancer_id">
<code class="descname">loadbalancer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.loadbalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Load Balancer in which to create the Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the LB Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.probe_id">
<code class="descname">probe_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.probe_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A reference to a Probe used by this Load Balancing Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.protocol">
<code class="descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The transport protocol for the external endpoint. Possible values are <cite>Tcp</cite>, <cite>Udp</cite> or <cite>All</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.Rule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.Rule.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.Rule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.Rule.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_azure.lb.get_backend_address_pool">
<code class="descclassname">pulumi_azure.lb.</code><code class="descname">get_backend_address_pool</code><span class="sig-paren">(</span><em>loadbalancer_id=None</em>, <em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.get_backend_address_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Load Balancer Backend Address Pool.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.lb.get_lb">
<code class="descclassname">pulumi_azure.lb.</code><code class="descname">get_lb</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.get_lb" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Load Balancer</p>
</dd></dl>

</div>
