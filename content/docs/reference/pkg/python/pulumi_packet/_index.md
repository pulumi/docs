---
title: Package pulumi_packet
title_tag: Package pulumi_packet | Python SDK
linktitle: pulumi_packet
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "packet" >}}

<div class="section" id="pulumi-packet">
<h1>Pulumi Packet<a class="headerlink" href="#pulumi-packet" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-packet/issues">pulumi/pulumi-packet repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-packet/issues">terraform-providers/terraform-provider-packet repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_packet"></span><dl class="py class">
<dt id="pulumi_packet.AwaitableGetDeviceBgpNeighborsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">AwaitableGetDeviceBgpNeighborsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">bgp_neighbors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.AwaitableGetDeviceBgpNeighborsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_packet.AwaitableGetDeviceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">AwaitableGetDeviceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_private_ipv4</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_public_ipv4</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_public_ipv6</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">always_pxe</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_cycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hardware_reservation_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipxe_script_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">operating_system</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_key_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.AwaitableGetDeviceResult" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">BgpSession</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_route</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.BgpSession" title="Permalink to this definition">¶</a></dt>
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
<dl class="py method">
<dt id="pulumi_packet.BgpSession.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_route</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.bgp_session.BgpSession<a class="headerlink" href="#pulumi_packet.BgpSession.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BgpSession resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code></p></li>
<li><p><strong>default_route</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to set the default route policy. False by default.</p></li>
<li><p><strong>device_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of device</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.BgpSession.address_family">
<em class="property">property </em><code class="sig-name descname">address_family</code><a class="headerlink" href="#pulumi_packet.BgpSession.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.BgpSession.default_route">
<em class="property">property </em><code class="sig-name descname">default_route</code><a class="headerlink" href="#pulumi_packet.BgpSession.default_route" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to set the default route policy. False by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.BgpSession.device_id">
<em class="property">property </em><code class="sig-name descname">device_id</code><a class="headerlink" href="#pulumi_packet.BgpSession.device_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of device</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">Device</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">always_pxe</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_cycle</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facilities</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_detach_volumes</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hardware_reservation_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_addresses</span><span class="p">:</span> <span class="n">Union[List[Union[DeviceIpAddressArgs, Mapping[str, Any], Awaitable[Union[DeviceIpAddressArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[DeviceIpAddressArgs, Mapping[str, Any], Awaitable[Union[DeviceIpAddressArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipxe_script_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">operating_system</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_ssh_key_ids</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_for_reservation_deprovision</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Device" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet device resource. This can be used to create,
modify, and delete devices.</p>
<blockquote>
<div><dl class="simple">
<dt><strong>Note:</strong> All arguments including the <code class="docutils literal notranslate"><span class="pre">root_password</span></code> and <code class="docutils literal notranslate"><span class="pre">user_data</span></code> will be stored in</dt><dd><p>the raw state as plain-text.</p>
</dd>
</dl>
<p><a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<p>Create a device and add it to cool_project</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_packet</span> <span class="k">as</span> <span class="nn">packet</span>

<span class="n">web1</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">Device</span><span class="p">(</span><span class="s2">&quot;web1&quot;</span><span class="p">,</span>
    <span class="n">hostname</span><span class="o">=</span><span class="s2">&quot;tf.coreos2&quot;</span><span class="p">,</span>
    <span class="n">plan</span><span class="o">=</span><span class="s2">&quot;t1.small.x86&quot;</span><span class="p">,</span>
    <span class="n">facilities</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;ewr1&quot;</span><span class="p">],</span>
    <span class="n">operating_system</span><span class="o">=</span><span class="s2">&quot;coreos_stable&quot;</span><span class="p">,</span>
    <span class="n">billing_cycle</span><span class="o">=</span><span class="s2">&quot;hourly&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">local</span><span class="p">[</span><span class="s2">&quot;project_id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>Same as above, but boot via iPXE initially, using the Ignition Provider for provisioning</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_packet</span> <span class="k">as</span> <span class="nn">packet</span>

<span class="n">pxe1</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">Device</span><span class="p">(</span><span class="s2">&quot;pxe1&quot;</span><span class="p">,</span>
    <span class="n">hostname</span><span class="o">=</span><span class="s2">&quot;tf.coreos2-pxe&quot;</span><span class="p">,</span>
    <span class="n">plan</span><span class="o">=</span><span class="s2">&quot;t1.small.x86&quot;</span><span class="p">,</span>
    <span class="n">facilities</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;ewr1&quot;</span><span class="p">],</span>
    <span class="n">operating_system</span><span class="o">=</span><span class="s2">&quot;custom_ipxe&quot;</span><span class="p">,</span>
    <span class="n">billing_cycle</span><span class="o">=</span><span class="s2">&quot;hourly&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">local</span><span class="p">[</span><span class="s2">&quot;project_id&quot;</span><span class="p">],</span>
    <span class="n">ipxe_script_url</span><span class="o">=</span><span class="s2">&quot;https://rawgit.com/cloudnativelabs/pxe/master/packet/coreos-stable-packet.ipxe&quot;</span><span class="p">,</span>
    <span class="n">always_pxe</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">user_data</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;ignition_config&quot;</span><span class="p">][</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;rendered&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>Create a device without a public IP address, with only a /30 private IPv4 subnet (4 IP addresses)</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_packet</span> <span class="k">as</span> <span class="nn">packet</span>

<span class="n">web1</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">Device</span><span class="p">(</span><span class="s2">&quot;web1&quot;</span><span class="p">,</span>
    <span class="n">hostname</span><span class="o">=</span><span class="s2">&quot;tf.coreos2&quot;</span><span class="p">,</span>
    <span class="n">plan</span><span class="o">=</span><span class="s2">&quot;t1.small.x86&quot;</span><span class="p">,</span>
    <span class="n">facilities</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;ewr1&quot;</span><span class="p">],</span>
    <span class="n">operating_system</span><span class="o">=</span><span class="s2">&quot;coreos_stable&quot;</span><span class="p">,</span>
    <span class="n">billing_cycle</span><span class="o">=</span><span class="s2">&quot;hourly&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">local</span><span class="p">[</span><span class="s2">&quot;project_id&quot;</span><span class="p">],</span>
    <span class="n">ip_addresses</span><span class="o">=</span><span class="p">[</span><span class="n">packet</span><span class="o">.</span><span class="n">DeviceIpAddressArgs</span><span class="p">(</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;private_ipv4&quot;</span><span class="p">,</span>
        <span class="n">cidr</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span>
    <span class="p">)])</span>
</pre></div>
</div>
<p>Deploy device on next-available reserved hardware and do custom partitioning.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_packet</span> <span class="k">as</span> <span class="nn">packet</span>

<span class="n">web1</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">Device</span><span class="p">(</span><span class="s2">&quot;web1&quot;</span><span class="p">,</span>
    <span class="n">hostname</span><span class="o">=</span><span class="s2">&quot;tftest&quot;</span><span class="p">,</span>
    <span class="n">plan</span><span class="o">=</span><span class="s2">&quot;t1.small.x86&quot;</span><span class="p">,</span>
    <span class="n">facilities</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;sjc1&quot;</span><span class="p">],</span>
    <span class="n">operating_system</span><span class="o">=</span><span class="s2">&quot;ubuntu_16_04&quot;</span><span class="p">,</span>
    <span class="n">billing_cycle</span><span class="o">=</span><span class="s2">&quot;hourly&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">local</span><span class="p">[</span><span class="s2">&quot;project_id&quot;</span><span class="p">],</span>
    <span class="n">hardware_reservation_id</span><span class="o">=</span><span class="s2">&quot;next-available&quot;</span><span class="p">,</span>
    <span class="n">storage</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">  &quot;disks&quot;: [</span>
