---
title: Module ec2transitgateway
title_tag: Module ec2transitgateway | Package pulumi_aws | Python SDK
linktitle: ec2transitgateway
notitle: true
---

<div class="section" id="ec2transitgateway">
<h1>ec2transitgateway<a class="headerlink" href="#ec2transitgateway" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.ec2transitgateway"></span><dl class="py class">
<dt id="pulumi_aws.ec2transitgateway.AwaitableGetDirectConnectGatewayAttachmentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">AwaitableGetDirectConnectGatewayAttachmentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">dx_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.AwaitableGetDirectConnectGatewayAttachmentResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ec2transitgateway.AwaitableGetPeeringAttachmentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">AwaitableGetPeeringAttachmentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.AwaitableGetPeeringAttachmentResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ec2transitgateway.AwaitableGetRouteTableResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">AwaitableGetRouteTableResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">default_association_route_table</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_propagation_route_table</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.AwaitableGetRouteTableResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ec2transitgateway.AwaitableGetTransitGatewayResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">AwaitableGetTransitGatewayResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">amazon_side_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">association_default_route_table_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_accept_shared_attachments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_route_table_association</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_route_table_propagation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_support</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">propagation_default_route_table_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_ecmp_support</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.AwaitableGetTransitGatewayResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ec2transitgateway.AwaitableGetVpcAttachmentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">AwaitableGetVpcAttachmentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">dns_support</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_support</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_owner_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.AwaitableGetVpcAttachmentResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ec2transitgateway.AwaitableGetVpnAttachmentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">AwaitableGetVpnAttachmentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_connection_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.AwaitableGetVpnAttachmentResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ec2transitgateway.GetDirectConnectGatewayAttachmentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">GetDirectConnectGatewayAttachmentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">dx_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetDirectConnectGatewayAttachmentResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDirectConnectGatewayAttachment.</p>
<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetDirectConnectGatewayAttachmentResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetDirectConnectGatewayAttachmentResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetDirectConnectGatewayAttachmentResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetDirectConnectGatewayAttachmentResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value tags for the EC2 Transit Gateway Attachment</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ec2transitgateway.GetPeeringAttachmentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">GetPeeringAttachmentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetPeeringAttachmentResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPeeringAttachment.</p>
<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetPeeringAttachmentResult.peer_account_id">
<code class="sig-name descname">peer_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetPeeringAttachmentResult.peer_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the peer AWS account</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetPeeringAttachmentResult.peer_region">
<code class="sig-name descname">peer_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetPeeringAttachmentResult.peer_region" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the peer AWS region</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetPeeringAttachmentResult.peer_transit_gateway_id">
<code class="sig-name descname">peer_transit_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetPeeringAttachmentResult.peer_transit_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the peer EC2 Transit Gateway</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetPeeringAttachmentResult.transit_gateway_id">
<code class="sig-name descname">transit_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetPeeringAttachmentResult.transit_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the local EC2 Transit Gateway</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ec2transitgateway.GetRouteTableResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">GetRouteTableResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">default_association_route_table</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_propagation_route_table</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetRouteTableResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRouteTable.</p>
<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetRouteTableResult.default_association_route_table">
<code class="sig-name descname">default_association_route_table</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetRouteTableResult.default_association_route_table" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether this is the default association route table for the EC2 Transit Gateway</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetRouteTableResult.default_propagation_route_table">
<code class="sig-name descname">default_propagation_route_table</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetRouteTableResult.default_propagation_route_table" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether this is the default propagation route table for the EC2 Transit Gateway</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetRouteTableResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetRouteTableResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>EC2 Transit Gateway Route Table identifier</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetRouteTableResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetRouteTableResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value tags for the EC2 Transit Gateway Route Table</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetRouteTableResult.transit_gateway_id">
<code class="sig-name descname">transit_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetRouteTableResult.transit_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>EC2 Transit Gateway identifier</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">GetTransitGatewayResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">amazon_side_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">association_default_route_table_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_accept_shared_attachments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_route_table_association</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_route_table_propagation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_support</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">propagation_default_route_table_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_ecmp_support</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTransitGateway.</p>
<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.amazon_side_asn">
<code class="sig-name descname">amazon_side_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.amazon_side_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>Private Autonomous System Number (ASN) for the Amazon side of a BGP session</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>EC2 Transit Gateway Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.association_default_route_table_id">
<code class="sig-name descname">association_default_route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.association_default_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the default association route table</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.auto_accept_shared_attachments">
<code class="sig-name descname">auto_accept_shared_attachments</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.auto_accept_shared_attachments" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether resource attachment requests are automatically accepted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.default_route_table_association">
<code class="sig-name descname">default_route_table_association</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.default_route_table_association" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether resource attachments are automatically associated with the default association route table.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.default_route_table_propagation">
<code class="sig-name descname">default_route_table_propagation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.default_route_table_propagation" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether resource attachments automatically propagate routes to the default propagation route table.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the EC2 Transit Gateway</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.dns_support">
<code class="sig-name descname">dns_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.dns_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether DNS support is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>EC2 Transit Gateway identifier</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.owner_id">
<code class="sig-name descname">owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the AWS account that owns the EC2 Transit Gateway</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.propagation_default_route_table_id">
<code class="sig-name descname">propagation_default_route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.propagation_default_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the default propagation route table.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value tags for the EC2 Transit Gateway</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetTransitGatewayResult.vpn_ecmp_support">
<code class="sig-name descname">vpn_ecmp_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetTransitGatewayResult.vpn_ecmp_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether VPN Equal Cost Multipath Protocol support is enabled.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ec2transitgateway.GetVpcAttachmentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">GetVpcAttachmentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">dns_support</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_support</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_owner_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpcAttachmentResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVpcAttachment.</p>
<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.dns_support">
<code class="sig-name descname">dns_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.dns_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether DNS support is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>EC2 Transit Gateway VPC Attachment identifier</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.ipv6_support">
<code class="sig-name descname">ipv6_support</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.ipv6_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether IPv6 support is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifiers of EC2 Subnets.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value tags for the EC2 Transit Gateway VPC Attachment</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.transit_gateway_id">
<code class="sig-name descname">transit_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.transit_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>EC2 Transit Gateway identifier</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 VPC.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.vpc_owner_id">
<code class="sig-name descname">vpc_owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpcAttachmentResult.vpc_owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the AWS account that owns the EC2 VPC.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ec2transitgateway.GetVpnAttachmentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">GetVpnAttachmentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_connection_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpnAttachmentResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVpnAttachment.</p>
<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetVpnAttachmentResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpnAttachmentResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.GetVpnAttachmentResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.GetVpnAttachmentResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value tags for the EC2 Transit Gateway VPN Attachment</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.ec2transitgateway.PeeringAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">PeeringAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.PeeringAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EC2 Transit Gateway Peering Attachment.
For examples of custom route table association and propagation, see the <a class="reference external" href="https://docs.aws.amazon.com/vpc/latest/tgw/TGW_Scenarios.html">EC2 Transit Gateway Networking Examples Guide</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>
<span class="kn">import</span> <span class="nn">pulumi_pulumi</span> <span class="k">as</span> <span class="nn">pulumi</span>

