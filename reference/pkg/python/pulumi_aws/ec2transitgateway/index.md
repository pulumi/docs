<div class="section" id="module-pulumi_aws.ec2transitgateway">
<span id="ec2transitgateway"></span><h1>ec2transitgateway<a class="headerlink" href="#module-pulumi_aws.ec2transitgateway" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.ec2transitgateway.GetRouteTableResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2transitgateway.</code><code class="descname">GetRouteTableResult</code><span class="sig-paren">(</span><em>default_association_route_table=None</em>, <em>default_propagation_route_table=None</em>, <em>tags=None</em>, <em>transit_gateway_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetRouteTableResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRouteTable.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetRouteTableResult.default_association_route_table">
<code class="descname">default_association_route_table</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetRouteTableResult.default_association_route_table" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether this is the default association route table for the EC2 Transit Gateway</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetRouteTableResult.default_propagation_route_table">
<code class="descname">default_propagation_route_table</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetRouteTableResult.default_propagation_route_table" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether this is the default propagation route table for the EC2 Transit Gateway</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetRouteTableResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetRouteTableResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value tags for the EC2 Transit Gateway Route Table</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetRouteTableResult.transit_gateway_id">
<code class="descname">transit_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetRouteTableResult.transit_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>EC2 Transit Gateway identifier</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2transitgateway.</code><code class="descname">GetTransitGatewayResult</code><span class="sig-paren">(</span><em>amazon_side_asn=None</em>, <em>arn=None</em>, <em>association_default_route_table_id=None</em>, <em>auto_accept_shared_attachments=None</em>, <em>default_route_table_association=None</em>, <em>default_route_table_propagation=None</em>, <em>description=None</em>, <em>dns_support=None</em>, <em>owner_id=None</em>, <em>propagation_default_route_table_id=None</em>, <em>tags=None</em>, <em>vpn_ecmp_support=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTransitGateway.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.amazon_side_asn">
<code class="descname">amazon_side_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.amazon_side_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>Private Autonomous System Number (ASN) for the Amazon side of a BGP session</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>EC2 Transit Gateway Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.association_default_route_table_id">
<code class="descname">association_default_route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.association_default_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the default association route table</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.auto_accept_shared_attachments">
<code class="descname">auto_accept_shared_attachments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.auto_accept_shared_attachments" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether resource attachment requests are automatically accepted.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.default_route_table_association">
<code class="descname">default_route_table_association</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.default_route_table_association" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether resource attachments are automatically associated with the default association route table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.default_route_table_propagation">
<code class="descname">default_route_table_propagation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.default_route_table_propagation" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether resource attachments automatically propagate routes to the default propagation route table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the EC2 Transit Gateway</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.dns_support">
<code class="descname">dns_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.dns_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether DNS support is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the AWS account that owns the EC2 Transit Gateway</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.propagation_default_route_table_id">
<code class="descname">propagation_default_route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.propagation_default_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the default propagation route table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value tags for the EC2 Transit Gateway</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.vpn_ecmp_support">
<code class="descname">vpn_ecmp_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.vpn_ecmp_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether VPN Equal Cost Multipath Protocol support is enabled.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2transitgateway.GetVpcAttachmentResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2transitgateway.</code><code class="descname">GetVpcAttachmentResult</code><span class="sig-paren">(</span><em>dns_support=None</em>, <em>ipv6_support=None</em>, <em>subnet_ids=None</em>, <em>tags=None</em>, <em>transit_gateway_id=None</em>, <em>vpc_id=None</em>, <em>vpc_owner_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpcAttachmentResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVpcAttachment.</p>
<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.dns_support">
<code class="descname">dns_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.dns_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether DNS support is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.ipv6_support">
<code class="descname">ipv6_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.ipv6_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether IPv6 support is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.subnet_ids">
<code class="descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifiers of EC2 Subnets.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value tags for the EC2 Transit Gateway VPC Attachment</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.transit_gateway_id">
<code class="descname">transit_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.transit_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>EC2 Transit Gateway identifier</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.vpc_owner_id">
<code class="descname">vpc_owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.vpc_owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the AWS account that owns the EC2 VPC.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.ec2transitgateway.Route">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2transitgateway.</code><code class="descname">Route</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>destination_cidr_block=None</em>, <em>transit_gateway_attachment_id=None</em>, <em>transit_gateway_route_table_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.Route" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EC2 Transit Gateway Route.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>destination_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.</li>
<li><strong>transit_gateway_attachment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway Attachment.</li>
<li><strong>transit_gateway_route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway Route Table.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.Route.destination_cidr_block">
<code class="descname">destination_cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.Route.destination_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.Route.transit_gateway_attachment_id">
<code class="descname">transit_gateway_attachment_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.Route.transit_gateway_attachment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway Attachment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.Route.transit_gateway_route_table_id">
<code class="descname">transit_gateway_route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.Route.transit_gateway_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway Route Table.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2transitgateway.Route.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.Route.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.Route.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.Route.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.RouteTable">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2transitgateway.</code><code class="descname">RouteTable</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>tags=None</em>, <em>transit_gateway_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTable" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EC2 Transit Gateway Route Table.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value tags for the EC2 Transit Gateway Route Table.</li>
<li><strong>transit_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTable.default_association_route_table">
<code class="descname">default_association_route_table</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTable.default_association_route_table" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether this is the default association route table for the EC2 Transit Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTable.default_propagation_route_table">
<code class="descname">default_propagation_route_table</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTable.default_propagation_route_table" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether this is the default propagation route table for the EC2 Transit Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTable.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTable.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value tags for the EC2 Transit Gateway Route Table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTable.transit_gateway_id">
<code class="descname">transit_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTable.transit_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2transitgateway.RouteTable.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.RouteTable.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.RouteTableAssociation">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2transitgateway.</code><code class="descname">RouteTableAssociation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>transit_gateway_attachment_id=None</em>, <em>transit_gateway_route_table_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTableAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EC2 Transit Gateway Route Table association.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>transit_gateway_attachment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway Attachment.</li>
<li><strong>transit_gateway_route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway Route Table.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTableAssociation.resource_id">
<code class="descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTableAssociation.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTableAssociation.resource_type">
<code class="descname">resource_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTableAssociation.resource_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTableAssociation.transit_gateway_attachment_id">
<code class="descname">transit_gateway_attachment_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTableAssociation.transit_gateway_attachment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway Attachment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTableAssociation.transit_gateway_route_table_id">
<code class="descname">transit_gateway_route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTableAssociation.transit_gateway_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway Route Table.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2transitgateway.RouteTableAssociation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTableAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.RouteTableAssociation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTableAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.RouteTablePropagation">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2transitgateway.</code><code class="descname">RouteTablePropagation</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>transit_gateway_attachment_id=None</em>, <em>transit_gateway_route_table_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTablePropagation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EC2 Transit Gateway Route Table propagation.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>transit_gateway_attachment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway Attachment.</li>
<li><strong>transit_gateway_route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway Route Table.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTablePropagation.resource_id">
<code class="descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTablePropagation.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTablePropagation.resource_type">
<code class="descname">resource_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTablePropagation.resource_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the resource</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTablePropagation.transit_gateway_attachment_id">
<code class="descname">transit_gateway_attachment_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTablePropagation.transit_gateway_attachment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway Attachment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTablePropagation.transit_gateway_route_table_id">
<code class="descname">transit_gateway_route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTablePropagation.transit_gateway_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway Route Table.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2transitgateway.RouteTablePropagation.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTablePropagation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.RouteTablePropagation.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTablePropagation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.TransitGateway">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2transitgateway.</code><code class="descname">TransitGateway</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>amazon_side_asn=None</em>, <em>auto_accept_shared_attachments=None</em>, <em>default_route_table_association=None</em>, <em>default_route_table_propagation=None</em>, <em>description=None</em>, <em>dns_support=None</em>, <em>tags=None</em>, <em>vpn_ecmp_support=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EC2 Transit Gateway.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>amazon_side_asn</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is <code class="docutils literal notranslate"><span class="pre">64512</span></code> to <code class="docutils literal notranslate"><span class="pre">65534</span></code> for 16-bit ASNs and <code class="docutils literal notranslate"><span class="pre">4200000000</span></code> to <code class="docutils literal notranslate"><span class="pre">4294967294</span></code> for 32-bit ASNs. Default value: <code class="docutils literal notranslate"><span class="pre">64512</span></code>.</li>
<li><strong>auto_accept_shared_attachments</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether resource attachment requests are automatically accepted. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">disable</span></code>.</li>
<li><strong>default_route_table_association</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether resource attachments are automatically associated with the default association route table. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</li>
<li><strong>default_route_table_propagation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether resource attachments automatically propagate routes to the default propagation route table. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the EC2 Transit Gateway.</li>
<li><strong>dns_support</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether DNS support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value tags for the EC2 Transit Gateway.</li>
<li><strong>vpn_ecmp_support</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether VPN Equal Cost Multipath Protocol support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.amazon_side_asn">
<code class="descname">amazon_side_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.amazon_side_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>Private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is <code class="docutils literal notranslate"><span class="pre">64512</span></code> to <code class="docutils literal notranslate"><span class="pre">65534</span></code> for 16-bit ASNs and <code class="docutils literal notranslate"><span class="pre">4200000000</span></code> to <code class="docutils literal notranslate"><span class="pre">4294967294</span></code> for 32-bit ASNs. Default value: <code class="docutils literal notranslate"><span class="pre">64512</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>EC2 Transit Gateway Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.association_default_route_table_id">
<code class="descname">association_default_route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.association_default_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the default association route table</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.auto_accept_shared_attachments">
<code class="descname">auto_accept_shared_attachments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.auto_accept_shared_attachments" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether resource attachment requests are automatically accepted. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">disable</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.default_route_table_association">
<code class="descname">default_route_table_association</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.default_route_table_association" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether resource attachments are automatically associated with the default association route table. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.default_route_table_propagation">
<code class="descname">default_route_table_propagation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.default_route_table_propagation" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether resource attachments automatically propagate routes to the default propagation route table. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the EC2 Transit Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.dns_support">
<code class="descname">dns_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.dns_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether DNS support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.owner_id">
<code class="descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the AWS account that owns the EC2 Transit Gateway</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.propagation_default_route_table_id">
<code class="descname">propagation_default_route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.propagation_default_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the default propagation route table</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value tags for the EC2 Transit Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.vpn_ecmp_support">
<code class="descname">vpn_ecmp_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.vpn_ecmp_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether VPN Equal Cost Multipath Protocol support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment">
<em class="property">class </em><code class="descclassname">pulumi_aws.ec2transitgateway.</code><code class="descname">VpcAttachment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>dns_support=None</em>, <em>ipv6_support=None</em>, <em>subnet_ids=None</em>, <em>tags=None</em>, <em>transit_gateway_default_route_table_association=None</em>, <em>transit_gateway_default_route_table_propagation=None</em>, <em>transit_gateway_id=None</em>, <em>vpc_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EC2 Transit Gateway VPC Attachment. For examples of custom route table association and propagation, see the EC2 Transit Gateway Networking Examples Guide.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>dns_support</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether DNS support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</li>
<li><strong>ipv6_support</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether IPv6 support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">disable</span></code>.</li>
<li><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Identifiers of EC2 Subnets.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value tags for the EC2 Transit Gateway VPC Attachment.</li>
<li><strong>transit_gateway_default_route_table_association</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether the VPC Attachment should be associated with the EC2 Transit Gateway association default route table. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>transit_gateway_default_route_table_propagation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether the VPC Attachment should propagate routes with the EC2 Transit Gateway propagation default route table. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>transit_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway.</li>
<li><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 VPC.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.dns_support">
<code class="descname">dns_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.dns_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether DNS support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.ipv6_support">
<code class="descname">ipv6_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.ipv6_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether IPv6 support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">disable</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.subnet_ids">
<code class="descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifiers of EC2 Subnets.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value tags for the EC2 Transit Gateway VPC Attachment.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.transit_gateway_default_route_table_association">
<code class="descname">transit_gateway_default_route_table_association</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.transit_gateway_default_route_table_association" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether the VPC Attachment should be associated with the EC2 Transit Gateway association default route table. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.transit_gateway_default_route_table_propagation">
<code class="descname">transit_gateway_default_route_table_propagation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.transit_gateway_default_route_table_propagation" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether the VPC Attachment should propagate routes with the EC2 Transit Gateway propagation default route table. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.transit_gateway_id">
<code class="descname">transit_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.transit_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.vpc_id">
<code class="descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 VPC.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.vpc_owner_id">
<code class="descname">vpc_owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.vpc_owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the AWS account that owns the EC2 VPC.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.get_route_table">
<code class="descclassname">pulumi_aws.ec2transitgateway.</code><code class="descname">get_route_table</code><span class="sig-paren">(</span><em>filters=None</em>, <em>id=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.get_route_table" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on an EC2 Transit Gateway Route Table.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2transitgateway.get_transit_gateway">
<code class="descclassname">pulumi_aws.ec2transitgateway.</code><code class="descname">get_transit_gateway</code><span class="sig-paren">(</span><em>filters=None</em>, <em>id=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.get_transit_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on an EC2 Transit Gateway.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.ec2transitgateway.get_vpc_attachment">
<code class="descclassname">pulumi_aws.ec2transitgateway.</code><code class="descname">get_vpc_attachment</code><span class="sig-paren">(</span><em>filters=None</em>, <em>id=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.get_vpc_attachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on an EC2 Transit Gateway VPC Attachment.</p>
</dd></dl>

</div>