<span class="s2">    {</span>
<span class="s2">      &quot;device&quot;: &quot;/dev/sda&quot;,</span>
<span class="s2">      &quot;wipeTable&quot;: true,</span>
<span class="s2">      &quot;partitions&quot;: [</span>
<span class="s2">        {</span>
<span class="s2">          &quot;label&quot;: &quot;BIOS&quot;,</span>
<span class="s2">          &quot;number&quot;: 1,</span>
<span class="s2">          &quot;size&quot;: &quot;4096&quot;</span>
<span class="s2">        },</span>
<span class="s2">        {</span>
<span class="s2">          &quot;label&quot;: &quot;SWAP&quot;,</span>
<span class="s2">          &quot;number&quot;: 2,</span>
<span class="s2">          &quot;size&quot;: &quot;3993600&quot;</span>
<span class="s2">        },</span>
<span class="s2">        {</span>
<span class="s2">          &quot;label&quot;: &quot;ROOT&quot;,</span>
<span class="s2">          &quot;number&quot;: 3,</span>
<span class="s2">          &quot;size&quot;: &quot;0&quot;</span>
<span class="s2">        }</span>
<span class="s2">      ]</span>
<span class="s2">    }</span>
<span class="s2">  ],</span>
<span class="s2">  &quot;filesystems&quot;: [</span>
<span class="s2">    {</span>
<span class="s2">      &quot;mount&quot;: {</span>
<span class="s2">        &quot;device&quot;: &quot;/dev/sda3&quot;,</span>
<span class="s2">        &quot;format&quot;: &quot;ext4&quot;,</span>
<span class="s2">        &quot;point&quot;: &quot;/&quot;,</span>
<span class="s2">        &quot;create&quot;: {</span>
<span class="s2">          &quot;options&quot;: [</span>
<span class="s2">            &quot;-L&quot;,</span>
<span class="s2">            &quot;ROOT&quot;</span>
<span class="s2">          ]</span>
<span class="s2">        }</span>
<span class="s2">      }</span>
<span class="s2">    },</span>
<span class="s2">    {</span>
<span class="s2">      &quot;mount&quot;: {</span>
<span class="s2">        &quot;device&quot;: &quot;/dev/sda2&quot;,</span>
<span class="s2">        &quot;format&quot;: &quot;swap&quot;,</span>
<span class="s2">        &quot;point&quot;: &quot;none&quot;,</span>
<span class="s2">        &quot;create&quot;: {</span>
<span class="s2">          &quot;options&quot;: [</span>
<span class="s2">            &quot;-L&quot;,</span>
<span class="s2">            &quot;SWAP&quot;</span>
<span class="s2">          ]</span>
<span class="s2">        }</span>
<span class="s2">      }</span>
<span class="s2">    }</span>
<span class="s2">  ]</span>
<span class="s2">}</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>always_pxe</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, a device with OS <code class="docutils literal notranslate"><span class="pre">custom_ipxe</span></code> will
continue to boot via iPXE on reboots.</p></li>
<li><p><strong>billing_cycle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – monthly or hourly</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description string for the device</p></li>
<li><p><strong>facilities</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of facility codes with deployment preferences. Packet API will go through the list and will deploy your device to first facility with free capacity. List items must be facility codes or <code class="docutils literal notranslate"><span class="pre">any</span></code> (a wildcard). To find the facility code, visit <a class="reference external" href="https://www.packet.com/developers/api/facilities">Facilities API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</p></li>
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
<li><p><strong>ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DeviceIpAddressArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of IP address types for the device (structure is documented below).</p></li>
<li><p><strong>ipxe_script_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL pointing to a hosted iPXE script. More
information is in the
<a class="reference external" href="https://www.packet.com/developers/docs/servers/operating-systems/custom-ipxe/">Custom iPXE</a>
doc.</p></li>
<li><p><strong>operating_system</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operating system slug. To find the slug, or visit <a class="reference external" href="https://www.packet.com/developers/api/operatingsystems">Operating Systems API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The device plan slug. To find the plan slug, visit <a class="reference external" href="https://www.packet.com/developers/api/plans">Device plans API docs</a>, set your auth token in the top of the page and see JSON from the API response.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which to create the device</p></li>
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
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Tags attached to the device</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string of the desired User Data for the device.</p></li>
<li><p><strong>wait_for_reservation_deprovision</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Only used for devices in reserved hardware. If set, the deletion of this device will block until the hardware reservation is marked provisionable (about 4 minutes in August 2019).</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_packet.Device.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_private_ipv4</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_public_ipv4</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_public_ipv6</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">always_pxe</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_cycle</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deployed_facility</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facilities</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_detach_volumes</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hardware_reservation_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_addresses</span><span class="p">:</span> <span class="n">Union[List[Union[DeviceIpAddressArgs, Mapping[str, Any], Awaitable[Union[DeviceIpAddressArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[DeviceIpAddressArgs, Mapping[str, Any], Awaitable[Union[DeviceIpAddressArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipxe_script_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="p">:</span> <span class="n">Union[List[Union[DeviceNetworkArgs, Mapping[str, Any], Awaitable[Union[DeviceNetworkArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[DeviceNetworkArgs, Mapping[str, Any], Awaitable[Union[DeviceNetworkArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">operating_system</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ports</span><span class="p">:</span> <span class="n">Union[List[Union[DevicePortArgs, Mapping[str, Any], Awaitable[Union[DevicePortArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[DevicePortArgs, Mapping[str, Any], Awaitable[Union[DevicePortArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_ssh_key_ids</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_key_ids</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_for_reservation_deprovision</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.device.Device<a class="headerlink" href="#pulumi_packet.Device.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Device resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<li><p><strong>facilities</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – <p>List of facility codes with deployment preferences. Packet API will go through the list and will deploy your device to first facility with free capacity. List items must be facility codes or <code class="docutils literal notranslate"><span class="pre">any</span></code> (a wildcard). To find the facility code, visit <a class="reference external" href="https://www.packet.com/developers/api/facilities">Facilities API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</p>
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
<li><p><strong>ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DeviceIpAddressArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of IP address types for the device (structure is documented below).</p></li>
<li><p><strong>ipxe_script_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>URL pointing to a hosted iPXE script. More
information is in the
<a class="reference external" href="https://www.packet.com/developers/docs/servers/operating-systems/custom-ipxe/">Custom iPXE</a>
doc.</p>
</p></li>
<li><p><strong>locked</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the device is locked</p></li>
<li><p><strong>networks</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DeviceNetworkArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The device’s private and public IP (v4 and v6) network details. When a device is run without any special network configuration, it will have 3 networks:</p></li>
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
<li><p><strong>ports</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DevicePortArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Ports assigned to the device</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which to create the device</p></li>
<li><p><strong>root_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Root password to the server (disabled after 24 hours)</p></li>
<li><p><strong>ssh_key_ids</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of IDs of SSH keys deployed in the device, can be both user and project SSH keys</p></li>
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
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Tags attached to the device</p></li>
<li><p><strong>updated</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timestamp for the last time the device was updated</p></li>
<li><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string of the desired User Data for the device.</p></li>
<li><p><strong>wait_for_reservation_deprovision</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Only used for devices in reserved hardware. If set, the deletion of this device will block until the hardware reservation is marked provisionable (about 4 minutes in August 2019).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.access_private_ipv4">
<em class="property">property </em><code class="sig-name descname">access_private_ipv4</code><a class="headerlink" href="#pulumi_packet.Device.access_private_ipv4" title="Permalink to this definition">¶</a></dt>
<dd><p>The ipv4 private IP assigned to the device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.access_public_ipv4">
<em class="property">property </em><code class="sig-name descname">access_public_ipv4</code><a class="headerlink" href="#pulumi_packet.Device.access_public_ipv4" title="Permalink to this definition">¶</a></dt>
<dd><p>The ipv4 maintenance IP assigned to the device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.access_public_ipv6">
<em class="property">property </em><code class="sig-name descname">access_public_ipv6</code><a class="headerlink" href="#pulumi_packet.Device.access_public_ipv6" title="Permalink to this definition">¶</a></dt>
<dd><p>The ipv6 maintenance IP assigned to the device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.always_pxe">
<em class="property">property </em><code class="sig-name descname">always_pxe</code><a class="headerlink" href="#pulumi_packet.Device.always_pxe" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, a device with OS <code class="docutils literal notranslate"><span class="pre">custom_ipxe</span></code> will
continue to boot via iPXE on reboots.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.billing_cycle">
<em class="property">property </em><code class="sig-name descname">billing_cycle</code><a class="headerlink" href="#pulumi_packet.Device.billing_cycle" title="Permalink to this definition">¶</a></dt>
<dd><p>monthly or hourly</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.created">
<em class="property">property </em><code class="sig-name descname">created</code><a class="headerlink" href="#pulumi_packet.Device.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the device was created</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.deployed_facility">
<em class="property">property </em><code class="sig-name descname">deployed_facility</code><a class="headerlink" href="#pulumi_packet.Device.deployed_facility" title="Permalink to this definition">¶</a></dt>
<dd><p>The facility where the device is deployed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_packet.Device.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description string for the device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.facilities">
<em class="property">property </em><code class="sig-name descname">facilities</code><a class="headerlink" href="#pulumi_packet.Device.facilities" title="Permalink to this definition">¶</a></dt>
<dd><p>List of facility codes with deployment preferences. Packet API will go through the list and will deploy your device to first facility with free capacity. List items must be facility codes or <code class="docutils literal notranslate"><span class="pre">any</span></code> (a wildcard). To find the facility code, visit <a class="reference external" href="https://www.packet.com/developers/api/facilities">Facilities API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.force_detach_volumes">
<em class="property">property </em><code class="sig-name descname">force_detach_volumes</code><a class="headerlink" href="#pulumi_packet.Device.force_detach_volumes" title="Permalink to this definition">¶</a></dt>
<dd><p>Delete device even if it has volumes attached. Only applies for destroy action.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.hardware_reservation_id">
<em class="property">property </em><code class="sig-name descname">hardware_reservation_id</code><a class="headerlink" href="#pulumi_packet.Device.hardware_reservation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of hardware reservation which this device occupies</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code>- The hostname of the device</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.hostname">
<em class="property">property </em><code class="sig-name descname">hostname</code><a class="headerlink" href="#pulumi_packet.Device.hostname" title="Permalink to this definition">¶</a></dt>
<dd><p>The device name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.ip_addresses">
<em class="property">property </em><code class="sig-name descname">ip_addresses</code><a class="headerlink" href="#pulumi_packet.Device.ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IP address types for the device (structure is documented below).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.ipxe_script_url">
<em class="property">property </em><code class="sig-name descname">ipxe_script_url</code><a class="headerlink" href="#pulumi_packet.Device.ipxe_script_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL pointing to a hosted iPXE script. More
information is in the
<a class="reference external" href="https://www.packet.com/developers/docs/servers/operating-systems/custom-ipxe/">Custom iPXE</a>
doc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.locked">
<em class="property">property </em><code class="sig-name descname">locked</code><a class="headerlink" href="#pulumi_packet.Device.locked" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the device is locked</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.networks">
<em class="property">property </em><code class="sig-name descname">networks</code><a class="headerlink" href="#pulumi_packet.Device.networks" title="Permalink to this definition">¶</a></dt>
<dd><p>The device’s private and public IP (v4 and v6) network details. When a device is run without any special network configuration, it will have 3 networks:</p>
<ul class="simple">
<li><p>Public IPv4 at <code class="docutils literal notranslate"><span class="pre">packet_device.name.network.0</span></code></p></li>
<li><p>IPv6 at <code class="docutils literal notranslate"><span class="pre">packet_device.name.network.1</span></code></p></li>
<li><p>Private IPv4 at <code class="docutils literal notranslate"><span class="pre">packet_device.name.network.2</span></code>
Elastic addresses then stack by type - an assigned public IPv4 will go after the management public IPv4 (to index 1), and will then shift the indices of the IPv6 and private IPv4. Assigned private IPv4 will go after the management private IPv4 (to the end of the network list).
The fields of the network attributes are:</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.operating_system">
<em class="property">property </em><code class="sig-name descname">operating_system</code><a class="headerlink" href="#pulumi_packet.Device.operating_system" title="Permalink to this definition">¶</a></dt>
<dd><p>The operating system slug. To find the slug, or visit <a class="reference external" href="https://www.packet.com/developers/api/operatingsystems">Operating Systems API docs</a>, set your API auth token in the top of the page and see JSON from the API response.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.plan">
<em class="property">property </em><code class="sig-name descname">plan</code><a class="headerlink" href="#pulumi_packet.Device.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>The device plan slug. To find the plan slug, visit <a class="reference external" href="https://www.packet.com/developers/api/plans">Device plans API docs</a>, set your auth token in the top of the page and see JSON from the API response.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.ports">
<em class="property">property </em><code class="sig-name descname">ports</code><a class="headerlink" href="#pulumi_packet.Device.ports" title="Permalink to this definition">¶</a></dt>
<dd><p>Ports assigned to the device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_packet.Device.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which to create the device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.root_password">
<em class="property">property </em><code class="sig-name descname">root_password</code><a class="headerlink" href="#pulumi_packet.Device.root_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Root password to the server (disabled after 24 hours)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.ssh_key_ids">
<em class="property">property </em><code class="sig-name descname">ssh_key_ids</code><a class="headerlink" href="#pulumi_packet.Device.ssh_key_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IDs of SSH keys deployed in the device, can be both user and project SSH keys</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_packet.Device.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.storage">
<em class="property">property </em><code class="sig-name descname">storage</code><a class="headerlink" href="#pulumi_packet.Device.storage" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON for custom partitioning. Only usable on reserved hardware. More information in in the <a class="reference external" href="https://www.packet.com/developers/docs/servers/key-features/cpr/">Custom Partitioning and RAID</a> doc.</p>
<ul class="simple">
<li><p>Please note that the disks.partitions.size attribute must be a string, not an integer. It can be a number string, or size notation string, e.g. “4G” or “8M” (for gigabytes and megabytes).</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_packet.Device.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tags attached to the device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.updated">
<em class="property">property </em><code class="sig-name descname">updated</code><a class="headerlink" href="#pulumi_packet.Device.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the device was updated</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.user_data">
<em class="property">property </em><code class="sig-name descname">user_data</code><a class="headerlink" href="#pulumi_packet.Device.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>A string of the desired User Data for the device.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Device.wait_for_reservation_deprovision">
<em class="property">property </em><code class="sig-name descname">wait_for_reservation_deprovision</code><a class="headerlink" href="#pulumi_packet.Device.wait_for_reservation_deprovision" title="Permalink to this definition">¶</a></dt>
<dd><p>Only used for devices in reserved hardware. If set, the deletion of this device will block until the hardware reservation is marked provisionable (about 4 minutes in August 2019).</p>
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
<dt id="pulumi_packet.DeviceNetworkType">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">DeviceNetworkType</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.DeviceNetworkType" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a DeviceNetworkType resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] device_id: The ID of the device on which the network type should be set.
:param pulumi.Input[str] type: Network type to set. Must be one of <code class="docutils literal notranslate"><span class="pre">layer3</span></code>, <code class="docutils literal notranslate"><span class="pre">hybrid</span></code>, <code class="docutils literal notranslate"><span class="pre">layer2-individual</span></code> and <code class="docutils literal notranslate"><span class="pre">layer2-bonded</span></code>.</p>
<dl class="py method">
<dt id="pulumi_packet.DeviceNetworkType.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.device_network_type.DeviceNetworkType<a class="headerlink" href="#pulumi_packet.DeviceNetworkType.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DeviceNetworkType resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>device_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the device on which the network type should be set.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network type to set. Must be one of <code class="docutils literal notranslate"><span class="pre">layer3</span></code>, <code class="docutils literal notranslate"><span class="pre">hybrid</span></code>, <code class="docutils literal notranslate"><span class="pre">layer2-individual</span></code> and <code class="docutils literal notranslate"><span class="pre">layer2-bonded</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.DeviceNetworkType.device_id">
<em class="property">property </em><code class="sig-name descname">device_id</code><a class="headerlink" href="#pulumi_packet.DeviceNetworkType.device_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the device on which the network type should be set.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.DeviceNetworkType.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_packet.DeviceNetworkType.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Network type to set. Must be one of <code class="docutils literal notranslate"><span class="pre">layer3</span></code>, <code class="docutils literal notranslate"><span class="pre">hybrid</span></code>, <code class="docutils literal notranslate"><span class="pre">layer2-individual</span></code> and <code class="docutils literal notranslate"><span class="pre">layer2-bonded</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.DeviceNetworkType.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.DeviceNetworkType.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.DeviceNetworkType.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.DeviceNetworkType.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.GetDeviceBgpNeighborsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetDeviceBgpNeighborsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">bgp_neighbors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetDeviceBgpNeighborsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDeviceBgpNeighbors.</p>
<dl class="py method">
<dt id="pulumi_packet.GetDeviceBgpNeighborsResult.bgp_neighbors">
<em class="property">property </em><code class="sig-name descname">bgp_neighbors</code><a class="headerlink" href="#pulumi_packet.GetDeviceBgpNeighborsResult.bgp_neighbors" title="Permalink to this definition">¶</a></dt>
<dd><p>array of BGP neighbor records with attributes:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetDeviceBgpNeighborsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_packet.GetDeviceBgpNeighborsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.GetDeviceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetDeviceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_private_ipv4</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_public_ipv4</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_public_ipv6</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">always_pxe</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_cycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hardware_reservation_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipxe_script_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">networks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">operating_system</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">root_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_key_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetDeviceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDevice.</p>
<dl class="py method">
<dt id="pulumi_packet.GetDeviceResult.access_private_ipv4">
<em class="property">property </em><code class="sig-name descname">access_private_ipv4</code><a class="headerlink" href="#pulumi_packet.GetDeviceResult.access_private_ipv4" title="Permalink to this definition">¶</a></dt>
<dd><p>The ipv4 private IP assigned to the device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetDeviceResult.access_public_ipv4">
<em class="property">property </em><code class="sig-name descname">access_public_ipv4</code><a class="headerlink" href="#pulumi_packet.GetDeviceResult.access_public_ipv4" title="Permalink to this definition">¶</a></dt>
<dd><p>The ipv4 management IP assigned to the device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetDeviceResult.access_public_ipv6">
<em class="property">property </em><code class="sig-name descname">access_public_ipv6</code><a class="headerlink" href="#pulumi_packet.GetDeviceResult.access_public_ipv6" title="Permalink to this definition">¶</a></dt>
<dd><p>The ipv6 management IP assigned to the device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetDeviceResult.billing_cycle">
<em class="property">property </em><code class="sig-name descname">billing_cycle</code><a class="headerlink" href="#pulumi_packet.GetDeviceResult.billing_cycle" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing cycle of the device (monthly or hourly)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetDeviceResult.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_packet.GetDeviceResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description string for the device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetDeviceResult.facility">
<em class="property">property </em><code class="sig-name descname">facility</code><a class="headerlink" href="#pulumi_packet.GetDeviceResult.facility" title="Permalink to this definition">¶</a></dt>
<dd><p>The facility where the device is deployed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetDeviceResult.hardware_reservation_id">
<em class="property">property </em><code class="sig-name descname">hardware_reservation_id</code><a class="headerlink" href="#pulumi_packet.GetDeviceResult.hardware_reservation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of hardware reservation which this device occupies</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetDeviceResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_packet.GetDeviceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetDeviceResult.network_type">
<em class="property">property </em><code class="sig-name descname">network_type</code><a class="headerlink" href="#pulumi_packet.GetDeviceResult.network_type" title="Permalink to this definition">¶</a></dt>
<dd><p>L2 network type of the device, one of “layer3”, “layer2-bonded”, “layer2-individual”, “hybrid”</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetDeviceResult.networks">
<em class="property">property </em><code class="sig-name descname">networks</code><a class="headerlink" href="#pulumi_packet.GetDeviceResult.networks" title="Permalink to this definition">¶</a></dt>
<dd><p>The device’s private and public IP (v4 and v6) network details. When a device is run without any special network configuration, it will have 3 networks:</p>
<ul class="simple">
<li><p>Public IPv4 at <code class="docutils literal notranslate"><span class="pre">packet_device.name.network.0</span></code></p></li>
<li><p>IPv6 at <code class="docutils literal notranslate"><span class="pre">packet_device.name.network.1</span></code></p></li>
<li><p>Private IPv4 at <code class="docutils literal notranslate"><span class="pre">packet_device.name.network.2</span></code>
Elastic addresses then stack by type - an assigned public IPv4 will go after the management public IPv4 (to index 1), and will then shift the indices of the IPv6 and private IPv4. Assigned private IPv4 will go after the management private IPv4 (to the end of the network list).
The fields of the network attributes are:</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetDeviceResult.operating_system">
<em class="property">property </em><code class="sig-name descname">operating_system</code><a class="headerlink" href="#pulumi_packet.GetDeviceResult.operating_system" title="Permalink to this definition">¶</a></dt>
<dd><p>The operating system running on the device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetDeviceResult.plan">
<em class="property">property </em><code class="sig-name descname">plan</code><a class="headerlink" href="#pulumi_packet.GetDeviceResult.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>The hardware config of the device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetDeviceResult.ports">
<em class="property">property </em><code class="sig-name descname">ports</code><a class="headerlink" href="#pulumi_packet.GetDeviceResult.ports" title="Permalink to this definition">¶</a></dt>
<dd><p>Ports assigned to the device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetDeviceResult.root_password">
<em class="property">property </em><code class="sig-name descname">root_password</code><a class="headerlink" href="#pulumi_packet.GetDeviceResult.root_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Root password to the server (if still available)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetDeviceResult.ssh_key_ids">
<em class="property">property </em><code class="sig-name descname">ssh_key_ids</code><a class="headerlink" href="#pulumi_packet.GetDeviceResult.ssh_key_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IDs of SSH keys deployed in the device, can be both user or project SSH keys</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetDeviceResult.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_packet.GetDeviceResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetDeviceResult.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_packet.GetDeviceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tags attached to the device</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.GetIpBlockRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetIpBlockRangesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetIpBlockRangesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIpBlockRanges.</p>
<dl class="py method">
<dt id="pulumi_packet.GetIpBlockRangesResult.global_ipv4s">
<em class="property">property </em><code class="sig-name descname">global_ipv4s</code><a class="headerlink" href="#pulumi_packet.GetIpBlockRangesResult.global_ipv4s" title="Permalink to this definition">¶</a></dt>
<dd><p>list of CIDR expressions for Global IPv4 blocks in the project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetIpBlockRangesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_packet.GetIpBlockRangesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetIpBlockRangesResult.ipv6s">
<em class="property">property </em><code class="sig-name descname">ipv6s</code><a class="headerlink" href="#pulumi_packet.GetIpBlockRangesResult.ipv6s" title="Permalink to this definition">¶</a></dt>
<dd><p>list of CIDR expressions for IPv6 blocks in the project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetIpBlockRangesResult.private_ipv4s">
<em class="property">property </em><code class="sig-name descname">private_ipv4s</code><a class="headerlink" href="#pulumi_packet.GetIpBlockRangesResult.private_ipv4s" title="Permalink to this definition">¶</a></dt>
<dd><p>list of CIDR expressions for Private IPv4 blocks in the project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetIpBlockRangesResult.public_ipv4s">
<em class="property">property </em><code class="sig-name descname">public_ipv4s</code><a class="headerlink" href="#pulumi_packet.GetIpBlockRangesResult.public_ipv4s" title="Permalink to this definition">¶</a></dt>
<dd><p>list of CIDR expressions for Public IPv4 blocks in the project</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.GetOperatingSystemResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetOperatingSystemResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">distro</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisionable_on</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slug</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetOperatingSystemResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getOperatingSystem.</p>
<dl class="py method">
<dt id="pulumi_packet.GetOperatingSystemResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_packet.GetOperatingSystemResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetOperatingSystemResult.slug">
<em class="property">property </em><code class="sig-name descname">slug</code><a class="headerlink" href="#pulumi_packet.GetOperatingSystemResult.slug" title="Permalink to this definition">¶</a></dt>
<dd><p>Operating system slug (same as <code class="docutils literal notranslate"><span class="pre">id</span></code>)</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.GetOrganizationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetOrganizationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logo</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">twitter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">website</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetOrganizationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getOrganization.</p>
<dl class="py method">
<dt id="pulumi_packet.GetOrganizationResult.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_packet.GetOrganizationResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description string</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetOrganizationResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_packet.GetOrganizationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetOrganizationResult.logo">
<em class="property">property </em><code class="sig-name descname">logo</code><a class="headerlink" href="#pulumi_packet.GetOrganizationResult.logo" title="Permalink to this definition">¶</a></dt>
<dd><p>Logo URL</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetOrganizationResult.project_ids">
<em class="property">property </em><code class="sig-name descname">project_ids</code><a class="headerlink" href="#pulumi_packet.GetOrganizationResult.project_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>UUIDs of project resources which belong to this organization</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetOrganizationResult.twitter">
<em class="property">property </em><code class="sig-name descname">twitter</code><a class="headerlink" href="#pulumi_packet.GetOrganizationResult.twitter" title="Permalink to this definition">¶</a></dt>
<dd><p>Twitter handle</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetOrganizationResult.website">
<em class="property">property </em><code class="sig-name descname">website</code><a class="headerlink" href="#pulumi_packet.GetOrganizationResult.website" title="Permalink to this definition">¶</a></dt>
<dd><p>Website link</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.GetPrecreatedIpBlockResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetPrecreatedIpBlockResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_notation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateway</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">manageable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">management</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">netmask</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quantity</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetPrecreatedIpBlockResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPrecreatedIpBlock.</p>
<dl class="py method">
<dt id="pulumi_packet.GetPrecreatedIpBlockResult.cidr_notation">
<em class="property">property </em><code class="sig-name descname">cidr_notation</code><a class="headerlink" href="#pulumi_packet.GetPrecreatedIpBlockResult.cidr_notation" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR notation of the looked up block.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetPrecreatedIpBlockResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_packet.GetPrecreatedIpBlockResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.GetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetProjectResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">backend_transfer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">payment_method_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProject.</p>
<dl class="py method">
<dt id="pulumi_packet.GetProjectResult.backend_transfer">
<em class="property">property </em><code class="sig-name descname">backend_transfer</code><a class="headerlink" href="#pulumi_packet.GetProjectResult.backend_transfer" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Backend Transfer is enabled for this project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetProjectResult.bgp_config">
<em class="property">property </em><code class="sig-name descname">bgp_config</code><a class="headerlink" href="#pulumi_packet.GetProjectResult.bgp_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional BGP settings. Refer to <a class="reference external" href="https://www.packet.com/developers/docs/network/advanced/local-and-global-bgp/">Packet guide for BGP</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetProjectResult.created">
<em class="property">property </em><code class="sig-name descname">created</code><a class="headerlink" href="#pulumi_packet.GetProjectResult.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the project was created</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetProjectResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_packet.GetProjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetProjectResult.organization_id">
<em class="property">property </em><code class="sig-name descname">organization_id</code><a class="headerlink" href="#pulumi_packet.GetProjectResult.organization_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of this project’s parent organization</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetProjectResult.payment_method_id">
<em class="property">property </em><code class="sig-name descname">payment_method_id</code><a class="headerlink" href="#pulumi_packet.GetProjectResult.payment_method_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of payment method for this project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetProjectResult.updated">
<em class="property">property </em><code class="sig-name descname">updated</code><a class="headerlink" href="#pulumi_packet.GetProjectResult.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the project was updated</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetProjectResult.user_ids">
<em class="property">property </em><code class="sig-name descname">user_ids</code><a class="headerlink" href="#pulumi_packet.GetProjectResult.user_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of UUIDs of user accounts which beling to this project</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.GetSpotMarketPriceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetSpotMarketPriceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">price</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetSpotMarketPriceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSpotMarketPrice.</p>
<dl class="py method">
<dt id="pulumi_packet.GetSpotMarketPriceResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_packet.GetSpotMarketPriceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetSpotMarketPriceResult.price">
<em class="property">property </em><code class="sig-name descname">price</code><a class="headerlink" href="#pulumi_packet.GetSpotMarketPriceResult.price" title="Permalink to this definition">¶</a></dt>
<dd><p>Current spot market price for given plan in given facility.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.GetSpotMarketRequestResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetSpotMarketRequestResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">device_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetSpotMarketRequestResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSpotMarketRequest.</p>
<dl class="py method">
<dt id="pulumi_packet.GetSpotMarketRequestResult.device_ids">
<em class="property">property </em><code class="sig-name descname">device_ids</code><a class="headerlink" href="#pulumi_packet.GetSpotMarketRequestResult.device_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IDs of devices spawned by the referenced Spot Market Request</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetSpotMarketRequestResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_packet.GetSpotMarketRequestResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.GetVolumeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">GetVolumeResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">billing_cycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.GetVolumeResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVolume.</p>
<dl class="py method">
<dt id="pulumi_packet.GetVolumeResult.billing_cycle">
<em class="property">property </em><code class="sig-name descname">billing_cycle</code><a class="headerlink" href="#pulumi_packet.GetVolumeResult.billing_cycle" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing cycle, defaults to hourly</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetVolumeResult.device_ids">
<em class="property">property </em><code class="sig-name descname">device_ids</code><a class="headerlink" href="#pulumi_packet.GetVolumeResult.device_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>UUIDs of devices to which this volume is attached</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetVolumeResult.facility">
<em class="property">property </em><code class="sig-name descname">facility</code><a class="headerlink" href="#pulumi_packet.GetVolumeResult.facility" title="Permalink to this definition">¶</a></dt>
<dd><p>The facility slug the volume resides in</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetVolumeResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_packet.GetVolumeResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetVolumeResult.locked">
<em class="property">property </em><code class="sig-name descname">locked</code><a class="headerlink" href="#pulumi_packet.GetVolumeResult.locked" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the volume is locked or not</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetVolumeResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_packet.GetVolumeResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the volume</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">project_id</span></code> - The project id the volume is in</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetVolumeResult.plan">
<em class="property">property </em><code class="sig-name descname">plan</code><a class="headerlink" href="#pulumi_packet.GetVolumeResult.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Performance plan the volume is on</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetVolumeResult.size">
<em class="property">property </em><code class="sig-name descname">size</code><a class="headerlink" href="#pulumi_packet.GetVolumeResult.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size in GB of the volume</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.GetVolumeResult.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_packet.GetVolumeResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the volume</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_packet.IpAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">IpAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_notation</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.IpAttachment" title="Permalink to this definition">¶</a></dt>
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
<dl class="py method">
<dt id="pulumi_packet.IpAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_notation</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateway</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">manageable</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">management</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">netmask</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.ip_attachment.IpAttachment<a class="headerlink" href="#pulumi_packet.IpAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IpAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<dt id="pulumi_packet.IpAttachment.address_family">
<em class="property">property </em><code class="sig-name descname">address_family</code><a class="headerlink" href="#pulumi_packet.IpAttachment.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p>Address family as integer (4 or 6)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.IpAttachment.cidr">
<em class="property">property </em><code class="sig-name descname">cidr</code><a class="headerlink" href="#pulumi_packet.IpAttachment.cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>length of CIDR prefix of the subnet as integer</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.IpAttachment.cidr_notation">
<em class="property">property </em><code class="sig-name descname">cidr_notation</code><a class="headerlink" href="#pulumi_packet.IpAttachment.cidr_notation" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR notation of subnet from block reserved in the same
project and facility as the device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.IpAttachment.device_id">
<em class="property">property </em><code class="sig-name descname">device_id</code><a class="headerlink" href="#pulumi_packet.IpAttachment.device_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of device to which to assign the subnet</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.IpAttachment.gateway">
<em class="property">property </em><code class="sig-name descname">gateway</code><a class="headerlink" href="#pulumi_packet.IpAttachment.gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>IP address of gateway for the subnet</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.IpAttachment.netmask">
<em class="property">property </em><code class="sig-name descname">netmask</code><a class="headerlink" href="#pulumi_packet.IpAttachment.netmask" title="Permalink to this definition">¶</a></dt>
<dd><p>Subnet mask in decimal notation, e.g. “255.255.255.0”</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.IpAttachment.network">
<em class="property">property </em><code class="sig-name descname">network</code><a class="headerlink" href="#pulumi_packet.IpAttachment.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Subnet network address</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.IpAttachment.public">
<em class="property">property </em><code class="sig-name descname">public</code><a class="headerlink" href="#pulumi_packet.IpAttachment.public" title="Permalink to this definition">¶</a></dt>
<dd><p>boolean flag whether subnet is reachable from the Internet</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">Organization</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logo</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">twitter</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">website</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Organization" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage organization resource in Packet.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_packet</span> <span class="k">as</span> <span class="nn">packet</span>

<span class="c1"># Create a new Project</span>
<span class="n">tf_organization1</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">Organization</span><span class="p">(</span><span class="s2">&quot;tfOrganization1&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;quux&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;foobar&quot;</span><span class="p">)</span>
</pre></div>
</div>
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
<dl class="py method">
<dt id="pulumi_packet.Organization.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logo</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">twitter</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">website</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.organization.Organization<a class="headerlink" href="#pulumi_packet.Organization.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Organization resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<dt id="pulumi_packet.Organization.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_packet.Organization.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description string.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Organization.logo">
<em class="property">property </em><code class="sig-name descname">logo</code><a class="headerlink" href="#pulumi_packet.Organization.logo" title="Permalink to this definition">¶</a></dt>
<dd><p>Logo URL.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Organization.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_packet.Organization.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Organization.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Organization.twitter">
<em class="property">property </em><code class="sig-name descname">twitter</code><a class="headerlink" href="#pulumi_packet.Organization.twitter" title="Permalink to this definition">¶</a></dt>
<dd><p>Twitter handle.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Organization.website">
<em class="property">property </em><code class="sig-name descname">website</code><a class="headerlink" href="#pulumi_packet.Organization.website" title="Permalink to this definition">¶</a></dt>
<dd><p>Website link.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">PortVlanAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_bond</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">native</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vlan_vnid</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.PortVlanAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to attach device ports to VLANs.</p>
<p>Device and VLAN must be in the same facility.</p>
<p>If you need this resource to add the port back to bond on removal, set <code class="docutils literal notranslate"><span class="pre">force_bond</span> <span class="pre">=</span> <span class="pre">true</span></code>.</p>
<p>To learn more about Layer 2 networking in Packet, refer to</p>
<ul class="simple">
<li><p><a class="reference external" href="https://www.packet.com/resources/guides/layer-2-configurations/">https://www.packet.com/resources/guides/layer-2-configurations/</a></p></li>
<li><p><a class="reference external" href="https://www.packet.com/developers/docs/network/advanced/layer-2/">https://www.packet.com/developers/docs/network/advanced/layer-2/</a></p></li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_packet</span> <span class="k">as</span> <span class="nn">packet</span>

<span class="c1"># Hybrid network type</span>
<span class="n">test_vlan</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">Vlan</span><span class="p">(</span><span class="s2">&quot;testVlan&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;VLAN in New Jersey&quot;</span><span class="p">,</span>
    <span class="n">facility</span><span class="o">=</span><span class="s2">&quot;ewr1&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">local</span><span class="p">[</span><span class="s2">&quot;project_id&quot;</span><span class="p">])</span>
<span class="n">test_device</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">Device</span><span class="p">(</span><span class="s2">&quot;testDevice&quot;</span><span class="p">,</span>
    <span class="n">hostname</span><span class="o">=</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">plan</span><span class="o">=</span><span class="s2">&quot;m1.xlarge.x86&quot;</span><span class="p">,</span>
    <span class="n">facilities</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;ewr1&quot;</span><span class="p">],</span>
    <span class="n">operating_system</span><span class="o">=</span><span class="s2">&quot;ubuntu_16_04&quot;</span><span class="p">,</span>
    <span class="n">billing_cycle</span><span class="o">=</span><span class="s2">&quot;hourly&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">local</span><span class="p">[</span><span class="s2">&quot;project_id&quot;</span><span class="p">])</span>
<span class="n">test_device_network_type</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">DeviceNetworkType</span><span class="p">(</span><span class="s2">&quot;testDeviceNetworkType&quot;</span><span class="p">,</span>
    <span class="n">device_id</span><span class="o">=</span><span class="n">test_device</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;hybrid&quot;</span><span class="p">)</span>
<span class="n">test_port_vlan_attachment</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">PortVlanAttachment</span><span class="p">(</span><span class="s2">&quot;testPortVlanAttachment&quot;</span><span class="p">,</span>
    <span class="n">device_id</span><span class="o">=</span><span class="n">test_device_network_type</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">port_name</span><span class="o">=</span><span class="s2">&quot;eth1&quot;</span><span class="p">,</span>
    <span class="n">vlan_vnid</span><span class="o">=</span><span class="n">test_vlan</span><span class="o">.</span><span class="n">vxlan</span><span class="p">)</span>
<span class="c1"># Layer 2 network</span>
<span class="n">test_index_device_device</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">Device</span><span class="p">(</span><span class="s2">&quot;testIndex/deviceDevice&quot;</span><span class="p">,</span>
    <span class="n">hostname</span><span class="o">=</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">plan</span><span class="o">=</span><span class="s2">&quot;m1.xlarge.x86&quot;</span><span class="p">,</span>
    <span class="n">facilities</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;ewr1&quot;</span><span class="p">],</span>
    <span class="n">operating_system</span><span class="o">=</span><span class="s2">&quot;ubuntu_16_04&quot;</span><span class="p">,</span>
    <span class="n">billing_cycle</span><span class="o">=</span><span class="s2">&quot;hourly&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">local</span><span class="p">[</span><span class="s2">&quot;project_id&quot;</span><span class="p">])</span>
<span class="n">test_index_device_network_type_device_network_type</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">DeviceNetworkType</span><span class="p">(</span><span class="s2">&quot;testIndex/deviceNetworkTypeDeviceNetworkType&quot;</span><span class="p">,</span>
    <span class="n">device_id</span><span class="o">=</span><span class="n">test_device</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;layer2-individual&quot;</span><span class="p">)</span>
<span class="n">test1_vlan</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">Vlan</span><span class="p">(</span><span class="s2">&quot;test1Vlan&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;VLAN in New Jersey&quot;</span><span class="p">,</span>
    <span class="n">facility</span><span class="o">=</span><span class="s2">&quot;ewr1&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">local</span><span class="p">[</span><span class="s2">&quot;project_id&quot;</span><span class="p">])</span>
<span class="n">test2_vlan</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">Vlan</span><span class="p">(</span><span class="s2">&quot;test2Vlan&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;VLAN in New Jersey&quot;</span><span class="p">,</span>
    <span class="n">facility</span><span class="o">=</span><span class="s2">&quot;ewr1&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">local</span><span class="p">[</span><span class="s2">&quot;project_id&quot;</span><span class="p">])</span>
<span class="n">test1_port_vlan_attachment</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">PortVlanAttachment</span><span class="p">(</span><span class="s2">&quot;test1PortVlanAttachment&quot;</span><span class="p">,</span>
    <span class="n">device_id</span><span class="o">=</span><span class="n">test_device_network_type</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">vlan_vnid</span><span class="o">=</span><span class="n">test1_vlan</span><span class="o">.</span><span class="n">vxlan</span><span class="p">,</span>
    <span class="n">port_name</span><span class="o">=</span><span class="s2">&quot;eth1&quot;</span><span class="p">)</span>
<span class="n">test2_port_vlan_attachment</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">PortVlanAttachment</span><span class="p">(</span><span class="s2">&quot;test2PortVlanAttachment&quot;</span><span class="p">,</span>
    <span class="n">device_id</span><span class="o">=</span><span class="n">test_device_network_type</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">vlan_vnid</span><span class="o">=</span><span class="n">test2_vlan</span><span class="o">.</span><span class="n">vxlan</span><span class="p">,</span>
    <span class="n">port_name</span><span class="o">=</span><span class="s2">&quot;eth1&quot;</span><span class="p">,</span>
    <span class="n">native</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">opts</span><span class="o">=</span><span class="n">ResourceOptions</span><span class="p">(</span><span class="n">depends_on</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;packet_port_vlan_attachment.test1&quot;</span><span class="p">]))</span>
</pre></div>
</div>
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
<dl class="py method">
<dt id="pulumi_packet.PortVlanAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_bond</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">native</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vlan_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vlan_vnid</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.port_vlan_attachment.PortVlanAttachment<a class="headerlink" href="#pulumi_packet.PortVlanAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PortVlanAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<dt id="pulumi_packet.PortVlanAttachment.device_id">
<em class="property">property </em><code class="sig-name descname">device_id</code><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.device_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of device to be assigned to the VLAN</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.PortVlanAttachment.force_bond">
<em class="property">property </em><code class="sig-name descname">force_bond</code><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.force_bond" title="Permalink to this definition">¶</a></dt>
<dd><p>Add port back to the bond when this resource is removed. Default is false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.PortVlanAttachment.native">
<em class="property">property </em><code class="sig-name descname">native</code><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.native" title="Permalink to this definition">¶</a></dt>
<dd><p>Mark this VLAN a native VLAN on the port. This can be used only if this assignment assigns second or further VLAN to the port. To ensure that this attachment is not first on a port, you can use <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> pointing to another packet_port_vlan_attachment, just like in the layer2-individual example above.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.PortVlanAttachment.port_name">
<em class="property">property </em><code class="sig-name descname">port_name</code><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.port_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of network port to be assigned to the VLAN</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.PortVlanAttachment.vlan_vnid">
<em class="property">property </em><code class="sig-name descname">vlan_vnid</code><a class="headerlink" href="#pulumi_packet.PortVlanAttachment.vlan_vnid" title="Permalink to this definition">¶</a></dt>
<dd><p>VXLAN Network Identifier, integer</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">Project</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend_transfer</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_config</span><span class="p">:</span> <span class="n">Union[ProjectBgpConfigArgs, Mapping[str, Any], Awaitable[Union[ProjectBgpConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">payment_method_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet project resource to allow you manage devices
in your projects.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_packet</span> <span class="k">as</span> <span class="nn">packet</span>

<span class="c1"># Create a new project</span>
<span class="n">tf_project1</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;tfProject1&quot;</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Terraform Fun&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Example with BGP config</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_packet</span> <span class="k">as</span> <span class="nn">packet</span>

<span class="c1"># Create a new Project</span>
<span class="n">tf_project1</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;tfProject1&quot;</span><span class="p">,</span>
    <span class="n">bgp_config</span><span class="o">=</span><span class="n">packet</span><span class="o">.</span><span class="n">ProjectBgpConfigArgs</span><span class="p">(</span>
        <span class="n">asn</span><span class="o">=</span><span class="mi">65000</span><span class="p">,</span>
        <span class="n">deployment_type</span><span class="o">=</span><span class="s2">&quot;local&quot;</span><span class="p">,</span>
        <span class="n">md5</span><span class="o">=</span><span class="s2">&quot;C179c28c41a85b&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;tftest&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_transfer</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable <a class="reference external" href="https://www.packet.com/developers/docs/network/basic/backend-transfer/">Backend Transfer</a>, default is false</p></li>
<li><p><strong>bgp_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ProjectBgpConfigArgs'</em><em>]</em><em>]</em>) – <p>Optional BGP settings. Refer to <a class="reference external" href="https://www.packet.com/developers/docs/network/advanced/local-and-global-bgp/">Packet guide for BGP</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project</p></li>
<li><p><strong>organization_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of organization under which you want to create the project. If you leave it out, the project will be create under your the default organization of your account.</p></li>
<li><p><strong>payment_method_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of payment method for this project. The payment method and the project need to belong to the same organization (passed with <code class="docutils literal notranslate"><span class="pre">organization_id</span></code>, or default).</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_packet.Project.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backend_transfer</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_config</span><span class="p">:</span> <span class="n">Union[ProjectBgpConfigArgs, Mapping[str, Any], Awaitable[Union[ProjectBgpConfigArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">payment_method_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.project.Project<a class="headerlink" href="#pulumi_packet.Project.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Project resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_transfer</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Enable or disable <a class="reference external" href="https://www.packet.com/developers/docs/network/basic/backend-transfer/">Backend Transfer</a>, default is false</p>
</p></li>
<li><p><strong>bgp_config</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ProjectBgpConfigArgs'</em><em>]</em><em>]</em>) – <p>Optional BGP settings. Refer to <a class="reference external" href="https://www.packet.com/developers/docs/network/advanced/local-and-global-bgp/">Packet guide for BGP</a>.</p>
</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timestamp for when the project was created</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project</p></li>
<li><p><strong>organization_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of organization under which you want to create the project. If you leave it out, the project will be create under your the default organization of your account.</p></li>
<li><p><strong>payment_method_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The UUID of payment method for this project. The payment method and the project need to belong to the same organization (passed with <code class="docutils literal notranslate"><span class="pre">organization_id</span></code>, or default).</p></li>
<li><p><strong>updated</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timestamp for the last time the project was updated</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Project.backend_transfer">
<em class="property">property </em><code class="sig-name descname">backend_transfer</code><a class="headerlink" href="#pulumi_packet.Project.backend_transfer" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable <a class="reference external" href="https://www.packet.com/developers/docs/network/basic/backend-transfer/">Backend Transfer</a>, default is false</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Project.bgp_config">
<em class="property">property </em><code class="sig-name descname">bgp_config</code><a class="headerlink" href="#pulumi_packet.Project.bgp_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional BGP settings. Refer to <a class="reference external" href="https://www.packet.com/developers/docs/network/advanced/local-and-global-bgp/">Packet guide for BGP</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Project.created">
<em class="property">property </em><code class="sig-name descname">created</code><a class="headerlink" href="#pulumi_packet.Project.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the project was created</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Project.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_packet.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Project.organization_id">
<em class="property">property </em><code class="sig-name descname">organization_id</code><a class="headerlink" href="#pulumi_packet.Project.organization_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of organization under which you want to create the project. If you leave it out, the project will be create under your the default organization of your account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Project.payment_method_id">
<em class="property">property </em><code class="sig-name descname">payment_method_id</code><a class="headerlink" href="#pulumi_packet.Project.payment_method_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of payment method for this project. The payment method and the project need to belong to the same organization (passed with <code class="docutils literal notranslate"><span class="pre">organization_id</span></code>, or default).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Project.updated">
<em class="property">property </em><code class="sig-name descname">updated</code><a class="headerlink" href="#pulumi_packet.Project.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the project was updated</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">ProjectSshKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.ProjectSshKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet project SSH key resource to manage project-specific SSH keys.
Project SSH keys will only be populated onto servers that belong to that project, in contrast to User SSH Keys.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_packet</span> <span class="k">as</span> <span class="nn">packet</span>

<span class="n">project_id</span> <span class="o">=</span> <span class="s2">&quot;&lt;UUID_of_your_project&gt;&quot;</span>
<span class="n">test_project_ssh_key</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">ProjectSshKey</span><span class="p">(</span><span class="s2">&quot;testProjectSshKey&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">public_key</span><span class="o">=</span><span class="s2">&quot;ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDM/unxJeFqxsTJcu6mhqsMHSaVlpu+Jj/P+44zrm6X/MAoHSX3X9oLgujEjjZ74yLfdfe0bJrbL2YgJzNaEkIQQ1VPMHB5EhTKUBGnzlPP0hHTnxsjAm9qDHgUPgvgFDQSAMzdJRJ0Cexo16Ph9VxCoLh3dxiE7s2gaM2FdVg7P8aSxKypsxAhYV3D0AwqzoOyT6WWhBoQ0xZ85XevOTnJCpImSemEGs6nVGEsWcEc1d1YvdxFjAK4SdsKUMkj4Dsy/leKsdi/DEAf356vbMT1UHsXXvy5TlHu/Pa6qF53v32Enz+nhKy7/8W2Yt2yWx8HnQcT2rug9lvCXagJO6oauqRTO77C4QZn13ZLMZgLT66S/tNh2EX0gi6vmIs5dth8uF+K6nxIyKJXbcA4ASg7F1OJrHKFZdTc5v1cPeq6PcbqGgc+8SrPYQmzvQqLoMBuxyos2hUkYOmw3aeWJj9nFa8Wu5WaN89mUeOqSkU4S5cgUzWUOmKey56B/j/s1sVys9rMhZapVs0wL4L9GBBM48N5jAQZnnpo85A8KsZq5ME22bTLqnxsDXqDYZvS7PSI6Dxi7eleOFE/NYYDkrgDLHTQri8ucDMVeVWHgoMY2bPXdn7KKy5jW5jKsf8EPARXg77A4gRYmgKrcwIKqJEUPqyxJBe0CPoGTqgXPRsUiQ== tomk@hp2&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project_id</span><span class="p">)</span>
<span class="n">test_device</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">Device</span><span class="p">(</span><span class="s2">&quot;testDevice&quot;</span><span class="p">,</span>
    <span class="n">hostname</span><span class="o">=</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">plan</span><span class="o">=</span><span class="s2">&quot;baremetal_0&quot;</span><span class="p">,</span>
    <span class="n">facilities</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;ewr1&quot;</span><span class="p">],</span>
    <span class="n">operating_system</span><span class="o">=</span><span class="s2">&quot;ubuntu_16_04&quot;</span><span class="p">,</span>
    <span class="n">billing_cycle</span><span class="o">=</span><span class="s2">&quot;hourly&quot;</span><span class="p">,</span>
    <span class="n">project_ssh_key_ids</span><span class="o">=</span><span class="p">[</span><span class="n">test_project_ssh_key</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project_id</span><span class="p">)</span>
</pre></div>
</div>
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
<dl class="py method">
<dt id="pulumi_packet.ProjectSshKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fingerprint</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.project_ssh_key.ProjectSshKey<a class="headerlink" href="#pulumi_packet.ProjectSshKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectSshKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<dt id="pulumi_packet.ProjectSshKey.created">
<em class="property">property </em><code class="sig-name descname">created</code><a class="headerlink" href="#pulumi_packet.ProjectSshKey.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the SSH key was created</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ProjectSshKey.fingerprint">
<em class="property">property </em><code class="sig-name descname">fingerprint</code><a class="headerlink" href="#pulumi_packet.ProjectSshKey.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the SSH key</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ProjectSshKey.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_packet.ProjectSshKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SSH key for identification</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ProjectSshKey.owner_id">
<em class="property">property </em><code class="sig-name descname">owner_id</code><a class="headerlink" href="#pulumi_packet.ProjectSshKey.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of parent project (same as project_id)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ProjectSshKey.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_packet.ProjectSshKey.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of parent project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ProjectSshKey.public_key">
<em class="property">property </em><code class="sig-name descname">public_key</code><a class="headerlink" href="#pulumi_packet.ProjectSshKey.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key. If this is a file, it can be read using the file interpolation function</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ProjectSshKey.updated">
<em class="property">property </em><code class="sig-name descname">updated</code><a class="headerlink" href="#pulumi_packet.ProjectSshKey.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the SSH key was updated</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Provider" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">ReservedIpBlock</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quantity</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.ReservedIpBlock" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to create and manage blocks of reserved IP addresses in a project.</p>
<p>When a user provisions first device in a facility, Packet API automatically allocates IPv6/56 and private IPv4/25 blocks.
The new device then gets IPv6 and private IPv4 addresses from those block. It also gets a public IPv4/31 address.
Every new device in the project and facility will automatically get IPv6 and private IPv4 addresses from these pre-allocated blocks.
The IPv6 and private IPv4 blocks can’t be created, only imported. With this resource, it’s possible to create either public IPv4 blocks or global IPv4 blocks.</p>
<p>Public blocks are allocated in a facility. Addresses from public blocks can only be assigned to devices in the facility. Public blocks can have mask from /24 (256 addresses) to /32 (1 address). If you create public block with this resource, you must fill the facility argmument.</p>
<p>Addresses from global blocks can be assigned in any facility. Global blocks can have mask from /30 (4 addresses), to /32 (1 address). If you create global block with this resource, you must specify type = “global_ipv4” and you must omit the facility argument.</p>
<p>Once IP block is allocated or imported, an address from it can be assigned to device with the <code class="docutils literal notranslate"><span class="pre">IpAttachment</span></code> resource.</p>
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
<dl class="py method">
<dt id="pulumi_packet.ReservedIpBlock.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_notation</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateway</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">manageable</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">management</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">netmask</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quantity</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.reserved_ip_block.ReservedIpBlock<a class="headerlink" href="#pulumi_packet.ReservedIpBlock.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ReservedIpBlock resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Address family as integer (4 or 6)</p></li>
<li><p><strong>cidr</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – length of CIDR prefix of the block as integer</p></li>
<li><p><strong>cidr_notation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Address and mask in CIDR notation, e.g. “147.229.15.30/31”</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Arbitrary description</p></li>
<li><p><strong>facility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Facility where to allocate the public IP address block, makes sense only for type==public_ipv4, must be empty for type==global<a href="#id16"><span class="problematic" id="id17">*</span></a>ipv4</p></li>
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
<dt id="pulumi_packet.ReservedIpBlock.address_family">
<em class="property">property </em><code class="sig-name descname">address_family</code><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p>Address family as integer (4 or 6)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ReservedIpBlock.cidr">
<em class="property">property </em><code class="sig-name descname">cidr</code><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.cidr" title="Permalink to this definition">¶</a></dt>
<dd><p>length of CIDR prefix of the block as integer</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ReservedIpBlock.cidr_notation">
<em class="property">property </em><code class="sig-name descname">cidr_notation</code><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.cidr_notation" title="Permalink to this definition">¶</a></dt>
<dd><p>Address and mask in CIDR notation, e.g. “147.229.15.30/31”</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ReservedIpBlock.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Arbitrary description</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ReservedIpBlock.facility">
<em class="property">property </em><code class="sig-name descname">facility</code><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.facility" title="Permalink to this definition">¶</a></dt>
<dd><p>Facility where to allocate the public IP address block, makes sense only for type==public_ipv4, must be empty for type==global_ipv4</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ReservedIpBlock.global_">
<em class="property">property </em><code class="sig-name descname">global_</code><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.global_" title="Permalink to this definition">¶</a></dt>
<dd><p>boolean flag whether addresses from a block are global (i.e. can be assigned in any facility)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ReservedIpBlock.netmask">
<em class="property">property </em><code class="sig-name descname">netmask</code><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.netmask" title="Permalink to this definition">¶</a></dt>
<dd><p>Mask in decimal notation, e.g. “255.255.255.0”</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ReservedIpBlock.network">
<em class="property">property </em><code class="sig-name descname">network</code><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.network" title="Permalink to this definition">¶</a></dt>
<dd><p>Network IP address portion of the block specification</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ReservedIpBlock.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The packet project ID where to allocate the address block</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ReservedIpBlock.public">
<em class="property">property </em><code class="sig-name descname">public</code><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.public" title="Permalink to this definition">¶</a></dt>
<dd><p>boolean flag whether addresses from a block are public</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ReservedIpBlock.quantity">
<em class="property">property </em><code class="sig-name descname">quantity</code><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.quantity" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of allocated /32 addresses, a power of 2</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.ReservedIpBlock.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_packet.ReservedIpBlock.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Either “global_ipv4” or “public_ipv4”, defaults to “public_ipv4” for backward compatibility</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">SpotMarketRequest</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">devices_max</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">devices_min</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facilities</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_parameters</span><span class="p">:</span> <span class="n">Union[SpotMarketRequestInstanceParametersArgs, Mapping[str, Any], Awaitable[Union[SpotMarketRequestInstanceParametersArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_bid_price</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_for_devices</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SpotMarketRequest" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet Spot Market Request resource to allow you to
manage spot market requests on your account. For more detail on Spot Market, see <a class="reference external" href="https://www.packet.com/developers/docs/getting-started/deployment-options/spot-market/">this article in Packet documentaion</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_packet</span> <span class="k">as</span> <span class="nn">packet</span>

<span class="c1"># Create a spot market request</span>
<span class="n">req</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">SpotMarketRequest</span><span class="p">(</span><span class="s2">&quot;req&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">local</span><span class="p">[</span><span class="s2">&quot;project_id&quot;</span><span class="p">],</span>
    <span class="n">max_bid_price</span><span class="o">=</span><span class="mf">0.03</span><span class="p">,</span>
    <span class="n">facilities</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;ewr1&quot;</span><span class="p">],</span>
    <span class="n">devices_min</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">devices_max</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">instance_parameters</span><span class="o">=</span><span class="n">packet</span><span class="o">.</span><span class="n">SpotMarketRequestInstanceParametersArgs</span><span class="p">(</span>
        <span class="n">hostname</span><span class="o">=</span><span class="s2">&quot;testspot&quot;</span><span class="p">,</span>
        <span class="n">billing_cycle</span><span class="o">=</span><span class="s2">&quot;hourly&quot;</span><span class="p">,</span>
        <span class="n">operating_system</span><span class="o">=</span><span class="s2">&quot;coreos_stable&quot;</span><span class="p">,</span>
        <span class="n">plan</span><span class="o">=</span><span class="s2">&quot;t1.small.x86&quot;</span><span class="p">,</span>
    <span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>devices_max</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum number devices to be created</p></li>
<li><p><strong>devices_min</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Miniumum number devices to be created</p></li>
<li><p><strong>facilities</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Facility IDs where devices should be created</p></li>
<li><p><strong>instance_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SpotMarketRequestInstanceParametersArgs'</em><em>]</em><em>]</em>) – Device parameters. See device resource for details</p></li>
<li><p><strong>max_bid_price</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum price user is willing to pay per hour per device</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project ID</p></li>
<li><p><strong>wait_for_devices</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_packet.SpotMarketRequest.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">devices_max</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">devices_min</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facilities</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_parameters</span><span class="p">:</span> <span class="n">Union[SpotMarketRequestInstanceParametersArgs, Mapping[str, Any], Awaitable[Union[SpotMarketRequestInstanceParametersArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_bid_price</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wait_for_devices</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.spot_market_request.SpotMarketRequest<a class="headerlink" href="#pulumi_packet.SpotMarketRequest.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SpotMarketRequest resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>devices_max</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum number devices to be created</p></li>
<li><p><strong>devices_min</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Miniumum number devices to be created</p></li>
<li><p><strong>facilities</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Facility IDs where devices should be created</p></li>
<li><p><strong>instance_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SpotMarketRequestInstanceParametersArgs'</em><em>]</em><em>]</em>) – Device parameters. See device resource for details</p></li>
<li><p><strong>max_bid_price</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum price user is willing to pay per hour per device</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project ID</p></li>
<li><p><strong>wait_for_devices</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.SpotMarketRequest.devices_max">
<em class="property">property </em><code class="sig-name descname">devices_max</code><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.devices_max" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum number devices to be created</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.SpotMarketRequest.devices_min">
<em class="property">property </em><code class="sig-name descname">devices_min</code><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.devices_min" title="Permalink to this definition">¶</a></dt>
<dd><p>Miniumum number devices to be created</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.SpotMarketRequest.facilities">
<em class="property">property </em><code class="sig-name descname">facilities</code><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.facilities" title="Permalink to this definition">¶</a></dt>
<dd><p>Facility IDs where devices should be created</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.SpotMarketRequest.instance_parameters">
<em class="property">property </em><code class="sig-name descname">instance_parameters</code><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.instance_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Device parameters. See device resource for details</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.SpotMarketRequest.max_bid_price">
<em class="property">property </em><code class="sig-name descname">max_bid_price</code><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.max_bid_price" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum price user is willing to pay per hour per device</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.SpotMarketRequest.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Project ID</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.SpotMarketRequest.wait_for_devices">
<em class="property">property </em><code class="sig-name descname">wait_for_devices</code><a class="headerlink" href="#pulumi_packet.SpotMarketRequest.wait_for_devices" title="Permalink to this definition">¶</a></dt>
<dd><p>On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">SshKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.SshKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage User SSH keys on your Packet user account. If you create a new device in a project, all the keys of the project’s collaborators will be injected to the device.</p>
<p>The link between User SSH key and device is implicit. If you want to make sure that a key will be copied to a device, you must ensure that the device resource <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> the key resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_packet</span> <span class="k">as</span> <span class="nn">packet</span>

<span class="c1"># Create a new SSH key</span>
<span class="n">key1</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">SshKey</span><span class="p">(</span><span class="s2">&quot;key1&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;terraform-1&quot;</span><span class="p">,</span>
    <span class="n">public_key</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;/home/terraform/.ssh/id_rsa.pub&quot;</span><span class="p">))</span>
<span class="c1"># Create new device with &quot;key1&quot; included. The device resource &quot;depends_on&quot; the</span>
<span class="c1"># key, in order to make sure the key is created before the device.</span>
<span class="n">test</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">Device</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">hostname</span><span class="o">=</span><span class="s2">&quot;test-device&quot;</span><span class="p">,</span>
    <span class="n">plan</span><span class="o">=</span><span class="s2">&quot;t1.small.x86&quot;</span><span class="p">,</span>
    <span class="n">facilities</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;sjc1&quot;</span><span class="p">],</span>
    <span class="n">operating_system</span><span class="o">=</span><span class="s2">&quot;ubuntu_16_04&quot;</span><span class="p">,</span>
    <span class="n">billing_cycle</span><span class="o">=</span><span class="s2">&quot;hourly&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">local</span><span class="p">[</span><span class="s2">&quot;project_id&quot;</span><span class="p">],</span>
    <span class="n">opts</span><span class="o">=</span><span class="n">ResourceOptions</span><span class="p">(</span><span class="n">depends_on</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;packet_ssh_key.key1&quot;</span><span class="p">]))</span>
</pre></div>
</div>
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
<dl class="py method">
<dt id="pulumi_packet.SshKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fingerprint</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.ssh_key.SshKey<a class="headerlink" href="#pulumi_packet.SshKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SshKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<dt id="pulumi_packet.SshKey.created">
<em class="property">property </em><code class="sig-name descname">created</code><a class="headerlink" href="#pulumi_packet.SshKey.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the SSH key was created</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.SshKey.fingerprint">
<em class="property">property </em><code class="sig-name descname">fingerprint</code><a class="headerlink" href="#pulumi_packet.SshKey.fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The fingerprint of the SSH key</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.SshKey.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_packet.SshKey.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SSH key for identification</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.SshKey.owner_id">
<em class="property">property </em><code class="sig-name descname">owner_id</code><a class="headerlink" href="#pulumi_packet.SshKey.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of the Packet API User who owns this key</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.SshKey.public_key">
<em class="property">property </em><code class="sig-name descname">public_key</code><a class="headerlink" href="#pulumi_packet.SshKey.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key. If this is a file, it
can be read using the file interpolation function</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.SshKey.updated">
<em class="property">property </em><code class="sig-name descname">updated</code><a class="headerlink" href="#pulumi_packet.SshKey.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the SSH key was updated</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">Vlan</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Vlan" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to allow users to manage Virtual Networks in their projects.</p>
<p>To learn more about Layer 2 networking in Packet, refer to</p>
<ul class="simple">
<li><p><a class="reference external" href="https://www.packet.com/resources/guides/layer-2-configurations/">https://www.packet.com/resources/guides/layer-2-configurations/</a></p></li>
<li><p><a class="reference external" href="https://www.packet.com/developers/docs/network/advanced/layer-2/">https://www.packet.com/developers/docs/network/advanced/layer-2/</a></p></li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_packet</span> <span class="k">as</span> <span class="nn">packet</span>

<span class="c1"># Create a new VLAN in datacenter &quot;ewr1&quot;</span>
<span class="n">vlan1</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">Vlan</span><span class="p">(</span><span class="s2">&quot;vlan1&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;VLAN in New Jersey&quot;</span><span class="p">,</span>
    <span class="n">facility</span><span class="o">=</span><span class="s2">&quot;ewr1&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">local</span><span class="p">[</span><span class="s2">&quot;project_id&quot;</span><span class="p">])</span>
</pre></div>
</div>
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
<dl class="py method">
<dt id="pulumi_packet.Vlan.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vxlan</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.vlan.Vlan<a class="headerlink" href="#pulumi_packet.Vlan.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Vlan resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<dt id="pulumi_packet.Vlan.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_packet.Vlan.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description string</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Vlan.facility">
<em class="property">property </em><code class="sig-name descname">facility</code><a class="headerlink" href="#pulumi_packet.Vlan.facility" title="Permalink to this definition">¶</a></dt>
<dd><p>Facility where to create the VLAN</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Vlan.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_packet.Vlan.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of parent project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Vlan.vxlan">
<em class="property">property </em><code class="sig-name descname">vxlan</code><a class="headerlink" href="#pulumi_packet.Vlan.vxlan" title="Permalink to this definition">¶</a></dt>
<dd><p>VXLAN segment ID</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">Volume</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_cycle</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_policies</span><span class="p">:</span> <span class="n">Union[List[Union[VolumeSnapshotPolicyArgs, Mapping[str, Any], Awaitable[Union[VolumeSnapshotPolicyArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[VolumeSnapshotPolicyArgs, Mapping[str, Any], Awaitable[Union[VolumeSnapshotPolicyArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.Volume" title="Permalink to this definition">¶</a></dt>
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
:param pulumi.Input[List[pulumi.Input[pulumi.InputType[‘VolumeSnapshotPolicyArgs’]]]] snapshot_policies: Optional list of snapshot policies</p>
<dl class="py method">
<dt id="pulumi_packet.Volume.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">attachments</span><span class="p">:</span> <span class="n">Union[List[Union[VolumeAttachmentArgs, Mapping[str, Any], Awaitable[Union[VolumeAttachmentArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[VolumeAttachmentArgs, Mapping[str, Any], Awaitable[Union[VolumeAttachmentArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">billing_cycle</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_policies</span><span class="p">:</span> <span class="n">Union[List[Union[VolumeSnapshotPolicyArgs, Mapping[str, Any], Awaitable[Union[VolumeSnapshotPolicyArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[VolumeSnapshotPolicyArgs, Mapping[str, Any], Awaitable[Union[VolumeSnapshotPolicyArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.volume.Volume<a class="headerlink" href="#pulumi_packet.Volume.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Volume resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>attachments</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'VolumeAttachmentArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of attachments, each with it’s own <code class="docutils literal notranslate"><span class="pre">href</span></code> attribute</p></li>
<li><p><strong>billing_cycle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing cycle, defaults to “hourly”</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timestamp for when the volume was created</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Optional description for the volume</p></li>
<li><p><strong>facility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The facility to create the volume in</p></li>
<li><p><strong>locked</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Lock or unlock the volume</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the volume</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service plan slug of the volume</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The packet project ID to deploy the volume in</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size in GB to make the volume</p></li>
<li><p><strong>snapshot_policies</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'VolumeSnapshotPolicyArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Optional list of snapshot policies</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of the volume</p></li>
<li><p><strong>updated</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timestamp for the last time the volume was updated</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Volume.attachments">
<em class="property">property </em><code class="sig-name descname">attachments</code><a class="headerlink" href="#pulumi_packet.Volume.attachments" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of attachments, each with it’s own <code class="docutils literal notranslate"><span class="pre">href</span></code> attribute</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Volume.billing_cycle">
<em class="property">property </em><code class="sig-name descname">billing_cycle</code><a class="headerlink" href="#pulumi_packet.Volume.billing_cycle" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing cycle, defaults to “hourly”</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Volume.created">
<em class="property">property </em><code class="sig-name descname">created</code><a class="headerlink" href="#pulumi_packet.Volume.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for when the volume was created</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Volume.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_packet.Volume.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional description for the volume</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Volume.facility">
<em class="property">property </em><code class="sig-name descname">facility</code><a class="headerlink" href="#pulumi_packet.Volume.facility" title="Permalink to this definition">¶</a></dt>
<dd><p>The facility to create the volume in</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Volume.locked">
<em class="property">property </em><code class="sig-name descname">locked</code><a class="headerlink" href="#pulumi_packet.Volume.locked" title="Permalink to this definition">¶</a></dt>
<dd><p>Lock or unlock the volume</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Volume.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_packet.Volume.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the volume</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Volume.plan">
<em class="property">property </em><code class="sig-name descname">plan</code><a class="headerlink" href="#pulumi_packet.Volume.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>The service plan slug of the volume</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Volume.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_packet.Volume.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The packet project ID to deploy the volume in</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Volume.size">
<em class="property">property </em><code class="sig-name descname">size</code><a class="headerlink" href="#pulumi_packet.Volume.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size in GB to make the volume</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Volume.snapshot_policies">
<em class="property">property </em><code class="sig-name descname">snapshot_policies</code><a class="headerlink" href="#pulumi_packet.Volume.snapshot_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional list of snapshot policies</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Volume.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_packet.Volume.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the volume</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.Volume.updated">
<em class="property">property </em><code class="sig-name descname">updated</code><a class="headerlink" href="#pulumi_packet.Volume.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The timestamp for the last time the volume was updated</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">VolumeAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_packet.VolumeAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a VolumeAttachment resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] device_id: The ID of the device to which the volume should be attached
:param pulumi.Input[str] volume_id: The ID of the volume to attach</p>
<dl class="py method">
<dt id="pulumi_packet.VolumeAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.volume_attachment.VolumeAttachment<a class="headerlink" href="#pulumi_packet.VolumeAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VolumeAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>device_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the device to which the volume should be attached</p></li>
<li><p><strong>volume_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the volume to attach</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.VolumeAttachment.device_id">
<em class="property">property </em><code class="sig-name descname">device_id</code><a class="headerlink" href="#pulumi_packet.VolumeAttachment.device_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the device to which the volume should be attached</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_packet.VolumeAttachment.volume_id">
<em class="property">property </em><code class="sig-name descname">volume_id</code><a class="headerlink" href="#pulumi_packet.VolumeAttachment.volume_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the volume to attach</p>
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
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_device</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">device_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.get_device.AwaitableGetDeviceResult<a class="headerlink" href="#pulumi_packet.get_device" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_packet.get_device_bgp_neighbors">
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_device_bgp_neighbors</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">device_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.get_device_bgp_neighbors.AwaitableGetDeviceBgpNeighborsResult<a class="headerlink" href="#pulumi_packet.get_device_bgp_neighbors" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this datasource to retrieve list of BGP neighbors of a device in the Packet host.</p>
<p>To have any BGP neighbors listed, the device must be in BGP-enabled project and have a BGP session assigned.</p>
<p>To learn more about using BGP in Packet, see the BgpSession resource documentation.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_packet</span> <span class="k">as</span> <span class="nn">packet</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">get_device_bgp_neighbors</span><span class="p">(</span><span class="n">device_id</span><span class="o">=</span><span class="s2">&quot;4c641195-25e5-4c3c-b2b7-4cd7a42c7b40&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;bgpNeighborsListing&quot;</span><span class="p">,</span> <span class="n">test</span><span class="o">.</span><span class="n">bgp_neighbors</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>device_id</strong> (<em>str</em>) – UUID of BGP-enabled device whose neighbors to list</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_packet.get_ip_block_ranges">
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_ip_block_ranges</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">facility</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.get_ip_block_ranges.AwaitableGetIpBlockRangesResult<a class="headerlink" href="#pulumi_packet.get_ip_block_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this datasource to get CIDR expressions for allocated IP blocks of all the types in a project, optionally filtered by facility.</p>
<p>There are four types of IP blocks in Packet: global IPv4, public IPv4, private IPv4 and IPv6. Both global and public IPv4 are routable from the Internet. Public IPv4 block is allocated in a facility, and addresses from it can only be assigned to devices in that facility. Addresses from Global IPv4 block can be assigned to a device in any facility.</p>
<p>The datasource has 4 list attributes: <code class="docutils literal notranslate"><span class="pre">global_ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">public_ipv4</span></code>, <code class="docutils literal notranslate"><span class="pre">private_ipv4</span></code> and <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>, each listing CIDR notation (<code class="docutils literal notranslate"><span class="pre">&lt;network&gt;/&lt;mask&gt;</span></code>) of respective blocks from the project.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_packet</span> <span class="k">as</span> <span class="nn">packet</span>

<span class="n">project_id</span> <span class="o">=</span> <span class="s2">&quot;&lt;UUID_of_your_project&gt;&quot;</span>
<span class="n">test</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">get_ip_block_ranges</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="n">project_id</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;out&quot;</span><span class="p">,</span> <span class="n">test</span><span class="p">)</span>
</pre></div>
</div>
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
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_operating_system</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">distro</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisionable_on</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.get_operating_system.AwaitableGetOperatingSystemResult<a class="headerlink" href="#pulumi_packet.get_operating_system" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get Packet Operating System image.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_packet</span> <span class="k">as</span> <span class="nn">packet</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">get_operating_system</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Container Linux&quot;</span><span class="p">,</span>
    <span class="n">distro</span><span class="o">=</span><span class="s2">&quot;coreos&quot;</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="s2">&quot;alpha&quot;</span><span class="p">,</span>
    <span class="n">provisionable_on</span><span class="o">=</span><span class="s2">&quot;c1.small.x86&quot;</span><span class="p">)</span>
<span class="n">server</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">Device</span><span class="p">(</span><span class="s2">&quot;server&quot;</span><span class="p">,</span>
    <span class="n">hostname</span><span class="o">=</span><span class="s2">&quot;tf.coreos2&quot;</span><span class="p">,</span>
    <span class="n">plan</span><span class="o">=</span><span class="s2">&quot;c1.small.x86&quot;</span><span class="p">,</span>
    <span class="n">facilities</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;ewr1&quot;</span><span class="p">],</span>
    <span class="n">operating_system</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">billing_cycle</span><span class="o">=</span><span class="s2">&quot;hourly&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">local</span><span class="p">[</span><span class="s2">&quot;project_id&quot;</span><span class="p">])</span>
</pre></div>
</div>
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
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_organization</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.get_organization.AwaitableGetOrganizationResult<a class="headerlink" href="#pulumi_packet.get_organization" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_precreated_ip_block</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">address_family</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>float<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">facility</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.get_precreated_ip_block.AwaitableGetPrecreatedIpBlockResult<a class="headerlink" href="#pulumi_packet.get_precreated_ip_block" title="Permalink to this definition">¶</a></dt>
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
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_project</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.get_project.AwaitableGetProjectResult<a class="headerlink" href="#pulumi_packet.get_project" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this datasource to retrieve attributes of the Project API resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_packet</span> <span class="k">as</span> <span class="nn">packet</span>

<span class="n">tf_project1</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">get_project</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Terraform Fun&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;usersOfTerraformFun&quot;</span><span class="p">,</span> <span class="n">tf_project1</span><span class="o">.</span><span class="n">user_ids</span><span class="p">)</span>
</pre></div>
</div>
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
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_spot_market_price</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">facility</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.get_spot_market_price.AwaitableGetSpotMarketPriceResult<a class="headerlink" href="#pulumi_packet.get_spot_market_price" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get Packet Spot Market Price.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_packet</span> <span class="k">as</span> <span class="nn">packet</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">get_spot_market_price</span><span class="p">(</span><span class="n">facility</span><span class="o">=</span><span class="s2">&quot;ewr1&quot;</span><span class="p">,</span>
    <span class="n">plan</span><span class="o">=</span><span class="s2">&quot;c1.small.x86&quot;</span><span class="p">)</span>
</pre></div>
</div>
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
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_spot_market_request</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">request_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.get_spot_market_request.AwaitableGetSpotMarketRequestResult<a class="headerlink" href="#pulumi_packet.get_spot_market_request" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>request_id</strong> (<em>str</em>) – The id of the Spot Market Request</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_packet.get_volume">
<code class="sig-prename descclassname">pulumi_packet.</code><code class="sig-name descname">get_volume</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_packet.get_volume.AwaitableGetVolumeResult<a class="headerlink" href="#pulumi_packet.get_volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Packet Block Storage Volume datasource to allow you to read existing volumes.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_packet</span> <span class="k">as</span> <span class="nn">packet</span>

<span class="n">volume1</span> <span class="o">=</span> <span class="n">packet</span><span class="o">.</span><span class="n">get_volume</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;terraform-volume-1&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">local</span><span class="p">[</span><span class="s2">&quot;project_id&quot;</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;volumeSize&quot;</span><span class="p">,</span> <span class="n">volume1</span><span class="o">.</span><span class="n">size</span><span class="p">)</span>
</pre></div>
</div>
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
