---
title: Module cm
title_tag: Module cm | Package pulumi_f5bigip | Python SDK
linktitle: cm
notitle: true
---

<div class="section" id="cm">
<h1>cm<a class="headerlink" href="#cm" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-f5bigip">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-f5bigip/issues">pulumi/pulumi-f5bigip repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-f5bigip/issues">terraform-providers/terraform-provider-f5bigip repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_f5bigip.cm"></span><dl class="class">
<dt id="pulumi_f5bigip.cm.Device">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.cm.</code><code class="sig-name descname">Device</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">configsync_ip=None</em>, <em class="sig-param">mirror_ip=None</em>, <em class="sig-param">mirror_secondary_ip=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.Device" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">cm.Device</span></code> provides details about a specific bigip</p>
<p>This resource is helpful when configuring the BIG-IP device in cluster or in HA mode.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-bigip/blob/master/website/docs/r/cm_device.html.markdown">https://github.com/terraform-providers/terraform-provider-bigip/blob/master/website/docs/r/cm_device.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_f5bigip.cm.Device.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">configsync_ip=None</em>, <em class="sig-param">mirror_ip=None</em>, <em class="sig-param">mirror_secondary_ip=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.Device.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Device resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-bigip/blob/master/website/docs/r/cm_device.html.markdown">https://github.com/terraform-providers/terraform-provider-bigip/blob/master/website/docs/r/cm_device.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.cm.Device.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.Device.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.cm.Device.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.Device.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.cm.DeviceGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.cm.</code><code class="sig-name descname">DeviceGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_sync=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">devices=None</em>, <em class="sig-param">full_load_on_sync=None</em>, <em class="sig-param">incremental_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_failover=None</em>, <em class="sig-param">partition=None</em>, <em class="sig-param">save_on_auto_sync=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">cm.DeviceGroup</span></code> A device group is a collection of BIG-IP devices that are configured to securely synchronize their BIG-IP configuration data, and fail over when needed.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_sync</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if the device-group will automatically sync configuration data to its members</p></li>
<li><p><strong>devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Name of the device to be included in device group, this need to be configured before using devicegroup resource</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Is the name of the device Group</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if the device-group will be used for failover or resource syncing</p></li>
</ul>
</dd>
</dl>
<p>The <strong>devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Is the name of the device Group</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">setSyncLeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-bigip/blob/master/website/docs/r/cm_devicegroup.html.markdown">https://github.com/terraform-providers/terraform-provider-bigip/blob/master/website/docs/r/cm_devicegroup.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_f5bigip.cm.DeviceGroup.auto_sync">
<code class="sig-name descname">auto_sync</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.auto_sync" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the device-group will automatically sync configuration data to its members</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.cm.DeviceGroup.devices">
<code class="sig-name descname">devices</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the device to be included in device group, this need to be configured before using devicegroup resource</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Is the name of the device Group</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">setSyncLeader</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.cm.DeviceGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the name of the device Group</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.cm.DeviceGroup.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the device-group will be used for failover or resource syncing</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.cm.DeviceGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_sync=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">devices=None</em>, <em class="sig-param">full_load_on_sync=None</em>, <em class="sig-param">incremental_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_failover=None</em>, <em class="sig-param">partition=None</em>, <em class="sig-param">save_on_auto_sync=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DeviceGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_sync</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if the device-group will automatically sync configuration data to its members</p></li>
<li><p><strong>devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Name of the device to be included in device group, this need to be configured before using devicegroup resource</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Is the name of the device Group</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if the device-group will be used for failover or resource syncing</p></li>
</ul>
</dd>
</dl>
<p>The <strong>devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Is the name of the device Group</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">setSyncLeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-bigip/blob/master/website/docs/r/cm_devicegroup.html.markdown">https://github.com/terraform-providers/terraform-provider-bigip/blob/master/website/docs/r/cm_devicegroup.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.cm.DeviceGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.cm.DeviceGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