<span class="n">local</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">providers</span><span class="o">.</span><span class="n">Aws</span><span class="p">(</span><span class="s2">&quot;local&quot;</span><span class="p">,</span> <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-east-1&quot;</span><span class="p">)</span>
<span class="n">peer</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">providers</span><span class="o">.</span><span class="n">Aws</span><span class="p">(</span><span class="s2">&quot;peer&quot;</span><span class="p">,</span> <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-west-2&quot;</span><span class="p">)</span>
<span class="n">peer_region</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_region</span><span class="p">()</span>
<span class="n">local_transit_gateway</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">TransitGateway</span><span class="p">(</span><span class="s2">&quot;localTransitGateway&quot;</span><span class="p">,</span> <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
    <span class="s2">&quot;Name&quot;</span><span class="p">:</span> <span class="s2">&quot;Local TGW&quot;</span><span class="p">,</span>
<span class="p">})</span>
<span class="n">peer_transit_gateway</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">TransitGateway</span><span class="p">(</span><span class="s2">&quot;peerTransitGateway&quot;</span><span class="p">,</span> <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
    <span class="s2">&quot;Name&quot;</span><span class="p">:</span> <span class="s2">&quot;Peer TGW&quot;</span><span class="p">,</span>
<span class="p">})</span>
<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">PeeringAttachment</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">peer_account_id</span><span class="o">=</span><span class="n">peer_transit_gateway</span><span class="o">.</span><span class="n">owner_id</span><span class="p">,</span>
    <span class="n">peer_region</span><span class="o">=</span><span class="n">peer_region</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">peer_transit_gateway_id</span><span class="o">=</span><span class="n">peer_transit_gateway</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">transit_gateway_id</span><span class="o">=</span><span class="n">local_transit_gateway</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;Name&quot;</span><span class="p">:</span> <span class="s2">&quot;TGW Peering Requestor&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>peer_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account ID of EC2 Transit Gateway to peer with. Defaults to the account ID the current provider is currently connected to.</p></li>
