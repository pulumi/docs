<div class="section" id="module-pulumi_packet">
<span id="pulumi-packet"></span><h1>Pulumi Packet<a class="headerlink" href="#module-pulumi_packet" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_packet.Device">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">Device</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>always_pxe=None</em>, <em>billing_cycle=None</em>, <em>description=None</em>, <em>facility=None</em>, <em>hardware_reservation_id=None</em>, <em>hostname=None</em>, <em>ipxe_script_url=None</em>, <em>operating_system=None</em>, <em>plan=None</em>, <em>project_id=None</em>, <em>public_ipv4_subnet_size=None</em>, <em>storage=None</em>, <em>tags=None</em>, <em>user_data=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Device" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet device resource. This can be used to create,
modify, and delete devices.</p>
<blockquote>
<div><dl class="docutils">
<dt><strong>Note:</strong> All arguments including the root_password and user_data will be stored in</dt>
<dd>the raw state as plain-text.</dd>
</dl>
<p><a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<p>:param str <strong>name</strong>: The name of the resource.
:param pulumi.ResourceOptions <strong>opts</strong>: Options for the resource.
:param pulumi.Input[bool] always_pxe: If true, a device with OS <code class="docutils literal notranslate"><span class="pre">custom_ipxe</span></code> will</p>
<blockquote>
<div>continue to boot via iPXE on reboots.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>billing_cycle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – monthly or hourly</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description string for the device</li>
<li><strong>facility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The facility in which to create the device. To find the facility code, visit <a class="reference external" href="https://www.packet.net/developers/api/#facilities">Facilities API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</li>
<li><strong>hardware_reservation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of hardware reservation where you want this device deployed, or <code class="docutils literal notranslate"><span class="pre">next-available</span></code> if you want to pick your next available reservation automatically.</li>
<li><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The device name</li>
<li><strong>ipxe_script_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL pointing to a hosted iPXE script. More
information is in the
<a class="reference external" href="https://help.packet.net/article/26-custom-ipxe">Custom iPXE</a>
doc.</li>
<li><strong>operating_system</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operating system slug. To find the slug, or visit <a class="reference external" href="https://www.packet.net/developers/api/#operatingsystems">Operating Systems API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</li>
<li><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The device plan slug. To find the plan slug, visit <a class="reference external" href="https://www.packet.net/developers/api/#plans">Device plans API docs</a>, set your auth token in the top of the page and see JSON from the API response.</li>
<li><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project in which to create the device</li>
<li><strong>public_ipv4_subnet_size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Size of allocated subnet, more
information is in the
<a class="reference external" href="https://help.packet.net/article/55-custom-subnet-size">Custom Subnet Size</a> doc.</li>
<li><strong>storage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON for custom partitioning. Only usable on reserved hardware. More information in in the <a class="reference external" href="https://help.packet.net/article/61-custom-partitioning-raid">Custom Partitioning and RAID</a> doc.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Tags attached to the device</li>
<li><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string of the desired User Data for the device.</li>
</ul>
</td>
</tr>
</tbody>
</table>
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
<dt id="pulumi_packet.Device.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description string for the device</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.facility">
<code class="descname">facility</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.facility" title="Permalink to this definition">¶</a></dt>
<dd><p>The facility in which to create the device. To find the facility code, visit <a class="reference external" href="https://www.packet.net/developers/api/#facilities">Facilities API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</p>
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
<dt id="pulumi_packet.Device.ipxe_script_url">
<code class="descname">ipxe_script_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.ipxe_script_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL pointing to a hosted iPXE script. More
information is in the
<a class="reference external" href="https://help.packet.net/article/26-custom-ipxe">Custom iPXE</a>
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
<dd><p>The device’s private and public IP (v4 and v6) network details</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.operating_system">
<code class="descname">operating_system</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.operating_system" title="Permalink to this definition">¶</a></dt>
<dd><p>The operating system slug. To find the slug, or visit <a class="reference external" href="https://www.packet.net/developers/api/#operatingsystems">Operating Systems API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.plan">
<code class="descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>The device plan slug. To find the plan slug, visit <a class="reference external" href="https://www.packet.net/developers/api/#plans">Device plans API docs</a>, set your auth token in the top of the page and see JSON from the API response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.project_id">
<code class="descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the project in which to create the device</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.public_ipv4_subnet_size">
<code class="descname">public_ipv4_subnet_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.public_ipv4_subnet_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size of allocated subnet, more
information is in the
<a class="reference external" href="https://help.packet.net/article/55-custom-subnet-size">Custom Subnet Size</a> doc.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.root_password">
<code class="descname">root_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.root_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Root password to the server (disabled after 24 hours)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the device</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Device.storage">
<code class="descname">storage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.storage" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON for custom partitioning. Only usable on reserved hardware. More information in in the <a class="reference external" href="https://help.packet.net/article/61-custom-partitioning-raid">Custom Partitioning and RAID</a> doc.</p>
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
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">GetOperatingSystemResult</code><span class="sig-paren">(</span><em>slug=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetOperatingSystemResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getOperatingSystem.</p>
<dl class="attribute">
<dt id="pulumi_packet.GetOperatingSystemResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetOperatingSystemResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_packet.GetPrecreatedIpBlockResult">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">GetPrecreatedIpBlockResult</code><span class="sig-paren">(</span><em>address=None</em>, <em>cidr=None</em>, <em>cidr_notation=None</em>, <em>gateway=None</em>, <em>manageable=None</em>, <em>management=None</em>, <em>netmask=None</em>, <em>network=None</em>, <em>quantity=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetPrecreatedIpBlockResult" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">GetSpotMarketPriceResult</code><span class="sig-paren">(</span><em>price=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetSpotMarketPriceResult" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">IpAttachment</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>cidr_notation=None</em>, <em>device_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.IpAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to attach elastic IP subnets to devices.</p>
<p>To attach an IP subnet from a reserved block to a provisioned device, you must derive a subnet CIDR belonging to
one of your reserved blocks in the same project and facility as the target device.</p>
<p>For example, you have reserved IPv4 address block 147.229.10.152/30, you can choose to assign either the whole
block as one subnet to a device; or 2 subnets with CIDRs 147.229.10.152/31’ and 147.229.10.154/31; or 4 subnets
with mask prefix length 32. More about the elastic IP subnets is <a class="reference external" href="https://help.packet.net/article/54-elastic-ips">here</a>.</p>
<p>Device and reserved block must be in the same facility.</p>
<p>:param str <strong>name</strong>: The name of the resource.
:param pulumi.ResourceOptions <strong>opts</strong>: Options for the resource.
:param pulumi.Input[str] cidr_notation: CIDR notation of subnet from block reserved in the same</p>
<blockquote>
<div>project and facility as the device</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>device_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of device to which to assign the subnet</td>
</tr>
</tbody>
</table>
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
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">Organization</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>description=None</em>, <em>logo=None</em>, <em>name=None</em>, <em>twitter=None</em>, <em>website=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Organization" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage organization resource in Packet.</p>
<p>:param str <strong>name</strong>: The name of the resource.
:param pulumi.ResourceOptions <strong>opts</strong>: Options for the resource.
:param pulumi.Input[str] description: Description string.
:param pulumi.Input[str] logo: Logo URL.
:param pulumi.Input[str] name: The name of the Organization.
:param pulumi.Input[str] twitter: Twitter handle.
:param pulumi.Input[str] website: Website link.</p>
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
<dt id="pulumi_packet.Project">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">Project</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>name=None</em>, <em>organization_id=None</em>, <em>payment_method_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet Project resource to allow you manage devices
in your projects.</p>
<p>:param str <strong>name</strong>: The name of the resource.
:param pulumi.ResourceOptions <strong>opts</strong>: Options for the resource.
:param pulumi.Input[str] name: The name of the Project on Packet.net
:param pulumi.Input[str] organization_id: The UUID of Organization under which you want to create the project. If you leave it out, the project will be create under your the default Organization of your account.
:param pulumi.Input[str] payment_method_id: The UUID of payment method for this project. If you keep it empty, Packet API will pick your default Payment Method.</p>
<dl class="attribute">
<dt id="pulumi_packet.Project.created">
<code class="descname">created</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the Project was created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Project.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Project on Packet.net</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Project.organization_id">
<code class="descname">organization_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.organization_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of Organization under which you want to create the project. If you leave it out, the project will be create under your the default Organization of your account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Project.payment_method_id">
<code class="descname">payment_method_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.payment_method_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of payment method for this project. If you keep it empty, Packet API will pick your default Payment Method.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.Project.updated">
<code class="descname">updated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the Project was updated</p>
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
<dt id="pulumi_packet.Provider">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">Provider</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>auth_token=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the packet package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://pulumi.io/reference/programming-model.html#providers">documentation</a> for more information.</p>
<p>:param str <strong>name</strong>: The name of the resource.
:param pulumi.ResourceOptions <strong>opts</strong>: Options for the resource.
:param pulumi.Input[str] auth_token</p>
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
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">ReservedIpBlock</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>facility=None</em>, <em>project_id=None</em>, <em>quantity=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.ReservedIpBlock" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create and manage blocks of reserved IP addresses in a project.</p>
<p>When user provision first device in a facility, Packet automatically allocates IPv6/56 and private IPv4/25 blocks.
The new device then gets IPv6 and private IPv4 addresses from those block. It also gets a public IPv4/31 address.
Every new device in the project and facility will automatically get IPv6 and private IPv4 addresses from pre-allocated i
blocks.
The IPv6 and private IPv4 blocks can’t be created, only imported.</p>
<p>It is only possible to create public IPv4 blocks, with masks from /24 (256 addresses) to /32 (1 address).</p>
<p>Once IP block is allocated or imported, an address from it can be assigned to device with the <code class="docutils literal notranslate"><span class="pre">packet_ip_attachment</span></code> resource.</p>
<p>:param str <strong>name</strong>: The name of the resource.
:param pulumi.ResourceOptions <strong>opts</strong>: Options for the resource.
:param pulumi.Input[str] facility: The facility where to allocate the address block
:param pulumi.Input[str] project_id: The packet project ID where to allocate the address block
:param pulumi.Input[int] quantity: The number of allocated /32 addresses, a power of 2</p>
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
<dd><p>The facility where to allocate the address block</p>
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
<dt id="pulumi_packet.SSHKey">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">SSHKey</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>name=None</em>, <em>public_key=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SSHKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet SSH key resource to allow you manage SSH
keys on your account. All SSH keys on your account are loaded on
all new devices, they do not have to be explicitly declared on
device creation.</p>
<p>:param str <strong>name</strong>: The name of the resource.
:param pulumi.ResourceOptions <strong>opts</strong>: Options for the resource.
:param pulumi.Input[str] name: The name of the SSH key for identification
:param pulumi.Input[str] public_key: The public key. If this is a file, it</p>
<blockquote>
<div>can be read using the file interpolation function</div></blockquote>
<dl class="attribute">
<dt id="pulumi_packet.SSHKey.created">
<code class="descname">created</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SSHKey.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the SSH key was created</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.SSHKey.fingerprint">
<code class="descname">fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SSHKey.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the SSH key</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.SSHKey.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SSHKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SSH key for identification</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.SSHKey.public_key">
<code class="descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SSHKey.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key. If this is a file, it
can be read using the file interpolation function</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_packet.SSHKey.updated">
<code class="descname">updated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SSHKey.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the SSH key was updated</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_packet.SSHKey.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SSHKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.SSHKey.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SSHKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">SpotMarketRequest</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>devices_max=None</em>, <em>devices_min=None</em>, <em>facilities=None</em>, <em>instance_parameters=None</em>, <em>max_bid_price=None</em>, <em>project_id=None</em>, <em>wait_for_devices=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SpotMarketRequest" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet Spot Market Request resource to allow you to
manage spot market requests on your account. <a class="reference external" href="https://help.packet.net/en-us/article/20-spot-market">https://help.packet.net/en-us/article/20-spot-market</a></p>
<p>:param str <strong>name</strong>: The name of the resource.
:param pulumi.ResourceOptions <strong>opts</strong>: Options for the resource.
:param pulumi.Input[int] devices_max: Maximum number devices to be created
:param pulumi.Input[int] devices_min: Miniumum number devices to be created
:param pulumi.Input[list] facilities: Facility IDs where devices should be created
:param pulumi.Input[dict] instance_parameters: Device parameters. See device resource for details
:param pulumi.Input[float] max_bid_price: Maximum price user is willing to pay per hour per device
:param pulumi.Input[str] project_id: Project ID
:param pulumi.Input[bool] wait_for_devices: On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed</p>
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
<dt id="pulumi_packet.Volume">
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">Volume</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>billing_cycle=None</em>, <em>description=None</em>, <em>facility=None</em>, <em>locked=None</em>, <em>plan=None</em>, <em>project_id=None</em>, <em>size=None</em>, <em>snapshot_policies=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet Block Storage Volume resource to allow you to
manage block volumes on your account.
Once created by Terraform, they must then be attached and mounted
using the api and <code class="docutils literal notranslate"><span class="pre">packet_block_attach</span></code> and <code class="docutils literal notranslate"><span class="pre">packet_block_detach</span></code>
scripts.</p>
<p>:param str <strong>name</strong>: The name of the resource.
:param pulumi.ResourceOptions <strong>opts</strong>: Options for the resource.
:param pulumi.Input[str] billing_cycle: The billing cycle, defaults to “hourly”
:param pulumi.Input[str] description: Optional description for the volume
:param pulumi.Input[str] facility: The facility to create the volume in
:param pulumi.Input[bool] locked: Lock or unlock the volume
:param pulumi.Input[str] plan: The service plan slug of the volume
:param pulumi.Input[str] project_id: The packet project ID to deploy the volume in
:param pulumi.Input[int] size: The size in GB to make the volume
:param pulumi.Input[list] snapshot_policies: Optional list of snapshot policies</p>
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
<em class="property">class </em><code class="descclassname">pulumi_packet.</code><code class="descname">VolumeAttachment</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>device_id=None</em>, <em>volume_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.VolumeAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides attachment of Packet Block Storage Volume to Devices.</p>
<p>Device and volume must be in the same location (facility).</p>
<p>Once attached by Terraform, they must then be mounted using the <code class="docutils literal notranslate"><span class="pre">packet_block_attach</span></code> and <code class="docutils literal notranslate"><span class="pre">packet_block_detach</span></code> scripts.</p>
<p>:param str <strong>name</strong>: The name of the resource.
:param pulumi.ResourceOptions <strong>opts</strong>: Options for the resource.
:param pulumi.Input[str] device_id: The ID of the device to which the volume should be attached
:param pulumi.Input[str] volume_id: The ID of the volume to attach</p>
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
<code class="descclassname">pulumi_packet.</code><code class="descname">get_operating_system</code><span class="sig-paren">(</span><em>distro=None</em>, <em>name=None</em>, <em>provisionable_on=None</em>, <em>version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.get_operating_system" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get Packet Operating System image.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_packet.get_precreated_ip_block">
<code class="descclassname">pulumi_packet.</code><code class="descname">get_precreated_ip_block</code><span class="sig-paren">(</span><em>address_family=None</em>, <em>facility=None</em>, <em>project_id=None</em>, <em>public=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.get_precreated_ip_block" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get CIDR expression for precreated IPv6 and IPv4 blocks in Packet.
You can then use the cidrsubnet TF builtin function to derive subnets.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_packet.get_spot_market_price">
<code class="descclassname">pulumi_packet.</code><code class="descname">get_spot_market_price</code><span class="sig-paren">(</span><em>facility=None</em>, <em>plan=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.get_spot_market_price" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get Packet Spot Market Price.</p>
</dd></dl>

</div>
