<div class="section" id="module-pulumi_f5bigip.cm">
<span id="cm"></span><h1>cm<a class="headerlink" href="#module-pulumi_f5bigip.cm" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_f5bigip.cm.Device">
<em class="property">class </em><code class="descclassname">pulumi_f5bigip.cm.</code><code class="descname">Device</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>configsync_ip=None</em>, <em>mirror_ip=None</em>, <em>mirror_secondary_ip=None</em>, <em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.Device" title="Permalink to this definition">¶</a></dt>
<dd><p><cite>bigip_cm_device</cite> provides details about a specific bigip</p>
<p>This resource is helpful when configuring the BIG-IP device in cluster or in HA mode.</p>
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
<p>:param pulumi.Input[str] configsync_ip
:param pulumi.Input[str] mirror_ip
:param pulumi.Input[str] mirror_secondary_ip
:param pulumi.Input[str] name</p>
<dl class="method">
<dt id="pulumi_f5bigip.cm.Device.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.Device.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.cm.Device.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.Device.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.cm.DeviceGroup">
<em class="property">class </em><code class="descclassname">pulumi_f5bigip.cm.</code><code class="descname">DeviceGroup</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>auto_sync=None</em>, <em>description=None</em>, <em>devices=None</em>, <em>full_load_on_sync=None</em>, <em>incremental_config=None</em>, <em>name=None</em>, <em>network_failover=None</em>, <em>partition=None</em>, <em>save_on_auto_sync=None</em>, <em>type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup" title="Permalink to this definition">¶</a></dt>
<dd><p><cite>bigip_cm_devicegroup</cite> A device group is a collection of BIG-IP devices that are configured to securely synchronize their BIG-IP configuration data, and fail over when needed.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>auto_sync</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if the device-group will automatically sync configuration data to its members</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] description
:param pulumi.Input[list] devices: Name of the device to be included in device group, this need to be configured before using devicegroup resource
:param pulumi.Input[str] full_load_on_sync
:param pulumi.Input[int] incremental_config
:param pulumi.Input[str] name: Is the name of the device Group
:param pulumi.Input[str] network_failover
:param pulumi.Input[str] partition
:param pulumi.Input[str] save_on_auto_sync
:param pulumi.Input[str] type: Specifies if the device-group will be used for failover or resource syncing</p>
<dl class="attribute">
<dt id="pulumi_f5bigip.cm.DeviceGroup.auto_sync">
<code class="descname">auto_sync</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.auto_sync" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the device-group will automatically sync configuration data to its members</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.cm.DeviceGroup.devices">
<code class="descname">devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the device to be included in device group, this need to be configured before using devicegroup resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.cm.DeviceGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the name of the device Group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.cm.DeviceGroup.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the device-group will be used for failover or resource syncing</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.cm.DeviceGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.cm.DeviceGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
