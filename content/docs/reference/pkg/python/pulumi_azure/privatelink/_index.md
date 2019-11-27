---
title: Module privatelink
linktitle: privatelink
notitle: true
---

<div class="section" id="privatelink">
<h1>privatelink<a class="headerlink" href="#privatelink" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.privatelink"></span><dl class="class">
<dt id="pulumi_azure.privatelink.AwaitableGetServiceEndpointConnectionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatelink.</code><code class="sig-name descname">AwaitableGetServiceEndpointConnectionsResult</code><span class="sig-paren">(</span><em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">private_endpoint_connections=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.AwaitableGetServiceEndpointConnectionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.privatelink.AwaitableGetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatelink.</code><code class="sig-name descname">AwaitableGetServiceResult</code><span class="sig-paren">(</span><em class="sig-param">alias=None</em>, <em class="sig-param">auto_approval_subscription_ids=None</em>, <em class="sig-param">load_balancer_frontend_ip_configuration_ids=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">nat_ip_configuration=None</em>, <em class="sig-param">network_interface_ids=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">visibility_subscription_ids=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.AwaitableGetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.privatelink.GetServiceEndpointConnectionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatelink.</code><code class="sig-name descname">GetServiceEndpointConnectionsResult</code><span class="sig-paren">(</span><em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">private_endpoint_connections=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceEndpointConnectionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServiceEndpointConnections.</p>
<dl class="attribute">
<dt id="pulumi_azure.privatelink.GetServiceEndpointConnectionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceEndpointConnectionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.privatelink.GetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatelink.</code><code class="sig-name descname">GetServiceResult</code><span class="sig-paren">(</span><em class="sig-param">alias=None</em>, <em class="sig-param">auto_approval_subscription_ids=None</em>, <em class="sig-param">load_balancer_frontend_ip_configuration_ids=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">nat_ip_configuration=None</em>, <em class="sig-param">network_interface_ids=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">visibility_subscription_ids=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getService.</p>
<dl class="attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.alias">
<code class="sig-name descname">alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.alias" title="Permalink to this definition">¶</a></dt>
<dd><p>The alias is a globally unique name for your private link service which Azure generates for you. Your can use this alias to request a connection to your private link service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.auto_approval_subscription_ids">
<code class="sig-name descname">auto_approval_subscription_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.auto_approval_subscription_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of subscription(s) globally unique identifiers that will be auto approved to use the private link service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.load_balancer_frontend_ip_configuration_ids">
<code class="sig-name descname">load_balancer_frontend_ip_configuration_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.load_balancer_frontend_ip_configuration_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of Standard Load Balancer(SLB) resource IDs. The Private Link service is tied to the frontend IP address of a SLB. All traffic destined for the private link service will reach the frontend of the SLB. You can configure SLB rules to direct this traffic to appropriate backend pools where your applications are running.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The supported Azure location where the resource exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of private link service NAT IP configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.nat_ip_configuration">
<code class="sig-name descname">nat_ip_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.nat_ip_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">nat_ip_configuration</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.visibility_subscription_ids">
<code class="sig-name descname">visibility_subscription_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.visibility_subscription_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of subscription(s) globally unique identifiers(GUID) that will be able to see the private link service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_azure.privatelink.get_service">
<code class="sig-prename descclassname">pulumi_azure.privatelink.</code><code class="sig-name descname">get_service</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.get_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Private Link Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the private link service.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group in which the private link service resides.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/private_link_service.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/private_link_service.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.privatelink.get_service_endpoint_connections">
<code class="sig-prename descclassname">pulumi_azure.privatelink.</code><code class="sig-name descname">get_service_endpoint_connections</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.get_service_endpoint_connections" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access endpoint connection information about an existing Private Link Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the private link service.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group in which the private link service resides.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/private_link_service_endpoint_connections.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/private_link_service_endpoint_connections.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