<li><p><strong>peer_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Region of EC2 Transit Gateway to peer with.</p></li>
<li><p><strong>peer_transit_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway to peer with.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value tags for the EC2 Transit Gateway Peering Attachment.</p></li>
<li><p><strong>transit_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.PeeringAttachment.peer_account_id">
<code class="sig-name descname">peer_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.PeeringAttachment.peer_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account ID of EC2 Transit Gateway to peer with. Defaults to the account ID the current provider is currently connected to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.PeeringAttachment.peer_region">
<code class="sig-name descname">peer_region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.PeeringAttachment.peer_region" title="Permalink to this definition">¶</a></dt>
<dd><p>Region of EC2 Transit Gateway to peer with.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.PeeringAttachment.peer_transit_gateway_id">
<code class="sig-name descname">peer_transit_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.PeeringAttachment.peer_transit_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway to peer with.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.PeeringAttachment.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.PeeringAttachment.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value tags for the EC2 Transit Gateway Peering Attachment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.PeeringAttachment.transit_gateway_id">
<code class="sig-name descname">transit_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.PeeringAttachment.transit_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2transitgateway.PeeringAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.PeeringAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PeeringAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>peer_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account ID of EC2 Transit Gateway to peer with. Defaults to the account ID the current provider is currently connected to.</p></li>
<li><p><strong>peer_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Region of EC2 Transit Gateway to peer with.</p></li>
<li><p><strong>peer_transit_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway to peer with.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value tags for the EC2 Transit Gateway Peering Attachment.</p></li>
<li><p><strong>transit_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2transitgateway.PeeringAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.PeeringAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.PeeringAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.PeeringAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.Route">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">Route</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blackhole</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_attachment_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_route_table_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.Route" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EC2 Transit Gateway Route.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">Route</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">destination_cidr_block</span><span class="o">=</span><span class="s2">&quot;0.0.0.0/0&quot;</span><span class="p">,</span>
    <span class="n">transit_gateway_attachment_id</span><span class="o">=</span><span class="n">aws_ec2_transit_gateway_vpc_attachment</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">transit_gateway_route_table_id</span><span class="o">=</span><span class="n">aws_ec2_transit_gateway</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;association_default_route_table_id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">Route</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">blackhole</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">destination_cidr_block</span><span class="o">=</span><span class="s2">&quot;0.0.0.0/0&quot;</span><span class="p">,</span>
    <span class="n">transit_gateway_route_table_id</span><span class="o">=</span><span class="n">aws_ec2_transit_gateway</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;association_default_route_table_id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blackhole</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether to drop traffic that matches this route (default to <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><strong>destination_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.</p></li>
<li><p><strong>transit_gateway_attachment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway Attachment (required if <code class="docutils literal notranslate"><span class="pre">blackhole</span></code> is set to false).</p></li>
<li><p><strong>transit_gateway_route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway Route Table.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.Route.blackhole">
<code class="sig-name descname">blackhole</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.Route.blackhole" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether to drop traffic that matches this route (default to <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.Route.destination_cidr_block">
<code class="sig-name descname">destination_cidr_block</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.Route.destination_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.Route.transit_gateway_attachment_id">
<code class="sig-name descname">transit_gateway_attachment_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.Route.transit_gateway_attachment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway Attachment (required if <code class="docutils literal notranslate"><span class="pre">blackhole</span></code> is set to false).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.Route.transit_gateway_route_table_id">
<code class="sig-name descname">transit_gateway_route_table_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.Route.transit_gateway_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway Route Table.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2transitgateway.Route.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blackhole</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">destination_cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_attachment_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_route_table_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.Route.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Route resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blackhole</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether to drop traffic that matches this route (default to <code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><strong>destination_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.</p></li>
<li><p><strong>transit_gateway_attachment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway Attachment (required if <code class="docutils literal notranslate"><span class="pre">blackhole</span></code> is set to false).</p></li>
<li><p><strong>transit_gateway_route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway Route Table.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2transitgateway.Route.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.Route.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.Route.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.Route.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.RouteTable">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">RouteTable</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTable" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EC2 Transit Gateway Route Table.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">RouteTable</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">transit_gateway_id</span><span class="o">=</span><span class="n">aws_ec2_transit_gateway</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value tags for the EC2 Transit Gateway Route Table.</p></li>
<li><p><strong>transit_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTable.default_association_route_table">
<code class="sig-name descname">default_association_route_table</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTable.default_association_route_table" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether this is the default association route table for the EC2 Transit Gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTable.default_propagation_route_table">
<code class="sig-name descname">default_propagation_route_table</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTable.default_propagation_route_table" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether this is the default propagation route table for the EC2 Transit Gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTable.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTable.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value tags for the EC2 Transit Gateway Route Table.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTable.transit_gateway_id">
<code class="sig-name descname">transit_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTable.transit_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2transitgateway.RouteTable.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_association_route_table</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_propagation_route_table</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTable.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RouteTable resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_association_route_table</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether this is the default association route table for the EC2 Transit Gateway.</p></li>
<li><p><strong>default_propagation_route_table</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether this is the default propagation route table for the EC2 Transit Gateway.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value tags for the EC2 Transit Gateway Route Table.</p></li>
<li><p><strong>transit_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2transitgateway.RouteTable.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.RouteTable.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.RouteTableAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">RouteTableAssociation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_attachment_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_route_table_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTableAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EC2 Transit Gateway Route Table association.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">RouteTableAssociation</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">transit_gateway_attachment_id</span><span class="o">=</span><span class="n">aws_ec2_transit_gateway_vpc_attachment</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">transit_gateway_route_table_id</span><span class="o">=</span><span class="n">aws_ec2_transit_gateway_route_table</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>transit_gateway_attachment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway Attachment.</p></li>
<li><p><strong>transit_gateway_route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway Route Table.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTableAssociation.resource_id">
<code class="sig-name descname">resource_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTableAssociation.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the resource</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTableAssociation.resource_type">
<code class="sig-name descname">resource_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTableAssociation.resource_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the resource</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTableAssociation.transit_gateway_attachment_id">
<code class="sig-name descname">transit_gateway_attachment_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTableAssociation.transit_gateway_attachment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway Attachment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTableAssociation.transit_gateway_route_table_id">
<code class="sig-name descname">transit_gateway_route_table_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTableAssociation.transit_gateway_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway Route Table.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2transitgateway.RouteTableAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_attachment_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_route_table_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTableAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RouteTableAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the resource</p></li>
<li><p><strong>resource_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the resource</p></li>
<li><p><strong>transit_gateway_attachment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway Attachment.</p></li>
<li><p><strong>transit_gateway_route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway Route Table.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2transitgateway.RouteTableAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTableAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.RouteTableAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTableAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.RouteTablePropagation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">RouteTablePropagation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_attachment_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_route_table_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTablePropagation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EC2 Transit Gateway Route Table propagation.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">RouteTablePropagation</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">transit_gateway_attachment_id</span><span class="o">=</span><span class="n">aws_ec2_transit_gateway_vpc_attachment</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">transit_gateway_route_table_id</span><span class="o">=</span><span class="n">aws_ec2_transit_gateway_route_table</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>transit_gateway_attachment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway Attachment.</p></li>
<li><p><strong>transit_gateway_route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway Route Table.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTablePropagation.resource_id">
<code class="sig-name descname">resource_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTablePropagation.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the resource</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTablePropagation.resource_type">
<code class="sig-name descname">resource_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTablePropagation.resource_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the resource</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTablePropagation.transit_gateway_attachment_id">
<code class="sig-name descname">transit_gateway_attachment_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTablePropagation.transit_gateway_attachment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway Attachment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.RouteTablePropagation.transit_gateway_route_table_id">
<code class="sig-name descname">transit_gateway_route_table_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTablePropagation.transit_gateway_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway Route Table.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2transitgateway.RouteTablePropagation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_attachment_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_route_table_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTablePropagation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RouteTablePropagation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the resource</p></li>
<li><p><strong>resource_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the resource</p></li>
<li><p><strong>transit_gateway_attachment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway Attachment.</p></li>
<li><p><strong>transit_gateway_route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway Route Table.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2transitgateway.RouteTablePropagation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTablePropagation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.RouteTablePropagation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.RouteTablePropagation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.TransitGateway">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">TransitGateway</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_side_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_accept_shared_attachments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_route_table_association</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_route_table_propagation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_support</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_ecmp_support</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EC2 Transit Gateway.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">TransitGateway</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>amazon_side_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is <code class="docutils literal notranslate"><span class="pre">64512</span></code> to <code class="docutils literal notranslate"><span class="pre">65534</span></code> for 16-bit ASNs and <code class="docutils literal notranslate"><span class="pre">4200000000</span></code> to <code class="docutils literal notranslate"><span class="pre">4294967294</span></code> for 32-bit ASNs. Default value: <code class="docutils literal notranslate"><span class="pre">64512</span></code>.</p></li>
<li><p><strong>auto_accept_shared_attachments</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether resource attachment requests are automatically accepted. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">disable</span></code>.</p></li>
<li><p><strong>default_route_table_association</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether resource attachments are automatically associated with the default association route table. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p></li>
<li><p><strong>default_route_table_propagation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether resource attachments automatically propagate routes to the default propagation route table. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the EC2 Transit Gateway.</p></li>
<li><p><strong>dns_support</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether DNS support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value tags for the EC2 Transit Gateway.</p></li>
<li><p><strong>vpn_ecmp_support</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether VPN Equal Cost Multipath Protocol support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.amazon_side_asn">
<code class="sig-name descname">amazon_side_asn</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.amazon_side_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>Private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is <code class="docutils literal notranslate"><span class="pre">64512</span></code> to <code class="docutils literal notranslate"><span class="pre">65534</span></code> for 16-bit ASNs and <code class="docutils literal notranslate"><span class="pre">4200000000</span></code> to <code class="docutils literal notranslate"><span class="pre">4294967294</span></code> for 32-bit ASNs. Default value: <code class="docutils literal notranslate"><span class="pre">64512</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>EC2 Transit Gateway Amazon Resource Name (ARN)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.association_default_route_table_id">
<code class="sig-name descname">association_default_route_table_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.association_default_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the default association route table</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.auto_accept_shared_attachments">
<code class="sig-name descname">auto_accept_shared_attachments</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.auto_accept_shared_attachments" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether resource attachment requests are automatically accepted. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">disable</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.default_route_table_association">
<code class="sig-name descname">default_route_table_association</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.default_route_table_association" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether resource attachments are automatically associated with the default association route table. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.default_route_table_propagation">
<code class="sig-name descname">default_route_table_propagation</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.default_route_table_propagation" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether resource attachments automatically propagate routes to the default propagation route table. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the EC2 Transit Gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.dns_support">
<code class="sig-name descname">dns_support</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.dns_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether DNS support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.owner_id">
<code class="sig-name descname">owner_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the AWS account that owns the EC2 Transit Gateway</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.propagation_default_route_table_id">
<code class="sig-name descname">propagation_default_route_table_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.propagation_default_route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the default propagation route table</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value tags for the EC2 Transit Gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.vpn_ecmp_support">
<code class="sig-name descname">vpn_ecmp_support</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.vpn_ecmp_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether VPN Equal Cost Multipath Protocol support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">amazon_side_asn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">association_default_route_table_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_accept_shared_attachments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_route_table_association</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_route_table_propagation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_support</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">propagation_default_route_table_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_ecmp_support</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TransitGateway resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>amazon_side_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Private Autonomous System Number (ASN) for the Amazon side of a BGP session. The range is <code class="docutils literal notranslate"><span class="pre">64512</span></code> to <code class="docutils literal notranslate"><span class="pre">65534</span></code> for 16-bit ASNs and <code class="docutils literal notranslate"><span class="pre">4200000000</span></code> to <code class="docutils literal notranslate"><span class="pre">4294967294</span></code> for 32-bit ASNs. Default value: <code class="docutils literal notranslate"><span class="pre">64512</span></code>.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – EC2 Transit Gateway Amazon Resource Name (ARN)</p></li>
<li><p><strong>association_default_route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the default association route table</p></li>
<li><p><strong>auto_accept_shared_attachments</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether resource attachment requests are automatically accepted. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">disable</span></code>.</p></li>
<li><p><strong>default_route_table_association</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether resource attachments are automatically associated with the default association route table. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p></li>
<li><p><strong>default_route_table_propagation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether resource attachments automatically propagate routes to the default propagation route table. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the EC2 Transit Gateway.</p></li>
<li><p><strong>dns_support</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether DNS support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p></li>
<li><p><strong>owner_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the AWS account that owns the EC2 Transit Gateway</p></li>
<li><p><strong>propagation_default_route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the default propagation route table</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value tags for the EC2 Transit Gateway.</p></li>
<li><p><strong>vpn_ecmp_support</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether VPN Equal Cost Multipath Protocol support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.TransitGateway.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.TransitGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">VpcAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_support</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_support</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_default_route_table_association</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_default_route_table_propagation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an EC2 Transit Gateway VPC Attachment. For examples of custom route table association and propagation, see the EC2 Transit Gateway Networking Examples Guide.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">VpcAttachment</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">subnet_ids</span><span class="o">=</span><span class="p">[</span><span class="n">aws_subnet</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]],</span>
    <span class="n">transit_gateway_id</span><span class="o">=</span><span class="n">aws_ec2_transit_gateway</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">aws_vpc</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dns_support</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether DNS support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p></li>
<li><p><strong>ipv6_support</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether IPv6 support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">disable</span></code>.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Identifiers of EC2 Subnets.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value tags for the EC2 Transit Gateway VPC Attachment.</p></li>
<li><p><strong>transit_gateway_default_route_table_association</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether the VPC Attachment should be associated with the EC2 Transit Gateway association default route table. This cannot be configured or perform drift detection with Resource Access Manager shared EC2 Transit Gateways. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>transit_gateway_default_route_table_propagation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether the VPC Attachment should propagate routes with the EC2 Transit Gateway propagation default route table. This cannot be configured or perform drift detection with Resource Access Manager shared EC2 Transit Gateways. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>transit_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 VPC.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.dns_support">
<code class="sig-name descname">dns_support</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.dns_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether DNS support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.ipv6_support">
<code class="sig-name descname">ipv6_support</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.ipv6_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether IPv6 support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">disable</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifiers of EC2 Subnets.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value tags for the EC2 Transit Gateway VPC Attachment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.transit_gateway_default_route_table_association">
<code class="sig-name descname">transit_gateway_default_route_table_association</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.transit_gateway_default_route_table_association" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether the VPC Attachment should be associated with the EC2 Transit Gateway association default route table. This cannot be configured or perform drift detection with Resource Access Manager shared EC2 Transit Gateways. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.transit_gateway_default_route_table_propagation">
<code class="sig-name descname">transit_gateway_default_route_table_propagation</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.transit_gateway_default_route_table_propagation" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether the VPC Attachment should propagate routes with the EC2 Transit Gateway propagation default route table. This cannot be configured or perform drift detection with Resource Access Manager shared EC2 Transit Gateways. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.transit_gateway_id">
<code class="sig-name descname">transit_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.transit_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 VPC.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.vpc_owner_id">
<code class="sig-name descname">vpc_owner_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.vpc_owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the AWS account that owns the EC2 VPC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_support</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_support</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_default_route_table_association</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_default_route_table_propagation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_owner_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VpcAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dns_support</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether DNS support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p></li>
<li><p><strong>ipv6_support</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether IPv6 support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">disable</span></code>.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Identifiers of EC2 Subnets.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value tags for the EC2 Transit Gateway VPC Attachment.</p></li>
<li><p><strong>transit_gateway_default_route_table_association</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether the VPC Attachment should be associated with the EC2 Transit Gateway association default route table. This cannot be configured or perform drift detection with Resource Access Manager shared EC2 Transit Gateways. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>transit_gateway_default_route_table_propagation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether the VPC Attachment should propagate routes with the EC2 Transit Gateway propagation default route table. This cannot be configured or perform drift detection with Resource Access Manager shared EC2 Transit Gateways. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>transit_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 VPC.</p></li>
<li><p><strong>vpc_owner_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the AWS account that owns the EC2 VPC.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.VpcAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.VpcAttachmentAccepter">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">VpcAttachmentAccepter</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_attachment_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_default_route_table_association</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_default_route_table_propagation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachmentAccepter" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the accepter’s side of an EC2 Transit Gateway VPC Attachment.</p>
<p>When a cross-account (requester’s AWS account differs from the accepter’s AWS account) EC2 Transit Gateway VPC Attachment
is created, an EC2 Transit Gateway VPC Attachment resource is automatically created in the accepter’s account.
The requester can use the <code class="docutils literal notranslate"><span class="pre">ec2transitgateway.VpcAttachment</span></code> resource to manage its side of the connection
and the accepter can use the <code class="docutils literal notranslate"><span class="pre">ec2transitgateway.VpcAttachmentAccepter</span></code> resource to “adopt” its side of the
connection into management.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">VpcAttachmentAccepter</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;Name&quot;</span><span class="p">:</span> <span class="s2">&quot;Example cross-account attachment&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">transit_gateway_attachment_id</span><span class="o">=</span><span class="n">aws_ec2_transit_gateway_vpc_attachment</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value tags for the EC2 Transit Gateway VPC Attachment.</p></li>
<li><p><strong>transit_gateway_attachment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the EC2 Transit Gateway Attachment to manage.</p></li>
<li><p><strong>transit_gateway_default_route_table_association</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether the VPC Attachment should be associated with the EC2 Transit Gateway association default route table. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>transit_gateway_default_route_table_propagation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether the VPC Attachment should propagate routes with the EC2 Transit Gateway propagation default route table. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.dns_support">
<code class="sig-name descname">dns_support</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.dns_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether DNS support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.ipv6_support">
<code class="sig-name descname">ipv6_support</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.ipv6_support" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether IPv6 support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.subnet_ids">
<code class="sig-name descname">subnet_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.subnet_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifiers of EC2 Subnets.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value tags for the EC2 Transit Gateway VPC Attachment.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.transit_gateway_attachment_id">
<code class="sig-name descname">transit_gateway_attachment_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.transit_gateway_attachment_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the EC2 Transit Gateway Attachment to manage.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.transit_gateway_default_route_table_association">
<code class="sig-name descname">transit_gateway_default_route_table_association</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.transit_gateway_default_route_table_association" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether the VPC Attachment should be associated with the EC2 Transit Gateway association default route table. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.transit_gateway_default_route_table_propagation">
<code class="sig-name descname">transit_gateway_default_route_table_propagation</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.transit_gateway_default_route_table_propagation" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean whether the VPC Attachment should propagate routes with the EC2 Transit Gateway propagation default route table. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.transit_gateway_id">
<code class="sig-name descname">transit_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.transit_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 Transit Gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of EC2 VPC.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.vpc_owner_id">
<code class="sig-name descname">vpc_owner_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.vpc_owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier of the AWS account that owns the EC2 VPC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_support</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipv6_support</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_attachment_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_default_route_table_association</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_default_route_table_propagation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_owner_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VpcAttachmentAccepter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dns_support</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether DNS support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p></li>
<li><p><strong>ipv6_support</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whether IPv6 support is enabled. Valid values: <code class="docutils literal notranslate"><span class="pre">disable</span></code>, <code class="docutils literal notranslate"><span class="pre">enable</span></code>.</p></li>
<li><p><strong>subnet_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Identifiers of EC2 Subnets.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value tags for the EC2 Transit Gateway VPC Attachment.</p></li>
<li><p><strong>transit_gateway_attachment_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the EC2 Transit Gateway Attachment to manage.</p></li>
<li><p><strong>transit_gateway_default_route_table_association</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether the VPC Attachment should be associated with the EC2 Transit Gateway association default route table. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>transit_gateway_default_route_table_propagation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean whether the VPC Attachment should propagate routes with the EC2 Transit Gateway propagation default route table. Default value: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>transit_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 Transit Gateway.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of EC2 VPC.</p></li>
<li><p><strong>vpc_owner_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier of the AWS account that owns the EC2 VPC.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.VpcAttachmentAccepter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2transitgateway.get_direct_connect_gateway_attachment">
<code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">get_direct_connect_gateway_attachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">dx_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.get_direct_connect_gateway_attachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on an EC2 Transit Gateway’s attachment to a Direct Connect Gateway.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">get_direct_connect_gateway_attachment</span><span class="p">(</span><span class="n">dx_gateway_id</span><span class="o">=</span><span class="n">aws_dx_gateway</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">transit_gateway_id</span><span class="o">=</span><span class="n">aws_ec2_transit_gateway</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dx_gateway_id</strong> (<em>str</em>) – Identifier of the Direct Connect Gateway.</p></li>
<li><p><strong>filters</strong> (<em>list</em>) – Configuration block(s) for filtering. Detailed below.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A map of tags, each pair of which must exactly match a pair on the desired Transit Gateway Direct Connect Gateway Attachment.</p></li>
<li><p><strong>transit_gateway_id</strong> (<em>str</em>) – Identifier of the EC2 Transit Gateway.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the filter field. Valid values can be found in the <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayAttachments.html">EC2 DescribeTransitGatewayAttachments API Reference</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Set of values that are accepted for the given filter field. Results will be selected if any given value matches.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.ec2transitgateway.get_peering_attachment">
<code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">get_peering_attachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.get_peering_attachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on an EC2 Transit Gateway Peering Attachment.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">get_peering_attachment</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;transit-gateway-attachment-id&quot;</span><span class="p">,</span>
    <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;tgw-attach-12345678&quot;</span><span class="p">],</span>
