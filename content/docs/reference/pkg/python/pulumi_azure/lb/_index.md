---
title: Module lb
title_tag: Module lb | Package pulumi_azure | Python SDK
linktitle: lb
notitle: true
---

<div class="section" id="lb">
<h1>lb<a class="headerlink" href="#lb" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.lb"></span><dl class="class">
<dt id="pulumi_azure.lb.AwaitableGetBackendAddressPoolResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.lb.</code><code class="sig-name descname">AwaitableGetBackendAddressPoolResult</code><span class="sig-paren">(</span><em class="sig-param">backend_ip_configurations=None</em>, <em class="sig-param">loadbalancer_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.AwaitableGetBackendAddressPoolResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.lb.AwaitableGetLBResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.lb.</code><code class="sig-name descname">AwaitableGetLBResult</code><span class="sig-paren">(</span><em class="sig-param">frontend_ip_configurations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">private_ip_address=None</em>, <em class="sig-param">private_ip_addresses=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.AwaitableGetLBResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.lb.BackendAddressPool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.lb.</code><code class="sig-name descname">BackendAddressPool</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">loadbalancer_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.BackendAddressPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Load Balancer Backend Address Pool.</p>
<blockquote>
<div><p><strong>NOTE:</strong> When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer in which to create the Backend Address Pool.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Backend Address Pool.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_backend_address_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_backend_address_pool.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.lb.BackendAddressPool.backend_ip_configurations">
<code class="sig-name descname">backend_ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.BackendAddressPool.backend_ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>The Backend IP Configurations associated with this Backend Address Pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.BackendAddressPool.load_balancing_rules">
<code class="sig-name descname">load_balancing_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.BackendAddressPool.load_balancing_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>The Load Balancing Rules associated with this Backend Address Pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.BackendAddressPool.loadbalancer_id">
<code class="sig-name descname">loadbalancer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.BackendAddressPool.loadbalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Load Balancer in which to create the Backend Address Pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.BackendAddressPool.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.BackendAddressPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Backend Address Pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.BackendAddressPool.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.BackendAddressPool.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.BackendAddressPool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_ip_configurations=None</em>, <em class="sig-param">load_balancing_rules=None</em>, <em class="sig-param">loadbalancer_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.BackendAddressPool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BackendAddressPool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The Backend IP Configurations associated with this Backend Address Pool.</p></li>
<li><p><strong>load_balancing_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The Load Balancing Rules associated with this Backend Address Pool.</p></li>
<li><p><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer in which to create the Backend Address Pool.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Backend Address Pool.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_backend_address_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_backend_address_pool.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.BackendAddressPool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.BackendAddressPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.lb.BackendAddressPool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.BackendAddressPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.lb.GetBackendAddressPoolResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.lb.</code><code class="sig-name descname">GetBackendAddressPoolResult</code><span class="sig-paren">(</span><em class="sig-param">backend_ip_configurations=None</em>, <em class="sig-param">loadbalancer_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.GetBackendAddressPoolResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBackendAddressPool.</p>
<dl class="attribute">
<dt id="pulumi_azure.lb.GetBackendAddressPoolResult.backend_ip_configurations">
<code class="sig-name descname">backend_ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetBackendAddressPoolResult.backend_ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of references to IP addresses defined in network interfaces.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.GetBackendAddressPoolResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetBackendAddressPoolResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Backend Address Pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.GetBackendAddressPoolResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetBackendAddressPoolResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.lb.GetLBResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.lb.</code><code class="sig-name descname">GetLBResult</code><span class="sig-paren">(</span><em class="sig-param">frontend_ip_configurations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">private_ip_address=None</em>, <em class="sig-param">private_ip_addresses=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.GetLBResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLB.</p>
<dl class="attribute">
<dt id="pulumi_azure.lb.GetLBResult.frontend_ip_configurations">
<code class="sig-name descname">frontend_ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetLBResult.frontend_ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) A <code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.GetLBResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetLBResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the Load Balancer exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.GetLBResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetLBResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Frontend IP Configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.GetLBResult.private_ip_address">
<code class="sig-name descname">private_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetLBResult.private_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Private IP Address to assign to the Load Balancer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.GetLBResult.private_ip_addresses">
<code class="sig-name descname">private_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetLBResult.private_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of private IP address assigned to the load balancer in <code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration</span></code> blocks, if any.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.GetLBResult.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetLBResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU of the Load Balancer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.GetLBResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetLBResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.GetLBResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.GetLBResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.lb.LoadBalancer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.lb.</code><code class="sig-name descname">LoadBalancer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">frontend_ip_configurations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Load Balancer Resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>frontend_ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or multiple <code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration</span></code> blocks as documented below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure Region where the Load Balancer should be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the frontend ip configuration.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which to create the Load Balancer.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU of the Azure Load Balancer. Accepted values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Basic</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>frontend_ip_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The id of the Frontend IP Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inbound_nat_rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">load_balancer_rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the frontend ip configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outboundRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Private IP Address to assign to the Load Balancer. The last one and first four IPs in any range are reserved and cannot be manually assigned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddressAllocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The allocation method for the Private IP Address used by this Load Balancer. Possible values as <code class="docutils literal notranslate"><span class="pre">Dynamic</span></code> and <code class="docutils literal notranslate"><span class="pre">Static</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of a Public IP Address which should be associated with the Load Balancer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpPrefixId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of a Public IP Prefix which should be associated with the Load Balancer. Public IP Prefix can only be used with outbound rules.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet which should be associated with the IP Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zones</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A list of Availability Zones which the Load Balancer’s IP Addresses should be created in.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.lb.LoadBalancer.frontend_ip_configurations">
<code class="sig-name descname">frontend_ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.frontend_ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or multiple <code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration</span></code> blocks as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The id of the Frontend IP Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inbound_nat_rules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">load_balancer_rules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the frontend ip configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outboundRules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Private IP Address to assign to the Load Balancer. The last one and first four IPs in any range are reserved and cannot be manually assigned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddressAllocation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The allocation method for the Private IP Address used by this Load Balancer. Possible values as <code class="docutils literal notranslate"><span class="pre">Dynamic</span></code> and <code class="docutils literal notranslate"><span class="pre">Static</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of a Public IP Address which should be associated with the Load Balancer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpPrefixId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of a Public IP Prefix which should be associated with the Load Balancer. Public IP Prefix can only be used with outbound rules.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet which should be associated with the IP Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zones</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A list of Availability Zones which the Load Balancer’s IP Addresses should be created in.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.LoadBalancer.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure Region where the Load Balancer should be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.LoadBalancer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the frontend ip configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.LoadBalancer.private_ip_address">
<code class="sig-name descname">private_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.private_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Private IP Address to assign to the Load Balancer. The last one and first four IPs in any range are reserved and cannot be manually assigned.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.LoadBalancer.private_ip_addresses">
<code class="sig-name descname">private_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.private_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of private IP address assigned to the load balancer in <code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration</span></code> blocks, if any.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.LoadBalancer.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which to create the Load Balancer.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.LoadBalancer.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU of the Azure Load Balancer. Accepted values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Basic</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.LoadBalancer.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.LoadBalancer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">frontend_ip_configurations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">private_ip_address=None</em>, <em class="sig-param">private_ip_addresses=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LoadBalancer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>frontend_ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or multiple <code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration</span></code> blocks as documented below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure Region where the Load Balancer should be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the frontend ip configuration.</p></li>
<li><p><strong>private_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Private IP Address to assign to the Load Balancer. The last one and first four IPs in any range are reserved and cannot be manually assigned.</p></li>
<li><p><strong>private_ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of private IP address assigned to the load balancer in <code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration</span></code> blocks, if any.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which to create the Load Balancer.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU of the Azure Load Balancer. Accepted values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Basic</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>frontend_ip_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The id of the Frontend IP Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">inbound_nat_rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">load_balancer_rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the frontend ip configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outboundRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Private IP Address to assign to the Load Balancer. The last one and first four IPs in any range are reserved and cannot be manually assigned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateIpAddressAllocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The allocation method for the Private IP Address used by this Load Balancer. Possible values as <code class="docutils literal notranslate"><span class="pre">Dynamic</span></code> and <code class="docutils literal notranslate"><span class="pre">Static</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of a Public IP Address which should be associated with the Load Balancer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpPrefixId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of a Public IP Prefix which should be associated with the Load Balancer. Public IP Prefix can only be used with outbound rules.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet which should be associated with the IP Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">zones</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A list of Availability Zones which the Load Balancer’s IP Addresses should be created in.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.LoadBalancer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.lb.LoadBalancer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.LoadBalancer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.lb.NatPool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.lb.</code><code class="sig-name descname">NatPool</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_port=None</em>, <em class="sig-param">frontend_ip_configuration_name=None</em>, <em class="sig-param">frontend_port_end=None</em>, <em class="sig-param">frontend_port_start=None</em>, <em class="sig-param">loadbalancer_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.NatPool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Load Balancer NAT pool.</p>
<blockquote>
<div><p><strong>NOTE:</strong> This resource cannot be used with with virtual machines, instead use the <code class="docutils literal notranslate"><span class="pre">lb.NatRule</span></code> resource.</p>
<p><strong>NOTE</strong> When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port used for the internal endpoint. Possible values range between 1 and 65535, inclusive.</p></li>
<li><p><strong>frontend_ip_configuration_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the frontend IP configuration exposing this rule.</p></li>
<li><p><strong>frontend_port_end</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The last port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.</p></li>
<li><p><strong>frontend_port_start</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The first port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.</p></li>
<li><p><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer in which to create the NAT pool.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the NAT pool.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The transport protocol for the external endpoint. Possible values are <code class="docutils literal notranslate"><span class="pre">Udp</span></code> or <code class="docutils literal notranslate"><span class="pre">Tcp</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_nat_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_nat_pool.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.lb.NatPool.backend_port">
<code class="sig-name descname">backend_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatPool.backend_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port used for the internal endpoint. Possible values range between 1 and 65535, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatPool.frontend_ip_configuration_name">
<code class="sig-name descname">frontend_ip_configuration_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatPool.frontend_ip_configuration_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the frontend IP configuration exposing this rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatPool.frontend_port_end">
<code class="sig-name descname">frontend_port_end</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatPool.frontend_port_end" title="Permalink to this definition">¶</a></dt>
<dd><p>The last port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatPool.frontend_port_start">
<code class="sig-name descname">frontend_port_start</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatPool.frontend_port_start" title="Permalink to this definition">¶</a></dt>
<dd><p>The first port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatPool.loadbalancer_id">
<code class="sig-name descname">loadbalancer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatPool.loadbalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Load Balancer in which to create the NAT pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatPool.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatPool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the NAT pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatPool.protocol">
<code class="sig-name descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatPool.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The transport protocol for the external endpoint. Possible values are <code class="docutils literal notranslate"><span class="pre">Udp</span></code> or <code class="docutils literal notranslate"><span class="pre">Tcp</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatPool.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatPool.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.NatPool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_port=None</em>, <em class="sig-param">frontend_ip_configuration_id=None</em>, <em class="sig-param">frontend_ip_configuration_name=None</em>, <em class="sig-param">frontend_port_end=None</em>, <em class="sig-param">frontend_port_start=None</em>, <em class="sig-param">loadbalancer_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.NatPool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NatPool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port used for the internal endpoint. Possible values range between 1 and 65535, inclusive.</p></li>
<li><p><strong>frontend_ip_configuration_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the frontend IP configuration exposing this rule.</p></li>
<li><p><strong>frontend_port_end</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The last port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.</p></li>
<li><p><strong>frontend_port_start</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The first port number in the range of external ports that will be used to provide Inbound Nat to NICs associated with this Load Balancer. Possible values range between 1 and 65534, inclusive.</p></li>
<li><p><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer in which to create the NAT pool.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the NAT pool.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The transport protocol for the external endpoint. Possible values are <code class="docutils literal notranslate"><span class="pre">Udp</span></code> or <code class="docutils literal notranslate"><span class="pre">Tcp</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_nat_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_nat_pool.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.NatPool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.NatPool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.lb.NatPool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.NatPool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.lb.NatRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.lb.</code><code class="sig-name descname">NatRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_port=None</em>, <em class="sig-param">enable_floating_ip=None</em>, <em class="sig-param">enable_tcp_reset=None</em>, <em class="sig-param">frontend_ip_configuration_name=None</em>, <em class="sig-param">frontend_port=None</em>, <em class="sig-param">idle_timeout_in_minutes=None</em>, <em class="sig-param">loadbalancer_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.NatRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Load Balancer NAT Rule.</p>
<blockquote>
<div><p><strong>NOTE:</strong> This resource cannot be used with with virtual machine scale sets, instead use the <code class="docutils literal notranslate"><span class="pre">lb.NatPool</span></code> resource.</p>
<p><strong>NOTE</strong> When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port used for internal connections on the endpoint. Possible values range between 1 and 65535, inclusive.</p></li>
<li><p><strong>enable_floating_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Are the Floating IPs enabled for this Load Balncer Rule? A “floating” IP is reassigned to a secondary server in case the primary server fails. Required to configure a SQL AlwaysOn Availability Group. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_tcp_reset</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is TCP Reset enabled for this Load Balancer Rule? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>frontend_ip_configuration_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the frontend IP configuration exposing this rule.</p></li>
<li><p><strong>frontend_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 1 and 65534, inclusive.</p></li>
<li><p><strong>idle_timeout_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the idle timeout in minutes for TCP connections. Valid values are between <code class="docutils literal notranslate"><span class="pre">4</span></code> and <code class="docutils literal notranslate"><span class="pre">30</span></code> minutes. Defaults to <code class="docutils literal notranslate"><span class="pre">4</span></code> minutes.</p></li>
<li><p><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer in which to create the NAT Rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the NAT Rule.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The transport protocol for the external endpoint. Possible values are <code class="docutils literal notranslate"><span class="pre">Udp</span></code>, <code class="docutils literal notranslate"><span class="pre">Tcp</span></code> or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_nat_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_nat_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.lb.NatRule.backend_port">
<code class="sig-name descname">backend_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatRule.backend_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port used for internal connections on the endpoint. Possible values range between 1 and 65535, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatRule.enable_floating_ip">
<code class="sig-name descname">enable_floating_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatRule.enable_floating_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Are the Floating IPs enabled for this Load Balncer Rule? A “floating” IP is reassigned to a secondary server in case the primary server fails. Required to configure a SQL AlwaysOn Availability Group. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatRule.enable_tcp_reset">
<code class="sig-name descname">enable_tcp_reset</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatRule.enable_tcp_reset" title="Permalink to this definition">¶</a></dt>
<dd><p>Is TCP Reset enabled for this Load Balancer Rule? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatRule.frontend_ip_configuration_name">
<code class="sig-name descname">frontend_ip_configuration_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatRule.frontend_ip_configuration_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the frontend IP configuration exposing this rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatRule.frontend_port">
<code class="sig-name descname">frontend_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatRule.frontend_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 1 and 65534, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatRule.idle_timeout_in_minutes">
<code class="sig-name descname">idle_timeout_in_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatRule.idle_timeout_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the idle timeout in minutes for TCP connections. Valid values are between <code class="docutils literal notranslate"><span class="pre">4</span></code> and <code class="docutils literal notranslate"><span class="pre">30</span></code> minutes. Defaults to <code class="docutils literal notranslate"><span class="pre">4</span></code> minutes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatRule.loadbalancer_id">
<code class="sig-name descname">loadbalancer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatRule.loadbalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Load Balancer in which to create the NAT Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the NAT Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatRule.protocol">
<code class="sig-name descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatRule.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The transport protocol for the external endpoint. Possible values are <code class="docutils literal notranslate"><span class="pre">Udp</span></code>, <code class="docutils literal notranslate"><span class="pre">Tcp</span></code> or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.NatRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.NatRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.NatRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_ip_configuration_id=None</em>, <em class="sig-param">backend_port=None</em>, <em class="sig-param">enable_floating_ip=None</em>, <em class="sig-param">enable_tcp_reset=None</em>, <em class="sig-param">frontend_ip_configuration_id=None</em>, <em class="sig-param">frontend_ip_configuration_name=None</em>, <em class="sig-param">frontend_port=None</em>, <em class="sig-param">idle_timeout_in_minutes=None</em>, <em class="sig-param">loadbalancer_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.NatRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NatRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port used for internal connections on the endpoint. Possible values range between 1 and 65535, inclusive.</p></li>
<li><p><strong>enable_floating_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Are the Floating IPs enabled for this Load Balncer Rule? A “floating” IP is reassigned to a secondary server in case the primary server fails. Required to configure a SQL AlwaysOn Availability Group. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_tcp_reset</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is TCP Reset enabled for this Load Balancer Rule? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>frontend_ip_configuration_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the frontend IP configuration exposing this rule.</p></li>
<li><p><strong>frontend_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 1 and 65534, inclusive.</p></li>
<li><p><strong>idle_timeout_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the idle timeout in minutes for TCP connections. Valid values are between <code class="docutils literal notranslate"><span class="pre">4</span></code> and <code class="docutils literal notranslate"><span class="pre">30</span></code> minutes. Defaults to <code class="docutils literal notranslate"><span class="pre">4</span></code> minutes.</p></li>
<li><p><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer in which to create the NAT Rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the NAT Rule.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The transport protocol for the external endpoint. Possible values are <code class="docutils literal notranslate"><span class="pre">Udp</span></code>, <code class="docutils literal notranslate"><span class="pre">Tcp</span></code> or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_nat_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_nat_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.NatRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.NatRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.lb.NatRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.NatRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.lb.OutboundRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.lb.</code><code class="sig-name descname">OutboundRule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allocated_outbound_ports=None</em>, <em class="sig-param">backend_address_pool_id=None</em>, <em class="sig-param">enable_tcp_reset=None</em>, <em class="sig-param">frontend_ip_configurations=None</em>, <em class="sig-param">idle_timeout_in_minutes=None</em>, <em class="sig-param">loadbalancer_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.OutboundRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Load Balancer Outbound Rule.</p>
<blockquote>
<div><p><strong>NOTE</strong> When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration and a Backend Address Pool Attached.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocated_outbound_ports</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of outbound ports to be used for NAT.</p></li>
<li><p><strong>backend_address_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Backend Address Pool. Outbound traffic is randomly load balanced across IPs in the backend IPs.</p></li>
<li><p><strong>enable_tcp_reset</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected connection termination. This element is only used when the protocol is set to TCP.</p></li>
<li><p><strong>frontend_ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration</span></code> blocks as defined below.</p></li>
<li><p><strong>idle_timeout_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The timeout for the TCP idle connection</p></li>
<li><p><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer in which to create the Outbound Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Outbound Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The transport protocol for the external endpoint. Possible values are <code class="docutils literal notranslate"><span class="pre">Udp</span></code>, <code class="docutils literal notranslate"><span class="pre">Tcp</span></code> or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>frontend_ip_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Load Balancer Outbound Rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Outbound Rule. Changing this forces a new resource to be created.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_outbound_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_outbound_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.lb.OutboundRule.allocated_outbound_ports">
<code class="sig-name descname">allocated_outbound_ports</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.OutboundRule.allocated_outbound_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of outbound ports to be used for NAT.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.OutboundRule.backend_address_pool_id">
<code class="sig-name descname">backend_address_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.OutboundRule.backend_address_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Backend Address Pool. Outbound traffic is randomly load balanced across IPs in the backend IPs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.OutboundRule.enable_tcp_reset">
<code class="sig-name descname">enable_tcp_reset</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.OutboundRule.enable_tcp_reset" title="Permalink to this definition">¶</a></dt>
<dd><p>Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected connection termination. This element is only used when the protocol is set to TCP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.OutboundRule.frontend_ip_configurations">
<code class="sig-name descname">frontend_ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.OutboundRule.frontend_ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Load Balancer Outbound Rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Outbound Rule. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.OutboundRule.idle_timeout_in_minutes">
<code class="sig-name descname">idle_timeout_in_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.OutboundRule.idle_timeout_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>The timeout for the TCP idle connection</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.OutboundRule.loadbalancer_id">
<code class="sig-name descname">loadbalancer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.OutboundRule.loadbalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Load Balancer in which to create the Outbound Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.OutboundRule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.OutboundRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Outbound Rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.OutboundRule.protocol">
<code class="sig-name descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.OutboundRule.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The transport protocol for the external endpoint. Possible values are <code class="docutils literal notranslate"><span class="pre">Udp</span></code>, <code class="docutils literal notranslate"><span class="pre">Tcp</span></code> or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.OutboundRule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.OutboundRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.OutboundRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">allocated_outbound_ports=None</em>, <em class="sig-param">backend_address_pool_id=None</em>, <em class="sig-param">enable_tcp_reset=None</em>, <em class="sig-param">frontend_ip_configurations=None</em>, <em class="sig-param">idle_timeout_in_minutes=None</em>, <em class="sig-param">loadbalancer_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.OutboundRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OutboundRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allocated_outbound_ports</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of outbound ports to be used for NAT.</p></li>
<li><p><strong>backend_address_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Backend Address Pool. Outbound traffic is randomly load balanced across IPs in the backend IPs.</p></li>
<li><p><strong>enable_tcp_reset</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Receive bidirectional TCP Reset on TCP flow idle timeout or unexpected connection termination. This element is only used when the protocol is set to TCP.</p></li>
<li><p><strong>frontend_ip_configurations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">frontend_ip_configuration</span></code> blocks as defined below.</p></li>
<li><p><strong>idle_timeout_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The timeout for the TCP idle connection</p></li>
<li><p><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer in which to create the Outbound Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Outbound Rule. Changing this forces a new resource to be created.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The transport protocol for the external endpoint. Possible values are <code class="docutils literal notranslate"><span class="pre">Udp</span></code>, <code class="docutils literal notranslate"><span class="pre">Tcp</span></code> or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>frontend_ip_configurations</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Load Balancer Outbound Rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Outbound Rule. Changing this forces a new resource to be created.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_outbound_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_outbound_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.OutboundRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.OutboundRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.lb.OutboundRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.OutboundRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.lb.Probe">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.lb.</code><code class="sig-name descname">Probe</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">interval_in_seconds=None</em>, <em class="sig-param">loadbalancer_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">number_of_probes=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">request_path=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.Probe" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a LoadBalancer Probe Resource.</p>
<blockquote>
<div><p><strong>NOTE</strong> When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>interval_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The interval, in seconds between probes to the backend endpoint for health status. The default value is 15, the minimum value is 5.</p></li>
<li><p><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the LoadBalancer in which to create the NAT Rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Probe.</p></li>
<li><p><strong>number_of_probes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of failed probe attempts after which the backend endpoint is removed from rotation. The default value is 2. NumberOfProbes multiplied by intervalInSeconds value must be greater or equal to 10.Endpoints are returned to rotation when at least one probe is successful.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Port on which the Probe queries the backend endpoint. Possible values range from 1 to 65535, inclusive.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the protocol of the end point. Possible values are <code class="docutils literal notranslate"><span class="pre">Http</span></code>, <code class="docutils literal notranslate"><span class="pre">Https</span></code> or <code class="docutils literal notranslate"><span class="pre">Tcp</span></code>. If Tcp is specified, a received ACK is required for the probe to be successful. If Http is specified, a 200 OK response from the specified URI is required for the probe to be successful.</p></li>
<li><p><strong>request_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI used for requesting health status from the backend endpoint. Required if protocol is set to Http. Otherwise, it is not allowed.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_probe.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_probe.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.lb.Probe.interval_in_seconds">
<code class="sig-name descname">interval_in_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Probe.interval_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The interval, in seconds between probes to the backend endpoint for health status. The default value is 15, the minimum value is 5.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Probe.loadbalancer_id">
<code class="sig-name descname">loadbalancer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Probe.loadbalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the LoadBalancer in which to create the NAT Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Probe.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Probe.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Probe.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Probe.number_of_probes">
<code class="sig-name descname">number_of_probes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Probe.number_of_probes" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of failed probe attempts after which the backend endpoint is removed from rotation. The default value is 2. NumberOfProbes multiplied by intervalInSeconds value must be greater or equal to 10.Endpoints are returned to rotation when at least one probe is successful.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Probe.port">
<code class="sig-name descname">port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Probe.port" title="Permalink to this definition">¶</a></dt>
<dd><p>Port on which the Probe queries the backend endpoint. Possible values range from 1 to 65535, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Probe.protocol">
<code class="sig-name descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Probe.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the protocol of the end point. Possible values are <code class="docutils literal notranslate"><span class="pre">Http</span></code>, <code class="docutils literal notranslate"><span class="pre">Https</span></code> or <code class="docutils literal notranslate"><span class="pre">Tcp</span></code>. If Tcp is specified, a received ACK is required for the probe to be successful. If Http is specified, a 200 OK response from the specified URI is required for the probe to be successful.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Probe.request_path">
<code class="sig-name descname">request_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Probe.request_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI used for requesting health status from the backend endpoint. Required if protocol is set to Http. Otherwise, it is not allowed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Probe.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Probe.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.Probe.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">interval_in_seconds=None</em>, <em class="sig-param">load_balancer_rules=None</em>, <em class="sig-param">loadbalancer_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">number_of_probes=None</em>, <em class="sig-param">port=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">request_path=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.Probe.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Probe resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>interval_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The interval, in seconds between probes to the backend endpoint for health status. The default value is 15, the minimum value is 5.</p></li>
<li><p><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the LoadBalancer in which to create the NAT Rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Probe.</p></li>
<li><p><strong>number_of_probes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of failed probe attempts after which the backend endpoint is removed from rotation. The default value is 2. NumberOfProbes multiplied by intervalInSeconds value must be greater or equal to 10.Endpoints are returned to rotation when at least one probe is successful.</p></li>
<li><p><strong>port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Port on which the Probe queries the backend endpoint. Possible values range from 1 to 65535, inclusive.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the protocol of the end point. Possible values are <code class="docutils literal notranslate"><span class="pre">Http</span></code>, <code class="docutils literal notranslate"><span class="pre">Https</span></code> or <code class="docutils literal notranslate"><span class="pre">Tcp</span></code>. If Tcp is specified, a received ACK is required for the probe to be successful. If Http is specified, a 200 OK response from the specified URI is required for the probe to be successful.</p></li>
<li><p><strong>request_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI used for requesting health status from the backend endpoint. Required if protocol is set to Http. Otherwise, it is not allowed.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_probe.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_probe.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.Probe.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.Probe.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.lb.Probe.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.Probe.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.lb.Rule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.lb.</code><code class="sig-name descname">Rule</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_address_pool_id=None</em>, <em class="sig-param">backend_port=None</em>, <em class="sig-param">disable_outbound_snat=None</em>, <em class="sig-param">enable_floating_ip=None</em>, <em class="sig-param">enable_tcp_reset=None</em>, <em class="sig-param">frontend_ip_configuration_name=None</em>, <em class="sig-param">frontend_port=None</em>, <em class="sig-param">idle_timeout_in_minutes=None</em>, <em class="sig-param">load_distribution=None</em>, <em class="sig-param">loadbalancer_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">probe_id=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.Rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Load Balancer Rule.</p>
<blockquote>
<div><p><strong>NOTE</strong> When using this resource, the Load Balancer needs to have a FrontEnd IP Configuration Attached</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_address_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A reference to a Backend Address Pool over which this Load Balancing Rule operates.</p></li>
<li><p><strong>backend_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port used for internal connections on the endpoint. Possible values range between 0 and 65535, inclusive.</p></li>
<li><p><strong>disable_outbound_snat</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is snat enabled for this Load Balancer Rule? Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_floating_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Are the Floating IPs enabled for this Load Balncer Rule? A “floating” IP is reassigned to a secondary server in case the primary server fails. Required to configure a SQL AlwaysOn Availability Group. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_tcp_reset</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is TCP Reset enabled for this Load Balancer Rule? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>frontend_ip_configuration_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the frontend IP configuration to which the rule is associated.</p></li>
<li><p><strong>frontend_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 0 and 65534, inclusive.</p></li>
<li><p><strong>idle_timeout_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the idle timeout in minutes for TCP connections. Valid values are between <code class="docutils literal notranslate"><span class="pre">4</span></code> and <code class="docutils literal notranslate"><span class="pre">30</span></code> minutes. Defaults to <code class="docutils literal notranslate"><span class="pre">4</span></code> minutes.</p></li>
<li><p><strong>load_distribution</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the load balancing distribution type to be used by the Load Balancer. Possible values are: <code class="docutils literal notranslate"><span class="pre">Default</span></code> – The load balancer is configured to use a 5 tuple hash to map traffic to available servers. <code class="docutils literal notranslate"><span class="pre">SourceIP</span></code> – The load balancer is configured to use a 2 tuple hash to map traffic to available servers. <code class="docutils literal notranslate"><span class="pre">SourceIPProtocol</span></code> – The load balancer is configured to use a 3 tuple hash to map traffic to available servers. Also known as Session Persistence, where  the options are called <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Client</span> <span class="pre">IP</span></code> and <code class="docutils literal notranslate"><span class="pre">Client</span> <span class="pre">IP</span> <span class="pre">and</span> <span class="pre">Protocol</span></code> respectively.</p></li>
<li><p><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer in which to create the Rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the LB Rule.</p></li>
<li><p><strong>probe_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A reference to a Probe used by this Load Balancing Rule.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The transport protocol for the external endpoint. Possible values are <code class="docutils literal notranslate"><span class="pre">Tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">Udp</span></code> or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_rule.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.backend_address_pool_id">
<code class="sig-name descname">backend_address_pool_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.backend_address_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A reference to a Backend Address Pool over which this Load Balancing Rule operates.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.backend_port">
<code class="sig-name descname">backend_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.backend_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port used for internal connections on the endpoint. Possible values range between 0 and 65535, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.disable_outbound_snat">
<code class="sig-name descname">disable_outbound_snat</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.disable_outbound_snat" title="Permalink to this definition">¶</a></dt>
<dd><p>Is snat enabled for this Load Balancer Rule? Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.enable_floating_ip">
<code class="sig-name descname">enable_floating_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.enable_floating_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Are the Floating IPs enabled for this Load Balncer Rule? A “floating” IP is reassigned to a secondary server in case the primary server fails. Required to configure a SQL AlwaysOn Availability Group. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.enable_tcp_reset">
<code class="sig-name descname">enable_tcp_reset</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.enable_tcp_reset" title="Permalink to this definition">¶</a></dt>
<dd><p>Is TCP Reset enabled for this Load Balancer Rule? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.frontend_ip_configuration_name">
<code class="sig-name descname">frontend_ip_configuration_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.frontend_ip_configuration_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the frontend IP configuration to which the rule is associated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.frontend_port">
<code class="sig-name descname">frontend_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.frontend_port" title="Permalink to this definition">¶</a></dt>
<dd><p>The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 0 and 65534, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.idle_timeout_in_minutes">
<code class="sig-name descname">idle_timeout_in_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.idle_timeout_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the idle timeout in minutes for TCP connections. Valid values are between <code class="docutils literal notranslate"><span class="pre">4</span></code> and <code class="docutils literal notranslate"><span class="pre">30</span></code> minutes. Defaults to <code class="docutils literal notranslate"><span class="pre">4</span></code> minutes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.load_distribution">
<code class="sig-name descname">load_distribution</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.load_distribution" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the load balancing distribution type to be used by the Load Balancer. Possible values are: <code class="docutils literal notranslate"><span class="pre">Default</span></code> – The load balancer is configured to use a 5 tuple hash to map traffic to available servers. <code class="docutils literal notranslate"><span class="pre">SourceIP</span></code> – The load balancer is configured to use a 2 tuple hash to map traffic to available servers. <code class="docutils literal notranslate"><span class="pre">SourceIPProtocol</span></code> – The load balancer is configured to use a 3 tuple hash to map traffic to available servers. Also known as Session Persistence, where  the options are called <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Client</span> <span class="pre">IP</span></code> and <code class="docutils literal notranslate"><span class="pre">Client</span> <span class="pre">IP</span> <span class="pre">and</span> <span class="pre">Protocol</span></code> respectively.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.loadbalancer_id">
<code class="sig-name descname">loadbalancer_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.loadbalancer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Load Balancer in which to create the Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the LB Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.probe_id">
<code class="sig-name descname">probe_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.probe_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A reference to a Probe used by this Load Balancing Rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.protocol">
<code class="sig-name descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The transport protocol for the external endpoint. Possible values are <code class="docutils literal notranslate"><span class="pre">Tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">Udp</span></code> or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.lb.Rule.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.lb.Rule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.Rule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backend_address_pool_id=None</em>, <em class="sig-param">backend_port=None</em>, <em class="sig-param">disable_outbound_snat=None</em>, <em class="sig-param">enable_floating_ip=None</em>, <em class="sig-param">enable_tcp_reset=None</em>, <em class="sig-param">frontend_ip_configuration_id=None</em>, <em class="sig-param">frontend_ip_configuration_name=None</em>, <em class="sig-param">frontend_port=None</em>, <em class="sig-param">idle_timeout_in_minutes=None</em>, <em class="sig-param">load_distribution=None</em>, <em class="sig-param">loadbalancer_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">probe_id=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.Rule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Rule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backend_address_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A reference to a Backend Address Pool over which this Load Balancing Rule operates.</p></li>
<li><p><strong>backend_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port used for internal connections on the endpoint. Possible values range between 0 and 65535, inclusive.</p></li>
<li><p><strong>disable_outbound_snat</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is snat enabled for this Load Balancer Rule? Default <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_floating_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Are the Floating IPs enabled for this Load Balncer Rule? A “floating” IP is reassigned to a secondary server in case the primary server fails. Required to configure a SQL AlwaysOn Availability Group. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_tcp_reset</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is TCP Reset enabled for this Load Balancer Rule? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>frontend_ip_configuration_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the frontend IP configuration to which the rule is associated.</p></li>
<li><p><strong>frontend_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The port for the external endpoint. Port numbers for each Rule must be unique within the Load Balancer. Possible values range between 0 and 65534, inclusive.</p></li>
<li><p><strong>idle_timeout_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the idle timeout in minutes for TCP connections. Valid values are between <code class="docutils literal notranslate"><span class="pre">4</span></code> and <code class="docutils literal notranslate"><span class="pre">30</span></code> minutes. Defaults to <code class="docutils literal notranslate"><span class="pre">4</span></code> minutes.</p></li>
<li><p><strong>load_distribution</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the load balancing distribution type to be used by the Load Balancer. Possible values are: <code class="docutils literal notranslate"><span class="pre">Default</span></code> – The load balancer is configured to use a 5 tuple hash to map traffic to available servers. <code class="docutils literal notranslate"><span class="pre">SourceIP</span></code> – The load balancer is configured to use a 2 tuple hash to map traffic to available servers. <code class="docutils literal notranslate"><span class="pre">SourceIPProtocol</span></code> – The load balancer is configured to use a 3 tuple hash to map traffic to available servers. Also known as Session Persistence, where  the options are called <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Client</span> <span class="pre">IP</span></code> and <code class="docutils literal notranslate"><span class="pre">Client</span> <span class="pre">IP</span> <span class="pre">and</span> <span class="pre">Protocol</span></code> respectively.</p></li>
<li><p><strong>loadbalancer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Load Balancer in which to create the Rule.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the LB Rule.</p></li>
<li><p><strong>probe_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A reference to a Probe used by this Load Balancing Rule.</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The transport protocol for the external endpoint. Possible values are <code class="docutils literal notranslate"><span class="pre">Tcp</span></code>, <code class="docutils literal notranslate"><span class="pre">Udp</span></code> or <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_rule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/lb_rule.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.lb.Rule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.Rule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.lb.Rule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.Rule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.lb.get_backend_address_pool">
<code class="sig-prename descclassname">pulumi_azure.lb.</code><code class="sig-name descname">get_backend_address_pool</code><span class="sig-paren">(</span><em class="sig-param">loadbalancer_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.get_backend_address_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Load Balancer’s Backend Address Pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>loadbalancer_id</strong> (<em>str</em>) – The ID of the Load Balancer in which the Backend Address Pool exists.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Backend Address Pool.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/lb_backend_address_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/lb_backend_address_pool.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.lb.get_lb">
<code class="sig-prename descclassname">pulumi_azure.lb.</code><code class="sig-name descname">get_lb</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.lb.get_lb" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Load Balancer</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Load Balancer.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group in which the Load Balancer exists.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/lb.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/lb.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
