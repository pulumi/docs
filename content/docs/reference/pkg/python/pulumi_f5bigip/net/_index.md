---
title: Module net
title_tag: Module net | Package pulumi_f5bigip | Python SDK
linktitle: net
notitle: true
---

<div class="section" id="net">
<h1>net<a class="headerlink" href="#net" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-f5bigip">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-f5bigip/issues">pulumi/pulumi-f5bigip repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-f5bigip/issues">terraform-providers/terraform-provider-f5bigip repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_f5bigip.net"></span><dl class="class">
<dt id="pulumi_f5bigip.net.Route">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.net.</code><code class="sig-name descname">Route</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">gw=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.Route" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">net.Route</span></code> Manages a route configuration</p>
<p>For resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>gw</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Gateway address</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the route</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a gateway address for the route.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.net.Route.gw">
<code class="sig-name descname">gw</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.Route.gw" title="Permalink to this definition">¶</a></dt>
<dd><p>Gateway address</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.net.Route.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.Route.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the route</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.net.Route.network">
<code class="sig-name descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.Route.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a gateway address for the route.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.net.Route.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">gw=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.Route.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Route resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>gw</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Gateway address</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the route</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a gateway address for the route.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.net.Route.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.Route.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.net.Route.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.Route.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.net.SelfIp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.net.</code><code class="sig-name descname">SelfIp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ip=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">traffic_group=None</em>, <em class="sig-param">vlan=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.SelfIp" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">net.SelfIp</span></code> Manages a selfip configuration</p>
<p>Resource should be named with their “full path”. The full path is the combination of the partition + name of the resource, for example /Common/my-selfip.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Self IP’s address and netmask.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the selfip</p></li>
<li><p><strong>traffic_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the traffic group, defaults to <code class="docutils literal notranslate"><span class="pre">traffic-group-local-only</span></code> if not specified.</p></li>
<li><p><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the VLAN for which you are setting a self IP address. This setting must be provided when a self IP is created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_f5bigip.net.SelfIp.ip">
<code class="sig-name descname">ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.SelfIp.ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The Self IP’s address and netmask.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.net.SelfIp.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.SelfIp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the selfip</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.net.SelfIp.traffic_group">
<code class="sig-name descname">traffic_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.SelfIp.traffic_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the traffic group, defaults to <code class="docutils literal notranslate"><span class="pre">traffic-group-local-only</span></code> if not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.net.SelfIp.vlan">
<code class="sig-name descname">vlan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.SelfIp.vlan" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the VLAN for which you are setting a self IP address. This setting must be provided when a self IP is created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.net.SelfIp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ip=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">traffic_group=None</em>, <em class="sig-param">vlan=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.SelfIp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SelfIp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Self IP’s address and netmask.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the selfip</p></li>
<li><p><strong>traffic_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the traffic group, defaults to <code class="docutils literal notranslate"><span class="pre">traffic-group-local-only</span></code> if not specified.</p></li>
<li><p><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the VLAN for which you are setting a self IP address. This setting must be provided when a self IP is created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.net.SelfIp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.SelfIp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.net.SelfIp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.SelfIp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.net.Vlan">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_f5bigip.net.</code><code class="sig-name descname">Vlan</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">interfaces=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tag=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.Vlan" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">net.Vlan</span></code> Manages a vlan configuration</p>
<p>For resources should be named with their “full path”. The full path is the combination of the partition + name of the resource. For example /Common/my-pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>interfaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies which interfaces you want this VLAN to use for traffic management.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the vlan</p></li>
<li><p><strong>tag</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies a number that the system adds into the header of any frame passing through the VLAN.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">tagged</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies a list of tagged interfaces or trunks associated with this VLAN. Note that you can associate tagged interfaces or trunks with any number of VLANs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vlanport</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Physical or virtual port used for traffic</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_f5bigip.net.Vlan.interfaces">
<code class="sig-name descname">interfaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.Vlan.interfaces" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies which interfaces you want this VLAN to use for traffic management.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">tagged</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies a list of tagged interfaces or trunks associated with this VLAN. Note that you can associate tagged interfaces or trunks with any number of VLANs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vlanport</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Physical or virtual port used for traffic</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.net.Vlan.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.Vlan.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the vlan</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_f5bigip.net.Vlan.tag">
<code class="sig-name descname">tag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_f5bigip.net.Vlan.tag" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a number that the system adds into the header of any frame passing through the VLAN.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.net.Vlan.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">interfaces=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">tag=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.Vlan.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Vlan resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>interfaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies which interfaces you want this VLAN to use for traffic management.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the vlan</p></li>
<li><p><strong>tag</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies a number that the system adds into the header of any frame passing through the VLAN.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">tagged</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies a list of tagged interfaces or trunks associated with this VLAN. Note that you can associate tagged interfaces or trunks with any number of VLANs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vlanport</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Physical or virtual port used for traffic</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_f5bigip.net.Vlan.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.Vlan.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_f5bigip.net.Vlan.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_f5bigip.net.Vlan.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