<span class="p">}])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">attachment</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">get_peering_attachment</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="s2">&quot;tgw-attach-12345678&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filters</strong> (<em>list</em>) – One or more configuration blocks containing name-values filters. Detailed below.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – Identifier of the EC2 Transit Gateway Peering Attachment.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A mapping of tags, each pair of which must exactly match
a pair on the specific EC2 Transit Gateway Peering Attachment to retrieve.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the field to filter by, as defined by
<a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayPeeringAttachments.html">the underlying AWS API</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Set of values that are accepted for the given field.
An EC2 Transit Gateway Peering Attachment be selected if any one of the given values matches.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.ec2transitgateway.get_route_table">
<code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">get_route_table</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.get_route_table" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on an EC2 Transit Gateway Route Table.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">get_route_table</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="p">[</span>
    <span class="p">{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;default-association-route-table&quot;</span><span class="p">,</span>
        <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;true&quot;</span><span class="p">],</span>
    <span class="p">},</span>
    <span class="p">{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;transit-gateway-id&quot;</span><span class="p">,</span>
        <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;tgw-12345678&quot;</span><span class="p">],</span>
    <span class="p">},</span>
<span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">get_route_table</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="s2">&quot;tgw-rtb-12345678&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filters</strong> (<em>list</em>) – One or more configuration blocks containing name-values filters. Detailed below.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – Identifier of the EC2 Transit Gateway Route Table.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – Key-value tags for the EC2 Transit Gateway Route Table</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the filter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of one or more values for the filter.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.ec2transitgateway.get_transit_gateway">
<code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">get_transit_gateway</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.get_transit_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on an EC2 Transit Gateway.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">get_transit_gateway</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;options.amazon-side-asn&quot;</span><span class="p">,</span>
    <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;64512&quot;</span><span class="p">],</span>
