---
---

<div class="section" id="module-pulumi_f5bigip.net">
<span id="net"></span><h1>net<a class="headerlink" href="#module-pulumi_f5bigip.net" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_f5bigip.net.Route">
<em class="property">class </em><code class="descclassname">pulumi_f5bigip.net.</code><code class="descname">Route</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>gw=None</em>, <em>name=None</em>, <em>network=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.Route" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">bigip_net_route</span></code> Manages a route configuration</p>
<p>For resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the route</li>
<li><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a gateway address for the route.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_f5bigip.net.Route.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.Route.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the route</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.net.Route.network">
<code class="descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.Route.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a gateway address for the route.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.net.Route.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.Route.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.net.Route.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.Route.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.net.SelfIp">
<em class="property">class </em><code class="descclassname">pulumi_f5bigip.net.</code><code class="descname">SelfIp</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>ip=None</em>, <em>name=None</em>, <em>traffic_group=None</em>, <em>vlan=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.SelfIp" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">bigip_net_selfip</span></code> Manages a selfip configuration</p>
<p>Resource should be named with their “full path”. The full path is the combination of the partition + name of the resource, for example /Common/my-selfip.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Self IP’s address and netmask.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the selfip</li>
<li><strong>traffic_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the traffic group, defaults to <code class="docutils literal notranslate"><span class="pre">traffic-group-local-only</span></code> if not specified.</li>
<li><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the VLAN for which you are setting a self IP address. This setting must be provided when a self IP is created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_f5bigip.net.SelfIp.ip">
<code class="descname">ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.SelfIp.ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The Self IP’s address and netmask.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.net.SelfIp.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.SelfIp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the selfip</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.net.SelfIp.traffic_group">
<code class="descname">traffic_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.SelfIp.traffic_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the traffic group, defaults to <code class="docutils literal notranslate"><span class="pre">traffic-group-local-only</span></code> if not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.net.SelfIp.vlan">
<code class="descname">vlan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.SelfIp.vlan" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the VLAN for which you are setting a self IP address. This setting must be provided when a self IP is created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.net.SelfIp.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.SelfIp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.net.SelfIp.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.SelfIp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.net.Vlan">
<em class="property">class </em><code class="descclassname">pulumi_f5bigip.net.</code><code class="descname">Vlan</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>interfaces=None</em>, <em>name=None</em>, <em>tag=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.Vlan" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">bigip_net_vlan</span></code> Manages a vlan configuration</p>
<p>For resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>interfaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies which interfaces you want this VLAN to use for traffic management.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the vlan</li>
<li><strong>tag</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies a number that the system adds into the header of any frame passing through the VLAN.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_f5bigip.net.Vlan.interfaces">
<code class="descname">interfaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.Vlan.interfaces" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies which interfaces you want this VLAN to use for traffic management.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.net.Vlan.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.Vlan.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the vlan</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.net.Vlan.tag">
<code class="descname">tag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.Vlan.tag" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a number that the system adds into the header of any frame passing through the VLAN.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.net.Vlan.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.Vlan.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.net.Vlan.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.Vlan.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
