<div class="section" id="module-pulumi_openstack.networking">
<span id="networking"></span><h1>networking<a class="headerlink" href="#module-pulumi_openstack.networking" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_openstack.networking.AddressScope">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">AddressScope</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>ip_version=None</em>, <em>name=None</em>, <em>project_id=None</em>, <em>region=None</em>, <em>shared=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AddressScope" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Neutron addressscope resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – IP version, either 4 (default) or 6. Changing this
creates a new address-scope.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the address-scope. Changing this updates the
name of the existing address-scope.</li>
<li><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the address-scope. Required if admin
wants to create a address-scope for another project. Changing this creates a
new address-scope.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron address-scope. If omitted,
the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
address-scope.</li>
<li><strong>shared</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether this address-scope is shared across
all projects. Changing this updates the shared status of the existing
address-scope.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.networking.AddressScope.ip_version">
<code class="descname">ip_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.AddressScope.ip_version" title="Permalink to this definition">¶</a></dt>
<dd><p>IP version, either 4 (default) or 6. Changing this
creates a new address-scope.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.AddressScope.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.AddressScope.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the address-scope. Changing this updates the
name of the existing address-scope.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.AddressScope.project_id">
<code class="descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.AddressScope.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the address-scope. Required if admin
wants to create a address-scope for another project. Changing this creates a
new address-scope.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.AddressScope.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.AddressScope.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron address-scope. If omitted,
the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
address-scope.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.AddressScope.shared">
<code class="descname">shared</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.AddressScope.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether this address-scope is shared across
all projects. Changing this updates the shared status of the existing
address-scope.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.AddressScope.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AddressScope.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.AddressScope.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AddressScope.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.FloatingIp">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">FloatingIp</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>address=None</em>, <em>description=None</em>, <em>fixed_ip=None</em>, <em>pool=None</em>, <em>port_id=None</em>, <em>region=None</em>, <em>subnet_id=None</em>, <em>tags=None</em>, <em>tenant_id=None</em>, <em>value_specs=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 floating IP resource within OpenStack Neutron (networking)
that can be used for load balancers.
These are similar to Nova (compute) floating IP resources,
but only compute floating IPs can be used with compute instances.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The actual/specific floating IP to obtain. By default,
non-admin users are not able to specify a floating IP, so you must either be
an admin user or have had a custom policy or role applied to your OpenStack
user or project.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description for the floating IP.</li>
<li><strong>fixed_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Fixed IP of the port to associate with this floating IP. Required if
the port has multiple fixed IPs.</li>
<li><strong>pool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the pool from which to obtain the floating
IP. Changing this creates a new floating IP.</li>
<li><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of an existing port with at least one IP address to
associate with this floating IP.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a floating IP that can be used with
another networking resource, such as a load balancer. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
floating IP (which may or may not have a different address).</li>
<li><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subnet ID of the floating IP pool. Specify this if
the floating IP network has multiple subnets.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the floating IP.</li>
<li><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target tenant ID in which to allocate the floating
IP, if you specify this together with a port_id, make sure the target port
belongs to the same tenant. Changing this creates a new floating IP (which
may or may not have a different address)</li>
<li><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.address">
<code class="descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The actual/specific floating IP to obtain. By default,
non-admin users are not able to specify a floating IP, so you must either be
an admin user or have had a custom policy or role applied to your OpenStack
user or project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.all_tags">
<code class="descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of tags assigned on the floating IP, which have
been explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description for the floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.fixed_ip">
<code class="descname">fixed_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.fixed_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Fixed IP of the port to associate with this floating IP. Required if
the port has multiple fixed IPs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.pool">
<code class="descname">pool</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.pool" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the pool from which to obtain the floating
IP. Changing this creates a new floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.port_id">
<code class="descname">port_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.port_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of an existing port with at least one IP address to
associate with this floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a floating IP that can be used with
another networking resource, such as a load balancer. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
floating IP (which may or may not have a different address).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The subnet ID of the floating IP pool. Specify this if
the floating IP network has multiple subnets.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags for the floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.tenant_id">
<code class="descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The target tenant ID in which to allocate the floating
IP, if you specify this together with a port_id, make sure the target port
belongs to the same tenant. Changing this creates a new floating IP (which
may or may not have a different address)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.value_specs">
<code class="descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.FloatingIp.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.FloatingIp.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.FloatingIpAssociate">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">FloatingIpAssociate</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>floating_ip=None</em>, <em>port_id=None</em>, <em>region=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.FloatingIpAssociate" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates a floating IP to a port. This is useful for situations
where you have a pre-allocated floating IP or are unable to use the
<code class="docutils literal notranslate"><span class="pre">openstack_networking_floatingip_v2</span></code> resource to create a floating IP.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>floating_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP Address of an existing floating IP.</li>
<li><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of an existing port with at least one IP address to
associate with this floating IP.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a floating IP that can be used with
another networking resource, such as a load balancer. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
floating IP (which may or may not have a different address).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIpAssociate.floating_ip">
<code class="descname">floating_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIpAssociate.floating_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>IP Address of an existing floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIpAssociate.port_id">
<code class="descname">port_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIpAssociate.port_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of an existing port with at least one IP address to
associate with this floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIpAssociate.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIpAssociate.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a floating IP that can be used with
another networking resource, such as a load balancer. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
floating IP (which may or may not have a different address).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.FloatingIpAssociate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.FloatingIpAssociate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.FloatingIpAssociate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.FloatingIpAssociate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.GetFloatingIpResult">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">GetFloatingIpResult</code><span class="sig-paren">(</span><em>all_tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetFloatingIpResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFloatingIp.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetFloatingIpResult.all_tags">
<code class="descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetFloatingIpResult.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags applied on the floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetFloatingIpResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetFloatingIpResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetNetworkResult">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">GetNetworkResult</code><span class="sig-paren">(</span><em>admin_state_up=None</em>, <em>all_tags=None</em>, <em>availability_zone_hints=None</em>, <em>region=None</em>, <em>shared=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetwork.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetNetworkResult.admin_state_up">
<code class="descname">admin_state_up</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) The administrative state of the network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetNetworkResult.all_tags">
<code class="descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of string tags applied on the network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetNetworkResult.availability_zone_hints">
<code class="descname">availability_zone_hints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult.availability_zone_hints" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) The availability zone candidates for the network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetNetworkResult.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetNetworkResult.shared">
<code class="descname">shared</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional)  Specifies whether the network resource can be accessed
by any tenant or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetNetworkResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetPortIdsResult">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">GetPortIdsResult</code><span class="sig-paren">(</span><em>ids=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetPortIdsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPortIds.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortIdsResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortIdsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetPortResult">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">GetPortResult</code><span class="sig-paren">(</span><em>all_fixed_ips=None</em>, <em>all_security_group_ids=None</em>, <em>all_tags=None</em>, <em>allowed_address_pairs=None</em>, <em>extra_dhcp_options=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPort.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.all_fixed_ips">
<code class="descname">all_fixed_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.all_fixed_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of Fixed IP addresses on the port in the
order returned by the Network v2 API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.all_security_group_ids">
<code class="descname">all_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.all_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of security group IDs applied on the port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.all_tags">
<code class="descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of string tags applied on the port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.allowed_address_pairs">
<code class="descname">allowed_address_pairs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.allowed_address_pairs" title="Permalink to this definition">¶</a></dt>
<dd><p>An IP/MAC Address pair of additional IP
addresses that can be active on this port. The structure is described
below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.extra_dhcp_options">
<code class="descname">extra_dhcp_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.extra_dhcp_options" title="Permalink to this definition">¶</a></dt>
<dd><p>An extra DHCP option configured on the port.
The structure is described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetRouterResult">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">GetRouterResult</code><span class="sig-paren">(</span><em>all_tags=None</em>, <em>availability_zone_hints=None</em>, <em>enable_snat=None</em>, <em>external_fixed_ips=None</em>, <em>external_network_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetRouterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRouter.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetRouterResult.all_tags">
<code class="descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetRouterResult.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of string tags applied on the router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetRouterResult.availability_zone_hints">
<code class="descname">availability_zone_hints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetRouterResult.availability_zone_hints" title="Permalink to this definition">¶</a></dt>
<dd><p>The availability zone that is used to make router resources highly available.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetRouterResult.enable_snat">
<code class="descname">enable_snat</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetRouterResult.enable_snat" title="Permalink to this definition">¶</a></dt>
<dd><p>The value that points out if the Source NAT is enabled on the router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetRouterResult.external_fixed_ips">
<code class="descname">external_fixed_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetRouterResult.external_fixed_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>The external fixed IPs of the router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetRouterResult.external_network_id">
<code class="descname">external_network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetRouterResult.external_network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The network UUID of an external gateway for the router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetRouterResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetRouterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetSecGroupResult">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">GetSecGroupResult</code><span class="sig-paren">(</span><em>all_tags=None</em>, <em>region=None</em>, <em>tenant_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetSecGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecGroup.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSecGroupResult.all_tags">
<code class="descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSecGroupResult.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of string tags applied on the security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSecGroupResult.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSecGroupResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSecGroupResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSecGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">GetSubnetPoolResult</code><span class="sig-paren">(</span><em>address_scope_id=None</em>, <em>all_tags=None</em>, <em>created_at=None</em>, <em>default_prefixlen=None</em>, <em>default_quota=None</em>, <em>description=None</em>, <em>ip_version=None</em>, <em>is_default=None</em>, <em>max_prefixlen=None</em>, <em>min_prefixlen=None</em>, <em>name=None</em>, <em>prefixes=None</em>, <em>project_id=None</em>, <em>region=None</em>, <em>revision_number=None</em>, <em>shared=None</em>, <em>updated_at=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSubnetPool.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.address_scope_id">
<code class="descname">address_scope_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.address_scope_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">ip_version</span></code> -The IP protocol version.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.all_tags">
<code class="descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of string tags applied on the subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.created_at">
<code class="descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which subnetpool was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.default_prefixlen">
<code class="descname">default_prefixlen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.default_prefixlen" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.default_quota">
<code class="descname">default_quota</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.default_quota" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.is_default">
<code class="descname">is_default</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.is_default" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.max_prefixlen">
<code class="descname">max_prefixlen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.max_prefixlen" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.min_prefixlen">
<code class="descname">min_prefixlen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.min_prefixlen" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.prefixes">
<code class="descname">prefixes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.prefixes" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.project_id">
<code class="descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.revision_number">
<code class="descname">revision_number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.revision_number" title="Permalink to this definition">¶</a></dt>
<dd><p>The revision number of the subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.shared">
<code class="descname">shared</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.updated_at">
<code class="descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which subnetpool was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetSubnetResult">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">GetSubnetResult</code><span class="sig-paren">(</span><em>all_tags=None</em>, <em>allocation_pools=None</em>, <em>cidr=None</em>, <em>description=None</em>, <em>dns_nameservers=None</em>, <em>enable_dhcp=None</em>, <em>gateway_ip=None</em>, <em>host_routes=None</em>, <em>ip_version=None</em>, <em>ipv6_address_mode=None</em>, <em>ipv6_ra_mode=None</em>, <em>name=None</em>, <em>network_id=None</em>, <em>region=None</em>, <em>subnet_id=None</em>, <em>subnetpool_id=None</em>, <em>tenant_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSubnet.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetResult.all_tags">
<code class="descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetResult.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags applied on the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetResult.allocation_pools">
<code class="descname">allocation_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetResult.allocation_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>Allocation pools of the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetResult.dns_nameservers">
<code class="descname">dns_nameservers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetResult.dns_nameservers" title="Permalink to this definition">¶</a></dt>
<dd><p>DNS Nameservers of the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetResult.enable_dhcp">
<code class="descname">enable_dhcp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetResult.enable_dhcp" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the subnet has DHCP enabled or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetResult.host_routes">
<code class="descname">host_routes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetResult.host_routes" title="Permalink to this definition">¶</a></dt>
<dd><p>Host Routes of the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetResult.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.Network">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">Network</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>admin_state_up=None</em>, <em>availability_zone_hints=None</em>, <em>description=None</em>, <em>external=None</em>, <em>name=None</em>, <em>region=None</em>, <em>segments=None</em>, <em>shared=None</em>, <em>tags=None</em>, <em>tenant_id=None</em>, <em>transparent_vlan=None</em>, <em>value_specs=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Network" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Neutron network resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the network.
Acceptable values are “true” and “false”. Changing this value updates the
state of the existing network.</li>
<li><strong>availability_zone_hints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An availability zone is used to make
network resources highly available. Used for resources with high availability
so that they are scheduled on different availability zones. Changing this
creates a new network.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the network. Changing this
updates the name of the existing network.</li>
<li><strong>external</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the network resource has the
external routing facility. Valid values are true and false. Defaults to
false. Changing this updates the external attribute of the existing network.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the network. Changing this updates the name of
the existing network.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron network. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
network.</li>
<li><strong>segments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of one or more provider segment objects.</li>
<li><strong>shared</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the network resource can be accessed
by any tenant or not. Changing this updates the sharing capabilities of the
existing network.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the network.</li>
<li><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the network. Required if admin wants to
create a network for another tenant. Changing this creates a new network.</li>
<li><strong>transparent_vlan</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the network resource has the
VLAN transparent attribute set. Valid values are true and false. Defaults to
false. Changing this updates the <code class="docutils literal notranslate"><span class="pre">transparent_vlan</span></code> attribute of the existing
network.</li>
<li><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.admin_state_up">
<code class="descname">admin_state_up</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative state of the network.
Acceptable values are “true” and “false”. Changing this value updates the
state of the existing network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.all_tags">
<code class="descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of tags assigned on the network, which have been
explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.availability_zone_hints">
<code class="descname">availability_zone_hints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.availability_zone_hints" title="Permalink to this definition">¶</a></dt>
<dd><p>An availability zone is used to make
network resources highly available. Used for resources with high availability
so that they are scheduled on different availability zones. Changing this
creates a new network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description of the network. Changing this
updates the name of the existing network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.external">
<code class="descname">external</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.external" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the network resource has the
external routing facility. Valid values are true and false. Defaults to
false. Changing this updates the external attribute of the existing network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the network. Changing this updates the name of
the existing network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron network. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.segments">
<code class="descname">segments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.segments" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of one or more provider segment objects.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.shared">
<code class="descname">shared</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the network resource can be accessed
by any tenant or not. Changing this updates the sharing capabilities of the
existing network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags for the network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.tenant_id">
<code class="descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the network. Required if admin wants to
create a network for another tenant. Changing this creates a new network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.transparent_vlan">
<code class="descname">transparent_vlan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.transparent_vlan" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the network resource has the
VLAN transparent attribute set. Valid values are true and false. Defaults to
false. Changing this updates the <code class="docutils literal notranslate"><span class="pre">transparent_vlan</span></code> attribute of the existing
network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.value_specs">
<code class="descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.Network.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Network.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.Network.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Network.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.Port">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">Port</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>admin_state_up=None</em>, <em>allowed_address_pairs=None</em>, <em>description=None</em>, <em>device_id=None</em>, <em>device_owner=None</em>, <em>extra_dhcp_options=None</em>, <em>fixed_ips=None</em>, <em>mac_address=None</em>, <em>name=None</em>, <em>network_id=None</em>, <em>no_fixed_ip=None</em>, <em>no_security_groups=None</em>, <em>region=None</em>, <em>security_group_ids=None</em>, <em>tags=None</em>, <em>tenant_id=None</em>, <em>value_specs=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Port" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 port resource within OpenStack.</p>
<p>There are some notes to consider when connecting Instances to networks using
Ports. Please see the <code class="docutils literal notranslate"><span class="pre">openstack_compute_instance_v2</span></code> documentation for further
documentation.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Administrative up/down status for the port
(must be “true” or “false” if provided). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing port.</li>
<li><strong>allowed_address_pairs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An IP/MAC Address pair of additional IP
addresses that can be active on this port. The structure is described
below.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the floating IP. Changing
this updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing port.</li>
<li><strong>device_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the device attached to the port. Changing this
creates a new port.</li>
<li><strong>device_owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The device owner of the Port. Changing this creates
a new port.</li>
<li><strong>extra_dhcp_options</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An extra DHCP option that needs to be configured
on the port. The structure is described below. Can be specified multiple
times.</li>
<li><strong>fixed_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of desired IPs for
this port. The structure is described below.</li>
<li><strong>mac_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a specific MAC address for the port. Changing
this creates a new port.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the port. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing port.</li>
<li><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the network to attach the port to. Changing
this creates a new port.</li>
<li><strong>no_fixed_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Create a port with no fixed
IP address. This will also remove any fixed IPs previously set on a port. <code class="docutils literal notranslate"><span class="pre">true</span></code>
is the only valid value for this argument.</li>
<li><strong>no_security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to
<code class="docutils literal notranslate"><span class="pre">true</span></code>, then no security groups are applied to the port. If set to <code class="docutils literal notranslate"><span class="pre">false</span></code> and
no <code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> are specified, then the Port will yield to the default
behavior of the Networking service, which is to usually apply the “default”
security group.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
port.</li>
<li><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list
of security group IDs to apply to the port. The security groups must be
specified by ID and not name (as opposed to how they are configured with
the Compute Instance).</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Argument Reference above.</li>
<li><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the Port. Required if admin wants
to create a port for another tenant. Changing this creates a new port.</li>
<li><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.admin_state_up">
<code class="descname">admin_state_up</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>Administrative up/down status for the port
(must be “true” or “false” if provided). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.all_fixed_ips">
<code class="descname">all_fixed_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.all_fixed_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of Fixed IP addresses on the port in the
order returned by the Network v2 API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.all_security_group_ids">
<code class="descname">all_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.all_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of Security Group IDs on the port
which have been explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.all_tags">
<code class="descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of tags assigned on the port, which have been
explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.allowed_address_pairs">
<code class="descname">allowed_address_pairs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.allowed_address_pairs" title="Permalink to this definition">¶</a></dt>
<dd><p>An IP/MAC Address pair of additional IP
addresses that can be active on this port. The structure is described
below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description of the floating IP. Changing
this updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.device_id">
<code class="descname">device_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.device_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the device attached to the port. Changing this
creates a new port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.device_owner">
<code class="descname">device_owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.device_owner" title="Permalink to this definition">¶</a></dt>
<dd><p>The device owner of the Port. Changing this creates
a new port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.extra_dhcp_options">
<code class="descname">extra_dhcp_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.extra_dhcp_options" title="Permalink to this definition">¶</a></dt>
<dd><p>An extra DHCP option that needs to be configured
on the port. The structure is described below. Can be specified multiple
times.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.fixed_ips">
<code class="descname">fixed_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.fixed_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of desired IPs for
this port. The structure is described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.mac_address">
<code class="descname">mac_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.mac_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify a specific MAC address for the port. Changing
this creates a new port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the port. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.network_id">
<code class="descname">network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the network to attach the port to. Changing
this creates a new port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.no_fixed_ip">
<code class="descname">no_fixed_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.no_fixed_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a port with no fixed
IP address. This will also remove any fixed IPs previously set on a port. <code class="docutils literal notranslate"><span class="pre">true</span></code>
is the only valid value for this argument.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.no_security_groups">
<code class="descname">no_security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.no_security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to
<code class="docutils literal notranslate"><span class="pre">true</span></code>, then no security groups are applied to the port. If set to <code class="docutils literal notranslate"><span class="pre">false</span></code> and
no <code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> are specified, then the Port will yield to the default
behavior of the Networking service, which is to usually apply the “default”
security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.security_group_ids">
<code class="descname">security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list
of security group IDs to apply to the port. The security groups must be
specified by ID and not name (as opposed to how they are configured with
the Compute Instance).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.tenant_id">
<code class="descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the Port. Required if admin wants
to create a port for another tenant. Changing this creates a new port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.value_specs">
<code class="descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.Port.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Port.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.Port.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Port.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.PortSecGroupAssociate">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">PortSecGroupAssociate</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>enforce=None</em>, <em>port_id=None</em>, <em>region=None</em>, <em>security_group_ids=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.PortSecGroupAssociate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 port’s security groups within OpenStack. Useful, when the port was
created not by Terraform (e.g. Manila or LBaaS). It should not be used, when the
port was created directly within Terraform.</p>
<p>When the resource is deleted, Terraform doesn’t delete the port, but unsets the
list of user defined security group IDs.  However, if <code class="docutils literal notranslate"><span class="pre">enforce</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>
and the resource is deleted, Terraform will remove all assigned security group
IDs.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>enforce</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to replace or append the list of security
groups, specified in the <code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An UUID of the port to apply security groups to.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to manage a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
resource.</li>
<li><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security group IDs to apply to
the port. The security groups must be specified by ID and not name (as
opposed to how they are configured with the Compute Instance).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.networking.PortSecGroupAssociate.all_security_group_ids">
<code class="descname">all_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.PortSecGroupAssociate.all_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of Security Group IDs on the port
which have been explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.PortSecGroupAssociate.enforce">
<code class="descname">enforce</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.PortSecGroupAssociate.enforce" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to replace or append the list of security
groups, specified in the <code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.PortSecGroupAssociate.port_id">
<code class="descname">port_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.PortSecGroupAssociate.port_id" title="Permalink to this definition">¶</a></dt>
<dd><p>An UUID of the port to apply security groups to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.PortSecGroupAssociate.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.PortSecGroupAssociate.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to manage a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.PortSecGroupAssociate.security_group_ids">
<code class="descname">security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.PortSecGroupAssociate.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of security group IDs to apply to
the port. The security groups must be specified by ID and not name (as
opposed to how they are configured with the Compute Instance).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.PortSecGroupAssociate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.PortSecGroupAssociate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.PortSecGroupAssociate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.PortSecGroupAssociate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.Router">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">Router</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>admin_state_up=None</em>, <em>availability_zone_hints=None</em>, <em>description=None</em>, <em>distributed=None</em>, <em>enable_snat=None</em>, <em>external_fixed_ips=None</em>, <em>external_gateway=None</em>, <em>external_network_id=None</em>, <em>name=None</em>, <em>region=None</em>, <em>tags=None</em>, <em>tenant_id=None</em>, <em>value_specs=None</em>, <em>vendor_options=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Router" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 router resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Administrative up/down status for the router
(must be “true” or “false” if provided). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing router.</li>
<li><strong>availability_zone_hints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An availability zone is used to make 
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description for the router.</li>
<li><strong>distributed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.</li>
<li><strong>enable_snat</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable Source NAT for the router. Valid values are
“true” or “false”. An <code class="docutils literal notranslate"><span class="pre">external_network_id</span></code> has to be set in order to
set this property. Changing this updates the <code class="docutils literal notranslate"><span class="pre">enable_snat</span></code> of the router.</li>
<li><strong>external_fixed_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An external fixed IP for the router. This
can be repeated. The structure is described below. An <code class="docutils literal notranslate"><span class="pre">external_network_id</span></code>
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.</li>
<li><strong>external_gateway</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.</li>
<li><strong>external_network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the router. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing router.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
router.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the router.</li>
<li><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.</li>
<li><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional driver-specific options.</li>
<li><strong>vendor_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional vendor-specific options.
Supported options are described below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.admin_state_up">
<code class="descname">admin_state_up</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>Administrative up/down status for the router
(must be “true” or “false” if provided). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.all_tags">
<code class="descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of tags assigned on the router, which have been
explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.availability_zone_hints">
<code class="descname">availability_zone_hints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.availability_zone_hints" title="Permalink to this definition">¶</a></dt>
<dd><p>An availability zone is used to make 
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description for the router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.distributed">
<code class="descname">distributed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.distributed" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.enable_snat">
<code class="descname">enable_snat</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.enable_snat" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable Source NAT for the router. Valid values are
“true” or “false”. An <code class="docutils literal notranslate"><span class="pre">external_network_id</span></code> has to be set in order to
set this property. Changing this updates the <code class="docutils literal notranslate"><span class="pre">enable_snat</span></code> of the router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.external_fixed_ips">
<code class="descname">external_fixed_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.external_fixed_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>An external fixed IP for the router. This
can be repeated. The structure is described below. An <code class="docutils literal notranslate"><span class="pre">external_network_id</span></code>
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.external_gateway">
<code class="descname">external_gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.external_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.external_network_id">
<code class="descname">external_network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.external_network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the router. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags for the router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.tenant_id">
<code class="descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.value_specs">
<code class="descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional driver-specific options.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.vendor_options">
<code class="descname">vendor_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.vendor_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional vendor-specific options.
Supported options are described below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.Router.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Router.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.Router.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Router.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.RouterInterface">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">RouterInterface</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>port_id=None</em>, <em>region=None</em>, <em>router_id=None</em>, <em>subnet_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.RouterInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 router interface resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the port this interface connects to. Changing
this creates a new router interface.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
router interface.</li>
<li><strong>router_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the router this interface belongs to. Changing
this creates a new router interface.</li>
<li><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the subnet this interface connects to. Changing
this creates a new router interface.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.networking.RouterInterface.port_id">
<code class="descname">port_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RouterInterface.port_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the port this interface connects to. Changing
this creates a new router interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.RouterInterface.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RouterInterface.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
router interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.RouterInterface.router_id">
<code class="descname">router_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RouterInterface.router_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the router this interface belongs to. Changing
this creates a new router interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.RouterInterface.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RouterInterface.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the subnet this interface connects to. Changing
this creates a new router interface.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.RouterInterface.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.RouterInterface.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.RouterInterface.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.RouterInterface.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.RouterRoute">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">RouterRoute</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>destination_cidr=None</em>, <em>next_hop=None</em>, <em>region=None</em>, <em>router_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.RouterRoute" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a routing entry on a OpenStack V2 router.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">next_hop</span></code> IP address must be directly reachable from the router at the <code class="docutils literal notranslate"><span class="pre">openstack_networking_router_route_v2</span></code>
resource creation time.  You can ensure that by explicitly specifying a dependency on the <code class="docutils literal notranslate"><span class="pre">openstack_networking_router_interface_v2</span></code>
resource that connects the next hop to the router, as in the example above.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>destination_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CIDR block to match on the packet’s destination IP. Changing
this creates a new routing entry.</li>
<li><strong>next_hop</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address of the next hop gateway.  Changing
this creates a new routing entry.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a router. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
routing entry.</li>
<li><strong>router_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the router this routing entry belongs to. Changing
this creates a new routing entry.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.networking.RouterRoute.destination_cidr">
<code class="descname">destination_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RouterRoute.destination_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR block to match on the packet’s destination IP. Changing
this creates a new routing entry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.RouterRoute.next_hop">
<code class="descname">next_hop</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RouterRoute.next_hop" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address of the next hop gateway.  Changing
this creates a new routing entry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.RouterRoute.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RouterRoute.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a router. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
routing entry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.RouterRoute.router_id">
<code class="descname">router_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RouterRoute.router_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the router this routing entry belongs to. Changing
this creates a new routing entry.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.RouterRoute.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.RouterRoute.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.RouterRoute.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.RouterRoute.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.SecGroup">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">SecGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>delete_default_rules=None</em>, <em>description=None</em>, <em>name=None</em>, <em>region=None</em>, <em>tags=None</em>, <em>tenant_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SecGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 neutron security group resource within OpenStack.
Unlike Nova security groups, neutron separates the group from the rules
and also allows an admin to target a specific tenant_id.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>delete_default_rules</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to delete the default
egress security rules. This is <code class="docutils literal notranslate"><span class="pre">false</span></code> by default. See the below note
for more information.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the security group.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the security group.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
security group.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the security group.</li>
<li><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the security group. Required if admin
wants to create a port for another tenant. Changing this creates a new
security group.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroup.all_tags">
<code class="descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of tags assigned on the security group, which have
been explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroup.delete_default_rules">
<code class="descname">delete_default_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.delete_default_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to delete the default
egress security rules. This is <code class="docutils literal notranslate"><span class="pre">false</span></code> by default. See the below note
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroup.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroup.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags for the security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroup.tenant_id">
<code class="descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the security group. Required if admin
wants to create a port for another tenant. Changing this creates a new
security group.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.SecGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.SecGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.SecGroupRule">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">SecGroupRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>direction=None</em>, <em>ethertype=None</em>, <em>port_range_max=None</em>, <em>port_range_min=None</em>, <em>protocol=None</em>, <em>region=None</em>, <em>remote_group_id=None</em>, <em>remote_ip_prefix=None</em>, <em>security_group_id=None</em>, <em>tenant_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 neutron security group rule resource within OpenStack.
Unlike Nova security groups, neutron separates the group from the rules
and also allows an admin to target a specific tenant_id.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the rule. Changing this creates a new security group rule.</li>
<li><strong>direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The direction of the rule, valid values are <strong>ingress</strong>
or <strong>egress</strong>. Changing this creates a new security group rule.</li>
<li><strong>ethertype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The layer 3 protocol type, valid values are <strong>IPv4</strong>
or <strong>IPv6</strong>. Changing this creates a new security group rule.</li>
<li><strong>port_range_max</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The higher part of the allowed port range, valid
integer value needs to be between 1 and 65535. Changing this creates a new
security group rule.</li>
<li><strong>port_range_min</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The lower part of the allowed port range, valid
integer value needs to be between 1 and 65535. Changing this creates a new
security group rule.</li>
<li><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The layer 4 protocol type, valid values are following. Changing this creates a new security group rule. This is required if you want to specify a port range.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
security group rule.</li>
<li><strong>remote_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The remote group id, the value needs to be an
Openstack ID of a security group in the same tenant. Changing this creates
a new security group rule.</li>
<li><strong>remote_ip_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The remote CIDR, the value needs to be a valid
CIDR (i.e. 192.168.0.0/16). Changing this creates a new security group rule.</li>
<li><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security group id the rule should belong
to, the value needs to be an Openstack ID of a security group in the same
tenant. Changing this creates a new security group rule.</li>
<li><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the security group. Required if admin
wants to create a port for another tenant. Changing this creates a new
security group rule.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the rule. Changing this creates a new security group rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.direction">
<code class="descname">direction</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.direction" title="Permalink to this definition">¶</a></dt>
<dd><p>The direction of the rule, valid values are <strong>ingress</strong>
or <strong>egress</strong>. Changing this creates a new security group rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.ethertype">
<code class="descname">ethertype</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.ethertype" title="Permalink to this definition">¶</a></dt>
<dd><p>The layer 3 protocol type, valid values are <strong>IPv4</strong>
or <strong>IPv6</strong>. Changing this creates a new security group rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.port_range_max">
<code class="descname">port_range_max</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.port_range_max" title="Permalink to this definition">¶</a></dt>
<dd><p>The higher part of the allowed port range, valid
integer value needs to be between 1 and 65535. Changing this creates a new
security group rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.port_range_min">
<code class="descname">port_range_min</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.port_range_min" title="Permalink to this definition">¶</a></dt>
<dd><p>The lower part of the allowed port range, valid
integer value needs to be between 1 and 65535. Changing this creates a new
security group rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.protocol">
<code class="descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The layer 4 protocol type, valid values are following. Changing this creates a new security group rule. This is required if you want to specify a port range.</p>
<ul class="simple">
<li><strong>tcp</strong></li>
<li><strong>udp</strong></li>
<li><strong>icmp</strong></li>
<li><strong>ah</strong></li>
<li><strong>dccp</strong></li>
<li><strong>egp</strong></li>
<li><strong>esp</strong></li>
<li><strong>gre</strong></li>
<li><strong>igmp</strong></li>
<li><strong>ipv6-encap</strong></li>
<li><strong>ipv6-frag</strong></li>
<li><strong>ipv6-icmp</strong></li>
<li><strong>ipv6-nonxt</strong></li>
<li><strong>ipv6-opts</strong></li>
<li><strong>ipv6-route</strong></li>
<li><strong>ospf</strong></li>
<li><strong>pgm</strong></li>
<li><strong>rsvp</strong></li>
<li><strong>sctp</strong></li>
<li><strong>udplite</strong></li>
<li><strong>vrrp</strong></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
security group rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.remote_group_id">
<code class="descname">remote_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.remote_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The remote group id, the value needs to be an
Openstack ID of a security group in the same tenant. Changing this creates
a new security group rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.remote_ip_prefix">
<code class="descname">remote_ip_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.remote_ip_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The remote CIDR, the value needs to be a valid
CIDR (i.e. 192.168.0.0/16). Changing this creates a new security group rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.security_group_id">
<code class="descname">security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The security group id the rule should belong
to, the value needs to be an Openstack ID of a security group in the same
tenant. Changing this creates a new security group rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.tenant_id">
<code class="descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the security group. Required if admin
wants to create a port for another tenant. Changing this creates a new
security group rule.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.SecGroupRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.SecGroupRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.Subnet">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">Subnet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allocation_pools=None</em>, <em>cidr=None</em>, <em>description=None</em>, <em>dns_nameservers=None</em>, <em>enable_dhcp=None</em>, <em>gateway_ip=None</em>, <em>host_routes=None</em>, <em>ip_version=None</em>, <em>ipv6_address_mode=None</em>, <em>ipv6_ra_mode=None</em>, <em>name=None</em>, <em>network_id=None</em>, <em>no_gateway=None</em>, <em>region=None</em>, <em>subnetpool_id=None</em>, <em>tags=None</em>, <em>tenant_id=None</em>, <em>value_specs=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Neutron subnet resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allocation_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of sub-ranges of CIDR available for
dynamic allocation to ports. The allocation_pool object structure is
documented below. Changing this creates a new subnet.</li>
<li><strong>cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the subnet. Changing this
updates the name of the existing subnet.</li>
<li><strong>dns_nameservers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.</li>
<li><strong>enable_dhcp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the network.
Acceptable values are “true” and “false”. Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.</li>
<li><strong>gateway_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default gateway used by devices in this subnet.
Leaving this blank and not setting <code class="docutils literal notranslate"><span class="pre">no_gateway</span></code> will cause a default
gateway of <code class="docutils literal notranslate"><span class="pre">.1</span></code> to be used. Changing this updates the gateway IP of the
existing subnet.</li>
<li><strong>host_routes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.</li>
<li><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – IP version, either 4 (default) or 6. Changing this creates a
new subnet.</li>
<li><strong>ipv6_address_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv6 address mode. Valid values are
<code class="docutils literal notranslate"><span class="pre">dhcpv6-stateful</span></code>, <code class="docutils literal notranslate"><span class="pre">dhcpv6-stateless</span></code>, or <code class="docutils literal notranslate"><span class="pre">slaac</span></code>.</li>
<li><strong>ipv6_ra_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv6 Router Advertisement mode. Valid values
are <code class="docutils literal notranslate"><span class="pre">dhcpv6-stateful</span></code>, <code class="docutils literal notranslate"><span class="pre">dhcpv6-stateless</span></code>, or <code class="docutils literal notranslate"><span class="pre">slaac</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnet. Changing this updates the name of
the existing subnet.</li>
<li><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of the parent network. Changing this
creates a new subnet.</li>
<li><strong>no_gateway</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
subnet.</li>
<li><strong>subnetpool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnetpool associated with the subnet.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the subnet.</li>
<li><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.</li>
<li><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.all_tags">
<code class="descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of ags assigned on the subnet, which have been
explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.allocation_pools">
<code class="descname">allocation_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.allocation_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of sub-ranges of CIDR available for
dynamic allocation to ports. The allocation_pool object structure is
documented below. Changing this creates a new subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.cidr">
<code class="descname">cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description of the subnet. Changing this
updates the name of the existing subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.dns_nameservers">
<code class="descname">dns_nameservers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.dns_nameservers" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.enable_dhcp">
<code class="descname">enable_dhcp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.enable_dhcp" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative state of the network.
Acceptable values are “true” and “false”. Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.gateway_ip">
<code class="descname">gateway_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.gateway_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Default gateway used by devices in this subnet.
Leaving this blank and not setting <code class="docutils literal notranslate"><span class="pre">no_gateway</span></code> will cause a default
gateway of <code class="docutils literal notranslate"><span class="pre">.1</span></code> to be used. Changing this updates the gateway IP of the
existing subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.host_routes">
<code class="descname">host_routes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.host_routes" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.ip_version">
<code class="descname">ip_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.ip_version" title="Permalink to this definition">¶</a></dt>
<dd><p>IP version, either 4 (default) or 6. Changing this creates a
new subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.ipv6_address_mode">
<code class="descname">ipv6_address_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.ipv6_address_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv6 address mode. Valid values are
<code class="docutils literal notranslate"><span class="pre">dhcpv6-stateful</span></code>, <code class="docutils literal notranslate"><span class="pre">dhcpv6-stateless</span></code>, or <code class="docutils literal notranslate"><span class="pre">slaac</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.ipv6_ra_mode">
<code class="descname">ipv6_ra_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.ipv6_ra_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv6 Router Advertisement mode. Valid values
are <code class="docutils literal notranslate"><span class="pre">dhcpv6-stateful</span></code>, <code class="docutils literal notranslate"><span class="pre">dhcpv6-stateless</span></code>, or <code class="docutils literal notranslate"><span class="pre">slaac</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the subnet. Changing this updates the name of
the existing subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.network_id">
<code class="descname">network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of the parent network. Changing this
creates a new subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.no_gateway">
<code class="descname">no_gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.no_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.subnetpool_id">
<code class="descname">subnetpool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.subnetpool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the subnetpool associated with the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags for the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.tenant_id">
<code class="descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.value_specs">
<code class="descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.Subnet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Subnet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.Subnet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Subnet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.SubnetPool">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">SubnetPool</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>address_scope_id=None</em>, <em>default_prefixlen=None</em>, <em>default_quota=None</em>, <em>description=None</em>, <em>ip_version=None</em>, <em>is_default=None</em>, <em>max_prefixlen=None</em>, <em>min_prefixlen=None</em>, <em>name=None</em>, <em>prefixes=None</em>, <em>project_id=None</em>, <em>region=None</em>, <em>shared=None</em>, <em>tags=None</em>, <em>value_specs=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Neutron subnetpool resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>address_scope_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Neutron address scope to assign to the
subnetpool. Changing this updates the address scope id of the existing
subnetpool.</li>
<li><strong>default_prefixlen</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The size of the prefix to allocate when the cidr
or prefixlen attributes are omitted when you create the subnet. Defaults to the
MinPrefixLen. Changing this updates the default prefixlen of the existing
subnetpool.</li>
<li><strong>default_quota</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The per-project quota on the prefix space that can be
allocated from the subnetpool for project subnets. Changing this updates the
default quota of the existing subnetpool.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the subnetpool.
Changing this updates the description of the existing subnetpool.</li>
<li><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The IP protocol version.</li>
<li><strong>is_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the subnetpool is default
subnetpool or not. Changing this updates the default status of the existing
subnetpool.</li>
<li><strong>max_prefixlen</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum prefix size that can be allocated from
the subnetpool. For IPv4 subnetpools, default is 32. For IPv6 subnetpools,
default is 128. Changing this updates the max prefixlen of the existing
subnetpool.</li>
<li><strong>min_prefixlen</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The smallest prefix that can be allocated from a
subnetpool. For IPv4 subnetpools, default is 8. For IPv6 subnetpools, default
is 64. Changing this updates the min prefixlen of the existing subnetpool.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnetpool. Changing this updates the name of
the existing subnetpool.</li>
<li><strong>prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of subnet prefixes to assign to the subnetpool.
Neutron API merges adjacent prefixes and treats them as a single prefix. Each
subnet prefix must be unique among all subnet prefixes in all subnetpools that
are associated with the address scope. Changing this updates the prefixes list
of the existing subnetpool.</li>
<li><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the subnetpool. Required if admin wants to
create a subnetpool for another project. Changing this creates a new subnetpool.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnetpool. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
subnetpool.</li>
<li><strong>shared</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether this subnetpool is shared across
all projects. Changing this updates the shared status of the existing
subnetpool.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the subnetpool.</li>
<li><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.address_scope_id">
<code class="descname">address_scope_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.address_scope_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Neutron address scope to assign to the
subnetpool. Changing this updates the address scope id of the existing
subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.all_tags">
<code class="descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of tags assigned on the subnetpool, which have been
explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.created_at">
<code class="descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which subnetpool was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.default_prefixlen">
<code class="descname">default_prefixlen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.default_prefixlen" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the prefix to allocate when the cidr
or prefixlen attributes are omitted when you create the subnet. Defaults to the
MinPrefixLen. Changing this updates the default prefixlen of the existing
subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.default_quota">
<code class="descname">default_quota</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.default_quota" title="Permalink to this definition">¶</a></dt>
<dd><p>The per-project quota on the prefix space that can be
allocated from the subnetpool for project subnets. Changing this updates the
default quota of the existing subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable description for the subnetpool.
Changing this updates the description of the existing subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.ip_version">
<code class="descname">ip_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.ip_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP protocol version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.is_default">
<code class="descname">is_default</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.is_default" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the subnetpool is default
subnetpool or not. Changing this updates the default status of the existing
subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.max_prefixlen">
<code class="descname">max_prefixlen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.max_prefixlen" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum prefix size that can be allocated from
the subnetpool. For IPv4 subnetpools, default is 32. For IPv6 subnetpools,
default is 128. Changing this updates the max prefixlen of the existing
subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.min_prefixlen">
<code class="descname">min_prefixlen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.min_prefixlen" title="Permalink to this definition">¶</a></dt>
<dd><p>The smallest prefix that can be allocated from a
subnetpool. For IPv4 subnetpools, default is 8. For IPv6 subnetpools, default
is 64. Changing this updates the min prefixlen of the existing subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the subnetpool. Changing this updates the name of
the existing subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.prefixes">
<code class="descname">prefixes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.prefixes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of subnet prefixes to assign to the subnetpool.
Neutron API merges adjacent prefixes and treats them as a single prefix. Each
subnet prefix must be unique among all subnet prefixes in all subnetpools that
are associated with the address scope. Changing this updates the prefixes list
of the existing subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.project_id">
<code class="descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the subnetpool. Required if admin wants to
create a subnetpool for another project. Changing this creates a new subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnetpool. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.revision_number">
<code class="descname">revision_number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.revision_number" title="Permalink to this definition">¶</a></dt>
<dd><p>The revision number of the subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.shared">
<code class="descname">shared</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether this subnetpool is shared across
all projects. Changing this updates the shared status of the existing
subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags for the subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.updated_at">
<code class="descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which subnetpool was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.value_specs">
<code class="descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.SubnetPool.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.SubnetPool.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.SubnetRoute">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">SubnetRoute</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>destination_cidr=None</em>, <em>next_hop=None</em>, <em>region=None</em>, <em>subnet_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SubnetRoute" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a routing entry on a OpenStack V2 subnet.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>destination_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CIDR block to match on the packet’s destination IP. Changing
this creates a new routing entry.</li>
<li><strong>next_hop</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address of the next hop gateway.  Changing
this creates a new routing entry.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a subnet. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
routing entry.</li>
<li><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the subnet this routing entry belongs to. Changing
this creates a new routing entry.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetRoute.destination_cidr">
<code class="descname">destination_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetRoute.destination_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR block to match on the packet’s destination IP. Changing
this creates a new routing entry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetRoute.next_hop">
<code class="descname">next_hop</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetRoute.next_hop" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address of the next hop gateway.  Changing
this creates a new routing entry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetRoute.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetRoute.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a subnet. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
routing entry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetRoute.subnet_id">
<code class="descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetRoute.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the subnet this routing entry belongs to. Changing
this creates a new routing entry.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.SubnetRoute.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SubnetRoute.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.SubnetRoute.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SubnetRoute.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.Trunk">
<em class="property">class </em><code class="descclassname">pulumi_openstack.networking.</code><code class="descname">Trunk</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>admin_state_up=None</em>, <em>description=None</em>, <em>name=None</em>, <em>port_id=None</em>, <em>region=None</em>, <em>sub_ports=None</em>, <em>tags=None</em>, <em>tenant_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Trunk" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a networking V2 trunk resource within OpenStack.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Administrative up/down status for the trunk
(must be “true” or “false” if provided). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing trunk.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the trunk. Changing this
updates the name of the existing trunk.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the trunk. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing trunk.</li>
<li><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the port to be used as the parent port of the
trunk. This is the port that should be used as the compute instance network
port. Changing this creates a new trunk.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to create a trunk. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
trunk.</li>
<li><strong>sub_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The set of ports that will be made subports of the trunk.
The structure of each subport is described below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the port.</li>
<li><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the Trunk. Required if admin wants
to create a trunk on behalf of another tenant. Changing this creates a new trunk.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_openstack.networking.Trunk.admin_state_up">
<code class="descname">admin_state_up</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Trunk.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>Administrative up/down status for the trunk
(must be “true” or “false” if provided). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing trunk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Trunk.all_tags">
<code class="descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Trunk.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of tags assigned on the trunk, which have been
explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Trunk.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Trunk.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description of the trunk. Changing this
updates the name of the existing trunk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Trunk.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Trunk.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the trunk. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing trunk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Trunk.port_id">
<code class="descname">port_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Trunk.port_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the port to be used as the parent port of the
trunk. This is the port that should be used as the compute instance network
port. Changing this creates a new trunk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Trunk.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Trunk.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to create a trunk. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
trunk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Trunk.sub_ports">
<code class="descname">sub_ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Trunk.sub_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of ports that will be made subports of the trunk.
The structure of each subport is described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Trunk.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Trunk.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags for the port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Trunk.tenant_id">
<code class="descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Trunk.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the Trunk. Required if admin wants
to create a trunk on behalf of another tenant. Changing this creates a new trunk.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.Trunk.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Trunk.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.Trunk.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Trunk.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.get_floating_ip">
<code class="descclassname">pulumi_openstack.networking.</code><code class="descname">get_floating_ip</code><span class="sig-paren">(</span><em>address=None</em>, <em>description=None</em>, <em>fixed_ip=None</em>, <em>pool=None</em>, <em>port_id=None</em>, <em>region=None</em>, <em>status=None</em>, <em>tags=None</em>, <em>tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_floating_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack floating IP.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_network">
<code class="descclassname">pulumi_openstack.networking.</code><code class="descname">get_network</code><span class="sig-paren">(</span><em>description=None</em>, <em>external=None</em>, <em>matching_subnet_cidr=None</em>, <em>name=None</em>, <em>network_id=None</em>, <em>region=None</em>, <em>status=None</em>, <em>tags=None</em>, <em>tenant_id=None</em>, <em>transparent_vlan=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_network" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack network.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_port">
<code class="descclassname">pulumi_openstack.networking.</code><code class="descname">get_port</code><span class="sig-paren">(</span><em>admin_state_up=None</em>, <em>description=None</em>, <em>device_id=None</em>, <em>device_owner=None</em>, <em>fixed_ip=None</em>, <em>mac_address=None</em>, <em>name=None</em>, <em>network_id=None</em>, <em>port_id=None</em>, <em>project_id=None</em>, <em>region=None</em>, <em>security_group_ids=None</em>, <em>status=None</em>, <em>tags=None</em>, <em>tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack port.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_port_ids">
<code class="descclassname">pulumi_openstack.networking.</code><code class="descname">get_port_ids</code><span class="sig-paren">(</span><em>admin_state_up=None</em>, <em>description=None</em>, <em>device_id=None</em>, <em>device_owner=None</em>, <em>fixed_ip=None</em>, <em>mac_address=None</em>, <em>name=None</em>, <em>network_id=None</em>, <em>project_id=None</em>, <em>region=None</em>, <em>security_group_ids=None</em>, <em>sort_direction=None</em>, <em>sort_key=None</em>, <em>status=None</em>, <em>tags=None</em>, <em>tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_port_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get a list of Openstack Port IDs matching the
specified criteria.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_router">
<code class="descclassname">pulumi_openstack.networking.</code><code class="descname">get_router</code><span class="sig-paren">(</span><em>admin_state_up=None</em>, <em>description=None</em>, <em>distributed=None</em>, <em>enable_snat=None</em>, <em>name=None</em>, <em>region=None</em>, <em>router_id=None</em>, <em>status=None</em>, <em>tags=None</em>, <em>tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_router" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack router.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_sec_group">
<code class="descclassname">pulumi_openstack.networking.</code><code class="descname">get_sec_group</code><span class="sig-paren">(</span><em>description=None</em>, <em>name=None</em>, <em>region=None</em>, <em>secgroup_id=None</em>, <em>tags=None</em>, <em>tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_sec_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack security group.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_subnet">
<code class="descclassname">pulumi_openstack.networking.</code><code class="descname">get_subnet</code><span class="sig-paren">(</span><em>cidr=None</em>, <em>description=None</em>, <em>dhcp_disabled=None</em>, <em>dhcp_enabled=None</em>, <em>gateway_ip=None</em>, <em>ip_version=None</em>, <em>ipv6_address_mode=None</em>, <em>ipv6_ra_mode=None</em>, <em>name=None</em>, <em>network_id=None</em>, <em>region=None</em>, <em>subnet_id=None</em>, <em>subnetpool_id=None</em>, <em>tags=None</em>, <em>tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack subnet.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_subnet_pool">
<code class="descclassname">pulumi_openstack.networking.</code><code class="descname">get_subnet_pool</code><span class="sig-paren">(</span><em>address_scope_id=None</em>, <em>default_prefixlen=None</em>, <em>default_quota=None</em>, <em>description=None</em>, <em>ip_version=None</em>, <em>is_default=None</em>, <em>max_prefixlen=None</em>, <em>min_prefixlen=None</em>, <em>name=None</em>, <em>project_id=None</em>, <em>region=None</em>, <em>shared=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_subnet_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack subnetpool.</p>
</dd></dl>

</div>
