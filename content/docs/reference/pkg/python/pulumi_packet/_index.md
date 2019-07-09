---
---

<div class="section" id="pulumi-packet">
<h1>Pulumi Packet<a class="headerlink" href="#pulumi-packet" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-packet/issues">pulumi/pulumi-packet repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/issues">terraform-providers/terraform-provider-packet repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_packet"></span><dl class="class">
<dt id="pulumi_packet.BgpSession">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">BgpSession</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>address_family=None</em>, <em>default_route=None</em>, <em>device_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.BgpSession" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage BGP sessions in Packet Host. Refer to <a class="reference external" href="https://support.packet.com/kb/articles/bgp">Packet BGP documentation</a> for more details.</p>
<p>You need to have BGP config enabled in your project.</p>
<p>BGP session must be linked to a device running <a class="reference external" href="https://bird.network.cz">BIRD</a> or other BGP routing daemon which will control route advertisements via the session to Packet’s upstream routers.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code></li>
<li><strong>default_route</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to set the default route policy. False by default.</li>
<li><strong>device_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of device</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/bgp_session.html.markdown">https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/bgp_session.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_packet.BgpSession.address_family">
<code class="descname">address_family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.BgpSession.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.BgpSession.default_route">
<code class="descname">default_route</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.BgpSession.default_route" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to set the default route policy. False by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.BgpSession.device_id">
<code class="descname">device_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.BgpSession.device_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of device</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_packet.BgpSession.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.BgpSession.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.BgpSession.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.BgpSession.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Connect">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">Connect</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>facility=None</em>, <em>name=None</em>, <em>port_speed=None</em>, <em>project_id=None</em>, <em>provider_id=None</em>, <em>provider_payload=None</em>, <em>vxlan=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Connect" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource for <a class="reference external" href="https://www.packet.com/cloud/all-features/packet-connect/">Packet Connect</a>, a link between Packet VLANs and VLANs in other cloud providers.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>facility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Facility where to create the VLAN</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name for the Connect resource</li>
<li><strong>port_speed</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Port speed in Mbps</li>
<li><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of parent project</li>
<li><strong>provider_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of Connect Provider. Provider IDs are</li>
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
<li><strong>provider_payload</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Authorization key for the Connect provider</li>
<li><strong>vxlan</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – VXLAN Network identifier of the linked Packet VLAN</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/connect.html.markdown">https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/connect.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_packet.Connect.facility">
<code class="descname">facility</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Connect.facility" title="Permalink to this definition">¶</a></dt>
<dd><p>Facility where to create the VLAN</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Connect.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Connect.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name for the Connect resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Connect.port_speed">
<code class="descname">port_speed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Connect.port_speed" title="Permalink to this definition">¶</a></dt>
<dd><p>Port speed in Mbps</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Connect.project_id">
<code class="descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Connect.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of parent project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Connect.provider_id">
<code class="descname">provider_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Connect.provider_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of Connect Provider. Provider IDs are</p>
<ul class="simple">
<li>Azure ExpressRoute - “ed5de8e0-77a9-4d3b-9de0-65281d3aa831”</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Connect.provider_payload">
<code class="descname">provider_payload</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Connect.provider_payload" title="Permalink to this definition">¶</a></dt>
<dd><p>Authorization key for the Connect provider</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Connect.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Connect.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the Connect resource, one of PROVISIONING, PROVISIONED, DEPROVISIONING, DEPROVISIONED</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Connect.vxlan">
<code class="descname">vxlan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Connect.vxlan" title="Permalink to this definition">¶</a></dt>
<dd><p>VXLAN Network identifier of the linked Packet VLAN</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_packet.Connect.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Connect.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Connect.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Connect.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Device">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">Device</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>always_pxe=None</em>, <em>billing_cycle=None</em>, <em>description=None</em>, <em>facilities=None</em>, <em>hardware_reservation_id=None</em>, <em>hostname=None</em>, <em>ip_address_types=None</em>, <em>ipxe_script_url=None</em>, <em>network_type=None</em>, <em>operating_system=None</em>, <em>plan=None</em>, <em>project_id=None</em>, <em>project_ssh_key_ids=None</em>, <em>public_ipv4_subnet_size=None</em>, <em>storage=None</em>, <em>tags=None</em>, <em>user_data=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Device" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet device resource. This can be used to create,
modify, and delete devices.</p>
<blockquote>
<div><dl class="docutils">
<dt><strong>Note:</strong> All arguments including the <code class="docutils literal notranslate"><span class="pre">root_password</span></code> and <code class="docutils literal notranslate"><span class="pre">user_data</span></code> will be stored in</dt>
<dd>the raw state as plain-text.</dd>
</dl>
<p><a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>always_pxe</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, a device with OS <code class="docutils literal notranslate"><span class="pre">custom_ipxe</span></code> will
continue to boot via iPXE on reboots.</li>
<li><strong>billing_cycle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – monthly or hourly</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description string for the device</li>
<li><strong>facilities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of facility codes with deployment preferences. Packet API will go through the list and will deploy your device to first facility with free capacity. List items must be facility codes or <code class="docutils literal notranslate"><span class="pre">any</span></code> (a wildcard). To find the facility code, visit <a class="reference external" href="https://www.packet.com/developers/api/#facilities">Facilities API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</li>
<li><strong>hardware_reservation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of hardware reservation where you want this device deployed, or <code class="docutils literal notranslate"><span class="pre">next-available</span></code> if you want to pick your next available reservation automatically.</li>
<li><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The device name</li>
<li><strong>ip_address_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set containing one or more of [<code class="docutils literal notranslate"><span class="pre">private_ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">public_ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">public_ipv6</span></code>]. It specifies which IP address types a new device should obtain. If omitted, a created device will obtain all 3 addresses. If you only want private IPv4 address for the new device, pass [<code class="docutils literal notranslate"><span class="pre">private_ipv4</span></code>].</li>
<li><strong>ipxe_script_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL pointing to a hosted iPXE script. More
information is in the
<a class="reference external" href="https://support.packet.com/kb/articles/custom-ipxe">Custom iPXE</a>
doc.</li>
<li><strong>operating_system</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operating system slug. To find the slug, or visit <a class="reference external" href="https://www.packet.com/developers/api/#operatingsystems">Operating Systems API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</li>
<li><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The device plan slug. To find the plan slug, visit <a class="reference external" href="https://www.packet.com/developers/api/#plans">Device plans API docs</a>, set your auth token in the top of the page and see JSON from the API response.</li>
<li><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project in which to create the device</li>
<li><strong>project_ssh_key_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Array of IDs of the project SSH keys which should be added to the device. If you omit this, SSH keys of all the members of the parent project will be added to the device. If you specify this array, only the listed project SSH keys will be added. Project SSH keys can be created with the [packet_project_ssh_key][packet_project_ssh_key.html] resource.</li>
<li><strong>public_ipv4_subnet_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size of allocated subnet, more
information is in the
<a class="reference external" href="https://support.packet.com/kb/articles/custom-subnet-size">Custom Subnet Size</a> doc.</li>
<li><strong>storage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON for custom partitioning. Only usable on reserved hardware. More information in in the <a class="reference external" href="https://support.packet.com/kb/articles/custom-partitioning-raid">Custom Partitioning and RAID</a> doc.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Tags attached to the device</li>
<li><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string of the desired User Data for the device.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/device.html.markdown">https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/device.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_packet.Device.access_private_ipv4">
<code class="descname">access_private_ipv4</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.access_private_ipv4" title="Permalink to this definition">¶</a></dt>
<dd><p>The ipv4 private IP assigned to the device</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.access_public_ipv4">
<code class="descname">access_public_ipv4</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.access_public_ipv4" title="Permalink to this definition">¶</a></dt>
<dd><p>The ipv4 maintenance IP assigned to the device</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.access_public_ipv6">
<code class="descname">access_public_ipv6</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.access_public_ipv6" title="Permalink to this definition">¶</a></dt>
<dd><p>The ipv6 maintenance IP assigned to the device</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.always_pxe">
<code class="descname">always_pxe</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.always_pxe" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, a device with OS <code class="docutils literal notranslate"><span class="pre">custom_ipxe</span></code> will
continue to boot via iPXE on reboots.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.billing_cycle">
<code class="descname">billing_cycle</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.billing_cycle" title="Permalink to this definition">¶</a></dt>
<dd><p>monthly or hourly</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.created">
<code class="descname">created</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the device was created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.deployed_facility">
<code class="descname">deployed_facility</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.deployed_facility" title="Permalink to this definition">¶</a></dt>
<dd><p>The facility where the device is deployed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description string for the device</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.facilities">
<code class="descname">facilities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.facilities" title="Permalink to this definition">¶</a></dt>
<dd><p>List of facility codes with deployment preferences. Packet API will go through the list and will deploy your device to first facility with free capacity. List items must be facility codes or <code class="docutils literal notranslate"><span class="pre">any</span></code> (a wildcard). To find the facility code, visit <a class="reference external" href="https://www.packet.com/developers/api/#facilities">Facilities API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.hardware_reservation_id">
<code class="descname">hardware_reservation_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.hardware_reservation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of hardware reservation where you want this device deployed, or <code class="docutils literal notranslate"><span class="pre">next-available</span></code> if you want to pick your next available reservation automatically.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.hostname">
<code class="descname">hostname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The device name</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.ip_address_types">
<code class="descname">ip_address_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.ip_address_types" title="Permalink to this definition">¶</a></dt>
<dd><p>A set containing one or more of [<code class="docutils literal notranslate"><span class="pre">private_ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">public_ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">public_ipv6</span></code>]. It specifies which IP address types a new device should obtain. If omitted, a created device will obtain all 3 addresses. If you only want private IPv4 address for the new device, pass [<code class="docutils literal notranslate"><span class="pre">private_ipv4</span></code>].</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.ipxe_script_url">
<code class="descname">ipxe_script_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.ipxe_script_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL pointing to a hosted iPXE script. More
information is in the
<a class="reference external" href="https://support.packet.com/kb/articles/custom-ipxe">Custom iPXE</a>
doc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.locked">
<code class="descname">locked</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.locked" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the device is locked</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.networks">
<code class="descname">networks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.networks" title="Permalink to this definition">¶</a></dt>
<dd><p>The device’s private and public IP (v4 and v6) network details. When a device is run without any special network configuration, it will have 3 networks:</p>
<ul class="simple">
<li>Public IPv4 at <code class="docutils literal notranslate"><span class="pre">packet_device.name.network.0</span></code></li>
<li>IPv6 at <code class="docutils literal notranslate"><span class="pre">packet_device.name.network.1</span></code></li>
<li>Private IPv4 at <code class="docutils literal notranslate"><span class="pre">packet_device.name.network.2</span></code>
Elastic addresses then stack by type - an assigned public IPv4 will go after the management public IPv4 (to index 1), and will then shift the indices of the IPv6 and private IPv4. Assigned private IPv4 will go after the management private IPv4 (to the end of the network list).
The fields of the network attributes are:</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.operating_system">
<code class="descname">operating_system</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.operating_system" title="Permalink to this definition">¶</a></dt>
<dd><p>The operating system slug. To find the slug, or visit <a class="reference external" href="https://www.packet.com/developers/api/#operatingsystems">Operating Systems API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.plan">
<code class="descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>The device plan slug. To find the plan slug, visit <a class="reference external" href="https://www.packet.com/developers/api/#plans">Device plans API docs</a>, set your auth token in the top of the page and see JSON from the API response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.ports">
<code class="descname">ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.ports" title="Permalink to this definition">¶</a></dt>
<dd><p>Ports assigned to the device</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.project_id">
<code class="descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the project in which to create the device</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.project_ssh_key_ids">
<code class="descname">project_ssh_key_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.project_ssh_key_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of IDs of the project SSH keys which should be added to the device. If you omit this, SSH keys of all the members of the parent project will be added to the device. If you specify this array, only the listed project SSH keys will be added. Project SSH keys can be created with the [packet_project_ssh_key][packet_project_ssh_key.html] resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.public_ipv4_subnet_size">
<code class="descname">public_ipv4_subnet_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.public_ipv4_subnet_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size of allocated subnet, more
information is in the
<a class="reference external" href="https://support.packet.com/kb/articles/custom-subnet-size">Custom Subnet Size</a> doc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.root_password">
<code class="descname">root_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.root_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Root password to the server (disabled after 24 hours)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.ssh_key_ids">
<code class="descname">ssh_key_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.ssh_key_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IDs of SSH keys deployed in the device, can be both user and project SSH keys</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the device</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.storage">
<code class="descname">storage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.storage" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON for custom partitioning. Only usable on reserved hardware. More information in in the <a class="reference external" href="https://support.packet.com/kb/articles/custom-partitioning-raid">Custom Partitioning and RAID</a> doc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tags attached to the device</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.updated">
<code class="descname">updated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the device was updated</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.user_data">
<code class="descname">user_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>A string of the desired User Data for the device.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_packet.Device.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Device.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Device.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Device.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.GetOperatingSystemResult">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">GetOperatingSystemResult</code><span class="sig-paren">(</span><em>distro=None</em>, <em>name=None</em>, <em>provisionable_on=None</em>, <em>slug=None</em>, <em>version=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetOperatingSystemResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getOperatingSystem.</p>
<dl class="attribute">
<dt id="pulumi_packet.GetOperatingSystemResult.slug">
<code class="descname">slug</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetOperatingSystemResult.slug" title="Permalink to this definition">¶</a></dt>
<dd><p>Operating system slug (same as <code class="docutils literal notranslate"><span class="pre">id</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.GetOperatingSystemResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetOperatingSystemResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_packet.GetPrecreatedIpBlockResult">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">GetPrecreatedIpBlockResult</code><span class="sig-paren">(</span><em>address=None</em>, <em>address_family=None</em>, <em>cidr=None</em>, <em>cidr_notation=None</em>, <em>facility=None</em>, <em>gateway=None</em>, <em>global_=None</em>, <em>manageable=None</em>, <em>management=None</em>, <em>netmask=None</em>, <em>network=None</em>, <em>project_id=None</em>, <em>public=None</em>, <em>quantity=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetPrecreatedIpBlockResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPrecreatedIpBlock.</p>
<dl class="attribute">
<dt id="pulumi_packet.GetPrecreatedIpBlockResult.cidr_notation">
<code class="descname">cidr_notation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetPrecreatedIpBlockResult.cidr_notation" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR notation of the looked up block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.GetPrecreatedIpBlockResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetPrecreatedIpBlockResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_packet.GetSpotMarketPriceResult">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">GetSpotMarketPriceResult</code><span class="sig-paren">(</span><em>facility=None</em>, <em>plan=None</em>, <em>price=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetSpotMarketPriceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSpotMarketPrice.</p>
<dl class="attribute">
<dt id="pulumi_packet.GetSpotMarketPriceResult.price">
<code class="descname">price</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetSpotMarketPriceResult.price" title="Permalink to this definition">¶</a></dt>
<dd><p>Current spot market price for given plan in given facility.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.GetSpotMarketPriceResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetSpotMarketPriceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_packet.IpAttachment">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">IpAttachment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cidr_notation=None</em>, <em>device_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.IpAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to attach elastic IP subnets to devices.</p>
<p>To attach an IP subnet from a reserved block to a provisioned device, you must derive a subnet CIDR belonging to
one of your reserved blocks in the same project and facility as the target device.</p>
<p>For example, you have reserved IPv4 address block 147.229.10.152/30, you can choose to assign either the whole
block as one subnet to a device; or 2 subnets with CIDRs 147.229.10.152/31’ and 147.229.10.154/31; or 4 subnets
with mask prefix length 32. More about the elastic IP subnets is <a class="reference external" href="https://support.packet.com/kb/articles/elastic-ips">here</a>.</p>
<p>Device and reserved block must be in the same facility.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cidr_notation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CIDR notation of subnet from block reserved in the same
project and facility as the device</li>
<li><strong>device_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of device to which to assign the subnet</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/ip_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/ip_attachment.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_packet.IpAttachment.address_family">
<code class="descname">address_family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.IpAttachment.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p>Address family as integer (4 or 6)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.IpAttachment.cidr">
<code class="descname">cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.IpAttachment.cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>length of CIDR prefix of the subnet as integer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.IpAttachment.cidr_notation">
<code class="descname">cidr_notation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.IpAttachment.cidr_notation" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR notation of subnet from block reserved in the same
project and facility as the device</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.IpAttachment.device_id">
<code class="descname">device_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.IpAttachment.device_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of device to which to assign the subnet</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.IpAttachment.gateway">
<code class="descname">gateway</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.IpAttachment.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address of gateway for the subnet</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.IpAttachment.netmask">
<code class="descname">netmask</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.IpAttachment.netmask" title="Permalink to this definition">¶</a></dt>
<dd><p>Subnet mask in decimal notation, e.g. “255.255.255.0”</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.IpAttachment.network">
<code class="descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.IpAttachment.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Subnet network address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.IpAttachment.public">
<code class="descname">public</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.IpAttachment.public" title="Permalink to this definition">¶</a></dt>
<dd><p>boolean flag whether subnet is reachable from the Internet</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_packet.IpAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.IpAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.IpAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.IpAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Organization">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">Organization</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>logo=None</em>, <em>name=None</em>, <em>twitter=None</em>, <em>website=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Organization" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage organization resource in Packet.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description string.</li>
<li><strong>logo</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Logo URL.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Organization.</li>
<li><strong>twitter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Twitter handle.</li>
<li><strong>website</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Website link.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/organization.html.markdown">https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/organization.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_packet.Organization.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Organization.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Organization.logo">
<code class="descname">logo</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Organization.logo" title="Permalink to this definition">¶</a></dt>
<dd><p>Logo URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Organization.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Organization.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Organization.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Organization.twitter">
<code class="descname">twitter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Organization.twitter" title="Permalink to this definition">¶</a></dt>
<dd><p>Twitter handle.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Organization.website">
<code class="descname">website</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Organization.website" title="Permalink to this definition">¶</a></dt>
<dd><p>Website link.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_packet.Organization.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Organization.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Organization.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Organization.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.PortVlanAttachment">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">PortVlanAttachment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>device_id=None</em>, <em>force_bond=None</em>, <em>native=None</em>, <em>port_name=None</em>, <em>vlan_vnid=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.PortVlanAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to attach device ports to VLANs.</p>
<p>Device and VLAN must be in the same facility.</p>
<p>If you need this resource to add the port back to bond on removal, set <code class="docutils literal notranslate"><span class="pre">force_bond</span> <span class="pre">=</span> <span class="pre">true</span></code>.</p>
<p>To learn more about Layer 2 networking in Packet, refer to</p>
<ul class="simple">
<li><a class="reference external" href="https://support.packet.com/kb/articles/layer-2-configurations">https://support.packet.com/kb/articles/layer-2-configurations</a></li>
<li><a class="reference external" href="https://support.packet.com/kb/articles/layer-2-overview">https://support.packet.com/kb/articles/layer-2-overview</a></li>
</ul>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">id</span></code> - UUID of device port used in the assignment</li>
<li><code class="docutils literal notranslate"><span class="pre">vlan_id</span></code> - UUID of VLAN API resource</li>
<li><code class="docutils literal notranslate"><span class="pre">port_id</span></code> - UUID of device port</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>device_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of device to be assigned to the VLAN</li>
<li><strong>force_bond</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Add port back to the bond when this resource is removed. Default is false.</li>
<li><strong>native</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Mark this VLAN a native VLAN on the port. This can be used only if this assignment assigns second or further VLAN to the port. To ensure that this attachment is not first on a port, you can use <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> pointing to another packet_port_vlan_attachment, just like in the layer2-individual example above.</li>
<li><strong>port_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of network port to be assigned to the VLAN</li>
<li><strong>vlan_vnid</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – VXLAN Network Identifier, integer</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/port_vlan_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/port_vlan_attachment.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_packet.PortVlanAttachment.device_id">
<code class="descname">device_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.device_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of device to be assigned to the VLAN</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.PortVlanAttachment.force_bond">
<code class="descname">force_bond</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.force_bond" title="Permalink to this definition">¶</a></dt>
<dd><p>Add port back to the bond when this resource is removed. Default is false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.PortVlanAttachment.native">
<code class="descname">native</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.native" title="Permalink to this definition">¶</a></dt>
<dd><p>Mark this VLAN a native VLAN on the port. This can be used only if this assignment assigns second or further VLAN to the port. To ensure that this attachment is not first on a port, you can use <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> pointing to another packet_port_vlan_attachment, just like in the layer2-individual example above.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.PortVlanAttachment.port_name">
<code class="descname">port_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.port_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of network port to be assigned to the VLAN</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.PortVlanAttachment.vlan_vnid">
<code class="descname">vlan_vnid</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.vlan_vnid" title="Permalink to this definition">¶</a></dt>
<dd><p>VXLAN Network Identifier, integer</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_packet.PortVlanAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.PortVlanAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Project">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">Project</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>backend_transfer=None</em>, <em>bgp_config=None</em>, <em>name=None</em>, <em>organization_id=None</em>, <em>payment_method_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet project resource to allow you manage devices
in your projects.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>backend_transfer</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable <a class="reference external" href="https://support.packet.com/kb/articles/backend-transfer">Backend Transfer</a>, default is false</li>
<li><strong>bgp_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Optional BGP settings. Refer to <a class="reference external" href="https://support.packet.com/kb/articles/bgp">Packet guide for BGP</a>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project</li>
<li><strong>organization_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of organization under which you want to create the project. If you leave it out, the project will be create under your the default organization of your account.</li>
<li><strong>payment_method_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of payment method for this project. The payment method and the project need to belong to the same organization (passed with <code class="docutils literal notranslate"><span class="pre">organization_id</span></code>, or default).</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/project.html.markdown">https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/project.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_packet.Project.backend_transfer">
<code class="descname">backend_transfer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.backend_transfer" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable <a class="reference external" href="https://support.packet.com/kb/articles/backend-transfer">Backend Transfer</a>, default is false</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Project.bgp_config">
<code class="descname">bgp_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.bgp_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional BGP settings. Refer to <a class="reference external" href="https://support.packet.com/kb/articles/bgp">Packet guide for BGP</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Project.created">
<code class="descname">created</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the project was created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Project.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Project.organization_id">
<code class="descname">organization_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.organization_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of organization under which you want to create the project. If you leave it out, the project will be create under your the default organization of your account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Project.payment_method_id">
<code class="descname">payment_method_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.payment_method_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of payment method for this project. The payment method and the project need to belong to the same organization (passed with <code class="docutils literal notranslate"><span class="pre">organization_id</span></code>, or default).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Project.updated">
<code class="descname">updated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the project was updated</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_packet.Project.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Project.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.ProjectSshKey">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">ProjectSshKey</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>project_id=None</em>, <em>public_key=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.ProjectSshKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet project SSH key resource to manage project-specific SSH keys. On contrary to user SSH keys, project SSH keys are used to exclusively populate <code class="docutils literal notranslate"><span class="pre">authorized_keys</span></code> in new devices.</p>
<p>If you supply a list of project SSH keys when creating a new device, only the listed keys are used; user SSH keys are ignored.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SSH key for identification</li>
<li><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of parent project</li>
<li><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key. If this is a file, it can be read using the file interpolation function</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/project_ssh_key.html.markdown">https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/project_ssh_key.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_packet.ProjectSshKey.created">
<code class="descname">created</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ProjectSshKey.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the SSH key was created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.ProjectSshKey.fingerprint">
<code class="descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ProjectSshKey.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the SSH key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.ProjectSshKey.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ProjectSshKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SSH key for identification</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.ProjectSshKey.project_id">
<code class="descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ProjectSshKey.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of parent project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.ProjectSshKey.public_key">
<code class="descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ProjectSshKey.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key. If this is a file, it can be read using the file interpolation function</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.ProjectSshKey.updated">
<code class="descname">updated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ProjectSshKey.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the SSH key was updated</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_packet.ProjectSshKey.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.ProjectSshKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.ProjectSshKey.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.ProjectSshKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Provider">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">Provider</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>auth_token=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the packet package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://pulumi.io/reference/programming-model.html#providers">documentation</a> for more information.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/index.html.markdown">https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/index.html.markdown</a>.</div></blockquote>
<dl class="method">
<dt id="pulumi_packet.Provider.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Provider.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.ReservedIpBlock">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">ReservedIpBlock</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>facility=None</em>, <em>project_id=None</em>, <em>quantity=None</em>, <em>type=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.ReservedIpBlock" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create and manage blocks of reserved IP addresses in a project.</p>
<p>When a user provisions first device in a facility, Packet API automatically allocates IPv6/56 and private IPv4/25 blocks.
The new device then gets IPv6 and private IPv4 addresses from those block. It also gets a public IPv4/31 address.
Every new device in the project and facility will automatically get IPv6 and private IPv4 addresses from these pre-allocated blocks.
The IPv6 and private IPv4 blocks can’t be created, only imported. With this resource, it’s possible to create either public IPv4 blocks or global IPv4 blocks.</p>
<p>Public blocks are allocated in a facility. Addresses from public blocks can only be assigned to devices in the facility. Public blocks can have mask from /24 (256 addresses) to /32 (1 address). If you create public block with this resource, you must fill the facility argmument.</p>
<p>Addresses from global blocks can be assigned in any facility. Global blocks can have mask from /30 (4 addresses), to /32 (1 address). If you create global block with this resource, you must specify type = “global_ipv4” and you must omit the facility argument.</p>
<p>Once IP block is allocated or imported, an address from it can be assigned to device with the <code class="docutils literal notranslate"><span class="pre">packet_ip_attachment</span></code> resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>facility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Facility where to allocate the public IP address block, makes sense only for type==public_ipv4, must be empty for type==global_ipv4</li>
<li><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The packet project ID where to allocate the address block</li>
<li><strong>quantity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of allocated /32 addresses, a power of 2</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Either “global_ipv4” or “public_ipv4”, defaults to “public_ipv4” for backward compatibility</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/reserved_ip_block.html.markdown">https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/reserved_ip_block.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_packet.ReservedIpBlock.address_family">
<code class="descname">address_family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p>Address family as integer (4 or 6)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.ReservedIpBlock.cidr">
<code class="descname">cidr</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>length of CIDR prefix of the block as integer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.ReservedIpBlock.cidr_notation">
<code class="descname">cidr_notation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.cidr_notation" title="Permalink to this definition">¶</a></dt>
<dd><p>Address and mask in CIDR notation, e.g. “147.229.15.30/31”</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.ReservedIpBlock.facility">
<code class="descname">facility</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.facility" title="Permalink to this definition">¶</a></dt>
<dd><p>Facility where to allocate the public IP address block, makes sense only for type==public_ipv4, must be empty for type==global_ipv4</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.ReservedIpBlock.global_">
<code class="descname">global_</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.global_" title="Permalink to this definition">¶</a></dt>
<dd><p>boolean flag whether addresses from a block are global (i.e. can be assigned in any facility)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.ReservedIpBlock.netmask">
<code class="descname">netmask</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.netmask" title="Permalink to this definition">¶</a></dt>
<dd><p>Mask in decimal notation, e.g. “255.255.255.0”</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.ReservedIpBlock.network">
<code class="descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Network IP address portion of the block specification</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.ReservedIpBlock.project_id">
<code class="descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The packet project ID where to allocate the address block</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.ReservedIpBlock.public">
<code class="descname">public</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.public" title="Permalink to this definition">¶</a></dt>
<dd><p>boolean flag whether addresses from a block are public</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.ReservedIpBlock.quantity">
<code class="descname">quantity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.quantity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of allocated /32 addresses, a power of 2</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.ReservedIpBlock.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Either “global_ipv4” or “public_ipv4”, defaults to “public_ipv4” for backward compatibility</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_packet.ReservedIpBlock.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.ReservedIpBlock.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.SpotMarketRequest">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">SpotMarketRequest</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>devices_max=None</em>, <em>devices_min=None</em>, <em>facilities=None</em>, <em>instance_parameters=None</em>, <em>max_bid_price=None</em>, <em>project_id=None</em>, <em>wait_for_devices=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SpotMarketRequest" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet Spot Market Request resource to allow you to
manage spot market requests on your account. <a class="reference external" href="https://support.packet.com/kb/articles/spot-market">https://support.packet.com/kb/articles/spot-market</a></p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>devices_max</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum number devices to be created</li>
<li><strong>devices_min</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Miniumum number devices to be created</li>
<li><strong>facilities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Facility IDs where devices should be created</li>
<li><strong>instance_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Device parameters. See device resource for details</li>
<li><strong>max_bid_price</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum price user is willing to pay per hour per device</li>
<li><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project ID</li>
<li><strong>wait_for_devices</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/spot_market_request.html.markdown">https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/spot_market_request.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_packet.SpotMarketRequest.devices_max">
<code class="descname">devices_max</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.devices_max" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum number devices to be created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.SpotMarketRequest.devices_min">
<code class="descname">devices_min</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.devices_min" title="Permalink to this definition">¶</a></dt>
<dd><p>Miniumum number devices to be created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.SpotMarketRequest.facilities">
<code class="descname">facilities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.facilities" title="Permalink to this definition">¶</a></dt>
<dd><p>Facility IDs where devices should be created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.SpotMarketRequest.instance_parameters">
<code class="descname">instance_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.instance_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Device parameters. See device resource for details</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.SpotMarketRequest.max_bid_price">
<code class="descname">max_bid_price</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.max_bid_price" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum price user is willing to pay per hour per device</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.SpotMarketRequest.project_id">
<code class="descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Project ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.SpotMarketRequest.wait_for_devices">
<code class="descname">wait_for_devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.wait_for_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_packet.SpotMarketRequest.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.SpotMarketRequest.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.SshKey">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">SshKey</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>public_key=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SshKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage User SSH keys on your Packet user account. If you create a new device in a project, all the keys of the project’s collaborators will be injected to the device.</p>
<p>The link between User SSH key and device is implicit. If you want to make sure that a key will be copied to a device, you must ensure that the device resource <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> the key resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SSH key for identification</li>
<li><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key. If this is a file, it
can be read using the file interpolation function</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/ssh_key.html.markdown">https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/ssh_key.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_packet.SshKey.created">
<code class="descname">created</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SshKey.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the SSH key was created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.SshKey.fingerprint">
<code class="descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SshKey.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the SSH key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.SshKey.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SshKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SSH key for identification</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.SshKey.public_key">
<code class="descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SshKey.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key. If this is a file, it
can be read using the file interpolation function</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.SshKey.updated">
<code class="descname">updated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SshKey.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the SSH key was updated</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_packet.SshKey.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SshKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.SshKey.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SshKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Vlan">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">Vlan</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>facility=None</em>, <em>project_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Vlan" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to allow users to manage Virtual Networks in their projects.</p>
<p>To learn more about Layer 2 networking in Packet, refer to</p>
<ul class="simple">
<li><a class="reference external" href="https://support.packet.com/kb/articles/layer-2-configurations">https://support.packet.com/kb/articles/layer-2-configurations</a></li>
<li><a class="reference external" href="https://support.packet.com/kb/articles/layer-2-overview">https://support.packet.com/kb/articles/layer-2-overview</a></li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description string</li>
<li><strong>facility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Facility where to create the VLAN</li>
<li><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of parent project</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/vlan.html.markdown">https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/vlan.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_packet.Vlan.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Vlan.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description string</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Vlan.facility">
<code class="descname">facility</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Vlan.facility" title="Permalink to this definition">¶</a></dt>
<dd><p>Facility where to create the VLAN</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Vlan.project_id">
<code class="descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Vlan.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of parent project</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Vlan.vxlan">
<code class="descname">vxlan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Vlan.vxlan" title="Permalink to this definition">¶</a></dt>
<dd><p>VXLAN segment ID</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_packet.Vlan.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Vlan.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Vlan.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Vlan.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Volume">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">Volume</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>billing_cycle=None</em>, <em>description=None</em>, <em>facility=None</em>, <em>locked=None</em>, <em>plan=None</em>, <em>project_id=None</em>, <em>size=None</em>, <em>snapshot_policies=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Volume resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>billing_cycle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing cycle, defaults to “hourly”</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Optional description for the volume</li>
<li><strong>facility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The facility to create the volume in</li>
<li><strong>locked</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Lock or unlock the volume</li>
<li><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service plan slug of the volume</li>
<li><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The packet project ID to deploy the volume in</li>
<li><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size in GB to make the volume</li>
<li><strong>snapshot_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Optional list of snapshot policies</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/volume.html.markdown">https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/volume.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_packet.Volume.attachments">
<code class="descname">attachments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.attachments" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of attachments, each with it’s own <code class="docutils literal notranslate"><span class="pre">href</span></code> attribute</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Volume.billing_cycle">
<code class="descname">billing_cycle</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.billing_cycle" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing cycle, defaults to “hourly”</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Volume.created">
<code class="descname">created</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the volume was created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Volume.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional description for the volume</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Volume.facility">
<code class="descname">facility</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.facility" title="Permalink to this definition">¶</a></dt>
<dd><p>The facility to create the volume in</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Volume.locked">
<code class="descname">locked</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.locked" title="Permalink to this definition">¶</a></dt>
<dd><p>Lock or unlock the volume</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Volume.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the volume</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Volume.plan">
<code class="descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>The service plan slug of the volume</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Volume.project_id">
<code class="descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The packet project ID to deploy the volume in</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Volume.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size in GB to make the volume</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Volume.snapshot_policies">
<code class="descname">snapshot_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.snapshot_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional list of snapshot policies</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Volume.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the volume</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Volume.updated">
<code class="descname">updated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the volume was updated</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_packet.Volume.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Volume.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Volume.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Volume.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.VolumeAttachment">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">VolumeAttachment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>device_id=None</em>, <em>volume_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.VolumeAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a VolumeAttachment resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>device_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the device to which the volume should be attached</li>
<li><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the volume to attach</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/volume_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/volume_attachment.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_packet.VolumeAttachment.device_id">
<code class="descname">device_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.VolumeAttachment.device_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the device to which the volume should be attached</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.VolumeAttachment.volume_id">
<code class="descname">volume_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.VolumeAttachment.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the volume to attach</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_packet.VolumeAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.VolumeAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.VolumeAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.VolumeAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.get_operating_system">
<code class="descclassname">pulumi_packet.</code><code class="descname">get_operating_system</code><span class="sig-paren">(</span><em>distro=None</em>, <em>name=None</em>, <em>provisionable_on=None</em>, <em>version=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.get_operating_system" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get Packet Operating System image.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/d/operating_system.html.markdown">https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/d/operating_system.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_packet.get_precreated_ip_block">
<code class="descclassname">pulumi_packet.</code><code class="descname">get_precreated_ip_block</code><span class="sig-paren">(</span><em>address_family=None</em>, <em>facility=None</em>, <em>global_=None</em>, <em>project_id=None</em>, <em>public=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.get_precreated_ip_block" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get CIDR expression for precreated IPv6 and IPv4 blocks in Packet.
You can then use the cidrsubnet TF builtin function to derive subnets.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/d/precreated_ip_block.html.markdown">https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/d/precreated_ip_block.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_packet.get_spot_market_price">
<code class="descclassname">pulumi_packet.</code><code class="descname">get_spot_market_price</code><span class="sig-paren">(</span><em>facility=None</em>, <em>plan=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.get_spot_market_price" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get Packet Spot Market Price.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/d/spot_market_price.html.markdown">https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/d/spot_market_price.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
