---
title: Module privatelink
title_tag: Module privatelink | Package pulumi_azure | Python SDK
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
<span class="target" id="module-pulumi_azure.privatelink"></span><dl class="py class">
<dt id="pulumi_azure.privatelink.AwaitableGetEndpointConnectionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatelink.</code><code class="sig-name descname">AwaitableGetEndpointConnectionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_service_connections</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.AwaitableGetEndpointConnectionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.privatelink.AwaitableGetServiceEndpointConnectionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatelink.</code><code class="sig-name descname">AwaitableGetServiceEndpointConnectionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_endpoint_connections</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.AwaitableGetServiceEndpointConnectionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.privatelink.AwaitableGetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatelink.</code><code class="sig-name descname">AwaitableGetServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">alias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_approval_subscription_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_proxy_protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_frontend_ip_configuration_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nat_ip_configurations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility_subscription_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.AwaitableGetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.privatelink.Endpoint">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatelink.</code><code class="sig-name descname">Endpoint</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_service_connection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.Endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Private Endpoint.</p>
<blockquote>
<div><p><strong>NOTE</strong> Private Endpoint is currently in Public Preview.</p>
</div></blockquote>
<p>Azure Private Endpoint is a network interface that connects you privately and securely to a service powered by Azure Private Link. Private Endpoint uses a private IP address from your VNet, effectively bringing the service into your VNet. The service could be an Azure service such as Azure Storage, SQL, etc. or your own Private Link Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Name of the Private Endpoint. Changing this forces a new resource to be created.</p></li>
<li><p><strong>private_service_connection</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">private_service_connection</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Name of the Resource Group within which the Private Endpoint should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet from which Private IP Addresses will be allocated for this Private Endpoint. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>private_service_connection</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isManualConnection</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Does the Private Endpoint require Manual Approval from the remote resource owner? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Name of the Private Service Connection. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateConnectionResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Private Link Enabled Remote Resource which this Private Endpoint should be connected to. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The private IP address associated with the private endpoint, note that you will have a private IP address assigned to the private endpoint even if the connection request was <code class="docutils literal notranslate"><span class="pre">Rejected</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMessage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A message passed to the owner of the remote resource when the private endpoint attempts to establish the connection to the remote resource. The request message can be a maximum of <code class="docutils literal notranslate"><span class="pre">140</span></code> characters in length. Only valid if <code class="docutils literal notranslate"><span class="pre">is_manual_connection</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subresourceNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of subresource names which the Private Endpoint is able to connect to. <code class="docutils literal notranslate"><span class="pre">subresource_names</span></code> corresponds to <code class="docutils literal notranslate"><span class="pre">group_id</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.privatelink.Endpoint.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.Endpoint.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.privatelink.Endpoint.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.Endpoint.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Name of the Private Endpoint. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.privatelink.Endpoint.private_service_connection">
<code class="sig-name descname">private_service_connection</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.Endpoint.private_service_connection" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">private_service_connection</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isManualConnection</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Does the Private Endpoint require Manual Approval from the remote resource owner? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the Name of the Private Service Connection. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateConnectionResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Private Link Enabled Remote Resource which this Private Endpoint should be connected to. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The private IP address associated with the private endpoint, note that you will have a private IP address assigned to the private endpoint even if the connection request was <code class="docutils literal notranslate"><span class="pre">Rejected</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMessage</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A message passed to the owner of the remote resource when the private endpoint attempts to establish the connection to the remote resource. The request message can be a maximum of <code class="docutils literal notranslate"><span class="pre">140</span></code> characters in length. Only valid if <code class="docutils literal notranslate"><span class="pre">is_manual_connection</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subresourceNames</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of subresource names which the Private Endpoint is able to connect to. <code class="docutils literal notranslate"><span class="pre">subresource_names</span></code> corresponds to <code class="docutils literal notranslate"><span class="pre">group_id</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.privatelink.Endpoint.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.Endpoint.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Name of the Resource Group within which the Private Endpoint should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.privatelink.Endpoint.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.Endpoint.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Subnet from which Private IP Addresses will be allocated for this Private Endpoint. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.privatelink.Endpoint.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.Endpoint.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.privatelink.Endpoint.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_service_connection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnet_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.Endpoint.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Endpoint resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Name of the Private Endpoint. Changing this forces a new resource to be created.</p></li>
<li><p><strong>private_service_connection</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">private_service_connection</span></code> block as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Name of the Resource Group within which the Private Endpoint should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet from which Private IP Addresses will be allocated for this Private Endpoint. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>private_service_connection</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isManualConnection</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Does the Private Endpoint require Manual Approval from the remote resource owner? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Name of the Private Service Connection. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">privateConnectionResourceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Private Link Enabled Remote Resource which this Private Endpoint should be connected to. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_ip_address</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The private IP address associated with the private endpoint, note that you will have a private IP address assigned to the private endpoint even if the connection request was <code class="docutils literal notranslate"><span class="pre">Rejected</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMessage</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A message passed to the owner of the remote resource when the private endpoint attempts to establish the connection to the remote resource. The request message can be a maximum of <code class="docutils literal notranslate"><span class="pre">140</span></code> characters in length. Only valid if <code class="docutils literal notranslate"><span class="pre">is_manual_connection</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subresourceNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of subresource names which the Private Endpoint is able to connect to. <code class="docutils literal notranslate"><span class="pre">subresource_names</span></code> corresponds to <code class="docutils literal notranslate"><span class="pre">group_id</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.privatelink.Endpoint.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.Endpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.privatelink.Endpoint.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.Endpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.privatelink.GetEndpointConnectionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatelink.</code><code class="sig-name descname">GetEndpointConnectionResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_service_connections</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.GetEndpointConnectionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getEndpointConnection.</p>
<dl class="py attribute">
<dt id="pulumi_azure.privatelink.GetEndpointConnectionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetEndpointConnectionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.privatelink.GetEndpointConnectionResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetEndpointConnectionResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The supported Azure location where the resource exists.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.privatelink.GetEndpointConnectionResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetEndpointConnectionResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the private endpoint.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.privatelink.GetServiceEndpointConnectionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatelink.</code><code class="sig-name descname">GetServiceEndpointConnectionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_endpoint_connections</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceEndpointConnectionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServiceEndpointConnections.</p>
<dl class="py attribute">
<dt id="pulumi_azure.privatelink.GetServiceEndpointConnectionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceEndpointConnectionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.privatelink.GetServiceEndpointConnectionsResult.service_name">
<code class="sig-name descname">service_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceEndpointConnectionsResult.service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the private link service.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.privatelink.GetServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.privatelink.</code><code class="sig-name descname">GetServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">alias</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_approval_subscription_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_proxy_protocol</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancer_frontend_ip_configuration_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nat_ip_configurations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility_subscription_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getService.</p>
<dl class="py attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.alias">
<code class="sig-name descname">alias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.alias" title="Permalink to this definition">¶</a></dt>
<dd><p>The alias is a globally unique name for your private link service which Azure generates for you. Your can use this alias to request a connection to your private link service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.auto_approval_subscription_ids">
<code class="sig-name descname">auto_approval_subscription_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.auto_approval_subscription_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of subscription(s) globally unique identifiers that will be auto approved to use the private link service.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.enable_proxy_protocol">
<code class="sig-name descname">enable_proxy_protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.enable_proxy_protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>Does the Private Link Service support the Proxy Protocol?</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.load_balancer_frontend_ip_configuration_ids">
<code class="sig-name descname">load_balancer_frontend_ip_configuration_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.load_balancer_frontend_ip_configuration_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of Standard Load Balancer(SLB) resource IDs. The Private Link service is tied to the frontend IP address of a SLB. All traffic destined for the private link service will reach the frontend of the SLB. You can configure SLB rules to direct this traffic to appropriate backend pools where your applications are running.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The supported Azure location where the resource exists.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of private link service NAT IP configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.nat_ip_configurations">
<code class="sig-name descname">nat_ip_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.nat_ip_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">nat_ip_configuration</span></code> block as defined below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.privatelink.GetServiceResult.visibility_subscription_ids">
<code class="sig-name descname">visibility_subscription_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.privatelink.GetServiceResult.visibility_subscription_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of subscription(s) globally unique identifiers(GUID) that will be able to see the private link service.</p>
</dd></dl>

