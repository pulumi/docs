---
title: Module network
title_tag: Module network | Package pulumi_azure | Python SDK
linktitle: network
notitle: true
---

<div class="section" id="network">
<h1>network<a class="headerlink" href="#network" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.network"></span><dl class="class">
<dt id="pulumi_azure.network.ApplicationGateway">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">ApplicationGateway</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">authentication_certificates=None</em>, <em class="sig-param">autoscale_configuration=None</em>, <em class="sig-param">backend_address_pools=None</em>, <em class="sig-param">backend_http_settings=None</em>, <em class="sig-param">custom_error_configurations=None</em>, <em class="sig-param">enable_http2=None</em>, <em class="sig-param">frontend_ip_configurations=None</em>, <em class="sig-param">frontend_ports=None</em>, <em class="sig-param">gateway_ip_configurations=None</em>, <em class="sig-param">http_listeners=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">probes=None</em>, <em class="sig-param">redirect_configurations=None</em>, <em class="sig-param">request_routing_rules=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">rewrite_rule_sets=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">ssl_certificates=None</em>, <em class="sig-param">ssl_policies=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">trusted_root_certificates=None</em>, <em class="sig-param">url_path_maps=None</em>, <em class="sig-param">waf_configuration=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Application Gateway.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/application_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/application_gateway.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authentication_certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">authentication_certificate</span></code> blocks as defined below.</p></li>
<li><p><strong>autoscale_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">autoscale_configuration</span></code> block as defined below.</p></li>
<li><p><strong>backend_address_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">backend_address_pool</span></code> blocks as defined below.</p></li>
<li><p><strong>backend_http_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">backend_http_settings</span></code> blocks as defined below.</p></li>
<li><p><strong>custom_error_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">custom_error_configuration</span></code> blocks as defined below.</p></li>
<li><p><strong>enable_http2</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is HTTP2 enabled on the application gateway resource? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>frontend_ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration</span></code> blocks as defined below.</p></li>
<li><p><strong>frontend_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">frontend_port</span></code> blocks as defined below.</p></li>
<li><p><strong>gateway_ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">gateway_ip_configuration</span></code> blocks as defined below.</p></li>
<li><p><strong>http_listeners</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">http_listener</span></code> blocks as defined below.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure region where the Application Gateway should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><strong>probes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">probe</span></code> blocks as defined below.</p></li>
<li><p><strong>redirect_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">redirect_configuration</span></code> block as defined below.</p></li>
<li><p><strong>request_routing_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">request_routing_rule</span></code> blocks as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to the Application Gateway should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>rewrite_rule_sets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">rewrite_rule_set</span></code> blocks as defined below. Only valid for v2 SKUs.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p></li>
<li><p><strong>ssl_certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">ssl_certificate</span></code> blocks as defined below.</p></li>
<li><p><strong>ssl_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – a <code class="docutils literal notranslate"><span class="pre">ssl</span> <span class="pre">policy</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>trusted_root_certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">trusted_root_certificate</span></code> blocks as defined below.</p></li>
<li><p><strong>url_path_maps</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">url_path_map</span></code> blocks as defined below.</p></li>
<li><p><strong>waf_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">waf_configuration</span></code> block as defined below.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of availability zones to spread the Application Gateway over.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>authentication_certificates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>autoscale_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>backend_address_pools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fqdns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>backend_http_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">affinityCookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authentication_certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">authentication_certificate</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectionDraining</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">drainTimeoutSec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieBasedAffinity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pickHostNameFromBackendAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">probe_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Probe.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">probeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trustedRootCertificateNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>custom_error_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customErrorPageUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>frontend_ip_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddressAllocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>frontend_ports</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>gateway_ip_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>http_listeners</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">custom_error_configurations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">custom_error_configuration</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">customErrorPageUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Frontend Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontendPortId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Frontend Port.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontendPortName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireSni</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCertificateId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated SSL Certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCertificateName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>probes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">match</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimumServers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pickHostNameFromBackendHttpSettings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unhealthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>redirect_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includePath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeQueryString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetListenerId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetListenerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>request_routing_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">backend_address_pool_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Backend Address Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backendAddressPoolName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backendHttpSettingsId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Backend HTTP Settings Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backendHttpSettingsName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpListenerId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated HTTP Listener.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpListenerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectConfigurationId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Redirect Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectConfigurationName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rewriteRuleSetId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Rewrite Rule Set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rewriteRuleSetName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlPathMapId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated URL Path Map.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlPathMapName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>rewrite_rule_sets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rewriteRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">conditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreCase</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">variable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestHeaderConfigurations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">headerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseHeaderConfigurations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">headerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleSequence</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ssl_certificates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_secret_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicCertData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Public Certificate Data associated with the SSL Certificate.</p></li>
</ul>
<p>The <strong>ssl_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cipherSuites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabledProtocols</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minProtocolVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policy_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>trusted_root_certificates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>url_path_maps</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultBackendAddressPoolId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Default Backend Address Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultBackendAddressPoolName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultBackendHttpSettingsId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Default Backend HTTP Settings Collection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultBackendHttpSettingsName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultRedirectConfigurationId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Default Redirect Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultRedirectConfigurationName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultRewriteRuleSetId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultRewriteRuleSetName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of <code class="docutils literal notranslate"><span class="pre">path_rule</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">backend_address_pool_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Backend Address Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backendAddressPoolName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backendHttpSettingsId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Backend HTTP Settings Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backendHttpSettingsName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">paths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectConfigurationId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Redirect Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectConfigurationName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rewriteRuleSetId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Rewrite Rule Set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rewriteRuleSetName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>waf_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disabledRuleGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleGroupName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selectorMatchOperator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileUploadLimitMb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firewallMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRequestBodySizeKb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestBodyCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleSetType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleSetVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.authentication_certificates">
<code class="sig-name descname">authentication_certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.authentication_certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">authentication_certificate</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.autoscale_configuration">
<code class="sig-name descname">autoscale_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.autoscale_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">autoscale_configuration</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.backend_address_pools">
<code class="sig-name descname">backend_address_pools</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.backend_address_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">backend_address_pool</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fqdns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.backend_http_settings">
<code class="sig-name descname">backend_http_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.backend_http_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">backend_http_settings</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">affinityCookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authentication_certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">authentication_certificate</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectionDraining</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">drainTimeoutSec</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieBasedAffinity</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pickHostNameFromBackendAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">probe_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the associated Probe.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">probeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trustedRootCertificateNames</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.custom_error_configurations">
<code class="sig-name descname">custom_error_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.custom_error_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">custom_error_configuration</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customErrorPageUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.enable_http2">
<code class="sig-name descname">enable_http2</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.enable_http2" title="Permalink to this definition">¶</a></dt>
<dd><p>Is HTTP2 enabled on the application gateway resource? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.frontend_ip_configurations">
<code class="sig-name descname">frontend_ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.frontend_ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddressAllocation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.frontend_ports">
<code class="sig-name descname">frontend_ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.frontend_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">frontend_port</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.gateway_ip_configurations">
<code class="sig-name descname">gateway_ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.gateway_ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">gateway_ip_configuration</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.http_listeners">
<code class="sig-name descname">http_listeners</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.http_listeners" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">http_listener</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">custom_error_configurations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">custom_error_configuration</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">customErrorPageUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the associated Frontend Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontendPortId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the associated Frontend Port.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontendPortName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireSni</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCertificateId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the associated SSL Certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCertificateName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure region where the Application Gateway should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Application Gateway. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.probes">
<code class="sig-name descname">probes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.probes" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">probe</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">match</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCodes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimumServers</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pickHostNameFromBackendHttpSettings</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unhealthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.redirect_configurations">
<code class="sig-name descname">redirect_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.redirect_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">redirect_configuration</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includePath</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeQueryString</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetListenerId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetListenerName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.request_routing_rules">
<code class="sig-name descname">request_routing_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.request_routing_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">request_routing_rule</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">backend_address_pool_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the associated Backend Address Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backendAddressPoolName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backendHttpSettingsId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the associated Backend HTTP Settings Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backendHttpSettingsName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpListenerId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the associated HTTP Listener.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpListenerName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectConfigurationId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the associated Redirect Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectConfigurationName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rewriteRuleSetId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the associated Rewrite Rule Set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rewriteRuleSetName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlPathMapId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the associated URL Path Map.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlPathMapName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to the Application Gateway should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.rewrite_rule_sets">
<code class="sig-name descname">rewrite_rule_sets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.rewrite_rule_sets" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">rewrite_rule_set</span></code> blocks as defined below. Only valid for v2 SKUs.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rewriteRules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">conditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreCase</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negate</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pattern</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">variable</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestHeaderConfigurations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">headerName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseHeaderConfigurations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">headerName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleSequence</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.ssl_certificates">
<code class="sig-name descname">ssl_certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.ssl_certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">ssl_certificate</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_secret_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicCertData</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Public Certificate Data associated with the SSL Certificate.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.ssl_policies">
<code class="sig-name descname">ssl_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.ssl_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>a <code class="docutils literal notranslate"><span class="pre">ssl</span> <span class="pre">policy</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cipherSuites</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabledProtocols</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minProtocolVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policy_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.trusted_root_certificates">
<code class="sig-name descname">trusted_root_certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.trusted_root_certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">trusted_root_certificate</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.url_path_maps">
<code class="sig-name descname">url_path_maps</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.url_path_maps" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">url_path_map</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultBackendAddressPoolId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Default Backend Address Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultBackendAddressPoolName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultBackendHttpSettingsId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Default Backend HTTP Settings Collection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultBackendHttpSettingsName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultRedirectConfigurationId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Default Redirect Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultRedirectConfigurationName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultRewriteRuleSetId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultRewriteRuleSetName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathRules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of <code class="docutils literal notranslate"><span class="pre">path_rule</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">backend_address_pool_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the associated Backend Address Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backendAddressPoolName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backendHttpSettingsId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the associated Backend HTTP Settings Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backendHttpSettingsName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">paths</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectConfigurationId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the associated Redirect Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectConfigurationName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rewriteRuleSetId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the associated Rewrite Rule Set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rewriteRuleSetName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.waf_configuration">
<code class="sig-name descname">waf_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.waf_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">waf_configuration</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disabledRuleGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleGroupName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selectorMatchOperator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileUploadLimitMb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firewallMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRequestBodySizeKb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestBodyCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleSetType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleSetVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationGateway.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of availability zones to spread the Application Gateway over.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.ApplicationGateway.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">authentication_certificates=None</em>, <em class="sig-param">autoscale_configuration=None</em>, <em class="sig-param">backend_address_pools=None</em>, <em class="sig-param">backend_http_settings=None</em>, <em class="sig-param">custom_error_configurations=None</em>, <em class="sig-param">enable_http2=None</em>, <em class="sig-param">frontend_ip_configurations=None</em>, <em class="sig-param">frontend_ports=None</em>, <em class="sig-param">gateway_ip_configurations=None</em>, <em class="sig-param">http_listeners=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">probes=None</em>, <em class="sig-param">redirect_configurations=None</em>, <em class="sig-param">request_routing_rules=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">rewrite_rule_sets=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">ssl_certificates=None</em>, <em class="sig-param">ssl_policies=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">trusted_root_certificates=None</em>, <em class="sig-param">url_path_maps=None</em>, <em class="sig-param">waf_configuration=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApplicationGateway resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authentication_certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">authentication_certificate</span></code> blocks as defined below.</p></li>
<li><p><strong>autoscale_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">autoscale_configuration</span></code> block as defined below.</p></li>
<li><p><strong>backend_address_pools</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">backend_address_pool</span></code> blocks as defined below.</p></li>
<li><p><strong>backend_http_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">backend_http_settings</span></code> blocks as defined below.</p></li>
<li><p><strong>custom_error_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">custom_error_configuration</span></code> blocks as defined below.</p></li>
<li><p><strong>enable_http2</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is HTTP2 enabled on the application gateway resource? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>frontend_ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration</span></code> blocks as defined below.</p></li>
<li><p><strong>frontend_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">frontend_port</span></code> blocks as defined below.</p></li>
<li><p><strong>gateway_ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">gateway_ip_configuration</span></code> blocks as defined below.</p></li>
<li><p><strong>http_listeners</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">http_listener</span></code> blocks as defined below.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure region where the Application Gateway should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><strong>probes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">probe</span></code> blocks as defined below.</p></li>
<li><p><strong>redirect_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">redirect_configuration</span></code> block as defined below.</p></li>
<li><p><strong>request_routing_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">request_routing_rule</span></code> blocks as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to the Application Gateway should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>rewrite_rule_sets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">rewrite_rule_set</span></code> blocks as defined below. Only valid for v2 SKUs.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as defined below.</p></li>
<li><p><strong>ssl_certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">ssl_certificate</span></code> blocks as defined below.</p></li>
<li><p><strong>ssl_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – a <code class="docutils literal notranslate"><span class="pre">ssl</span> <span class="pre">policy</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>trusted_root_certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">trusted_root_certificate</span></code> blocks as defined below.</p></li>
<li><p><strong>url_path_maps</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">url_path_map</span></code> blocks as defined below.</p></li>
<li><p><strong>waf_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">waf_configuration</span></code> block as defined below.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of availability zones to spread the Application Gateway over.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>authentication_certificates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>autoscale_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minCapacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>backend_address_pools</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">fqdns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>backend_http_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">affinityCookieName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">authentication_certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">authentication_certificate</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">connectionDraining</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">drainTimeoutSec</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookieBasedAffinity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pickHostNameFromBackendAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">probe_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Probe.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">probeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trustedRootCertificateNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>custom_error_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customErrorPageUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>frontend_ip_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddressAllocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>frontend_ports</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>gateway_ip_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>http_listeners</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">custom_error_configurations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">custom_error_configuration</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">customErrorPageUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Frontend Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontendPortId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Frontend Port.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontendPortName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireSni</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCertificateId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated SSL Certificate.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sslCertificateName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>probes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">match</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statusCodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">minimumServers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pickHostNameFromBackendHttpSettings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unhealthyThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>redirect_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includePath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeQueryString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetListenerId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetListenerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>request_routing_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">backend_address_pool_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Backend Address Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backendAddressPoolName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backendHttpSettingsId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Backend HTTP Settings Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backendHttpSettingsName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpListenerId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated HTTP Listener.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpListenerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectConfigurationId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Redirect Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectConfigurationName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rewriteRuleSetId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Rewrite Rule Set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rewriteRuleSetName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlPathMapId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated URL Path Map.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlPathMapName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>rewrite_rule_sets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rewriteRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">conditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ignoreCase</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">variable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestHeaderConfigurations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">headerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">responseHeaderConfigurations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">headerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleSequence</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ssl_certificates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_secret_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicCertData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Public Certificate Data associated with the SSL Certificate.</p></li>
</ul>
<p>The <strong>ssl_policies</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cipherSuites</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disabledProtocols</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minProtocolVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">policy_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>trusted_root_certificates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>url_path_maps</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultBackendAddressPoolId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Default Backend Address Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultBackendAddressPoolName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultBackendHttpSettingsId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Default Backend HTTP Settings Collection.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultBackendHttpSettingsName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultRedirectConfigurationId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Default Redirect Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultRedirectConfigurationName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultRewriteRuleSetId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">defaultRewriteRuleSetName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of <code class="docutils literal notranslate"><span class="pre">path_rule</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">backend_address_pool_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Backend Address Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backendAddressPoolName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backendHttpSettingsId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Backend HTTP Settings Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">backendHttpSettingsName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Rewrite Rule Set</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Application Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">paths</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectConfigurationId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Redirect Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectConfigurationName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rewriteRuleSetId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the associated Rewrite Rule Set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rewriteRuleSetName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>waf_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disabledRuleGroups</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleGroupName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">exclusions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchVariable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selectorMatchOperator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileUploadLimitMb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">firewallMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRequestBodySizeKb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestBodyCheck</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleSetType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleSetVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.ApplicationGateway.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ApplicationGateway.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ApplicationGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ApplicationSecurityGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">ApplicationSecurityGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ApplicationSecurityGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Application Security Group.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/application_security_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/application_security_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Application Security Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Application Security Group.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationSecurityGroup.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationSecurityGroup.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationSecurityGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationSecurityGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Application Security Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationSecurityGroup.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationSecurityGroup.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Application Security Group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ApplicationSecurityGroup.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ApplicationSecurityGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.ApplicationSecurityGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ApplicationSecurityGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ApplicationSecurityGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Application Security Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Application Security Group.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.ApplicationSecurityGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ApplicationSecurityGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ApplicationSecurityGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ApplicationSecurityGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.AwaitableGetApplicationSecurityGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">AwaitableGetApplicationSecurityGroupResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.AwaitableGetApplicationSecurityGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.AwaitableGetExpressRouteCircuitResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">AwaitableGetExpressRouteCircuitResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">peerings=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_key=None</em>, <em class="sig-param">service_provider_properties=None</em>, <em class="sig-param">service_provider_provisioning_state=None</em>, <em class="sig-param">sku=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.AwaitableGetExpressRouteCircuitResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.AwaitableGetFirewallResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">AwaitableGetFirewallResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ip_configurations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.AwaitableGetFirewallResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.AwaitableGetGatewayConnectionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">AwaitableGetGatewayConnectionResult</code><span class="sig-paren">(</span><em class="sig-param">authorization_key=None</em>, <em class="sig-param">connection_protocol=None</em>, <em class="sig-param">egress_bytes_transferred=None</em>, <em class="sig-param">enable_bgp=None</em>, <em class="sig-param">express_route_circuit_id=None</em>, <em class="sig-param">express_route_gateway_bypass=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ingress_bytes_transferred=None</em>, <em class="sig-param">ipsec_policies=None</em>, <em class="sig-param">local_network_gateway_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">peer_virtual_network_gateway_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">resource_guid=None</em>, <em class="sig-param">routing_weight=None</em>, <em class="sig-param">shared_key=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">use_policy_based_traffic_selectors=None</em>, <em class="sig-param">virtual_network_gateway_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.AwaitableGetGatewayConnectionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.AwaitableGetNatGatewayResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">AwaitableGetNatGatewayResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">idle_timeout_in_minutes=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">public_ip_address_ids=None</em>, <em class="sig-param">public_ip_prefix_ids=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">resource_guid=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.AwaitableGetNatGatewayResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.AwaitableGetNetworkDdosProtectionPlanResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">AwaitableGetNetworkDdosProtectionPlanResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_network_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.AwaitableGetNetworkDdosProtectionPlanResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.AwaitableGetNetworkInterfaceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">AwaitableGetNetworkInterfaceResult</code><span class="sig-paren">(</span><em class="sig-param">applied_dns_servers=None</em>, <em class="sig-param">dns_servers=None</em>, <em class="sig-param">enable_accelerated_networking=None</em>, <em class="sig-param">enable_ip_forwarding=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">internal_dns_name_label=None</em>, <em class="sig-param">ip_configurations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">mac_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_security_group_id=None</em>, <em class="sig-param">private_ip_address=None</em>, <em class="sig-param">private_ip_addresses=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_machine_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.AwaitableGetNetworkInterfaceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.AwaitableGetNetworkSecurityGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">AwaitableGetNetworkSecurityGroupResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">security_rules=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.AwaitableGetNetworkSecurityGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.AwaitableGetNetworkWatcherResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">AwaitableGetNetworkWatcherResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.AwaitableGetNetworkWatcherResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.AwaitableGetPublicIPResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">AwaitableGetPublicIPResult</code><span class="sig-paren">(</span><em class="sig-param">allocation_method=None</em>, <em class="sig-param">domain_name_label=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">idle_timeout_in_minutes=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">reverse_fqdn=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.AwaitableGetPublicIPResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.AwaitableGetPublicIPsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">AwaitableGetPublicIPsResult</code><span class="sig-paren">(</span><em class="sig-param">allocation_type=None</em>, <em class="sig-param">attached=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">public_ips=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.AwaitableGetPublicIPsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.AwaitableGetPublicIpPrefixResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">AwaitableGetPublicIpPrefixResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ip_prefix=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">prefix_length=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.AwaitableGetPublicIpPrefixResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.AwaitableGetRouteTableResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">AwaitableGetRouteTableResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">routes=None</em>, <em class="sig-param">subnets=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.AwaitableGetRouteTableResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.AwaitableGetSubnetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">AwaitableGetSubnetResult</code><span class="sig-paren">(</span><em class="sig-param">address_prefix=None</em>, <em class="sig-param">enforce_private_link_endpoint_network_policies=None</em>, <em class="sig-param">enforce_private_link_service_network_policies=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_security_group_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">route_table_id=None</em>, <em class="sig-param">service_endpoints=None</em>, <em class="sig-param">virtual_network_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.AwaitableGetSubnetResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.AwaitableGetTrafficManagerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">AwaitableGetTrafficManagerResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.AwaitableGetTrafficManagerResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.AwaitableGetVirtualHubResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">AwaitableGetVirtualHubResult</code><span class="sig-paren">(</span><em class="sig-param">address_prefix=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_wan_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.AwaitableGetVirtualHubResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.AwaitableGetVirtualNetworkGatewayResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">AwaitableGetVirtualNetworkGatewayResult</code><span class="sig-paren">(</span><em class="sig-param">active_active=None</em>, <em class="sig-param">bgp_settings=None</em>, <em class="sig-param">default_local_network_gateway_id=None</em>, <em class="sig-param">enable_bgp=None</em>, <em class="sig-param">generation=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ip_configurations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">vpn_client_configurations=None</em>, <em class="sig-param">vpn_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.AwaitableGetVirtualNetworkGatewayResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.AwaitableGetVirtualNetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">AwaitableGetVirtualNetworkResult</code><span class="sig-paren">(</span><em class="sig-param">address_spaces=None</em>, <em class="sig-param">dns_servers=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">subnets=None</em>, <em class="sig-param">vnet_peerings=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.AwaitableGetVirtualNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.DdosProtectionPlan">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">DdosProtectionPlan</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.DdosProtectionPlan" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AzureNetwork DDoS Protection Plan.</p>
<blockquote>
<div><p><strong>NOTE</strong> Azure only allows <code class="docutils literal notranslate"><span class="pre">one</span></code> DDoS Protection Plan per region.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_ddos_protection_plan.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_ddos_protection_plan.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Network DDoS Protection Plan. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.DdosProtectionPlan.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.DdosProtectionPlan.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.DdosProtectionPlan.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.DdosProtectionPlan.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Network DDoS Protection Plan. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.DdosProtectionPlan.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.DdosProtectionPlan.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.DdosProtectionPlan.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.DdosProtectionPlan.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.DdosProtectionPlan.virtual_network_ids">
<code class="sig-name descname">virtual_network_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.DdosProtectionPlan.virtual_network_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Virtual Network ID’s associated with the DDoS Protection Plan.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.DdosProtectionPlan.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_network_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.DdosProtectionPlan.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DdosProtectionPlan resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Network DDoS Protection Plan. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>virtual_network_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Virtual Network ID’s associated with the DDoS Protection Plan.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.DdosProtectionPlan.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.DdosProtectionPlan.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.DdosProtectionPlan.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.DdosProtectionPlan.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ExpressRouteCircuit">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">ExpressRouteCircuit</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_classic_operations=None</em>, <em class="sig-param">bandwidth_in_mbps=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">peering_location=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_provider_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an ExpressRoute circuit.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/express_route_circuit.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/express_route_circuit.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_classic_operations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow the circuit to interact with classic (RDFE) resources. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>bandwidth_in_mbps</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The bandwidth in Mbps of the circuit being created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ExpressRoute circuit. Changing this forces a new resource to be created.</p></li>
<li><p><strong>peering_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the peering location and <strong>not</strong> the Azure resource location.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the ExpressRoute circuit. Changing this forces a new resource to be created.</p></li>
<li><p><strong>service_provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ExpressRoute Service Provider.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block for the ExpressRoute circuit as documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">family</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The billing mode for bandwidth. Possible values are <code class="docutils literal notranslate"><span class="pre">MeteredData</span></code> or <code class="docutils literal notranslate"><span class="pre">UnlimitedData</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service tier. Possible values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Local</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.allow_classic_operations">
<code class="sig-name descname">allow_classic_operations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.allow_classic_operations" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow the circuit to interact with classic (RDFE) resources. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.bandwidth_in_mbps">
<code class="sig-name descname">bandwidth_in_mbps</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.bandwidth_in_mbps" title="Permalink to this definition">¶</a></dt>
<dd><p>The bandwidth in Mbps of the circuit being created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ExpressRoute circuit. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.peering_location">
<code class="sig-name descname">peering_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.peering_location" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the peering location and <strong>not</strong> the Azure resource location.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the ExpressRoute circuit. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.service_key">
<code class="sig-name descname">service_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.service_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The string needed by the service provider to provision the ExpressRoute circuit.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.service_provider_name">
<code class="sig-name descname">service_provider_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.service_provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ExpressRoute Service Provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.service_provider_provisioning_state">
<code class="sig-name descname">service_provider_provisioning_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.service_provider_provisioning_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The ExpressRoute circuit provisioning state from your chosen service provider. Possible values are “NotProvisioned”, “Provisioning”, “Provisioned”, and “Deprovisioning”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block for the ExpressRoute circuit as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">family</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The billing mode for bandwidth. Possible values are <code class="docutils literal notranslate"><span class="pre">MeteredData</span></code> or <code class="docutils literal notranslate"><span class="pre">UnlimitedData</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The service tier. Possible values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Local</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuit.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.ExpressRouteCircuit.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_classic_operations=None</em>, <em class="sig-param">bandwidth_in_mbps=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">peering_location=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_key=None</em>, <em class="sig-param">service_provider_name=None</em>, <em class="sig-param">service_provider_provisioning_state=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ExpressRouteCircuit resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_classic_operations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow the circuit to interact with classic (RDFE) resources. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>bandwidth_in_mbps</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The bandwidth in Mbps of the circuit being created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ExpressRoute circuit. Changing this forces a new resource to be created.</p></li>
<li><p><strong>peering_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the peering location and <strong>not</strong> the Azure resource location.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the ExpressRoute circuit. Changing this forces a new resource to be created.</p></li>
<li><p><strong>service_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The string needed by the service provider to provision the ExpressRoute circuit.</p></li>
<li><p><strong>service_provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ExpressRoute Service Provider.</p></li>
<li><p><strong>service_provider_provisioning_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ExpressRoute circuit provisioning state from your chosen service provider. Possible values are “NotProvisioned”, “Provisioning”, “Provisioned”, and “Deprovisioning”.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block for the ExpressRoute circuit as documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">family</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The billing mode for bandwidth. Possible values are <code class="docutils literal notranslate"><span class="pre">MeteredData</span></code> or <code class="docutils literal notranslate"><span class="pre">UnlimitedData</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service tier. Possible values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Local</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.ExpressRouteCircuit.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ExpressRouteCircuit.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuit.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ExpressRouteCircuitAuthorization">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">ExpressRouteCircuitAuthorization</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">express_route_circuit_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitAuthorization" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an ExpressRoute Circuit Authorization.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/express_route_circuit_authorization.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/express_route_circuit_authorization.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>express_route_circuit_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Express Route Circuit in which to create the Authorization.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ExpressRoute circuit. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the ExpressRoute circuit. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitAuthorization.authorization_key">
<code class="sig-name descname">authorization_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitAuthorization.authorization_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Authorization Key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitAuthorization.authorization_use_status">
<code class="sig-name descname">authorization_use_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitAuthorization.authorization_use_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The authorization use status.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitAuthorization.express_route_circuit_name">
<code class="sig-name descname">express_route_circuit_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitAuthorization.express_route_circuit_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Express Route Circuit in which to create the Authorization.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitAuthorization.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitAuthorization.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ExpressRoute circuit. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitAuthorization.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitAuthorization.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the ExpressRoute circuit. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.ExpressRouteCircuitAuthorization.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">authorization_key=None</em>, <em class="sig-param">authorization_use_status=None</em>, <em class="sig-param">express_route_circuit_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitAuthorization.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ExpressRouteCircuitAuthorization resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorization_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Authorization Key.</p></li>
<li><p><strong>authorization_use_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authorization use status.</p></li>
<li><p><strong>express_route_circuit_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Express Route Circuit in which to create the Authorization.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ExpressRoute circuit. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the ExpressRoute circuit. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.ExpressRouteCircuitAuthorization.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitAuthorization.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ExpressRouteCircuitAuthorization.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitAuthorization.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">ExpressRouteCircuitPeering</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">express_route_circuit_name=None</em>, <em class="sig-param">microsoft_peering_config=None</em>, <em class="sig-param">peer_asn=None</em>, <em class="sig-param">peering_type=None</em>, <em class="sig-param">primary_peer_address_prefix=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_peer_address_prefix=None</em>, <em class="sig-param">shared_key=None</em>, <em class="sig-param">vlan_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an ExpressRoute Circuit Peering.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/express_route_circuit_peering.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/express_route_circuit_peering.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>express_route_circuit_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ExpressRoute Circuit in which to create the Peering.</p></li>
<li><p><strong>microsoft_peering_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">microsoft_peering_config</span></code> block as defined below. Required when <code class="docutils literal notranslate"><span class="pre">peering_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">MicrosoftPeering</span></code>.</p></li>
<li><p><strong>peer_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Either a 16-bit or a 32-bit ASN. Can either be public or private..</p></li>
<li><p><strong>peering_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the ExpressRoute Circuit Peering. Acceptable values include <code class="docutils literal notranslate"><span class="pre">AzurePrivatePeering</span></code>, <code class="docutils literal notranslate"><span class="pre">AzurePublicPeering</span></code> and <code class="docutils literal notranslate"><span class="pre">MicrosoftPeering</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>primary_peer_address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">/30</span></code> subnet for the primary link.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the Express Route Circuit Peering. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_peer_address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">/30</span></code> subnet for the secondary link.</p></li>
<li><p><strong>shared_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared key. Can be a maximum of 25 characters.</p></li>
<li><p><strong>vlan_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A valid VLAN ID to establish this peering on.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>microsoft_peering_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">advertisedPublicPrefixes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.azure_asn">
<code class="sig-name descname">azure_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.azure_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ASN used by Azure.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.express_route_circuit_name">
<code class="sig-name descname">express_route_circuit_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.express_route_circuit_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ExpressRoute Circuit in which to create the Peering.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.microsoft_peering_config">
<code class="sig-name descname">microsoft_peering_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.microsoft_peering_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">microsoft_peering_config</span></code> block as defined below. Required when <code class="docutils literal notranslate"><span class="pre">peering_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">MicrosoftPeering</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">advertisedPublicPrefixes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.peer_asn">
<code class="sig-name descname">peer_asn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.peer_asn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Either a 16-bit or a 32-bit ASN. Can either be public or private..</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.peering_type">
<code class="sig-name descname">peering_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.peering_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the ExpressRoute Circuit Peering. Acceptable values include <code class="docutils literal notranslate"><span class="pre">AzurePrivatePeering</span></code>, <code class="docutils literal notranslate"><span class="pre">AzurePublicPeering</span></code> and <code class="docutils literal notranslate"><span class="pre">MicrosoftPeering</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.primary_azure_port">
<code class="sig-name descname">primary_azure_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.primary_azure_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Port used by Azure for this Peering.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.primary_peer_address_prefix">
<code class="sig-name descname">primary_peer_address_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.primary_peer_address_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">/30</span></code> subnet for the primary link.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the Express Route Circuit Peering. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.secondary_azure_port">
<code class="sig-name descname">secondary_azure_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.secondary_azure_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The Secondary Port used by Azure for this Peering.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.secondary_peer_address_prefix">
<code class="sig-name descname">secondary_peer_address_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.secondary_peer_address_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">/30</span></code> subnet for the secondary link.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.shared_key">
<code class="sig-name descname">shared_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.shared_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared key. Can be a maximum of 25 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.vlan_id">
<code class="sig-name descname">vlan_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.vlan_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A valid VLAN ID to establish this peering on.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">azure_asn=None</em>, <em class="sig-param">express_route_circuit_name=None</em>, <em class="sig-param">microsoft_peering_config=None</em>, <em class="sig-param">peer_asn=None</em>, <em class="sig-param">peering_type=None</em>, <em class="sig-param">primary_azure_port=None</em>, <em class="sig-param">primary_peer_address_prefix=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_azure_port=None</em>, <em class="sig-param">secondary_peer_address_prefix=None</em>, <em class="sig-param">shared_key=None</em>, <em class="sig-param">vlan_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ExpressRouteCircuitPeering resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>azure_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ASN used by Azure.</p></li>
<li><p><strong>express_route_circuit_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ExpressRoute Circuit in which to create the Peering.</p></li>
<li><p><strong>microsoft_peering_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">microsoft_peering_config</span></code> block as defined below. Required when <code class="docutils literal notranslate"><span class="pre">peering_type</span></code> is set to <code class="docutils literal notranslate"><span class="pre">MicrosoftPeering</span></code>.</p></li>
<li><p><strong>peer_asn</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Either a 16-bit or a 32-bit ASN. Can either be public or private..</p></li>
<li><p><strong>peering_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the ExpressRoute Circuit Peering. Acceptable values include <code class="docutils literal notranslate"><span class="pre">AzurePrivatePeering</span></code>, <code class="docutils literal notranslate"><span class="pre">AzurePublicPeering</span></code> and <code class="docutils literal notranslate"><span class="pre">MicrosoftPeering</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>primary_azure_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Port used by Azure for this Peering.</p></li>
<li><p><strong>primary_peer_address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">/30</span></code> subnet for the primary link.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the Express Route Circuit Peering. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_azure_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Secondary Port used by Azure for this Peering.</p></li>
<li><p><strong>secondary_peer_address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">/30</span></code> subnet for the secondary link.</p></li>
<li><p><strong>shared_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared key. Can be a maximum of 25 characters.</p></li>
<li><p><strong>vlan_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – A valid VLAN ID to establish this peering on.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>microsoft_peering_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">advertisedPublicPrefixes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ExpressRouteCircuitPeering.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteCircuitPeering.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ExpressRouteGateway">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">ExpressRouteGateway</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">scale_units=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_hub_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an ExpressRoute gateway.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/express_route_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/express_route_gateway.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ExpressRoute gateway. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the ExpressRoute gateway. Changing this forces a new resource to be created.</p></li>
<li><p><strong>scale_units</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of scale units with which to provision the ExpressRoute gateway. Each scale unit is equal to 2Gbps, with support for up to 10 scale units (20Gbps).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>virtual_hub_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Virtual HUB within which the ExpressRoute gateway should be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteGateway.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteGateway.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteGateway.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteGateway.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the ExpressRoute gateway. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteGateway.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteGateway.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the ExpressRoute gateway. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteGateway.scale_units">
<code class="sig-name descname">scale_units</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteGateway.scale_units" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of scale units with which to provision the ExpressRoute gateway. Each scale unit is equal to 2Gbps, with support for up to 10 scale units (20Gbps).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteGateway.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteGateway.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.ExpressRouteGateway.virtual_hub_id">
<code class="sig-name descname">virtual_hub_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.ExpressRouteGateway.virtual_hub_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a Virtual HUB within which the ExpressRoute gateway should be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.ExpressRouteGateway.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">scale_units=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_hub_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteGateway.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ExpressRouteGateway resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the ExpressRoute gateway. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the ExpressRoute gateway. Changing this forces a new resource to be created.</p></li>
<li><p><strong>scale_units</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of scale units with which to provision the ExpressRoute gateway. Each scale unit is equal to 2Gbps, with support for up to 10 scale units (20Gbps).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>virtual_hub_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Virtual HUB within which the ExpressRoute gateway should be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.ExpressRouteGateway.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.ExpressRouteGateway.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.ExpressRouteGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.Firewall">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">Firewall</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ip_configurations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Firewall" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Firewall.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/firewall.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/firewall.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> block as documented below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the availability zones in which the Azure Firewall should be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ip_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The private IP address of the Azure Firewall.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.Firewall.ip_configurations">
<code class="sig-name descname">ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Firewall.ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The private IP address of the Azure Firewall.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Firewall.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Firewall.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Firewall.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Firewall.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Firewall. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Firewall.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Firewall.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Firewall.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Firewall.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Firewall.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Firewall.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the availability zones in which the Azure Firewall should be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.Firewall.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ip_configurations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Firewall.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Firewall resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> block as documented below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the availability zones in which the Azure Firewall should be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ip_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The private IP address of the Azure Firewall.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.Firewall.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Firewall.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.Firewall.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Firewall.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">FirewallApplicationRuleCollection</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">azure_firewall_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">rules=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Application Rule Collection within an Azure Firewall.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/firewall_application_rule_collection.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/firewall_application_rule_collection.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the action the rule will apply to matching traffic. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p></li>
<li><p><strong>azure_firewall_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Firewall in which the Application Rule Collection should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Application Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the priority of the rule collection. Possible values are between <code class="docutils literal notranslate"><span class="pre">100</span></code> - <code class="docutils literal notranslate"><span class="pre">65000</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">rule</span></code> blocks as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fqdnTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Application Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocols</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetFqdns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection.action">
<code class="sig-name descname">action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection.action" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the action the rule will apply to matching traffic. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection.azure_firewall_name">
<code class="sig-name descname">azure_firewall_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection.azure_firewall_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Firewall in which the Application Rule Collection should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Application Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the priority of the rule collection. Possible values are between <code class="docutils literal notranslate"><span class="pre">100</span></code> - <code class="docutils literal notranslate"><span class="pre">65000</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection.rules">
<code class="sig-name descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">rule</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fqdnTags</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Application Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocols</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetFqdns</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">azure_firewall_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">rules=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FirewallApplicationRuleCollection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the action the rule will apply to matching traffic. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p></li>
<li><p><strong>azure_firewall_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Firewall in which the Application Rule Collection should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Application Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the priority of the rule collection. Possible values are between <code class="docutils literal notranslate"><span class="pre">100</span></code> - <code class="docutils literal notranslate"><span class="pre">65000</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">rule</span></code> blocks as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fqdnTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Application Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocols</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetFqdns</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.FirewallApplicationRuleCollection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.FirewallApplicationRuleCollection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.FirewallNatRuleCollection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">FirewallNatRuleCollection</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">azure_firewall_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">rules=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.FirewallNatRuleCollection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a NAT Rule Collection within an Azure Firewall.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/firewall_nat_rule_collection.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/firewall_nat_rule_collection.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the action the rule will apply to matching traffic. Possible values are <code class="docutils literal notranslate"><span class="pre">Dnat</span></code> and <code class="docutils literal notranslate"><span class="pre">Snat</span></code>.</p></li>
<li><p><strong>azure_firewall_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Firewall in which the NAT Rule Collection should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the NAT Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the priority of the rule collection. Possible values are between <code class="docutils literal notranslate"><span class="pre">100</span></code> - <code class="docutils literal notranslate"><span class="pre">65000</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">rule</span></code> blocks as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the NAT Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocols</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">translatedAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">translatedPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.FirewallNatRuleCollection.action">
<code class="sig-name descname">action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallNatRuleCollection.action" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the action the rule will apply to matching traffic. Possible values are <code class="docutils literal notranslate"><span class="pre">Dnat</span></code> and <code class="docutils literal notranslate"><span class="pre">Snat</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallNatRuleCollection.azure_firewall_name">
<code class="sig-name descname">azure_firewall_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallNatRuleCollection.azure_firewall_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Firewall in which the NAT Rule Collection should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallNatRuleCollection.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallNatRuleCollection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the NAT Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallNatRuleCollection.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallNatRuleCollection.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the priority of the rule collection. Possible values are between <code class="docutils literal notranslate"><span class="pre">100</span></code> - <code class="docutils literal notranslate"><span class="pre">65000</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallNatRuleCollection.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallNatRuleCollection.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallNatRuleCollection.rules">
<code class="sig-name descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallNatRuleCollection.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">rule</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the NAT Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocols</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">translatedAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">translatedPort</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.FirewallNatRuleCollection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">azure_firewall_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">rules=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.FirewallNatRuleCollection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FirewallNatRuleCollection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the action the rule will apply to matching traffic. Possible values are <code class="docutils literal notranslate"><span class="pre">Dnat</span></code> and <code class="docutils literal notranslate"><span class="pre">Snat</span></code>.</p></li>
<li><p><strong>azure_firewall_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Firewall in which the NAT Rule Collection should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the NAT Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the priority of the rule collection. Possible values are between <code class="docutils literal notranslate"><span class="pre">100</span></code> - <code class="docutils literal notranslate"><span class="pre">65000</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">rule</span></code> blocks as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the NAT Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocols</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">translatedAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">translatedPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.FirewallNatRuleCollection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.FirewallNatRuleCollection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.FirewallNatRuleCollection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.FirewallNatRuleCollection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">FirewallNetworkRuleCollection</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">azure_firewall_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">rules=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Network Rule Collection within an Azure Firewall.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/firewall_network_rule_collection.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/firewall_network_rule_collection.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the action the rule will apply to matching traffic. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p></li>
<li><p><strong>azure_firewall_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Firewall in which the Network Rule Collection should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Network Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the priority of the rule collection. Possible values are between <code class="docutils literal notranslate"><span class="pre">100</span></code> - <code class="docutils literal notranslate"><span class="pre">65000</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">rule</span></code> blocks as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Network Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocols</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection.action">
<code class="sig-name descname">action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection.action" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the action the rule will apply to matching traffic. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection.azure_firewall_name">
<code class="sig-name descname">azure_firewall_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection.azure_firewall_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Firewall in which the Network Rule Collection should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Network Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the priority of the rule collection. Possible values are between <code class="docutils literal notranslate"><span class="pre">100</span></code> - <code class="docutils literal notranslate"><span class="pre">65000</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection.rules">
<code class="sig-name descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">rule</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Network Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocols</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">action=None</em>, <em class="sig-param">azure_firewall_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">rules=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FirewallNetworkRuleCollection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the action the rule will apply to matching traffic. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p></li>
<li><p><strong>azure_firewall_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Firewall in which the Network Rule Collection should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Network Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the priority of the rule collection. Possible values are between <code class="docutils literal notranslate"><span class="pre">100</span></code> - <code class="docutils literal notranslate"><span class="pre">65000</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which the Firewall exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">rule</span></code> blocks as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destinationPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Network Rule Collection which must be unique within the Firewall. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocols</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceAddresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.FirewallNetworkRuleCollection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.FirewallNetworkRuleCollection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.GetApplicationSecurityGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">GetApplicationSecurityGroupResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetApplicationSecurityGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getApplicationSecurityGroup.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetApplicationSecurityGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetApplicationSecurityGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetApplicationSecurityGroupResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetApplicationSecurityGroupResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The supported Azure location where the Application Security Group exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetApplicationSecurityGroupResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetApplicationSecurityGroupResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetExpressRouteCircuitResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">GetExpressRouteCircuitResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">peerings=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_key=None</em>, <em class="sig-param">service_provider_properties=None</em>, <em class="sig-param">service_provider_provisioning_state=None</em>, <em class="sig-param">sku=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetExpressRouteCircuitResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getExpressRouteCircuit.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetExpressRouteCircuitResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetExpressRouteCircuitResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetExpressRouteCircuitResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetExpressRouteCircuitResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the ExpressRoute circuit exists</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetExpressRouteCircuitResult.peerings">
<code class="sig-name descname">peerings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetExpressRouteCircuitResult.peerings" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">peerings</span></code> block for the ExpressRoute circuit as documented below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetExpressRouteCircuitResult.service_key">
<code class="sig-name descname">service_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetExpressRouteCircuitResult.service_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The string needed by the service provider to provision the ExpressRoute circuit.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetExpressRouteCircuitResult.service_provider_properties">
<code class="sig-name descname">service_provider_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetExpressRouteCircuitResult.service_provider_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">service_provider_properties</span></code> block for the ExpressRoute circuit as documented below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetExpressRouteCircuitResult.service_provider_provisioning_state">
<code class="sig-name descname">service_provider_provisioning_state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetExpressRouteCircuitResult.service_provider_provisioning_state" title="Permalink to this definition">¶</a></dt>
<dd><p>The ExpressRoute circuit provisioning state from your chosen service provider. Possible values are “NotProvisioned”, “Provisioning”, “Provisioned”, and “Deprovisioning”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetExpressRouteCircuitResult.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetExpressRouteCircuitResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block for the ExpressRoute circuit as documented below.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetFirewallResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">GetFirewallResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ip_configurations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetFirewallResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFirewall.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetFirewallResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetFirewallResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetFirewallResult.ip_configurations">
<code class="sig-name descname">ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetFirewallResult.ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> block as defined below.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetGatewayConnectionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">GetGatewayConnectionResult</code><span class="sig-paren">(</span><em class="sig-param">authorization_key=None</em>, <em class="sig-param">connection_protocol=None</em>, <em class="sig-param">egress_bytes_transferred=None</em>, <em class="sig-param">enable_bgp=None</em>, <em class="sig-param">express_route_circuit_id=None</em>, <em class="sig-param">express_route_gateway_bypass=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ingress_bytes_transferred=None</em>, <em class="sig-param">ipsec_policies=None</em>, <em class="sig-param">local_network_gateway_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">peer_virtual_network_gateway_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">resource_guid=None</em>, <em class="sig-param">routing_weight=None</em>, <em class="sig-param">shared_key=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">use_policy_based_traffic_selectors=None</em>, <em class="sig-param">virtual_network_gateway_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetGatewayConnectionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGatewayConnection.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetGatewayConnectionResult.authorization_key">
<code class="sig-name descname">authorization_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetGatewayConnectionResult.authorization_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The authorization key associated with the
Express Route Circuit. This field is present only if the type is an
ExpressRoute connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetGatewayConnectionResult.enable_bgp">
<code class="sig-name descname">enable_bgp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetGatewayConnectionResult.enable_bgp" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, BGP (Border Gateway Protocol) is enabled
for this connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetGatewayConnectionResult.express_route_circuit_id">
<code class="sig-name descname">express_route_circuit_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetGatewayConnectionResult.express_route_circuit_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Express Route Circuit
(i.e. when <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">ExpressRoute</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetGatewayConnectionResult.express_route_gateway_bypass">
<code class="sig-name descname">express_route_gateway_bypass</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetGatewayConnectionResult.express_route_gateway_bypass" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, data packets will bypass ExpressRoute Gateway for data forwarding. This is only valid for ExpressRoute connections.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetGatewayConnectionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetGatewayConnectionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetGatewayConnectionResult.local_network_gateway_id">
<code class="sig-name descname">local_network_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetGatewayConnectionResult.local_network_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the local network gateway
when a Site-to-Site connection (i.e. when <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">IPsec</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetGatewayConnectionResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetGatewayConnectionResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location/region where the connection is
located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetGatewayConnectionResult.peer_virtual_network_gateway_id">
<code class="sig-name descname">peer_virtual_network_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetGatewayConnectionResult.peer_virtual_network_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the peer virtual
network gateway when a VNet-to-VNet connection (i.e. when <code class="docutils literal notranslate"><span class="pre">type</span></code>
is <code class="docutils literal notranslate"><span class="pre">Vnet2Vnet</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetGatewayConnectionResult.routing_weight">
<code class="sig-name descname">routing_weight</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetGatewayConnectionResult.routing_weight" title="Permalink to this definition">¶</a></dt>
<dd><p>The routing weight.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetGatewayConnectionResult.shared_key">
<code class="sig-name descname">shared_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetGatewayConnectionResult.shared_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared IPSec key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetGatewayConnectionResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetGatewayConnectionResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetGatewayConnectionResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetGatewayConnectionResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of connection. Valid options are <code class="docutils literal notranslate"><span class="pre">IPsec</span></code>
(Site-to-Site), <code class="docutils literal notranslate"><span class="pre">ExpressRoute</span></code> (ExpressRoute), and <code class="docutils literal notranslate"><span class="pre">Vnet2Vnet</span></code> (VNet-to-VNet).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetGatewayConnectionResult.use_policy_based_traffic_selectors">
<code class="sig-name descname">use_policy_based_traffic_selectors</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetGatewayConnectionResult.use_policy_based_traffic_selectors" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an <code class="docutils literal notranslate"><span class="pre">ipsec_policy</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetGatewayConnectionResult.virtual_network_gateway_id">
<code class="sig-name descname">virtual_network_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetGatewayConnectionResult.virtual_network_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Virtual Network Gateway
in which the connection is created.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetNatGatewayResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">GetNatGatewayResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">idle_timeout_in_minutes=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">public_ip_address_ids=None</em>, <em class="sig-param">public_ip_prefix_ids=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">resource_guid=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetNatGatewayResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNatGateway.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetNatGatewayResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNatGatewayResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNatGatewayResult.idle_timeout_in_minutes">
<code class="sig-name descname">idle_timeout_in_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNatGatewayResult.idle_timeout_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>The idle timeout in minutes which is used for the NAT Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNatGatewayResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNatGatewayResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the NAT Gateway exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNatGatewayResult.public_ip_address_ids">
<code class="sig-name descname">public_ip_address_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNatGatewayResult.public_ip_address_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of existing Public IP Address resource IDs which the NAT Gateway is using.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNatGatewayResult.public_ip_prefix_ids">
<code class="sig-name descname">public_ip_prefix_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNatGatewayResult.public_ip_prefix_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of existing Public IP Prefix resource IDs which the NAT Gateway is using.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNatGatewayResult.resource_guid">
<code class="sig-name descname">resource_guid</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNatGatewayResult.resource_guid" title="Permalink to this definition">¶</a></dt>
<dd><p>The Resource GUID of the NAT Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNatGatewayResult.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNatGatewayResult.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU used by the NAT Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNatGatewayResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNatGatewayResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNatGatewayResult.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNatGatewayResult.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Availability Zones which the NAT Gateway exists in.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetNetworkDdosProtectionPlanResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">GetNetworkDdosProtectionPlanResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_network_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetNetworkDdosProtectionPlanResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkDdosProtectionPlan.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkDdosProtectionPlanResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkDdosProtectionPlanResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkDdosProtectionPlanResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkDdosProtectionPlanResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkDdosProtectionPlanResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkDdosProtectionPlanResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkDdosProtectionPlanResult.virtual_network_ids">
<code class="sig-name descname">virtual_network_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkDdosProtectionPlanResult.virtual_network_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The Resource ID list of the Virtual Networks associated with DDoS Protection Plan.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">GetNetworkInterfaceResult</code><span class="sig-paren">(</span><em class="sig-param">applied_dns_servers=None</em>, <em class="sig-param">dns_servers=None</em>, <em class="sig-param">enable_accelerated_networking=None</em>, <em class="sig-param">enable_ip_forwarding=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">internal_dns_name_label=None</em>, <em class="sig-param">ip_configurations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">mac_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_security_group_id=None</em>, <em class="sig-param">private_ip_address=None</em>, <em class="sig-param">private_ip_addresses=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_machine_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkInterface.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.applied_dns_servers">
<code class="sig-name descname">applied_dns_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.applied_dns_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of DNS servers applied to the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.dns_servers">
<code class="sig-name descname">dns_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.dns_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of DNS servers used by the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.enable_accelerated_networking">
<code class="sig-name descname">enable_accelerated_networking</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.enable_accelerated_networking" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates if accelerated networking is set on the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.enable_ip_forwarding">
<code class="sig-name descname">enable_ip_forwarding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.enable_ip_forwarding" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicate if IP forwarding is set on the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.internal_dns_name_label">
<code class="sig-name descname">internal_dns_name_label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.internal_dns_name_label" title="Permalink to this definition">¶</a></dt>
<dd><p>The internal dns name label of the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.ip_configurations">
<code class="sig-name descname">ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.mac_address">
<code class="sig-name descname">mac_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.mac_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The MAC address used by the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the IP Configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.network_security_group_id">
<code class="sig-name descname">network_security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.network_security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the network security group associated to the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.private_ip_address">
<code class="sig-name descname">private_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.private_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Private IP Address assigned to this Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.private_ip_addresses">
<code class="sig-name descname">private_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.private_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of private ip addresses associates to the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>List the tags associated to the specified Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkInterfaceResult.virtual_machine_id">
<code class="sig-name descname">virtual_machine_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkInterfaceResult.virtual_machine_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the virtual machine that the specified Network Interface is attached to.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetNetworkSecurityGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">GetNetworkSecurityGroupResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">security_rules=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetNetworkSecurityGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkSecurityGroup.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkSecurityGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkSecurityGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkSecurityGroupResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkSecurityGroupResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The supported Azure location where the resource exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkSecurityGroupResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkSecurityGroupResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the security rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkSecurityGroupResult.security_rules">
<code class="sig-name descname">security_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkSecurityGroupResult.security_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">security_rule</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkSecurityGroupResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkSecurityGroupResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetNetworkWatcherResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">GetNetworkWatcherResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetNetworkWatcherResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkWatcher.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkWatcherResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkWatcherResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkWatcherResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkWatcherResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The supported Azure location where the resource exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetNetworkWatcherResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetNetworkWatcherResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetPublicIPResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">GetPublicIPResult</code><span class="sig-paren">(</span><em class="sig-param">allocation_method=None</em>, <em class="sig-param">domain_name_label=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">idle_timeout_in_minutes=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">reverse_fqdn=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetPublicIPResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPublicIP.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIPResult.domain_name_label">
<code class="sig-name descname">domain_name_label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIPResult.domain_name_label" title="Permalink to this definition">¶</a></dt>
<dd><p>The label for the Domain Name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIPResult.fqdn">
<code class="sig-name descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIPResult.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>Fully qualified domain name of the A DNS record associated with the public IP. This is the concatenation of the domainNameLabel and the regionalized DNS zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIPResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIPResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIPResult.idle_timeout_in_minutes">
<code class="sig-name descname">idle_timeout_in_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIPResult.idle_timeout_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the timeout for the TCP idle connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIPResult.ip_address">
<code class="sig-name descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIPResult.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address value that was allocated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIPResult.ip_version">
<code class="sig-name descname">ip_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIPResult.ip_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP version being used, for example <code class="docutils literal notranslate"><span class="pre">IPv4</span></code> or <code class="docutils literal notranslate"><span class="pre">IPv6</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIPResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIPResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assigned to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetPublicIPsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">GetPublicIPsResult</code><span class="sig-paren">(</span><em class="sig-param">allocation_type=None</em>, <em class="sig-param">attached=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">public_ips=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetPublicIPsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPublicIPs.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIPsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIPsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIPsResult.public_ips">
<code class="sig-name descname">public_ips</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIPsResult.public_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>A List of <code class="docutils literal notranslate"><span class="pre">public_ips</span></code> blocks as defined below filtered by the criteria above.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetPublicIpPrefixResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">GetPublicIpPrefixResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ip_prefix=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">prefix_length=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetPublicIpPrefixResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPublicIpPrefix.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIpPrefixResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIpPrefixResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIpPrefixResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIpPrefixResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The supported Azure location where the resource exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIpPrefixResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIpPrefixResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Public IP prefix resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIpPrefixResult.prefix_length">
<code class="sig-name descname">prefix_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIpPrefixResult.prefix_length" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of bits of the prefix.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIpPrefixResult.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIpPrefixResult.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the public IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIpPrefixResult.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIpPrefixResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU of the Public IP Prefix.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetPublicIpPrefixResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetPublicIpPrefixResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assigned to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetRouteTableResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">GetRouteTableResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">routes=None</em>, <em class="sig-param">subnets=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetRouteTableResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRouteTable.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetRouteTableResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetRouteTableResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetRouteTableResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetRouteTableResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which the Route Table exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetRouteTableResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetRouteTableResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Route.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetRouteTableResult.routes">
<code class="sig-name descname">routes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetRouteTableResult.routes" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">route</span></code> blocks as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetRouteTableResult.subnets">
<code class="sig-name descname">subnets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetRouteTableResult.subnets" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of Subnets associated with this route table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetRouteTableResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetRouteTableResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the Route Table.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetSubnetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">GetSubnetResult</code><span class="sig-paren">(</span><em class="sig-param">address_prefix=None</em>, <em class="sig-param">enforce_private_link_endpoint_network_policies=None</em>, <em class="sig-param">enforce_private_link_service_network_policies=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_security_group_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">route_table_id=None</em>, <em class="sig-param">service_endpoints=None</em>, <em class="sig-param">virtual_network_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetSubnetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSubnet.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetSubnetResult.address_prefix">
<code class="sig-name descname">address_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetSubnetResult.address_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The address prefix used for the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetSubnetResult.enforce_private_link_endpoint_network_policies">
<code class="sig-name descname">enforce_private_link_endpoint_network_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetSubnetResult.enforce_private_link_endpoint_network_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or Disable network policies for the private link endpoint on the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetSubnetResult.enforce_private_link_service_network_policies">
<code class="sig-name descname">enforce_private_link_service_network_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetSubnetResult.enforce_private_link_service_network_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or Disable network policies for the private link service on the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetSubnetResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetSubnetResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetSubnetResult.network_security_group_id">
<code class="sig-name descname">network_security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetSubnetResult.network_security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Security Group associated with the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetSubnetResult.route_table_id">
<code class="sig-name descname">route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetSubnetResult.route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Route Table associated with this subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetSubnetResult.service_endpoints">
<code class="sig-name descname">service_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetSubnetResult.service_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Service Endpoints within this subnet.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetTrafficManagerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">GetTrafficManagerResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetTrafficManagerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTrafficManager.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetTrafficManagerResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetTrafficManagerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetVirtualHubResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">GetVirtualHubResult</code><span class="sig-paren">(</span><em class="sig-param">address_prefix=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_wan_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetVirtualHubResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVirtualHub.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualHubResult.address_prefix">
<code class="sig-name descname">address_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualHubResult.address_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The Address Prefix used for this Virtual Hub.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualHubResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualHubResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualHubResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualHubResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region where the Virtual Hub exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualHubResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualHubResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the Virtual Hub.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualHubResult.virtual_wan_id">
<code class="sig-name descname">virtual_wan_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualHubResult.virtual_wan_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Virtual WAN within which the Virtual Hub exists.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">GetVirtualNetworkGatewayResult</code><span class="sig-paren">(</span><em class="sig-param">active_active=None</em>, <em class="sig-param">bgp_settings=None</em>, <em class="sig-param">default_local_network_gateway_id=None</em>, <em class="sig-param">enable_bgp=None</em>, <em class="sig-param">generation=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ip_configurations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">vpn_client_configurations=None</em>, <em class="sig-param">vpn_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVirtualNetworkGateway.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.active_active">
<code class="sig-name descname">active_active</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.active_active" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this an Active-Active Gateway?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.default_local_network_gateway_id">
<code class="sig-name descname">default_local_network_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.default_local_network_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (<em>forced tunneling</em>). Refer to the
<a class="reference external" href="https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm">Azure documentation on forced tunneling</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.enable_bgp">
<code class="sig-name descname">enable_bgp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.enable_bgp" title="Permalink to this definition">¶</a></dt>
<dd><p>Will BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.generation">
<code class="sig-name descname">generation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.generation" title="Permalink to this definition">¶</a></dt>
<dd><p>The Generation of the Virtual Network Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.ip_configurations">
<code class="sig-name descname">ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or two <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> blocks documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location/region where the Virtual Network Gateway is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The user-defined name of the revoked certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration of the size and capacity of the Virtual Network Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the Virtual Network Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.vpn_client_configurations">
<code class="sig-name descname">vpn_client_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.vpn_client_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">vpn_client_configuration</span></code> block which is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkGatewayResult.vpn_type">
<code class="sig-name descname">vpn_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkGatewayResult.vpn_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The routing type of the Virtual Network Gateway.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.GetVirtualNetworkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">GetVirtualNetworkResult</code><span class="sig-paren">(</span><em class="sig-param">address_spaces=None</em>, <em class="sig-param">dns_servers=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">subnets=None</em>, <em class="sig-param">vnet_peerings=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVirtualNetwork.</p>
<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkResult.address_spaces">
<code class="sig-name descname">address_spaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkResult.address_spaces" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of address spaces used by the virtual network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkResult.dns_servers">
<code class="sig-name descname">dns_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkResult.dns_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of DNS servers used by the virtual network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Location of the virtual network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkResult.subnets">
<code class="sig-name descname">subnets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkResult.subnets" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of name of the subnets that are attached to this virtual network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.GetVirtualNetworkResult.vnet_peerings">
<code class="sig-name descname">vnet_peerings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.GetVirtualNetworkResult.vnet_peerings" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of name - virtual network id of the virtual network peerings.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.network.LocalNetworkGateway">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">LocalNetworkGateway</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address_spaces=None</em>, <em class="sig-param">bgp_settings=None</em>, <em class="sig-param">gateway_address=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a local network gateway connection over which specific connections can be configured.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/local_network_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/local_network_gateway.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_spaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of string CIDRs representing the
address spaces the gateway exposes.</p></li>
<li><p><strong>bgp_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">bgp_settings</span></code> block as defined below containing the
Local Network Gateway’s BGP speaker settings.</p></li>
<li><p><strong>gateway_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the gateway to which to
connect.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location/region where the local network gateway is
created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the local network gateway. Changing this
forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the local network gateway.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bgp_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">asn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The BGP speaker’s ASN.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bgpPeeringAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The BGP peering address and BGP identifier
of this BGP speaker.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">peerWeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The weight added to routes learned from this
BGP speaker.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.LocalNetworkGateway.address_spaces">
<code class="sig-name descname">address_spaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.address_spaces" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of string CIDRs representing the
address spaces the gateway exposes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.LocalNetworkGateway.bgp_settings">
<code class="sig-name descname">bgp_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.bgp_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">bgp_settings</span></code> block as defined below containing the
Local Network Gateway’s BGP speaker settings.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">asn</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The BGP speaker’s ASN.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bgpPeeringAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The BGP peering address and BGP identifier
of this BGP speaker.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">peerWeight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The weight added to routes learned from this
BGP speaker.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.LocalNetworkGateway.gateway_address">
<code class="sig-name descname">gateway_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.gateway_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of the gateway to which to
connect.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.LocalNetworkGateway.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location/region where the local network gateway is
created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.LocalNetworkGateway.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the local network gateway. Changing this
forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.LocalNetworkGateway.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the local network gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.LocalNetworkGateway.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.LocalNetworkGateway.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address_spaces=None</em>, <em class="sig-param">bgp_settings=None</em>, <em class="sig-param">gateway_address=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LocalNetworkGateway resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_spaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of string CIDRs representing the
address spaces the gateway exposes.</p></li>
<li><p><strong>bgp_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">bgp_settings</span></code> block as defined below containing the
Local Network Gateway’s BGP speaker settings.</p></li>
<li><p><strong>gateway_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the gateway to which to
connect.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location/region where the local network gateway is
created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the local network gateway. Changing this
forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the local network gateway.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bgp_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">asn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The BGP speaker’s ASN.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bgpPeeringAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The BGP peering address and BGP identifier
of this BGP speaker.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">peerWeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The weight added to routes learned from this
BGP speaker.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.LocalNetworkGateway.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.LocalNetworkGateway.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.LocalNetworkGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NatGateway">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">NatGateway</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">idle_timeout_in_minutes=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">public_ip_address_ids=None</em>, <em class="sig-param">public_ip_prefix_ids=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NatGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Azure NAT Gateway.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The Azure NAT Gateway service is currently in private preview. Your subscription must be on the NAT Gateway private preview whitelist for this resource to be provisioned correctly. If you attempt to provision this resource and receive an <code class="docutils literal notranslate"><span class="pre">InvalidResourceType</span></code> error may mean that your subscription is not part of the NAT Gateway private preview or you are using a region which does not yet support the NAT Gateway private preview service. The NAT Gateway private preview service is currently available in a limited set of regions. Private preview resources may have multiple breaking changes over their lifecycle until they GA. You can opt into the Private Preview by contacting your Microsoft Representative.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/nat_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/nat_gateway.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>idle_timeout_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The idle timeout which should be used in minutes. Defaults to <code class="docutils literal notranslate"><span class="pre">4</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the NAT Gateway should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the NAT Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><strong>public_ip_address_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Public IP Address ID’s which should be associated with the NAT Gateway resource.</p></li>
<li><p><strong>public_ip_prefix_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Public IP Prefix ID’s which should be associated with the NAT Gateway resource.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which the NAT Gateway should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU which should be used. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of availability zones where the NAT Gateway should be provisioned. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.NatGateway.idle_timeout_in_minutes">
<code class="sig-name descname">idle_timeout_in_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NatGateway.idle_timeout_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>The idle timeout which should be used in minutes. Defaults to <code class="docutils literal notranslate"><span class="pre">4</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NatGateway.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NatGateway.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the NAT Gateway should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NatGateway.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NatGateway.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the NAT Gateway. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NatGateway.public_ip_address_ids">
<code class="sig-name descname">public_ip_address_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NatGateway.public_ip_address_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Public IP Address ID’s which should be associated with the NAT Gateway resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NatGateway.public_ip_prefix_ids">
<code class="sig-name descname">public_ip_prefix_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NatGateway.public_ip_prefix_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Public IP Prefix ID’s which should be associated with the NAT Gateway resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NatGateway.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NatGateway.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which the NAT Gateway should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NatGateway.resource_guid">
<code class="sig-name descname">resource_guid</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NatGateway.resource_guid" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource GUID property of the NAT Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NatGateway.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NatGateway.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU which should be used. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NatGateway.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NatGateway.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NatGateway.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NatGateway.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of availability zones where the NAT Gateway should be provisioned. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NatGateway.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">idle_timeout_in_minutes=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">public_ip_address_ids=None</em>, <em class="sig-param">public_ip_prefix_ids=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">resource_guid=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NatGateway.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NatGateway resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>idle_timeout_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The idle timeout which should be used in minutes. Defaults to <code class="docutils literal notranslate"><span class="pre">4</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the NAT Gateway should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the NAT Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><strong>public_ip_address_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Public IP Address ID’s which should be associated with the NAT Gateway resource.</p></li>
<li><p><strong>public_ip_prefix_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Public IP Prefix ID’s which should be associated with the NAT Gateway resource.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which the NAT Gateway should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_guid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource GUID property of the NAT Gateway.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU which should be used. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of availability zones where the NAT Gateway should be provisioned. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NatGateway.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NatGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NatGateway.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NatGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkConnectionMonitor">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">NetworkConnectionMonitor</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_start=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">interval_in_seconds=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_watcher_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkConnectionMonitor" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures a Network Connection Monitor to monitor communication between a Virtual Machine and an endpoint using a Network Watcher.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_connection_monitor.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_connection_monitor.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_start</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the connection monitor will start automatically once created. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">destination</span></code> block as defined below.</p></li>
<li><p><strong>interval_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Monitoring interval in seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">60</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Connection Monitor. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_watcher_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Watcher. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Connection Monitor. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">source</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>destination</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_machine_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>source</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_machine_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkConnectionMonitor.auto_start">
<code class="sig-name descname">auto_start</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkConnectionMonitor.auto_start" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the connection monitor will start automatically once created. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkConnectionMonitor.destination">
<code class="sig-name descname">destination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkConnectionMonitor.destination" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">destination</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_machine_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkConnectionMonitor.interval_in_seconds">
<code class="sig-name descname">interval_in_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkConnectionMonitor.interval_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>Monitoring interval in seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">60</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkConnectionMonitor.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkConnectionMonitor.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkConnectionMonitor.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkConnectionMonitor.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Network Connection Monitor. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkConnectionMonitor.network_watcher_name">
<code class="sig-name descname">network_watcher_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkConnectionMonitor.network_watcher_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Network Watcher. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkConnectionMonitor.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkConnectionMonitor.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Connection Monitor. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkConnectionMonitor.source">
<code class="sig-name descname">source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkConnectionMonitor.source" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">source</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_machine_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkConnectionMonitor.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkConnectionMonitor.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkConnectionMonitor.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_start=None</em>, <em class="sig-param">destination=None</em>, <em class="sig-param">interval_in_seconds=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_watcher_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkConnectionMonitor.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkConnectionMonitor resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_start</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the connection monitor will start automatically once created. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>destination</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">destination</span></code> block as defined below.</p></li>
<li><p><strong>interval_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Monitoring interval in seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">60</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Connection Monitor. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_watcher_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Watcher. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Connection Monitor. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">source</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>destination</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_machine_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>source</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtual_machine_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkConnectionMonitor.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkConnectionMonitor.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkConnectionMonitor.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkConnectionMonitor.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterface">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">NetworkInterface</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dns_servers=None</em>, <em class="sig-param">enable_accelerated_networking=None</em>, <em class="sig-param">enable_ip_forwarding=None</em>, <em class="sig-param">internal_dns_name_label=None</em>, <em class="sig-param">ip_configurations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterface" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Network Interface.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_interface.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_interface.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dns_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IP Addresses defining the DNS Servers which should be used for this Network Interface.</p></li>
<li><p><strong>enable_accelerated_networking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Accelerated Networking be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_ip_forwarding</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should IP Forwarding be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>internal_dns_name_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The (relative) DNS Name used for internal communications between Virtual Machines in the same Virtual Network.</p></li>
<li><p><strong>ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> blocks as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the Network Interface should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Interface. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which to create the Network Interface. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ip_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Network Interface. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The first private IP address of the network interface.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddressAllocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddressVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.applied_dns_servers">
<code class="sig-name descname">applied_dns_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.applied_dns_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>If the Virtual Machine using this Network Interface is part of an Availability Set, then this list will have the union of all DNS servers from all Network Interfaces that are part of the Availability Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.dns_servers">
<code class="sig-name descname">dns_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.dns_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IP Addresses defining the DNS Servers which should be used for this Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.enable_accelerated_networking">
<code class="sig-name descname">enable_accelerated_networking</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.enable_accelerated_networking" title="Permalink to this definition">¶</a></dt>
<dd><p>Should Accelerated Networking be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.enable_ip_forwarding">
<code class="sig-name descname">enable_ip_forwarding</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.enable_ip_forwarding" title="Permalink to this definition">¶</a></dt>
<dd><p>Should IP Forwarding be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.internal_dns_name_label">
<code class="sig-name descname">internal_dns_name_label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.internal_dns_name_label" title="Permalink to this definition">¶</a></dt>
<dd><p>The (relative) DNS Name used for internal communications between Virtual Machines in the same Virtual Network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.ip_configurations">
<code class="sig-name descname">ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Network Interface. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The first private IP address of the network interface.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddressAllocation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddressVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the Network Interface should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.mac_address">
<code class="sig-name descname">mac_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.mac_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Media Access Control (MAC) Address of the Network Interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Network Interface. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.private_ip_address">
<code class="sig-name descname">private_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.private_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The first private IP address of the network interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.private_ip_addresses">
<code class="sig-name descname">private_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.private_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The private IP addresses of the network interface.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which to create the Network Interface. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterface.virtual_machine_id">
<code class="sig-name descname">virtual_machine_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.virtual_machine_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Virtual Machine which this Network Interface is connected to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkInterface.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">applied_dns_servers=None</em>, <em class="sig-param">dns_servers=None</em>, <em class="sig-param">enable_accelerated_networking=None</em>, <em class="sig-param">enable_ip_forwarding=None</em>, <em class="sig-param">internal_dns_name_label=None</em>, <em class="sig-param">ip_configurations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">mac_address=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">private_ip_address=None</em>, <em class="sig-param">private_ip_addresses=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_machine_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkInterface resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>applied_dns_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If the Virtual Machine using this Network Interface is part of an Availability Set, then this list will have the union of all DNS servers from all Network Interfaces that are part of the Availability Set.</p></li>
<li><p><strong>dns_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IP Addresses defining the DNS Servers which should be used for this Network Interface.</p></li>
<li><p><strong>enable_accelerated_networking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Accelerated Networking be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_ip_forwarding</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should IP Forwarding be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>internal_dns_name_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The (relative) DNS Name used for internal communications between Virtual Machines in the same Virtual Network.</p></li>
<li><p><strong>ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> blocks as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the Network Interface should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>mac_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Media Access Control (MAC) Address of the Network Interface.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Interface. Changing this forces a new resource to be created.</p></li>
<li><p><strong>private_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The first private IP address of the network interface.</p></li>
<li><p><strong>private_ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The private IP addresses of the network interface.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which to create the Network Interface. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>virtual_machine_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Machine which this Network Interface is connected to.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ip_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Network Interface. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The first private IP address of the network interface.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddressAllocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddressVersion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkInterface.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterface.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterface.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_address_pool_id=None</em>, <em class="sig-param">ip_configuration_name=None</em>, <em class="sig-param">network_interface_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the association between a Network Interface and a Application Gateway’s Backend Address Pool.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_interface_application_gateway_backend_address_pool_association.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_interface_application_gateway_backend_address_pool_association.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_address_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Application Gateway’s Backend Address Pool which this Network Interface which should be connected to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>ip_configuration_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the IP Configuration within the Network Interface which should be connected to the Backend Address Pool. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Interface. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.backend_address_pool_id">
<code class="sig-name descname">backend_address_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.backend_address_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Application Gateway’s Backend Address Pool which this Network Interface which should be connected to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.ip_configuration_name">
<code class="sig-name descname">ip_configuration_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.ip_configuration_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the IP Configuration within the Network Interface which should be connected to the Backend Address Pool. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.network_interface_id">
<code class="sig-name descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Interface. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_address_pool_id=None</em>, <em class="sig-param">ip_configuration_name=None</em>, <em class="sig-param">network_interface_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_address_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Application Gateway’s Backend Address Pool which this Network Interface which should be connected to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>ip_configuration_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the IP Configuration within the Network Interface which should be connected to the Backend Address Pool. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Interface. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationGatewayBackendAddressPoolAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterfaceApplicationSecurityGroupAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">NetworkInterfaceApplicationSecurityGroupAssociation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_security_group_id=None</em>, <em class="sig-param">network_interface_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationSecurityGroupAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the association between a Network Interface and a Application Security Group.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_interface_application_security_group_association.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_interface_application_security_group_association.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Application Security Group which this Network Interface which should be connected to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Interface. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceApplicationSecurityGroupAssociation.application_security_group_id">
<code class="sig-name descname">application_security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationSecurityGroupAssociation.application_security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Application Security Group which this Network Interface which should be connected to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceApplicationSecurityGroupAssociation.network_interface_id">
<code class="sig-name descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationSecurityGroupAssociation.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Interface. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkInterfaceApplicationSecurityGroupAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_security_group_id=None</em>, <em class="sig-param">network_interface_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationSecurityGroupAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkInterfaceApplicationSecurityGroupAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Application Security Group which this Network Interface which should be connected to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Interface. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkInterfaceApplicationSecurityGroupAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationSecurityGroupAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterfaceApplicationSecurityGroupAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceApplicationSecurityGroupAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">NetworkInterfaceBackendAddressPoolAssociation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_address_pool_id=None</em>, <em class="sig-param">ip_configuration_name=None</em>, <em class="sig-param">network_interface_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the association between a Network Interface and a Load Balancer’s Backend Address Pool.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_interface_backend_address_pool_association.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_interface_backend_address_pool_association.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_address_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer Backend Address Pool which this Network Interface which should be connected to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>ip_configuration_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the IP Configuration within the Network Interface which should be connected to the Backend Address Pool. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Interface. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.backend_address_pool_id">
<code class="sig-name descname">backend_address_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.backend_address_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Load Balancer Backend Address Pool which this Network Interface which should be connected to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.ip_configuration_name">
<code class="sig-name descname">ip_configuration_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.ip_configuration_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the IP Configuration within the Network Interface which should be connected to the Backend Address Pool. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.network_interface_id">
<code class="sig-name descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Interface. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_address_pool_id=None</em>, <em class="sig-param">ip_configuration_name=None</em>, <em class="sig-param">network_interface_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkInterfaceBackendAddressPoolAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_address_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer Backend Address Pool which this Network Interface which should be connected to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>ip_configuration_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the IP Configuration within the Network Interface which should be connected to the Backend Address Pool. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Interface. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceBackendAddressPoolAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterfaceNatRuleAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">NetworkInterfaceNatRuleAssociation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ip_configuration_name=None</em>, <em class="sig-param">nat_rule_id=None</em>, <em class="sig-param">network_interface_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceNatRuleAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the association between a Network Interface and a Load Balancer’s NAT Rule.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_interface_nat_rule_association.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_interface_nat_rule_association.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip_configuration_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>nat_rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Interface. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceNatRuleAssociation.ip_configuration_name">
<code class="sig-name descname">ip_configuration_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceNatRuleAssociation.ip_configuration_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceNatRuleAssociation.nat_rule_id">
<code class="sig-name descname">nat_rule_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceNatRuleAssociation.nat_rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceNatRuleAssociation.network_interface_id">
<code class="sig-name descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceNatRuleAssociation.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Interface. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkInterfaceNatRuleAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ip_configuration_name=None</em>, <em class="sig-param">nat_rule_id=None</em>, <em class="sig-param">network_interface_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceNatRuleAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkInterfaceNatRuleAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip_configuration_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the IP Configuration within the Network Interface which should be connected to the NAT Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>nat_rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer NAT Rule which this Network Interface which should be connected to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Interface. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkInterfaceNatRuleAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceNatRuleAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterfaceNatRuleAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceNatRuleAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterfaceSecurityGroupAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">NetworkInterfaceSecurityGroupAssociation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">network_interface_id=None</em>, <em class="sig-param">network_security_group_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceSecurityGroupAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages the association between a Network Interface and a Network Security Group.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_interface_security_group_association.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_interface_security_group_association.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Interface. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Security Group which should be attached to the Network Interface. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceSecurityGroupAssociation.network_interface_id">
<code class="sig-name descname">network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceSecurityGroupAssociation.network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Interface. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkInterfaceSecurityGroupAssociation.network_security_group_id">
<code class="sig-name descname">network_security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceSecurityGroupAssociation.network_security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Security Group which should be attached to the Network Interface. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkInterfaceSecurityGroupAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">network_interface_id=None</em>, <em class="sig-param">network_security_group_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceSecurityGroupAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkInterfaceSecurityGroupAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Interface. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Security Group which should be attached to the Network Interface. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkInterfaceSecurityGroupAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceSecurityGroupAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkInterfaceSecurityGroupAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkInterfaceSecurityGroupAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkPacketCapture">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">NetworkPacketCapture</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">filters=None</em>, <em class="sig-param">maximum_bytes_per_packet=None</em>, <em class="sig-param">maximum_bytes_per_session=None</em>, <em class="sig-param">maximum_capture_duration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_watcher_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_location=None</em>, <em class="sig-param">target_resource_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkPacketCapture" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures Network Packet Capturing against a Virtual Machine using a Network Watcher.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_packet_capture.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_packet_capture.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">filter</span></code> blocks as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>maximum_bytes_per_packet</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of bytes captured per packet. The remaining bytes are truncated. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> (Entire Packet Captured). Changing this forces a new resource to be created.</p></li>
<li><p><strong>maximum_bytes_per_session</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum size of the capture in Bytes. Defaults to <code class="docutils literal notranslate"><span class="pre">1073741824</span></code> (1GB). Changing this forces a new resource to be created.</p></li>
<li><p><strong>maximum_capture_duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum duration of the capture session in seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">18000</span></code> (5 hours). Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for this Network Packet Capture. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_watcher_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Watcher. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Network Watcher exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_location</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_location</span></code> block as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Resource to capture packets from. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">localIpAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteIpAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remotePort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>storage_location</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filePath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storagePath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI of the storage path to save the packet capture.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkPacketCapture.filters">
<code class="sig-name descname">filters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkPacketCapture.filters" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">filter</span></code> blocks as defined below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">localIpAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localPort</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteIpAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remotePort</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkPacketCapture.maximum_bytes_per_packet">
<code class="sig-name descname">maximum_bytes_per_packet</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkPacketCapture.maximum_bytes_per_packet" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of bytes captured per packet. The remaining bytes are truncated. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> (Entire Packet Captured). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkPacketCapture.maximum_bytes_per_session">
<code class="sig-name descname">maximum_bytes_per_session</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkPacketCapture.maximum_bytes_per_session" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum size of the capture in Bytes. Defaults to <code class="docutils literal notranslate"><span class="pre">1073741824</span></code> (1GB). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkPacketCapture.maximum_capture_duration">
<code class="sig-name descname">maximum_capture_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkPacketCapture.maximum_capture_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum duration of the capture session in seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">18000</span></code> (5 hours). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkPacketCapture.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkPacketCapture.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for this Network Packet Capture. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkPacketCapture.network_watcher_name">
<code class="sig-name descname">network_watcher_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkPacketCapture.network_watcher_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Network Watcher. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkPacketCapture.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkPacketCapture.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Network Watcher exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkPacketCapture.storage_location">
<code class="sig-name descname">storage_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkPacketCapture.storage_location" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_location</span></code> block as defined below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filePath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storagePath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URI of the storage path to save the packet capture.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkPacketCapture.target_resource_id">
<code class="sig-name descname">target_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkPacketCapture.target_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Resource to capture packets from. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkPacketCapture.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">filters=None</em>, <em class="sig-param">maximum_bytes_per_packet=None</em>, <em class="sig-param">maximum_bytes_per_session=None</em>, <em class="sig-param">maximum_capture_duration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_watcher_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_location=None</em>, <em class="sig-param">target_resource_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkPacketCapture.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkPacketCapture resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">filter</span></code> blocks as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>maximum_bytes_per_packet</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of bytes captured per packet. The remaining bytes are truncated. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> (Entire Packet Captured). Changing this forces a new resource to be created.</p></li>
<li><p><strong>maximum_bytes_per_session</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum size of the capture in Bytes. Defaults to <code class="docutils literal notranslate"><span class="pre">1073741824</span></code> (1GB). Changing this forces a new resource to be created.</p></li>
<li><p><strong>maximum_capture_duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum duration of the capture session in seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">18000</span></code> (5 hours). Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for this Network Packet Capture. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_watcher_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Watcher. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Network Watcher exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_location</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_location</span></code> block as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Resource to capture packets from. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">localIpAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteIpAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remotePort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>storage_location</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filePath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storagePath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI of the storage path to save the packet capture.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkPacketCapture.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkPacketCapture.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkPacketCapture.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkPacketCapture.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkSecurityGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">NetworkSecurityGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">security_rules=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a network security group that contains a list of network security rules.  Network security groups enable inbound or outbound traffic to be enabled or denied.</p>
<blockquote>
<div><p><strong>NOTE on Network Security Groups and Network Security Rules:</strong> This provider currently
provides both a standalone Network Security Rule resource, and allows for Network Security Rules to be defined in-line within the Network Security Group resource.
At this time you cannot use a Network Security Group with in-line Network Security Rules in conjunction with any Network Security Rule resources. Doing so will cause a conflict of rule settings and will overwrite rules.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_security_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_security_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the security rule.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the network security group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>security_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of objects representing security rules, as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>security_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">access</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether network traffic is allowed or denied. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description for this rule. Restricted to 140 characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination_address_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - CIDR or destination IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if <code class="docutils literal notranslate"><span class="pre">destination_address_prefixes</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination_address_prefixes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of destination address prefixes. Tags may not be used. This is required if <code class="docutils literal notranslate"><span class="pre">destination_address_prefix</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination_application_security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A List of destination Application Security Group ID’s</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination_port_range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Destination Port or Range. Integer or range between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code> or <code class="docutils literal notranslate"><span class="pre">*</span></code> to match any. This is required if <code class="docutils literal notranslate"><span class="pre">destination_port_ranges</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination_port_ranges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of destination ports or port ranges. This is required if <code class="docutils literal notranslate"><span class="pre">destination_port_range</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">direction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The direction specifies if rule will be evaluated on incoming or outgoing traffic. Possible values are <code class="docutils literal notranslate"><span class="pre">Inbound</span></code> and <code class="docutils literal notranslate"><span class="pre">Outbound</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the security rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Network protocol this rule applies to. Can be <code class="docutils literal notranslate"><span class="pre">Tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">Udp</span></code>, <code class="docutils literal notranslate"><span class="pre">Icmp</span></code>, or <code class="docutils literal notranslate"><span class="pre">*</span></code> to match all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_address_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - CIDR or source IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if <code class="docutils literal notranslate"><span class="pre">source_address_prefixes</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_address_prefixes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of source address prefixes. Tags may not be used. This is required if <code class="docutils literal notranslate"><span class="pre">source_address_prefix</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_application_security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A List of source Application Security Group ID’s</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_port_range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Source Port or Range. Integer or range between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code> or <code class="docutils literal notranslate"><span class="pre">*</span></code> to match any. This is required if <code class="docutils literal notranslate"><span class="pre">source_port_ranges</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_port_ranges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of source ports or port ranges. This is required if <code class="docutils literal notranslate"><span class="pre">source_port_range</span></code> is not specified.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityGroup.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityGroup.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the security rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityGroup.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityGroup.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the network security group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityGroup.security_rules">
<code class="sig-name descname">security_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityGroup.security_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of objects representing security rules, as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">access</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies whether network traffic is allowed or denied. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A description for this rule. Restricted to 140 characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination_address_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - CIDR or destination IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if <code class="docutils literal notranslate"><span class="pre">destination_address_prefixes</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination_address_prefixes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of destination address prefixes. Tags may not be used. This is required if <code class="docutils literal notranslate"><span class="pre">destination_address_prefix</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination_application_security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A List of destination Application Security Group ID’s</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination_port_range</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Destination Port or Range. Integer or range between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code> or <code class="docutils literal notranslate"><span class="pre">*</span></code> to match any. This is required if <code class="docutils literal notranslate"><span class="pre">destination_port_ranges</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination_port_ranges</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of destination ports or port ranges. This is required if <code class="docutils literal notranslate"><span class="pre">destination_port_range</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">direction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The direction specifies if rule will be evaluated on incoming or outgoing traffic. Possible values are <code class="docutils literal notranslate"><span class="pre">Inbound</span></code> and <code class="docutils literal notranslate"><span class="pre">Outbound</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the security rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Network protocol this rule applies to. Can be <code class="docutils literal notranslate"><span class="pre">Tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">Udp</span></code>, <code class="docutils literal notranslate"><span class="pre">Icmp</span></code>, or <code class="docutils literal notranslate"><span class="pre">*</span></code> to match all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_address_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - CIDR or source IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if <code class="docutils literal notranslate"><span class="pre">source_address_prefixes</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_address_prefixes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of source address prefixes. Tags may not be used. This is required if <code class="docutils literal notranslate"><span class="pre">source_address_prefix</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_application_security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A List of source Application Security Group ID’s</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_port_range</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Source Port or Range. Integer or range between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code> or <code class="docutils literal notranslate"><span class="pre">*</span></code> to match any. This is required if <code class="docutils literal notranslate"><span class="pre">source_port_ranges</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_port_ranges</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of source ports or port ranges. This is required if <code class="docutils literal notranslate"><span class="pre">source_port_range</span></code> is not specified.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityGroup.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkSecurityGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">security_rules=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkSecurityGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the security rule.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the network security group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>security_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of objects representing security rules, as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>security_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">access</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies whether network traffic is allowed or denied. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description for this rule. Restricted to 140 characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination_address_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - CIDR or destination IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if <code class="docutils literal notranslate"><span class="pre">destination_address_prefixes</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination_address_prefixes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of destination address prefixes. Tags may not be used. This is required if <code class="docutils literal notranslate"><span class="pre">destination_address_prefix</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination_application_security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A List of destination Application Security Group ID’s</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination_port_range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Destination Port or Range. Integer or range between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code> or <code class="docutils literal notranslate"><span class="pre">*</span></code> to match any. This is required if <code class="docutils literal notranslate"><span class="pre">destination_port_ranges</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">destination_port_ranges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of destination ports or port ranges. This is required if <code class="docutils literal notranslate"><span class="pre">destination_port_range</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">direction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The direction specifies if rule will be evaluated on incoming or outgoing traffic. Possible values are <code class="docutils literal notranslate"><span class="pre">Inbound</span></code> and <code class="docutils literal notranslate"><span class="pre">Outbound</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the security rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Network protocol this rule applies to. Can be <code class="docutils literal notranslate"><span class="pre">Tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">Udp</span></code>, <code class="docutils literal notranslate"><span class="pre">Icmp</span></code>, or <code class="docutils literal notranslate"><span class="pre">*</span></code> to match all.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_address_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - CIDR or source IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if <code class="docutils literal notranslate"><span class="pre">source_address_prefixes</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_address_prefixes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of source address prefixes. Tags may not be used. This is required if <code class="docutils literal notranslate"><span class="pre">source_address_prefix</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_application_security_group_ids</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A List of source Application Security Group ID’s</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_port_range</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Source Port or Range. Integer or range between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code> or <code class="docutils literal notranslate"><span class="pre">*</span></code> to match any. This is required if <code class="docutils literal notranslate"><span class="pre">source_port_ranges</span></code> is not specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_port_ranges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of source ports or port ranges. This is required if <code class="docutils literal notranslate"><span class="pre">source_port_range</span></code> is not specified.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkSecurityGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkSecurityGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkSecurityRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">NetworkSecurityRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">destination_address_prefix=None</em>, <em class="sig-param">destination_address_prefixes=None</em>, <em class="sig-param">destination_application_security_group_ids=None</em>, <em class="sig-param">destination_port_range=None</em>, <em class="sig-param">destination_port_ranges=None</em>, <em class="sig-param">direction=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_security_group_name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_address_prefix=None</em>, <em class="sig-param">source_address_prefixes=None</em>, <em class="sig-param">source_application_security_group_ids=None</em>, <em class="sig-param">source_port_range=None</em>, <em class="sig-param">source_port_ranges=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Network Security Rule.</p>
<blockquote>
<div><p><strong>NOTE on Network Security Groups and Network Security Rules:</strong> This provider currently
provides both a standalone Network Security Rule resource, and allows for Network Security Rules to be defined in-line within the Network Security Group resource.
At this time you cannot use a Network Security Group with in-line Network Security Rules in conjunction with any Network Security Rule resources. Doing so will cause a conflict of rule settings and will overwrite rules.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_security_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_security_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether network traffic is allowed or denied. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this rule. Restricted to 140 characters.</p></li>
<li><p><strong>destination_address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CIDR or destination IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if <code class="docutils literal notranslate"><span class="pre">destination_address_prefixes</span></code> is not specified.</p></li>
<li><p><strong>destination_address_prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of destination address prefixes. Tags may not be used. This is required if <code class="docutils literal notranslate"><span class="pre">destination_address_prefix</span></code> is not specified.</p></li>
<li><p><strong>destination_application_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A List of destination Application Security Group ID’s</p></li>
<li><p><strong>destination_port_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination Port or Range. Integer or range between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code> or <cite>*``to match any. This is required if`</cite>destination_port_ranges<a href="#id1"><span class="problematic" id="id2">``</span></a>is not specified.</p></li>
<li><p><strong>destination_port_ranges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of destination ports or port ranges. This is required if``destination_port_range<a href="#id3"><span class="problematic" id="id4">``</span></a>is not specified.</p></li>
<li><p><strong>direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The direction specifies if rule will be evaluated on incoming or outgoing traffic. Possible values are``Inbound<code class="docutils literal notranslate"><span class="pre">and</span></code>Outbound<a href="#id5"><span class="problematic" id="id6">``</span></a>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the security rule. This needs to be unique across all Rules in the Network Security Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_security_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Security Group that we want to attach the rule to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network protocol this rule applies to. Possible values include``Tcp<code class="docutils literal notranslate"><span class="pre">,</span></code>Udp<code class="docutils literal notranslate"><span class="pre">,</span></code>Icmp<code class="docutils literal notranslate"><span class="pre">,</span> <span class="pre">or</span></code><a href="#id7"><span class="problematic" id="id8">*</span></a>` (which matches all).</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Network Security Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CIDR or source IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if <code class="docutils literal notranslate"><span class="pre">source_address_prefixes</span></code> is not specified.</p></li>
<li><p><strong>source_address_prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of source address prefixes. Tags may not be used. This is required if <code class="docutils literal notranslate"><span class="pre">source_address_prefix</span></code> is not specified.</p></li>
<li><p><strong>source_application_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A List of source Application Security Group ID’s</p></li>
<li><p><strong>source_port_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Source Port or Range. Integer or range between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code> or <code class="docutils literal notranslate"><span class="pre">*</span></code> to match any. This is required if <code class="docutils literal notranslate"><span class="pre">source_port_ranges</span></code> is not specified.</p></li>
<li><p><strong>source_port_ranges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of source ports or port ranges. This is required if <code class="docutils literal notranslate"><span class="pre">source_port_range</span></code> is not specified.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.access">
<code class="sig-name descname">access</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.access" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether network traffic is allowed or denied. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for this rule. Restricted to 140 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.destination_address_prefix">
<code class="sig-name descname">destination_address_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.destination_address_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR or destination IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if <code class="docutils literal notranslate"><span class="pre">destination_address_prefixes</span></code> is not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.destination_address_prefixes">
<code class="sig-name descname">destination_address_prefixes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.destination_address_prefixes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of destination address prefixes. Tags may not be used. This is required if <code class="docutils literal notranslate"><span class="pre">destination_address_prefix</span></code> is not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.destination_application_security_group_ids">
<code class="sig-name descname">destination_application_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.destination_application_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A List of destination Application Security Group ID’s</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.destination_port_range">
<code class="sig-name descname">destination_port_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.destination_port_range" title="Permalink to this definition">¶</a></dt>
<dd><p>Destination Port or Range. Integer or range between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code> or <code class="docutils literal notranslate"><span class="pre">*</span></code> to match any. This is required if <code class="docutils literal notranslate"><span class="pre">destination_port_ranges</span></code> is not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.destination_port_ranges">
<code class="sig-name descname">destination_port_ranges</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.destination_port_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>List of destination ports or port ranges. This is required if <code class="docutils literal notranslate"><span class="pre">destination_port_range</span></code> is not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.direction">
<code class="sig-name descname">direction</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.direction" title="Permalink to this definition">¶</a></dt>
<dd><p>The direction specifies if rule will be evaluated on incoming or outgoing traffic. Possible values are <code class="docutils literal notranslate"><span class="pre">Inbound</span></code> and <code class="docutils literal notranslate"><span class="pre">Outbound</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the security rule. This needs to be unique across all Rules in the Network Security Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.network_security_group_name">
<code class="sig-name descname">network_security_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.network_security_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Network Security Group that we want to attach the rule to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.protocol">
<code class="sig-name descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>Network protocol this rule applies to. Possible values include <code class="docutils literal notranslate"><span class="pre">Tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">Udp</span></code>, <code class="docutils literal notranslate"><span class="pre">Icmp</span></code>, or <code class="docutils literal notranslate"><span class="pre">*</span></code> (which matches all).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Network Security Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.source_address_prefix">
<code class="sig-name descname">source_address_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.source_address_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR or source IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if <code class="docutils literal notranslate"><span class="pre">source_address_prefixes</span></code> is not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.source_address_prefixes">
<code class="sig-name descname">source_address_prefixes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.source_address_prefixes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of source address prefixes. Tags may not be used. This is required if <code class="docutils literal notranslate"><span class="pre">source_address_prefix</span></code> is not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.source_application_security_group_ids">
<code class="sig-name descname">source_application_security_group_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.source_application_security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A List of source Application Security Group ID’s</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.source_port_range">
<code class="sig-name descname">source_port_range</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.source_port_range" title="Permalink to this definition">¶</a></dt>
<dd><p>Source Port or Range. Integer or range between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code> or <code class="docutils literal notranslate"><span class="pre">*</span></code> to match any. This is required if <code class="docutils literal notranslate"><span class="pre">source_port_ranges</span></code> is not specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkSecurityRule.source_port_ranges">
<code class="sig-name descname">source_port_ranges</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.source_port_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>List of source ports or port ranges. This is required if <code class="docutils literal notranslate"><span class="pre">source_port_range</span></code> is not specified.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkSecurityRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">destination_address_prefix=None</em>, <em class="sig-param">destination_address_prefixes=None</em>, <em class="sig-param">destination_application_security_group_ids=None</em>, <em class="sig-param">destination_port_range=None</em>, <em class="sig-param">destination_port_ranges=None</em>, <em class="sig-param">direction=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_security_group_name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_address_prefix=None</em>, <em class="sig-param">source_address_prefixes=None</em>, <em class="sig-param">source_application_security_group_ids=None</em>, <em class="sig-param">source_port_range=None</em>, <em class="sig-param">source_port_ranges=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkSecurityRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether network traffic is allowed or denied. Possible values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this rule. Restricted to 140 characters.</p></li>
<li><p><strong>destination_address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CIDR or destination IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if <code class="docutils literal notranslate"><span class="pre">destination_address_prefixes</span></code> is not specified.</p></li>
<li><p><strong>destination_address_prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of destination address prefixes. Tags may not be used. This is required if <code class="docutils literal notranslate"><span class="pre">destination_address_prefix</span></code> is not specified.</p></li>
<li><p><strong>destination_application_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A List of destination Application Security Group ID’s</p></li>
<li><p><strong>destination_port_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination Port or Range. Integer or range between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code> or <cite>*``to match any. This is required if`</cite>destination_port_ranges<a href="#id9"><span class="problematic" id="id10">``</span></a>is not specified.</p></li>
<li><p><strong>destination_port_ranges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of destination ports or port ranges. This is required if``destination_port_range<a href="#id11"><span class="problematic" id="id12">``</span></a>is not specified.</p></li>
<li><p><strong>direction</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The direction specifies if rule will be evaluated on incoming or outgoing traffic. Possible values are``Inbound<code class="docutils literal notranslate"><span class="pre">and</span></code>Outbound<a href="#id13"><span class="problematic" id="id14">``</span></a>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the security rule. This needs to be unique across all Rules in the Network Security Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_security_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Security Group that we want to attach the rule to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network protocol this rule applies to. Possible values include``Tcp<code class="docutils literal notranslate"><span class="pre">,</span></code>Udp<code class="docutils literal notranslate"><span class="pre">,</span></code>Icmp<code class="docutils literal notranslate"><span class="pre">,</span> <span class="pre">or</span></code><a href="#id15"><span class="problematic" id="id16">*</span></a>` (which matches all).</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Network Security Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – CIDR or source IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if <code class="docutils literal notranslate"><span class="pre">source_address_prefixes</span></code> is not specified.</p></li>
<li><p><strong>source_address_prefixes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of source address prefixes. Tags may not be used. This is required if <code class="docutils literal notranslate"><span class="pre">source_address_prefix</span></code> is not specified.</p></li>
<li><p><strong>source_application_security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A List of source Application Security Group ID’s</p></li>
<li><p><strong>source_port_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Source Port or Range. Integer or range between <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code> or <code class="docutils literal notranslate"><span class="pre">*</span></code> to match any. This is required if <code class="docutils literal notranslate"><span class="pre">source_port_ranges</span></code> is not specified.</p></li>
<li><p><strong>source_port_ranges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of source ports or port ranges. This is required if <code class="docutils literal notranslate"><span class="pre">source_port_range</span></code> is not specified.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkSecurityRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkSecurityRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkSecurityRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkWatcher">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">NetworkWatcher</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkWatcher" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Network Watcher.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_watcher.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_watcher.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Watcher. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Network Watcher. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkWatcher.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkWatcher.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkWatcher.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkWatcher.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Network Watcher. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkWatcher.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkWatcher.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Network Watcher. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkWatcher.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkWatcher.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkWatcher.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkWatcher.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkWatcher resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Watcher. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Network Watcher. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkWatcher.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkWatcher.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkWatcher.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkWatcher.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkWatcherFlowLog">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">NetworkWatcherFlowLog</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">network_security_group_id=None</em>, <em class="sig-param">network_watcher_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">retention_policy=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">traffic_analytics=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkWatcherFlowLog" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Network Watcher Flow Log.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_watcher_flow_log.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_watcher_flow_log.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to enable/disable traffic analytics.</p></li>
<li><p><strong>network_security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Security Group for which to enable flow logs for. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_watcher_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Watcher. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Network Watcher was deployed. Changing this forces a new resource to be created.</p></li>
<li><p><strong>retention_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> block as documented below.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Storage Account where flow logs are stored.</p></li>
<li><p><strong>traffic_analytics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">traffic_analytics</span></code> block as documented below.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The version (revision) of the flow log. Possible values are <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>retention_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days to retain flow log records.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean flag to enable/disable traffic analytics.</p></li>
</ul>
<p>The <strong>traffic_analytics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean flag to enable/disable traffic analytics.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">intervalInMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently service should do flow analytics in minutes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource guid of the attached workspace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspaceRegion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location of the attached workspace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspace_resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource ID of the attached workspace.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.NetworkWatcherFlowLog.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkWatcherFlowLog.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to enable/disable traffic analytics.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkWatcherFlowLog.network_security_group_id">
<code class="sig-name descname">network_security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkWatcherFlowLog.network_security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Security Group for which to enable flow logs for. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkWatcherFlowLog.network_watcher_name">
<code class="sig-name descname">network_watcher_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkWatcherFlowLog.network_watcher_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Network Watcher. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkWatcherFlowLog.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkWatcherFlowLog.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Network Watcher was deployed. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkWatcherFlowLog.retention_policy">
<code class="sig-name descname">retention_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkWatcherFlowLog.retention_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of days to retain flow log records.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean flag to enable/disable traffic analytics.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkWatcherFlowLog.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkWatcherFlowLog.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Storage Account where flow logs are stored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkWatcherFlowLog.traffic_analytics">
<code class="sig-name descname">traffic_analytics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkWatcherFlowLog.traffic_analytics" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">traffic_analytics</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Boolean flag to enable/disable traffic analytics.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">intervalInMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How frequently service should do flow analytics in minutes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The resource guid of the attached workspace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspaceRegion</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The location of the attached workspace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspace_resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The resource ID of the attached workspace.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.NetworkWatcherFlowLog.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.NetworkWatcherFlowLog.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version (revision) of the flow log. Possible values are <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkWatcherFlowLog.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">network_security_group_id=None</em>, <em class="sig-param">network_watcher_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">retention_policy=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">traffic_analytics=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkWatcherFlowLog.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkWatcherFlowLog resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to enable/disable traffic analytics.</p></li>
<li><p><strong>network_security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Security Group for which to enable flow logs for. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_watcher_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Watcher. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Network Watcher was deployed. Changing this forces a new resource to be created.</p></li>
<li><p><strong>retention_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> block as documented below.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Storage Account where flow logs are stored.</p></li>
<li><p><strong>traffic_analytics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">traffic_analytics</span></code> block as documented below.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The version (revision) of the flow log. Possible values are <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">2</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>retention_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">days</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of days to retain flow log records.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean flag to enable/disable traffic analytics.</p></li>
</ul>
<p>The <strong>traffic_analytics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Boolean flag to enable/disable traffic analytics.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">intervalInMinutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How frequently service should do flow analytics in minutes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource guid of the attached workspace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspaceRegion</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location of the attached workspace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspace_resource_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource ID of the attached workspace.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.NetworkWatcherFlowLog.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkWatcherFlowLog.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.NetworkWatcherFlowLog.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.NetworkWatcherFlowLog.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.PacketCapture">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">PacketCapture</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">filters=None</em>, <em class="sig-param">maximum_bytes_per_packet=None</em>, <em class="sig-param">maximum_bytes_per_session=None</em>, <em class="sig-param">maximum_capture_duration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_watcher_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_location=None</em>, <em class="sig-param">target_resource_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PacketCapture" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures Packet Capturing against a Virtual Machine using a Network Watcher.</p>
<blockquote>
<div><p><strong>NOTE:</strong> This resource has been deprecated in favour of the <code class="docutils literal notranslate"><span class="pre">network.NetworkConnectionMonitor</span></code> resource and will be removed in the next major version of the AzureRM Provider. The new resource shares the same fields as this one, and information on migrating across can be found in this guide.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/packet_capture.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/packet_capture.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">filter</span></code> blocks as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>maximum_bytes_per_packet</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of bytes captured per packet. The remaining bytes are truncated. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> (Entire Packet Captured). Changing this forces a new resource to be created.</p></li>
<li><p><strong>maximum_bytes_per_session</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum size of the capture in Bytes. Defaults to <code class="docutils literal notranslate"><span class="pre">1073741824</span></code> (1GB). Changing this forces a new resource to be created.</p></li>
<li><p><strong>maximum_capture_duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum duration of the capture session in seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">18000</span></code> (5 hours). Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for this Packet Capture. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_watcher_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Watcher. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Network Watcher exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_location</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_location</span></code> block as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Resource to capture packets from. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">localIpAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteIpAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remotePort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>storage_location</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filePath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storagePath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI of the storage path to save the packet capture.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.PacketCapture.filters">
<code class="sig-name descname">filters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PacketCapture.filters" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">filter</span></code> blocks as defined below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">localIpAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localPort</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteIpAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remotePort</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PacketCapture.maximum_bytes_per_packet">
<code class="sig-name descname">maximum_bytes_per_packet</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PacketCapture.maximum_bytes_per_packet" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of bytes captured per packet. The remaining bytes are truncated. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> (Entire Packet Captured). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PacketCapture.maximum_bytes_per_session">
<code class="sig-name descname">maximum_bytes_per_session</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PacketCapture.maximum_bytes_per_session" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum size of the capture in Bytes. Defaults to <code class="docutils literal notranslate"><span class="pre">1073741824</span></code> (1GB). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PacketCapture.maximum_capture_duration">
<code class="sig-name descname">maximum_capture_duration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PacketCapture.maximum_capture_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum duration of the capture session in seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">18000</span></code> (5 hours). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PacketCapture.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PacketCapture.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name to use for this Packet Capture. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PacketCapture.network_watcher_name">
<code class="sig-name descname">network_watcher_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PacketCapture.network_watcher_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Network Watcher. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PacketCapture.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PacketCapture.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Network Watcher exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PacketCapture.storage_location">
<code class="sig-name descname">storage_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PacketCapture.storage_location" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_location</span></code> block as defined below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filePath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storagePath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URI of the storage path to save the packet capture.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PacketCapture.target_resource_id">
<code class="sig-name descname">target_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PacketCapture.target_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Resource to capture packets from. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.PacketCapture.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">filters=None</em>, <em class="sig-param">maximum_bytes_per_packet=None</em>, <em class="sig-param">maximum_bytes_per_session=None</em>, <em class="sig-param">maximum_capture_duration=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_watcher_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_location=None</em>, <em class="sig-param">target_resource_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PacketCapture.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PacketCapture resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">filter</span></code> blocks as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>maximum_bytes_per_packet</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of bytes captured per packet. The remaining bytes are truncated. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> (Entire Packet Captured). Changing this forces a new resource to be created.</p></li>
<li><p><strong>maximum_bytes_per_session</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum size of the capture in Bytes. Defaults to <code class="docutils literal notranslate"><span class="pre">1073741824</span></code> (1GB). Changing this forces a new resource to be created.</p></li>
<li><p><strong>maximum_capture_duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum duration of the capture session in seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">18000</span></code> (5 hours). Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name to use for this Packet Capture. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_watcher_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Network Watcher. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Network Watcher exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_location</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_location</span></code> block as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Resource to capture packets from. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">localIpAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">localPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteIpAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">remotePort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>storage_location</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filePath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storagePath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URI of the storage path to save the packet capture.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.PacketCapture.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PacketCapture.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.PacketCapture.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PacketCapture.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.PointToPointVpnGateway">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">PointToPointVpnGateway</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connection_configuration=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">scale_unit=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_hub_id=None</em>, <em class="sig-param">vpn_server_configuration_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PointToPointVpnGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Point-to-Site VPN Gateway.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/point_to_site_vpn_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/point_to_site_vpn_gateway.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">connection_configuration</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Point-to-Site VPN Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Point-to-Site VPN Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><strong>scale_unit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Scale Unit for this Point-to-Site VPN Gateway.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Point-to-Site VPN Gateway.</p></li>
<li><p><strong>virtual_hub_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Hub where this Point-to-Site VPN Gateway should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>vpn_server_configuration_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPN Server Configuration which this Point-to-Site VPN Gateway should use. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>connection_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Point-to-Site VPN Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpnClientAddressPool</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">addressPrefixes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.PointToPointVpnGateway.connection_configuration">
<code class="sig-name descname">connection_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PointToPointVpnGateway.connection_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">connection_configuration</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Point-to-Site VPN Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpnClientAddressPool</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">addressPrefixes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PointToPointVpnGateway.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PointToPointVpnGateway.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PointToPointVpnGateway.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PointToPointVpnGateway.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Point-to-Site VPN Gateway. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PointToPointVpnGateway.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PointToPointVpnGateway.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Point-to-Site VPN Gateway. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PointToPointVpnGateway.scale_unit">
<code class="sig-name descname">scale_unit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PointToPointVpnGateway.scale_unit" title="Permalink to this definition">¶</a></dt>
<dd><p>The Scale Unit for this Point-to-Site VPN Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PointToPointVpnGateway.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PointToPointVpnGateway.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the Point-to-Site VPN Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PointToPointVpnGateway.virtual_hub_id">
<code class="sig-name descname">virtual_hub_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PointToPointVpnGateway.virtual_hub_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Virtual Hub where this Point-to-Site VPN Gateway should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PointToPointVpnGateway.vpn_server_configuration_id">
<code class="sig-name descname">vpn_server_configuration_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PointToPointVpnGateway.vpn_server_configuration_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VPN Server Configuration which this Point-to-Site VPN Gateway should use. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.PointToPointVpnGateway.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">connection_configuration=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">scale_unit=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_hub_id=None</em>, <em class="sig-param">vpn_server_configuration_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PointToPointVpnGateway.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PointToPointVpnGateway resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">connection_configuration</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Point-to-Site VPN Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Point-to-Site VPN Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><strong>scale_unit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Scale Unit for this Point-to-Site VPN Gateway.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Point-to-Site VPN Gateway.</p></li>
<li><p><strong>virtual_hub_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Hub where this Point-to-Site VPN Gateway should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>vpn_server_configuration_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VPN Server Configuration which this Point-to-Site VPN Gateway should use. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>connection_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Point-to-Site VPN Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpnClientAddressPool</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">addressPrefixes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.PointToPointVpnGateway.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PointToPointVpnGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.PointToPointVpnGateway.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PointToPointVpnGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.Profile">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">Profile</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">container_network_interface=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Network Profile.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/network_profile.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>container_network_interface</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">container_network_interface</span></code> block as documented below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Network Profile. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>container_network_interface</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_configurations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Network Profile. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Network Profile. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.Profile.container_network_interface">
<code class="sig-name descname">container_network_interface</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Profile.container_network_interface" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">container_network_interface</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_configurations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Network Profile. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Network Profile. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Profile.container_network_interface_ids">
<code class="sig-name descname">container_network_interface_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Profile.container_network_interface_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Container Network Interface ID’s.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Profile.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Profile.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Profile.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Profile.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Network Profile. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Profile.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Profile.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Profile.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Profile.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.Profile.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">container_network_interface=None</em>, <em class="sig-param">container_network_interface_ids=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Profile.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Profile resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>container_network_interface</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">container_network_interface</span></code> block as documented below.</p></li>
<li><p><strong>container_network_interface_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Container Network Interface ID’s.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Network Profile. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>container_network_interface</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip_configurations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Network Profile. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Network Profile. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.Profile.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Profile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.Profile.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Profile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.PublicIp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">PublicIp</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allocation_method=None</em>, <em class="sig-param">domain_name_label=None</em>, <em class="sig-param">idle_timeout_in_minutes=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">public_ip_prefix_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">reverse_fqdn=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PublicIp" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Public IP Address.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/public_ip.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/public_ip.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocation_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the allocation method for this IP address. Possible values are <code class="docutils literal notranslate"><span class="pre">Static</span></code> or <code class="docutils literal notranslate"><span class="pre">Dynamic</span></code>.</p></li>
<li><p><strong>domain_name_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Label for the Domain Name. Will be used to make up the FQDN.  If a domain name label is specified, an A DNS record is created for the public IP in the Microsoft Azure DNS system.</p></li>
<li><p><strong>idle_timeout_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the timeout for the TCP idle connection. The value can be set between 4 and 30 minutes.</p></li>
<li><p><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP Version to use, IPv6 or IPv4.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Public IP resource . Changing this forces a
new resource to be created.</p></li>
<li><p><strong>public_ip_prefix_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If specified then public IP address allocated will be provided from the public IP prefix resource.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the public ip.</p></li>
<li><p><strong>reverse_fqdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A fully qualified domain name that resolves to this public IP address. If the reverseFqdn is specified, then a PTR DNS record is created pointing from the IP address in the in-addr.arpa domain to the reverse FQDN.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU of the Public IP. Accepted values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Basic</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A collection containing the availability zone to allocate the Public IP in.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.allocation_method">
<code class="sig-name descname">allocation_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.allocation_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the allocation method for this IP address. Possible values are <code class="docutils literal notranslate"><span class="pre">Static</span></code> or <code class="docutils literal notranslate"><span class="pre">Dynamic</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.domain_name_label">
<code class="sig-name descname">domain_name_label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.domain_name_label" title="Permalink to this definition">¶</a></dt>
<dd><p>Label for the Domain Name. Will be used to make up the FQDN.  If a domain name label is specified, an A DNS record is created for the public IP in the Microsoft Azure DNS system.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.fqdn">
<code class="sig-name descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>Fully qualified domain name of the A DNS record associated with the public IP. <code class="docutils literal notranslate"><span class="pre">domain_name_label</span></code> must be specified to get the <code class="docutils literal notranslate"><span class="pre">fqdn</span></code>. This is the concatenation of the <code class="docutils literal notranslate"><span class="pre">domain_name_label</span></code> and the regionalized DNS zone</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.idle_timeout_in_minutes">
<code class="sig-name descname">idle_timeout_in_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.idle_timeout_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the timeout for the TCP idle connection. The value can be set between 4 and 30 minutes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.ip_address">
<code class="sig-name descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address value that was allocated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.ip_version">
<code class="sig-name descname">ip_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.ip_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP Version to use, IPv6 or IPv4.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Public IP resource . Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.public_ip_prefix_id">
<code class="sig-name descname">public_ip_prefix_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.public_ip_prefix_id" title="Permalink to this definition">¶</a></dt>
<dd><p>If specified then public IP address allocated will be provided from the public IP prefix resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the public ip.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.reverse_fqdn">
<code class="sig-name descname">reverse_fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.reverse_fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>A fully qualified domain name that resolves to this public IP address. If the reverseFqdn is specified, then a PTR DNS record is created pointing from the IP address in the in-addr.arpa domain to the reverse FQDN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU of the Public IP. Accepted values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Basic</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIp.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIp.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection containing the availability zone to allocate the Public IP in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.PublicIp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allocation_method=None</em>, <em class="sig-param">domain_name_label=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">idle_timeout_in_minutes=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">ip_version=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">public_ip_prefix_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">reverse_fqdn=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PublicIp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PublicIp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocation_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the allocation method for this IP address. Possible values are <code class="docutils literal notranslate"><span class="pre">Static</span></code> or <code class="docutils literal notranslate"><span class="pre">Dynamic</span></code>.</p></li>
<li><p><strong>domain_name_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Label for the Domain Name. Will be used to make up the FQDN.  If a domain name label is specified, an A DNS record is created for the public IP in the Microsoft Azure DNS system.</p></li>
<li><p><strong>fqdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Fully qualified domain name of the A DNS record associated with the public IP. <code class="docutils literal notranslate"><span class="pre">domain_name_label</span></code> must be specified to get the <code class="docutils literal notranslate"><span class="pre">fqdn</span></code>. This is the concatenation of the <code class="docutils literal notranslate"><span class="pre">domain_name_label</span></code> and the regionalized DNS zone</p></li>
<li><p><strong>idle_timeout_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the timeout for the TCP idle connection. The value can be set between 4 and 30 minutes.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address value that was allocated.</p></li>
<li><p><strong>ip_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP Version to use, IPv6 or IPv4.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Public IP resource . Changing this forces a
new resource to be created.</p></li>
<li><p><strong>public_ip_prefix_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If specified then public IP address allocated will be provided from the public IP prefix resource.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the public ip.</p></li>
<li><p><strong>reverse_fqdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A fully qualified domain name that resolves to this public IP address. If the reverseFqdn is specified, then a PTR DNS record is created pointing from the IP address in the in-addr.arpa domain to the reverse FQDN.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU of the Public IP. Accepted values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Basic</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A collection containing the availability zone to allocate the Public IP in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.PublicIp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PublicIp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.PublicIp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PublicIp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.PublicIpPrefix">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">PublicIpPrefix</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">prefix_length=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PublicIpPrefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Public IP Prefix.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/public_ip_prefix.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/public_ip_prefix.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Public IP Prefix resource . Changing this forces a new resource to be created.</p></li>
<li><p><strong>prefix_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of bits of the prefix. The value can be set between 28 (16 addresses) and 31 (2 addresses). Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Public IP Prefix.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU of the Public IP Prefix. Accepted values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A collection containing the availability zone to allocate the Public IP Prefix in.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.PublicIpPrefix.ip_prefix">
<code class="sig-name descname">ip_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIpPrefix.ip_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address prefix value that was allocated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIpPrefix.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIpPrefix.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIpPrefix.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIpPrefix.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Public IP Prefix resource . Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIpPrefix.prefix_length">
<code class="sig-name descname">prefix_length</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIpPrefix.prefix_length" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of bits of the prefix. The value can be set between 28 (16 addresses) and 31 (2 addresses). Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIpPrefix.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIpPrefix.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Public IP Prefix.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIpPrefix.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIpPrefix.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU of the Public IP Prefix. Accepted values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIpPrefix.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIpPrefix.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.PublicIpPrefix.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.PublicIpPrefix.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection containing the availability zone to allocate the Public IP Prefix in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.PublicIpPrefix.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ip_prefix=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">prefix_length=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PublicIpPrefix.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PublicIpPrefix resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address prefix value that was allocated.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Public IP Prefix resource . Changing this forces a new resource to be created.</p></li>
<li><p><strong>prefix_length</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of bits of the prefix. The value can be set between 28 (16 addresses) and 31 (2 addresses). Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Public IP Prefix.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU of the Public IP Prefix. Accepted values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A collection containing the availability zone to allocate the Public IP Prefix in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.PublicIpPrefix.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PublicIpPrefix.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.PublicIpPrefix.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.PublicIpPrefix.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.Route">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">Route</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address_prefix=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">next_hop_in_ip_address=None</em>, <em class="sig-param">next_hop_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">route_table_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Route" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Route within a Route Table.</p>
<blockquote>
<div><p><strong>NOTE on Route Tables and Routes:</strong> This provider currently
provides both a standalone Route resource, and allows for Routes to be defined in-line within the Route Table resource.
At this time you cannot use a Route Table with in-line Routes in conjunction with any Route resources. Doing so will cause a conflict of Route configurations and will overwrite Routes.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/route.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/route.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination CIDR to which the route applies, such as <code class="docutils literal notranslate"><span class="pre">10.1.0.0/16</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the route. Changing this forces a new resource to be created.</p></li>
<li><p><strong>next_hop_in_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains the IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is <code class="docutils literal notranslate"><span class="pre">VirtualAppliance</span></code>.</p></li>
<li><p><strong>next_hop_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of Azure hop the packet should be sent to. Possible values are <code class="docutils literal notranslate"><span class="pre">VirtualNetworkGateway</span></code>, <code class="docutils literal notranslate"><span class="pre">VnetLocal</span></code>, <code class="docutils literal notranslate"><span class="pre">Internet</span></code>, <code class="docutils literal notranslate"><span class="pre">VirtualAppliance</span></code> and <code class="docutils literal notranslate"><span class="pre">None</span></code></p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the route. Changing this forces a new resource to be created.</p></li>
<li><p><strong>route_table_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the route table within which create the route. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.Route.address_prefix">
<code class="sig-name descname">address_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Route.address_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination CIDR to which the route applies, such as <code class="docutils literal notranslate"><span class="pre">10.1.0.0/16</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Route.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Route.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the route. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Route.next_hop_in_ip_address">
<code class="sig-name descname">next_hop_in_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Route.next_hop_in_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is <code class="docutils literal notranslate"><span class="pre">VirtualAppliance</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Route.next_hop_type">
<code class="sig-name descname">next_hop_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Route.next_hop_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of Azure hop the packet should be sent to. Possible values are <code class="docutils literal notranslate"><span class="pre">VirtualNetworkGateway</span></code>, <code class="docutils literal notranslate"><span class="pre">VnetLocal</span></code>, <code class="docutils literal notranslate"><span class="pre">Internet</span></code>, <code class="docutils literal notranslate"><span class="pre">VirtualAppliance</span></code> and <code class="docutils literal notranslate"><span class="pre">None</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Route.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Route.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the route. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Route.route_table_name">
<code class="sig-name descname">route_table_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Route.route_table_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the route table within which create the route. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.Route.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address_prefix=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">next_hop_in_ip_address=None</em>, <em class="sig-param">next_hop_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">route_table_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Route.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Route resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination CIDR to which the route applies, such as <code class="docutils literal notranslate"><span class="pre">10.1.0.0/16</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the route. Changing this forces a new resource to be created.</p></li>
<li><p><strong>next_hop_in_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains the IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is <code class="docutils literal notranslate"><span class="pre">VirtualAppliance</span></code>.</p></li>
<li><p><strong>next_hop_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of Azure hop the packet should be sent to. Possible values are <code class="docutils literal notranslate"><span class="pre">VirtualNetworkGateway</span></code>, <code class="docutils literal notranslate"><span class="pre">VnetLocal</span></code>, <code class="docutils literal notranslate"><span class="pre">Internet</span></code>, <code class="docutils literal notranslate"><span class="pre">VirtualAppliance</span></code> and <code class="docutils literal notranslate"><span class="pre">None</span></code></p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the route. Changing this forces a new resource to be created.</p></li>
<li><p><strong>route_table_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the route table within which create the route. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.Route.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Route.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.Route.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Route.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.RouteTable">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">RouteTable</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">disable_bgp_route_propagation=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">routes=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.RouteTable" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Route Table</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/route_table.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/route_table.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disable_bgp_route_propagation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls propagation of routes learned by BGP on that route table. True means disable.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the route.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the route table. Changing this forces a new resource to be created.</p></li>
<li><p><strong>routes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of objects representing routes. Each object accepts the arguments documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>routes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The destination CIDR to which the route applies, such as 10.1.0.0/16</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the route.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">next_hop_in_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Contains the IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is <code class="docutils literal notranslate"><span class="pre">VirtualAppliance</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">next_hop_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Azure hop the packet should be sent to. Possible values are <code class="docutils literal notranslate"><span class="pre">VirtualNetworkGateway</span></code>, <code class="docutils literal notranslate"><span class="pre">VnetLocal</span></code>, <code class="docutils literal notranslate"><span class="pre">Internet</span></code>, <code class="docutils literal notranslate"><span class="pre">VirtualAppliance</span></code> and <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.RouteTable.disable_bgp_route_propagation">
<code class="sig-name descname">disable_bgp_route_propagation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.RouteTable.disable_bgp_route_propagation" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag which controls propagation of routes learned by BGP on that route table. True means disable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.RouteTable.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.RouteTable.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.RouteTable.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.RouteTable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the route.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.RouteTable.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.RouteTable.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the route table. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.RouteTable.routes">
<code class="sig-name descname">routes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.RouteTable.routes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of objects representing routes. Each object accepts the arguments documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The destination CIDR to which the route applies, such as 10.1.0.0/16</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the route.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">next_hop_in_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Contains the IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is <code class="docutils literal notranslate"><span class="pre">VirtualAppliance</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">next_hop_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of Azure hop the packet should be sent to. Possible values are <code class="docutils literal notranslate"><span class="pre">VirtualNetworkGateway</span></code>, <code class="docutils literal notranslate"><span class="pre">VnetLocal</span></code>, <code class="docutils literal notranslate"><span class="pre">Internet</span></code>, <code class="docutils literal notranslate"><span class="pre">VirtualAppliance</span></code> and <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.RouteTable.subnets">
<code class="sig-name descname">subnets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.RouteTable.subnets" title="Permalink to this definition">¶</a></dt>
<dd><p>The collection of Subnets associated with this route table.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.RouteTable.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.RouteTable.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.RouteTable.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">disable_bgp_route_propagation=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">routes=None</em>, <em class="sig-param">subnets=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.RouteTable.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RouteTable resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disable_bgp_route_propagation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag which controls propagation of routes learned by BGP on that route table. True means disable.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the route.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the route table. Changing this forces a new resource to be created.</p></li>
<li><p><strong>routes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of objects representing routes. Each object accepts the arguments documented below.</p></li>
<li><p><strong>subnets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The collection of Subnets associated with this route table.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>routes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The destination CIDR to which the route applies, such as 10.1.0.0/16</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the route.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">next_hop_in_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Contains the IP address packets should be forwarded to. Next hop values are only allowed in routes where the next hop type is <code class="docutils literal notranslate"><span class="pre">VirtualAppliance</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">next_hop_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Azure hop the packet should be sent to. Possible values are <code class="docutils literal notranslate"><span class="pre">VirtualNetworkGateway</span></code>, <code class="docutils literal notranslate"><span class="pre">VnetLocal</span></code>, <code class="docutils literal notranslate"><span class="pre">Internet</span></code>, <code class="docutils literal notranslate"><span class="pre">VirtualAppliance</span></code> and <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.RouteTable.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.RouteTable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.RouteTable.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.RouteTable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.Subnet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">Subnet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address_prefix=None</em>, <em class="sig-param">delegations=None</em>, <em class="sig-param">enforce_private_link_endpoint_network_policies=None</em>, <em class="sig-param">enforce_private_link_service_network_policies=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_endpoints=None</em>, <em class="sig-param">virtual_network_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a subnet. Subnets represent network segments within the IP space defined by the virtual network.</p>
<blockquote>
<div><p><strong>NOTE on Virtual Networks and Subnet’s:</strong> This provider currently
provides both a standalone Subnet resource, and allows for Subnets to be defined in-line within the Virtual Network resource.
At this time you cannot use a Virtual Network with in-line Subnets in conjunction with any Subnet resources. Doing so will cause a conflict of Subnet configurations and will overwrite Subnet’s.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/subnet.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/subnet.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address prefix to use for the subnet.</p></li>
<li><p><strong>delegations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">delegation</span></code> blocks as defined below.</p></li>
<li><p><strong>enforce_private_link_endpoint_network_policies</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or Disable network policies for the private link endpoint on the subnet. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>. Conflicts with enforce_private_link_service_network_policies.</p></li>
<li><p><strong>enforce_private_link_service_network_policies</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or Disable network policies for the private link service on the subnet. Default valule is <code class="docutils literal notranslate"><span class="pre">false</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">enforce_private_link_endpoint_network_policies</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnet. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the subnet. Changing this forces a new resource to be created.</p></li>
<li><p><strong>service_endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of Service endpoints to associate with the subnet. Possible values include: <code class="docutils literal notranslate"><span class="pre">Microsoft.AzureActiveDirectory</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.AzureCosmosDB</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.ContainerRegistry</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.EventHub</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.KeyVault</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.ServiceBus</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.Sql</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.Storage</span></code> and <code class="docutils literal notranslate"><span class="pre">Microsoft.Web</span></code>.</p></li>
<li><p><strong>virtual_network_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual network to which to attach the subnet. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>delegations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the subnet. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceDelegation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the subnet. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.Subnet.address_prefix">
<code class="sig-name descname">address_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Subnet.address_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The address prefix to use for the subnet.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Subnet.delegations">
<code class="sig-name descname">delegations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Subnet.delegations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">delegation</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the subnet. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceDelegation</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the subnet. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Subnet.enforce_private_link_endpoint_network_policies">
<code class="sig-name descname">enforce_private_link_endpoint_network_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Subnet.enforce_private_link_endpoint_network_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or Disable network policies for the private link endpoint on the subnet. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>. Conflicts with enforce_private_link_service_network_policies.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Subnet.enforce_private_link_service_network_policies">
<code class="sig-name descname">enforce_private_link_service_network_policies</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Subnet.enforce_private_link_service_network_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or Disable network policies for the private link service on the subnet. Default valule is <code class="docutils literal notranslate"><span class="pre">false</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">enforce_private_link_endpoint_network_policies</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Subnet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Subnet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the subnet. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Subnet.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Subnet.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the subnet. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Subnet.service_endpoints">
<code class="sig-name descname">service_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Subnet.service_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of Service endpoints to associate with the subnet. Possible values include: <code class="docutils literal notranslate"><span class="pre">Microsoft.AzureActiveDirectory</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.AzureCosmosDB</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.ContainerRegistry</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.EventHub</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.KeyVault</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.ServiceBus</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.Sql</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.Storage</span></code> and <code class="docutils literal notranslate"><span class="pre">Microsoft.Web</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.Subnet.virtual_network_name">
<code class="sig-name descname">virtual_network_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.Subnet.virtual_network_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the virtual network to which to attach the subnet. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.Subnet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address_prefix=None</em>, <em class="sig-param">delegations=None</em>, <em class="sig-param">enforce_private_link_endpoint_network_policies=None</em>, <em class="sig-param">enforce_private_link_service_network_policies=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_endpoints=None</em>, <em class="sig-param">virtual_network_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Subnet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Subnet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The address prefix to use for the subnet.</p></li>
<li><p><strong>delegations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">delegation</span></code> blocks as defined below.</p></li>
<li><p><strong>enforce_private_link_endpoint_network_policies</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or Disable network policies for the private link endpoint on the subnet. Default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>. Conflicts with enforce_private_link_service_network_policies.</p></li>
<li><p><strong>enforce_private_link_service_network_policies</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or Disable network policies for the private link service on the subnet. Default valule is <code class="docutils literal notranslate"><span class="pre">false</span></code>. Conflicts with <code class="docutils literal notranslate"><span class="pre">enforce_private_link_endpoint_network_policies</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the subnet. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the subnet. Changing this forces a new resource to be created.</p></li>
<li><p><strong>service_endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of Service endpoints to associate with the subnet. Possible values include: <code class="docutils literal notranslate"><span class="pre">Microsoft.AzureActiveDirectory</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.AzureCosmosDB</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.ContainerRegistry</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.EventHub</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.KeyVault</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.ServiceBus</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.Sql</span></code>, <code class="docutils literal notranslate"><span class="pre">Microsoft.Storage</span></code> and <code class="docutils literal notranslate"><span class="pre">Microsoft.Web</span></code>.</p></li>
<li><p><strong>virtual_network_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual network to which to attach the subnet. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>delegations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the subnet. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceDelegation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">actions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the subnet. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.Subnet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Subnet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.Subnet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.Subnet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.SubnetNatGatewayAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">SubnetNatGatewayAssociation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">nat_gateway_id=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.SubnetNatGatewayAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates a NAT Gateway with a Subnet within a Virtual Network.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/subnet_nat_gateway_association.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/subnet_nat_gateway_association.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>nat_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the NAT Gateway which should be associated with the Subnet. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.SubnetNatGatewayAssociation.nat_gateway_id">
<code class="sig-name descname">nat_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.SubnetNatGatewayAssociation.nat_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the NAT Gateway which should be associated with the Subnet. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.SubnetNatGatewayAssociation.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.SubnetNatGatewayAssociation.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Subnet. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.SubnetNatGatewayAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">nat_gateway_id=None</em>, <em class="sig-param">subnet_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.SubnetNatGatewayAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SubnetNatGatewayAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>nat_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the NAT Gateway which should be associated with the Subnet. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.SubnetNatGatewayAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.SubnetNatGatewayAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.SubnetNatGatewayAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.SubnetNatGatewayAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.SubnetNetworkSecurityGroupAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">SubnetNetworkSecurityGroupAssociation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">network_security_group_id=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.SubnetNetworkSecurityGroupAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates a Network Security Group with a Subnet within a Virtual Network.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/subnet_network_security_group_association.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/subnet_network_security_group_association.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>network_security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Security Group which should be associated with the Subnet. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.SubnetNetworkSecurityGroupAssociation.network_security_group_id">
<code class="sig-name descname">network_security_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.SubnetNetworkSecurityGroupAssociation.network_security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Security Group which should be associated with the Subnet. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.SubnetNetworkSecurityGroupAssociation.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.SubnetNetworkSecurityGroupAssociation.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Subnet. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.SubnetNetworkSecurityGroupAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">network_security_group_id=None</em>, <em class="sig-param">subnet_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.SubnetNetworkSecurityGroupAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SubnetNetworkSecurityGroupAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>network_security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Security Group which should be associated with the Subnet. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.SubnetNetworkSecurityGroupAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.SubnetNetworkSecurityGroupAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.SubnetNetworkSecurityGroupAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.SubnetNetworkSecurityGroupAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.SubnetRouteTableAssociation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">SubnetRouteTableAssociation</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">route_table_id=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.SubnetRouteTableAssociation" title="Permalink to this definition">¶</a></dt>
<dd><p>Associates a Route Table with a Subnet within a Virtual Network.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/subnet_route_table_association.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/subnet_route_table_association.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Route Table which should be associated with the Subnet. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.SubnetRouteTableAssociation.route_table_id">
<code class="sig-name descname">route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.SubnetRouteTableAssociation.route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Route Table which should be associated with the Subnet. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.SubnetRouteTableAssociation.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.SubnetRouteTableAssociation.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Subnet. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.SubnetRouteTableAssociation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">route_table_id=None</em>, <em class="sig-param">subnet_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.SubnetRouteTableAssociation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SubnetRouteTableAssociation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Route Table which should be associated with the Subnet. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.SubnetRouteTableAssociation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.SubnetRouteTableAssociation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.SubnetRouteTableAssociation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.SubnetRouteTableAssociation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.TrafficManagerEndpoint">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">TrafficManagerEndpoint</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">custom_headers=None</em>, <em class="sig-param">endpoint_location=None</em>, <em class="sig-param">endpoint_status=None</em>, <em class="sig-param">geo_mappings=None</em>, <em class="sig-param">min_child_endpoints=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">profile_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">subnets=None</em>, <em class="sig-param">target=None</em>, <em class="sig-param">target_resource_id=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">weight=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.TrafficManagerEndpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Traffic Manager Endpoint.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/traffic_manager_endpoint.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/traffic_manager_endpoint.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_headers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">custom_header</span></code> blocks as defined below</p></li>
<li><p><strong>endpoint_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure location of the Endpoint,
this must be specified for Profiles using the <code class="docutils literal notranslate"><span class="pre">Performance</span></code> routing method
if the Endpoint is of either type <code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code> or <code class="docutils literal notranslate"><span class="pre">externalEndpoints</span></code>.
For Endpoints of type <code class="docutils literal notranslate"><span class="pre">azureEndpoints</span></code> the value will be taken from the
location of the Azure target resource.</p></li>
<li><p><strong>endpoint_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the Endpoint, can be set to
either <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><strong>geo_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Geographic Regions used to distribute traffic, such as <code class="docutils literal notranslate"><span class="pre">WORLD</span></code>, <code class="docutils literal notranslate"><span class="pre">UK</span></code> or <code class="docutils literal notranslate"><span class="pre">DE</span></code>. The same location can’t be specified in two endpoints. <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/trafficmanager/geographichierarchies/getdefault">See the Geographic Hierarchies documentation for more information</a>.</p></li>
<li><p><strong>min_child_endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – This argument specifies the minimum number
of endpoints that must be ‘online’ in the child profile in order for the
parent profile to direct traffic to any of the endpoints in that child
profile. This argument only applies to Endpoints of type <code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code>
and defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Traffic Manager endpoint. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the priority of this Endpoint, this must be
specified for Profiles using the <code class="docutils literal notranslate"><span class="pre">Priority</span></code> traffic routing method. Supports
values between 1 and 1000, with no Endpoints sharing the same value. If
omitted the value will be computed in order of creation.</p></li>
<li><p><strong>profile_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Traffic Manager Profile to attach
create the Traffic Manager endpoint.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the Traffic Manager endpoint.</p></li>
<li><p><strong>subnets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">subnet</span></code> blocks as defined below</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FQDN DNS name of the target. This argument must be
provided for an endpoint of type <code class="docutils literal notranslate"><span class="pre">externalEndpoints</span></code>, for other types it
will be computed.</p></li>
<li><p><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource id of an Azure resource to
target. This argument must be provided for an endpoint of type
<code class="docutils literal notranslate"><span class="pre">azureEndpoints</span></code> or <code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Endpoint type, must be one of:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `azureEndpoints`
- `externalEndpoints`
- `nestedEndpoints`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies how much traffic should be distributed to this
endpoint, this must be specified for Profiles using the  <code class="docutils literal notranslate"><span class="pre">Weighted</span></code> traffic
routing method. Supports values between 1 and 1000.</p>
</dd>
</dl>
<p>The <strong>custom_headers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Traffic Manager endpoint. Changing this forces a
new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>subnets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">first</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">last</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerEndpoint.custom_headers">
<code class="sig-name descname">custom_headers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerEndpoint.custom_headers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">custom_header</span></code> blocks as defined below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Traffic Manager endpoint. Changing this forces a
new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerEndpoint.endpoint_location">
<code class="sig-name descname">endpoint_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerEndpoint.endpoint_location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure location of the Endpoint,
this must be specified for Profiles using the <code class="docutils literal notranslate"><span class="pre">Performance</span></code> routing method
if the Endpoint is of either type <code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code> or <code class="docutils literal notranslate"><span class="pre">externalEndpoints</span></code>.
For Endpoints of type <code class="docutils literal notranslate"><span class="pre">azureEndpoints</span></code> the value will be taken from the
location of the Azure target resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerEndpoint.endpoint_status">
<code class="sig-name descname">endpoint_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerEndpoint.endpoint_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the Endpoint, can be set to
either <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerEndpoint.geo_mappings">
<code class="sig-name descname">geo_mappings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerEndpoint.geo_mappings" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Geographic Regions used to distribute traffic, such as <code class="docutils literal notranslate"><span class="pre">WORLD</span></code>, <code class="docutils literal notranslate"><span class="pre">UK</span></code> or <code class="docutils literal notranslate"><span class="pre">DE</span></code>. The same location can’t be specified in two endpoints. <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/trafficmanager/geographichierarchies/getdefault">See the Geographic Hierarchies documentation for more information</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerEndpoint.min_child_endpoints">
<code class="sig-name descname">min_child_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerEndpoint.min_child_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>This argument specifies the minimum number
of endpoints that must be ‘online’ in the child profile in order for the
parent profile to direct traffic to any of the endpoints in that child
profile. This argument only applies to Endpoints of type <code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code>
and defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerEndpoint.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerEndpoint.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Traffic Manager endpoint. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerEndpoint.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerEndpoint.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the priority of this Endpoint, this must be
specified for Profiles using the <code class="docutils literal notranslate"><span class="pre">Priority</span></code> traffic routing method. Supports
values between 1 and 1000, with no Endpoints sharing the same value. If
omitted the value will be computed in order of creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerEndpoint.profile_name">
<code class="sig-name descname">profile_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerEndpoint.profile_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Traffic Manager Profile to attach
create the Traffic Manager endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerEndpoint.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerEndpoint.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the Traffic Manager endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerEndpoint.subnets">
<code class="sig-name descname">subnets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerEndpoint.subnets" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">subnet</span></code> blocks as defined below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">first</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">last</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerEndpoint.target">
<code class="sig-name descname">target</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerEndpoint.target" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN DNS name of the target. This argument must be
provided for an endpoint of type <code class="docutils literal notranslate"><span class="pre">externalEndpoints</span></code>, for other types it
will be computed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerEndpoint.target_resource_id">
<code class="sig-name descname">target_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerEndpoint.target_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource id of an Azure resource to
target. This argument must be provided for an endpoint of type
<code class="docutils literal notranslate"><span class="pre">azureEndpoints</span></code> or <code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerEndpoint.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerEndpoint.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Endpoint type, must be one of:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">azureEndpoints</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">externalEndpoints</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerEndpoint.weight">
<code class="sig-name descname">weight</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerEndpoint.weight" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies how much traffic should be distributed to this
endpoint, this must be specified for Profiles using the  <code class="docutils literal notranslate"><span class="pre">Weighted</span></code> traffic
routing method. Supports values between 1 and 1000.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.TrafficManagerEndpoint.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">custom_headers=None</em>, <em class="sig-param">endpoint_location=None</em>, <em class="sig-param">endpoint_monitor_status=None</em>, <em class="sig-param">endpoint_status=None</em>, <em class="sig-param">geo_mappings=None</em>, <em class="sig-param">min_child_endpoints=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">profile_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">subnets=None</em>, <em class="sig-param">target=None</em>, <em class="sig-param">target_resource_id=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">weight=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.TrafficManagerEndpoint.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TrafficManagerEndpoint resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_headers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">custom_header</span></code> blocks as defined below</p></li>
<li><p><strong>endpoint_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure location of the Endpoint,
this must be specified for Profiles using the <code class="docutils literal notranslate"><span class="pre">Performance</span></code> routing method
if the Endpoint is of either type <code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code> or <code class="docutils literal notranslate"><span class="pre">externalEndpoints</span></code>.
For Endpoints of type <code class="docutils literal notranslate"><span class="pre">azureEndpoints</span></code> the value will be taken from the
location of the Azure target resource.</p></li>
<li><p><strong>endpoint_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the Endpoint, can be set to
either <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><strong>geo_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of Geographic Regions used to distribute traffic, such as <code class="docutils literal notranslate"><span class="pre">WORLD</span></code>, <code class="docutils literal notranslate"><span class="pre">UK</span></code> or <code class="docutils literal notranslate"><span class="pre">DE</span></code>. The same location can’t be specified in two endpoints. <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/trafficmanager/geographichierarchies/getdefault">See the Geographic Hierarchies documentation for more information</a>.</p>
</p></li>
<li><p><strong>min_child_endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – This argument specifies the minimum number
of endpoints that must be ‘online’ in the child profile in order for the
parent profile to direct traffic to any of the endpoints in that child
profile. This argument only applies to Endpoints of type <code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code>
and defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Traffic Manager endpoint. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the priority of this Endpoint, this must be
specified for Profiles using the <code class="docutils literal notranslate"><span class="pre">Priority</span></code> traffic routing method. Supports
values between 1 and 1000, with no Endpoints sharing the same value. If
omitted the value will be computed in order of creation.</p></li>
<li><p><strong>profile_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Traffic Manager Profile to attach
create the Traffic Manager endpoint.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the Traffic Manager endpoint.</p></li>
<li><p><strong>subnets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">subnet</span></code> blocks as defined below</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FQDN DNS name of the target. This argument must be
provided for an endpoint of type <code class="docutils literal notranslate"><span class="pre">externalEndpoints</span></code>, for other types it
will be computed.</p></li>
<li><p><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource id of an Azure resource to
target. This argument must be provided for an endpoint of type
<code class="docutils literal notranslate"><span class="pre">azureEndpoints</span></code> or <code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Endpoint type, must be one of:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `azureEndpoints`
- `externalEndpoints`
- `nestedEndpoints`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies how much traffic should be distributed to this
endpoint, this must be specified for Profiles using the  <code class="docutils literal notranslate"><span class="pre">Weighted</span></code> traffic
routing method. Supports values between 1 and 1000.</p>
</dd>
</dl>
<p>The <strong>custom_headers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Traffic Manager endpoint. Changing this forces a
new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>subnets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">first</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">last</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.TrafficManagerEndpoint.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.TrafficManagerEndpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.TrafficManagerEndpoint.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.TrafficManagerEndpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.TrafficManagerProfile">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">TrafficManagerProfile</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dns_config=None</em>, <em class="sig-param">monitor_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">profile_status=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">traffic_routing_method=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.TrafficManagerProfile" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Traffic Manager Profile to which multiple endpoints can be attached.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/traffic_manager_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/traffic_manager_profile.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dns_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – This block specifies the DNS configuration of the Profile, it supports the fields documented below.</p></li>
<li><p><strong>monitor_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – This block specifies the Endpoint monitoring configuration for the Profile, it supports the fields documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Traffic Manager profile. Changing this forces a new resource to be created.</p></li>
<li><p><strong>profile_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the profile, can be set to either <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Traffic Manager profile.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>traffic_routing_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the algorithm used to route traffic, possible values are:</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dns_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">relativeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>monitor_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">expectedStatusCodeRanges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval_in_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">toleratedNumberOfFailures</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerProfile.dns_config">
<code class="sig-name descname">dns_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerProfile.dns_config" title="Permalink to this definition">¶</a></dt>
<dd><p>This block specifies the DNS configuration of the Profile, it supports the fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">relativeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerProfile.fqdn">
<code class="sig-name descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerProfile.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the created Profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerProfile.monitor_config">
<code class="sig-name descname">monitor_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerProfile.monitor_config" title="Permalink to this definition">¶</a></dt>
<dd><p>This block specifies the Endpoint monitoring configuration for the Profile, it supports the fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">expectedStatusCodeRanges</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval_in_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">toleratedNumberOfFailures</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerProfile.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerProfile.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Traffic Manager profile. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerProfile.profile_status">
<code class="sig-name descname">profile_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerProfile.profile_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the profile, can be set to either <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerProfile.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerProfile.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Traffic Manager profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerProfile.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerProfile.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.TrafficManagerProfile.traffic_routing_method">
<code class="sig-name descname">traffic_routing_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.TrafficManagerProfile.traffic_routing_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the algorithm used to route traffic, possible values are:</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.TrafficManagerProfile.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dns_config=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">monitor_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">profile_status=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">traffic_routing_method=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.TrafficManagerProfile.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TrafficManagerProfile resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dns_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – This block specifies the DNS configuration of the Profile, it supports the fields documented below.</p></li>
<li><p><strong>fqdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FQDN of the created Profile.</p></li>
<li><p><strong>monitor_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – This block specifies the Endpoint monitoring configuration for the Profile, it supports the fields documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Traffic Manager profile. Changing this forces a new resource to be created.</p></li>
<li><p><strong>profile_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the profile, can be set to either <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Traffic Manager profile.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>traffic_routing_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the algorithm used to route traffic, possible values are:</p></li>
</ul>
</dd>
</dl>
<p>The <strong>dns_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">relativeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>monitor_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">expectedStatusCodeRanges</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interval_in_seconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutInSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">toleratedNumberOfFailures</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.TrafficManagerProfile.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.TrafficManagerProfile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.TrafficManagerProfile.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.TrafficManagerProfile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualHub">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">VirtualHub</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address_prefix=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">routes=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_wan_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualHub" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Virtual Hub within a Virtual WAN.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_hub.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_hub.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Address Prefix which should be used for this Virtual Hub.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the Virtual Hub should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Virtual Hub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group where the Virtual Hub should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>routes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">route</span></code> blocks as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Virtual Hub.</p></li>
<li><p><strong>virtual_wan_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Virtual WAN within which the Virtual Hub should be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>routes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">addressPrefixes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nextHopIpAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.VirtualHub.address_prefix">
<code class="sig-name descname">address_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualHub.address_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The Address Prefix which should be used for this Virtual Hub.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualHub.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualHub.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the Virtual Hub should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualHub.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualHub.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Virtual Hub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualHub.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualHub.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group where the Virtual Hub should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualHub.routes">
<code class="sig-name descname">routes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualHub.routes" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">route</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">addressPrefixes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nextHopIpAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualHub.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualHub.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the Virtual Hub.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualHub.virtual_wan_id">
<code class="sig-name descname">virtual_wan_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualHub.virtual_wan_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a Virtual WAN within which the Virtual Hub should be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VirtualHub.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address_prefix=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">routes=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_wan_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualHub.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualHub resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Address Prefix which should be used for this Virtual Hub.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the Virtual Hub should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Virtual Hub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group where the Virtual Hub should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>routes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">route</span></code> blocks as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Virtual Hub.</p></li>
<li><p><strong>virtual_wan_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Virtual WAN within which the Virtual Hub should be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>routes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">addressPrefixes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nextHopIpAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VirtualHub.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualHub.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualHub.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualHub.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualHubConnection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">VirtualHubConnection</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">hub_to_vitual_network_traffic_allowed=None</em>, <em class="sig-param">internet_security_enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">remote_virtual_network_id=None</em>, <em class="sig-param">virtual_hub_id=None</em>, <em class="sig-param">vitual_network_to_hub_gateways_traffic_allowed=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualHubConnection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Connection for a Virtual Hub.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_hub_connection.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_hub_connection.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>hub_to_vitual_network_traffic_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the Virtual Hub traffic allowed to transit via the Remote Virtual Network? Changing this forces a new resource to be created.</p></li>
<li><p><strong>internet_security_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Internet Security be enabled to secure internet traffic? Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name which should be used for this Connection, which must be unique within the Virtual Hub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>remote_virtual_network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Network which the Virtual Hub should be connected to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>virtual_hub_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Hub within which this connection should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>vitual_network_to_hub_gateways_traffic_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is Remote Virtual Network traffic allowed to transit the Hub’s Virtual Network Gateway’s? Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.VirtualHubConnection.hub_to_vitual_network_traffic_allowed">
<code class="sig-name descname">hub_to_vitual_network_traffic_allowed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualHubConnection.hub_to_vitual_network_traffic_allowed" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the Virtual Hub traffic allowed to transit via the Remote Virtual Network? Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualHubConnection.internet_security_enabled">
<code class="sig-name descname">internet_security_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualHubConnection.internet_security_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should Internet Security be enabled to secure internet traffic? Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualHubConnection.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualHubConnection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name which should be used for this Connection, which must be unique within the Virtual Hub. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualHubConnection.remote_virtual_network_id">
<code class="sig-name descname">remote_virtual_network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualHubConnection.remote_virtual_network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Virtual Network which the Virtual Hub should be connected to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualHubConnection.virtual_hub_id">
<code class="sig-name descname">virtual_hub_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualHubConnection.virtual_hub_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Virtual Hub within which this connection should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualHubConnection.vitual_network_to_hub_gateways_traffic_allowed">
<code class="sig-name descname">vitual_network_to_hub_gateways_traffic_allowed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualHubConnection.vitual_network_to_hub_gateways_traffic_allowed" title="Permalink to this definition">¶</a></dt>
<dd><p>Is Remote Virtual Network traffic allowed to transit the Hub’s Virtual Network Gateway’s? Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VirtualHubConnection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">hub_to_vitual_network_traffic_allowed=None</em>, <em class="sig-param">internet_security_enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">remote_virtual_network_id=None</em>, <em class="sig-param">virtual_hub_id=None</em>, <em class="sig-param">vitual_network_to_hub_gateways_traffic_allowed=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualHubConnection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualHubConnection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>hub_to_vitual_network_traffic_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the Virtual Hub traffic allowed to transit via the Remote Virtual Network? Changing this forces a new resource to be created.</p></li>
<li><p><strong>internet_security_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Internet Security be enabled to secure internet traffic? Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name which should be used for this Connection, which must be unique within the Virtual Hub. Changing this forces a new resource to be created.</p></li>
<li><p><strong>remote_virtual_network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Network which the Virtual Hub should be connected to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>virtual_hub_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Hub within which this connection should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>vitual_network_to_hub_gateways_traffic_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is Remote Virtual Network traffic allowed to transit the Hub’s Virtual Network Gateway’s? Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VirtualHubConnection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualHubConnection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualHubConnection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualHubConnection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualNetwork">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">VirtualNetwork</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address_spaces=None</em>, <em class="sig-param">ddos_protection_plan=None</em>, <em class="sig-param">dns_servers=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">subnets=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a virtual network including any configured subnets. Each subnet can
optionally be configured with a security group to be associated with the subnet.</p>
<blockquote>
<div><p><strong>NOTE on Virtual Networks and Subnet’s:</strong> This provider currently
provides both a standalone Subnet resource, and allows for Subnets to be defined in-line within the Virtual Network resource.
At this time you cannot use a Virtual Network with in-line Subnets in conjunction with any Subnet resources. Doing so will cause a conflict of Subnet configurations and will overwrite Subnet’s.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_network.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_network.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_spaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The address space that is used the virtual
network. You can supply more than one address space. Changing this forces
a new resource to be created.</p></li>
<li><p><strong>ddos_protection_plan</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">ddos_protection_plan</span></code> block as documented below.</p></li>
<li><p><strong>dns_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IP addresses of DNS servers</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location/region where the virtual network is
created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual network. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the virtual network.</p></li>
<li><p><strong>subnets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Can be specified multiple times to define multiple
subnets. Each <code class="docutils literal notranslate"><span class="pre">subnet</span></code> block supports fields documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ddos_protection_plan</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of this subnet.</p></li>
</ul>
<p>The <strong>subnets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of this subnet.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the virtual network. Changing this forces a
new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetwork.address_spaces">
<code class="sig-name descname">address_spaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.address_spaces" title="Permalink to this definition">¶</a></dt>
<dd><p>The address space that is used the virtual
network. You can supply more than one address space. Changing this forces
a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetwork.ddos_protection_plan">
<code class="sig-name descname">ddos_protection_plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.ddos_protection_plan" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">ddos_protection_plan</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of this subnet.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetwork.dns_servers">
<code class="sig-name descname">dns_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.dns_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of IP addresses of DNS servers</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetwork.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location/region where the virtual network is
created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetwork.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the virtual network. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetwork.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the virtual network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetwork.subnets">
<code class="sig-name descname">subnets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.subnets" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be specified multiple times to define multiple
subnets. Each <code class="docutils literal notranslate"><span class="pre">subnet</span></code> block supports fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of this subnet.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the virtual network. Changing this forces a
new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetwork.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VirtualNetwork.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">address_spaces=None</em>, <em class="sig-param">ddos_protection_plan=None</em>, <em class="sig-param">dns_servers=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">subnets=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualNetwork resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>address_spaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The address space that is used the virtual
network. You can supply more than one address space. Changing this forces
a new resource to be created.</p></li>
<li><p><strong>ddos_protection_plan</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">ddos_protection_plan</span></code> block as documented below.</p></li>
<li><p><strong>dns_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of IP addresses of DNS servers</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location/region where the virtual network is
created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual network. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the virtual network.</p></li>
<li><p><strong>subnets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Can be specified multiple times to define multiple
subnets. Each <code class="docutils literal notranslate"><span class="pre">subnet</span></code> block supports fields documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ddos_protection_plan</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of this subnet.</p></li>
</ul>
<p>The <strong>subnets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of this subnet.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the virtual network. Changing this forces a
new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">securityGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VirtualNetwork.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualNetwork.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetwork.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualNetworkGateway">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">VirtualNetworkGateway</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">active_active=None</em>, <em class="sig-param">bgp_settings=None</em>, <em class="sig-param">default_local_network_gateway_id=None</em>, <em class="sig-param">enable_bgp=None</em>, <em class="sig-param">generation=None</em>, <em class="sig-param">ip_configurations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">vpn_client_configuration=None</em>, <em class="sig-param">vpn_type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Virtual Network Gateway to establish secure, cross-premises connectivity.</p>
<blockquote>
<div><p><strong>Note:</strong> Please be aware that provisioning a Virtual Network Gateway takes a long time (between 30 minutes and 1 hour)</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_network_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_network_gateway.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active_active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a <code class="docutils literal notranslate"><span class="pre">HighPerformance</span></code> or an
<code class="docutils literal notranslate"><span class="pre">UltraPerformance</span></code> sku. If <code class="docutils literal notranslate"><span class="pre">false</span></code>, an active-standby gateway will be created.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>default_local_network_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (<em>forced tunneling</em>). Refer to the
<a class="reference external" href="https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm">Azure documentation on forced tunneling</a>.
If not specified, forced tunneling is disabled.</p>
</p></li>
<li><p><strong>enable_bgp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>generation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Generation of the Virtual Network gateway. Possible values include <code class="docutils literal notranslate"><span class="pre">Generation1</span></code>, <code class="docutils literal notranslate"><span class="pre">Generation2</span></code> or <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p></li>
<li><p><strong>ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or two <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> blocks documented below.
An active-standby gateway requires exactly one <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> block whereas
an active-active gateway requires exactly two <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> blocks.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Configuration of the size and capacity of the virtual network
gateway. Valid options are <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">HighPerformance</span></code>, <code class="docutils literal notranslate"><span class="pre">UltraPerformance</span></code>,
<code class="docutils literal notranslate"><span class="pre">ErGw1AZ</span></code>, <code class="docutils literal notranslate"><span class="pre">ErGw2AZ</span></code>, <code class="docutils literal notranslate"><span class="pre">ErGw3AZ</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw1</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw2</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw3</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw4</span></code>,<code class="docutils literal notranslate"><span class="pre">VpnGw5</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw1AZ</span></code>,
<code class="docutils literal notranslate"><span class="pre">VpnGw2AZ</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw3AZ</span></code>,<code class="docutils literal notranslate"><span class="pre">VpnGw4AZ</span></code> and <code class="docutils literal notranslate"><span class="pre">VpnGw5AZ</span></code> and depend on the <code class="docutils literal notranslate"><span class="pre">type</span></code>, <code class="docutils literal notranslate"><span class="pre">vpn_type</span></code> and
<code class="docutils literal notranslate"><span class="pre">generation</span></code> arguments.
A <code class="docutils literal notranslate"><span class="pre">PolicyBased</span></code> gateway only supports the <code class="docutils literal notranslate"><span class="pre">Basic</span></code> sku. Further, the <code class="docutils literal notranslate"><span class="pre">UltraPerformance</span></code>
sku is only supported by an <code class="docutils literal notranslate"><span class="pre">ExpressRoute</span></code> gateway.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the Virtual Network Gateway. Valid options are
<code class="docutils literal notranslate"><span class="pre">Vpn</span></code> or <code class="docutils literal notranslate"><span class="pre">ExpressRoute</span></code>. Changing the type forces a new resource to be created.</p></li>
<li><p><strong>vpn_client_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">vpn_client_configuration</span></code> block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.</p></li>
<li><p><strong>vpn_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The routing type of the Virtual Network Gateway. Valid
options are <code class="docutils literal notranslate"><span class="pre">RouteBased</span></code> or <code class="docutils literal notranslate"><span class="pre">PolicyBased</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">RouteBased</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bgp_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">asn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">peerWeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">peeringAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ip_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddressAllocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>vpn_client_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address_spaces</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">radiusServerAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">radiusServerSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revokedCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicCertData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpnClientProtocols</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.active_active">
<code class="sig-name descname">active_active</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.active_active" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a <code class="docutils literal notranslate"><span class="pre">HighPerformance</span></code> or an
<code class="docutils literal notranslate"><span class="pre">UltraPerformance</span></code> sku. If <code class="docutils literal notranslate"><span class="pre">false</span></code>, an active-standby gateway will be created.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.default_local_network_gateway_id">
<code class="sig-name descname">default_local_network_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.default_local_network_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (<em>forced tunneling</em>). Refer to the
<a class="reference external" href="https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm">Azure documentation on forced tunneling</a>.
If not specified, forced tunneling is disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.enable_bgp">
<code class="sig-name descname">enable_bgp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.enable_bgp" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.generation">
<code class="sig-name descname">generation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.generation" title="Permalink to this definition">¶</a></dt>
<dd><p>The Generation of the Virtual Network gateway. Possible values include <code class="docutils literal notranslate"><span class="pre">Generation1</span></code>, <code class="docutils literal notranslate"><span class="pre">Generation2</span></code> or <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.ip_configurations">
<code class="sig-name descname">ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or two <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> blocks documented below.
An active-standby gateway requires exactly one <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> block whereas
an active-active gateway requires exactly two <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> blocks.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddressAllocation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration of the size and capacity of the virtual network
gateway. Valid options are <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">HighPerformance</span></code>, <code class="docutils literal notranslate"><span class="pre">UltraPerformance</span></code>,
<code class="docutils literal notranslate"><span class="pre">ErGw1AZ</span></code>, <code class="docutils literal notranslate"><span class="pre">ErGw2AZ</span></code>, <code class="docutils literal notranslate"><span class="pre">ErGw3AZ</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw1</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw2</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw3</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw4</span></code>,<code class="docutils literal notranslate"><span class="pre">VpnGw5</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw1AZ</span></code>,
<code class="docutils literal notranslate"><span class="pre">VpnGw2AZ</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw3AZ</span></code>,<code class="docutils literal notranslate"><span class="pre">VpnGw4AZ</span></code> and <code class="docutils literal notranslate"><span class="pre">VpnGw5AZ</span></code> and depend on the <code class="docutils literal notranslate"><span class="pre">type</span></code>, <code class="docutils literal notranslate"><span class="pre">vpn_type</span></code> and
<code class="docutils literal notranslate"><span class="pre">generation</span></code> arguments.
A <code class="docutils literal notranslate"><span class="pre">PolicyBased</span></code> gateway only supports the <code class="docutils literal notranslate"><span class="pre">Basic</span></code> sku. Further, the <code class="docutils literal notranslate"><span class="pre">UltraPerformance</span></code>
sku is only supported by an <code class="docutils literal notranslate"><span class="pre">ExpressRoute</span></code> gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the Virtual Network Gateway. Valid options are
<code class="docutils literal notranslate"><span class="pre">Vpn</span></code> or <code class="docutils literal notranslate"><span class="pre">ExpressRoute</span></code>. Changing the type forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.vpn_client_configuration">
<code class="sig-name descname">vpn_client_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.vpn_client_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">vpn_client_configuration</span></code> block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address_spaces</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">radiusServerAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">radiusServerSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revokedCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicCertData</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpnClientProtocols</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGateway.vpn_type">
<code class="sig-name descname">vpn_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.vpn_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The routing type of the Virtual Network Gateway. Valid
options are <code class="docutils literal notranslate"><span class="pre">RouteBased</span></code> or <code class="docutils literal notranslate"><span class="pre">PolicyBased</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">RouteBased</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VirtualNetworkGateway.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">active_active=None</em>, <em class="sig-param">bgp_settings=None</em>, <em class="sig-param">default_local_network_gateway_id=None</em>, <em class="sig-param">enable_bgp=None</em>, <em class="sig-param">generation=None</em>, <em class="sig-param">ip_configurations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">vpn_client_configuration=None</em>, <em class="sig-param">vpn_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualNetworkGateway resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active_active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, an active-active Virtual Network Gateway
will be created. An active-active gateway requires a <code class="docutils literal notranslate"><span class="pre">HighPerformance</span></code> or an
<code class="docutils literal notranslate"><span class="pre">UltraPerformance</span></code> sku. If <code class="docutils literal notranslate"><span class="pre">false</span></code>, an active-standby gateway will be created.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>default_local_network_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The ID of the local network gateway
through which outbound Internet traffic from the virtual network in which the
gateway is created will be routed (<em>forced tunneling</em>). Refer to the
<a class="reference external" href="https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-forced-tunneling-rm">Azure documentation on forced tunneling</a>.
If not specified, forced tunneling is disabled.</p>
</p></li>
<li><p><strong>enable_bgp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, BGP (Border Gateway Protocol) will be enabled
for this Virtual Network Gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>generation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Generation of the Virtual Network gateway. Possible values include <code class="docutils literal notranslate"><span class="pre">Generation1</span></code>, <code class="docutils literal notranslate"><span class="pre">Generation2</span></code> or <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p></li>
<li><p><strong>ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or two <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> blocks documented below.
An active-standby gateway requires exactly one <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> block whereas
an active-active gateway requires exactly two <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> blocks.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location/region where the Virtual Network Gateway is
located. Changing the location/region forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the Virtual Network Gateway. Changing the resource group name forces
a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Configuration of the size and capacity of the virtual network
gateway. Valid options are <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">HighPerformance</span></code>, <code class="docutils literal notranslate"><span class="pre">UltraPerformance</span></code>,
<code class="docutils literal notranslate"><span class="pre">ErGw1AZ</span></code>, <code class="docutils literal notranslate"><span class="pre">ErGw2AZ</span></code>, <code class="docutils literal notranslate"><span class="pre">ErGw3AZ</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw1</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw2</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw3</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw4</span></code>,<code class="docutils literal notranslate"><span class="pre">VpnGw5</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw1AZ</span></code>,
<code class="docutils literal notranslate"><span class="pre">VpnGw2AZ</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw3AZ</span></code>,<code class="docutils literal notranslate"><span class="pre">VpnGw4AZ</span></code> and <code class="docutils literal notranslate"><span class="pre">VpnGw5AZ</span></code> and depend on the <code class="docutils literal notranslate"><span class="pre">type</span></code>, <code class="docutils literal notranslate"><span class="pre">vpn_type</span></code> and
<code class="docutils literal notranslate"><span class="pre">generation</span></code> arguments.
A <code class="docutils literal notranslate"><span class="pre">PolicyBased</span></code> gateway only supports the <code class="docutils literal notranslate"><span class="pre">Basic</span></code> sku. Further, the <code class="docutils literal notranslate"><span class="pre">UltraPerformance</span></code>
sku is only supported by an <code class="docutils literal notranslate"><span class="pre">ExpressRoute</span></code> gateway.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the Virtual Network Gateway. Valid options are
<code class="docutils literal notranslate"><span class="pre">Vpn</span></code> or <code class="docutils literal notranslate"><span class="pre">ExpressRoute</span></code>. Changing the type forces a new resource to be created.</p></li>
<li><p><strong>vpn_client_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">vpn_client_configuration</span></code> block which
is documented below. In this block the Virtual Network Gateway can be configured
to accept IPSec point-to-site connections.</p></li>
<li><p><strong>vpn_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The routing type of the Virtual Network Gateway. Valid
options are <code class="docutils literal notranslate"><span class="pre">RouteBased</span></code> or <code class="docutils literal notranslate"><span class="pre">PolicyBased</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">RouteBased</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bgp_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">asn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">peerWeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">peeringAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ip_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddressAllocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>vpn_client_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address_spaces</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">radiusServerAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">radiusServerSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">revokedCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">rootCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Virtual Network Gateway. Changing the name
forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicCertData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpnClientProtocols</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VirtualNetworkGateway.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualNetworkGateway.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">VirtualNetworkGatewayConnection</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">authorization_key=None</em>, <em class="sig-param">connection_protocol=None</em>, <em class="sig-param">enable_bgp=None</em>, <em class="sig-param">express_route_circuit_id=None</em>, <em class="sig-param">express_route_gateway_bypass=None</em>, <em class="sig-param">ipsec_policy=None</em>, <em class="sig-param">local_network_gateway_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">peer_virtual_network_gateway_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">routing_weight=None</em>, <em class="sig-param">shared_key=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">use_policy_based_traffic_selectors=None</em>, <em class="sig-param">virtual_network_gateway_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a connection in an existing Virtual Network Gateway.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_network_gateway_connection.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_network_gateway_connection.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorization_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.</p></li>
<li><p><strong>connection_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IKE protocol version to use. Possible
values are <code class="docutils literal notranslate"><span class="pre">IKEv1</span></code> and <code class="docutils literal notranslate"><span class="pre">IKEv2</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IKEv2</span></code>.
Changing this value will force a resource to be created.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>&gt; **Note**: Only valid for `IPSec` connections on virtual network gateways with SKU `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw1AZ`, `VpnGw2AZ` or `VpnGw3AZ`.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>enable_bgp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>express_route_circuit_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">ExpressRoute</span></code>).
The Express Route Circuit can be in the same or in a different subscription.</p></li>
<li><p><strong>express_route_gateway_bypass</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, data packets will bypass ExpressRoute Gateway for data forwarding This is only valid for ExpressRoute connections.</p></li>
<li><p><strong>ipsec_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">ipsec_policy</span></code> block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to <a class="reference external" href="https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell">the relevant section in the Azure documentation</a>.</p></li>
<li><p><strong>local_network_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the local network gateway
when creating Site-to-Site connection (i.e. when <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">IPsec</span></code>).</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location/region where the connection is
located. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the connection. Changing the name forces a
new resource to be created.</p></li>
<li><p><strong>peer_virtual_network_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when <code class="docutils literal notranslate"><span class="pre">type</span></code>
is <code class="docutils literal notranslate"><span class="pre">Vnet2Vnet</span></code>). The peer Virtual Network Gateway can be in the same or
in a different subscription.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.</p></li>
<li><p><strong>routing_weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The routing weight. Defaults to <code class="docutils literal notranslate"><span class="pre">10</span></code>.</p></li>
<li><p><strong>shared_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of connection. Valid options are <code class="docutils literal notranslate"><span class="pre">IPsec</span></code>
(Site-to-Site), <code class="docutils literal notranslate"><span class="pre">ExpressRoute</span></code> (ExpressRoute), and <code class="docutils literal notranslate"><span class="pre">Vnet2Vnet</span></code> (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.</p></li>
<li><p><strong>use_policy_based_traffic_selectors</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an <code class="docutils literal notranslate"><span class="pre">ipsec_policy</span></code> block. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>virtual_network_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ipsec_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dhGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeIntegrity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecIntegrity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pfsGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">saDatasize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">saLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.authorization_key">
<code class="sig-name descname">authorization_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.authorization_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.connection_protocol">
<code class="sig-name descname">connection_protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.connection_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The IKE protocol version to use. Possible
values are <code class="docutils literal notranslate"><span class="pre">IKEv1</span></code> and <code class="docutils literal notranslate"><span class="pre">IKEv2</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IKEv2</span></code>.
Changing this value will force a resource to be created.</p>
<blockquote>
<div><p><strong>Note</strong>: Only valid for <code class="docutils literal notranslate"><span class="pre">IPSec</span></code> connections on virtual network gateways with SKU <code class="docutils literal notranslate"><span class="pre">VpnGw1</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw2</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw3</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw1AZ</span></code>, <code class="docutils literal notranslate"><span class="pre">VpnGw2AZ</span></code> or <code class="docutils literal notranslate"><span class="pre">VpnGw3AZ</span></code>.</p>
</div></blockquote>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.enable_bgp">
<code class="sig-name descname">enable_bgp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.enable_bgp" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.express_route_circuit_id">
<code class="sig-name descname">express_route_circuit_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.express_route_circuit_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">ExpressRoute</span></code>).
The Express Route Circuit can be in the same or in a different subscription.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.express_route_gateway_bypass">
<code class="sig-name descname">express_route_gateway_bypass</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.express_route_gateway_bypass" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, data packets will bypass ExpressRoute Gateway for data forwarding This is only valid for ExpressRoute connections.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.ipsec_policy">
<code class="sig-name descname">ipsec_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.ipsec_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">ipsec_policy</span></code> block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to <a class="reference external" href="https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell">the relevant section in the Azure documentation</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dhGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeIntegrity</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecIntegrity</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pfsGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">saDatasize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">saLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.local_network_gateway_id">
<code class="sig-name descname">local_network_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.local_network_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the local network gateway
when creating Site-to-Site connection (i.e. when <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">IPsec</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location/region where the connection is
located. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the connection. Changing the name forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.peer_virtual_network_gateway_id">
<code class="sig-name descname">peer_virtual_network_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.peer_virtual_network_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when <code class="docutils literal notranslate"><span class="pre">type</span></code>
is <code class="docutils literal notranslate"><span class="pre">Vnet2Vnet</span></code>). The peer Virtual Network Gateway can be in the same or
in a different subscription.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.routing_weight">
<code class="sig-name descname">routing_weight</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.routing_weight" title="Permalink to this definition">¶</a></dt>
<dd><p>The routing weight. Defaults to <code class="docutils literal notranslate"><span class="pre">10</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.shared_key">
<code class="sig-name descname">shared_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.shared_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of connection. Valid options are <code class="docutils literal notranslate"><span class="pre">IPsec</span></code>
(Site-to-Site), <code class="docutils literal notranslate"><span class="pre">ExpressRoute</span></code> (ExpressRoute), and <code class="docutils literal notranslate"><span class="pre">Vnet2Vnet</span></code> (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.use_policy_based_traffic_selectors">
<code class="sig-name descname">use_policy_based_traffic_selectors</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.use_policy_based_traffic_selectors" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an <code class="docutils literal notranslate"><span class="pre">ipsec_policy</span></code> block. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.virtual_network_gateway_id">
<code class="sig-name descname">virtual_network_gateway_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.virtual_network_gateway_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">authorization_key=None</em>, <em class="sig-param">connection_protocol=None</em>, <em class="sig-param">enable_bgp=None</em>, <em class="sig-param">express_route_circuit_id=None</em>, <em class="sig-param">express_route_gateway_bypass=None</em>, <em class="sig-param">ipsec_policy=None</em>, <em class="sig-param">local_network_gateway_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">peer_virtual_network_gateway_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">routing_weight=None</em>, <em class="sig-param">shared_key=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">use_policy_based_traffic_selectors=None</em>, <em class="sig-param">virtual_network_gateway_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualNetworkGatewayConnection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorization_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authorization key associated with the
Express Route Circuit. This field is required only if the type is an
ExpressRoute connection.</p></li>
<li><p><strong>connection_protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IKE protocol version to use. Possible
values are <code class="docutils literal notranslate"><span class="pre">IKEv1</span></code> and <code class="docutils literal notranslate"><span class="pre">IKEv2</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IKEv2</span></code>.
Changing this value will force a resource to be created.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>&gt; **Note**: Only valid for `IPSec` connections on virtual network gateways with SKU `VpnGw1`, `VpnGw2`, `VpnGw3`, `VpnGw1AZ`, `VpnGw2AZ` or `VpnGw3AZ`.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>enable_bgp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, BGP (Border Gateway Protocol) is enabled
for this connection. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>express_route_circuit_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Express Route Circuit
when creating an ExpressRoute connection (i.e. when <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">ExpressRoute</span></code>).
The Express Route Circuit can be in the same or in a different subscription.</p></li>
<li><p><strong>express_route_gateway_bypass</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, data packets will bypass ExpressRoute Gateway for data forwarding This is only valid for ExpressRoute connections.</p></li>
<li><p><strong>ipsec_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>A <code class="docutils literal notranslate"><span class="pre">ipsec_policy</span></code> block which is documented below.
Only a single policy can be defined for a connection. For details on
custom policies refer to <a class="reference external" href="https://docs.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell">the relevant section in the Azure documentation</a>.</p>
</p></li>
<li><p><strong>local_network_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the local network gateway
when creating Site-to-Site connection (i.e. when <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">IPsec</span></code>).</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location/region where the connection is
located. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the connection. Changing the name forces a
new resource to be created.</p></li>
<li><p><strong>peer_virtual_network_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the peer virtual
network gateway when creating a VNet-to-VNet connection (i.e. when <code class="docutils literal notranslate"><span class="pre">type</span></code>
is <code class="docutils literal notranslate"><span class="pre">Vnet2Vnet</span></code>). The peer Virtual Network Gateway can be in the same or
in a different subscription.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the connection Changing the name forces a new resource to be created.</p></li>
<li><p><strong>routing_weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The routing weight. Defaults to <code class="docutils literal notranslate"><span class="pre">10</span></code>.</p></li>
<li><p><strong>shared_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The shared IPSec key. A key must be provided if a
Site-to-Site or VNet-to-VNet connection is created whereas ExpressRoute
connections do not need a shared key.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of connection. Valid options are <code class="docutils literal notranslate"><span class="pre">IPsec</span></code>
(Site-to-Site), <code class="docutils literal notranslate"><span class="pre">ExpressRoute</span></code> (ExpressRoute), and <code class="docutils literal notranslate"><span class="pre">Vnet2Vnet</span></code> (VNet-to-VNet).
Each connection type requires different mandatory arguments (refer to the
examples above). Changing the connection type will force a new connection
to be created.</p></li>
<li><p><strong>use_policy_based_traffic_selectors</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, policy-based traffic
selectors are enabled for this connection. Enabling policy-based traffic
selectors requires an <code class="docutils literal notranslate"><span class="pre">ipsec_policy</span></code> block. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>virtual_network_gateway_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Network Gateway
in which the connection will be created. Changing the gateway forces a new
resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ipsec_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dhGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeIntegrity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecIntegrity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pfsGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">saDatasize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">saLifetime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualNetworkGatewayConnection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkGatewayConnection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualNetworkPeering">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">VirtualNetworkPeering</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_forwarded_traffic=None</em>, <em class="sig-param">allow_gateway_transit=None</em>, <em class="sig-param">allow_virtual_network_access=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">remote_virtual_network_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">use_remote_gateways=None</em>, <em class="sig-param">virtual_network_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a virtual network peering which allows resources to access other
resources in the linked virtual network.</p>
<p>Virtual Network peerings cannot be created, updated or deleted concurrently.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_network_peering.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_network_peering.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_forwarded_traffic</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls if forwarded traffic from  VMs
in the remote virtual network is allowed. Defaults to false.</p></li>
<li><p><strong>allow_gateway_transit</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls gatewayLinks can be used in the
remote virtual network’s link to the local virtual network.</p></li>
<li><p><strong>allow_virtual_network_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls if the VMs in the remote
virtual network can access VMs in the local virtual network. Defaults to
true.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual network peering. Changing this
forces a new resource to be created.</p></li>
<li><p><strong>remote_virtual_network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full Azure resource ID of the
remote virtual network.  Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.</p></li>
<li><p><strong>use_remote_gateways</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls if remote gateways can be used on
the local virtual network. If the flag is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, and
<code class="docutils literal notranslate"><span class="pre">allow_gateway_transit</span></code> on the remote peering is also <code class="docutils literal notranslate"><span class="pre">true</span></code>, virtual network will
use gateways of remote virtual network for transit. Only one peering can
have this flag set to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This flag cannot be set if virtual network
already has a gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>virtual_network_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual network. Changing
this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkPeering.allow_forwarded_traffic">
<code class="sig-name descname">allow_forwarded_traffic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.allow_forwarded_traffic" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls if forwarded traffic from  VMs
in the remote virtual network is allowed. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkPeering.allow_gateway_transit">
<code class="sig-name descname">allow_gateway_transit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.allow_gateway_transit" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls gatewayLinks can be used in the
remote virtual network’s link to the local virtual network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkPeering.allow_virtual_network_access">
<code class="sig-name descname">allow_virtual_network_access</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.allow_virtual_network_access" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls if the VMs in the remote
virtual network can access VMs in the local virtual network. Defaults to
true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkPeering.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the virtual network peering. Changing this
forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkPeering.remote_virtual_network_id">
<code class="sig-name descname">remote_virtual_network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.remote_virtual_network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The full Azure resource ID of the
remote virtual network.  Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkPeering.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkPeering.use_remote_gateways">
<code class="sig-name descname">use_remote_gateways</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.use_remote_gateways" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls if remote gateways can be used on
the local virtual network. If the flag is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, and
<code class="docutils literal notranslate"><span class="pre">allow_gateway_transit</span></code> on the remote peering is also <code class="docutils literal notranslate"><span class="pre">true</span></code>, virtual network will
use gateways of remote virtual network for transit. Only one peering can
have this flag set to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This flag cannot be set if virtual network
already has a gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualNetworkPeering.virtual_network_name">
<code class="sig-name descname">virtual_network_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.virtual_network_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the virtual network. Changing
this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VirtualNetworkPeering.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_forwarded_traffic=None</em>, <em class="sig-param">allow_gateway_transit=None</em>, <em class="sig-param">allow_virtual_network_access=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">remote_virtual_network_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">use_remote_gateways=None</em>, <em class="sig-param">virtual_network_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualNetworkPeering resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_forwarded_traffic</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls if forwarded traffic from  VMs
in the remote virtual network is allowed. Defaults to false.</p></li>
<li><p><strong>allow_gateway_transit</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls gatewayLinks can be used in the
remote virtual network’s link to the local virtual network.</p></li>
<li><p><strong>allow_virtual_network_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls if the VMs in the remote
virtual network can access VMs in the local virtual network. Defaults to
true.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual network peering. Changing this
forces a new resource to be created.</p></li>
<li><p><strong>remote_virtual_network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full Azure resource ID of the
remote virtual network.  Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.</p></li>
<li><p><strong>use_remote_gateways</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Controls if remote gateways can be used on
the local virtual network. If the flag is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, and
<code class="docutils literal notranslate"><span class="pre">allow_gateway_transit</span></code> on the remote peering is also <code class="docutils literal notranslate"><span class="pre">true</span></code>, virtual network will
use gateways of remote virtual network for transit. Only one peering can
have this flag set to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This flag cannot be set if virtual network
already has a gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>virtual_network_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual network. Changing
this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VirtualNetworkPeering.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualNetworkPeering.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualNetworkPeering.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualWan">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">VirtualWan</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_branch_to_branch_traffic=None</em>, <em class="sig-param">allow_vnet_to_vnet_traffic=None</em>, <em class="sig-param">disable_vpn_encryption=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">office365_local_breakout_category=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualWan" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Virtual WAN.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_wan.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_wan.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_branch_to_branch_traffic</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to specify whether branch to branch traffic is allowed. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>allow_vnet_to_vnet_traffic</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to specify whether VNet to VNet traffic is allowed. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>disable_vpn_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to specify whether VPN encryption is disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Virtual WAN. Changing this forces a new resource to be created.</p></li>
<li><p><strong>office365_local_breakout_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Office365 local breakout category. Possible values include: <code class="docutils literal notranslate"><span class="pre">Optimize</span></code>, <code class="docutils literal notranslate"><span class="pre">OptimizeAndAllow</span></code>, <code class="docutils literal notranslate"><span class="pre">All</span></code>, <code class="docutils literal notranslate"><span class="pre">None</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Virtual WAN. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Virtual WAN.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Virtual WAN type. Possible Values include: <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.network.VirtualWan.allow_branch_to_branch_traffic">
<code class="sig-name descname">allow_branch_to_branch_traffic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualWan.allow_branch_to_branch_traffic" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to specify whether branch to branch traffic is allowed. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualWan.allow_vnet_to_vnet_traffic">
<code class="sig-name descname">allow_vnet_to_vnet_traffic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualWan.allow_vnet_to_vnet_traffic" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to specify whether VNet to VNet traffic is allowed. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualWan.disable_vpn_encryption">
<code class="sig-name descname">disable_vpn_encryption</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualWan.disable_vpn_encryption" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to specify whether VPN encryption is disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualWan.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualWan.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualWan.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualWan.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Virtual WAN. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualWan.office365_local_breakout_category">
<code class="sig-name descname">office365_local_breakout_category</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualWan.office365_local_breakout_category" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Office365 local breakout category. Possible values include: <code class="docutils literal notranslate"><span class="pre">Optimize</span></code>, <code class="docutils literal notranslate"><span class="pre">OptimizeAndAllow</span></code>, <code class="docutils literal notranslate"><span class="pre">All</span></code>, <code class="docutils literal notranslate"><span class="pre">None</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualWan.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualWan.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Virtual WAN. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualWan.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualWan.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the Virtual WAN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VirtualWan.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VirtualWan.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Virtual WAN type. Possible Values include: <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VirtualWan.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allow_branch_to_branch_traffic=None</em>, <em class="sig-param">allow_vnet_to_vnet_traffic=None</em>, <em class="sig-param">disable_vpn_encryption=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">office365_local_breakout_category=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualWan.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualWan resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_branch_to_branch_traffic</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to specify whether branch to branch traffic is allowed. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>allow_vnet_to_vnet_traffic</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to specify whether VNet to VNet traffic is allowed. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>disable_vpn_encryption</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to specify whether VPN encryption is disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Virtual WAN. Changing this forces a new resource to be created.</p></li>
<li><p><strong>office365_local_breakout_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Office365 local breakout category. Possible values include: <code class="docutils literal notranslate"><span class="pre">Optimize</span></code>, <code class="docutils literal notranslate"><span class="pre">OptimizeAndAllow</span></code>, <code class="docutils literal notranslate"><span class="pre">All</span></code>, <code class="docutils literal notranslate"><span class="pre">None</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Virtual WAN. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Virtual WAN.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Virtual WAN type. Possible Values include: <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VirtualWan.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualWan.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VirtualWan.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VirtualWan.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VpnGateway">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">VpnGateway</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bgp_settings=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">scale_unit=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_hub_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VpnGateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a VPN Gateway within a Virtual Hub, which enables Site-to-Site communication.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/vpn_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/vpn_gateway.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bgp_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">bgp_settings</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where this VPN Gateway should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name which should be used for this VPN Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group in which this VPN Gateway should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>scale_unit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Scale Unit for this VPN Gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the VPN Gateway.</p></li>
<li><p><strong>virtual_hub_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Hub within which this VPN Gateway should be created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bgp_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">asn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bgpPeeringAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Address which should be used for the BGP Peering.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">peerWeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.VpnGateway.bgp_settings">
<code class="sig-name descname">bgp_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VpnGateway.bgp_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">bgp_settings</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">asn</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bgpPeeringAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Address which should be used for the BGP Peering.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">peerWeight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VpnGateway.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VpnGateway.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where this VPN Gateway should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VpnGateway.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VpnGateway.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name which should be used for this VPN Gateway. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VpnGateway.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VpnGateway.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Resource Group in which this VPN Gateway should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VpnGateway.scale_unit">
<code class="sig-name descname">scale_unit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VpnGateway.scale_unit" title="Permalink to this definition">¶</a></dt>
<dd><p>The Scale Unit for this VPN Gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VpnGateway.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VpnGateway.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the VPN Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VpnGateway.virtual_hub_id">
<code class="sig-name descname">virtual_hub_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VpnGateway.virtual_hub_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Virtual Hub within which this VPN Gateway should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VpnGateway.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bgp_settings=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">scale_unit=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_hub_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VpnGateway.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VpnGateway resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bgp_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">bgp_settings</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where this VPN Gateway should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name which should be used for this VPN Gateway. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group in which this VPN Gateway should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>scale_unit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Scale Unit for this VPN Gateway. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the VPN Gateway.</p></li>
<li><p><strong>virtual_hub_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Hub within which this VPN Gateway should be created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>bgp_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">asn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">bgpPeeringAddress</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Address which should be used for the BGP Peering.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">peerWeight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VpnGateway.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VpnGateway.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VpnGateway.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VpnGateway.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VpnServerConfiguration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">VpnServerConfiguration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">azure_active_directory_authentications=None</em>, <em class="sig-param">client_revoked_certificates=None</em>, <em class="sig-param">client_root_certificates=None</em>, <em class="sig-param">ipsec_policy=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">radius_server=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpn_authentication_types=None</em>, <em class="sig-param">vpn_protocols=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VpnServerConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a VPN Server Configuration.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/vpn_server_configuration.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/vpn_server_configuration.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>azure_active_directory_authentications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">azure_active_directory_authentication</span></code> block as defined below.</p></li>
<li><p><strong>client_revoked_certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">client_revoked_certificate</span></code> blocks as defined below.</p></li>
<li><p><strong>client_root_certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">client_root_certificate</span></code> blocks as defined below.</p></li>
<li><p><strong>ipsec_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">ipsec_policy</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where this VPN Server Configuration should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><strong>radius_server</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">radius_server</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group in which this VPN Server Configuration should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vpn_authentication_types</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A list of one of more Authentication Types applicable for this VPN Server Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">AAD</span></code> (Azure Active Directory), <code class="docutils literal notranslate"><span class="pre">Certificate</span></code> and <code class="docutils literal notranslate"><span class="pre">Radius</span></code>.</p></li>
<li><p><strong>vpn_protocols</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of VPN Protocols to use for this Server Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">IkeV2</span></code> and <code class="docutils literal notranslate"><span class="pre">OpenVPN</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>azure_active_directory_authentications</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">audience</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>client_revoked_certificates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>client_root_certificates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicCertData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ipsec_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dhGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeIntegrity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecIntegrity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pfsGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">saDataSizeKilobytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">saLifetimeSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>radius_server</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_root_certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">client_root_certificate</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverRootCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicCertData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.network.VpnServerConfiguration.azure_active_directory_authentications">
<code class="sig-name descname">azure_active_directory_authentications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VpnServerConfiguration.azure_active_directory_authentications" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">azure_active_directory_authentication</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">audience</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VpnServerConfiguration.client_revoked_certificates">
<code class="sig-name descname">client_revoked_certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VpnServerConfiguration.client_revoked_certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">client_revoked_certificate</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VpnServerConfiguration.client_root_certificates">
<code class="sig-name descname">client_root_certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VpnServerConfiguration.client_root_certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">client_root_certificate</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicCertData</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VpnServerConfiguration.ipsec_policy">
<code class="sig-name descname">ipsec_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VpnServerConfiguration.ipsec_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">ipsec_policy</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dhGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeIntegrity</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecIntegrity</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pfsGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">saDataSizeKilobytes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">saLifetimeSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VpnServerConfiguration.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VpnServerConfiguration.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where this VPN Server Configuration should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VpnServerConfiguration.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VpnServerConfiguration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VpnServerConfiguration.radius_server">
<code class="sig-name descname">radius_server</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VpnServerConfiguration.radius_server" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">radius_server</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_root_certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">client_root_certificate</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverRootCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicCertData</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VpnServerConfiguration.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VpnServerConfiguration.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of the Resource Group in which this VPN Server Configuration should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VpnServerConfiguration.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VpnServerConfiguration.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VpnServerConfiguration.vpn_authentication_types">
<code class="sig-name descname">vpn_authentication_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VpnServerConfiguration.vpn_authentication_types" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of one of more Authentication Types applicable for this VPN Server Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">AAD</span></code> (Azure Active Directory), <code class="docutils literal notranslate"><span class="pre">Certificate</span></code> and <code class="docutils literal notranslate"><span class="pre">Radius</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.network.VpnServerConfiguration.vpn_protocols">
<code class="sig-name descname">vpn_protocols</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.network.VpnServerConfiguration.vpn_protocols" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of VPN Protocols to use for this Server Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">IkeV2</span></code> and <code class="docutils literal notranslate"><span class="pre">OpenVPN</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VpnServerConfiguration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">azure_active_directory_authentications=None</em>, <em class="sig-param">client_revoked_certificates=None</em>, <em class="sig-param">client_root_certificates=None</em>, <em class="sig-param">ipsec_policy=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">radius_server=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpn_authentication_types=None</em>, <em class="sig-param">vpn_protocols=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VpnServerConfiguration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VpnServerConfiguration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>azure_active_directory_authentications</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">azure_active_directory_authentication</span></code> block as defined below.</p></li>
<li><p><strong>client_revoked_certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">client_revoked_certificate</span></code> blocks as defined below.</p></li>
<li><p><strong>client_root_certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">client_root_certificate</span></code> blocks as defined below.</p></li>
<li><p><strong>ipsec_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">ipsec_policy</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where this VPN Server Configuration should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><strong>radius_server</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">radius_server</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of the Resource Group in which this VPN Server Configuration should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vpn_authentication_types</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A list of one of more Authentication Types applicable for this VPN Server Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">AAD</span></code> (Azure Active Directory), <code class="docutils literal notranslate"><span class="pre">Certificate</span></code> and <code class="docutils literal notranslate"><span class="pre">Radius</span></code>.</p></li>
<li><p><strong>vpn_protocols</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of VPN Protocols to use for this Server Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">IkeV2</span></code> and <code class="docutils literal notranslate"><span class="pre">OpenVPN</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>azure_active_directory_authentications</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">audience</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">issuer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>client_revoked_certificates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>client_root_certificates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicCertData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>ipsec_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dhGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ikeIntegrity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecEncryption</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipsecIntegrity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pfsGroup</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">saDataSizeKilobytes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">saLifetimeSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>radius_server</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_root_certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">client_root_certificate</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverRootCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this VPN Server Configuration. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicCertData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.network.VpnServerConfiguration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VpnServerConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.network.VpnServerConfiguration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.VpnServerConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_azure.network.get_application_security_group">
<code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">get_application_security_group</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_application_security_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Application Security Group.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/application_security_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/application_security_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Application Security Group.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group in which the Application Security Group exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_express_route_circuit">
<code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">get_express_route_circuit</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_express_route_circuit" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing ExpressRoute circuit.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/express_route_circuit.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/express_route_circuit.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the ExpressRoute circuit.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where the ExpressRoute circuit exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_firewall">
<code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">get_firewall</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_firewall" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Azure Firewall.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/firewall.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/firewall.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Azure Firewall.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group in which the Azure Firewall exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_gateway_connection">
<code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">get_gateway_connection</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_gateway_connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Virtual Network Gateway Connection.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/virtual_network_gateway_connection.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/virtual_network_gateway_connection.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Virtual Network Gateway Connection.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group the Virtual Network Gateway Connection is located in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_nat_gateway">
<code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">get_nat_gateway</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">public_ip_address_ids=None</em>, <em class="sig-param">public_ip_prefix_ids=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_nat_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing NAT Gateway.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The Azure NAT Gateway service is currently in private preview. Your subscription must be on the NAT Gateway private preview whitelist for this resource to be provisioned correctly. If you attempt to provision this resource and receive an <code class="docutils literal notranslate"><span class="pre">InvalidResourceType</span></code> error may mean that your subscription is not part of the NAT Gateway private preview or you are using a region which does not yet support the NAT Gateway private preview service. The NAT Gateway private preview service is currently available in a limited set of regions. Private preview resources may have multiple breaking changes over their lifecycle until they GA. You can opt into the Private Preview by contacting your Microsoft Representative.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/nat_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/nat_gateway.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the Name of the NAT Gateway.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the Resource Group where the NAT Gateway exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_network_ddos_protection_plan">
<code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">get_network_ddos_protection_plan</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_network_ddos_protection_plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Azure Network DDoS Protection Plan.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/network_ddos_protection_plan.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/network_ddos_protection_plan.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Network DDoS Protection Plan.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group where the Network DDoS Protection Plan exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_network_interface">
<code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">get_network_interface</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_network_interface" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Network Interface.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/network_interface.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/network_interface.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Network Interface.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group the Network Interface is located in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_network_security_group">
<code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">get_network_security_group</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_network_security_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Network Security Group.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/network_security_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/network_security_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the Name of the Network Security Group.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the Name of the Resource Group within which the Network Security Group exists</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_network_watcher">
<code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">get_network_watcher</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_network_watcher" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Network Watcher.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/network_watcher.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/network_watcher.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the Name of the Network Watcher.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the Name of the Resource Group within which the Network Watcher exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_public_i_ps">
<code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">get_public_i_ps</code><span class="sig-paren">(</span><em class="sig-param">allocation_type=None</em>, <em class="sig-param">attached=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_public_i_ps" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about a set of existing Public IP Addresses.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/public_ips.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/public_ips.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>allocation_type</strong> (<em>str</em>) – The Allocation Type for the Public IP Address. Possible values include <code class="docutils literal notranslate"><span class="pre">Static</span></code> or <code class="docutils literal notranslate"><span class="pre">Dynamic</span></code>.</p></li>
<li><p><strong>attached</strong> (<em>bool</em>) – Filter to include IP Addresses which are attached to a device, such as a VM/LB (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or unattached (<code class="docutils literal notranslate"><span class="pre">false</span></code>).</p></li>
<li><p><strong>name_prefix</strong> (<em>str</em>) – A prefix match used for the IP Addresses <code class="docutils literal notranslate"><span class="pre">name</span></code> field, case sensitive.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_public_ip">
<code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">get_public_ip</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_public_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Public IP Address.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/public_ip.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/public_ip.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the public IP address.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_public_ip_prefix">
<code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">get_public_ip_prefix</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_public_ip_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Public IP Prefix.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/public_ip_prefix.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/public_ip_prefix.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the public IP prefix.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_route_table">
<code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">get_route_table</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_route_table" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Route Table.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/route_table.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/route_table.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Route Table.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group in which the Route Table exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_subnet">
<code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">get_subnet</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">virtual_network_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Subnet within a Virtual Network.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/subnet.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/subnet.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Subnet.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group the Virtual Network is located in.</p></li>
<li><p><strong>virtual_network_name</strong> (<em>str</em>) – Specifies the name of the Virtual Network this Subnet is located within.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_traffic_manager">
<code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">get_traffic_manager</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_traffic_manager" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access the ID of a specified Traffic Manager Geographical Location within the Geographical Hierarchy.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/traffic_manager_geographical_location.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/traffic_manager_geographical_location.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Location, for example <code class="docutils literal notranslate"><span class="pre">World</span></code>, <code class="docutils literal notranslate"><span class="pre">Europe</span></code> or <code class="docutils literal notranslate"><span class="pre">Germany</span></code>.</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_virtual_hub">
<code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">get_virtual_hub</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_virtual_hub" title="Permalink to this definition">¶</a></dt>
<dd><p>Uses this data source to access information about an existing Virtual Hub.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/virtual_hub.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/virtual_hub.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Virtual Hub.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where the Virtual Hub exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_virtual_network">
<code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">get_virtual_network</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_virtual_network" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Virtual Network.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/virtual_network.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/virtual_network.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Virtual Network.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group the Virtual Network is located in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.network.get_virtual_network_gateway">
<code class="sig-prename descclassname">pulumi_azure.network.</code><code class="sig-name descname">get_virtual_network_gateway</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.network.get_virtual_network_gateway" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Virtual Network Gateway.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/virtual_network_gateway.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/virtual_network_gateway.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Virtual Network Gateway.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group the Virtual Network Gateway is located in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
