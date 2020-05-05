---
title: Package pulumi_packet
title_tag: Package pulumi_packet | Python SDK
linktitle: pulumi_packet
notitle: true
---

<div class="section" id="pulumi-packet">
<h1>Pulumi Packet<a class="headerlink" href="#pulumi-packet" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-packet/issues">pulumi/pulumi-packet repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/issues">terraform-providers/terraform-provider-packet repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_packet"></span><dl class="py class">
<dt id="pulumi_packet.AwaitableGetDeviceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">AwaitableGetDeviceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_private_ipv4</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_public_ipv4</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_public_ipv6</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">always_pxe</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_cycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hardware_reservation_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipxe_script_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">operating_system</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ipv4_subnet_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_key_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.AwaitableGetDeviceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_packet.AwaitableGetIpBlockRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">AwaitableGetIpBlockRangesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.AwaitableGetIpBlockRangesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_packet.AwaitableGetOperatingSystemResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">AwaitableGetOperatingSystemResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">distro</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisionable_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slug</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.AwaitableGetOperatingSystemResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_packet.AwaitableGetOrganizationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">AwaitableGetOrganizationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logo</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">twitter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">website</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.AwaitableGetOrganizationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_packet.AwaitableGetPrecreatedIpBlockResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">AwaitableGetPrecreatedIpBlockResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_notation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">manageable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">management</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">netmask</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quantity</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.AwaitableGetPrecreatedIpBlockResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_packet.AwaitableGetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">AwaitableGetProjectResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">backend_transfer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">payment_method_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.AwaitableGetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_packet.AwaitableGetSpotMarketPriceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">AwaitableGetSpotMarketPriceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">price</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.AwaitableGetSpotMarketPriceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_packet.AwaitableGetSpotMarketRequestResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">AwaitableGetSpotMarketRequestResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">device_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.AwaitableGetSpotMarketRequestResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_packet.AwaitableGetVolumeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">AwaitableGetVolumeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">billing_cycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.AwaitableGetVolumeResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_packet.BgpSession">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">BgpSession</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_route</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.BgpSession" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage BGP sessions in Packet Host. Refer to <a class="reference external" href="https://www.packet.com/developers/docs/network/advanced/local-and-global-bgp/">Packet BGP documentation</a> for more details.</p>
<p>You need to have BGP config enabled in your project.</p>
<p>BGP session must be linked to a device running <a class="reference external" href="https://bird.network.cz">BIRD</a> or other BGP routing daemon which will control route advertisements via the session to Packet’s upstream routers.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code></p></li>
<li><p><strong>default_route</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to set the default route policy. False by default.</p></li>
<li><p><strong>device_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of device</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_packet.BgpSession.address_family">
<code class="sig-name descname">address_family</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.BgpSession.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.BgpSession.default_route">
<code class="sig-name descname">default_route</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.BgpSession.default_route" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to set the default route policy. False by default.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.BgpSession.device_id">
<code class="sig-name descname">device_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.BgpSession.device_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.BgpSession.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_route</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.BgpSession.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BgpSession resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code></p></li>
<li><p><strong>default_route</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to set the default route policy. False by default.</p></li>
<li><p><strong>device_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of device</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.BgpSession.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.BgpSession.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.BgpSession.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.BgpSession.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Device">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">Device</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">always_pxe</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_cycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facilities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_detach_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hardware_reservation_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipxe_script_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">operating_system</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_ssh_key_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ipv4_subnet_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_for_reservation_deprovision</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Device" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet device resource. This can be used to create,
modify, and delete devices.</p>
<blockquote>
<div><dl class="simple">
<dt><strong>Note:</strong> All arguments including the <code class="docutils literal notranslate"><span class="pre">root_password</span></code> and <code class="docutils literal notranslate"><span class="pre">user_data</span></code> will be stored in</dt><dd><p>the raw state as plain-text.</p>
</dd>
</dl>
<p><a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>always_pxe</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, a device with OS <code class="docutils literal notranslate"><span class="pre">custom_ipxe</span></code> will
continue to boot via iPXE on reboots.</p></li>
<li><p><strong>billing_cycle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – monthly or hourly</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description string for the device</p></li>
<li><p><strong>facilities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of facility codes with deployment preferences. Packet API will go through the list and will deploy your device to first facility with free capacity. List items must be facility codes or <code class="docutils literal notranslate"><span class="pre">any</span></code> (a wildcard). To find the facility code, visit <a class="reference external" href="https://www.packet.com/developers/api/facilities">Facilities API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</p></li>
<li><p><strong>force_detach_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Delete device even if it has volumes attached. Only applies for destroy action.</p></li>
<li><p><strong>hardware_reservation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of hardware reservation which this device occupies</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `hostname`- The hostname of the device
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The device name</p></li>
<li><p><strong>ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IP address types for the device (structure is documented below).</p></li>
<li><p><strong>ipxe_script_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL pointing to a hosted iPXE script. More
information is in the
<a class="reference external" href="https://www.packet.com/developers/docs/servers/operating-systems/custom-ipxe/">Custom iPXE</a>
doc.</p></li>
<li><p><strong>operating_system</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operating system slug. To find the slug, or visit <a class="reference external" href="https://www.packet.com/developers/api/operatingsystems">Operating Systems API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The device plan slug. To find the plan slug, visit <a class="reference external" href="https://www.packet.com/developers/api/plans">Device plans API docs</a>, set your auth token in the top of the page and see JSON from the API response.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which to create the device</p></li>
<li><p><strong>public_ipv4_subnet_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size of allocated subnet, more
information is in the
<a class="reference external" href="https://www.packet.com/developers/docs/servers/key-features/custom-subnet-size/">Custom Subnet Size</a> doc.</p></li>
<li><p><strong>storage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON for custom partitioning. Only usable on reserved hardware. More information in in the <a class="reference external" href="https://www.packet.com/developers/docs/servers/key-features/cpr/">Custom Partitioning and RAID</a> doc.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Please</span> <span class="n">note</span> <span class="n">that</span> <span class="n">the</span> <span class="n">disks</span><span class="o">.</span><span class="n">partitions</span><span class="o">.</span><span class="n">size</span> <span class="n">attribute</span> <span class="n">must</span> <span class="n">be</span> <span class="n">a</span> <span class="n">string</span><span class="p">,</span> <span class="ow">not</span> <span class="n">an</span> <span class="n">integer</span><span class="o">.</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">a</span> <span class="n">number</span> <span class="n">string</span><span class="p">,</span> <span class="ow">or</span> <span class="n">size</span> <span class="n">notation</span> <span class="n">string</span><span class="p">,</span> <span class="n">e</span><span class="o">.</span><span class="n">g</span><span class="o">.</span> <span class="s2">&quot;4G&quot;</span> <span class="ow">or</span> <span class="s2">&quot;8M&quot;</span> <span class="p">(</span><span class="k">for</span> <span class="n">gigabytes</span> <span class="ow">and</span> <span class="n">megabytes</span><span class="p">)</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Tags attached to the device</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string of the desired User Data for the device.</p></li>
<li><p><strong>wait_for_reservation_deprovision</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Only used for devices in reserved hardware. If set, the deletion of this device will block until the hardware reservation is marked provisionable (about 4 minutes in August 2019).</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ip_addresses</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - CIDR suffix for IP address block to be assigned, i.e. amount of addresses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reservationIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One of [<code class="docutils literal notranslate"><span class="pre">private_ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">public_ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">public_ipv6</span></code>]</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_packet.Device.access_private_ipv4">
<code class="sig-name descname">access_private_ipv4</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.access_private_ipv4" title="Permalink to this definition">¶</a></dt>
<dd><p>The ipv4 private IP assigned to the device</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.access_public_ipv4">
<code class="sig-name descname">access_public_ipv4</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.access_public_ipv4" title="Permalink to this definition">¶</a></dt>
<dd><p>The ipv4 maintenance IP assigned to the device</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.access_public_ipv6">
<code class="sig-name descname">access_public_ipv6</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.access_public_ipv6" title="Permalink to this definition">¶</a></dt>
<dd><p>The ipv6 maintenance IP assigned to the device</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.always_pxe">
<code class="sig-name descname">always_pxe</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.always_pxe" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, a device with OS <code class="docutils literal notranslate"><span class="pre">custom_ipxe</span></code> will
continue to boot via iPXE on reboots.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.billing_cycle">
<code class="sig-name descname">billing_cycle</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.billing_cycle" title="Permalink to this definition">¶</a></dt>
<dd><p>monthly or hourly</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.created">
<code class="sig-name descname">created</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the device was created</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.deployed_facility">
<code class="sig-name descname">deployed_facility</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.deployed_facility" title="Permalink to this definition">¶</a></dt>
<dd><p>The facility where the device is deployed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description string for the device</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.facilities">
<code class="sig-name descname">facilities</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.facilities" title="Permalink to this definition">¶</a></dt>
<dd><p>List of facility codes with deployment preferences. Packet API will go through the list and will deploy your device to first facility with free capacity. List items must be facility codes or <code class="docutils literal notranslate"><span class="pre">any</span></code> (a wildcard). To find the facility code, visit <a class="reference external" href="https://www.packet.com/developers/api/facilities">Facilities API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.force_detach_volumes">
<code class="sig-name descname">force_detach_volumes</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.force_detach_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p>Delete device even if it has volumes attached. Only applies for destroy action.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.hardware_reservation_id">
<code class="sig-name descname">hardware_reservation_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.hardware_reservation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of hardware reservation which this device occupies</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code>- The hostname of the device</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.hostname">
<code class="sig-name descname">hostname</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The device name</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.ip_addresses">
<code class="sig-name descname">ip_addresses</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IP address types for the device (structure is documented below).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cidr</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - CIDR suffix for IP address block to be assigned, i.e. amount of addresses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reservationIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - One of [<code class="docutils literal notranslate"><span class="pre">private_ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">public_ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">public_ipv6</span></code>]</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.ipxe_script_url">
<code class="sig-name descname">ipxe_script_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.ipxe_script_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL pointing to a hosted iPXE script. More
information is in the
<a class="reference external" href="https://www.packet.com/developers/docs/servers/operating-systems/custom-ipxe/">Custom iPXE</a>
doc.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.locked">
<code class="sig-name descname">locked</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.locked" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the device is locked</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.networks">
<code class="sig-name descname">networks</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.networks" title="Permalink to this definition">¶</a></dt>
<dd><p>The device’s private and public IP (v4 and v6) network details. When a device is run without any special network configuration, it will have 3 networks:</p>
<ul class="simple">
<li><p>Public IPv4 at <code class="docutils literal notranslate"><span class="pre">packet_device.name.network.0</span></code></p></li>
<li><p>IPv6 at <code class="docutils literal notranslate"><span class="pre">packet_device.name.network.1</span></code></p></li>
<li><p>Private IPv4 at <code class="docutils literal notranslate"><span class="pre">packet_device.name.network.2</span></code>
Elastic addresses then stack by type - an assigned public IPv4 will go after the management public IPv4 (to index 1), and will then shift the indices of the IPv6 and private IPv4. Assigned private IPv4 will go after the management private IPv4 (to the end of the network list).
The fields of the network attributes are:</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - IPv4 or IPv6 address string</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cidr</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - CIDR suffix for IP address block to be assigned, i.e. amount of addresses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">family</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - IP version - “4” or “6”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gateway</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - address of router</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - whether the address is routable from the Internet</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.operating_system">
<code class="sig-name descname">operating_system</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.operating_system" title="Permalink to this definition">¶</a></dt>
<dd><p>The operating system slug. To find the slug, or visit <a class="reference external" href="https://www.packet.com/developers/api/operatingsystems">Operating Systems API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.plan">
<code class="sig-name descname">plan</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>The device plan slug. To find the plan slug, visit <a class="reference external" href="https://www.packet.com/developers/api/plans">Device plans API docs</a>, set your auth token in the top of the page and see JSON from the API response.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.ports">
<code class="sig-name descname">ports</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.ports" title="Permalink to this definition">¶</a></dt>
<dd><p>Ports assigned to the device</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bonded</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether this port is part of a bond in bonded network setup</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code>- The ID of the project the device belongs to</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - ID of the port</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mac</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - MAC address assigned to the port</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the port (e.g. <code class="docutils literal notranslate"><span class="pre">eth0</span></code>, or <code class="docutils literal notranslate"><span class="pre">bond0</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - One of [<code class="docutils literal notranslate"><span class="pre">private_ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">public_ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">public_ipv6</span></code>]</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which to create the device</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.public_ipv4_subnet_size">
<code class="sig-name descname">public_ipv4_subnet_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.public_ipv4_subnet_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size of allocated subnet, more
information is in the
<a class="reference external" href="https://www.packet.com/developers/docs/servers/key-features/custom-subnet-size/">Custom Subnet Size</a> doc.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.root_password">
<code class="sig-name descname">root_password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.root_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Root password to the server (disabled after 24 hours)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.ssh_key_ids">
<code class="sig-name descname">ssh_key_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.ssh_key_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IDs of SSH keys deployed in the device, can be both user and project SSH keys</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.state">
<code class="sig-name descname">state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the device</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.storage">
<code class="sig-name descname">storage</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.storage" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON for custom partitioning. Only usable on reserved hardware. More information in in the <a class="reference external" href="https://www.packet.com/developers/docs/servers/key-features/cpr/">Custom Partitioning and RAID</a> doc.</p>
<ul class="simple">
<li><p>Please note that the disks.partitions.size attribute must be a string, not an integer. It can be a number string, or size notation string, e.g. “4G” or “8M” (for gigabytes and megabytes).</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tags attached to the device</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.updated">
<code class="sig-name descname">updated</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the device was updated</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.user_data">
<code class="sig-name descname">user_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>A string of the desired User Data for the device.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Device.wait_for_reservation_deprovision">
<code class="sig-name descname">wait_for_reservation_deprovision</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Device.wait_for_reservation_deprovision" title="Permalink to this definition">¶</a></dt>
<dd><p>Only used for devices in reserved hardware. If set, the deletion of this device will block until the hardware reservation is marked provisionable (about 4 minutes in August 2019).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_private_ipv4</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_public_ipv4</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_public_ipv6</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">always_pxe</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_cycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deployed_facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facilities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_detach_volumes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hardware_reservation_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipxe_script_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">operating_system</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_ssh_key_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ipv4_subnet_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_key_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_for_reservation_deprovision</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Device.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Device resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_private_ipv4</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ipv4 private IP assigned to the device</p></li>
<li><p><strong>access_public_ipv4</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ipv4 maintenance IP assigned to the device</p></li>
<li><p><strong>access_public_ipv6</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ipv6 maintenance IP assigned to the device</p></li>
<li><p><strong>always_pxe</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, a device with OS <code class="docutils literal notranslate"><span class="pre">custom_ipxe</span></code> will
continue to boot via iPXE on reboots.</p></li>
<li><p><strong>billing_cycle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – monthly or hourly</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timestamp for when the device was created</p></li>
<li><p><strong>deployed_facility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The facility where the device is deployed.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description string for the device</p></li>
<li><p><strong>facilities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>List of facility codes with deployment preferences. Packet API will go through the list and will deploy your device to first facility with free capacity. List items must be facility codes or <code class="docutils literal notranslate"><span class="pre">any</span></code> (a wildcard). To find the facility code, visit <a class="reference external" href="https://www.packet.com/developers/api/facilities">Facilities API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</p>
</p></li>
<li><p><strong>force_detach_volumes</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Delete device even if it has volumes attached. Only applies for destroy action.</p></li>
<li><p><strong>hardware_reservation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of hardware reservation which this device occupies</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `hostname`- The hostname of the device
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>hostname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The device name</p></li>
<li><p><strong>ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IP address types for the device (structure is documented below).</p></li>
<li><p><strong>ipxe_script_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>URL pointing to a hosted iPXE script. More
information is in the
<a class="reference external" href="https://www.packet.com/developers/docs/servers/operating-systems/custom-ipxe/">Custom iPXE</a>
doc.</p>
</p></li>
<li><p><strong>locked</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the device is locked</p></li>
<li><p><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The device’s private and public IP (v4 and v6) network details. When a device is run without any special network configuration, it will have 3 networks:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* Public IPv4 at `packet_device.name.network.0`
* IPv6 at `packet_device.name.network.1`
* Private IPv4 at `packet_device.name.network.2`
Elastic addresses then stack by type - an assigned public IPv4 will go after the management public IPv4 (to index 1), and will then shift the indices of the IPv6 and private IPv4. Assigned private IPv4 will go after the management private IPv4 (to the end of the network list).
The fields of the network attributes are:
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>operating_system</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The operating system slug. To find the slug, or visit <a class="reference external" href="https://www.packet.com/developers/api/operatingsystems">Operating Systems API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</p>
</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The device plan slug. To find the plan slug, visit <a class="reference external" href="https://www.packet.com/developers/api/plans">Device plans API docs</a>, set your auth token in the top of the page and see JSON from the API response.</p>
</p></li>
<li><p><strong>ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Ports assigned to the device</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which to create the device</p></li>
<li><p><strong>public_ipv4_subnet_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>Size of allocated subnet, more
information is in the
<a class="reference external" href="https://www.packet.com/developers/docs/servers/key-features/custom-subnet-size/">Custom Subnet Size</a> doc.</p>
</p></li>
<li><p><strong>root_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Root password to the server (disabled after 24 hours)</p></li>
<li><p><strong>ssh_key_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IDs of SSH keys deployed in the device, can be both user and project SSH keys</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the device</p></li>
<li><p><strong>storage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>JSON for custom partitioning. Only usable on reserved hardware. More information in in the <a class="reference external" href="https://www.packet.com/developers/docs/servers/key-features/cpr/">Custom Partitioning and RAID</a> doc.</p>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Please</span> <span class="n">note</span> <span class="n">that</span> <span class="n">the</span> <span class="n">disks</span><span class="o">.</span><span class="n">partitions</span><span class="o">.</span><span class="n">size</span> <span class="n">attribute</span> <span class="n">must</span> <span class="n">be</span> <span class="n">a</span> <span class="n">string</span><span class="p">,</span> <span class="ow">not</span> <span class="n">an</span> <span class="n">integer</span><span class="o">.</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">a</span> <span class="n">number</span> <span class="n">string</span><span class="p">,</span> <span class="ow">or</span> <span class="n">size</span> <span class="n">notation</span> <span class="n">string</span><span class="p">,</span> <span class="n">e</span><span class="o">.</span><span class="n">g</span><span class="o">.</span> <span class="s2">&quot;4G&quot;</span> <span class="ow">or</span> <span class="s2">&quot;8M&quot;</span> <span class="p">(</span><span class="k">for</span> <span class="n">gigabytes</span> <span class="ow">and</span> <span class="n">megabytes</span><span class="p">)</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Tags attached to the device</p></li>
<li><p><strong>updated</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timestamp for the last time the device was updated</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string of the desired User Data for the device.</p></li>
<li><p><strong>wait_for_reservation_deprovision</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Only used for devices in reserved hardware. If set, the deletion of this device will block until the hardware reservation is marked provisionable (about 4 minutes in August 2019).</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ip_addresses</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - CIDR suffix for IP address block to be assigned, i.e. amount of addresses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reservationIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One of [<code class="docutils literal notranslate"><span class="pre">private_ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">public_ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">public_ipv6</span></code>]</p></li>
</ul>
<p>The <strong>networks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - IPv4 or IPv6 address string</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - CIDR suffix for IP address block to be assigned, i.e. amount of addresses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">family</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - IP version - “4” or “6”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gateway</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - address of router</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - whether the address is routable from the Internet</p></li>
</ul>
<p>The <strong>ports</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">bonded</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether this port is part of a bond in bonded network setup</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code>- The ID of the project the device belongs to</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - ID of the port</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mac</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - MAC address assigned to the port</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the port (e.g. <code class="docutils literal notranslate"><span class="pre">eth0</span></code>, or <code class="docutils literal notranslate"><span class="pre">bond0</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - One of [<code class="docutils literal notranslate"><span class="pre">private_ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">public_ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">public_ipv6</span></code>]</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Device.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Device.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Device.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.GetDeviceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetDeviceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_private_ipv4</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_public_ipv4</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_public_ipv6</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">always_pxe</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_cycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hardware_reservation_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipxe_script_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">operating_system</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ipv4_subnet_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_key_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetDeviceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDevice.</p>
<dl class="py attribute">
<dt id="pulumi_packet.GetDeviceResult.access_private_ipv4">
<code class="sig-name descname">access_private_ipv4</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetDeviceResult.access_private_ipv4" title="Permalink to this definition">¶</a></dt>
<dd><p>The ipv4 private IP assigned to the device</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetDeviceResult.access_public_ipv4">
<code class="sig-name descname">access_public_ipv4</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetDeviceResult.access_public_ipv4" title="Permalink to this definition">¶</a></dt>
<dd><p>The ipv4 management IP assigned to the device</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetDeviceResult.access_public_ipv6">
<code class="sig-name descname">access_public_ipv6</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetDeviceResult.access_public_ipv6" title="Permalink to this definition">¶</a></dt>
<dd><p>The ipv6 management IP assigned to the device</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetDeviceResult.billing_cycle">
<code class="sig-name descname">billing_cycle</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetDeviceResult.billing_cycle" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing cycle of the device (monthly or hourly)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetDeviceResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetDeviceResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description string for the device</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetDeviceResult.facility">
<code class="sig-name descname">facility</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetDeviceResult.facility" title="Permalink to this definition">¶</a></dt>
<dd><p>The facility where the device is deployed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetDeviceResult.hardware_reservation_id">
<code class="sig-name descname">hardware_reservation_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetDeviceResult.hardware_reservation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of hardware reservation which this device occupies</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetDeviceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetDeviceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetDeviceResult.network_type">
<code class="sig-name descname">network_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetDeviceResult.network_type" title="Permalink to this definition">¶</a></dt>
<dd><p>L2 network type of the device, one of “layer3”, “layer2-bonded”, “layer2-individual”, “hybrid”</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetDeviceResult.networks">
<code class="sig-name descname">networks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetDeviceResult.networks" title="Permalink to this definition">¶</a></dt>
<dd><p>The device’s private and public IP (v4 and v6) network details. When a device is run without any special network configuration, it will have 3 networks:</p>
<ul class="simple">
<li><p>Public IPv4 at <code class="docutils literal notranslate"><span class="pre">packet_device.name.network.0</span></code></p></li>
<li><p>IPv6 at <code class="docutils literal notranslate"><span class="pre">packet_device.name.network.1</span></code></p></li>
<li><p>Private IPv4 at <code class="docutils literal notranslate"><span class="pre">packet_device.name.network.2</span></code>
Elastic addresses then stack by type - an assigned public IPv4 will go after the management public IPv4 (to index 1), and will then shift the indices of the IPv6 and private IPv4. Assigned private IPv4 will go after the management private IPv4 (to the end of the network list).
The fields of the network attributes are:</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetDeviceResult.operating_system">
<code class="sig-name descname">operating_system</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetDeviceResult.operating_system" title="Permalink to this definition">¶</a></dt>
<dd><p>The operating system running on the device</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetDeviceResult.plan">
<code class="sig-name descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetDeviceResult.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>The hardware config of the device</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetDeviceResult.ports">
<code class="sig-name descname">ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetDeviceResult.ports" title="Permalink to this definition">¶</a></dt>
<dd><p>Ports assigned to the device</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetDeviceResult.root_password">
<code class="sig-name descname">root_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetDeviceResult.root_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Root password to the server (if still available)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetDeviceResult.ssh_key_ids">
<code class="sig-name descname">ssh_key_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetDeviceResult.ssh_key_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IDs of SSH keys deployed in the device, can be both user or project SSH keys</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetDeviceResult.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetDeviceResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the device</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetDeviceResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetDeviceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tags attached to the device</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.GetIpBlockRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetIpBlockRangesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetIpBlockRangesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIpBlockRanges.</p>
<dl class="py attribute">
<dt id="pulumi_packet.GetIpBlockRangesResult.global_ipv4s">
<code class="sig-name descname">global_ipv4s</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetIpBlockRangesResult.global_ipv4s" title="Permalink to this definition">¶</a></dt>
<dd><p>list of CIDR expressions for Global IPv4 blocks in the project</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetIpBlockRangesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetIpBlockRangesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetIpBlockRangesResult.ipv6s">
<code class="sig-name descname">ipv6s</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetIpBlockRangesResult.ipv6s" title="Permalink to this definition">¶</a></dt>
<dd><p>list of CIDR expressions for IPv6 blocks in the project</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetIpBlockRangesResult.private_ipv4s">
<code class="sig-name descname">private_ipv4s</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetIpBlockRangesResult.private_ipv4s" title="Permalink to this definition">¶</a></dt>
<dd><p>list of CIDR expressions for Private IPv4 blocks in the project</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetIpBlockRangesResult.public_ipv4s">
<code class="sig-name descname">public_ipv4s</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetIpBlockRangesResult.public_ipv4s" title="Permalink to this definition">¶</a></dt>
<dd><p>list of CIDR expressions for Public IPv4 blocks in the project</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.GetOperatingSystemResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetOperatingSystemResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">distro</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisionable_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slug</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetOperatingSystemResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getOperatingSystem.</p>
<dl class="py attribute">
<dt id="pulumi_packet.GetOperatingSystemResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetOperatingSystemResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetOperatingSystemResult.slug">
<code class="sig-name descname">slug</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetOperatingSystemResult.slug" title="Permalink to this definition">¶</a></dt>
<dd><p>Operating system slug (same as <code class="docutils literal notranslate"><span class="pre">id</span></code>)</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.GetOrganizationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetOrganizationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logo</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">twitter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">website</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetOrganizationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getOrganization.</p>
<dl class="py attribute">
<dt id="pulumi_packet.GetOrganizationResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetOrganizationResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description string</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetOrganizationResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetOrganizationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetOrganizationResult.logo">
<code class="sig-name descname">logo</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetOrganizationResult.logo" title="Permalink to this definition">¶</a></dt>
<dd><p>Logo URL</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetOrganizationResult.project_ids">
<code class="sig-name descname">project_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetOrganizationResult.project_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>UUIDs of project resources which belong to this organization</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetOrganizationResult.twitter">
<code class="sig-name descname">twitter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetOrganizationResult.twitter" title="Permalink to this definition">¶</a></dt>
<dd><p>Twitter handle</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetOrganizationResult.website">
<code class="sig-name descname">website</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetOrganizationResult.website" title="Permalink to this definition">¶</a></dt>
<dd><p>Website link</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.GetPrecreatedIpBlockResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetPrecreatedIpBlockResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_notation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">manageable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">management</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">netmask</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quantity</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetPrecreatedIpBlockResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPrecreatedIpBlock.</p>
<dl class="py attribute">
<dt id="pulumi_packet.GetPrecreatedIpBlockResult.cidr_notation">
<code class="sig-name descname">cidr_notation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetPrecreatedIpBlockResult.cidr_notation" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR notation of the looked up block.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetPrecreatedIpBlockResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetPrecreatedIpBlockResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.GetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetProjectResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">backend_transfer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">payment_method_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProject.</p>
<dl class="py attribute">
<dt id="pulumi_packet.GetProjectResult.backend_transfer">
<code class="sig-name descname">backend_transfer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetProjectResult.backend_transfer" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Backend Transfer is enabled for this project</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetProjectResult.bgp_config">
<code class="sig-name descname">bgp_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetProjectResult.bgp_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional BGP settings. Refer to <a class="reference external" href="https://www.packet.com/developers/docs/network/advanced/local-and-global-bgp/">Packet guide for BGP</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetProjectResult.created">
<code class="sig-name descname">created</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetProjectResult.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the project was created</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetProjectResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetProjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetProjectResult.organization_id">
<code class="sig-name descname">organization_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetProjectResult.organization_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of this project’s parent organization</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetProjectResult.payment_method_id">
<code class="sig-name descname">payment_method_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetProjectResult.payment_method_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of payment method for this project</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetProjectResult.updated">
<code class="sig-name descname">updated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetProjectResult.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the project was updated</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetProjectResult.user_ids">
<code class="sig-name descname">user_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetProjectResult.user_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of UUIDs of user accounts which beling to this project</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.GetSpotMarketPriceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetSpotMarketPriceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">price</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetSpotMarketPriceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSpotMarketPrice.</p>
<dl class="py attribute">
<dt id="pulumi_packet.GetSpotMarketPriceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetSpotMarketPriceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetSpotMarketPriceResult.price">
<code class="sig-name descname">price</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetSpotMarketPriceResult.price" title="Permalink to this definition">¶</a></dt>
<dd><p>Current spot market price for given plan in given facility.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.GetSpotMarketRequestResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetSpotMarketRequestResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">device_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetSpotMarketRequestResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSpotMarketRequest.</p>
<dl class="py attribute">
<dt id="pulumi_packet.GetSpotMarketRequestResult.device_ids">
<code class="sig-name descname">device_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetSpotMarketRequestResult.device_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IDs of devices spawned by the referenced Spot Market Request</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetSpotMarketRequestResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetSpotMarketRequestResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.GetVolumeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetVolumeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">billing_cycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetVolumeResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVolume.</p>
<dl class="py attribute">
<dt id="pulumi_packet.GetVolumeResult.billing_cycle">
<code class="sig-name descname">billing_cycle</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetVolumeResult.billing_cycle" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing cycle, defaults to hourly</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetVolumeResult.device_ids">
<code class="sig-name descname">device_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetVolumeResult.device_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>UUIDs of devices to which this volume is attached</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetVolumeResult.facility">
<code class="sig-name descname">facility</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetVolumeResult.facility" title="Permalink to this definition">¶</a></dt>
<dd><p>The facility slug the volume resides in</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetVolumeResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetVolumeResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetVolumeResult.locked">
<code class="sig-name descname">locked</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetVolumeResult.locked" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the volume is locked or not</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetVolumeResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetVolumeResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the volume</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> - The project id the volume is in</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetVolumeResult.plan">
<code class="sig-name descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetVolumeResult.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Performance plan the volume is on</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetVolumeResult.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetVolumeResult.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size in GB of the volume</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.GetVolumeResult.state">
<code class="sig-name descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.GetVolumeResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the volume</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.IpAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">IpAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_notation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.IpAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to attach elastic IP subnets to devices.</p>
<p>To attach an IP subnet from a reserved block to a provisioned device, you must derive a subnet CIDR belonging to
one of your reserved blocks in the same project and facility as the target device.</p>
<p>For example, you have reserved IPv4 address block 147.229.10.152/30, you can choose to assign either the whole
block as one subnet to a device; or 2 subnets with CIDRs 147.229.10.152/31’ and 147.229.10.154/31; or 4 subnets
with mask prefix length 32. More about the elastic IP subnets is <a class="reference external" href="https://www.packet.com/developers/docs/network/basic/elastic-ips/">here</a>.</p>
<p>Device and reserved block must be in the same facility.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidr_notation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CIDR notation of subnet from block reserved in the same
project and facility as the device</p></li>
<li><p><strong>device_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of device to which to assign the subnet</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_packet.IpAttachment.address_family">
<code class="sig-name descname">address_family</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.IpAttachment.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p>Address family as integer (4 or 6)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.IpAttachment.cidr">
<code class="sig-name descname">cidr</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.IpAttachment.cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>length of CIDR prefix of the subnet as integer</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.IpAttachment.cidr_notation">
<code class="sig-name descname">cidr_notation</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.IpAttachment.cidr_notation" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR notation of subnet from block reserved in the same
project and facility as the device</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.IpAttachment.device_id">
<code class="sig-name descname">device_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.IpAttachment.device_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of device to which to assign the subnet</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.IpAttachment.gateway">
<code class="sig-name descname">gateway</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.IpAttachment.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address of gateway for the subnet</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.IpAttachment.netmask">
<code class="sig-name descname">netmask</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.IpAttachment.netmask" title="Permalink to this definition">¶</a></dt>
<dd><p>Subnet mask in decimal notation, e.g. “255.255.255.0”</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.IpAttachment.network">
<code class="sig-name descname">network</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.IpAttachment.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Subnet network address</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.IpAttachment.public">
<code class="sig-name descname">public</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.IpAttachment.public" title="Permalink to this definition">¶</a></dt>
<dd><p>boolean flag whether subnet is reachable from the Internet</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.IpAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_notation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">manageable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">management</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">netmask</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.IpAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IpAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Address family as integer (4 or 6)</p></li>
<li><p><strong>cidr</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – length of CIDR prefix of the subnet as integer</p></li>
<li><p><strong>cidr_notation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CIDR notation of subnet from block reserved in the same
project and facility as the device</p></li>
<li><p><strong>device_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of device to which to assign the subnet</p></li>
<li><p><strong>gateway</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP address of gateway for the subnet</p></li>
<li><p><strong>netmask</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subnet mask in decimal notation, e.g. “255.255.255.0”</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subnet network address</p></li>
<li><p><strong>public</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – boolean flag whether subnet is reachable from the Internet</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.IpAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.IpAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.IpAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.IpAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Organization">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">Organization</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logo</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">twitter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">website</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Organization" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage organization resource in Packet.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description string.</p></li>
<li><p><strong>logo</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Logo URL.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Organization.</p></li>
<li><p><strong>twitter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Twitter handle.</p></li>
<li><p><strong>website</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Website link.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_packet.Organization.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Organization.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description string.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Organization.logo">
<code class="sig-name descname">logo</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Organization.logo" title="Permalink to this definition">¶</a></dt>
<dd><p>Logo URL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Organization.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Organization.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Organization.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Organization.twitter">
<code class="sig-name descname">twitter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Organization.twitter" title="Permalink to this definition">¶</a></dt>
<dd><p>Twitter handle.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Organization.website">
<code class="sig-name descname">website</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Organization.website" title="Permalink to this definition">¶</a></dt>
<dd><p>Website link.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Organization.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logo</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">twitter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">website</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Organization.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Organization resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description string.</p></li>
<li><p><strong>logo</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Logo URL.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Organization.</p></li>
<li><p><strong>twitter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Twitter handle.</p></li>
<li><p><strong>website</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Website link.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Organization.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Organization.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Organization.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Organization.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.PortVlanAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">PortVlanAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_bond</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">native</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vlan_vnid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.PortVlanAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to attach device ports to VLANs.</p>
<p>Device and VLAN must be in the same facility.</p>
<p>If you need this resource to add the port back to bond on removal, set <code class="docutils literal notranslate"><span class="pre">force_bond</span> <span class="pre">=</span> <span class="pre">true</span></code>.</p>
<p>To learn more about Layer 2 networking in Packet, refer to</p>
<ul class="simple">
<li><p><a class="reference external" href="https://www.packet.com/resources/guides/layer-2-configurations/">https://www.packet.com/resources/guides/layer-2-configurations/</a></p></li>
<li><p><a class="reference external" href="https://www.packet.com/developers/docs/network/advanced/layer-2/">https://www.packet.com/developers/docs/network/advanced/layer-2/</a></p></li>
</ul>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> - UUID of device port used in the assignment</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vlan_id</span></code> - UUID of VLAN API resource</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port_id</span></code> - UUID of device port</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>device_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of device to be assigned to the VLAN</p></li>
<li><p><strong>force_bond</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Add port back to the bond when this resource is removed. Default is false.</p></li>
<li><p><strong>native</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Mark this VLAN a native VLAN on the port. This can be used only if this assignment assigns second or further VLAN to the port. To ensure that this attachment is not first on a port, you can use <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> pointing to another packet_port_vlan_attachment, just like in the layer2-individual example above.</p></li>
<li><p><strong>port_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of network port to be assigned to the VLAN</p></li>
<li><p><strong>vlan_vnid</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – VXLAN Network Identifier, integer</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_packet.PortVlanAttachment.device_id">
<code class="sig-name descname">device_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.device_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of device to be assigned to the VLAN</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.PortVlanAttachment.force_bond">
<code class="sig-name descname">force_bond</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.force_bond" title="Permalink to this definition">¶</a></dt>
<dd><p>Add port back to the bond when this resource is removed. Default is false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.PortVlanAttachment.native">
<code class="sig-name descname">native</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.native" title="Permalink to this definition">¶</a></dt>
<dd><p>Mark this VLAN a native VLAN on the port. This can be used only if this assignment assigns second or further VLAN to the port. To ensure that this attachment is not first on a port, you can use <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> pointing to another packet_port_vlan_attachment, just like in the layer2-individual example above.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.PortVlanAttachment.port_name">
<code class="sig-name descname">port_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.port_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of network port to be assigned to the VLAN</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.PortVlanAttachment.vlan_vnid">
<code class="sig-name descname">vlan_vnid</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.vlan_vnid" title="Permalink to this definition">¶</a></dt>
<dd><p>VXLAN Network Identifier, integer</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.PortVlanAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_bond</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">native</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vlan_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vlan_vnid</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PortVlanAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>device_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of device to be assigned to the VLAN</p></li>
<li><p><strong>force_bond</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Add port back to the bond when this resource is removed. Default is false.</p></li>
<li><p><strong>native</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Mark this VLAN a native VLAN on the port. This can be used only if this assignment assigns second or further VLAN to the port. To ensure that this attachment is not first on a port, you can use <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> pointing to another packet_port_vlan_attachment, just like in the layer2-individual example above.</p></li>
<li><p><strong>port_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of network port to be assigned to the VLAN</p></li>
<li><p><strong>vlan_vnid</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – VXLAN Network Identifier, integer</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.PortVlanAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.PortVlanAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Project">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">Project</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend_transfer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">payment_method_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet project resource to allow you manage devices
in your projects.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_transfer</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable <a class="reference external" href="https://www.packet.com/developers/docs/network/basic/backend-transfer/">Backend Transfer</a>, default is false</p></li>
<li><p><strong>bgp_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Optional BGP settings. Refer to <a class="reference external" href="https://www.packet.com/developers/docs/network/advanced/local-and-global-bgp/">Packet guide for BGP</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project</p></li>
<li><p><strong>organization_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of organization under which you want to create the project. If you leave it out, the project will be create under your the default organization of your account.</p></li>
<li><p><strong>payment_method_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of payment method for this project. The payment method and the project need to belong to the same organization (passed with <code class="docutils literal notranslate"><span class="pre">organization_id</span></code>, or default).</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bgp_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">asn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Autonomous System Numer for local BGP deployment</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deploymentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <code class="docutils literal notranslate"><span class="pre">private</span></code> or <code class="docutils literal notranslate"><span class="pre">public</span></code>, the <code class="docutils literal notranslate"><span class="pre">private</span></code> is likely to be usable immediately, the <code class="docutils literal notranslate"><span class="pre">public</span></code> will need to be review by Packet engineers</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of route filters allowed per server</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">md5</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Password for BGP session in plaintext (not a checksum)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - status of BGP configuration in the project</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_packet.Project.backend_transfer">
<code class="sig-name descname">backend_transfer</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.backend_transfer" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable <a class="reference external" href="https://www.packet.com/developers/docs/network/basic/backend-transfer/">Backend Transfer</a>, default is false</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Project.bgp_config">
<code class="sig-name descname">bgp_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.bgp_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional BGP settings. Refer to <a class="reference external" href="https://www.packet.com/developers/docs/network/advanced/local-and-global-bgp/">Packet guide for BGP</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">asn</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Autonomous System Numer for local BGP deployment</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deploymentType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - <code class="docutils literal notranslate"><span class="pre">private</span></code> or <code class="docutils literal notranslate"><span class="pre">public</span></code>, the <code class="docutils literal notranslate"><span class="pre">private</span></code> is likely to be usable immediately, the <code class="docutils literal notranslate"><span class="pre">public</span></code> will need to be review by Packet engineers</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of route filters allowed per server</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">md5</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Password for BGP session in plaintext (not a checksum)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - status of BGP configuration in the project</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Project.created">
<code class="sig-name descname">created</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the project was created</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Project.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the project</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Project.organization_id">
<code class="sig-name descname">organization_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.organization_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of organization under which you want to create the project. If you leave it out, the project will be create under your the default organization of your account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Project.payment_method_id">
<code class="sig-name descname">payment_method_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.payment_method_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of payment method for this project. The payment method and the project need to belong to the same organization (passed with <code class="docutils literal notranslate"><span class="pre">organization_id</span></code>, or default).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Project.updated">
<code class="sig-name descname">updated</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Project.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the project was updated</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Project.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend_transfer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">payment_method_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Project.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Project resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_transfer</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Enable or disable <a class="reference external" href="https://www.packet.com/developers/docs/network/basic/backend-transfer/">Backend Transfer</a>, default is false</p>
</p></li>
<li><p><strong>bgp_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Optional BGP settings. Refer to <a class="reference external" href="https://www.packet.com/developers/docs/network/advanced/local-and-global-bgp/">Packet guide for BGP</a>.</p>
</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timestamp for when the project was created</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project</p></li>
<li><p><strong>organization_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of organization under which you want to create the project. If you leave it out, the project will be create under your the default organization of your account.</p></li>
<li><p><strong>payment_method_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of payment method for this project. The payment method and the project need to belong to the same organization (passed with <code class="docutils literal notranslate"><span class="pre">organization_id</span></code>, or default).</p></li>
<li><p><strong>updated</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timestamp for the last time the project was updated</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bgp_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">asn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Autonomous System Numer for local BGP deployment</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">deploymentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - <code class="docutils literal notranslate"><span class="pre">private</span></code> or <code class="docutils literal notranslate"><span class="pre">public</span></code>, the <code class="docutils literal notranslate"><span class="pre">private</span></code> is likely to be usable immediately, the <code class="docutils literal notranslate"><span class="pre">public</span></code> will need to be review by Packet engineers</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of route filters allowed per server</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">md5</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Password for BGP session in plaintext (not a checksum)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - status of BGP configuration in the project</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Project.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Project.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.ProjectSshKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">ProjectSshKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.ProjectSshKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet project SSH key resource to manage project-specific SSH keys.
Project SSH keys will only be populated onto servers that belong to that project, in contrast to User SSH Keys.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SSH key for identification</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of parent project</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key. If this is a file, it can be read using the file interpolation function</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_packet.ProjectSshKey.created">
<code class="sig-name descname">created</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ProjectSshKey.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the SSH key was created</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.ProjectSshKey.fingerprint">
<code class="sig-name descname">fingerprint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ProjectSshKey.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the SSH key</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.ProjectSshKey.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ProjectSshKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SSH key for identification</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.ProjectSshKey.owner_id">
<code class="sig-name descname">owner_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ProjectSshKey.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of parent project (same as project_id)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.ProjectSshKey.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ProjectSshKey.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of parent project</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.ProjectSshKey.public_key">
<code class="sig-name descname">public_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ProjectSshKey.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key. If this is a file, it can be read using the file interpolation function</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.ProjectSshKey.updated">
<code class="sig-name descname">updated</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ProjectSshKey.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the SSH key was updated</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ProjectSshKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.ProjectSshKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectSshKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timestamp for when the SSH key was created</p></li>
<li><p><strong>fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fingerprint of the SSH key</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SSH key for identification</p></li>
<li><p><strong>owner_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of parent project (same as project_id)</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of parent project</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key. If this is a file, it can be read using the file interpolation function</p></li>
<li><p><strong>updated</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timestamp for the last time the SSH key was updated</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ProjectSshKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.ProjectSshKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.ProjectSshKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.ProjectSshKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the packet package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API auth key for API operations.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_packet.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.ReservedIpBlock">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">ReservedIpBlock</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quantity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.ReservedIpBlock" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create and manage blocks of reserved IP addresses in a project.</p>
<p>When a user provisions first device in a facility, Packet API automatically allocates IPv6/56 and private IPv4/25 blocks.
The new device then gets IPv6 and private IPv4 addresses from those block. It also gets a public IPv4/31 address.
Every new device in the project and facility will automatically get IPv6 and private IPv4 addresses from these pre-allocated blocks.
The IPv6 and private IPv4 blocks can’t be created, only imported. With this resource, it’s possible to create either public IPv4 blocks or global IPv4 blocks.</p>
<p>Public blocks are allocated in a facility. Addresses from public blocks can only be assigned to devices in the facility. Public blocks can have mask from /24 (256 addresses) to /32 (1 address). If you create public block with this resource, you must fill the facility argmument.</p>
<p>Addresses from global blocks can be assigned in any facility. Global blocks can have mask from /30 (4 addresses), to /32 (1 address). If you create global block with this resource, you must specify type = “global_ipv4” and you must omit the facility argument.</p>
<p>Once IP block is allocated or imported, an address from it can be assigned to device with the <code class="docutils literal notranslate"><span class="pre">.IpAttachment</span></code> resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Arbitrary description</p></li>
<li><p><strong>facility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Facility where to allocate the public IP address block, makes sense only for type==public_ipv4, must be empty for type==global_ipv4</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The packet project ID where to allocate the address block</p></li>
<li><p><strong>quantity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of allocated /32 addresses, a power of 2</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Either “global_ipv4” or “public_ipv4”, defaults to “public_ipv4” for backward compatibility</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_packet.ReservedIpBlock.address_family">
<code class="sig-name descname">address_family</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p>Address family as integer (4 or 6)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.ReservedIpBlock.cidr">
<code class="sig-name descname">cidr</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>length of CIDR prefix of the block as integer</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.ReservedIpBlock.cidr_notation">
<code class="sig-name descname">cidr_notation</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.cidr_notation" title="Permalink to this definition">¶</a></dt>
<dd><p>Address and mask in CIDR notation, e.g. “147.229.15.30/31”</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.ReservedIpBlock.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Arbitrary description</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.ReservedIpBlock.facility">
<code class="sig-name descname">facility</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.facility" title="Permalink to this definition">¶</a></dt>
<dd><p>Facility where to allocate the public IP address block, makes sense only for type==public_ipv4, must be empty for type==global_ipv4</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.ReservedIpBlock.global_">
<code class="sig-name descname">global_</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.global_" title="Permalink to this definition">¶</a></dt>
<dd><p>boolean flag whether addresses from a block are global (i.e. can be assigned in any facility)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.ReservedIpBlock.netmask">
<code class="sig-name descname">netmask</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.netmask" title="Permalink to this definition">¶</a></dt>
<dd><p>Mask in decimal notation, e.g. “255.255.255.0”</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.ReservedIpBlock.network">
<code class="sig-name descname">network</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Network IP address portion of the block specification</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.ReservedIpBlock.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The packet project ID where to allocate the address block</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.ReservedIpBlock.public">
<code class="sig-name descname">public</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.public" title="Permalink to this definition">¶</a></dt>
<dd><p>boolean flag whether addresses from a block are public</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.ReservedIpBlock.quantity">
<code class="sig-name descname">quantity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.quantity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of allocated /32 addresses, a power of 2</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.ReservedIpBlock.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Either “global_ipv4” or “public_ipv4”, defaults to “public_ipv4” for backward compatibility</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ReservedIpBlock.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_notation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">manageable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">management</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">netmask</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quantity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ReservedIpBlock resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Address family as integer (4 or 6)</p></li>
<li><p><strong>cidr</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – length of CIDR prefix of the block as integer</p></li>
<li><p><strong>cidr_notation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Address and mask in CIDR notation, e.g. “147.229.15.30/31”</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Arbitrary description</p></li>
<li><p><strong>facility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Facility where to allocate the public IP address block, makes sense only for type==public_ipv4, must be empty for type==global<a href="#id18"><span class="problematic" id="id19">*</span></a>ipv4</p></li>
</ul>
</dd>
</dl>
<p>:param pulumi.Input[bool] global*: boolean flag whether addresses from a block are global (i.e. can be assigned in any facility)
:param pulumi.Input[str] netmask: Mask in decimal notation, e.g. “255.255.255.0”
:param pulumi.Input[str] network: Network IP address portion of the block specification
:param pulumi.Input[str] project_id: The packet project ID where to allocate the address block
:param pulumi.Input[bool] public: boolean flag whether addresses from a block are public
:param pulumi.Input[float] quantity: The number of allocated /32 addresses, a power of 2
:param pulumi.Input[str] type: Either “global_ipv4” or “public_ipv4”, defaults to “public_ipv4” for backward compatibility</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ReservedIpBlock.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.ReservedIpBlock.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.SpotMarketRequest">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">SpotMarketRequest</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">devices_max</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">devices_min</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facilities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_bid_price</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_for_devices</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SpotMarketRequest" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet Spot Market Request resource to allow you to
manage spot market requests on your account. For more detail on Spot Market, see <a class="reference external" href="https://www.packet.com/developers/docs/getting-started/deployment-options/spot-market/">this article in Packing documentaion</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>devices_max</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum number devices to be created</p></li>
<li><p><strong>devices_min</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Miniumum number devices to be created</p></li>
<li><p><strong>facilities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Facility IDs where devices should be created</p></li>
<li><p><strong>instance_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Device parameters. See device resource for details</p></li>
<li><p><strong>max_bid_price</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum price user is willing to pay per hour per device</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project ID</p></li>
<li><p><strong>wait_for_devices</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed</p></li>
</ul>
</dd>
</dl>
<p>The <strong>instance_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">always_pxe</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">billing_cycle</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">features</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">locked</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operating_system</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">plan</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectSshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">termintationTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userSshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userdata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_packet.SpotMarketRequest.devices_max">
<code class="sig-name descname">devices_max</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.devices_max" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum number devices to be created</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.SpotMarketRequest.devices_min">
<code class="sig-name descname">devices_min</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.devices_min" title="Permalink to this definition">¶</a></dt>
<dd><p>Miniumum number devices to be created</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.SpotMarketRequest.facilities">
<code class="sig-name descname">facilities</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.facilities" title="Permalink to this definition">¶</a></dt>
<dd><p>Facility IDs where devices should be created</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.SpotMarketRequest.instance_parameters">
<code class="sig-name descname">instance_parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.instance_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Device parameters. See device resource for details</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">always_pxe</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">billing_cycle</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">features</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">locked</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operating_system</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">plan</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectSshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">termintationTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userSshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userdata</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.SpotMarketRequest.max_bid_price">
<code class="sig-name descname">max_bid_price</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.max_bid_price" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum price user is willing to pay per hour per device</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.SpotMarketRequest.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Project ID</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.SpotMarketRequest.wait_for_devices">
<code class="sig-name descname">wait_for_devices</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.wait_for_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.SpotMarketRequest.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">devices_max</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">devices_min</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facilities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_bid_price</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_for_devices</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SpotMarketRequest resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>devices_max</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum number devices to be created</p></li>
<li><p><strong>devices_min</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Miniumum number devices to be created</p></li>
<li><p><strong>facilities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Facility IDs where devices should be created</p></li>
<li><p><strong>instance_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Device parameters. See device resource for details</p></li>
<li><p><strong>max_bid_price</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum price user is willing to pay per hour per device</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project ID</p></li>
<li><p><strong>wait_for_devices</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed</p></li>
</ul>
</dd>
</dl>
<p>The <strong>instance_parameters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">always_pxe</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">billing_cycle</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">features</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">locked</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operating_system</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">plan</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projectSshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">termintationTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userSshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userdata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.SpotMarketRequest.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.SpotMarketRequest.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.SshKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">SshKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SshKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage User SSH keys on your Packet user account. If you create a new device in a project, all the keys of the project’s collaborators will be injected to the device.</p>
<p>The link between User SSH key and device is implicit. If you want to make sure that a key will be copied to a device, you must ensure that the device resource <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> the key resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SSH key for identification</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key. If this is a file, it
can be read using the file interpolation function</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_packet.SshKey.created">
<code class="sig-name descname">created</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SshKey.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the SSH key was created</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.SshKey.fingerprint">
<code class="sig-name descname">fingerprint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SshKey.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the SSH key</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.SshKey.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SshKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SSH key for identification</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.SshKey.owner_id">
<code class="sig-name descname">owner_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SshKey.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of the Packet API User who owns this key</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.SshKey.public_key">
<code class="sig-name descname">public_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SshKey.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key. If this is a file, it
can be read using the file interpolation function</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.SshKey.updated">
<code class="sig-name descname">updated</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.SshKey.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the SSH key was updated</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.SshKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fingerprint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SshKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SshKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timestamp for when the SSH key was created</p></li>
<li><p><strong>fingerprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fingerprint of the SSH key</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SSH key for identification</p></li>
<li><p><strong>owner_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of the Packet API User who owns this key</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key. If this is a file, it
can be read using the file interpolation function</p></li>
<li><p><strong>updated</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timestamp for the last time the SSH key was updated</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.SshKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SshKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.SshKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SshKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Vlan">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">Vlan</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Vlan" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to allow users to manage Virtual Networks in their projects.</p>
<p>To learn more about Layer 2 networking in Packet, refer to</p>
<ul class="simple">
<li><p><a class="reference external" href="https://www.packet.com/resources/guides/layer-2-configurations/">https://www.packet.com/resources/guides/layer-2-configurations/</a></p></li>
<li><p><a class="reference external" href="https://www.packet.com/developers/docs/network/advanced/layer-2/">https://www.packet.com/developers/docs/network/advanced/layer-2/</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description string</p></li>
<li><p><strong>facility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Facility where to create the VLAN</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of parent project</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_packet.Vlan.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Vlan.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description string</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Vlan.facility">
<code class="sig-name descname">facility</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Vlan.facility" title="Permalink to this definition">¶</a></dt>
<dd><p>Facility where to create the VLAN</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Vlan.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Vlan.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of parent project</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Vlan.vxlan">
<code class="sig-name descname">vxlan</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Vlan.vxlan" title="Permalink to this definition">¶</a></dt>
<dd><p>VXLAN segment ID</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Vlan.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vxlan</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Vlan.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Vlan resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description string</p></li>
<li><p><strong>facility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Facility where to create the VLAN</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of parent project</p></li>
<li><p><strong>vxlan</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – VXLAN segment ID</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Vlan.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Vlan.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Vlan.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Vlan.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Volume">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">Volume</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_cycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Volume resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] billing_cycle: The billing cycle, defaults to “hourly”
:param pulumi.Input[str] description: Optional description for the volume
:param pulumi.Input[str] facility: The facility to create the volume in
:param pulumi.Input[bool] locked: Lock or unlock the volume
:param pulumi.Input[str] plan: The service plan slug of the volume
:param pulumi.Input[str] project_id: The packet project ID to deploy the volume in
:param pulumi.Input[float] size: The size in GB to make the volume
:param pulumi.Input[list] snapshot_policies: Optional list of snapshot policies</p>
<p>The <strong>snapshot_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">snapshotCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshotFrequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_packet.Volume.attachments">
<code class="sig-name descname">attachments</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.attachments" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of attachments, each with it’s own <code class="docutils literal notranslate"><span class="pre">href</span></code> attribute</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">href</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Volume.billing_cycle">
<code class="sig-name descname">billing_cycle</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.billing_cycle" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing cycle, defaults to “hourly”</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Volume.created">
<code class="sig-name descname">created</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the volume was created</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Volume.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional description for the volume</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Volume.facility">
<code class="sig-name descname">facility</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.facility" title="Permalink to this definition">¶</a></dt>
<dd><p>The facility to create the volume in</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Volume.locked">
<code class="sig-name descname">locked</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.locked" title="Permalink to this definition">¶</a></dt>
<dd><p>Lock or unlock the volume</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Volume.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the volume</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Volume.plan">
<code class="sig-name descname">plan</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>The service plan slug of the volume</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Volume.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The packet project ID to deploy the volume in</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Volume.size">
<code class="sig-name descname">size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size in GB to make the volume</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Volume.snapshot_policies">
<code class="sig-name descname">snapshot_policies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.snapshot_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional list of snapshot policies</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">snapshotCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshotFrequency</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Volume.state">
<code class="sig-name descname">state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the volume</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.Volume.updated">
<code class="sig-name descname">updated</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.Volume.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the volume was updated</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Volume.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attachments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_cycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Volume.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Volume resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attachments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of attachments, each with it’s own <code class="docutils literal notranslate"><span class="pre">href</span></code> attribute</p></li>
<li><p><strong>billing_cycle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing cycle, defaults to “hourly”</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timestamp for when the volume was created</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Optional description for the volume</p></li>
<li><p><strong>facility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The facility to create the volume in</p></li>
<li><p><strong>locked</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Lock or unlock the volume</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the volume</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service plan slug of the volume</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The packet project ID to deploy the volume in</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size in GB to make the volume</p></li>
<li><p><strong>snapshot_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Optional list of snapshot policies</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of the volume</p></li>
<li><p><strong>updated</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timestamp for the last time the volume was updated</p></li>
</ul>
</dd>
</dl>
<p>The <strong>attachments</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">href</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>snapshot_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">snapshotCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshotFrequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Volume.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Volume.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.Volume.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Volume.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.VolumeAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">VolumeAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.VolumeAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a VolumeAttachment resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] device_id: The ID of the device to which the volume should be attached
:param pulumi.Input[str] volume_id: The ID of the volume to attach</p>
<dl class="py attribute">
<dt id="pulumi_packet.VolumeAttachment.device_id">
<code class="sig-name descname">device_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.VolumeAttachment.device_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the device to which the volume should be attached</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_packet.VolumeAttachment.volume_id">
<code class="sig-name descname">volume_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_packet.VolumeAttachment.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the volume to attach</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.VolumeAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.VolumeAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VolumeAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>device_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the device to which the volume should be attached</p></li>
<li><p><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the volume to attach</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.VolumeAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.VolumeAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.VolumeAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.VolumeAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_packet.get_device">
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_device</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">device_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.get_device" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet device datasource.</p>
<blockquote>
<div><dl class="simple">
<dt><strong>Note:</strong> All arguments including the <code class="docutils literal notranslate"><span class="pre">root_password</span></code> and <code class="docutils literal notranslate"><span class="pre">user_data</span></code> will be stored in</dt><dd><p>the raw state as plain-text.</p>
</dd>
</dl>
<p><a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>device_id</strong> (<em>str</em>) – Device ID</p></li>
<li><p><strong>hostname</strong> (<em>str</em>) – The device name</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The id of the project in which the devices exists</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_packet.get_ip_block_ranges">
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_ip_block_ranges</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.get_ip_block_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this datasource to get CIDR expressions for allocated IP blocks of all the types in a project, optionally filtered by facility.</p>
<p>There are four types of IP blocks in Packet: global IPv4, public IPv4, private IPv4 and IPv6. Both global and public IPv4 are routable from the Internet. Public IPv4 block is allocated in a facility, and addresses from it can only be assigned to devices in that facility. Addresses from Global IPv4 block can be assigned to a device in any facility.</p>
<p>The datasource has 4 list attributes: <code class="docutils literal notranslate"><span class="pre">global_ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">public_ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">private_ipv4</span></code> and <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>, each listing CIDR notation (<code class="docutils literal notranslate"><span class="pre">&lt;network&gt;/&lt;mask&gt;</span></code>) of respective blocks from the project.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>facility</strong> (<em>str</em>) – Facility code filtering the IP blocks. Global IPv4 blcoks will be listed anyway. If you omit this, all the block from the project will be listed.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – ID of the project from which to list the blocks.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_packet.get_operating_system">
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_operating_system</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">distro</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisionable_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.get_operating_system" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get Packet Operating System image.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>distro</strong> (<em>str</em>) – Name of the OS distribution.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Name or part of the name of the distribution. Case insensitive.</p></li>
<li><p><strong>provisionable_on</strong> (<em>str</em>) – Plan name.</p></li>
<li><p><strong>version</strong> (<em>str</em>) – Version of the distribution</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_packet.get_organization">
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_organization</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.get_organization" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet organization datasource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The organization name</p></li>
<li><p><strong>organization_id</strong> (<em>str</em>) – The UUID of the organization resource</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_packet.get_precreated_ip_block">
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_precreated_ip_block</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.get_precreated_ip_block" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get CIDR expression for precreated IPv6 and IPv4 blocks in Packet.
You can then use the cidrsubnet TF builtin function to derive subnets.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>address*family</strong> (<em>float</em>) – <p>4 or 6, depending on which block you are looking for.</p>
</p></li>
<li><p><strong>facility</strong> (<em>str</em>) – Facility of the searched block. (Optional) Only allowed for non-global blocks.</p></li>
</ul>
</dd>
</dl>
<p>:param bool global*: Whether to look for global block. Default is false for backward compatibility.
:param str project_id: ID of the project where the searched block should be.
:param bool public: Whether to look for public or private block.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_packet.get_project">
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_project</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.get_project" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this datasource to retrieve attributes of the Project API resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name which is used to look up the project</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The UUID by which to look up the project</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_packet.get_spot_market_price">
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_spot_market_price</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.get_spot_market_price" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get Packet Spot Market Price.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>facility</strong> (<em>str</em>) – Name of the facility.</p></li>
<li><p><strong>plan</strong> (<em>str</em>) – Name of the plan.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_packet.get_spot_market_request">
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_spot_market_request</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">request_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.get_spot_market_request" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet spot_market_request datasource. The datasource will contain list of device IDs created by referenced Spot Market Request.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>request_id</strong> (<em>str</em>) – The id of the Spot Market Request</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_packet.get_volume">
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_volume</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.get_volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet Block Storage Volume datasource to allow you to read existing volumes.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Name of volume for lookup</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The ID the parent Packet project (for lookup by name)</p></li>
<li><p><strong>volume_id</strong> (<em>str</em>) – ID of volume for lookup</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