</dd></dl>

<dl class="py function">
<dt id="pulumi_azure.privatelink.get_endpoint_connection">
<code class="sig-prename descclassname">pulumi_azure.privatelink.</code><code class="sig-name descname">get_endpoint_connection</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.get_endpoint_connection" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access the connection status information about an existing Private Endpoint Connection.</p>
<blockquote>
<div><p><strong>NOTE</strong> Private Endpoint is currently in Public Preview.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the Name of the private endpoint.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the Name of the Resource Group within which the private endpoint exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azure.privatelink.get_service">
<code class="sig-prename descclassname">pulumi_azure.privatelink.</code><code class="sig-name descname">get_service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.get_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Private Link Service.</p>
<blockquote>
<div><p><strong>NOTE</strong> Private Link is currently in Public Preview.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the private link service.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group in which the private link service resides.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azure.privatelink.get_service_endpoint_connections">
<code class="sig-prename descclassname">pulumi_azure.privatelink.</code><code class="sig-name descname">get_service_endpoint_connections</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.privatelink.get_service_endpoint_connections" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access endpoint connection information about an existing Private Link Service.</p>
<blockquote>
<div><p><strong>NOTE</strong> Private Link is currently in Public Preview.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group in which the private link service resides.</p></li>
<li><p><strong>service_id</strong> (<em>str</em>) – The resource ID of the private link service.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
