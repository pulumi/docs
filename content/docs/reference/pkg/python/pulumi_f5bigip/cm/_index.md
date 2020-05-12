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
<span class="target" id="module-pulumi_f5bigip.cm"></span><dl class="py class">
<dt id="pulumi_f5bigip.cm.Device">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.cm.</code><code class="sig-name descname">Device</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configsync_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mirror_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mirror_secondary_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.Device" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">cm.Device</span></code> provides details about a specific bigip</p>
<p>This resource is helpful when configuring the BIG-IP device in cluster or in HA mode.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_f5bigip</span> <span class="k">as</span> <span class="nn">f5bigip</span>

<span class="n">my_new_device</span> <span class="o">=</span> <span class="n">f5bigip</span><span class="o">.</span><span class="n">cm</span><span class="o">.</span><span class="n">Device</span><span class="p">(</span><span class="s2">&quot;myNewDevice&quot;</span><span class="p">,</span>
    <span class="n">configsync_ip</span><span class="o">=</span><span class="s2">&quot;2.2.2.2&quot;</span><span class="p">,</span>
    <span class="n">mirror_ip</span><span class="o">=</span><span class="s2">&quot;10.10.10.10&quot;</span><span class="p">,</span>
    <span class="n">mirror_secondary_ip</span><span class="o">=</span><span class="s2">&quot;11.11.11.11&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;bigip300.f5.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configsync_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address used for config sync</p></li>
<li><p><strong>mirror_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address used for state mirroring</p></li>
<li><p><strong>mirror_secondary_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Secondary IP address used for state mirroring</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Address of the Device which needs to be Deviceensed</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_f5bigip.cm.Device.configsync_ip">
<code class="sig-name descname">configsync_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.Device.configsync_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address used for config sync</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_f5bigip.cm.Device.mirror_ip">
<code class="sig-name descname">mirror_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.Device.mirror_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address used for state mirroring</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_f5bigip.cm.Device.mirror_secondary_ip">
<code class="sig-name descname">mirror_secondary_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.Device.mirror_secondary_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Secondary IP address used for state mirroring</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_f5bigip.cm.Device.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.Device.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Address of the Device which needs to be Deviceensed</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.cm.Device.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configsync_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mirror_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mirror_secondary_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.Device.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Device resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>configsync_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address used for config sync</p></li>
<li><p><strong>mirror_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address used for state mirroring</p></li>
<li><p><strong>mirror_secondary_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Secondary IP address used for state mirroring</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Address of the Device which needs to be Deviceensed</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.cm.Device.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.Device.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_f5bigip.cm.Device.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.Device.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_f5bigip.cm.DeviceGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.cm.</code><code class="sig-name descname">DeviceGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_sync</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_load_on_sync</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">incremental_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_failover</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">save_on_auto_sync</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">cm.DeviceGroup</span></code> A device group is a collection of BIG-IP devices that are configured to securely synchronize their BIG-IP configuration data, and fail over when needed.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_f5bigip</span> <span class="k">as</span> <span class="nn">f5bigip</span>

<span class="n">my_new_devicegroup</span> <span class="o">=</span> <span class="n">f5bigip</span><span class="o">.</span><span class="n">cm</span><span class="o">.</span><span class="n">DeviceGroup</span><span class="p">(</span><span class="s2">&quot;myNewDevicegroup&quot;</span><span class="p">,</span>
    <span class="n">auto_sync</span><span class="o">=</span><span class="s2">&quot;enabled&quot;</span><span class="p">,</span>
    <span class="n">devices</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;bigip1.cisco.com&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;bigip200.f5.com&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">],</span>
    <span class="n">full_load_on_sync</span><span class="o">=</span><span class="s2">&quot;true&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sanjose_devicegroup&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;sync-only&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_sync</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if the device-group will automatically sync configuration data to its members</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of Device group</p></li>
<li><p><strong>devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Name of the device to be included in device group, this need to be configured before using devicegroup resource</p></li>
<li><p><strong>full_load_on_sync</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if the device-group will perform a full-load upon sync</p></li>
<li><p><strong>incremental_config</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum size (in KB) to devote to incremental config sync cached transactions. The default is 1024 KB.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Is the name of the device Group</p></li>
<li><p><strong>network_failover</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if the device-group will use a network connection for failover</p></li>
<li><p><strong>partition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Device administrative partition</p></li>
<li><p><strong>save_on_auto_sync</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the configuration should be saved upon auto-sync.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if the device-group will be used for failover or resource syncing</p></li>
</ul>
</dd>
</dl>
<p>The <strong>devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Is the name of the device Group</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">setSyncLeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_f5bigip.cm.DeviceGroup.auto_sync">
<code class="sig-name descname">auto_sync</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.auto_sync" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the device-group will automatically sync configuration data to its members</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_f5bigip.cm.DeviceGroup.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of Device group</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_f5bigip.cm.DeviceGroup.devices">
<code class="sig-name descname">devices</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.devices" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the device to be included in device group, this need to be configured before using devicegroup resource</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Is the name of the device Group</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">setSyncLeader</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_f5bigip.cm.DeviceGroup.full_load_on_sync">
<code class="sig-name descname">full_load_on_sync</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.full_load_on_sync" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the device-group will perform a full-load upon sync</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_f5bigip.cm.DeviceGroup.incremental_config">
<code class="sig-name descname">incremental_config</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.incremental_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum size (in KB) to devote to incremental config sync cached transactions. The default is 1024 KB.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_f5bigip.cm.DeviceGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the name of the device Group</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_f5bigip.cm.DeviceGroup.network_failover">
<code class="sig-name descname">network_failover</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.network_failover" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the device-group will use a network connection for failover</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_f5bigip.cm.DeviceGroup.partition">
<code class="sig-name descname">partition</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.partition" title="Permalink to this definition">¶</a></dt>
<dd><p>Device administrative partition</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_f5bigip.cm.DeviceGroup.save_on_auto_sync">
<code class="sig-name descname">save_on_auto_sync</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.save_on_auto_sync" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the configuration should be saved upon auto-sync.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_f5bigip.cm.DeviceGroup.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the device-group will be used for failover or resource syncing</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.cm.DeviceGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_sync</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_load_on_sync</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">incremental_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_failover</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">partition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">save_on_auto_sync</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DeviceGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_sync</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if the device-group will automatically sync configuration data to its members</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of Device group</p></li>
<li><p><strong>devices</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Name of the device to be included in device group, this need to be configured before using devicegroup resource</p></li>
<li><p><strong>full_load_on_sync</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if the device-group will perform a full-load upon sync</p></li>
<li><p><strong>incremental_config</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum size (in KB) to devote to incremental config sync cached transactions. The default is 1024 KB.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Is the name of the device Group</p></li>
<li><p><strong>network_failover</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if the device-group will use a network connection for failover</p></li>
<li><p><strong>partition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Device administrative partition</p></li>
<li><p><strong>save_on_auto_sync</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the configuration should be saved upon auto-sync.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if the device-group will be used for failover or resource syncing</p></li>
</ul>
</dd>
</dl>
<p>The <strong>devices</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Is the name of the device Group</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">setSyncLeader</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_f5bigip.cm.DeviceGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_f5bigip.cm.DeviceGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.cm.DeviceGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
