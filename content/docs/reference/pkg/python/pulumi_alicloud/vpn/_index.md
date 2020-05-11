---
title: Module vpn
title_tag: Module vpn | Package pulumi_alicloud | Python SDK
linktitle: vpn
notitle: true
---

<div class="section" id="vpn">
<h1>vpn<a class="headerlink" href="#vpn" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.vpn"></span><dl class="py class">
<dt id="pulumi_alicloud.vpn.AwaitableGetConnectionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.vpn.</code><code class="sig-name descname">AwaitableGetConnectionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">connections</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.AwaitableGetConnectionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.vpn.AwaitableGetCustomerGatewaysResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.vpn.</code><code class="sig-name descname">AwaitableGetCustomerGatewaysResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">gateways</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.AwaitableGetCustomerGatewaysResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.vpn.AwaitableGetGatewaysResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.vpn.</code><code class="sig-name descname">AwaitableGetGatewaysResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">business_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateways</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.AwaitableGetGatewaysResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.vpn.Connection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.vpn.</code><code class="sig-name descname">Connection</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">effect_immediately</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ike_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipsec_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local_subnets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remote_subnets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.Connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Connection resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] customer_gateway_id: The ID of the customer gateway.
:param pulumi.Input[bool] effect_immediately: Whether to delete a successfully negotiated IPsec tunnel and initiate a negotiation again. Valid value:true,false.
:param pulumi.Input[list] ike_configs: The configurations of phase-one negotiation.
:param pulumi.Input[list] ipsec_configs: The configurations of phase-two negotiation.
:param pulumi.Input[list] local_subnets: The CIDR block of the VPC to be connected with the local data center. This parameter is used for phase-two negotiation.
:param pulumi.Input[str] name: The name of the IPsec connection.
:param pulumi.Input[list] remote_subnets: The CIDR block of the local data center. This parameter is used for phase-two negotiation.
:param pulumi.Input[str] vpn_gateway_id: The ID of the VPN gateway.</p>
<p>The <strong>ike_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ikeAuthAlg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authentication algorithm of phase-one negotiation. Valid value: md5 | sha1 | sha256 | sha384 | sha512 <a href="#id1"><span class="problematic" id="id2">|</span></a>. Default value: sha1</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeEncAlg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The encryption algorithm of phase-one negotiation. Valid value: aes | aes192 | aes256 | des | 3des. Default Valid value: aes</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The SA lifecycle as the result of phase-one negotiation. The valid value of n is [0, 86400], the unit is second and the default value is 86400.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeLocalId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identification of the VPN gateway.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The negotiation mode of IKE V1. Valid value: main (main mode) | aggressive (aggressive mode). Default value: main</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikePfs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Diffie-Hellman key exchange algorithm used by phase-one negotiation. Valid value: group1 | group2 | group5 | group14 | group24. Default value: group2</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeRemoteId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identification of the customer gateway.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of the IKE protocol. Valid value: ikev1 | ikev2. Default value: ikev1</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">psk</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Used for authentication between the IPsec VPN gateway and the customer gateway.</p></li>
</ul>
<p>The <strong>ipsec_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecAuthAlg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authentication algorithm of phase-two negotiation. Valid value: md5 | sha1 | sha256 | sha384 | sha512 <a href="#id3"><span class="problematic" id="id4">|</span></a>. Default value: sha1</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecEncAlg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The encryption algorithm of phase-two negotiation. Valid value: aes | aes192 | aes256 | des | 3des. Default value: aes</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The SA lifecycle as the result of phase-two negotiation. The valid value is [0, 86400], the unit is second and the default value is 86400.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecPfs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Diffie-Hellman key exchange algorithm used by phase-two negotiation. Valid value: group1 | group2 | group5 | group14 | group24| disabled. Default value: group2</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Connection.customer_gateway_id">
<code class="sig-name descname">customer_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Connection.customer_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the customer gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Connection.effect_immediately">
<code class="sig-name descname">effect_immediately</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Connection.effect_immediately" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to delete a successfully negotiated IPsec tunnel and initiate a negotiation again. Valid value:true,false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Connection.ike_configs">
<code class="sig-name descname">ike_configs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Connection.ike_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>The configurations of phase-one negotiation.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ikeAuthAlg</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The authentication algorithm of phase-one negotiation. Valid value: md5 | sha1 | sha256 | sha384 | sha512 <a href="#id5"><span class="problematic" id="id6">|</span></a>. Default value: sha1</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeEncAlg</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The encryption algorithm of phase-one negotiation. Valid value: aes | aes192 | aes256 | des | 3des. Default Valid value: aes</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The SA lifecycle as the result of phase-one negotiation. The valid value of n is [0, 86400], the unit is second and the default value is 86400.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeLocalId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The identification of the VPN gateway.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The negotiation mode of IKE V1. Valid value: main (main mode) | aggressive (aggressive mode). Default value: main</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikePfs</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Diffie-Hellman key exchange algorithm used by phase-one negotiation. Valid value: group1 | group2 | group5 | group14 | group24. Default value: group2</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeRemoteId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The identification of the customer gateway.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The version of the IKE protocol. Valid value: ikev1 | ikev2. Default value: ikev1</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">psk</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Used for authentication between the IPsec VPN gateway and the customer gateway.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Connection.ipsec_configs">
<code class="sig-name descname">ipsec_configs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Connection.ipsec_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>The configurations of phase-two negotiation.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecAuthAlg</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The authentication algorithm of phase-two negotiation. Valid value: md5 | sha1 | sha256 | sha384 | sha512 <a href="#id7"><span class="problematic" id="id8">|</span></a>. Default value: sha1</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecEncAlg</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The encryption algorithm of phase-two negotiation. Valid value: aes | aes192 | aes256 | des | 3des. Default value: aes</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The SA lifecycle as the result of phase-two negotiation. The valid value is [0, 86400], the unit is second and the default value is 86400.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecPfs</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Diffie-Hellman key exchange algorithm used by phase-two negotiation. Valid value: group1 | group2 | group5 | group14 | group24| disabled. Default value: group2</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Connection.local_subnets">
<code class="sig-name descname">local_subnets</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Connection.local_subnets" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block of the VPC to be connected with the local data center. This parameter is used for phase-two negotiation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Connection.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Connection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IPsec connection.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Connection.remote_subnets">
<code class="sig-name descname">remote_subnets</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Connection.remote_subnets" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block of the local data center. This parameter is used for phase-two negotiation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Connection.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Connection.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of VPN connection.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Connection.vpn_gateway_id">
<code class="sig-name descname">vpn_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Connection.vpn_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPN gateway.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.vpn.Connection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">effect_immediately</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ike_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ipsec_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local_subnets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remote_subnets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.Connection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Connection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>customer_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the customer gateway.</p></li>
<li><p><strong>effect_immediately</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to delete a successfully negotiated IPsec tunnel and initiate a negotiation again. Valid value:true,false.</p></li>
<li><p><strong>ike_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The configurations of phase-one negotiation.</p></li>
<li><p><strong>ipsec_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The configurations of phase-two negotiation.</p></li>
<li><p><strong>local_subnets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The CIDR block of the VPC to be connected with the local data center. This parameter is used for phase-two negotiation.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the IPsec connection.</p></li>
<li><p><strong>remote_subnets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The CIDR block of the local data center. This parameter is used for phase-two negotiation.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of VPN connection.</p></li>
<li><p><strong>vpn_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPN gateway.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ike_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ikeAuthAlg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authentication algorithm of phase-one negotiation. Valid value: md5 | sha1 | sha256 | sha384 | sha512 <a href="#id9"><span class="problematic" id="id10">|</span></a>. Default value: sha1</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeEncAlg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The encryption algorithm of phase-one negotiation. Valid value: aes | aes192 | aes256 | des | 3des. Default Valid value: aes</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The SA lifecycle as the result of phase-one negotiation. The valid value of n is [0, 86400], the unit is second and the default value is 86400.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeLocalId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identification of the VPN gateway.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The negotiation mode of IKE V1. Valid value: main (main mode) | aggressive (aggressive mode). Default value: main</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikePfs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Diffie-Hellman key exchange algorithm used by phase-one negotiation. Valid value: group1 | group2 | group5 | group14 | group24. Default value: group2</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeRemoteId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The identification of the customer gateway.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The version of the IKE protocol. Valid value: ikev1 | ikev2. Default value: ikev1</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">psk</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Used for authentication between the IPsec VPN gateway and the customer gateway.</p></li>
</ul>
<p>The <strong>ipsec_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecAuthAlg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The authentication algorithm of phase-two negotiation. Valid value: md5 | sha1 | sha256 | sha384 | sha512 <a href="#id11"><span class="problematic" id="id12">|</span></a>. Default value: sha1</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecEncAlg</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The encryption algorithm of phase-two negotiation. Valid value: aes | aes192 | aes256 | des | 3des. Default value: aes</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The SA lifecycle as the result of phase-two negotiation. The valid value is [0, 86400], the unit is second and the default value is 86400.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecPfs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Diffie-Hellman key exchange algorithm used by phase-two negotiation. Valid value: group1 | group2 | group5 | group14 | group24| disabled. Default value: group2</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.vpn.Connection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.Connection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.vpn.Connection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.Connection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.vpn.CustomerGateway">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.vpn.</code><code class="sig-name descname">CustomerGateway</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.CustomerGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a CustomerGateway resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: The description of the VPN customer gateway instance.
:param pulumi.Input[str] ip_address: The IP address of the customer gateway.
:param pulumi.Input[str] name: The name of the VPN customer gateway. Defaults to null.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.CustomerGateway.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.CustomerGateway.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the VPN customer gateway instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.CustomerGateway.ip_address">
<code class="sig-name descname">ip_address</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.CustomerGateway.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of the customer gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.CustomerGateway.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.CustomerGateway.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the VPN customer gateway. Defaults to null.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.vpn.CustomerGateway.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.CustomerGateway.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CustomerGateway resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the VPN customer gateway instance.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the customer gateway.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the VPN customer gateway. Defaults to null.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.vpn.CustomerGateway.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.CustomerGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.vpn.CustomerGateway.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.CustomerGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.vpn.Gateway">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.vpn.</code><code class="sig-name descname">Gateway</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_ipsec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_ssl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_connections</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.Gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Gateway resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: The description of the VPN instance.
:param pulumi.Input[bool] enable_ipsec: Enable or Disable IPSec VPN. At least one type of VPN should be enabled.
:param pulumi.Input[bool] enable_ssl: Enable or Disable SSL VPN.  At least one type of VPN should be enabled.
:param pulumi.Input[str] instance_charge_type: The charge type for instance. If it is an international site account, the valid value is PostPaid, otherwise PrePaid.</p>
<blockquote>
<div><p>Default to PostPaid.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the VPN. Defaults to null.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The filed is only required while the InstanceChargeType is PrePaid. Valid values: [1-9, 12, 24, 36]. Default to 1.</p></li>
<li><p><strong>ssl_connections</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The max connections of SSL VPN. Default to 5. The number of connections supported by each account is different. 
This field is ignored when enable_ssl is false.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPN belongs the vpc_id, the field can’t be changed.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPN belongs the vswitch_id, the field can’t be changed.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Gateway.business_status">
<code class="sig-name descname">business_status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Gateway.business_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The business status of the VPN gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Gateway.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Gateway.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the VPN instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Gateway.enable_ipsec">
<code class="sig-name descname">enable_ipsec</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Gateway.enable_ipsec" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or Disable IPSec VPN. At least one type of VPN should be enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Gateway.enable_ssl">
<code class="sig-name descname">enable_ssl</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Gateway.enable_ssl" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or Disable SSL VPN.  At least one type of VPN should be enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Gateway.instance_charge_type">
<code class="sig-name descname">instance_charge_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Gateway.instance_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The charge type for instance. If it is an international site account, the valid value is PostPaid, otherwise PrePaid. 
Default to PostPaid.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Gateway.internet_ip">
<code class="sig-name descname">internet_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Gateway.internet_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The internet ip of the VPN.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Gateway.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Gateway.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the VPN. Defaults to null.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Gateway.period">
<code class="sig-name descname">period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Gateway.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The filed is only required while the InstanceChargeType is PrePaid. Valid values: [1-9, 12, 24, 36]. Default to 1.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Gateway.ssl_connections">
<code class="sig-name descname">ssl_connections</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Gateway.ssl_connections" title="Permalink to this definition">¶</a></dt>
<dd><p>The max connections of SSL VPN. Default to 5. The number of connections supported by each account is different. 
This field is ignored when enable_ssl is false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Gateway.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Gateway.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the VPN gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Gateway.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Gateway.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPN belongs the vpc_id, the field can’t be changed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.Gateway.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.Gateway.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPN belongs the vswitch_id, the field can’t be changed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.vpn.Gateway.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">business_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_ipsec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_ssl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_connections</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.Gateway.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Gateway resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>business_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The business status of the VPN gateway.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the VPN instance.</p></li>
<li><p><strong>enable_ipsec</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or Disable IPSec VPN. At least one type of VPN should be enabled.</p></li>
<li><p><strong>enable_ssl</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or Disable SSL VPN.  At least one type of VPN should be enabled.</p></li>
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The charge type for instance. If it is an international site account, the valid value is PostPaid, otherwise PrePaid. 
Default to PostPaid.</p></li>
<li><p><strong>internet_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The internet ip of the VPN.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the VPN. Defaults to null.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The filed is only required while the InstanceChargeType is PrePaid. Valid values: [1-9, 12, 24, 36]. Default to 1.</p></li>
<li><p><strong>ssl_connections</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The max connections of SSL VPN. Default to 5. The number of connections supported by each account is different. 
This field is ignored when enable_ssl is false.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the VPN gateway.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPN belongs the vpc_id, the field can’t be changed.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPN belongs the vswitch_id, the field can’t be changed.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.vpn.Gateway.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.Gateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.vpn.Gateway.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.Gateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.vpn.GetConnectionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.vpn.</code><code class="sig-name descname">GetConnectionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">connections</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.GetConnectionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getConnections.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.GetConnectionsResult.connections">
<code class="sig-name descname">connections</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.GetConnectionsResult.connections" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of VPN connections. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.GetConnectionsResult.customer_gateway_id">
<code class="sig-name descname">customer_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.GetConnectionsResult.customer_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the VPN customer gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.GetConnectionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.GetConnectionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.GetConnectionsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.GetConnectionsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) IDs of the VPN connections.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.GetConnectionsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.GetConnectionsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) names of the VPN connections.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.GetConnectionsResult.vpn_gateway_id">
<code class="sig-name descname">vpn_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.GetConnectionsResult.vpn_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the VPN gateway.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.vpn.GetCustomerGatewaysResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.vpn.</code><code class="sig-name descname">GetCustomerGatewaysResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">gateways</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.GetCustomerGatewaysResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCustomerGateways.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.GetCustomerGatewaysResult.gateways">
<code class="sig-name descname">gateways</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.GetCustomerGatewaysResult.gateways" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of VPN customer gateways. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.GetCustomerGatewaysResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.GetCustomerGatewaysResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.vpn.GetGatewaysResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.vpn.</code><code class="sig-name descname">GetGatewaysResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">business_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gateways</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.GetGatewaysResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGateways.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.GetGatewaysResult.business_status">
<code class="sig-name descname">business_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.GetGatewaysResult.business_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The business status of the VPN gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.GetGatewaysResult.gateways">
<code class="sig-name descname">gateways</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.GetGatewaysResult.gateways" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of VPN gateways. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.GetGatewaysResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.GetGatewaysResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.GetGatewaysResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.GetGatewaysResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>IDs of the VPN.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.GetGatewaysResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.GetGatewaysResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>names of the VPN.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.GetGatewaysResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.GetGatewaysResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the VPN</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.GetGatewaysResult.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.GetGatewaysResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the VPC that the VPN belongs.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.vpn.RouteEntry">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.vpn.</code><code class="sig-name descname">RouteEntry</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">next_hop</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">publish_vpc</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_dest</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.RouteEntry" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a RouteEntry resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] next_hop: The next hop of the destination route.
:param pulumi.Input[bool] publish_vpc: Whether to issue the destination route to the VPC.
:param pulumi.Input[str] route_dest: The destination network segment of the destination route.
:param pulumi.Input[str] vpn_gateway_id: The id of the vpn gateway.
:param pulumi.Input[float] weight: The value should be 0 or 100.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.RouteEntry.next_hop">
<code class="sig-name descname">next_hop</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.RouteEntry.next_hop" title="Permalink to this definition">¶</a></dt>
<dd><p>The next hop of the destination route.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.RouteEntry.publish_vpc">
<code class="sig-name descname">publish_vpc</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.RouteEntry.publish_vpc" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to issue the destination route to the VPC.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.RouteEntry.route_dest">
<code class="sig-name descname">route_dest</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.RouteEntry.route_dest" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination network segment of the destination route.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.RouteEntry.vpn_gateway_id">
<code class="sig-name descname">vpn_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.RouteEntry.vpn_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the vpn gateway.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.RouteEntry.weight">
<code class="sig-name descname">weight</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.RouteEntry.weight" title="Permalink to this definition">¶</a></dt>
<dd><p>The value should be 0 or 100.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.vpn.RouteEntry.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">next_hop</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">publish_vpc</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_dest</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">weight</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.RouteEntry.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RouteEntry resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>next_hop</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The next hop of the destination route.</p></li>
<li><p><strong>publish_vpc</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to issue the destination route to the VPC.</p></li>
<li><p><strong>route_dest</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination network segment of the destination route.</p></li>
<li><p><strong>vpn_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the vpn gateway.</p></li>
<li><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The value should be 0 or 100.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.vpn.RouteEntry.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.RouteEntry.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.vpn.RouteEntry.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.RouteEntry.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.vpn.SslVpnClientCert">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.vpn.</code><code class="sig-name descname">SslVpnClientCert</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_vpn_server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnClientCert" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SslVpnClientCert resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_alicloud.vpn.SslVpnClientCert.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ca_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_cert</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssl_vpn_server_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnClientCert.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SslVpnClientCert resource’s state with the given name, id, and optional extra
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
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.vpn.SslVpnClientCert.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnClientCert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.vpn.SslVpnClientCert.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnClientCert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.vpn.SslVpnServer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.vpn.</code><code class="sig-name descname">SslVpnServer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cipher</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_ip_pool</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compress</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local_subnet</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnServer" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SslVpnServer resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] cipher: The encryption algorithm used by the SSL-VPN server. Valid value: AES-128-CBC (default)| AES-192-CBC | AES-256-CBC | none
:param pulumi.Input[str] client_ip_pool: The CIDR block from which access addresses are allocated to the virtual network interface card of the client.
:param pulumi.Input[bool] compress: Specify whether to compress the communication. Valid value: true (default) | false
:param pulumi.Input[str] local_subnet: The CIDR block to be accessed by the client through the SSL-VPN connection. It supports to set multi CIDRs by comma join ways, like <code class="docutils literal notranslate"><span class="pre">10.0.1.0/24,10.0.2.0/24,10.0.3.0/24</span></code>.
:param pulumi.Input[str] name: The name of the SSL-VPN server.
:param pulumi.Input[float] port: The port used by the SSL-VPN server. The default value is 1194.The following ports cannot be used: [22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, 4500].
:param pulumi.Input[str] protocol: The protocol used by the SSL-VPN server. Valid value: UDP(default) <a href="#id13"><span class="problematic" id="id14">|</span></a>TCP
:param pulumi.Input[str] vpn_gateway_id: The ID of the VPN gateway.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.SslVpnServer.cipher">
<code class="sig-name descname">cipher</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnServer.cipher" title="Permalink to this definition">¶</a></dt>
<dd><p>The encryption algorithm used by the SSL-VPN server. Valid value: AES-128-CBC (default)| AES-192-CBC | AES-256-CBC | none</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.SslVpnServer.client_ip_pool">
<code class="sig-name descname">client_ip_pool</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnServer.client_ip_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block from which access addresses are allocated to the virtual network interface card of the client.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.SslVpnServer.compress">
<code class="sig-name descname">compress</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnServer.compress" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify whether to compress the communication. Valid value: true (default) | false</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.SslVpnServer.connections">
<code class="sig-name descname">connections</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnServer.connections" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of current connections.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.SslVpnServer.internet_ip">
<code class="sig-name descname">internet_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnServer.internet_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The internet IP of the SSL-VPN server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.SslVpnServer.local_subnet">
<code class="sig-name descname">local_subnet</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnServer.local_subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>The CIDR block to be accessed by the client through the SSL-VPN connection. It supports to set multi CIDRs by comma join ways, like <code class="docutils literal notranslate"><span class="pre">10.0.1.0/24,10.0.2.0/24,10.0.3.0/24</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.SslVpnServer.max_connections">
<code class="sig-name descname">max_connections</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnServer.max_connections" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of connections.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.SslVpnServer.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnServer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SSL-VPN server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.SslVpnServer.port">
<code class="sig-name descname">port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnServer.port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port used by the SSL-VPN server. The default value is 1194.The following ports cannot be used: [22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, 4500].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.SslVpnServer.protocol">
<code class="sig-name descname">protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnServer.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol used by the SSL-VPN server. Valid value: UDP(default) <a href="#id15"><span class="problematic" id="id16">|</span></a>TCP</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.vpn.SslVpnServer.vpn_gateway_id">
<code class="sig-name descname">vpn_gateway_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnServer.vpn_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPN gateway.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.vpn.SslVpnServer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cipher</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_ip_pool</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compress</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connections</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">local_subnet</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_connections</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnServer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SslVpnServer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cipher</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The encryption algorithm used by the SSL-VPN server. Valid value: AES-128-CBC (default)| AES-192-CBC | AES-256-CBC | none</p></li>
<li><p><strong>client_ip_pool</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CIDR block from which access addresses are allocated to the virtual network interface card of the client.</p></li>
<li><p><strong>compress</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specify whether to compress the communication. Valid value: true (default) | false</p></li>
<li><p><strong>connections</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of current connections.</p></li>
<li><p><strong>internet_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The internet IP of the SSL-VPN server.</p></li>
<li><p><strong>local_subnet</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CIDR block to be accessed by the client through the SSL-VPN connection. It supports to set multi CIDRs by comma join ways, like <code class="docutils literal notranslate"><span class="pre">10.0.1.0/24,10.0.2.0/24,10.0.3.0/24</span></code>.</p></li>
<li><p><strong>max_connections</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of connections.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SSL-VPN server.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port used by the SSL-VPN server. The default value is 1194.The following ports cannot be used: [22, 2222, 22222, 9000, 9001, 9002, 7505, 80, 443, 53, 68, 123, 4510, 4560, 500, 4500].</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol used by the SSL-VPN server. Valid value: UDP(default) <a href="#id17"><span class="problematic" id="id18">|</span></a>TCP</p></li>
<li><p><strong>vpn_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPN gateway.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.vpn.SslVpnServer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnServer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.vpn.SslVpnServer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.SslVpnServer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.vpn.get_connections">
<code class="sig-prename descclassname">pulumi_alicloud.vpn.</code><code class="sig-name descname">get_connections</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">customer_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpn_gateway_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.get_connections" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPN connections data source lists lots of VPN connections resource information owned by an Alicloud account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>customer_gateway_id</strong> (<em>str</em>) – Use the VPN customer gateway ID as the search key.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – IDs of the VPN connections.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string of VPN connection name.</p></li>
<li><p><strong>output_file</strong> (<em>str</em>) – Save the result to the file.</p></li>
<li><p><strong>vpn_gateway_id</strong> (<em>str</em>) – Use the VPN gateway ID as the search key.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.vpn.get_customer_gateways">
<code class="sig-prename descclassname">pulumi_alicloud.vpn.</code><code class="sig-name descname">get_customer_gateways</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.get_customer_gateways" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPN customers gateways data source lists a number of VPN customer gateways resource information owned by an Alicloud account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – ID of the VPN customer gateways.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string of VPN customer gateways name.</p></li>
<li><p><strong>output_file</strong> (<em>str</em>) – Save the result to the file.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.vpn.get_gateways">
<code class="sig-prename descclassname">pulumi_alicloud.vpn.</code><code class="sig-name descname">get_gateways</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">business_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.vpn.get_gateways" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPNs data source lists a number of VPNs resource information owned by an Alicloud account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>business_status</strong> (<em>str</em>) – Limit search to specific business status - valid value is “Normal”, “FinancialLocked”.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – IDs of the VPN.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string of VPN name.</p></li>
<li><p><strong>output_file</strong> (<em>str</em>) – Save the result to the file.</p></li>
<li><p><strong>status</strong> (<em>str</em>) – Limit search to specific status - valid value is “Init”, “Provisioning”, “Active”, “Updating”, “Deleting”.</p></li>
<li><p><strong>vpc_id</strong> (<em>str</em>) – Use the VPC ID as the search key.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