<span class="p">}])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">get_transit_gateway</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="s2">&quot;tgw-12345678&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filters</strong> (<em>list</em>) – One or more configuration blocks containing name-values filters. Detailed below.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – Identifier of the EC2 Transit Gateway.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – Key-value tags for the EC2 Transit Gateway</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the filter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of one or more values for the filter.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.ec2transitgateway.get_vpc_attachment">
<code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">get_vpc_attachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.get_vpc_attachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on an EC2 Transit Gateway VPC Attachment.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">get_vpc_attachment</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;vpc-id&quot;</span><span class="p">,</span>
    <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;vpc-12345678&quot;</span><span class="p">],</span>
<span class="p">}])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">get_vpc_attachment</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="s2">&quot;tgw-attach-12345678&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filters</strong> (<em>list</em>) – One or more configuration blocks containing name-values filters. Detailed below.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – Identifier of the EC2 Transit Gateway VPC Attachment.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – Key-value tags for the EC2 Transit Gateway VPC Attachment</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the filter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of one or more values for the filter.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_aws.ec2transitgateway.get_vpn_attachment">
<code class="sig-prename descclassname">pulumi_aws.ec2transitgateway.</code><code class="sig-name descname">get_vpn_attachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transit_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2transitgateway.get_vpn_attachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information on an EC2 Transit Gateway VPN Attachment.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">get_vpn_attachment</span><span class="p">(</span><span class="n">transit_gateway_id</span><span class="o">=</span><span class="n">aws_ec2_transit_gateway</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">vpn_connection_id</span><span class="o">=</span><span class="n">aws_vpn_connection</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2transitgateway</span><span class="o">.</span><span class="n">get_vpn_attachment</span><span class="p">(</span><span class="n">filters</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;resource-id&quot;</span><span class="p">,</span>
    <span class="s2">&quot;values&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;some-resource&quot;</span><span class="p">],</span>
<span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filters</strong> (<em>list</em>) – Configuration block(s) for filtering. Detailed below.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A map of tags, each pair of which must exactly match a pair on the desired Transit Gateway VPN Attachment.</p></li>
<li><p><strong>transit_gateway_id</strong> (<em>str</em>) – Identifier of the EC2 Transit Gateway.</p></li>
<li><p><strong>vpn_connection_id</strong> (<em>str</em>) – Identifier of the EC2 VPN Connection.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the filter field. Valid values can be found in the <a class="reference external" href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayAttachments.html">EC2 DescribeTransitGatewayAttachments API Reference</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Set of values that are accepted for the given filter field. Results will be selected if any given value matches.</p></li>
</ul>
</dd></dl>

</div>
