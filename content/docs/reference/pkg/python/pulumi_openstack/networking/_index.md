---
title: Module networking
title_tag: Module networking | Package pulumi_openstack | Python SDK
linktitle: networking
notitle: true
---

<div class="section" id="networking">
<h1>networking<a class="headerlink" href="#networking" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-openstack/issues">pulumi/pulumi-openstack repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-openstack/issues">terraform-providers/terraform-provider-openstack repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_openstack.networking"></span><dl class="class">
<dt id="pulumi_openstack.networking.AddressScope">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">AddressScope</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">shared=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AddressScope" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Neutron addressscope resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – IP version, either 4 (default) or 6. Changing this
creates a new address-scope.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the address-scope. Changing this updates the
name of the existing address-scope.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the address-scope. Required if admin
wants to create a address-scope for another project. Changing this creates a
new address-scope.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron address-scope. If omitted,
the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
address-scope.</p></li>
<li><p><strong>shared</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether this address-scope is shared across
all projects. Changing this updates the shared status of the existing
address-scope.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.networking.AddressScope.ip_version">
<code class="sig-name descname">ip_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.AddressScope.ip_version" title="Permalink to this definition">¶</a></dt>
<dd><p>IP version, either 4 (default) or 6. Changing this
creates a new address-scope.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.AddressScope.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.AddressScope.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the address-scope. Changing this updates the
name of the existing address-scope.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.AddressScope.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.AddressScope.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the address-scope. Required if admin
wants to create a address-scope for another project. Changing this creates a
new address-scope.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.AddressScope.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.AddressScope.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron address-scope. If omitted,
the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
address-scope.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.AddressScope.shared">
<code class="sig-name descname">shared</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.AddressScope.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether this address-scope is shared across
all projects. Changing this updates the shared status of the existing
address-scope.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.AddressScope.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">shared=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AddressScope.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AddressScope resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – IP version, either 4 (default) or 6. Changing this
creates a new address-scope.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the address-scope. Changing this updates the
name of the existing address-scope.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the address-scope. Required if admin
wants to create a address-scope for another project. Changing this creates a
new address-scope.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron address-scope. If omitted,
the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
address-scope.</p></li>
<li><p><strong>shared</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether this address-scope is shared across
all projects. Changing this updates the shared status of the existing
address-scope.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.AddressScope.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AddressScope.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.AddressScope.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AddressScope.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.AwaitableGetAddressScopeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">AwaitableGetAddressScopeResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">shared=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AwaitableGetAddressScopeResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.AwaitableGetFloatingIpResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">AwaitableGetFloatingIpResult</code><span class="sig-paren">(</span><em class="sig-param">address=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dns_domain=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">fixed_ip=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">pool=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AwaitableGetFloatingIpResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.AwaitableGetNetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">AwaitableGetNetworkResult</code><span class="sig-paren">(</span><em class="sig-param">admin_state_up=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">availability_zone_hints=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dns_domain=None</em>, <em class="sig-param">external=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">matching_subnet_cidr=None</em>, <em class="sig-param">mtu=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">shared=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">transparent_vlan=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AwaitableGetNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.AwaitableGetPortIdsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">AwaitableGetPortIdsResult</code><span class="sig-paren">(</span><em class="sig-param">admin_state_up=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">device_id=None</em>, <em class="sig-param">device_owner=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">fixed_ip=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">mac_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">sort_direction=None</em>, <em class="sig-param">sort_key=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AwaitableGetPortIdsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.AwaitableGetPortResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">AwaitableGetPortResult</code><span class="sig-paren">(</span><em class="sig-param">admin_state_up=None</em>, <em class="sig-param">all_fixed_ips=None</em>, <em class="sig-param">all_security_group_ids=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">allowed_address_pairs=None</em>, <em class="sig-param">bindings=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">device_id=None</em>, <em class="sig-param">device_owner=None</em>, <em class="sig-param">dns_assignments=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">extra_dhcp_options=None</em>, <em class="sig-param">fixed_ip=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">mac_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_id=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AwaitableGetPortResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.AwaitableGetQosBandwidthLimitRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">AwaitableGetQosBandwidthLimitRuleResult</code><span class="sig-paren">(</span><em class="sig-param">direction=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">max_burst_kbps=None</em>, <em class="sig-param">max_kbps=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AwaitableGetQosBandwidthLimitRuleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.AwaitableGetQosDscpMarkingRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">AwaitableGetQosDscpMarkingRuleResult</code><span class="sig-paren">(</span><em class="sig-param">dscp_mark=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AwaitableGetQosDscpMarkingRuleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.AwaitableGetQosMinimumBandwidthRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">AwaitableGetQosMinimumBandwidthRuleResult</code><span class="sig-paren">(</span><em class="sig-param">direction=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">min_kbps=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AwaitableGetQosMinimumBandwidthRuleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.AwaitableGetQosPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">AwaitableGetQosPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">all_tags=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">is_default=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">revision_number=None</em>, <em class="sig-param">shared=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">updated_at=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AwaitableGetQosPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.AwaitableGetRouterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">AwaitableGetRouterResult</code><span class="sig-paren">(</span><em class="sig-param">admin_state_up=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">availability_zone_hints=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">distributed=None</em>, <em class="sig-param">enable_snat=None</em>, <em class="sig-param">external_fixed_ips=None</em>, <em class="sig-param">external_network_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router_id=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AwaitableGetRouterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.AwaitableGetSecGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">AwaitableGetSecGroupResult</code><span class="sig-paren">(</span><em class="sig-param">all_tags=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secgroup_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AwaitableGetSecGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.AwaitableGetSubnetPoolResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">AwaitableGetSubnetPoolResult</code><span class="sig-paren">(</span><em class="sig-param">address_scope_id=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">default_prefixlen=None</em>, <em class="sig-param">default_quota=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">is_default=None</em>, <em class="sig-param">max_prefixlen=None</em>, <em class="sig-param">min_prefixlen=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">prefixes=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">revision_number=None</em>, <em class="sig-param">shared=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">updated_at=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AwaitableGetSubnetPoolResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.AwaitableGetSubnetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">AwaitableGetSubnetResult</code><span class="sig-paren">(</span><em class="sig-param">all_tags=None</em>, <em class="sig-param">allocation_pools=None</em>, <em class="sig-param">cidr=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dhcp_disabled=None</em>, <em class="sig-param">dhcp_enabled=None</em>, <em class="sig-param">dns_nameservers=None</em>, <em class="sig-param">enable_dhcp=None</em>, <em class="sig-param">gateway_ip=None</em>, <em class="sig-param">host_routes=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">ipv6_address_mode=None</em>, <em class="sig-param">ipv6_ra_mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">subnetpool_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AwaitableGetSubnetResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.AwaitableGetTrunkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">AwaitableGetTrunkResult</code><span class="sig-paren">(</span><em class="sig-param">admin_state_up=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">sub_ports=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">trunk_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.AwaitableGetTrunkResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.FloatingIp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">FloatingIp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dns_domain=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">fixed_ip=None</em>, <em class="sig-param">pool=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">value_specs=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 floating IP resource within OpenStack Neutron (networking)
that can be used for load balancers.
These are similar to Nova (compute) floating IP resources,
but only compute floating IPs can be used with compute instances.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The actual/specific floating IP to obtain. By default,
non-admin users are not able to specify a floating IP, so you must either be
an admin user or have had a custom policy or role applied to your OpenStack
user or project.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description for the floating IP.</p></li>
<li><p><strong>dns_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The floating IP DNS domain. Available, when Neutron
DNS extension is enabled. The data in this attribute will be published in an
external DNS service when Neutron is configured to integrate with such a
service. Changing this creates a new floating IP.</p></li>
<li><p><strong>dns_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The floating IP DNS name. Available, when Neutron DNS
extension is enabled. The data in this attribute will be published in an
external DNS service when Neutron is configured to integrate with such a
service. Changing this creates a new floating IP.</p></li>
<li><p><strong>fixed_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Fixed IP of the port to associate with this floating IP. Required if
the port has multiple fixed IPs.</p></li>
<li><p><strong>pool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the pool from which to obtain the floating
IP. Changing this creates a new floating IP.</p></li>
<li><p><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of an existing port with at least one IP address to
associate with this floating IP.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a floating IP that can be used with
another networking resource, such as a load balancer. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
floating IP (which may or may not have a different address).</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subnet ID of the floating IP pool. Specify this if
the floating IP network has multiple subnets.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the floating IP.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target tenant ID in which to allocate the floating
IP, if you specify this together with a port_id, make sure the target port
belongs to the same tenant. Changing this creates a new floating IP (which
may or may not have a different address)</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.address">
<code class="sig-name descname">address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.address" title="Permalink to this definition">¶</a></dt>
<dd><p>The actual/specific floating IP to obtain. By default,
non-admin users are not able to specify a floating IP, so you must either be
an admin user or have had a custom policy or role applied to your OpenStack
user or project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of tags assigned on the floating IP, which have
been explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description for the floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.dns_domain">
<code class="sig-name descname">dns_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.dns_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The floating IP DNS domain. Available, when Neutron
DNS extension is enabled. The data in this attribute will be published in an
external DNS service when Neutron is configured to integrate with such a
service. Changing this creates a new floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.dns_name">
<code class="sig-name descname">dns_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The floating IP DNS name. Available, when Neutron DNS
extension is enabled. The data in this attribute will be published in an
external DNS service when Neutron is configured to integrate with such a
service. Changing this creates a new floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.fixed_ip">
<code class="sig-name descname">fixed_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.fixed_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Fixed IP of the port to associate with this floating IP. Required if
the port has multiple fixed IPs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.pool">
<code class="sig-name descname">pool</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.pool" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the pool from which to obtain the floating
IP. Changing this creates a new floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.port_id">
<code class="sig-name descname">port_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.port_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of an existing port with at least one IP address to
associate with this floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a floating IP that can be used with
another networking resource, such as a load balancer. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
floating IP (which may or may not have a different address).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The subnet ID of the floating IP pool. Specify this if
the floating IP network has multiple subnets.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags for the floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The target tenant ID in which to allocate the floating
IP, if you specify this together with a port_id, make sure the target port
belongs to the same tenant. Changing this creates a new floating IP (which
may or may not have a different address)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIp.value_specs">
<code class="sig-name descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.FloatingIp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dns_domain=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">fixed_ip=None</em>, <em class="sig-param">pool=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">value_specs=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FloatingIp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The actual/specific floating IP to obtain. By default,
non-admin users are not able to specify a floating IP, so you must either be
an admin user or have had a custom policy or role applied to your OpenStack
user or project.</p></li>
<li><p><strong>all_tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The collection of tags assigned on the floating IP, which have
been explicitly and implicitly added.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description for the floating IP.</p></li>
<li><p><strong>dns_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The floating IP DNS domain. Available, when Neutron
DNS extension is enabled. The data in this attribute will be published in an
external DNS service when Neutron is configured to integrate with such a
service. Changing this creates a new floating IP.</p></li>
<li><p><strong>dns_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The floating IP DNS name. Available, when Neutron DNS
extension is enabled. The data in this attribute will be published in an
external DNS service when Neutron is configured to integrate with such a
service. Changing this creates a new floating IP.</p></li>
<li><p><strong>fixed_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Fixed IP of the port to associate with this floating IP. Required if
the port has multiple fixed IPs.</p></li>
<li><p><strong>pool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the pool from which to obtain the floating
IP. Changing this creates a new floating IP.</p></li>
<li><p><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of an existing port with at least one IP address to
associate with this floating IP.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a floating IP that can be used with
another networking resource, such as a load balancer. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
floating IP (which may or may not have a different address).</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subnet ID of the floating IP pool. Specify this if
the floating IP network has multiple subnets.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the floating IP.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target tenant ID in which to allocate the floating
IP, if you specify this together with a port_id, make sure the target port
belongs to the same tenant. Changing this creates a new floating IP (which
may or may not have a different address)</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.FloatingIp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.FloatingIp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.FloatingIp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.FloatingIpAssociate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">FloatingIpAssociate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">fixed_ip=None</em>, <em class="sig-param">floating_ip=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.FloatingIpAssociate" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates a floating IP to a port. This is useful for situations
where you have a pre-allocated floating IP or are unable to use the
<code class="docutils literal notranslate"><span class="pre">networking.FloatingIp</span></code> resource to create a floating IP.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>floating_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP Address of an existing floating IP.</p></li>
<li><p><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of an existing port with at least one IP address to
associate with this floating IP.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a floating IP that can be used with
another networking resource, such as a load balancer. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
floating IP (which may or may not have a different address).</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIpAssociate.floating_ip">
<code class="sig-name descname">floating_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIpAssociate.floating_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>IP Address of an existing floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIpAssociate.port_id">
<code class="sig-name descname">port_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIpAssociate.port_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of an existing port with at least one IP address to
associate with this floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.FloatingIpAssociate.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.FloatingIpAssociate.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a floating IP that can be used with
another networking resource, such as a load balancer. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
floating IP (which may or may not have a different address).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.FloatingIpAssociate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">fixed_ip=None</em>, <em class="sig-param">floating_ip=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.FloatingIpAssociate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FloatingIpAssociate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>floating_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP Address of an existing floating IP.</p></li>
<li><p><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of an existing port with at least one IP address to
associate with this floating IP.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a floating IP that can be used with
another networking resource, such as a load balancer. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
floating IP (which may or may not have a different address).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.FloatingIpAssociate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.FloatingIpAssociate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.FloatingIpAssociate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.FloatingIpAssociate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.GetAddressScopeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">GetAddressScopeResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">shared=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetAddressScopeResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAddressScope.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetAddressScopeResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetAddressScopeResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetAddressScopeResult.ip_version">
<code class="sig-name descname">ip_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetAddressScopeResult.ip_version" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetAddressScopeResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetAddressScopeResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetAddressScopeResult.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetAddressScopeResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetAddressScopeResult.shared">
<code class="sig-name descname">shared</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetAddressScopeResult.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetFloatingIpResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">GetFloatingIpResult</code><span class="sig-paren">(</span><em class="sig-param">address=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dns_domain=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">fixed_ip=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">pool=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetFloatingIpResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFloatingIp.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetFloatingIpResult.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetFloatingIpResult.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags applied on the floating IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetFloatingIpResult.dns_domain">
<code class="sig-name descname">dns_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetFloatingIpResult.dns_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The floating IP DNS domain. Available, when Neutron DNS
extension is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetFloatingIpResult.dns_name">
<code class="sig-name descname">dns_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetFloatingIpResult.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The floating IP DNS name. Available, when Neutron DNS extension
is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetFloatingIpResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetFloatingIpResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetNetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">GetNetworkResult</code><span class="sig-paren">(</span><em class="sig-param">admin_state_up=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">availability_zone_hints=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dns_domain=None</em>, <em class="sig-param">external=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">matching_subnet_cidr=None</em>, <em class="sig-param">mtu=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">shared=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">transparent_vlan=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetwork.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetNetworkResult.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative state of the network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetNetworkResult.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of string tags applied on the network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetNetworkResult.availability_zone_hints">
<code class="sig-name descname">availability_zone_hints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult.availability_zone_hints" title="Permalink to this definition">¶</a></dt>
<dd><p>The availability zone candidates for the network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetNetworkResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetNetworkResult.dns_domain">
<code class="sig-name descname">dns_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult.dns_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The network DNS domain. Available, when Neutron DNS extension
is enabled</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetNetworkResult.external">
<code class="sig-name descname">external</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult.external" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetNetworkResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetNetworkResult.mtu">
<code class="sig-name descname">mtu</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult.mtu" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetNetworkResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetNetworkResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetNetworkResult.shared">
<code class="sig-name descname">shared</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the network resource can be accessed by any
tenant or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetNetworkResult.transparent_vlan">
<code class="sig-name descname">transparent_vlan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetNetworkResult.transparent_vlan" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetPortIdsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">GetPortIdsResult</code><span class="sig-paren">(</span><em class="sig-param">admin_state_up=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">device_id=None</em>, <em class="sig-param">device_owner=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">fixed_ip=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">mac_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">sort_direction=None</em>, <em class="sig-param">sort_key=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetPortIdsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPortIds.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortIdsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortIdsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetPortResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">GetPortResult</code><span class="sig-paren">(</span><em class="sig-param">admin_state_up=None</em>, <em class="sig-param">all_fixed_ips=None</em>, <em class="sig-param">all_security_group_ids=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">allowed_address_pairs=None</em>, <em class="sig-param">bindings=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">device_id=None</em>, <em class="sig-param">device_owner=None</em>, <em class="sig-param">dns_assignments=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">extra_dhcp_options=None</em>, <em class="sig-param">fixed_ip=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">mac_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_id=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPort.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.all_fixed_ips">
<code class="sig-name descname">all_fixed_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.all_fixed_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of Fixed IP addresses on the port in the
order returned by the Network v2 API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.all_security_group_ids">
<code class="sig-name descname">all_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.all_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of security group IDs applied on the port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of string tags applied on the port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.allowed_address_pairs">
<code class="sig-name descname">allowed_address_pairs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.allowed_address_pairs" title="Permalink to this definition">¶</a></dt>
<dd><p>An IP/MAC Address pair of additional IP
addresses that can be active on this port. The structure is described
below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.bindings">
<code class="sig-name descname">bindings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.bindings" title="Permalink to this definition">¶</a></dt>
<dd><p>The port binding information. The structure is described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.device_id">
<code class="sig-name descname">device_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.device_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.device_owner">
<code class="sig-name descname">device_owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.device_owner" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.dns_assignments">
<code class="sig-name descname">dns_assignments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.dns_assignments" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of maps representing port DNS assignments.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.dns_name">
<code class="sig-name descname">dns_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.extra_dhcp_options">
<code class="sig-name descname">extra_dhcp_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.extra_dhcp_options" title="Permalink to this definition">¶</a></dt>
<dd><p>An extra DHCP option configured on the port.
The structure is described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.mac_address">
<code class="sig-name descname">mac_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.mac_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The additional MAC address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the DHCP option.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.network_id">
<code class="sig-name descname">network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.port_id">
<code class="sig-name descname">port_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.port_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetPortResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetPortResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetQosBandwidthLimitRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">GetQosBandwidthLimitRuleResult</code><span class="sig-paren">(</span><em class="sig-param">direction=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">max_burst_kbps=None</em>, <em class="sig-param">max_kbps=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetQosBandwidthLimitRuleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getQosBandwidthLimitRule.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosBandwidthLimitRuleResult.direction">
<code class="sig-name descname">direction</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosBandwidthLimitRuleResult.direction" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosBandwidthLimitRuleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosBandwidthLimitRuleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosBandwidthLimitRuleResult.max_burst_kbps">
<code class="sig-name descname">max_burst_kbps</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosBandwidthLimitRuleResult.max_burst_kbps" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosBandwidthLimitRuleResult.max_kbps">
<code class="sig-name descname">max_kbps</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosBandwidthLimitRuleResult.max_kbps" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosBandwidthLimitRuleResult.qos_policy_id">
<code class="sig-name descname">qos_policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosBandwidthLimitRuleResult.qos_policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosBandwidthLimitRuleResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosBandwidthLimitRuleResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetQosDscpMarkingRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">GetQosDscpMarkingRuleResult</code><span class="sig-paren">(</span><em class="sig-param">dscp_mark=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetQosDscpMarkingRuleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getQosDscpMarkingRule.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosDscpMarkingRuleResult.dscp_mark">
<code class="sig-name descname">dscp_mark</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosDscpMarkingRuleResult.dscp_mark" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosDscpMarkingRuleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosDscpMarkingRuleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosDscpMarkingRuleResult.qos_policy_id">
<code class="sig-name descname">qos_policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosDscpMarkingRuleResult.qos_policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosDscpMarkingRuleResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosDscpMarkingRuleResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetQosMinimumBandwidthRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">GetQosMinimumBandwidthRuleResult</code><span class="sig-paren">(</span><em class="sig-param">direction=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">min_kbps=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetQosMinimumBandwidthRuleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getQosMinimumBandwidthRule.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosMinimumBandwidthRuleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosMinimumBandwidthRuleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosMinimumBandwidthRuleResult.min_kbps">
<code class="sig-name descname">min_kbps</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosMinimumBandwidthRuleResult.min_kbps" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosMinimumBandwidthRuleResult.qos_policy_id">
<code class="sig-name descname">qos_policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosMinimumBandwidthRuleResult.qos_policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosMinimumBandwidthRuleResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosMinimumBandwidthRuleResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetQosPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">GetQosPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">all_tags=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">is_default=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">revision_number=None</em>, <em class="sig-param">shared=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">updated_at=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetQosPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getQosPolicy.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosPolicyResult.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosPolicyResult.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of string tags applied on the QoS policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosPolicyResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosPolicyResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which QoS policy was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosPolicyResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosPolicyResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosPolicyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosPolicyResult.is_default">
<code class="sig-name descname">is_default</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosPolicyResult.is_default" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosPolicyResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosPolicyResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosPolicyResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosPolicyResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosPolicyResult.revision_number">
<code class="sig-name descname">revision_number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosPolicyResult.revision_number" title="Permalink to this definition">¶</a></dt>
<dd><p>The revision number of the QoS policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosPolicyResult.shared">
<code class="sig-name descname">shared</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosPolicyResult.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetQosPolicyResult.updated_at">
<code class="sig-name descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetQosPolicyResult.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which QoS policy was created.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetRouterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">GetRouterResult</code><span class="sig-paren">(</span><em class="sig-param">admin_state_up=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">availability_zone_hints=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">distributed=None</em>, <em class="sig-param">enable_snat=None</em>, <em class="sig-param">external_fixed_ips=None</em>, <em class="sig-param">external_network_id=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router_id=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetRouterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRouter.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetRouterResult.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetRouterResult.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of string tags applied on the router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetRouterResult.availability_zone_hints">
<code class="sig-name descname">availability_zone_hints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetRouterResult.availability_zone_hints" title="Permalink to this definition">¶</a></dt>
<dd><p>The availability zone that is used to make router resources highly available.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetRouterResult.enable_snat">
<code class="sig-name descname">enable_snat</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetRouterResult.enable_snat" title="Permalink to this definition">¶</a></dt>
<dd><p>The value that points out if the Source NAT is enabled on the router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetRouterResult.external_fixed_ips">
<code class="sig-name descname">external_fixed_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetRouterResult.external_fixed_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>The external fixed IPs of the router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetRouterResult.external_network_id">
<code class="sig-name descname">external_network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetRouterResult.external_network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The network UUID of an external gateway for the router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetRouterResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetRouterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetSecGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">GetSecGroupResult</code><span class="sig-paren">(</span><em class="sig-param">all_tags=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secgroup_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetSecGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecGroup.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSecGroupResult.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSecGroupResult.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of string tags applied on the security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSecGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSecGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSecGroupResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSecGroupResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code>- See Argument Reference above.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSecGroupResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSecGroupResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">GetSubnetPoolResult</code><span class="sig-paren">(</span><em class="sig-param">address_scope_id=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">default_prefixlen=None</em>, <em class="sig-param">default_quota=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">is_default=None</em>, <em class="sig-param">max_prefixlen=None</em>, <em class="sig-param">min_prefixlen=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">prefixes=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">revision_number=None</em>, <em class="sig-param">shared=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">updated_at=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSubnetPool.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.address_scope_id">
<code class="sig-name descname">address_scope_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.address_scope_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_version</span></code> -The IP protocol version.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of string tags applied on the subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which subnetpool was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.default_prefixlen">
<code class="sig-name descname">default_prefixlen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.default_prefixlen" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.default_quota">
<code class="sig-name descname">default_quota</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.default_quota" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.is_default">
<code class="sig-name descname">is_default</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.is_default" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.max_prefixlen">
<code class="sig-name descname">max_prefixlen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.max_prefixlen" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.min_prefixlen">
<code class="sig-name descname">min_prefixlen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.min_prefixlen" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.prefixes">
<code class="sig-name descname">prefixes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.prefixes" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.revision_number">
<code class="sig-name descname">revision_number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.revision_number" title="Permalink to this definition">¶</a></dt>
<dd><p>The revision number of the subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.shared">
<code class="sig-name descname">shared</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetPoolResult.updated_at">
<code class="sig-name descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetPoolResult.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which subnetpool was created.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetSubnetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">GetSubnetResult</code><span class="sig-paren">(</span><em class="sig-param">all_tags=None</em>, <em class="sig-param">allocation_pools=None</em>, <em class="sig-param">cidr=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dhcp_disabled=None</em>, <em class="sig-param">dhcp_enabled=None</em>, <em class="sig-param">dns_nameservers=None</em>, <em class="sig-param">enable_dhcp=None</em>, <em class="sig-param">gateway_ip=None</em>, <em class="sig-param">host_routes=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">ipv6_address_mode=None</em>, <em class="sig-param">ipv6_ra_mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">subnetpool_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSubnet.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetResult.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetResult.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags applied on the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetResult.allocation_pools">
<code class="sig-name descname">allocation_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetResult.allocation_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>Allocation pools of the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetResult.dns_nameservers">
<code class="sig-name descname">dns_nameservers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetResult.dns_nameservers" title="Permalink to this definition">¶</a></dt>
<dd><p>DNS Nameservers of the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetResult.enable_dhcp">
<code class="sig-name descname">enable_dhcp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetResult.enable_dhcp" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the subnet has DHCP enabled or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetResult.host_routes">
<code class="sig-name descname">host_routes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetResult.host_routes" title="Permalink to this definition">¶</a></dt>
<dd><p>Host Routes of the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetSubnetResult.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetSubnetResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>See Argument Reference above.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.GetTrunkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">GetTrunkResult</code><span class="sig-paren">(</span><em class="sig-param">admin_state_up=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">sub_ports=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">trunk_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.GetTrunkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTrunk.</p>
<dl class="attribute">
<dt id="pulumi_openstack.networking.GetTrunkResult.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetTrunkResult.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of string tags applied on the trunk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetTrunkResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetTrunkResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetTrunkResult.port_id">
<code class="sig-name descname">port_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetTrunkResult.port_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the trunk subport.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.GetTrunkResult.sub_ports">
<code class="sig-name descname">sub_ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.GetTrunkResult.sub_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of the trunk subports. The structure of each subport is
described below.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_openstack.networking.Network">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">Network</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_state_up=None</em>, <em class="sig-param">availability_zone_hints=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dns_domain=None</em>, <em class="sig-param">external=None</em>, <em class="sig-param">mtu=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port_security_enabled=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">segments=None</em>, <em class="sig-param">shared=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">transparent_vlan=None</em>, <em class="sig-param">value_specs=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Network" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Neutron network resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the network.
Acceptable values are “true” and “false”. Changing this value updates the
state of the existing network.</p></li>
<li><p><strong>availability_zone_hints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An availability zone is used to make
network resources highly available. Used for resources with high availability
so that they are scheduled on different availability zones. Changing this
creates a new network.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the network. Changing this
updates the name of the existing network.</p></li>
<li><p><strong>dns_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network DNS domain. Available, when Neutron DNS
extension is enabled. The <code class="docutils literal notranslate"><span class="pre">dns_domain</span></code> of a network in conjunction with the
<code class="docutils literal notranslate"><span class="pre">dns_name</span></code> attribute of its ports will be published in an external DNS
service when Neutron is configured to integrate with such a service.</p></li>
<li><p><strong>external</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the network resource has the
external routing facility. Valid values are true and false. Defaults to
false. Changing this updates the external attribute of the existing network.</p></li>
<li><p><strong>mtu</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The network MTU. Available for read-only, when Neutron
<code class="docutils literal notranslate"><span class="pre">net-mtu</span></code> extension is enabled. Available for the modification, when
Neutron <code class="docutils literal notranslate"><span class="pre">net-mtu-writable</span></code> extension is enabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the network. Changing this updates the name of
the existing network.</p></li>
<li><p><strong>port_security_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to explicitly enable or disable
port security on the network. Port Security is usually enabled by default, so
omitting this argument will usually result in a value of “true”. Setting this
explicitly to <code class="docutils literal notranslate"><span class="pre">false</span></code> will disable port security. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and
<code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>qos_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Reference to the associated QoS policy.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron network. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
network.</p></li>
<li><p><strong>segments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of one or more provider segment objects.</p></li>
<li><p><strong>shared</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the network resource can be accessed
by any tenant or not. Changing this updates the sharing capabilities of the
existing network.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the network.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the network. Required if admin wants to
create a network for another tenant. Changing this creates a new network.</p></li>
<li><p><strong>transparent_vlan</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the network resource has the
VLAN transparent attribute set. Valid values are true and false. Defaults to
false. Changing this updates the <code class="docutils literal notranslate"><span class="pre">transparent_vlan</span></code> attribute of the existing
network.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>segments</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">network_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of physical network.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">physicalNetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The physical network where this network is implemented.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">segmentation_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - An isolated segment on the physical network.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative state of the network.
Acceptable values are “true” and “false”. Changing this value updates the
state of the existing network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of tags assigned on the network, which have been
explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.availability_zone_hints">
<code class="sig-name descname">availability_zone_hints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.availability_zone_hints" title="Permalink to this definition">¶</a></dt>
<dd><p>An availability zone is used to make
network resources highly available. Used for resources with high availability
so that they are scheduled on different availability zones. Changing this
creates a new network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description of the network. Changing this
updates the name of the existing network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.dns_domain">
<code class="sig-name descname">dns_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.dns_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The network DNS domain. Available, when Neutron DNS
extension is enabled. The <code class="docutils literal notranslate"><span class="pre">dns_domain</span></code> of a network in conjunction with the
<code class="docutils literal notranslate"><span class="pre">dns_name</span></code> attribute of its ports will be published in an external DNS
service when Neutron is configured to integrate with such a service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.external">
<code class="sig-name descname">external</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.external" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the network resource has the
external routing facility. Valid values are true and false. Defaults to
false. Changing this updates the external attribute of the existing network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.mtu">
<code class="sig-name descname">mtu</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.mtu" title="Permalink to this definition">¶</a></dt>
<dd><p>The network MTU. Available for read-only, when Neutron
<code class="docutils literal notranslate"><span class="pre">net-mtu</span></code> extension is enabled. Available for the modification, when
Neutron <code class="docutils literal notranslate"><span class="pre">net-mtu-writable</span></code> extension is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the network. Changing this updates the name of
the existing network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.port_security_enabled">
<code class="sig-name descname">port_security_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.port_security_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to explicitly enable or disable
port security on the network. Port Security is usually enabled by default, so
omitting this argument will usually result in a value of “true”. Setting this
explicitly to <code class="docutils literal notranslate"><span class="pre">false</span></code> will disable port security. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and
<code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.qos_policy_id">
<code class="sig-name descname">qos_policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.qos_policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Reference to the associated QoS policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron network. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.segments">
<code class="sig-name descname">segments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.segments" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of one or more provider segment objects.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">network_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of physical network.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">physicalNetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The physical network where this network is implemented.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">segmentation_id</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - An isolated segment on the physical network.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.shared">
<code class="sig-name descname">shared</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the network resource can be accessed
by any tenant or not. Changing this updates the sharing capabilities of the
existing network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags for the network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the network. Required if admin wants to
create a network for another tenant. Changing this creates a new network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.transparent_vlan">
<code class="sig-name descname">transparent_vlan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.transparent_vlan" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the network resource has the
VLAN transparent attribute set. Valid values are true and false. Defaults to
false. Changing this updates the <code class="docutils literal notranslate"><span class="pre">transparent_vlan</span></code> attribute of the existing
network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Network.value_specs">
<code class="sig-name descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Network.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.Network.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_state_up=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">availability_zone_hints=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dns_domain=None</em>, <em class="sig-param">external=None</em>, <em class="sig-param">mtu=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port_security_enabled=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">segments=None</em>, <em class="sig-param">shared=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">transparent_vlan=None</em>, <em class="sig-param">value_specs=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Network.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Network resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the network.
Acceptable values are “true” and “false”. Changing this value updates the
state of the existing network.</p></li>
<li><p><strong>all_tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The collection of tags assigned on the network, which have been
explicitly and implicitly added.</p></li>
<li><p><strong>availability_zone_hints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An availability zone is used to make
network resources highly available. Used for resources with high availability
so that they are scheduled on different availability zones. Changing this
creates a new network.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the network. Changing this
updates the name of the existing network.</p></li>
<li><p><strong>dns_domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network DNS domain. Available, when Neutron DNS
extension is enabled. The <code class="docutils literal notranslate"><span class="pre">dns_domain</span></code> of a network in conjunction with the
<code class="docutils literal notranslate"><span class="pre">dns_name</span></code> attribute of its ports will be published in an external DNS
service when Neutron is configured to integrate with such a service.</p></li>
<li><p><strong>external</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the network resource has the
external routing facility. Valid values are true and false. Defaults to
false. Changing this updates the external attribute of the existing network.</p></li>
<li><p><strong>mtu</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The network MTU. Available for read-only, when Neutron
<code class="docutils literal notranslate"><span class="pre">net-mtu</span></code> extension is enabled. Available for the modification, when
Neutron <code class="docutils literal notranslate"><span class="pre">net-mtu-writable</span></code> extension is enabled.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the network. Changing this updates the name of
the existing network.</p></li>
<li><p><strong>port_security_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to explicitly enable or disable
port security on the network. Port Security is usually enabled by default, so
omitting this argument will usually result in a value of “true”. Setting this
explicitly to <code class="docutils literal notranslate"><span class="pre">false</span></code> will disable port security. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code> and
<code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>qos_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Reference to the associated QoS policy.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron network. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
network.</p></li>
<li><p><strong>segments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of one or more provider segment objects.</p></li>
<li><p><strong>shared</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the network resource can be accessed
by any tenant or not. Changing this updates the sharing capabilities of the
existing network.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the network.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the network. Required if admin wants to
create a network for another tenant. Changing this creates a new network.</p></li>
<li><p><strong>transparent_vlan</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the network resource has the
VLAN transparent attribute set. Valid values are true and false. Defaults to
false. Changing this updates the <code class="docutils literal notranslate"><span class="pre">transparent_vlan</span></code> attribute of the existing
network.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>segments</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">network_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of physical network.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">physicalNetwork</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The physical network where this network is implemented.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">segmentation_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - An isolated segment on the physical network.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.Network.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Network.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.Network.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Network.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.Port">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">Port</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_state_up=None</em>, <em class="sig-param">allowed_address_pairs=None</em>, <em class="sig-param">binding=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">device_id=None</em>, <em class="sig-param">device_owner=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">extra_dhcp_options=None</em>, <em class="sig-param">fixed_ips=None</em>, <em class="sig-param">mac_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_id=None</em>, <em class="sig-param">no_fixed_ip=None</em>, <em class="sig-param">no_security_groups=None</em>, <em class="sig-param">port_security_enabled=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">value_specs=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Port" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 port resource within OpenStack.</p>
<p>There are some notes to consider when connecting Instances to networks using
Ports. Please see the <code class="docutils literal notranslate"><span class="pre">compute.Instance</span></code> documentation for further
documentation.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Administrative up/down status for the port
(must be “true” or “false” if provided). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing port.</p></li>
<li><p><strong>allowed_address_pairs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An IP/MAC Address pair of additional IP
addresses that can be active on this port. The structure is described
below.</p></li>
<li><p><strong>binding</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The port binding allows to specify binding information
for the port. The structure is described below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the floating IP. Changing
this updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing port.</p></li>
<li><p><strong>device_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the device attached to the port. Changing this
creates a new port.</p></li>
<li><p><strong>device_owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The device owner of the Port. Changing this creates
a new port.</p></li>
<li><p><strong>dns_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The port DNS name. Available, when Neutron DNS extension
is enabled.</p></li>
<li><p><strong>extra_dhcp_options</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An extra DHCP option that needs to be configured
on the port. The structure is described below. Can be specified multiple
times.</p></li>
<li><p><strong>fixed_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of desired IPs for
this port. The structure is described below.</p></li>
<li><p><strong>mac_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The additional MAC address.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the DHCP option.</p></li>
<li><p><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the network to attach the port to. Changing
this creates a new port.</p></li>
<li><p><strong>no_fixed_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Create a port with no fixed
IP address. This will also remove any fixed IPs previously set on a port. <code class="docutils literal notranslate"><span class="pre">true</span></code>
is the only valid value for this argument.</p></li>
<li><p><strong>no_security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to
<code class="docutils literal notranslate"><span class="pre">true</span></code>, then no security groups are applied to the port. If set to <code class="docutils literal notranslate"><span class="pre">false</span></code> and
no <code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> are specified, then the Port will yield to the default
behavior of the Networking service, which is to usually apply the “default”
security group.</p></li>
<li><p><strong>port_security_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to explicitly enable or disable
port security on the port. Port Security is usually enabled by default, so
omitting argument will usually result in a value of “true”. Setting this
explicitly to <code class="docutils literal notranslate"><span class="pre">false</span></code> will disable port security. In order to disable port
security, the port must not have any security groups. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code>
and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>qos_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Reference to the associated QoS policy.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
port.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list
of security group IDs to apply to the port. The security groups must be
specified by ID and not name (as opposed to how they are configured with
the Compute Instance).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the port.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the Port. Required if admin wants
to create a port for another tenant. Changing this creates a new port.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>allowed_address_pairs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The additional IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mac_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The additional MAC address.</p></li>
</ul>
<p>The <strong>binding</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hostId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the host to allocate port on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">profile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Custom data to be passed as <code class="docutils literal notranslate"><span class="pre">binding:profile</span></code>. Data
must be passed as JSON.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vifDetails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of JSON strings containing additional
details for this specific binding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vifType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The VNIC type of the port binding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vnicType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - VNIC type for the port. Can either be <code class="docutils literal notranslate"><span class="pre">direct</span></code>,
<code class="docutils literal notranslate"><span class="pre">direct-physical</span></code>, <code class="docutils literal notranslate"><span class="pre">macvtap</span></code>, <code class="docutils literal notranslate"><span class="pre">normal</span></code>, <code class="docutils literal notranslate"><span class="pre">baremetal</span></code> or <code class="docutils literal notranslate"><span class="pre">virtio-forwarder</span></code>.
Default value is <code class="docutils literal notranslate"><span class="pre">normal</span></code>.</p></li>
</ul>
<p>The <strong>extra_dhcp_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - IP protocol version. Defaults to 4.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the DHCP option.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the DHCP option.</p></li>
</ul>
<p>The <strong>fixed_ips</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The additional IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Subnet in which to allocate IP address for
this port.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>Administrative up/down status for the port
(must be “true” or “false” if provided). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.all_fixed_ips">
<code class="sig-name descname">all_fixed_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.all_fixed_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of Fixed IP addresses on the port in the
order returned by the Network v2 API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.all_security_group_ids">
<code class="sig-name descname">all_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.all_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of Security Group IDs on the port
which have been explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of tags assigned on the port, which have been
explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.allowed_address_pairs">
<code class="sig-name descname">allowed_address_pairs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.allowed_address_pairs" title="Permalink to this definition">¶</a></dt>
<dd><p>An IP/MAC Address pair of additional IP
addresses that can be active on this port. The structure is described
below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The additional IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mac_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The additional MAC address.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.binding">
<code class="sig-name descname">binding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.binding" title="Permalink to this definition">¶</a></dt>
<dd><p>The port binding allows to specify binding information
for the port. The structure is described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hostId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the host to allocate port on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">profile</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Custom data to be passed as <code class="docutils literal notranslate"><span class="pre">binding:profile</span></code>. Data
must be passed as JSON.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vifDetails</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A map of JSON strings containing additional
details for this specific binding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vifType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The VNIC type of the port binding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vnicType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - VNIC type for the port. Can either be <code class="docutils literal notranslate"><span class="pre">direct</span></code>,
<code class="docutils literal notranslate"><span class="pre">direct-physical</span></code>, <code class="docutils literal notranslate"><span class="pre">macvtap</span></code>, <code class="docutils literal notranslate"><span class="pre">normal</span></code>, <code class="docutils literal notranslate"><span class="pre">baremetal</span></code> or <code class="docutils literal notranslate"><span class="pre">virtio-forwarder</span></code>.
Default value is <code class="docutils literal notranslate"><span class="pre">normal</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description of the floating IP. Changing
this updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.device_id">
<code class="sig-name descname">device_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.device_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the device attached to the port. Changing this
creates a new port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.device_owner">
<code class="sig-name descname">device_owner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.device_owner" title="Permalink to this definition">¶</a></dt>
<dd><p>The device owner of the Port. Changing this creates
a new port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.dns_assignments">
<code class="sig-name descname">dns_assignments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.dns_assignments" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of maps representing port DNS assignments.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.dns_name">
<code class="sig-name descname">dns_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The port DNS name. Available, when Neutron DNS extension
is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.extra_dhcp_options">
<code class="sig-name descname">extra_dhcp_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.extra_dhcp_options" title="Permalink to this definition">¶</a></dt>
<dd><p>An extra DHCP option that needs to be configured
on the port. The structure is described below. Can be specified multiple
times.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_version</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - IP protocol version. Defaults to 4.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the DHCP option.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Value of the DHCP option.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.fixed_ips">
<code class="sig-name descname">fixed_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.fixed_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of desired IPs for
this port. The structure is described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The additional IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Subnet in which to allocate IP address for
this port.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.mac_address">
<code class="sig-name descname">mac_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.mac_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The additional MAC address.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the DHCP option.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.network_id">
<code class="sig-name descname">network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the network to attach the port to. Changing
this creates a new port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.no_fixed_ip">
<code class="sig-name descname">no_fixed_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.no_fixed_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a port with no fixed
IP address. This will also remove any fixed IPs previously set on a port. <code class="docutils literal notranslate"><span class="pre">true</span></code>
is the only valid value for this argument.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.no_security_groups">
<code class="sig-name descname">no_security_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.no_security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to
<code class="docutils literal notranslate"><span class="pre">true</span></code>, then no security groups are applied to the port. If set to <code class="docutils literal notranslate"><span class="pre">false</span></code> and
no <code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> are specified, then the Port will yield to the default
behavior of the Networking service, which is to usually apply the “default”
security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.port_security_enabled">
<code class="sig-name descname">port_security_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.port_security_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to explicitly enable or disable
port security on the port. Port Security is usually enabled by default, so
omitting argument will usually result in a value of “true”. Setting this
explicitly to <code class="docutils literal notranslate"><span class="pre">false</span></code> will disable port security. In order to disable port
security, the port must not have any security groups. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code>
and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.qos_policy_id">
<code class="sig-name descname">qos_policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.qos_policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Reference to the associated QoS policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list
of security group IDs to apply to the port. The security groups must be
specified by ID and not name (as opposed to how they are configured with
the Compute Instance).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags for the port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the Port. Required if admin wants
to create a port for another tenant. Changing this creates a new port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Port.value_specs">
<code class="sig-name descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Port.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.Port.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_state_up=None</em>, <em class="sig-param">all_fixed_ips=None</em>, <em class="sig-param">all_security_group_ids=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">allowed_address_pairs=None</em>, <em class="sig-param">binding=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">device_id=None</em>, <em class="sig-param">device_owner=None</em>, <em class="sig-param">dns_assignments=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">extra_dhcp_options=None</em>, <em class="sig-param">fixed_ips=None</em>, <em class="sig-param">mac_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_id=None</em>, <em class="sig-param">no_fixed_ip=None</em>, <em class="sig-param">no_security_groups=None</em>, <em class="sig-param">port_security_enabled=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">value_specs=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Port.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Port resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Administrative up/down status for the port
(must be “true” or “false” if provided). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing port.</p></li>
<li><p><strong>all_fixed_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The collection of Fixed IP addresses on the port in the
order returned by the Network v2 API.</p></li>
<li><p><strong>all_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The collection of Security Group IDs on the port
which have been explicitly and implicitly added.</p></li>
<li><p><strong>all_tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The collection of tags assigned on the port, which have been
explicitly and implicitly added.</p></li>
<li><p><strong>allowed_address_pairs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An IP/MAC Address pair of additional IP
addresses that can be active on this port. The structure is described
below.</p></li>
<li><p><strong>binding</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The port binding allows to specify binding information
for the port. The structure is described below.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the floating IP. Changing
this updates the <code class="docutils literal notranslate"><span class="pre">description</span></code> of an existing port.</p></li>
<li><p><strong>device_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the device attached to the port. Changing this
creates a new port.</p></li>
<li><p><strong>device_owner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The device owner of the Port. Changing this creates
a new port.</p></li>
<li><p><strong>dns_assignments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of maps representing port DNS assignments.</p></li>
<li><p><strong>dns_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The port DNS name. Available, when Neutron DNS extension
is enabled.</p></li>
<li><p><strong>extra_dhcp_options</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An extra DHCP option that needs to be configured
on the port. The structure is described below. Can be specified multiple
times.</p></li>
<li><p><strong>fixed_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of desired IPs for
this port. The structure is described below.</p></li>
<li><p><strong>mac_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The additional MAC address.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the DHCP option.</p></li>
<li><p><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the network to attach the port to. Changing
this creates a new port.</p></li>
<li><p><strong>no_fixed_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Create a port with no fixed
IP address. This will also remove any fixed IPs previously set on a port. <code class="docutils literal notranslate"><span class="pre">true</span></code>
is the only valid value for this argument.</p></li>
<li><p><strong>no_security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to
<code class="docutils literal notranslate"><span class="pre">true</span></code>, then no security groups are applied to the port. If set to <code class="docutils literal notranslate"><span class="pre">false</span></code> and
no <code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code> are specified, then the Port will yield to the default
behavior of the Networking service, which is to usually apply the “default”
security group.</p></li>
<li><p><strong>port_security_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to explicitly enable or disable
port security on the port. Port Security is usually enabled by default, so
omitting argument will usually result in a value of “true”. Setting this
explicitly to <code class="docutils literal notranslate"><span class="pre">false</span></code> will disable port security. In order to disable port
security, the port must not have any security groups. Valid values are <code class="docutils literal notranslate"><span class="pre">true</span></code>
and <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>qos_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Reference to the associated QoS policy.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
port.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list
of security group IDs to apply to the port. The security groups must be
specified by ID and not name (as opposed to how they are configured with
the Compute Instance).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the port.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the Port. Required if admin wants
to create a port for another tenant. Changing this creates a new port.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>allowed_address_pairs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The additional IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mac_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The additional MAC address.</p></li>
</ul>
<p>The <strong>binding</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hostId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the host to allocate port on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">profile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Custom data to be passed as <code class="docutils literal notranslate"><span class="pre">binding:profile</span></code>. Data
must be passed as JSON.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vifDetails</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of JSON strings containing additional
details for this specific binding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vifType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The VNIC type of the port binding.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vnicType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - VNIC type for the port. Can either be <code class="docutils literal notranslate"><span class="pre">direct</span></code>,
<code class="docutils literal notranslate"><span class="pre">direct-physical</span></code>, <code class="docutils literal notranslate"><span class="pre">macvtap</span></code>, <code class="docutils literal notranslate"><span class="pre">normal</span></code>, <code class="docutils literal notranslate"><span class="pre">baremetal</span></code> or <code class="docutils literal notranslate"><span class="pre">virtio-forwarder</span></code>.
Default value is <code class="docutils literal notranslate"><span class="pre">normal</span></code>.</p></li>
</ul>
<p>The <strong>extra_dhcp_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - IP protocol version. Defaults to 4.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the DHCP option.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Value of the DHCP option.</p></li>
</ul>
<p>The <strong>fixed_ips</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The additional IP address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Subnet in which to allocate IP address for
this port.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.Port.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Port.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.Port.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Port.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.PortSecGroupAssociate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">PortSecGroupAssociate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enforce=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.PortSecGroupAssociate" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a PortSecGroupAssociate resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] enforce: Whether to replace or append the list of security</p>
<blockquote>
<div><p>groups, specified in the <code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An UUID of the port to apply security groups to.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to manage a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
resource.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security group IDs to apply to
the port. The security groups must be specified by ID and not name (as
opposed to how they are configured with the Compute Instance).</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.networking.PortSecGroupAssociate.all_security_group_ids">
<code class="sig-name descname">all_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.PortSecGroupAssociate.all_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of Security Group IDs on the port
which have been explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.PortSecGroupAssociate.enforce">
<code class="sig-name descname">enforce</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.PortSecGroupAssociate.enforce" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to replace or append the list of security
groups, specified in the <code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.PortSecGroupAssociate.port_id">
<code class="sig-name descname">port_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.PortSecGroupAssociate.port_id" title="Permalink to this definition">¶</a></dt>
<dd><p>An UUID of the port to apply security groups to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.PortSecGroupAssociate.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.PortSecGroupAssociate.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to manage a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.PortSecGroupAssociate.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.PortSecGroupAssociate.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of security group IDs to apply to
the port. The security groups must be specified by ID and not name (as
opposed to how they are configured with the Compute Instance).</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.PortSecGroupAssociate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">all_security_group_ids=None</em>, <em class="sig-param">enforce=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_group_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.PortSecGroupAssociate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PortSecGroupAssociate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>all_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The collection of Security Group IDs on the port
which have been explicitly and implicitly added.</p></li>
<li><p><strong>enforce</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to replace or append the list of security
groups, specified in the <code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An UUID of the port to apply security groups to.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to manage a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
resource.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security group IDs to apply to
the port. The security groups must be specified by ID and not name (as
opposed to how they are configured with the Compute Instance).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.PortSecGroupAssociate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.PortSecGroupAssociate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.PortSecGroupAssociate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.PortSecGroupAssociate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.QosBandwidthLimitRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">QosBandwidthLimitRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">direction=None</em>, <em class="sig-param">max_burst_kbps=None</em>, <em class="sig-param">max_kbps=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QosBandwidthLimitRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Neutron QoS bandwidth limit rule resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The direction of traffic. Defaults to “egress”. Changing this updates the direction of the
existing QoS bandwidth limit rule.</p></li>
<li><p><strong>max_burst_kbps</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum burst size in kilobits of a QoS bandwidth limit rule. Changing this updates the
maximum burst size in kilobits of the existing QoS bandwidth limit rule.</p></li>
<li><p><strong>max_kbps</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum kilobits per second of a QoS bandwidth limit rule. Changing this updates the
maximum kilobits per second of the existing QoS bandwidth limit rule.</p></li>
<li><p><strong>qos_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The QoS policy reference. Changing this creates a new QoS bandwidth limit rule.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron QoS bandwidth limit rule. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new QoS bandwidth limit rule.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.networking.QosBandwidthLimitRule.direction">
<code class="sig-name descname">direction</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosBandwidthLimitRule.direction" title="Permalink to this definition">¶</a></dt>
<dd><p>The direction of traffic. Defaults to “egress”. Changing this updates the direction of the
existing QoS bandwidth limit rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosBandwidthLimitRule.max_burst_kbps">
<code class="sig-name descname">max_burst_kbps</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosBandwidthLimitRule.max_burst_kbps" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum burst size in kilobits of a QoS bandwidth limit rule. Changing this updates the
maximum burst size in kilobits of the existing QoS bandwidth limit rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosBandwidthLimitRule.max_kbps">
<code class="sig-name descname">max_kbps</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosBandwidthLimitRule.max_kbps" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum kilobits per second of a QoS bandwidth limit rule. Changing this updates the
maximum kilobits per second of the existing QoS bandwidth limit rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosBandwidthLimitRule.qos_policy_id">
<code class="sig-name descname">qos_policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosBandwidthLimitRule.qos_policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The QoS policy reference. Changing this creates a new QoS bandwidth limit rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosBandwidthLimitRule.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosBandwidthLimitRule.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron QoS bandwidth limit rule. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new QoS bandwidth limit rule.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.QosBandwidthLimitRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">direction=None</em>, <em class="sig-param">max_burst_kbps=None</em>, <em class="sig-param">max_kbps=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QosBandwidthLimitRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing QosBandwidthLimitRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The direction of traffic. Defaults to “egress”. Changing this updates the direction of the
existing QoS bandwidth limit rule.</p></li>
<li><p><strong>max_burst_kbps</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum burst size in kilobits of a QoS bandwidth limit rule. Changing this updates the
maximum burst size in kilobits of the existing QoS bandwidth limit rule.</p></li>
<li><p><strong>max_kbps</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum kilobits per second of a QoS bandwidth limit rule. Changing this updates the
maximum kilobits per second of the existing QoS bandwidth limit rule.</p></li>
<li><p><strong>qos_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The QoS policy reference. Changing this creates a new QoS bandwidth limit rule.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron QoS bandwidth limit rule. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new QoS bandwidth limit rule.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.QosBandwidthLimitRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QosBandwidthLimitRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.QosBandwidthLimitRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QosBandwidthLimitRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.QosDscpMarkingRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">QosDscpMarkingRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dscp_mark=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QosDscpMarkingRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Neutron QoS DSCP marking rule resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dscp_mark</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The value of DSCP mark. Changing this updates the DSCP mark value existing
QoS DSCP marking rule.</p></li>
<li><p><strong>qos_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The QoS policy reference. Changing this creates a new QoS DSCP marking rule.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron QoS DSCP marking rule. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new QoS DSCP marking rule.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.networking.QosDscpMarkingRule.dscp_mark">
<code class="sig-name descname">dscp_mark</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosDscpMarkingRule.dscp_mark" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of DSCP mark. Changing this updates the DSCP mark value existing
QoS DSCP marking rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosDscpMarkingRule.qos_policy_id">
<code class="sig-name descname">qos_policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosDscpMarkingRule.qos_policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The QoS policy reference. Changing this creates a new QoS DSCP marking rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosDscpMarkingRule.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosDscpMarkingRule.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron QoS DSCP marking rule. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new QoS DSCP marking rule.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.QosDscpMarkingRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dscp_mark=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QosDscpMarkingRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing QosDscpMarkingRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dscp_mark</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The value of DSCP mark. Changing this updates the DSCP mark value existing
QoS DSCP marking rule.</p></li>
<li><p><strong>qos_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The QoS policy reference. Changing this creates a new QoS DSCP marking rule.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron QoS DSCP marking rule. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new QoS DSCP marking rule.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.QosDscpMarkingRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QosDscpMarkingRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.QosDscpMarkingRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QosDscpMarkingRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.QosMinimumBandwidthRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">QosMinimumBandwidthRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">direction=None</em>, <em class="sig-param">min_kbps=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QosMinimumBandwidthRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Neutron QoS minimum bandwidth rule resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The direction of traffic. Defaults to “egress”. Changing this updates the direction of the
existing QoS minimum bandwidth rule.</p></li>
<li><p><strong>min_kbps</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum kilobits per second. Changing this updates the min kbps value of the existing
QoS minimum bandwidth rule.</p></li>
<li><p><strong>qos_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The QoS policy reference. Changing this creates a new QoS minimum bandwidth rule.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron QoS minimum bandwidth rule. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new QoS minimum bandwidth rule.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.networking.QosMinimumBandwidthRule.direction">
<code class="sig-name descname">direction</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosMinimumBandwidthRule.direction" title="Permalink to this definition">¶</a></dt>
<dd><p>The direction of traffic. Defaults to “egress”. Changing this updates the direction of the
existing QoS minimum bandwidth rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosMinimumBandwidthRule.min_kbps">
<code class="sig-name descname">min_kbps</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosMinimumBandwidthRule.min_kbps" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum kilobits per second. Changing this updates the min kbps value of the existing
QoS minimum bandwidth rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosMinimumBandwidthRule.qos_policy_id">
<code class="sig-name descname">qos_policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosMinimumBandwidthRule.qos_policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The QoS policy reference. Changing this creates a new QoS minimum bandwidth rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosMinimumBandwidthRule.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosMinimumBandwidthRule.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron QoS minimum bandwidth rule. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new QoS minimum bandwidth rule.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.QosMinimumBandwidthRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">direction=None</em>, <em class="sig-param">min_kbps=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QosMinimumBandwidthRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing QosMinimumBandwidthRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The direction of traffic. Defaults to “egress”. Changing this updates the direction of the
existing QoS minimum bandwidth rule.</p></li>
<li><p><strong>min_kbps</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum kilobits per second. Changing this updates the min kbps value of the existing
QoS minimum bandwidth rule.</p></li>
<li><p><strong>qos_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The QoS policy reference. Changing this creates a new QoS minimum bandwidth rule.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron QoS minimum bandwidth rule. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new QoS minimum bandwidth rule.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.QosMinimumBandwidthRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QosMinimumBandwidthRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.QosMinimumBandwidthRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QosMinimumBandwidthRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.QosPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">QosPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">is_default=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">shared=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">value_specs=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QosPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Neutron QoS policy resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the QoS policy.
Changing this updates the description of the existing QoS policy.</p></li>
<li><p><strong>is_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the QoS policy is default
QoS policy or not. Changing this updates the default status of the existing
QoS policy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the QoS policy. Changing this updates the name of
the existing QoS policy.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the QoS policy. Required if admin wants to
create a QoS policy for another project. Changing this creates a new QoS policy.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron Qos policy. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
QoS policy.</p></li>
<li><p><strong>shared</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether this QoS policy is shared across
all projects. Changing this updates the shared status of the existing
QoS policy.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the QoS policy.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.networking.QosPolicy.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosPolicy.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of tags assigned on the QoS policy, which have been
explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosPolicy.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosPolicy.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which QoS policy was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosPolicy.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosPolicy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable description for the QoS policy.
Changing this updates the description of the existing QoS policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosPolicy.is_default">
<code class="sig-name descname">is_default</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosPolicy.is_default" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the QoS policy is default
QoS policy or not. Changing this updates the default status of the existing
QoS policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosPolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the QoS policy. Changing this updates the name of
the existing QoS policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosPolicy.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosPolicy.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the QoS policy. Required if admin wants to
create a QoS policy for another project. Changing this creates a new QoS policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosPolicy.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosPolicy.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron Qos policy. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
QoS policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosPolicy.revision_number">
<code class="sig-name descname">revision_number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosPolicy.revision_number" title="Permalink to this definition">¶</a></dt>
<dd><p>The revision number of the QoS policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosPolicy.shared">
<code class="sig-name descname">shared</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosPolicy.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether this QoS policy is shared across
all projects. Changing this updates the shared status of the existing
QoS policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosPolicy.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosPolicy.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags for the QoS policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosPolicy.updated_at">
<code class="sig-name descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosPolicy.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which QoS policy was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QosPolicy.value_specs">
<code class="sig-name descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QosPolicy.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.QosPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">is_default=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">revision_number=None</em>, <em class="sig-param">shared=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">updated_at=None</em>, <em class="sig-param">value_specs=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QosPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing QosPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>all_tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The collection of tags assigned on the QoS policy, which have been
explicitly and implicitly added.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time at which QoS policy was created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the QoS policy.
Changing this updates the description of the existing QoS policy.</p></li>
<li><p><strong>is_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the QoS policy is default
QoS policy or not. Changing this updates the default status of the existing
QoS policy.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the QoS policy. Changing this updates the name of
the existing QoS policy.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the QoS policy. Required if admin wants to
create a QoS policy for another project. Changing this creates a new QoS policy.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron Qos policy. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
QoS policy.</p></li>
<li><p><strong>revision_number</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The revision number of the QoS policy.</p></li>
<li><p><strong>shared</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether this QoS policy is shared across
all projects. Changing this updates the shared status of the existing
QoS policy.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the QoS policy.</p></li>
<li><p><strong>updated_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time at which QoS policy was created.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.QosPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QosPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.QosPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QosPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.QuotaV2">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">QuotaV2</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">floatingip=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">rbac_policy=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router=None</em>, <em class="sig-param">security_group=None</em>, <em class="sig-param">security_group_rule=None</em>, <em class="sig-param">subnet=None</em>, <em class="sig-param">subnetpool=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QuotaV2" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 networking quota resource within OpenStack.</p>
<blockquote>
<div><p><strong>Note:</strong> This usually requires admin privileges.</p>
<dl class="simple">
<dt><strong>Note:</strong> This resource has a no-op deletion so no actual actions will be done against the OpenStack API </dt><dd><p>in case of delete call.</p>
</dd>
</dl>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>floatingip</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for floating IPs. Changing this updates the
existing quota.</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for networks. Changing this updates the
existing quota.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for ports. Changing this updates the
existing quota.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the project to manage quota. Changing this
creates new quota.</p></li>
<li><p><strong>rbac_policy</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for RBAC policies.
Changing this updates the existing quota.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the quota. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates new quota.</p></li>
<li><p><strong>router</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for routers. Changing this updates the
existing quota.</p></li>
<li><p><strong>security_group</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for security groups. Changing
this updates the existing quota.</p></li>
<li><p><strong>security_group_rule</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for security group rules.
Changing this updates the existing quota.</p></li>
<li><p><strong>subnet</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for subnets. Changing
this updates the existing quota.</p></li>
<li><p><strong>subnetpool</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for subnetpools.
Changing this updates the existing quota.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.networking.QuotaV2.floatingip">
<code class="sig-name descname">floatingip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QuotaV2.floatingip" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for floating IPs. Changing this updates the
existing quota.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QuotaV2.network">
<code class="sig-name descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QuotaV2.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for networks. Changing this updates the
existing quota.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QuotaV2.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QuotaV2.port" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for ports. Changing this updates the
existing quota.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QuotaV2.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QuotaV2.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the project to manage quota. Changing this
creates new quota.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QuotaV2.rbac_policy">
<code class="sig-name descname">rbac_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QuotaV2.rbac_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for RBAC policies.
Changing this updates the existing quota.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QuotaV2.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QuotaV2.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to create the quota. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates new quota.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QuotaV2.router">
<code class="sig-name descname">router</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QuotaV2.router" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for routers. Changing this updates the
existing quota.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QuotaV2.security_group">
<code class="sig-name descname">security_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QuotaV2.security_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for security groups. Changing
this updates the existing quota.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QuotaV2.security_group_rule">
<code class="sig-name descname">security_group_rule</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QuotaV2.security_group_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for security group rules.
Changing this updates the existing quota.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QuotaV2.subnet">
<code class="sig-name descname">subnet</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QuotaV2.subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for subnets. Changing
this updates the existing quota.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.QuotaV2.subnetpool">
<code class="sig-name descname">subnetpool</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.QuotaV2.subnetpool" title="Permalink to this definition">¶</a></dt>
<dd><p>Quota value for subnetpools.
Changing this updates the existing quota.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.QuotaV2.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">floatingip=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">rbac_policy=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router=None</em>, <em class="sig-param">security_group=None</em>, <em class="sig-param">security_group_rule=None</em>, <em class="sig-param">subnet=None</em>, <em class="sig-param">subnetpool=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QuotaV2.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing QuotaV2 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>floatingip</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for floating IPs. Changing this updates the
existing quota.</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for networks. Changing this updates the
existing quota.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for ports. Changing this updates the
existing quota.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the project to manage quota. Changing this
creates new quota.</p></li>
<li><p><strong>rbac_policy</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for RBAC policies.
Changing this updates the existing quota.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to create the quota. If
omitted, the <code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this
creates new quota.</p></li>
<li><p><strong>router</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for routers. Changing this updates the
existing quota.</p></li>
<li><p><strong>security_group</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for security groups. Changing
this updates the existing quota.</p></li>
<li><p><strong>security_group_rule</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for security group rules.
Changing this updates the existing quota.</p></li>
<li><p><strong>subnet</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for subnets. Changing
this updates the existing quota.</p></li>
<li><p><strong>subnetpool</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Quota value for subnetpools.
Changing this updates the existing quota.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.QuotaV2.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QuotaV2.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.QuotaV2.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.QuotaV2.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.RbacPolicyV2">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">RbacPolicyV2</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">object_type=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">target_tenant=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.RbacPolicyV2" title="Permalink to this definition">¶</a></dt>
<dd><p>The RBAC policy resource contains functionality for working with Neutron RBAC
Policies. Role-Based Access Control (RBAC) policy framework enables both
operators and users to grant access to resources for specific projects.</p>
<p>Sharing an object with a specific project is accomplished by creating a
policy entry that permits the target project the <code class="docutils literal notranslate"><span class="pre">access_as_shared</span></code> action
on that object.</p>
<p>To make a network available as an external network for specific projects
rather than all projects, use the <code class="docutils literal notranslate"><span class="pre">access_as_external</span></code> action.
If a network is marked as external during creation, it now implicitly creates
a wildcard RBAC policy granting everyone access to preserve previous behavior
before this feature was added.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action for the RBAC policy. Can either be
<code class="docutils literal notranslate"><span class="pre">access_as_external</span></code> or <code class="docutils literal notranslate"><span class="pre">access_as_shared</span></code>.</p></li>
<li><p><strong>object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the <code class="docutils literal notranslate"><span class="pre">object_type</span></code> resource. An
<code class="docutils literal notranslate"><span class="pre">object_type</span></code> of <code class="docutils literal notranslate"><span class="pre">network</span></code> returns a network ID and an <code class="docutils literal notranslate"><span class="pre">object_type</span></code> of
<code class="docutils literal notranslate"><span class="pre">qos_policy</span></code> returns a QoS ID.</p></li>
<li><p><strong>object_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the object that the RBAC policy
affects. Can either be <code class="docutils literal notranslate"><span class="pre">qos-policy</span></code> or <code class="docutils literal notranslate"><span class="pre">network</span></code>.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a subnet. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
routing entry.</p></li>
<li><p><strong>target_tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the tenant to which the RBAC policy
will be enforced.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.networking.RbacPolicyV2.action">
<code class="sig-name descname">action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RbacPolicyV2.action" title="Permalink to this definition">¶</a></dt>
<dd><p>Action for the RBAC policy. Can either be
<code class="docutils literal notranslate"><span class="pre">access_as_external</span></code> or <code class="docutils literal notranslate"><span class="pre">access_as_shared</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.RbacPolicyV2.object_id">
<code class="sig-name descname">object_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RbacPolicyV2.object_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the <code class="docutils literal notranslate"><span class="pre">object_type</span></code> resource. An
<code class="docutils literal notranslate"><span class="pre">object_type</span></code> of <code class="docutils literal notranslate"><span class="pre">network</span></code> returns a network ID and an <code class="docutils literal notranslate"><span class="pre">object_type</span></code> of
<code class="docutils literal notranslate"><span class="pre">qos_policy</span></code> returns a QoS ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.RbacPolicyV2.object_type">
<code class="sig-name descname">object_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RbacPolicyV2.object_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the object that the RBAC policy
affects. Can either be <code class="docutils literal notranslate"><span class="pre">qos-policy</span></code> or <code class="docutils literal notranslate"><span class="pre">network</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.RbacPolicyV2.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RbacPolicyV2.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a subnet. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
routing entry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.RbacPolicyV2.target_tenant">
<code class="sig-name descname">target_tenant</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RbacPolicyV2.target_tenant" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the tenant to which the RBAC policy
will be enforced.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.RbacPolicyV2.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">object_id=None</em>, <em class="sig-param">object_type=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">target_tenant=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.RbacPolicyV2.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RbacPolicyV2 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Action for the RBAC policy. Can either be
<code class="docutils literal notranslate"><span class="pre">access_as_external</span></code> or <code class="docutils literal notranslate"><span class="pre">access_as_shared</span></code>.</p></li>
<li><p><strong>object_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the <code class="docutils literal notranslate"><span class="pre">object_type</span></code> resource. An
<code class="docutils literal notranslate"><span class="pre">object_type</span></code> of <code class="docutils literal notranslate"><span class="pre">network</span></code> returns a network ID and an <code class="docutils literal notranslate"><span class="pre">object_type</span></code> of
<code class="docutils literal notranslate"><span class="pre">qos_policy</span></code> returns a QoS ID.</p></li>
<li><p><strong>object_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the object that the RBAC policy
affects. Can either be <code class="docutils literal notranslate"><span class="pre">qos-policy</span></code> or <code class="docutils literal notranslate"><span class="pre">network</span></code>.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a subnet. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
routing entry.</p></li>
<li><p><strong>target_tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the tenant to which the RBAC policy
will be enforced.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.RbacPolicyV2.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.RbacPolicyV2.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.RbacPolicyV2.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.RbacPolicyV2.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.Router">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">Router</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_state_up=None</em>, <em class="sig-param">availability_zone_hints=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">distributed=None</em>, <em class="sig-param">enable_snat=None</em>, <em class="sig-param">external_fixed_ips=None</em>, <em class="sig-param">external_gateway=None</em>, <em class="sig-param">external_network_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">value_specs=None</em>, <em class="sig-param">vendor_options=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Router" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 router resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Administrative up/down status for the router
(must be “true” or “false” if provided). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing router.</p></li>
<li><p><strong>availability_zone_hints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An availability zone is used to make 
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description for the router.</p></li>
<li><p><strong>distributed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.</p></li>
<li><p><strong>enable_snat</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable Source NAT for the router. Valid values are
“true” or “false”. An <code class="docutils literal notranslate"><span class="pre">external_network_id</span></code> has to be set in order to
set this property. Changing this updates the <code class="docutils literal notranslate"><span class="pre">enable_snat</span></code> of the router.
Setting this value <strong>requires</strong> an <strong>ext-gw-mode</strong> extension to be enabled
in OpenStack Neutron.</p></li>
<li><p><strong>external_fixed_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An external fixed IP for the router. This
can be repeated. The structure is described below. An <code class="docutils literal notranslate"><span class="pre">external_network_id</span></code>
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.</p></li>
<li><p><strong>external_gateway</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.</p></li>
<li><p><strong>external_network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the router. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing router.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
router.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the router.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional driver-specific options.</p></li>
<li><p><strong>vendor_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional vendor-specific options.
Supported options are described below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>external_fixed_ips</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP address to set on the router.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Subnet in which the fixed IP belongs to.</p></li>
</ul>
<p>The <strong>vendor_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">setRouterGatewayAfterCreate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean to control whether
the Router gateway is assigned during creation or updated after creation.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>Administrative up/down status for the router
(must be “true” or “false” if provided). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of tags assigned on the router, which have been
explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.availability_zone_hints">
<code class="sig-name descname">availability_zone_hints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.availability_zone_hints" title="Permalink to this definition">¶</a></dt>
<dd><p>An availability zone is used to make 
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description for the router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.distributed">
<code class="sig-name descname">distributed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.distributed" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.enable_snat">
<code class="sig-name descname">enable_snat</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.enable_snat" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable Source NAT for the router. Valid values are
“true” or “false”. An <code class="docutils literal notranslate"><span class="pre">external_network_id</span></code> has to be set in order to
set this property. Changing this updates the <code class="docutils literal notranslate"><span class="pre">enable_snat</span></code> of the router.
Setting this value <strong>requires</strong> an <strong>ext-gw-mode</strong> extension to be enabled
in OpenStack Neutron.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.external_fixed_ips">
<code class="sig-name descname">external_fixed_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.external_fixed_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>An external fixed IP for the router. This
can be repeated. The structure is described below. An <code class="docutils literal notranslate"><span class="pre">external_network_id</span></code>
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IP address to set on the router.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Subnet in which the fixed IP belongs to.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.external_gateway">
<code class="sig-name descname">external_gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.external_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.external_network_id">
<code class="sig-name descname">external_network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.external_network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the router. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags for the router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.value_specs">
<code class="sig-name descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional driver-specific options.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Router.vendor_options">
<code class="sig-name descname">vendor_options</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Router.vendor_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional vendor-specific options.
Supported options are described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">setRouterGatewayAfterCreate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean to control whether
the Router gateway is assigned during creation or updated after creation.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.Router.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_state_up=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">availability_zone_hints=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">distributed=None</em>, <em class="sig-param">enable_snat=None</em>, <em class="sig-param">external_fixed_ips=None</em>, <em class="sig-param">external_gateway=None</em>, <em class="sig-param">external_network_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">value_specs=None</em>, <em class="sig-param">vendor_options=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Router.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Router resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Administrative up/down status for the router
(must be “true” or “false” if provided). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing router.</p></li>
<li><p><strong>all_tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The collection of tags assigned on the router, which have been
explicitly and implicitly added.</p></li>
<li><p><strong>availability_zone_hints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An availability zone is used to make 
network resources highly available. Used for resources with high availability so that they are scheduled on different availability zones. Changing
this creates a new router.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description for the router.</p></li>
<li><p><strong>distributed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether or not to create a
distributed router. The default policy setting in Neutron restricts
usage of this property to administrative users only.</p></li>
<li><p><strong>enable_snat</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable Source NAT for the router. Valid values are
“true” or “false”. An <code class="docutils literal notranslate"><span class="pre">external_network_id</span></code> has to be set in order to
set this property. Changing this updates the <code class="docutils literal notranslate"><span class="pre">enable_snat</span></code> of the router.
Setting this value <strong>requires</strong> an <strong>ext-gw-mode</strong> extension to be enabled
in OpenStack Neutron.</p></li>
<li><p><strong>external_fixed_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An external fixed IP for the router. This
can be repeated. The structure is described below. An <code class="docutils literal notranslate"><span class="pre">external_network_id</span></code>
has to be set in order to set this property. Changing this updates the
external fixed IPs of the router.</p></li>
<li><p><strong>external_gateway</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The
network UUID of an external gateway for the router. A router with an
external gateway is required if any compute instances or load balancers
will be using floating IPs. Changing this updates the external gateway
of an existing router.</p></li>
<li><p><strong>external_network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network UUID of an external gateway
for the router. A router with an external gateway is required if any
compute instances or load balancers will be using floating IPs. Changing
this updates the external gateway of the router.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the router. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing router.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
router.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the router.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the floating IP. Required if admin wants
to create a router for another tenant. Changing this creates a new router.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional driver-specific options.</p></li>
<li><p><strong>vendor_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional vendor-specific options.
Supported options are described below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>external_fixed_ips</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP address to set on the router.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Subnet in which the fixed IP belongs to.</p></li>
</ul>
<p>The <strong>vendor_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">setRouterGatewayAfterCreate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean to control whether
the Router gateway is assigned during creation or updated after creation.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.Router.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Router.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.Router.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Router.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.RouterInterface">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">RouterInterface</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router_id=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.RouterInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 router interface resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the port this interface connects to. Changing
this creates a new router interface.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
router interface.</p></li>
<li><p><strong>router_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the router this interface belongs to. Changing
this creates a new router interface.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the subnet this interface connects to. Changing
this creates a new router interface.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.networking.RouterInterface.port_id">
<code class="sig-name descname">port_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RouterInterface.port_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the port this interface connects to. Changing
this creates a new router interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.RouterInterface.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RouterInterface.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
router interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.RouterInterface.router_id">
<code class="sig-name descname">router_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RouterInterface.router_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the router this interface belongs to. Changing
this creates a new router interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.RouterInterface.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RouterInterface.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the subnet this interface connects to. Changing
this creates a new router interface.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.RouterInterface.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router_id=None</em>, <em class="sig-param">subnet_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.RouterInterface.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RouterInterface resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the port this interface connects to. Changing
this creates a new router interface.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to create a router. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
router interface.</p></li>
<li><p><strong>router_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the router this interface belongs to. Changing
this creates a new router interface.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the subnet this interface connects to. Changing
this creates a new router interface.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.RouterInterface.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.RouterInterface.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.RouterInterface.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.RouterInterface.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.RouterRoute">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">RouterRoute</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">destination_cidr=None</em>, <em class="sig-param">next_hop=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.RouterRoute" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a routing entry on a OpenStack V2 router.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">next_hop</span></code> IP address must be directly reachable from the router at the <code class="docutils literal notranslate"><span class="pre">networking.RouterRoute</span></code>
resource creation time.  You can ensure that by explicitly specifying a dependency on the <code class="docutils literal notranslate"><span class="pre">networking.RouterInterface</span></code>
resource that connects the next hop to the router, as in the example above.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CIDR block to match on the packet’s destination IP. Changing
this creates a new routing entry.</p></li>
<li><p><strong>next_hop</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address of the next hop gateway.  Changing
this creates a new routing entry.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a router. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
routing entry.</p></li>
<li><p><strong>router_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the router this routing entry belongs to. Changing
this creates a new routing entry.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.networking.RouterRoute.destination_cidr">
<code class="sig-name descname">destination_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RouterRoute.destination_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR block to match on the packet’s destination IP. Changing
this creates a new routing entry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.RouterRoute.next_hop">
<code class="sig-name descname">next_hop</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RouterRoute.next_hop" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address of the next hop gateway.  Changing
this creates a new routing entry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.RouterRoute.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RouterRoute.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a router. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
routing entry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.RouterRoute.router_id">
<code class="sig-name descname">router_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.RouterRoute.router_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the router this routing entry belongs to. Changing
this creates a new routing entry.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.RouterRoute.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">destination_cidr=None</em>, <em class="sig-param">next_hop=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.RouterRoute.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RouterRoute resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CIDR block to match on the packet’s destination IP. Changing
this creates a new routing entry.</p></li>
<li><p><strong>next_hop</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address of the next hop gateway.  Changing
this creates a new routing entry.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a router. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
routing entry.</p></li>
<li><p><strong>router_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the router this routing entry belongs to. Changing
this creates a new routing entry.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.RouterRoute.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.RouterRoute.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.RouterRoute.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.RouterRoute.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.SecGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">SecGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">delete_default_rules=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SecGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 neutron security group resource within OpenStack.
Unlike Nova security groups, neutron separates the group from the rules
and also allows an admin to target a specific tenant_id.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>delete_default_rules</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to delete the default
egress security rules. This is <code class="docutils literal notranslate"><span class="pre">false</span></code> by default. See the below note
for more information.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the security group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the security group.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
security group.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the security group.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the security group. Required if admin
wants to create a port for another tenant. Changing this creates a new
security group.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroup.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of tags assigned on the security group, which have
been explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroup.delete_default_rules">
<code class="sig-name descname">delete_default_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.delete_default_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to delete the default
egress security rules. This is <code class="docutils literal notranslate"><span class="pre">false</span></code> by default. See the below note
for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroup.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroup.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroup.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags for the security group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroup.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the security group. Required if admin
wants to create a port for another tenant. Changing this creates a new
security group.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.SecGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">delete_default_rules=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>all_tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The collection of tags assigned on the security group, which have
been explicitly and implicitly added.</p></li>
<li><p><strong>delete_default_rules</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to delete the default
egress security rules. This is <code class="docutils literal notranslate"><span class="pre">false</span></code> by default. See the below note
for more information.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the security group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the security group.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
security group.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the security group.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the security group. Required if admin
wants to create a port for another tenant. Changing this creates a new
security group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.SecGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.SecGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SecGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.SecGroupRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">SecGroupRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">direction=None</em>, <em class="sig-param">ethertype=None</em>, <em class="sig-param">port_range_max=None</em>, <em class="sig-param">port_range_min=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">remote_group_id=None</em>, <em class="sig-param">remote_ip_prefix=None</em>, <em class="sig-param">security_group_id=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 neutron security group rule resource within OpenStack.
Unlike Nova security groups, neutron separates the group from the rules
and also allows an admin to target a specific tenant_id.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the rule. Changing this creates a new security group rule.</p></li>
<li><p><strong>direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The direction of the rule, valid values are <strong>ingress</strong>
or <strong>egress</strong>. Changing this creates a new security group rule.</p></li>
<li><p><strong>ethertype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The layer 3 protocol type, valid values are <strong>IPv4</strong>
or <strong>IPv6</strong>. Changing this creates a new security group rule.</p></li>
<li><p><strong>port_range_max</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The higher part of the allowed port range, valid
integer value needs to be between 1 and 65535. Changing this creates a new
security group rule.</p></li>
<li><p><strong>port_range_min</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The lower part of the allowed port range, valid
integer value needs to be between 1 and 65535. Changing this creates a new
security group rule.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The layer 4 protocol type, valid values are following. Changing this creates a new security group rule. This is required if you want to specify a port range.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">__tcp__</span>
<span class="o">*</span> <span class="n">__udp__</span>
<span class="o">*</span> <span class="n">__icmp__</span>
<span class="o">*</span> <span class="n">__ah__</span>
<span class="o">*</span> <span class="n">__dccp__</span>
<span class="o">*</span> <span class="n">__egp__</span>
<span class="o">*</span> <span class="n">__esp__</span>
<span class="o">*</span> <span class="n">__gre__</span>
<span class="o">*</span> <span class="n">__igmp__</span>
<span class="o">*</span> <span class="n">__ipv6</span><span class="o">-</span><span class="n">encap__</span>
<span class="o">*</span> <span class="n">__ipv6</span><span class="o">-</span><span class="n">frag__</span>
<span class="o">*</span> <span class="n">__ipv6</span><span class="o">-</span><span class="n">icmp__</span>
<span class="o">*</span> <span class="n">__ipv6</span><span class="o">-</span><span class="n">nonxt__</span>
<span class="o">*</span> <span class="n">__ipv6</span><span class="o">-</span><span class="n">opts__</span>
<span class="o">*</span> <span class="n">__ipv6</span><span class="o">-</span><span class="n">route__</span>
<span class="o">*</span> <span class="n">__ospf__</span>
<span class="o">*</span> <span class="n">__pgm__</span>
<span class="o">*</span> <span class="n">__rsvp__</span>
<span class="o">*</span> <span class="n">__sctp__</span>
<span class="o">*</span> <span class="n">__udplite__</span>
<span class="o">*</span> <span class="n">__vrrp__</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
security group rule.</p></li>
<li><p><strong>remote_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The remote group id, the value needs to be an
Openstack ID of a security group in the same tenant. Changing this creates
a new security group rule.</p></li>
<li><p><strong>remote_ip_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The remote CIDR, the value needs to be a valid
CIDR (i.e. 192.168.0.0/16). Changing this creates a new security group rule.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security group id the rule should belong
to, the value needs to be an Openstack ID of a security group in the same
tenant. Changing this creates a new security group rule.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the security group. Required if admin
wants to create a port for another tenant. Changing this creates a new
security group rule.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the rule. Changing this creates a new security group rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.direction">
<code class="sig-name descname">direction</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.direction" title="Permalink to this definition">¶</a></dt>
<dd><p>The direction of the rule, valid values are <strong>ingress</strong>
or <strong>egress</strong>. Changing this creates a new security group rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.ethertype">
<code class="sig-name descname">ethertype</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.ethertype" title="Permalink to this definition">¶</a></dt>
<dd><p>The layer 3 protocol type, valid values are <strong>IPv4</strong>
or <strong>IPv6</strong>. Changing this creates a new security group rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.port_range_max">
<code class="sig-name descname">port_range_max</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.port_range_max" title="Permalink to this definition">¶</a></dt>
<dd><p>The higher part of the allowed port range, valid
integer value needs to be between 1 and 65535. Changing this creates a new
security group rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.port_range_min">
<code class="sig-name descname">port_range_min</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.port_range_min" title="Permalink to this definition">¶</a></dt>
<dd><p>The lower part of the allowed port range, valid
integer value needs to be between 1 and 65535. Changing this creates a new
security group rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.protocol">
<code class="sig-name descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The layer 4 protocol type, valid values are following. Changing this creates a new security group rule. This is required if you want to specify a port range.</p>
<ul class="simple">
<li><p><strong>tcp</strong></p></li>
<li><p><strong>udp</strong></p></li>
<li><p><strong>icmp</strong></p></li>
<li><p><strong>ah</strong></p></li>
<li><p><strong>dccp</strong></p></li>
<li><p><strong>egp</strong></p></li>
<li><p><strong>esp</strong></p></li>
<li><p><strong>gre</strong></p></li>
<li><p><strong>igmp</strong></p></li>
<li><p><strong>ipv6-encap</strong></p></li>
<li><p><strong>ipv6-frag</strong></p></li>
<li><p><strong>ipv6-icmp</strong></p></li>
<li><p><strong>ipv6-nonxt</strong></p></li>
<li><p><strong>ipv6-opts</strong></p></li>
<li><p><strong>ipv6-route</strong></p></li>
<li><p><strong>ospf</strong></p></li>
<li><p><strong>pgm</strong></p></li>
<li><p><strong>rsvp</strong></p></li>
<li><p><strong>sctp</strong></p></li>
<li><p><strong>udplite</strong></p></li>
<li><p><strong>vrrp</strong></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
security group rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.remote_group_id">
<code class="sig-name descname">remote_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.remote_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The remote group id, the value needs to be an
Openstack ID of a security group in the same tenant. Changing this creates
a new security group rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.remote_ip_prefix">
<code class="sig-name descname">remote_ip_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.remote_ip_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The remote CIDR, the value needs to be a valid
CIDR (i.e. 192.168.0.0/16). Changing this creates a new security group rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The security group id the rule should belong
to, the value needs to be an Openstack ID of a security group in the same
tenant. Changing this creates a new security group rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SecGroupRule.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the security group. Required if admin
wants to create a port for another tenant. Changing this creates a new
security group rule.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.SecGroupRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">direction=None</em>, <em class="sig-param">ethertype=None</em>, <em class="sig-param">port_range_max=None</em>, <em class="sig-param">port_range_min=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">remote_group_id=None</em>, <em class="sig-param">remote_ip_prefix=None</em>, <em class="sig-param">security_group_id=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecGroupRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the rule. Changing this creates a new security group rule.</p></li>
<li><p><strong>direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The direction of the rule, valid values are <strong>ingress</strong>
or <strong>egress</strong>. Changing this creates a new security group rule.</p></li>
<li><p><strong>ethertype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The layer 3 protocol type, valid values are <strong>IPv4</strong>
or <strong>IPv6</strong>. Changing this creates a new security group rule.</p></li>
<li><p><strong>port_range_max</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The higher part of the allowed port range, valid
integer value needs to be between 1 and 65535. Changing this creates a new
security group rule.</p></li>
<li><p><strong>port_range_min</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The lower part of the allowed port range, valid
integer value needs to be between 1 and 65535. Changing this creates a new
security group rule.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The layer 4 protocol type, valid values are following. Changing this creates a new security group rule. This is required if you want to specify a port range.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">__tcp__</span>
<span class="o">*</span> <span class="n">__udp__</span>
<span class="o">*</span> <span class="n">__icmp__</span>
<span class="o">*</span> <span class="n">__ah__</span>
<span class="o">*</span> <span class="n">__dccp__</span>
<span class="o">*</span> <span class="n">__egp__</span>
<span class="o">*</span> <span class="n">__esp__</span>
<span class="o">*</span> <span class="n">__gre__</span>
<span class="o">*</span> <span class="n">__igmp__</span>
<span class="o">*</span> <span class="n">__ipv6</span><span class="o">-</span><span class="n">encap__</span>
<span class="o">*</span> <span class="n">__ipv6</span><span class="o">-</span><span class="n">frag__</span>
<span class="o">*</span> <span class="n">__ipv6</span><span class="o">-</span><span class="n">icmp__</span>
<span class="o">*</span> <span class="n">__ipv6</span><span class="o">-</span><span class="n">nonxt__</span>
<span class="o">*</span> <span class="n">__ipv6</span><span class="o">-</span><span class="n">opts__</span>
<span class="o">*</span> <span class="n">__ipv6</span><span class="o">-</span><span class="n">route__</span>
<span class="o">*</span> <span class="n">__ospf__</span>
<span class="o">*</span> <span class="n">__pgm__</span>
<span class="o">*</span> <span class="n">__rsvp__</span>
<span class="o">*</span> <span class="n">__sctp__</span>
<span class="o">*</span> <span class="n">__udplite__</span>
<span class="o">*</span> <span class="n">__vrrp__</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to create a port. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
security group rule.</p></li>
<li><p><strong>remote_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The remote group id, the value needs to be an
Openstack ID of a security group in the same tenant. Changing this creates
a new security group rule.</p></li>
<li><p><strong>remote_ip_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The remote CIDR, the value needs to be a valid
CIDR (i.e. 192.168.0.0/16). Changing this creates a new security group rule.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The security group id the rule should belong
to, the value needs to be an Openstack ID of a security group in the same
tenant. Changing this creates a new security group rule.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the security group. Required if admin
wants to create a port for another tenant. Changing this creates a new
security group rule.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.SecGroupRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.SecGroupRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SecGroupRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.Subnet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">Subnet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allocation_pools=None</em>, <em class="sig-param">allocation_pools_collection=None</em>, <em class="sig-param">cidr=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dns_nameservers=None</em>, <em class="sig-param">enable_dhcp=None</em>, <em class="sig-param">gateway_ip=None</em>, <em class="sig-param">host_routes=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">ipv6_address_mode=None</em>, <em class="sig-param">ipv6_ra_mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_id=None</em>, <em class="sig-param">no_gateway=None</em>, <em class="sig-param">prefix_length=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">subnetpool_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">value_specs=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Neutron subnet resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocation_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block declaring the start and end range of
the IP addresses available for use with DHCP in this subnet. Multiple
<code class="docutils literal notranslate"><span class="pre">allocation_pool</span></code> blocks can be declared, providing the subnet with more
than one range of IP addresses to use with DHCP. However, each IP range
must be from the same CIDR that the subnet is part of.
The <code class="docutils literal notranslate"><span class="pre">allocation_pool</span></code> block is documented below.</p></li>
<li><p><strong>allocation_pools_collection</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block declaring the start and end range of the IP addresses available for
use with DHCP in this subnet.
The <code class="docutils literal notranslate"><span class="pre">allocation_pools</span></code> block is documented below.</p></li>
<li><p><strong>cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the subnet. Changing this
updates the name of the existing subnet.</p></li>
<li><p><strong>dns_nameservers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.</p></li>
<li><p><strong>enable_dhcp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the network.
Acceptable values are “true” and “false”. Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.</p></li>
<li><p><strong>gateway_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default gateway used by devices in this subnet.
Leaving this blank and not setting <code class="docutils literal notranslate"><span class="pre">no_gateway</span></code> will cause a default
gateway of <code class="docutils literal notranslate"><span class="pre">.1</span></code> to be used. Changing this updates the gateway IP of the
existing subnet.</p></li>
<li><p><strong>host_routes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – (<strong>Deprecated</strong> - use <code class="docutils literal notranslate"><span class="pre">networking.SubnetRoute</span></code>
instead) An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.</p></li>
<li><p><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – IP version, either 4 (default) or 6. Changing this creates a
new subnet.</p></li>
<li><p><strong>ipv6_address_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv6 address mode. Valid values are
<code class="docutils literal notranslate"><span class="pre">dhcpv6-stateful</span></code>, <code class="docutils literal notranslate"><span class="pre">dhcpv6-stateless</span></code>, or <code class="docutils literal notranslate"><span class="pre">slaac</span></code>.</p></li>
<li><p><strong>ipv6_ra_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv6 Router Advertisement mode. Valid values
are <code class="docutils literal notranslate"><span class="pre">dhcpv6-stateful</span></code>, <code class="docutils literal notranslate"><span class="pre">dhcpv6-stateless</span></code>, or <code class="docutils literal notranslate"><span class="pre">slaac</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnet. Changing this updates the name of
the existing subnet.</p></li>
<li><p><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of the parent network. Changing this
creates a new subnet.</p></li>
<li><p><strong>no_gateway</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.</p></li>
<li><p><strong>prefix_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The prefix length to use when creating a subnet
from a subnet pool. The default subnet pool prefix length that was defined
when creating the subnet pool will be used if not provided. Changing this
creates a new subnet.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
subnet.</p></li>
<li><p><strong>subnetpool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnetpool associated with the subnet.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the subnet.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>allocation_pools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ending address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The starting address.</p></li>
</ul>
<p>The <strong>allocation_pools_collection</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ending address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The starting address.</p></li>
</ul>
<p>The <strong>host_routes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">destination_cidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The destination CIDR.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">next_hop</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The next hop in the route.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of ags assigned on the subnet, which have been
explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.allocation_pools">
<code class="sig-name descname">allocation_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.allocation_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>A block declaring the start and end range of
the IP addresses available for use with DHCP in this subnet. Multiple
<code class="docutils literal notranslate"><span class="pre">allocation_pool</span></code> blocks can be declared, providing the subnet with more
than one range of IP addresses to use with DHCP. However, each IP range
must be from the same CIDR that the subnet is part of.
The <code class="docutils literal notranslate"><span class="pre">allocation_pool</span></code> block is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ending address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The starting address.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.allocation_pools_collection">
<code class="sig-name descname">allocation_pools_collection</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.allocation_pools_collection" title="Permalink to this definition">¶</a></dt>
<dd><p>A block declaring the start and end range of the IP addresses available for
use with DHCP in this subnet.
The <code class="docutils literal notranslate"><span class="pre">allocation_pools</span></code> block is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ending address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The starting address.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.cidr">
<code class="sig-name descname">cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description of the subnet. Changing this
updates the name of the existing subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.dns_nameservers">
<code class="sig-name descname">dns_nameservers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.dns_nameservers" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.enable_dhcp">
<code class="sig-name descname">enable_dhcp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.enable_dhcp" title="Permalink to this definition">¶</a></dt>
<dd><p>The administrative state of the network.
Acceptable values are “true” and “false”. Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.gateway_ip">
<code class="sig-name descname">gateway_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.gateway_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Default gateway used by devices in this subnet.
Leaving this blank and not setting <code class="docutils literal notranslate"><span class="pre">no_gateway</span></code> will cause a default
gateway of <code class="docutils literal notranslate"><span class="pre">.1</span></code> to be used. Changing this updates the gateway IP of the
existing subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.host_routes">
<code class="sig-name descname">host_routes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.host_routes" title="Permalink to this definition">¶</a></dt>
<dd><p>(<strong>Deprecated</strong> - use <code class="docutils literal notranslate"><span class="pre">networking.SubnetRoute</span></code>
instead) An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">destination_cidr</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The destination CIDR.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">next_hop</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The next hop in the route.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.ip_version">
<code class="sig-name descname">ip_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.ip_version" title="Permalink to this definition">¶</a></dt>
<dd><p>IP version, either 4 (default) or 6. Changing this creates a
new subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.ipv6_address_mode">
<code class="sig-name descname">ipv6_address_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.ipv6_address_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv6 address mode. Valid values are
<code class="docutils literal notranslate"><span class="pre">dhcpv6-stateful</span></code>, <code class="docutils literal notranslate"><span class="pre">dhcpv6-stateless</span></code>, or <code class="docutils literal notranslate"><span class="pre">slaac</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.ipv6_ra_mode">
<code class="sig-name descname">ipv6_ra_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.ipv6_ra_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv6 Router Advertisement mode. Valid values
are <code class="docutils literal notranslate"><span class="pre">dhcpv6-stateful</span></code>, <code class="docutils literal notranslate"><span class="pre">dhcpv6-stateless</span></code>, or <code class="docutils literal notranslate"><span class="pre">slaac</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the subnet. Changing this updates the name of
the existing subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.network_id">
<code class="sig-name descname">network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of the parent network. Changing this
creates a new subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.no_gateway">
<code class="sig-name descname">no_gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.no_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.prefix_length">
<code class="sig-name descname">prefix_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.prefix_length" title="Permalink to this definition">¶</a></dt>
<dd><p>The prefix length to use when creating a subnet
from a subnet pool. The default subnet pool prefix length that was defined
when creating the subnet pool will be used if not provided. Changing this
creates a new subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.subnetpool_id">
<code class="sig-name descname">subnetpool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.subnetpool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the subnetpool associated with the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags for the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Subnet.value_specs">
<code class="sig-name descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Subnet.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.Subnet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">allocation_pools=None</em>, <em class="sig-param">allocation_pools_collection=None</em>, <em class="sig-param">cidr=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dns_nameservers=None</em>, <em class="sig-param">enable_dhcp=None</em>, <em class="sig-param">gateway_ip=None</em>, <em class="sig-param">host_routes=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">ipv6_address_mode=None</em>, <em class="sig-param">ipv6_ra_mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_id=None</em>, <em class="sig-param">no_gateway=None</em>, <em class="sig-param">prefix_length=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">subnetpool_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">value_specs=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Subnet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Subnet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>all_tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The collection of ags assigned on the subnet, which have been
explicitly and implicitly added.</p></li>
<li><p><strong>allocation_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block declaring the start and end range of
the IP addresses available for use with DHCP in this subnet. Multiple
<code class="docutils literal notranslate"><span class="pre">allocation_pool</span></code> blocks can be declared, providing the subnet with more
than one range of IP addresses to use with DHCP. However, each IP range
must be from the same CIDR that the subnet is part of.
The <code class="docutils literal notranslate"><span class="pre">allocation_pool</span></code> block is documented below.</p></li>
<li><p><strong>allocation_pools_collection</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A block declaring the start and end range of the IP addresses available for
use with DHCP in this subnet.
The <code class="docutils literal notranslate"><span class="pre">allocation_pools</span></code> block is documented below.</p></li>
<li><p><strong>cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CIDR representing IP range for this subnet, based on IP
version. You can omit this option if you are creating a subnet from a
subnet pool.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the subnet. Changing this
updates the name of the existing subnet.</p></li>
<li><p><strong>dns_nameservers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of DNS name server names used by hosts
in this subnet. Changing this updates the DNS name servers for the existing
subnet.</p></li>
<li><p><strong>enable_dhcp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The administrative state of the network.
Acceptable values are “true” and “false”. Changing this value enables or
disables the DHCP capabilities of the existing subnet. Defaults to true.</p></li>
<li><p><strong>gateway_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default gateway used by devices in this subnet.
Leaving this blank and not setting <code class="docutils literal notranslate"><span class="pre">no_gateway</span></code> will cause a default
gateway of <code class="docutils literal notranslate"><span class="pre">.1</span></code> to be used. Changing this updates the gateway IP of the
existing subnet.</p></li>
<li><p><strong>host_routes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – (<strong>Deprecated</strong> - use <code class="docutils literal notranslate"><span class="pre">networking.SubnetRoute</span></code>
instead) An array of routes that should be used by devices
with IPs from this subnet (not including local subnet route). The host_route
object structure is documented below. Changing this updates the host routes
for the existing subnet.</p></li>
<li><p><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – IP version, either 4 (default) or 6. Changing this creates a
new subnet.</p></li>
<li><p><strong>ipv6_address_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv6 address mode. Valid values are
<code class="docutils literal notranslate"><span class="pre">dhcpv6-stateful</span></code>, <code class="docutils literal notranslate"><span class="pre">dhcpv6-stateless</span></code>, or <code class="docutils literal notranslate"><span class="pre">slaac</span></code>.</p></li>
<li><p><strong>ipv6_ra_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv6 Router Advertisement mode. Valid values
are <code class="docutils literal notranslate"><span class="pre">dhcpv6-stateful</span></code>, <code class="docutils literal notranslate"><span class="pre">dhcpv6-stateless</span></code>, or <code class="docutils literal notranslate"><span class="pre">slaac</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnet. Changing this updates the name of
the existing subnet.</p></li>
<li><p><strong>network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of the parent network. Changing this
creates a new subnet.</p></li>
<li><p><strong>no_gateway</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Do not set a gateway IP on this subnet. Changing
this removes or adds a default gateway IP of the existing subnet.</p></li>
<li><p><strong>prefix_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The prefix length to use when creating a subnet
from a subnet pool. The default subnet pool prefix length that was defined
when creating the subnet pool will be used if not provided. Changing this
creates a new subnet.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnet. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
subnet.</p></li>
<li><p><strong>subnetpool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnetpool associated with the subnet.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the subnet.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the subnet. Required if admin wants to
create a subnet for another tenant. Changing this creates a new subnet.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>allocation_pools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ending address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The starting address.</p></li>
</ul>
<p>The <strong>allocation_pools_collection</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ending address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The starting address.</p></li>
</ul>
<p>The <strong>host_routes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">destination_cidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The destination CIDR.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">next_hop</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The next hop in the route.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.Subnet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Subnet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.Subnet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Subnet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.SubnetPool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">SubnetPool</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address_scope_id=None</em>, <em class="sig-param">default_prefixlen=None</em>, <em class="sig-param">default_quota=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">is_default=None</em>, <em class="sig-param">max_prefixlen=None</em>, <em class="sig-param">min_prefixlen=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">prefixes=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">shared=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">value_specs=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a V2 Neutron subnetpool resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_scope_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Neutron address scope to assign to the
subnetpool. Changing this updates the address scope id of the existing
subnetpool.</p></li>
<li><p><strong>default_prefixlen</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the prefix to allocate when the cidr
or prefixlen attributes are omitted when you create the subnet. Defaults to the
MinPrefixLen. Changing this updates the default prefixlen of the existing
subnetpool.</p></li>
<li><p><strong>default_quota</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The per-project quota on the prefix space that can be
allocated from the subnetpool for project subnets. Changing this updates the
default quota of the existing subnetpool.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the subnetpool.
Changing this updates the description of the existing subnetpool.</p></li>
<li><p><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The IP protocol version.</p></li>
<li><p><strong>is_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the subnetpool is default
subnetpool or not. Changing this updates the default status of the existing
subnetpool.</p></li>
<li><p><strong>max_prefixlen</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum prefix size that can be allocated from
the subnetpool. For IPv4 subnetpools, default is 32. For IPv6 subnetpools,
default is 128. Changing this updates the max prefixlen of the existing
subnetpool.</p></li>
<li><p><strong>min_prefixlen</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The smallest prefix that can be allocated from a
subnetpool. For IPv4 subnetpools, default is 8. For IPv6 subnetpools, default
is 64. Changing this updates the min prefixlen of the existing subnetpool.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnetpool. Changing this updates the name of
the existing subnetpool.</p></li>
<li><p><strong>prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of subnet prefixes to assign to the subnetpool.
Neutron API merges adjacent prefixes and treats them as a single prefix. Each
subnet prefix must be unique among all subnet prefixes in all subnetpools that
are associated with the address scope. Changing this updates the prefixes list
of the existing subnetpool.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the subnetpool. Required if admin wants to
create a subnetpool for another project. Changing this creates a new subnetpool.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnetpool. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
subnetpool.</p></li>
<li><p><strong>shared</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether this subnetpool is shared across
all projects. Changing this updates the shared status of the existing
subnetpool.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the subnetpool.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.address_scope_id">
<code class="sig-name descname">address_scope_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.address_scope_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Neutron address scope to assign to the
subnetpool. Changing this updates the address scope id of the existing
subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of tags assigned on the subnetpool, which have been
explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which subnetpool was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.default_prefixlen">
<code class="sig-name descname">default_prefixlen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.default_prefixlen" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the prefix to allocate when the cidr
or prefixlen attributes are omitted when you create the subnet. Defaults to the
MinPrefixLen. Changing this updates the default prefixlen of the existing
subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.default_quota">
<code class="sig-name descname">default_quota</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.default_quota" title="Permalink to this definition">¶</a></dt>
<dd><p>The per-project quota on the prefix space that can be
allocated from the subnetpool for project subnets. Changing this updates the
default quota of the existing subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable description for the subnetpool.
Changing this updates the description of the existing subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.ip_version">
<code class="sig-name descname">ip_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.ip_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP protocol version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.is_default">
<code class="sig-name descname">is_default</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.is_default" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the subnetpool is default
subnetpool or not. Changing this updates the default status of the existing
subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.max_prefixlen">
<code class="sig-name descname">max_prefixlen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.max_prefixlen" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum prefix size that can be allocated from
the subnetpool. For IPv4 subnetpools, default is 32. For IPv6 subnetpools,
default is 128. Changing this updates the max prefixlen of the existing
subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.min_prefixlen">
<code class="sig-name descname">min_prefixlen</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.min_prefixlen" title="Permalink to this definition">¶</a></dt>
<dd><p>The smallest prefix that can be allocated from a
subnetpool. For IPv4 subnetpools, default is 8. For IPv6 subnetpools, default
is 64. Changing this updates the min prefixlen of the existing subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the subnetpool. Changing this updates the name of
the existing subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.prefixes">
<code class="sig-name descname">prefixes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.prefixes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of subnet prefixes to assign to the subnetpool.
Neutron API merges adjacent prefixes and treats them as a single prefix. Each
subnet prefix must be unique among all subnet prefixes in all subnetpools that
are associated with the address scope. Changing this updates the prefixes list
of the existing subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.project_id">
<code class="sig-name descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the subnetpool. Required if admin wants to
create a subnetpool for another project. Changing this creates a new subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnetpool. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.revision_number">
<code class="sig-name descname">revision_number</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.revision_number" title="Permalink to this definition">¶</a></dt>
<dd><p>The revision number of the subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.shared">
<code class="sig-name descname">shared</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether this subnetpool is shared across
all projects. Changing this updates the shared status of the existing
subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags for the subnetpool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.updated_at">
<code class="sig-name descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which subnetpool was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetPool.value_specs">
<code class="sig-name descname">value_specs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.value_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of additional options.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.SubnetPool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address_scope_id=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">default_prefixlen=None</em>, <em class="sig-param">default_quota=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">is_default=None</em>, <em class="sig-param">max_prefixlen=None</em>, <em class="sig-param">min_prefixlen=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">prefixes=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">revision_number=None</em>, <em class="sig-param">shared=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">updated_at=None</em>, <em class="sig-param">value_specs=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SubnetPool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_scope_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Neutron address scope to assign to the
subnetpool. Changing this updates the address scope id of the existing
subnetpool.</p></li>
<li><p><strong>all_tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The collection of tags assigned on the subnetpool, which have been
explicitly and implicitly added.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time at which subnetpool was created.</p></li>
<li><p><strong>default_prefixlen</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the prefix to allocate when the cidr
or prefixlen attributes are omitted when you create the subnet. Defaults to the
MinPrefixLen. Changing this updates the default prefixlen of the existing
subnetpool.</p></li>
<li><p><strong>default_quota</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The per-project quota on the prefix space that can be
allocated from the subnetpool for project subnets. Changing this updates the
default quota of the existing subnetpool.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable description for the subnetpool.
Changing this updates the description of the existing subnetpool.</p></li>
<li><p><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The IP protocol version.</p></li>
<li><p><strong>is_default</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the subnetpool is default
subnetpool or not. Changing this updates the default status of the existing
subnetpool.</p></li>
<li><p><strong>max_prefixlen</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum prefix size that can be allocated from
the subnetpool. For IPv4 subnetpools, default is 32. For IPv6 subnetpools,
default is 128. Changing this updates the max prefixlen of the existing
subnetpool.</p></li>
<li><p><strong>min_prefixlen</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The smallest prefix that can be allocated from a
subnetpool. For IPv4 subnetpools, default is 8. For IPv6 subnetpools, default
is 64. Changing this updates the min prefixlen of the existing subnetpool.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnetpool. Changing this updates the name of
the existing subnetpool.</p></li>
<li><p><strong>prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of subnet prefixes to assign to the subnetpool.
Neutron API merges adjacent prefixes and treats them as a single prefix. Each
subnet prefix must be unique among all subnet prefixes in all subnetpools that
are associated with the address scope. Changing this updates the prefixes list
of the existing subnetpool.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the subnetpool. Required if admin wants to
create a subnetpool for another project. Changing this creates a new subnetpool.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron subnetpool. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
subnetpool.</p></li>
<li><p><strong>revision_number</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The revision number of the subnetpool.</p></li>
<li><p><strong>shared</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether this subnetpool is shared across
all projects. Changing this updates the shared status of the existing
subnetpool.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the subnetpool.</p></li>
<li><p><strong>updated_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time at which subnetpool was created.</p></li>
<li><p><strong>value_specs</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of additional options.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.SubnetPool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.SubnetPool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SubnetPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.SubnetRoute">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">SubnetRoute</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">destination_cidr=None</em>, <em class="sig-param">next_hop=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SubnetRoute" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a routing entry on a OpenStack V2 subnet.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CIDR block to match on the packet’s destination IP. Changing
this creates a new routing entry.</p></li>
<li><p><strong>next_hop</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address of the next hop gateway.  Changing
this creates a new routing entry.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a subnet. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
routing entry.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the subnet this routing entry belongs to. Changing
this creates a new routing entry.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetRoute.destination_cidr">
<code class="sig-name descname">destination_cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetRoute.destination_cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR block to match on the packet’s destination IP. Changing
this creates a new routing entry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetRoute.next_hop">
<code class="sig-name descname">next_hop</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetRoute.next_hop" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address of the next hop gateway.  Changing
this creates a new routing entry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetRoute.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetRoute.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a subnet. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
routing entry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.SubnetRoute.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.SubnetRoute.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the subnet this routing entry belongs to. Changing
this creates a new routing entry.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.SubnetRoute.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">destination_cidr=None</em>, <em class="sig-param">next_hop=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">subnet_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SubnetRoute.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SubnetRoute resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>destination_cidr</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CIDR block to match on the packet’s destination IP. Changing
this creates a new routing entry.</p></li>
<li><p><strong>next_hop</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address of the next hop gateway.  Changing
this creates a new routing entry.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to configure a routing entry on a subnet. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
routing entry.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the subnet this routing entry belongs to. Changing
this creates a new routing entry.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.SubnetRoute.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SubnetRoute.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.SubnetRoute.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.SubnetRoute.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.Trunk">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">Trunk</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_state_up=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">sub_ports=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Trunk" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a networking V2 trunk resource within OpenStack.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Administrative up/down status for the trunk
(must be “true” or “false” if provided). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing trunk.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the trunk. Changing this
updates the name of the existing trunk.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the trunk. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing trunk.</p></li>
<li><p><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the port to be made a subport of the trunk.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to create a trunk. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
trunk.</p></li>
<li><p><strong>sub_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The set of ports that will be made subports of the trunk.
The structure of each subport is described below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the port.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the Trunk. Required if admin wants
to create a trunk on behalf of another tenant. Changing this creates a new trunk.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>sub_ports</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the port to be made a subport of the trunk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">segmentation_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The numeric id of the subport segment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">segmentationType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The segmentation technology to use, e.g., “vlan”.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_openstack.networking.Trunk.admin_state_up">
<code class="sig-name descname">admin_state_up</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Trunk.admin_state_up" title="Permalink to this definition">¶</a></dt>
<dd><p>Administrative up/down status for the trunk
(must be “true” or “false” if provided). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing trunk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Trunk.all_tags">
<code class="sig-name descname">all_tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Trunk.all_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of tags assigned on the trunk, which have been
explicitly and implicitly added.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Trunk.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Trunk.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description of the trunk. Changing this
updates the name of the existing trunk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Trunk.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Trunk.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the trunk. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing trunk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Trunk.port_id">
<code class="sig-name descname">port_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Trunk.port_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the port to be made a subport of the trunk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Trunk.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Trunk.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which to obtain the V2 networking client.
A networking client is needed to create a trunk. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
trunk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Trunk.sub_ports">
<code class="sig-name descname">sub_ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Trunk.sub_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of ports that will be made subports of the trunk.
The structure of each subport is described below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the port to be made a subport of the trunk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">segmentation_id</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The numeric id of the subport segment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">segmentationType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The segmentation technology to use, e.g., “vlan”.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Trunk.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Trunk.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of string tags for the port.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_openstack.networking.Trunk.tenant_id">
<code class="sig-name descname">tenant_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_openstack.networking.Trunk.tenant_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner of the Trunk. Required if admin wants
to create a trunk on behalf of another tenant. Changing this creates a new trunk.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.Trunk.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_state_up=None</em>, <em class="sig-param">all_tags=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">sub_ports=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Trunk.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Trunk resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_state_up</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Administrative up/down status for the trunk
(must be “true” or “false” if provided). Changing this updates the
<code class="docutils literal notranslate"><span class="pre">admin_state_up</span></code> of an existing trunk.</p></li>
<li><p><strong>all_tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The collection of tags assigned on the trunk, which have been
explicitly and implicitly added.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the trunk. Changing this
updates the name of the existing trunk.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the trunk. Changing this
updates the <code class="docutils literal notranslate"><span class="pre">name</span></code> of an existing trunk.</p></li>
<li><p><strong>port_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the port to be made a subport of the trunk.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which to obtain the V2 networking client.
A networking client is needed to create a trunk. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used. Changing this creates a new
trunk.</p></li>
<li><p><strong>sub_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The set of ports that will be made subports of the trunk.
The structure of each subport is described below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of string tags for the port.</p></li>
<li><p><strong>tenant_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner of the Trunk. Required if admin wants
to create a trunk on behalf of another tenant. Changing this creates a new trunk.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>sub_ports</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the port to be made a subport of the trunk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">segmentation_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The numeric id of the subport segment.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">segmentationType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The segmentation technology to use, e.g., “vlan”.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_openstack.networking.Trunk.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Trunk.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_openstack.networking.Trunk.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.Trunk.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_openstack.networking.get_address_scope">
<code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">get_address_scope</code><span class="sig-paren">(</span><em class="sig-param">ip_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">shared=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_address_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack address-scope.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ip_version</strong> (<em>float</em>) – IP version.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name of the address-scope.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The owner of the address-scope.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Neutron client.
A Neutron client is needed to retrieve address-scopes. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>shared</strong> (<em>bool</em>) – Indicates whether this address-scope is shared across
all projects.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_floating_ip">
<code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">get_floating_ip</code><span class="sig-paren">(</span><em class="sig-param">address=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">fixed_ip=None</em>, <em class="sig-param">pool=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_floating_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack floating IP.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>address</strong> (<em>str</em>) – The IP address of the floating IP.</p></li>
<li><p><strong>description</strong> (<em>str</em>) – Human-readable description of the floating IP.</p></li>
<li><p><strong>fixed_ip</strong> (<em>str</em>) – The specific IP address of the internal port which should be associated with the floating IP.</p></li>
<li><p><strong>pool</strong> (<em>str</em>) – The name of the pool from which the floating IP belongs to.</p></li>
<li><p><strong>port_id</strong> (<em>str</em>) – The ID of the port the floating IP is attached.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Neutron client.
A Neutron client is needed to retrieve floating IP ids. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – status of the floating IP (ACTIVE/DOWN).</p></li>
<li><p><strong>tags</strong> (<em>list</em>) – The list of floating IP tags to filter.</p></li>
<li><p><strong>tenant_id</strong> (<em>str</em>) – The owner of the floating IP.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_network">
<code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">get_network</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">external=None</em>, <em class="sig-param">matching_subnet_cidr=None</em>, <em class="sig-param">mtu=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">transparent_vlan=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_network" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack network.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>str</em>) – Human-readable description of the network.</p></li>
<li><p><strong>external</strong> (<em>bool</em>) – The external routing facility of the network.</p></li>
<li><p><strong>matching_subnet_cidr</strong> (<em>str</em>) – The CIDR of a subnet within the network.</p></li>
<li><p><strong>mtu</strong> (<em>float</em>) – The network MTU to filter. Available, when Neutron <code class="docutils literal notranslate"><span class="pre">net-mtu</span></code>
extension is enabled.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the network.</p></li>
<li><p><strong>network_id</strong> (<em>str</em>) – The ID of the network.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Neutron client.
A Neutron client is needed to retrieve networks ids. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – The status of the network.</p></li>
<li><p><strong>tags</strong> (<em>list</em>) – The list of network tags to filter.</p></li>
<li><p><strong>tenant_id</strong> (<em>str</em>) – The owner of the network.</p></li>
<li><p><strong>transparent_vlan</strong> (<em>bool</em>) – The VLAN transparent attribute for the
network.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_port">
<code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">get_port</code><span class="sig-paren">(</span><em class="sig-param">admin_state_up=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">device_id=None</em>, <em class="sig-param">device_owner=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">fixed_ip=None</em>, <em class="sig-param">mac_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_id=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack port.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>admin_state_up</strong> (<em>bool</em>) – The administrative state of the port.</p></li>
<li><p><strong>description</strong> (<em>str</em>) – Human-readable description of the port.</p></li>
<li><p><strong>device_id</strong> (<em>str</em>) – The ID of the device the port belongs to.</p></li>
<li><p><strong>device_owner</strong> (<em>str</em>) – The device owner of the port.</p></li>
<li><p><strong>dns_name</strong> (<em>str</em>) – The port DNS name to filter. Available, when Neutron
DNS extension is enabled.</p></li>
<li><p><strong>fixed_ip</strong> (<em>str</em>) – The port IP address filter.</p></li>
<li><p><strong>mac_address</strong> (<em>str</em>) – The MAC address of the port.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the port.</p></li>
<li><p><strong>network_id</strong> (<em>str</em>) – The ID of the network the port belongs to.</p></li>
<li><p><strong>port_id</strong> (<em>str</em>) – The ID of the port.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The owner of the port.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Neutron client.
A Neutron client is needed to retrieve port ids. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>security_group_ids</strong> (<em>list</em>) – The list of port security group IDs to filter.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – The status of the port.</p></li>
<li><p><strong>tags</strong> (<em>list</em>) – The list of port tags to filter.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_port_ids">
<code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">get_port_ids</code><span class="sig-paren">(</span><em class="sig-param">admin_state_up=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">device_id=None</em>, <em class="sig-param">device_owner=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">fixed_ip=None</em>, <em class="sig-param">mac_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">security_group_ids=None</em>, <em class="sig-param">sort_direction=None</em>, <em class="sig-param">sort_key=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_port_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get a list of Openstack Port IDs matching the
specified criteria.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>admin_state_up</strong> (<em>bool</em>) – The administrative state of the port.</p></li>
<li><p><strong>description</strong> (<em>str</em>) – Human-readable description of the port.</p></li>
<li><p><strong>device_id</strong> (<em>str</em>) – The ID of the device the port belongs to.</p></li>
<li><p><strong>device_owner</strong> (<em>str</em>) – The device owner of the port.</p></li>
<li><p><strong>fixed_ip</strong> (<em>str</em>) – The port IP address filter.</p></li>
<li><p><strong>mac_address</strong> (<em>str</em>) – The MAC address of the port.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the port.</p></li>
<li><p><strong>network_id</strong> (<em>str</em>) – The ID of the network the port belongs to.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The owner of the port.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Neutron client.
A Neutron client is needed to retrieve port ids. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>security_group_ids</strong> (<em>list</em>) – The list of port security group IDs to filter.</p></li>
<li><p><strong>sort_direction</strong> (<em>str</em>) – Order the results in either <code class="docutils literal notranslate"><span class="pre">asc</span></code> or <code class="docutils literal notranslate"><span class="pre">desc</span></code>.
Defaults to none.</p></li>
<li><p><strong>sort_key</strong> (<em>str</em>) – Sort ports based on a certain key. Defaults to none.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – The status of the port.</p></li>
<li><p><strong>tags</strong> (<em>list</em>) – The list of port tags to filter.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_qos_bandwidth_limit_rule">
<code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">get_qos_bandwidth_limit_rule</code><span class="sig-paren">(</span><em class="sig-param">max_burst_kbps=None</em>, <em class="sig-param">max_kbps=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_qos_bandwidth_limit_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack QoS bandwidth limit rule.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>max_burst_kbps</strong> (<em>float</em>) – The maximum burst size in kilobits of a QoS bandwidth limit rule.</p></li>
<li><p><strong>max_kbps</strong> (<em>float</em>) – The maximum kilobits per second of a QoS bandwidth limit rule.</p></li>
<li><p><strong>qos_policy_id</strong> (<em>str</em>) – The QoS policy reference.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron QoS bandwidth limit rule. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_qos_dscp_marking_rule">
<code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">get_qos_dscp_marking_rule</code><span class="sig-paren">(</span><em class="sig-param">dscp_mark=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_qos_dscp_marking_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack QoS DSCP marking rule.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dscp_mark</strong> (<em>float</em>) – The value of a DSCP mark.</p></li>
<li><p><strong>qos_policy_id</strong> (<em>str</em>) – The QoS policy reference.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron QoS DSCP marking rule. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_qos_minimum_bandwidth_rule">
<code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">get_qos_minimum_bandwidth_rule</code><span class="sig-paren">(</span><em class="sig-param">direction=None</em>, <em class="sig-param">min_kbps=None</em>, <em class="sig-param">qos_policy_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_qos_minimum_bandwidth_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack QoS minimum bandwidth rule.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>min_kbps</strong> (<em>float</em>) – The value of a minimum kbps bandwidth.</p></li>
<li><p><strong>qos_policy_id</strong> (<em>str</em>) – The QoS policy reference.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to create a Neutron QoS minimum bandwidth rule. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_qos_policy">
<code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">get_qos_policy</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">is_default=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">shared=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_qos_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack QoS policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>str</em>) – The human-readable description for the QoS policy.</p></li>
<li><p><strong>is_default</strong> (<em>bool</em>) – Whether the QoS policy is default policy or not.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the QoS policy.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The owner of the QoS policy.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to retrieve a QoS policy ID. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>shared</strong> (<em>bool</em>) – Whether this QoS policy is shared across all projects.</p></li>
<li><p><strong>tags</strong> (<em>list</em>) – The list of QoS policy tags to filter.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_router">
<code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">get_router</code><span class="sig-paren">(</span><em class="sig-param">admin_state_up=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">distributed=None</em>, <em class="sig-param">enable_snat=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">router_id=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_router" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack router.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>admin_state_up</strong> (<em>bool</em>) – Administrative up/down status for the router (must be “true” or “false” if provided).</p></li>
<li><p><strong>description</strong> (<em>str</em>) – Human-readable description of the router.</p></li>
<li><p><strong>distributed</strong> (<em>bool</em>) – Indicates whether or not to get a distributed router.</p></li>
<li><p><strong>enable_snat</strong> (<em>bool</em>) – The value that points out if the Source NAT is enabled on the router.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the router.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Neutron client.
A Neutron client is needed to retrieve router ids. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>router_id</strong> (<em>str</em>) – The UUID of the router resource.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – The status of the router (ACTIVE/DOWN).</p></li>
<li><p><strong>tags</strong> (<em>list</em>) – The list of router tags to filter.</p></li>
<li><p><strong>tenant_id</strong> (<em>str</em>) – The owner of the router.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_sec_group">
<code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">get_sec_group</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secgroup_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_sec_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack security group.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>str</em>) – Human-readable description the the subnet.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the security group.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Neutron client.
A Neutron client is needed to retrieve security groups ids. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>secgroup_id</strong> (<em>str</em>) – The ID of the security group.</p></li>
<li><p><strong>tags</strong> (<em>list</em>) – The list of security group tags to filter.</p></li>
<li><p><strong>tenant_id</strong> (<em>str</em>) – The owner of the security group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_subnet">
<code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">get_subnet</code><span class="sig-paren">(</span><em class="sig-param">cidr=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">dhcp_disabled=None</em>, <em class="sig-param">dhcp_enabled=None</em>, <em class="sig-param">gateway_ip=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">ipv6_address_mode=None</em>, <em class="sig-param">ipv6_ra_mode=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">subnetpool_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">tenant_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack subnet.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cidr</strong> (<em>str</em>) – The CIDR of the subnet.</p></li>
<li><p><strong>description</strong> (<em>str</em>) – Human-readable description for the subnet.</p></li>
<li><p><strong>dhcp_disabled</strong> (<em>bool</em>) – If the subnet has DHCP disabled.</p></li>
<li><p><strong>dhcp_enabled</strong> (<em>bool</em>) – If the subnet has DHCP enabled.</p></li>
<li><p><strong>gateway_ip</strong> (<em>str</em>) – The IP of the subnet’s gateway.</p></li>
<li><p><strong>ip_version</strong> (<em>float</em>) – The IP version of the subnet (either 4 or 6).</p></li>
<li><p><strong>ipv6_address_mode</strong> (<em>str</em>) – The IPv6 address mode. Valid values are
<code class="docutils literal notranslate"><span class="pre">dhcpv6-stateful</span></code>, <code class="docutils literal notranslate"><span class="pre">dhcpv6-stateless</span></code>, or <code class="docutils literal notranslate"><span class="pre">slaac</span></code>.</p></li>
<li><p><strong>ipv6_ra_mode</strong> (<em>str</em>) – The IPv6 Router Advertisement mode. Valid values
are <code class="docutils literal notranslate"><span class="pre">dhcpv6-stateful</span></code>, <code class="docutils literal notranslate"><span class="pre">dhcpv6-stateless</span></code>, or <code class="docutils literal notranslate"><span class="pre">slaac</span></code>.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the subnet.</p></li>
<li><p><strong>network_id</strong> (<em>str</em>) – The ID of the network the subnet belongs to.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Neutron client.
A Neutron client is needed to retrieve subnet ids. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>subnet_id</strong> (<em>str</em>) – The ID of the subnet.</p></li>
<li><p><strong>subnetpool_id</strong> (<em>str</em>) – The ID of the subnetpool associated with the subnet.</p></li>
<li><p><strong>tags</strong> (<em>list</em>) – The list of subnet tags to filter.</p></li>
<li><p><strong>tenant_id</strong> (<em>str</em>) – The owner of the subnet.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_subnet_pool">
<code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">get_subnet_pool</code><span class="sig-paren">(</span><em class="sig-param">address_scope_id=None</em>, <em class="sig-param">default_prefixlen=None</em>, <em class="sig-param">default_quota=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">is_default=None</em>, <em class="sig-param">max_prefixlen=None</em>, <em class="sig-param">min_prefixlen=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">shared=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_subnet_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack subnetpool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>address_scope_id</strong> (<em>str</em>) – The Neutron address scope that subnetpools
is assigned to.</p></li>
<li><p><strong>default_prefixlen</strong> (<em>float</em>) – The size of the subnetpool default prefix
length.</p></li>
<li><p><strong>default_quota</strong> (<em>float</em>) – The per-project quota on the prefix space that
can be allocated from the subnetpool for project subnets.</p></li>
<li><p><strong>description</strong> (<em>str</em>) – The human-readable description for the subnetpool.</p></li>
<li><p><strong>ip_version</strong> (<em>float</em>) – The IP protocol version.</p></li>
<li><p><strong>is_default</strong> (<em>bool</em>) – Whether the subnetpool is default subnetpool or not.</p></li>
<li><p><strong>max_prefixlen</strong> (<em>float</em>) – The size of the subnetpool max prefix length.</p></li>
<li><p><strong>min_prefixlen</strong> (<em>float</em>) – The size of the subnetpool min prefix length.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the subnetpool.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The owner of the subnetpool.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Networking client.
A Networking client is needed to retrieve a subnetpool id. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>shared</strong> (<em>bool</em>) – Whether this subnetpool is shared across all projects.</p></li>
<li><p><strong>tags</strong> (<em>list</em>) – The list of subnetpool tags to filter.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_openstack.networking.get_trunk">
<code class="sig-prename descclassname">pulumi_openstack.networking.</code><code class="sig-name descname">get_trunk</code><span class="sig-paren">(</span><em class="sig-param">admin_state_up=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">port_id=None</em>, <em class="sig-param">project_id=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">trunk_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_openstack.networking.get_trunk" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ID of an available OpenStack trunk.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>admin_state_up</strong> (<em>bool</em>) – The administrative state of the trunk.</p></li>
<li><p><strong>description</strong> (<em>str</em>) – Human-readable description of the trunk.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the trunk.</p></li>
<li><p><strong>port_id</strong> (<em>str</em>) – The ID of the trunk parent port.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The owner of the trunk.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which to obtain the V2 Neutron client.
A Neutron client is needed to retrieve trunk ids. If omitted, the
<code class="docutils literal notranslate"><span class="pre">region</span></code> argument of the provider is used.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – The status of the trunk.</p></li>
<li><p><strong>tags</strong> (<em>list</em>) – The list of trunk tags to filter.</p></li>
<li><p><strong>trunk_id</strong> (<em>str</em>) – The ID of the trunk.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
