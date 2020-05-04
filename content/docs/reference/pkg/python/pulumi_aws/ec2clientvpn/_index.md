---
title: Module ec2clientvpn
title_tag: Module ec2clientvpn | Package pulumi_aws | Python SDK
linktitle: ec2clientvpn
notitle: true
---

<div class="section" id="ec2clientvpn">
<h1>ec2clientvpn<a class="headerlink" href="#ec2clientvpn" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.ec2clientvpn"></span><dl class="py class">
<dt id="pulumi_aws.ec2clientvpn.Endpoint">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2clientvpn.</code><code class="sig-name descname">Endpoint</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authentication_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_log_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_certificate_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">split_tunnel</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transport_protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2clientvpn.Endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS Client VPN endpoint for OpenVPN clients. For more information on usage, please see the
<a class="reference external" href="https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html">AWS Client VPN Administrator’s Guide</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authentication_options</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Information about the authentication method to be used to authenticate clients.</p></li>
<li><p><strong>client_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 address range, in CIDR notation, from which to assign client IP addresses. The address range cannot overlap with the local CIDR of the VPC in which the associated subnet is located, or the routes that you add manually. The address range cannot be changed after the Client VPN endpoint has been created. The CIDR block should be /22 or greater.</p></li>
<li><p><strong>connection_log_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Information about the client connection logging options.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the repository.</p></li>
<li><p><strong>dns_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Information about the DNS servers to be used for DNS resolution. A Client VPN endpoint can have up to two DNS servers. If no DNS server is specified, the DNS address of the VPC that is to be associated with Client VPN endpoint is used as the DNS server.</p></li>
<li><p><strong>server_certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the ACM server certificate.</p></li>
<li><p><strong>split_tunnel</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether split-tunnel is enabled on VPN endpoint. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>transport_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The transport protocol to be used by the VPN session. Default value is <code class="docutils literal notranslate"><span class="pre">udp</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>authentication_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">active_directory_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Active Directory to be used for authentication if type is <code class="docutils literal notranslate"><span class="pre">directory-service-authentication</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootCertificateChainArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the client certificate. The certificate must be signed by a certificate authority (CA) and it must be provisioned in AWS Certificate Manager (ACM). Only necessary when type is set to <code class="docutils literal notranslate"><span class="pre">certificate-authentication</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of client authentication to be used. Specify <code class="docutils literal notranslate"><span class="pre">certificate-authentication</span></code> to use certificate-based authentication, or <code class="docutils literal notranslate"><span class="pre">directory-service-authentication</span></code> to use Active Directory authentication.</p></li>
</ul>
<p>The <strong>connection_log_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchLogGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the CloudWatch Logs log group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchLogStream</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the CloudWatch Logs log stream to which the connection data is published.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether connection logging is enabled.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.ec2clientvpn.Endpoint.authentication_options">
<code class="sig-name descname">authentication_options</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2clientvpn.Endpoint.authentication_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about the authentication method to be used to authenticate clients.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">active_directory_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Active Directory to be used for authentication if type is <code class="docutils literal notranslate"><span class="pre">directory-service-authentication</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootCertificateChainArn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARN of the client certificate. The certificate must be signed by a certificate authority (CA) and it must be provisioned in AWS Certificate Manager (ACM). Only necessary when type is set to <code class="docutils literal notranslate"><span class="pre">certificate-authentication</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of client authentication to be used. Specify <code class="docutils literal notranslate"><span class="pre">certificate-authentication</span></code> to use certificate-based authentication, or <code class="docutils literal notranslate"><span class="pre">directory-service-authentication</span></code> to use Active Directory authentication.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2clientvpn.Endpoint.client_cidr_block">
<code class="sig-name descname">client_cidr_block</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2clientvpn.Endpoint.client_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The IPv4 address range, in CIDR notation, from which to assign client IP addresses. The address range cannot overlap with the local CIDR of the VPC in which the associated subnet is located, or the routes that you add manually. The address range cannot be changed after the Client VPN endpoint has been created. The CIDR block should be /22 or greater.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2clientvpn.Endpoint.connection_log_options">
<code class="sig-name descname">connection_log_options</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2clientvpn.Endpoint.connection_log_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about the client connection logging options.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchLogGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the CloudWatch Logs log group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchLogStream</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the CloudWatch Logs log stream to which the connection data is published.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether connection logging is enabled.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2clientvpn.Endpoint.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2clientvpn.Endpoint.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2clientvpn.Endpoint.dns_name">
<code class="sig-name descname">dns_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2clientvpn.Endpoint.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS name to be used by clients when establishing their VPN session.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2clientvpn.Endpoint.dns_servers">
<code class="sig-name descname">dns_servers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2clientvpn.Endpoint.dns_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>Information about the DNS servers to be used for DNS resolution. A Client VPN endpoint can have up to two DNS servers. If no DNS server is specified, the DNS address of the VPC that is to be associated with Client VPN endpoint is used as the DNS server.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2clientvpn.Endpoint.server_certificate_arn">
<code class="sig-name descname">server_certificate_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2clientvpn.Endpoint.server_certificate_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the ACM server certificate.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2clientvpn.Endpoint.split_tunnel">
<code class="sig-name descname">split_tunnel</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2clientvpn.Endpoint.split_tunnel" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether split-tunnel is enabled on VPN endpoint. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2clientvpn.Endpoint.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2clientvpn.Endpoint.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current state of the Client VPN endpoint.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2clientvpn.Endpoint.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2clientvpn.Endpoint.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2clientvpn.Endpoint.transport_protocol">
<code class="sig-name descname">transport_protocol</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2clientvpn.Endpoint.transport_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The transport protocol to be used by the VPN session. Default value is <code class="docutils literal notranslate"><span class="pre">udp</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2clientvpn.Endpoint.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authentication_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_log_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dns_servers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">server_certificate_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">split_tunnel</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">transport_protocol</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2clientvpn.Endpoint.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Endpoint resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authentication_options</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Information about the authentication method to be used to authenticate clients.</p></li>
<li><p><strong>client_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IPv4 address range, in CIDR notation, from which to assign client IP addresses. The address range cannot overlap with the local CIDR of the VPC in which the associated subnet is located, or the routes that you add manually. The address range cannot be changed after the Client VPN endpoint has been created. The CIDR block should be /22 or greater.</p></li>
<li><p><strong>connection_log_options</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Information about the client connection logging options.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the repository.</p></li>
<li><p><strong>dns_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS name to be used by clients when establishing their VPN session.</p></li>
<li><p><strong>dns_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Information about the DNS servers to be used for DNS resolution. A Client VPN endpoint can have up to two DNS servers. If no DNS server is specified, the DNS address of the VPC that is to be associated with Client VPN endpoint is used as the DNS server.</p></li>
<li><p><strong>server_certificate_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the ACM server certificate.</p></li>
<li><p><strong>split_tunnel</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether split-tunnel is enabled on VPN endpoint. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current state of the Client VPN endpoint.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
<li><p><strong>transport_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The transport protocol to be used by the VPN session. Default value is <code class="docutils literal notranslate"><span class="pre">udp</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>authentication_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">active_directory_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Active Directory to be used for authentication if type is <code class="docutils literal notranslate"><span class="pre">directory-service-authentication</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootCertificateChainArn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARN of the client certificate. The certificate must be signed by a certificate authority (CA) and it must be provisioned in AWS Certificate Manager (ACM). Only necessary when type is set to <code class="docutils literal notranslate"><span class="pre">certificate-authentication</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of client authentication to be used. Specify <code class="docutils literal notranslate"><span class="pre">certificate-authentication</span></code> to use certificate-based authentication, or <code class="docutils literal notranslate"><span class="pre">directory-service-authentication</span></code> to use Active Directory authentication.</p></li>
</ul>
<p>The <strong>connection_log_options</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchLogGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the CloudWatch Logs log group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cloudwatchLogStream</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the CloudWatch Logs log stream to which the connection data is published.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether connection logging is enabled.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2clientvpn.Endpoint.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2clientvpn.Endpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2clientvpn.Endpoint.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2clientvpn.Endpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2clientvpn.NetworkAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.ec2clientvpn.</code><code class="sig-name descname">NetworkAssociation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_vpn_endpoint_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2clientvpn.NetworkAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides network associations for AWS Client VPN endpoints. For more information on usage, please see the 
<a class="reference external" href="https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html">AWS Client VPN Administrator’s Guide</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_vpn_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Client VPN endpoint.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnet to associate with the Client VPN endpoint.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.ec2clientvpn.NetworkAssociation.client_vpn_endpoint_id">
<code class="sig-name descname">client_vpn_endpoint_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2clientvpn.NetworkAssociation.client_vpn_endpoint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Client VPN endpoint.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2clientvpn.NetworkAssociation.security_groups">
<code class="sig-name descname">security_groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2clientvpn.NetworkAssociation.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>The IDs of the security groups applied to the target network association.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2clientvpn.NetworkAssociation.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2clientvpn.NetworkAssociation.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current state of the target network association.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2clientvpn.NetworkAssociation.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2clientvpn.NetworkAssociation.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the subnet to associate with the Client VPN endpoint.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.ec2clientvpn.NetworkAssociation.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.ec2clientvpn.NetworkAssociation.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPC in which the target network (subnet) is located.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2clientvpn.NetworkAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_vpn_endpoint_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2clientvpn.NetworkAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>client_vpn_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Client VPN endpoint.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The IDs of the security groups applied to the target network association.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current state of the target network association.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the subnet to associate with the Client VPN endpoint.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPC in which the target network (subnet) is located.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.ec2clientvpn.NetworkAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2clientvpn.NetworkAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.ec2clientvpn.NetworkAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.ec2clientvpn.NetworkAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
