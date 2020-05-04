---
title: Module directconnect
title_tag: Module directconnect | Package pulumi_aws | Python SDK
linktitle: directconnect
notitle: true
---

<div class="section" id="directconnect">
<h1>directconnect<a class="headerlink" href="#directconnect" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.directconnect"></span><dl class="py class">
<dt id="pulumi_aws.directconnect.AwaitableGetGatewayResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">AwaitableGetGatewayResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">amazon_side_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_account_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.AwaitableGetGatewayResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.directconnect.BgpPeer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">BgpPeer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_auth_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtual_interface_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Direct Connect BGP peer resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p></li>
<li><p><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon.
Required for IPv4 BGP peers on public virtual interfaces.</p></li>
<li><p><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p></li>
<li><p><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</p></li>
<li><p><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic.
Required for IPv4 BGP peers on public virtual interfaces.</p></li>
<li><p><strong>virtual_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect virtual interface on which to create the BGP peer.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.directconnect.BgpPeer.address_family">
<code class="sig-name descname">address_family</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p>The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.BgpPeer.amazon_address">
<code class="sig-name descname">amazon_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.amazon_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR address to use to send traffic to Amazon.
Required for IPv4 BGP peers on public virtual interfaces.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.BgpPeer.aws_device">
<code class="sig-name descname">aws_device</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.aws_device" title="Permalink to this definition">¶</a></dt>
<dd><p>The Direct Connect endpoint on which the BGP peer terminates.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.BgpPeer.bgp_asn">
<code class="sig-name descname">bgp_asn</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.bgp_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.BgpPeer.bgp_auth_key">
<code class="sig-name descname">bgp_auth_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.bgp_auth_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication key for BGP configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.BgpPeer.bgp_peer_id">
<code class="sig-name descname">bgp_peer_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.bgp_peer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the BGP peer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.BgpPeer.bgp_status">
<code class="sig-name descname">bgp_status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.bgp_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The Up/Down state of the BGP peer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.BgpPeer.customer_address">
<code class="sig-name descname">customer_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.customer_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR destination address to which Amazon should send traffic.
Required for IPv4 BGP peers on public virtual interfaces.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.BgpPeer.virtual_interface_id">
<code class="sig-name descname">virtual_interface_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.virtual_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect virtual interface on which to create the BGP peer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.BgpPeer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_auth_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_peer_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtual_interface_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BgpPeer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p></li>
<li><p><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon.
Required for IPv4 BGP peers on public virtual interfaces.</p></li>
<li><p><strong>aws_device</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Direct Connect endpoint on which the BGP peer terminates.</p></li>
<li><p><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p></li>
<li><p><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</p></li>
<li><p><strong>bgp_peer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the BGP peer.</p></li>
<li><p><strong>bgp_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Up/Down state of the BGP peer.</p></li>
<li><p><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic.
Required for IPv4 BGP peers on public virtual interfaces.</p></li>
<li><p><strong>virtual_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect virtual interface on which to create the BGP peer.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.BgpPeer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.BgpPeer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.Connection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">Connection</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.Connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Connection of Direct Connect.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The bandwidth of the connection. Valid values for dedicated connections: 1Gbps, 10Gbps. Valid values for hosted connections: 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps and 10Gbps. Case sensitive.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Direct Connect location where the connection is located. See <a class="reference external" href="https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html">DescribeLocations</a> for the list of AWS Direct Connect locations. Use <code class="docutils literal notranslate"><span class="pre">locationCode</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the connection.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.directconnect.Connection.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Connection.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the connection.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.Connection.aws_device">
<code class="sig-name descname">aws_device</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Connection.aws_device" title="Permalink to this definition">¶</a></dt>
<dd><p>The Direct Connect endpoint on which the physical connection terminates.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.Connection.bandwidth">
<code class="sig-name descname">bandwidth</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Connection.bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>The bandwidth of the connection. Valid values for dedicated connections: 1Gbps, 10Gbps. Valid values for hosted connections: 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps and 10Gbps. Case sensitive.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.Connection.has_logical_redundancy">
<code class="sig-name descname">has_logical_redundancy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Connection.has_logical_redundancy" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.Connection.jumbo_frame_capable">
<code class="sig-name descname">jumbo_frame_capable</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Connection.jumbo_frame_capable" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value representing if jumbo frames have been enabled for this connection.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.Connection.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Connection.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Direct Connect location where the connection is located. See <a class="reference external" href="https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html">DescribeLocations</a> for the list of AWS Direct Connect locations. Use <code class="docutils literal notranslate"><span class="pre">locationCode</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.Connection.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Connection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the connection.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.Connection.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Connection.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.Connection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_logical_redundancy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jumbo_frame_capable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.Connection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Connection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the connection.</p></li>
<li><p><strong>aws_device</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Direct Connect endpoint on which the physical connection terminates.</p></li>
<li><p><strong>bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The bandwidth of the connection. Valid values for dedicated connections: 1Gbps, 10Gbps. Valid values for hosted connections: 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps and 10Gbps. Case sensitive.</p></li>
<li><p><strong>has_logical_redundancy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).</p></li>
<li><p><strong>jumbo_frame_capable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value representing if jumbo frames have been enabled for this connection.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The AWS Direct Connect location where the connection is located. See <a class="reference external" href="https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html">DescribeLocations</a> for the list of AWS Direct Connect locations. Use <code class="docutils literal notranslate"><span class="pre">locationCode</span></code>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the connection.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.Connection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.Connection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.Connection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.Connection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.ConnectionAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">ConnectionAssociation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lag_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.ConnectionAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates a Direct Connect Connection with a LAG.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the connection.</p></li>
<li><p><strong>lag_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the LAG with which to associate the connection.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.directconnect.ConnectionAssociation.connection_id">
<code class="sig-name descname">connection_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.ConnectionAssociation.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the connection.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.ConnectionAssociation.lag_id">
<code class="sig-name descname">lag_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.ConnectionAssociation.lag_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the LAG with which to associate the connection.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.ConnectionAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lag_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.ConnectionAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ConnectionAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the connection.</p></li>
<li><p><strong>lag_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the LAG with which to associate the connection.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.ConnectionAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.ConnectionAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.ConnectionAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.ConnectionAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.Gateway">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">Gateway</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_side_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.Gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Direct Connect Gateway.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>amazon_side_asn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ASN to be configured on the Amazon side of the connection. The ASN must be in the private range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the connection.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.directconnect.Gateway.amazon_side_asn">
<code class="sig-name descname">amazon_side_asn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Gateway.amazon_side_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ASN to be configured on the Amazon side of the connection. The ASN must be in the private range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.Gateway.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Gateway.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the connection.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.Gateway.owner_account_id">
<code class="sig-name descname">owner_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Gateway.owner_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS Account ID of the gateway.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.Gateway.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_side_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_account_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.Gateway.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Gateway resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>amazon_side_asn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ASN to be configured on the Amazon side of the connection. The ASN must be in the private range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the connection.</p></li>
<li><p><strong>owner_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS Account ID of the gateway.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.Gateway.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.Gateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.Gateway.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.Gateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.GatewayAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">GatewayAssociation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_prefixes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">associated_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">associated_gateway_owner_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dx_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proposal_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates a Direct Connect Gateway with a VGW or transit gateway.</p>
<p>To create a cross-account association, create an <cite>``directconnect.GatewayAssociationProposal`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/dx_gateway_association_proposal.html">https://www.terraform.io/docs/providers/aws/r/dx_gateway_association_proposal.html</a>&gt;`_
in the AWS account that owns the VGW or transit gateway and then accept the proposal in the AWS account that owns the Direct Connect Gateway
by creating an <code class="docutils literal notranslate"><span class="pre">directconnect.GatewayAssociation</span></code> resource with the <code class="docutils literal notranslate"><span class="pre">proposal_id</span></code> and <code class="docutils literal notranslate"><span class="pre">associated_gateway_owner_account_id</span></code> attributes set.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.</p></li>
<li><p><strong>associated_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for single account Direct Connect gateway associations.</p></li>
<li><p><strong>associated_gateway_owner_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for cross-account Direct Connect gateway associations.</p></li>
<li><p><strong>dx_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect gateway.</p></li>
<li><p><strong>proposal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect gateway association proposal.
Used for cross-account Direct Connect gateway associations.</p></li>
<li><p><strong>vpn_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">associated_gateway_id</span></code> instead. The ID of the VGW with which to associate the gateway.
Used for single account Direct Connect gateway associations.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociation.allowed_prefixes">
<code class="sig-name descname">allowed_prefixes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.allowed_prefixes" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociation.associated_gateway_id">
<code class="sig-name descname">associated_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.associated_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for single account Direct Connect gateway associations.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociation.associated_gateway_owner_account_id">
<code class="sig-name descname">associated_gateway_owner_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.associated_gateway_owner_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for cross-account Direct Connect gateway associations.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociation.associated_gateway_type">
<code class="sig-name descname">associated_gateway_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.associated_gateway_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the associated gateway, <code class="docutils literal notranslate"><span class="pre">transitGateway</span></code> or <code class="docutils literal notranslate"><span class="pre">virtualPrivateGateway</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociation.dx_gateway_association_id">
<code class="sig-name descname">dx_gateway_association_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.dx_gateway_association_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect gateway association.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociation.dx_gateway_id">
<code class="sig-name descname">dx_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.dx_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociation.dx_gateway_owner_account_id">
<code class="sig-name descname">dx_gateway_owner_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.dx_gateway_owner_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the Direct Connect gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociation.proposal_id">
<code class="sig-name descname">proposal_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.proposal_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect gateway association proposal.
Used for cross-account Direct Connect gateway associations.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociation.vpn_gateway_id">
<code class="sig-name descname">vpn_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.vpn_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p><em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">associated_gateway_id</span></code> instead. The ID of the VGW with which to associate the gateway.
Used for single account Direct Connect gateway associations.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.GatewayAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_prefixes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">associated_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">associated_gateway_owner_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">associated_gateway_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dx_gateway_association_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dx_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dx_gateway_owner_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proposal_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GatewayAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.</p></li>
<li><p><strong>associated_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for single account Direct Connect gateway associations.</p></li>
<li><p><strong>associated_gateway_owner_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for cross-account Direct Connect gateway associations.</p></li>
<li><p><strong>associated_gateway_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the associated gateway, <code class="docutils literal notranslate"><span class="pre">transitGateway</span></code> or <code class="docutils literal notranslate"><span class="pre">virtualPrivateGateway</span></code>.</p></li>
<li><p><strong>dx_gateway_association_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect gateway association.</p></li>
<li><p><strong>dx_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect gateway.</p></li>
<li><p><strong>dx_gateway_owner_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the AWS account that owns the Direct Connect gateway.</p></li>
<li><p><strong>proposal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect gateway association proposal.
Used for cross-account Direct Connect gateway associations.</p></li>
<li><p><strong>vpn_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">associated_gateway_id</span></code> instead. The ID of the VGW with which to associate the gateway.
Used for single account Direct Connect gateway associations.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.GatewayAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.GatewayAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">GatewayAssociationProposal</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_prefixes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">associated_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dx_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dx_gateway_owner_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Direct Connect Gateway Association Proposal, typically for enabling cross-account associations. For single account associations, see the <cite>``directconnect.GatewayAssociation`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/dx_gateway_association.html">https://www.terraform.io/docs/providers/aws/r/dx_gateway_association.html</a>&gt;`_.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.</p></li>
<li><p><strong>associated_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.</p></li>
<li><p><strong>dx_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Direct Connect Gateway identifier.</p></li>
<li><p><strong>dx_gateway_owner_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS Account identifier of the Direct Connect Gateway’s owner.</p></li>
<li><p><strong>vpn_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">associated_gateway_id</span></code> instead. Virtual Gateway identifier to associate with the Direct Connect Gateway.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.allowed_prefixes">
<code class="sig-name descname">allowed_prefixes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.allowed_prefixes" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.associated_gateway_id">
<code class="sig-name descname">associated_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.associated_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.associated_gateway_owner_account_id">
<code class="sig-name descname">associated_gateway_owner_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.associated_gateway_owner_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.associated_gateway_type">
<code class="sig-name descname">associated_gateway_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.associated_gateway_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the associated gateway, <code class="docutils literal notranslate"><span class="pre">transitGateway</span></code> or <code class="docutils literal notranslate"><span class="pre">virtualPrivateGateway</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.dx_gateway_id">
<code class="sig-name descname">dx_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.dx_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Direct Connect Gateway identifier.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.dx_gateway_owner_account_id">
<code class="sig-name descname">dx_gateway_owner_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.dx_gateway_owner_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS Account identifier of the Direct Connect Gateway’s owner.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.vpn_gateway_id">
<code class="sig-name descname">vpn_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.vpn_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p><em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">associated_gateway_id</span></code> instead. Virtual Gateway identifier to associate with the Direct Connect Gateway.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allowed_prefixes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">associated_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">associated_gateway_owner_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">associated_gateway_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dx_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dx_gateway_owner_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GatewayAssociationProposal resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allowed_prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.</p></li>
<li><p><strong>associated_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.</p></li>
<li><p><strong>associated_gateway_owner_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.</p></li>
<li><p><strong>associated_gateway_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the associated gateway, <code class="docutils literal notranslate"><span class="pre">transitGateway</span></code> or <code class="docutils literal notranslate"><span class="pre">virtualPrivateGateway</span></code>.</p></li>
<li><p><strong>dx_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Direct Connect Gateway identifier.</p></li>
<li><p><strong>dx_gateway_owner_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS Account identifier of the Direct Connect Gateway’s owner.</p></li>
<li><p><strong>vpn_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">associated_gateway_id</span></code> instead. Virtual Gateway identifier to associate with the Direct Connect Gateway.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.GetGatewayResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">GetGatewayResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">amazon_side_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_account_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.GetGatewayResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGateway.</p>
<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GetGatewayResult.amazon_side_asn">
<code class="sig-name descname">amazon_side_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GetGatewayResult.amazon_side_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ASN on the Amazon side of the connection.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GetGatewayResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GetGatewayResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.GetGatewayResult.owner_account_id">
<code class="sig-name descname">owner_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GetGatewayResult.owner_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS Account ID of the gateway.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">HostedPrivateVirtualInterface</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_auth_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mtu</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vlan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Direct Connect hosted private virtual interface resource. This resource represents the allocator’s side of the hosted virtual interface.
A hosted virtual interface is a virtual interface that is owned by another AWS account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p></li>
<li><p><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p></li>
<li><p><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p></li>
<li><p><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p></li>
<li><p><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p></li>
<li><p><strong>mtu</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a virtual private interface can be either <code class="docutils literal notranslate"><span class="pre">1500</span></code> or <code class="docutils literal notranslate"><span class="pre">9001</span></code> (jumbo frames). Default is <code class="docutils literal notranslate"><span class="pre">1500</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the virtual interface.</p></li>
<li><p><strong>owner_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS account that will own the new virtual interface.</p></li>
<li><p><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The VLAN ID.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.address_family">
<code class="sig-name descname">address_family</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p>The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.amazon_address">
<code class="sig-name descname">amazon_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.amazon_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.aws_device">
<code class="sig-name descname">aws_device</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.aws_device" title="Permalink to this definition">¶</a></dt>
<dd><p>The Direct Connect endpoint on which the virtual interface terminates.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.bgp_asn">
<code class="sig-name descname">bgp_asn</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.bgp_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.bgp_auth_key">
<code class="sig-name descname">bgp_auth_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.bgp_auth_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication key for BGP configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.connection_id">
<code class="sig-name descname">connection_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.customer_address">
<code class="sig-name descname">customer_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.customer_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.jumbo_frame_capable">
<code class="sig-name descname">jumbo_frame_capable</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.jumbo_frame_capable" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether jumbo frames (9001 MTU) are supported.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.mtu">
<code class="sig-name descname">mtu</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.mtu" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a virtual private interface can be either <code class="docutils literal notranslate"><span class="pre">1500</span></code> or <code class="docutils literal notranslate"><span class="pre">9001</span></code> (jumbo frames). Default is <code class="docutils literal notranslate"><span class="pre">1500</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.owner_account_id">
<code class="sig-name descname">owner_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.owner_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account that will own the new virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.vlan">
<code class="sig-name descname">vlan</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.vlan" title="Permalink to this definition">¶</a></dt>
<dd><p>The VLAN ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_side_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_auth_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jumbo_frame_capable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mtu</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vlan</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HostedPrivateVirtualInterface resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p></li>
<li><p><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the virtual interface.</p></li>
<li><p><strong>aws_device</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Direct Connect endpoint on which the virtual interface terminates.</p></li>
<li><p><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p></li>
<li><p><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p></li>
<li><p><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p></li>
<li><p><strong>jumbo_frame_capable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether jumbo frames (9001 MTU) are supported.</p></li>
<li><p><strong>mtu</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a virtual private interface can be either <code class="docutils literal notranslate"><span class="pre">1500</span></code> or <code class="docutils literal notranslate"><span class="pre">9001</span></code> (jumbo frames). Default is <code class="docutils literal notranslate"><span class="pre">1500</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the virtual interface.</p></li>
<li><p><strong>owner_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS account that will own the new virtual interface.</p></li>
<li><p><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The VLAN ID.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">HostedPrivateVirtualInterfaceAccepter</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dx_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtual_interface_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage the accepter’s side of a Direct Connect hosted private virtual interface.
This resource accepts ownership of a private virtual interface created by another AWS account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dx_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect gateway to which to connect the virtual interface.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>virtual_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect virtual interface to accept.</p></li>
<li><p><strong>vpn_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the virtual private gateway to which to connect the virtual interface.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.dx_gateway_id">
<code class="sig-name descname">dx_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.dx_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect gateway to which to connect the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.virtual_interface_id">
<code class="sig-name descname">virtual_interface_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.virtual_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect virtual interface to accept.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.vpn_gateway_id">
<code class="sig-name descname">vpn_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.vpn_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the virtual private gateway to which to connect the virtual interface.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dx_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtual_interface_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HostedPrivateVirtualInterfaceAccepter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the virtual interface.</p></li>
<li><p><strong>dx_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect gateway to which to connect the virtual interface.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>virtual_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect virtual interface to accept.</p></li>
<li><p><strong>vpn_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the virtual private gateway to which to connect the virtual interface.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">HostedPublicVirtualInterface</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_auth_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_filter_prefixes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vlan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Direct Connect hosted public virtual interface resource. This resource represents the allocator’s side of the hosted virtual interface.
A hosted virtual interface is a virtual interface that is owned by another AWS account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p></li>
<li><p><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p></li>
<li><p><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p></li>
<li><p><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p></li>
<li><p><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the virtual interface.</p></li>
<li><p><strong>owner_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS account that will own the new virtual interface.</p></li>
<li><p><strong>route_filter_prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of routes to be advertised to the AWS network in this region.</p></li>
<li><p><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The VLAN ID.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.address_family">
<code class="sig-name descname">address_family</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p>The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.amazon_address">
<code class="sig-name descname">amazon_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.amazon_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.aws_device">
<code class="sig-name descname">aws_device</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.aws_device" title="Permalink to this definition">¶</a></dt>
<dd><p>The Direct Connect endpoint on which the virtual interface terminates.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.bgp_asn">
<code class="sig-name descname">bgp_asn</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.bgp_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.bgp_auth_key">
<code class="sig-name descname">bgp_auth_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.bgp_auth_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication key for BGP configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.connection_id">
<code class="sig-name descname">connection_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.customer_address">
<code class="sig-name descname">customer_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.customer_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.owner_account_id">
<code class="sig-name descname">owner_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.owner_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account that will own the new virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.route_filter_prefixes">
<code class="sig-name descname">route_filter_prefixes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.route_filter_prefixes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of routes to be advertised to the AWS network in this region.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.vlan">
<code class="sig-name descname">vlan</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.vlan" title="Permalink to this definition">¶</a></dt>
<dd><p>The VLAN ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_side_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_auth_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_filter_prefixes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vlan</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HostedPublicVirtualInterface resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p></li>
<li><p><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the virtual interface.</p></li>
<li><p><strong>aws_device</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Direct Connect endpoint on which the virtual interface terminates.</p></li>
<li><p><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p></li>
<li><p><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p></li>
<li><p><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the virtual interface.</p></li>
<li><p><strong>owner_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS account that will own the new virtual interface.</p></li>
<li><p><strong>route_filter_prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of routes to be advertised to the AWS network in this region.</p></li>
<li><p><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The VLAN ID.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">HostedPublicVirtualInterfaceAccepter</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtual_interface_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage the accepter’s side of a Direct Connect hosted public virtual interface.
This resource accepts ownership of a public virtual interface created by another AWS account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>virtual_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect virtual interface to accept.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.virtual_interface_id">
<code class="sig-name descname">virtual_interface_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.virtual_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect virtual interface to accept.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtual_interface_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HostedPublicVirtualInterfaceAccepter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the virtual interface.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>virtual_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect virtual interface to accept.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterface">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">HostedTransitVirtualInterface</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_auth_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mtu</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vlan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Direct Connect hosted transit virtual interface resource.
This resource represents the allocator’s side of the hosted virtual interface.
A hosted virtual interface is a virtual interface that is owned by another AWS account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p></li>
<li><p><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p></li>
<li><p><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p></li>
<li><p><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p></li>
<li><p><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p></li>
<li><p><strong>mtu</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a virtual transit interface can be either <code class="docutils literal notranslate"><span class="pre">1500</span></code> or <code class="docutils literal notranslate"><span class="pre">8500</span></code> (jumbo frames). Default is <code class="docutils literal notranslate"><span class="pre">1500</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the virtual interface.</p></li>
<li><p><strong>owner_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS account that will own the new virtual interface.</p></li>
<li><p><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The VLAN ID.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterface.address_family">
<code class="sig-name descname">address_family</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterface.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p>The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterface.amazon_address">
<code class="sig-name descname">amazon_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterface.amazon_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterface.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterface.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterface.aws_device">
<code class="sig-name descname">aws_device</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterface.aws_device" title="Permalink to this definition">¶</a></dt>
<dd><p>The Direct Connect endpoint on which the virtual interface terminates.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterface.bgp_asn">
<code class="sig-name descname">bgp_asn</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterface.bgp_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterface.bgp_auth_key">
<code class="sig-name descname">bgp_auth_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterface.bgp_auth_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication key for BGP configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterface.connection_id">
<code class="sig-name descname">connection_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterface.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterface.customer_address">
<code class="sig-name descname">customer_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterface.customer_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterface.jumbo_frame_capable">
<code class="sig-name descname">jumbo_frame_capable</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterface.jumbo_frame_capable" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether jumbo frames (8500 MTU) are supported.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterface.mtu">
<code class="sig-name descname">mtu</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterface.mtu" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a virtual transit interface can be either <code class="docutils literal notranslate"><span class="pre">1500</span></code> or <code class="docutils literal notranslate"><span class="pre">8500</span></code> (jumbo frames). Default is <code class="docutils literal notranslate"><span class="pre">1500</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterface.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterface.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterface.owner_account_id">
<code class="sig-name descname">owner_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterface.owner_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account that will own the new virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterface.vlan">
<code class="sig-name descname">vlan</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterface.vlan" title="Permalink to this definition">¶</a></dt>
<dd><p>The VLAN ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterface.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_side_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_auth_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jumbo_frame_capable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mtu</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vlan</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterface.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HostedTransitVirtualInterface resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p></li>
<li><p><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the virtual interface.</p></li>
<li><p><strong>aws_device</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Direct Connect endpoint on which the virtual interface terminates.</p></li>
<li><p><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p></li>
<li><p><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p></li>
<li><p><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p></li>
<li><p><strong>jumbo_frame_capable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether jumbo frames (8500 MTU) are supported.</p></li>
<li><p><strong>mtu</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a virtual transit interface can be either <code class="docutils literal notranslate"><span class="pre">1500</span></code> or <code class="docutils literal notranslate"><span class="pre">8500</span></code> (jumbo frames). Default is <code class="docutils literal notranslate"><span class="pre">1500</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the virtual interface.</p></li>
<li><p><strong>owner_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS account that will own the new virtual interface.</p></li>
<li><p><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The VLAN ID.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterface.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterface.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterface.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterface.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterfaceAcceptor">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">HostedTransitVirtualInterfaceAcceptor</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dx_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtual_interface_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterfaceAcceptor" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage the accepter’s side of a Direct Connect hosted transit virtual interface.
This resource accepts ownership of a transit virtual interface created by another AWS account.</p>
<blockquote>
<div><p><strong>NOTE:</strong> AWS allows a Direct Connect hosted transit virtual interface to be deleted from either the allocator’s or accepter’s side. However, this provider only allows the Direct Connect hosted transit virtual interface to be deleted from the allocator’s side by removing the corresponding <code class="docutils literal notranslate"><span class="pre">directconnect.HostedTransitVirtualInterface</span></code> resource from your configuration. Removing a <code class="docutils literal notranslate"><span class="pre">directconnect.HostedTransitVirtualInterfaceAcceptor</span></code> resource from your configuration will remove it from your statefile and management, <strong>but will not delete the Direct Connect virtual interface.</strong></p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dx_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect gateway to which to connect the virtual interface.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>virtual_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect virtual interface to accept.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterfaceAcceptor.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterfaceAcceptor.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterfaceAcceptor.dx_gateway_id">
<code class="sig-name descname">dx_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterfaceAcceptor.dx_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect gateway to which to connect the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterfaceAcceptor.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterfaceAcceptor.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterfaceAcceptor.virtual_interface_id">
<code class="sig-name descname">virtual_interface_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterfaceAcceptor.virtual_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect virtual interface to accept.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterfaceAcceptor.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dx_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">virtual_interface_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterfaceAcceptor.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HostedTransitVirtualInterfaceAcceptor resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the virtual interface.</p></li>
<li><p><strong>dx_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect gateway to which to connect the virtual interface.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>virtual_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect virtual interface to accept.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterfaceAcceptor.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterfaceAcceptor.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.HostedTransitVirtualInterfaceAcceptor.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedTransitVirtualInterfaceAcceptor.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.LinkAggregationGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">LinkAggregationGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connections_bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_destroy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Direct Connect LAG. Connections can be added to the LAG via the <cite>``directconnect.Connection`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/dx_connection.html">https://www.terraform.io/docs/providers/aws/r/dx_connection.html</a>&gt;`_ and <cite>``directconnect.ConnectionAssociation`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/dx_connection_association.html">https://www.terraform.io/docs/providers/aws/r/dx_connection_association.html</a>&gt;`_ resources.</p>
<blockquote>
<div><p><em>NOTE:</em> When creating a LAG, Direct Connect requires creating a Connection. This provider will remove this unmanaged connection during resource creation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connections_bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The bandwidth of the individual physical connections bundled by the LAG. Valid values: 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps and 10Gbps. Case sensitive.</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean that indicates all connections associated with the LAG should be deleted so that the LAG can be destroyed without error. These objects are <em>not</em> recoverable.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The AWS Direct Connect location in which the LAG should be allocated. See <a class="reference external" href="https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html">DescribeLocations</a> for the list of AWS Direct Connect locations. Use <code class="docutils literal notranslate"><span class="pre">locationCode</span></code>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the LAG.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the LAG.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">jumbo_frame_capable</span></code> -Indicates whether jumbo frames (9001 MTU) are supported.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.connections_bandwidth">
<code class="sig-name descname">connections_bandwidth</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.connections_bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>The bandwidth of the individual physical connections bundled by the LAG. Valid values: 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps and 10Gbps. Case sensitive.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.force_destroy">
<code class="sig-name descname">force_destroy</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean that indicates all connections associated with the LAG should be deleted so that the LAG can be destroyed without error. These objects are <em>not</em> recoverable.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.has_logical_redundancy">
<code class="sig-name descname">has_logical_redundancy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.has_logical_redundancy" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the LAG supports a secondary BGP peer in the same address family (IPv4/IPv6).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Direct Connect location in which the LAG should be allocated. See <a class="reference external" href="https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html">DescribeLocations</a> for the list of AWS Direct Connect locations. Use <code class="docutils literal notranslate"><span class="pre">locationCode</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the LAG.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connections_bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_destroy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_logical_redundancy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jumbo_frame_capable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LinkAggregationGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the LAG.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `jumbo_frame_capable` -Indicates whether jumbo frames (9001 MTU) are supported.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>connections_bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The bandwidth of the individual physical connections bundled by the LAG. Valid values: 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps and 10Gbps. Case sensitive.</p></li>
<li><p><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean that indicates all connections associated with the LAG should be deleted so that the LAG can be destroyed without error. These objects are <em>not</em> recoverable.</p></li>
<li><p><strong>has_logical_redundancy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether the LAG supports a secondary BGP peer in the same address family (IPv4/IPv6).</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The AWS Direct Connect location in which the LAG should be allocated. See <a class="reference external" href="https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html">DescribeLocations</a> for the list of AWS Direct Connect locations. Use <code class="docutils literal notranslate"><span class="pre">locationCode</span></code>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the LAG.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">PrivateVirtualInterface</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_auth_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dx_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mtu</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vlan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Direct Connect private virtual interface resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p></li>
<li><p><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p></li>
<li><p><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p></li>
<li><p><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p></li>
<li><p><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p></li>
<li><p><strong>dx_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect gateway to which to connect the virtual interface.</p></li>
<li><p><strong>mtu</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection.
The MTU of a virtual private interface can be either <code class="docutils literal notranslate"><span class="pre">1500</span></code> or <code class="docutils literal notranslate"><span class="pre">9001</span></code> (jumbo frames). Default is <code class="docutils literal notranslate"><span class="pre">1500</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the virtual interface.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The VLAN ID.</p></li>
<li><p><strong>vpn_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the virtual private gateway to which to connect the virtual interface.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.address_family">
<code class="sig-name descname">address_family</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p>The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.amazon_address">
<code class="sig-name descname">amazon_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.amazon_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.aws_device">
<code class="sig-name descname">aws_device</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.aws_device" title="Permalink to this definition">¶</a></dt>
<dd><p>The Direct Connect endpoint on which the virtual interface terminates.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.bgp_asn">
<code class="sig-name descname">bgp_asn</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.bgp_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.bgp_auth_key">
<code class="sig-name descname">bgp_auth_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.bgp_auth_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication key for BGP configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.connection_id">
<code class="sig-name descname">connection_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.customer_address">
<code class="sig-name descname">customer_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.customer_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.dx_gateway_id">
<code class="sig-name descname">dx_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.dx_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect gateway to which to connect the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.jumbo_frame_capable">
<code class="sig-name descname">jumbo_frame_capable</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.jumbo_frame_capable" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether jumbo frames (9001 MTU) are supported.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.mtu">
<code class="sig-name descname">mtu</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.mtu" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection.
The MTU of a virtual private interface can be either <code class="docutils literal notranslate"><span class="pre">1500</span></code> or <code class="docutils literal notranslate"><span class="pre">9001</span></code> (jumbo frames). Default is <code class="docutils literal notranslate"><span class="pre">1500</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.vlan">
<code class="sig-name descname">vlan</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.vlan" title="Permalink to this definition">¶</a></dt>
<dd><p>The VLAN ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.vpn_gateway_id">
<code class="sig-name descname">vpn_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.vpn_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the virtual private gateway to which to connect the virtual interface.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_side_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_auth_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dx_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jumbo_frame_capable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mtu</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vlan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PrivateVirtualInterface resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p></li>
<li><p><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the virtual interface.</p></li>
<li><p><strong>aws_device</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Direct Connect endpoint on which the virtual interface terminates.</p></li>
<li><p><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p></li>
<li><p><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p></li>
<li><p><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p></li>
<li><p><strong>dx_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect gateway to which to connect the virtual interface.</p></li>
<li><p><strong>jumbo_frame_capable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether jumbo frames (9001 MTU) are supported.</p></li>
<li><p><strong>mtu</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection.
The MTU of a virtual private interface can be either <code class="docutils literal notranslate"><span class="pre">1500</span></code> or <code class="docutils literal notranslate"><span class="pre">9001</span></code> (jumbo frames). Default is <code class="docutils literal notranslate"><span class="pre">1500</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the virtual interface.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The VLAN ID.</p></li>
<li><p><strong>vpn_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the virtual private gateway to which to connect the virtual interface.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.PublicVirtualInterface">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">PublicVirtualInterface</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_auth_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_filter_prefixes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vlan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Direct Connect public virtual interface resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p></li>
<li><p><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p></li>
<li><p><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p></li>
<li><p><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p></li>
<li><p><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the virtual interface.</p></li>
<li><p><strong>route_filter_prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of routes to be advertised to the AWS network in this region.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The VLAN ID.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.address_family">
<code class="sig-name descname">address_family</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p>The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.amazon_address">
<code class="sig-name descname">amazon_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.amazon_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.aws_device">
<code class="sig-name descname">aws_device</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.aws_device" title="Permalink to this definition">¶</a></dt>
<dd><p>The Direct Connect endpoint on which the virtual interface terminates.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.bgp_asn">
<code class="sig-name descname">bgp_asn</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.bgp_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.bgp_auth_key">
<code class="sig-name descname">bgp_auth_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.bgp_auth_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication key for BGP configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.connection_id">
<code class="sig-name descname">connection_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.customer_address">
<code class="sig-name descname">customer_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.customer_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.route_filter_prefixes">
<code class="sig-name descname">route_filter_prefixes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.route_filter_prefixes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of routes to be advertised to the AWS network in this region.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.vlan">
<code class="sig-name descname">vlan</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.vlan" title="Permalink to this definition">¶</a></dt>
<dd><p>The VLAN ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_side_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_auth_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_filter_prefixes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vlan</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PublicVirtualInterface resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p></li>
<li><p><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the virtual interface.</p></li>
<li><p><strong>aws_device</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Direct Connect endpoint on which the virtual interface terminates.</p></li>
<li><p><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p></li>
<li><p><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p></li>
<li><p><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the virtual interface.</p></li>
<li><p><strong>route_filter_prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of routes to be advertised to the AWS network in this region.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The VLAN ID.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.TransitVirtualInterface">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">TransitVirtualInterface</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_auth_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dx_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mtu</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vlan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.TransitVirtualInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Direct Connect transit virtual interface resource.
A transit virtual interface is a VLAN that transports traffic from a Direct Connect gateway to one or more transit gateways.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p></li>
<li><p><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p></li>
<li><p><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p></li>
<li><p><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p></li>
<li><p><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p></li>
<li><p><strong>dx_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect gateway to which to connect the virtual interface.</p></li>
<li><p><strong>mtu</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection.
The MTU of a virtual transit interface can be either <code class="docutils literal notranslate"><span class="pre">1500</span></code> or <code class="docutils literal notranslate"><span class="pre">8500</span></code> (jumbo frames). Default is <code class="docutils literal notranslate"><span class="pre">1500</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the virtual interface.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The VLAN ID.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.directconnect.TransitVirtualInterface.address_family">
<code class="sig-name descname">address_family</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.TransitVirtualInterface.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p>The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.TransitVirtualInterface.amazon_address">
<code class="sig-name descname">amazon_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.TransitVirtualInterface.amazon_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.TransitVirtualInterface.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.TransitVirtualInterface.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.TransitVirtualInterface.aws_device">
<code class="sig-name descname">aws_device</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.TransitVirtualInterface.aws_device" title="Permalink to this definition">¶</a></dt>
<dd><p>The Direct Connect endpoint on which the virtual interface terminates.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.TransitVirtualInterface.bgp_asn">
<code class="sig-name descname">bgp_asn</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.TransitVirtualInterface.bgp_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.TransitVirtualInterface.bgp_auth_key">
<code class="sig-name descname">bgp_auth_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.TransitVirtualInterface.bgp_auth_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication key for BGP configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.TransitVirtualInterface.connection_id">
<code class="sig-name descname">connection_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.TransitVirtualInterface.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.TransitVirtualInterface.customer_address">
<code class="sig-name descname">customer_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.TransitVirtualInterface.customer_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.TransitVirtualInterface.dx_gateway_id">
<code class="sig-name descname">dx_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.TransitVirtualInterface.dx_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect gateway to which to connect the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.TransitVirtualInterface.jumbo_frame_capable">
<code class="sig-name descname">jumbo_frame_capable</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.TransitVirtualInterface.jumbo_frame_capable" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether jumbo frames (8500 MTU) are supported.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.TransitVirtualInterface.mtu">
<code class="sig-name descname">mtu</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.TransitVirtualInterface.mtu" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection.
The MTU of a virtual transit interface can be either <code class="docutils literal notranslate"><span class="pre">1500</span></code> or <code class="docutils literal notranslate"><span class="pre">8500</span></code> (jumbo frames). Default is <code class="docutils literal notranslate"><span class="pre">1500</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.TransitVirtualInterface.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.TransitVirtualInterface.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the virtual interface.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.TransitVirtualInterface.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.TransitVirtualInterface.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.directconnect.TransitVirtualInterface.vlan">
<code class="sig-name descname">vlan</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.TransitVirtualInterface.vlan" title="Permalink to this definition">¶</a></dt>
<dd><p>The VLAN ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.TransitVirtualInterface.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address_family</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_side_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_device</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bgp_auth_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dx_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jumbo_frame_capable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mtu</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vlan</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.TransitVirtualInterface.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TransitVirtualInterface resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p></li>
<li><p><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the virtual interface.</p></li>
<li><p><strong>aws_device</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Direct Connect endpoint on which the virtual interface terminates.</p></li>
<li><p><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p></li>
<li><p><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p></li>
<li><p><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p></li>
<li><p><strong>dx_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect gateway to which to connect the virtual interface.</p></li>
<li><p><strong>jumbo_frame_capable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether jumbo frames (8500 MTU) are supported.</p></li>
<li><p><strong>mtu</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection.
The MTU of a virtual transit interface can be either <code class="docutils literal notranslate"><span class="pre">1500</span></code> or <code class="docutils literal notranslate"><span class="pre">8500</span></code> (jumbo frames). Default is <code class="docutils literal notranslate"><span class="pre">1500</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the virtual interface.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The VLAN ID.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.directconnect.TransitVirtualInterface.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.TransitVirtualInterface.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.TransitVirtualInterface.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.TransitVirtualInterface.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.get_gateway">
<code class="sig-prename descclassname">pulumi_aws.directconnect.</code><code class="sig-name descname">get_gateway</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.get_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve information about a Direct Connect Gateway.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the gateway to retrieve.</p>
</dd>
</dl>
</dd></dl>

</div>
