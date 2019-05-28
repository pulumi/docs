---
---

<div class="section" id="module-pulumi_aws.directconnect">
<span id="directconnect"></span><h1>directconnect<a class="headerlink" href="#module-pulumi_aws.directconnect" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.directconnect.BgpPeer">
<em class="property">class </em><code class="descclassname">pulumi_aws.directconnect.</code><code class="descname">BgpPeer</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>address_family=None</em>, <em>amazon_address=None</em>, <em>bgp_asn=None</em>, <em>bgp_auth_key=None</em>, <em>customer_address=None</em>, <em>virtual_interface_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Direct Connect BGP peer resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</li>
<li><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon.
Required for IPv4 BGP peers on public virtual interfaces.</li>
<li><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</li>
<li><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</li>
<li><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic.
Required for IPv4 BGP peers on public virtual interfaces.</li>
<li><strong>virtual_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect virtual interface on which to create the BGP peer.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.directconnect.BgpPeer.address_family">
<code class="descname">address_family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p>The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.BgpPeer.amazon_address">
<code class="descname">amazon_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.amazon_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR address to use to send traffic to Amazon.
Required for IPv4 BGP peers on public virtual interfaces.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.BgpPeer.aws_device">
<code class="descname">aws_device</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.aws_device" title="Permalink to this definition">¶</a></dt>
<dd><p>The Direct Connect endpoint on which the BGP peer terminates.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.BgpPeer.bgp_asn">
<code class="descname">bgp_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.bgp_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.BgpPeer.bgp_auth_key">
<code class="descname">bgp_auth_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.bgp_auth_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication key for BGP configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.BgpPeer.bgp_peer_id">
<code class="descname">bgp_peer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.bgp_peer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the BGP peer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.BgpPeer.bgp_status">
<code class="descname">bgp_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.bgp_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The Up/Down state of the BGP peer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.BgpPeer.customer_address">
<code class="descname">customer_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.customer_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR destination address to which Amazon should send traffic.
Required for IPv4 BGP peers on public virtual interfaces.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.BgpPeer.virtual_interface_id">
<code class="descname">virtual_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.virtual_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect virtual interface on which to create the BGP peer.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directconnect.BgpPeer.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.BgpPeer.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.BgpPeer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.Connection">
<em class="property">class </em><code class="descclassname">pulumi_aws.directconnect.</code><code class="descname">Connection</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bandwidth=None</em>, <em>location=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.Connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Connection of Direct Connect.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The bandwidth of the connection. Available values: 1Gbps, 10Gbps. Case sensitive.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Direct Connect location where the connection is located. See <a class="reference external" href="https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html">DescribeLocations</a> for the list of AWS Direct Connect locations. Use <code class="docutils literal notranslate"><span class="pre">locationCode</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the connection.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.directconnect.Connection.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Connection.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.Connection.aws_device">
<code class="descname">aws_device</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Connection.aws_device" title="Permalink to this definition">¶</a></dt>
<dd><p>The Direct Connect endpoint on which the physical connection terminates.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.Connection.bandwidth">
<code class="descname">bandwidth</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Connection.bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>The bandwidth of the connection. Available values: 1Gbps, 10Gbps. Case sensitive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.Connection.has_logical_redundancy">
<code class="descname">has_logical_redundancy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Connection.has_logical_redundancy" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the connection supports a secondary BGP peer in the same address family (IPv4/IPv6).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.Connection.jumbo_frame_capable">
<code class="descname">jumbo_frame_capable</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Connection.jumbo_frame_capable" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value representing if jumbo frames have been enabled for this connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.Connection.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Connection.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Direct Connect location where the connection is located. See <a class="reference external" href="https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html">DescribeLocations</a> for the list of AWS Direct Connect locations. Use <code class="docutils literal notranslate"><span class="pre">locationCode</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.Connection.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Connection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.Connection.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Connection.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directconnect.Connection.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.Connection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.Connection.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.Connection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.ConnectionAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.directconnect.</code><code class="descname">ConnectionAssociation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>connection_id=None</em>, <em>lag_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.ConnectionAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates a Direct Connect Connection with a LAG.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the connection.</li>
<li><strong>lag_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the LAG with which to associate the connection.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.directconnect.ConnectionAssociation.connection_id">
<code class="descname">connection_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.ConnectionAssociation.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.ConnectionAssociation.lag_id">
<code class="descname">lag_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.ConnectionAssociation.lag_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the LAG with which to associate the connection.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directconnect.ConnectionAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.ConnectionAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.ConnectionAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.ConnectionAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.Gateway">
<em class="property">class </em><code class="descclassname">pulumi_aws.directconnect.</code><code class="descname">Gateway</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>amazon_side_asn=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.Gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Direct Connect Gateway.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>amazon_side_asn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ASN to be configured on the Amazon side of the connection. The ASN must be in the private range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the connection.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.directconnect.Gateway.amazon_side_asn">
<code class="descname">amazon_side_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Gateway.amazon_side_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ASN to be configured on the Amazon side of the connection. The ASN must be in the private range of 64,512 to 65,534 or 4,200,000,000 to 4,294,967,294.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.Gateway.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Gateway.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.Gateway.owner_account_id">
<code class="descname">owner_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.Gateway.owner_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS Account ID of the gateway.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directconnect.Gateway.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.Gateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.Gateway.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.Gateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.GatewayAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.directconnect.</code><code class="descname">GatewayAssociation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allowed_prefixes=None</em>, <em>associated_gateway_id=None</em>, <em>associated_gateway_owner_account_id=None</em>, <em>dx_gateway_id=None</em>, <em>proposal_id=None</em>, <em>vpn_gateway_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates a Direct Connect Gateway with a VGW or transit gateway.</p>
<p>To create a cross-account association, create an <cite>``aws_dx_gateway_association_proposal`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/dx_gateway_association_proposal.html">https://www.terraform.io/docs/providers/aws/r/dx_gateway_association_proposal.html</a>&gt;`_
in the AWS account that owns the VGW or transit gateway and then accept the proposal in the AWS account that owns the Direct Connect Gateway
by creating an <code class="docutils literal notranslate"><span class="pre">aws_dx_gateway_association</span></code> resource with the <code class="docutils literal notranslate"><span class="pre">proposal_id</span></code> and <code class="docutils literal notranslate"><span class="pre">associated_gateway_owner_account_id</span></code> attributes set.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allowed_prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.</li>
<li><strong>associated_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for single account Direct Connect gateway associations.</li>
<li><strong>associated_gateway_owner_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for cross-account Direct Connect gateway associations.</li>
<li><strong>dx_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect gateway.</li>
<li><strong>proposal_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect gateway association proposal.
Used for cross-account Direct Connect gateway associations.</li>
<li><strong>vpn_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">associated_gateway_id</span></code> instead. The ID of the VGW with which to associate the gateway.
Used for single account Direct Connect gateway associations.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociation.allowed_prefixes">
<code class="descname">allowed_prefixes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.allowed_prefixes" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociation.associated_gateway_id">
<code class="descname">associated_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.associated_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for single account Direct Connect gateway associations.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociation.associated_gateway_owner_account_id">
<code class="descname">associated_gateway_owner_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.associated_gateway_owner_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.
Used for cross-account Direct Connect gateway associations.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociation.associated_gateway_type">
<code class="descname">associated_gateway_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.associated_gateway_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the associated gateway, <code class="docutils literal notranslate"><span class="pre">transitGateway</span></code> or <code class="docutils literal notranslate"><span class="pre">virtualPrivateGateway</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociation.dx_gateway_association_id">
<code class="descname">dx_gateway_association_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.dx_gateway_association_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect gateway association.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociation.dx_gateway_id">
<code class="descname">dx_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.dx_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociation.dx_gateway_owner_account_id">
<code class="descname">dx_gateway_owner_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.dx_gateway_owner_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the Direct Connect gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociation.proposal_id">
<code class="descname">proposal_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.proposal_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect gateway association proposal.
Used for cross-account Direct Connect gateway associations.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociation.vpn_gateway_id">
<code class="descname">vpn_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.vpn_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p><em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">associated_gateway_id</span></code> instead. The ID of the VGW with which to associate the gateway.
Used for single account Direct Connect gateway associations.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directconnect.GatewayAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.GatewayAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal">
<em class="property">class </em><code class="descclassname">pulumi_aws.directconnect.</code><code class="descname">GatewayAssociationProposal</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allowed_prefixes=None</em>, <em>associated_gateway_id=None</em>, <em>dx_gateway_id=None</em>, <em>dx_gateway_owner_account_id=None</em>, <em>vpn_gateway_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Direct Connect Gateway Association Proposal, typically for enabling cross-account associations. For single account associations, see the <cite>``aws_dx_gateway_association`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/dx_gateway_association.html">https://www.terraform.io/docs/providers/aws/r/dx_gateway_association.html</a>&gt;`_.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allowed_prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.</li>
<li><strong>associated_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.</li>
<li><strong>dx_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Direct Connect Gateway identifier.</li>
<li><strong>dx_gateway_owner_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS Account identifier of the Direct Connect Gateway’s owner.</li>
<li><strong>vpn_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">associated_gateway_id</span></code> instead. Virtual Gateway identifier to associate with the Direct Connect Gateway.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.allowed_prefixes">
<code class="descname">allowed_prefixes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.allowed_prefixes" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC prefixes (CIDRs) to advertise to the Direct Connect gateway. Defaults to the CIDR block of the VPC associated with the Virtual Gateway. To enable drift detection, must be configured.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.associated_gateway_id">
<code class="descname">associated_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.associated_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VGW or transit gateway with which to associate the Direct Connect gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.associated_gateway_owner_account_id">
<code class="descname">associated_gateway_owner_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.associated_gateway_owner_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the AWS account that owns the VGW or transit gateway with which to associate the Direct Connect gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.associated_gateway_type">
<code class="descname">associated_gateway_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.associated_gateway_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the associated gateway, <code class="docutils literal notranslate"><span class="pre">transitGateway</span></code> or <code class="docutils literal notranslate"><span class="pre">virtualPrivateGateway</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.dx_gateway_id">
<code class="descname">dx_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.dx_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Direct Connect Gateway identifier.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.dx_gateway_owner_account_id">
<code class="descname">dx_gateway_owner_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.dx_gateway_owner_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS Account identifier of the Direct Connect Gateway’s owner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.vpn_gateway_id">
<code class="descname">vpn_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.vpn_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p><em>Deprecated:</em> Use <code class="docutils literal notranslate"><span class="pre">associated_gateway_id</span></code> instead. Virtual Gateway identifier to associate with the Direct Connect Gateway.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.GatewayAssociationProposal.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.GatewayAssociationProposal.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.GetGatewayResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.directconnect.</code><code class="descname">GetGatewayResult</code><span class="sig-paren">(</span><em>amazon_side_asn=None</em>, <em>name=None</em>, <em>owner_account_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.GetGatewayResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGateway.</p>
<dl class="attribute">
<dt id="pulumi_aws.directconnect.GetGatewayResult.amazon_side_asn">
<code class="descname">amazon_side_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GetGatewayResult.amazon_side_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ASN on the Amazon side of the connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.GetGatewayResult.owner_account_id">
<code class="descname">owner_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GetGatewayResult.owner_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS Account ID of the gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.GetGatewayResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.GetGatewayResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface">
<em class="property">class </em><code class="descclassname">pulumi_aws.directconnect.</code><code class="descname">HostedPrivateVirtualInterface</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>address_family=None</em>, <em>amazon_address=None</em>, <em>bgp_asn=None</em>, <em>bgp_auth_key=None</em>, <em>connection_id=None</em>, <em>customer_address=None</em>, <em>mtu=None</em>, <em>name=None</em>, <em>owner_account_id=None</em>, <em>vlan=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Direct Connect hosted private virtual interface resource. This resource represents the allocator’s side of the hosted virtual interface.
A hosted virtual interface is a virtual interface that is owned by another AWS account.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</li>
<li><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</li>
<li><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</li>
<li><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</li>
<li><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</li>
<li><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</li>
<li><strong>mtu</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a virtual private interface can be either <code class="docutils literal notranslate"><span class="pre">1500</span></code> or <code class="docutils literal notranslate"><span class="pre">9001</span></code> (jumbo frames). Default is <code class="docutils literal notranslate"><span class="pre">1500</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the virtual interface.</li>
<li><strong>owner_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS account that will own the new virtual interface.</li>
<li><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The VLAN ID.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.address_family">
<code class="descname">address_family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p>The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.amazon_address">
<code class="descname">amazon_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.amazon_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.aws_device">
<code class="descname">aws_device</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.aws_device" title="Permalink to this definition">¶</a></dt>
<dd><p>The Direct Connect endpoint on which the virtual interface terminates.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.bgp_asn">
<code class="descname">bgp_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.bgp_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.bgp_auth_key">
<code class="descname">bgp_auth_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.bgp_auth_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication key for BGP configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.connection_id">
<code class="descname">connection_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.customer_address">
<code class="descname">customer_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.customer_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.jumbo_frame_capable">
<code class="descname">jumbo_frame_capable</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.jumbo_frame_capable" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether jumbo frames (9001 MTU) are supported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.mtu">
<code class="descname">mtu</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.mtu" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection. The MTU of a virtual private interface can be either <code class="docutils literal notranslate"><span class="pre">1500</span></code> or <code class="docutils literal notranslate"><span class="pre">9001</span></code> (jumbo frames). Default is <code class="docutils literal notranslate"><span class="pre">1500</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the virtual interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.owner_account_id">
<code class="descname">owner_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.owner_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account that will own the new virtual interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.vlan">
<code class="descname">vlan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.vlan" title="Permalink to this definition">¶</a></dt>
<dd><p>The VLAN ID.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterface.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterface.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter">
<em class="property">class </em><code class="descclassname">pulumi_aws.directconnect.</code><code class="descname">HostedPrivateVirtualInterfaceAccepter</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>dx_gateway_id=None</em>, <em>tags=None</em>, <em>virtual_interface_id=None</em>, <em>vpn_gateway_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage the accepter’s side of a Direct Connect hosted private virtual interface.
This resource accepts ownership of a private virtual interface created by another AWS account.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>dx_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect gateway to which to connect the virtual interface.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>virtual_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect virtual interface to accept.</li>
<li><strong>vpn_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the virtual private gateway to which to connect the virtual interface.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.dx_gateway_id">
<code class="descname">dx_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.dx_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect gateway to which to connect the virtual interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.virtual_interface_id">
<code class="descname">virtual_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.virtual_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect virtual interface to accept.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.vpn_gateway_id">
<code class="descname">vpn_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.vpn_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the virtual private gateway to which to connect the virtual interface.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPrivateVirtualInterfaceAccepter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface">
<em class="property">class </em><code class="descclassname">pulumi_aws.directconnect.</code><code class="descname">HostedPublicVirtualInterface</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>address_family=None</em>, <em>amazon_address=None</em>, <em>bgp_asn=None</em>, <em>bgp_auth_key=None</em>, <em>connection_id=None</em>, <em>customer_address=None</em>, <em>name=None</em>, <em>owner_account_id=None</em>, <em>route_filter_prefixes=None</em>, <em>vlan=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Direct Connect hosted public virtual interface resource. This resource represents the allocator’s side of the hosted virtual interface.
A hosted virtual interface is a virtual interface that is owned by another AWS account.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</li>
<li><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</li>
<li><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</li>
<li><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</li>
<li><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</li>
<li><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the virtual interface.</li>
<li><strong>owner_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS account that will own the new virtual interface.</li>
<li><strong>route_filter_prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of routes to be advertised to the AWS network in this region.</li>
<li><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The VLAN ID.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.address_family">
<code class="descname">address_family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p>The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.amazon_address">
<code class="descname">amazon_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.amazon_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.aws_device">
<code class="descname">aws_device</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.aws_device" title="Permalink to this definition">¶</a></dt>
<dd><p>The Direct Connect endpoint on which the virtual interface terminates.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.bgp_asn">
<code class="descname">bgp_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.bgp_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.bgp_auth_key">
<code class="descname">bgp_auth_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.bgp_auth_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication key for BGP configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.connection_id">
<code class="descname">connection_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.customer_address">
<code class="descname">customer_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.customer_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the virtual interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.owner_account_id">
<code class="descname">owner_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.owner_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS account that will own the new virtual interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.route_filter_prefixes">
<code class="descname">route_filter_prefixes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.route_filter_prefixes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of routes to be advertised to the AWS network in this region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.vlan">
<code class="descname">vlan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.vlan" title="Permalink to this definition">¶</a></dt>
<dd><p>The VLAN ID.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterface.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterface.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter">
<em class="property">class </em><code class="descclassname">pulumi_aws.directconnect.</code><code class="descname">HostedPublicVirtualInterfaceAccepter</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>tags=None</em>, <em>virtual_interface_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage the accepter’s side of a Direct Connect hosted public virtual interface.
This resource accepts ownership of a public virtual interface created by another AWS account.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>virtual_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect virtual interface to accept.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.virtual_interface_id">
<code class="descname">virtual_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.virtual_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect virtual interface to accept.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.HostedPublicVirtualInterfaceAccepter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.LinkAggregationGroup">
<em class="property">class </em><code class="descclassname">pulumi_aws.directconnect.</code><code class="descname">LinkAggregationGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>connections_bandwidth=None</em>, <em>force_destroy=None</em>, <em>location=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Direct Connect LAG. Connections can be added to the LAG via the <cite>``aws_dx_connection`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/dx_connection.html">https://www.terraform.io/docs/providers/aws/r/dx_connection.html</a>&gt;`_ and <cite>``aws_dx_connection_association`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/dx_connection_association.html">https://www.terraform.io/docs/providers/aws/r/dx_connection_association.html</a>&gt;`_ resources.</p>
<blockquote>
<div><em>NOTE:</em> When creating a LAG, Direct Connect requires creating a Connection. Terraform will remove this unmanaged connection during resource creation.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>connections_bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The bandwidth of the individual physical connections bundled by the LAG. Available values: 1Gbps, 10Gbps. Case sensitive.</li>
<li><strong>force_destroy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean that indicates all connections associated with the LAG should be deleted so that the LAG can be destroyed without error. These objects are <em>not</em> recoverable.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The AWS Direct Connect location in which the LAG should be allocated. See <a class="reference external" href="https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html">DescribeLocations</a> for the list of AWS Direct Connect locations. Use <code class="docutils literal notranslate"><span class="pre">locationCode</span></code>.</p>
</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the LAG.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the LAG.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">jumbo_frame_capable</span></code> -Indicates whether jumbo frames (9001 MTU) are supported.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.connections_bandwidth">
<code class="descname">connections_bandwidth</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.connections_bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>The bandwidth of the individual physical connections bundled by the LAG. Available values: 1Gbps, 10Gbps. Case sensitive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.force_destroy">
<code class="descname">force_destroy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.force_destroy" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean that indicates all connections associated with the LAG should be deleted so that the LAG can be destroyed without error. These objects are <em>not</em> recoverable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.has_logical_redundancy">
<code class="descname">has_logical_redundancy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.has_logical_redundancy" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the LAG supports a secondary BGP peer in the same address family (IPv4/IPv6).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Direct Connect location in which the LAG should be allocated. See <a class="reference external" href="https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html">DescribeLocations</a> for the list of AWS Direct Connect locations. Use <code class="docutils literal notranslate"><span class="pre">locationCode</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the LAG.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.LinkAggregationGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.LinkAggregationGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface">
<em class="property">class </em><code class="descclassname">pulumi_aws.directconnect.</code><code class="descname">PrivateVirtualInterface</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>address_family=None</em>, <em>amazon_address=None</em>, <em>bgp_asn=None</em>, <em>bgp_auth_key=None</em>, <em>connection_id=None</em>, <em>customer_address=None</em>, <em>dx_gateway_id=None</em>, <em>mtu=None</em>, <em>name=None</em>, <em>tags=None</em>, <em>vlan=None</em>, <em>vpn_gateway_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Direct Connect private virtual interface resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</li>
<li><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</li>
<li><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</li>
<li><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</li>
<li><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</li>
<li><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</li>
<li><strong>dx_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect gateway to which to connect the virtual interface.</li>
<li><strong>mtu</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection.
The MTU of a virtual private interface can be either <code class="docutils literal notranslate"><span class="pre">1500</span></code> or <code class="docutils literal notranslate"><span class="pre">9001</span></code> (jumbo frames). Default is <code class="docutils literal notranslate"><span class="pre">1500</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the virtual interface.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The VLAN ID.</li>
<li><strong>vpn_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the virtual private gateway to which to connect the virtual interface.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.address_family">
<code class="descname">address_family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p>The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.amazon_address">
<code class="descname">amazon_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.amazon_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.aws_device">
<code class="descname">aws_device</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.aws_device" title="Permalink to this definition">¶</a></dt>
<dd><p>The Direct Connect endpoint on which the virtual interface terminates.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.bgp_asn">
<code class="descname">bgp_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.bgp_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.bgp_auth_key">
<code class="descname">bgp_auth_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.bgp_auth_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication key for BGP configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.connection_id">
<code class="descname">connection_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.customer_address">
<code class="descname">customer_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.customer_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.dx_gateway_id">
<code class="descname">dx_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.dx_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect gateway to which to connect the virtual interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.jumbo_frame_capable">
<code class="descname">jumbo_frame_capable</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.jumbo_frame_capable" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether jumbo frames (9001 MTU) are supported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.mtu">
<code class="descname">mtu</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.mtu" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum transmission unit (MTU) is the size, in bytes, of the largest permissible packet that can be passed over the connection.
The MTU of a virtual private interface can be either <code class="docutils literal notranslate"><span class="pre">1500</span></code> or <code class="docutils literal notranslate"><span class="pre">9001</span></code> (jumbo frames). Default is <code class="docutils literal notranslate"><span class="pre">1500</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the virtual interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.vlan">
<code class="descname">vlan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.vlan" title="Permalink to this definition">¶</a></dt>
<dd><p>The VLAN ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.vpn_gateway_id">
<code class="descname">vpn_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.vpn_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the virtual private gateway to which to connect the virtual interface.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.PrivateVirtualInterface.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.PrivateVirtualInterface.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.PublicVirtualInterface">
<em class="property">class </em><code class="descclassname">pulumi_aws.directconnect.</code><code class="descname">PublicVirtualInterface</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>address_family=None</em>, <em>amazon_address=None</em>, <em>bgp_asn=None</em>, <em>bgp_auth_key=None</em>, <em>connection_id=None</em>, <em>customer_address=None</em>, <em>name=None</em>, <em>route_filter_prefixes=None</em>, <em>tags=None</em>, <em>vlan=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Direct Connect public virtual interface resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>address_family</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</li>
<li><strong>amazon_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</li>
<li><strong>bgp_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</li>
<li><strong>bgp_auth_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication key for BGP configuration.</li>
<li><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</li>
<li><strong>customer_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the virtual interface.</li>
<li><strong>route_filter_prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of routes to be advertised to the AWS network in this region.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>vlan</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The VLAN ID.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.address_family">
<code class="descname">address_family</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.address_family" title="Permalink to this definition">¶</a></dt>
<dd><p>The address family for the BGP peer. <code class="docutils literal notranslate"><span class="pre">ipv4</span></code> or <code class="docutils literal notranslate"><span class="pre">ipv6</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.amazon_address">
<code class="descname">amazon_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.amazon_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR address to use to send traffic to Amazon. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the virtual interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.aws_device">
<code class="descname">aws_device</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.aws_device" title="Permalink to this definition">¶</a></dt>
<dd><p>The Direct Connect endpoint on which the virtual interface terminates.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.bgp_asn">
<code class="descname">bgp_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.bgp_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.bgp_auth_key">
<code class="descname">bgp_auth_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.bgp_auth_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication key for BGP configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.connection_id">
<code class="descname">connection_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Direct Connect connection (or LAG) on which to create the virtual interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.customer_address">
<code class="descname">customer_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.customer_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 CIDR destination address to which Amazon should send traffic. Required for IPv4 BGP peers.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the virtual interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.route_filter_prefixes">
<code class="descname">route_filter_prefixes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.route_filter_prefixes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of routes to be advertised to the AWS network in this region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.vlan">
<code class="descname">vlan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.vlan" title="Permalink to this definition">¶</a></dt>
<dd><p>The VLAN ID.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.PublicVirtualInterface.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.PublicVirtualInterface.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.directconnect.get_gateway">
<code class="descclassname">pulumi_aws.directconnect.</code><code class="descname">get_gateway</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.directconnect.get_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve information about a Direct Connect Gateway.</p>
</dd></dl>

</div>
