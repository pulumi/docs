---
title: Module trafficmanager
title_tag: Module trafficmanager | Package pulumi_azure | Python SDK
linktitle: trafficmanager
notitle: true
---

<div class="section" id="trafficmanager">
<h1>trafficmanager<a class="headerlink" href="#trafficmanager" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.trafficmanager"></span><dl class="class">
<dt id="pulumi_azure.trafficmanager.AwaitableGetGeographicalLocationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.trafficmanager.</code><code class="sig-name descname">AwaitableGetGeographicalLocationResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.AwaitableGetGeographicalLocationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.trafficmanager.Endpoint">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.trafficmanager.</code><code class="sig-name descname">Endpoint</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">custom_headers=None</em>, <em class="sig-param">endpoint_location=None</em>, <em class="sig-param">endpoint_status=None</em>, <em class="sig-param">geo_mappings=None</em>, <em class="sig-param">min_child_endpoints=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">profile_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">subnets=None</em>, <em class="sig-param">target=None</em>, <em class="sig-param">target_resource_id=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">weight=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.trafficmanager.Endpoint.custom_headers">
<code class="sig-name descname">custom_headers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.custom_headers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">custom_header</span></code> blocks as defined below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Traffic Manager endpoint. Changing this forces a
new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.endpoint_location">
<code class="sig-name descname">endpoint_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.endpoint_location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure location of the Endpoint,
this must be specified for Profiles using the <code class="docutils literal notranslate"><span class="pre">Performance</span></code> routing method
if the Endpoint is of either type <code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code> or <code class="docutils literal notranslate"><span class="pre">externalEndpoints</span></code>.
For Endpoints of type <code class="docutils literal notranslate"><span class="pre">azureEndpoints</span></code> the value will be taken from the
location of the Azure target resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.endpoint_status">
<code class="sig-name descname">endpoint_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.endpoint_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the Endpoint, can be set to
either <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.geo_mappings">
<code class="sig-name descname">geo_mappings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.geo_mappings" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Geographic Regions used to distribute traffic, such as <code class="docutils literal notranslate"><span class="pre">WORLD</span></code>, <code class="docutils literal notranslate"><span class="pre">UK</span></code> or <code class="docutils literal notranslate"><span class="pre">DE</span></code>. The same location can’t be specified in two endpoints. <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/trafficmanager/geographichierarchies/getdefault">See the Geographic Hierarchies documentation for more information</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.min_child_endpoints">
<code class="sig-name descname">min_child_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.min_child_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>This argument specifies the minimum number
of endpoints that must be ‘online’ in the child profile in order for the
parent profile to direct traffic to any of the endpoints in that child
profile. This argument only applies to Endpoints of type <code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code>
and defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Traffic Manager endpoint. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the priority of this Endpoint, this must be
specified for Profiles using the <code class="docutils literal notranslate"><span class="pre">Priority</span></code> traffic routing method. Supports
values between 1 and 1000, with no Endpoints sharing the same value. If
omitted the value will be computed in order of creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.profile_name">
<code class="sig-name descname">profile_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.profile_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Traffic Manager Profile to attach
create the Traffic Manager endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the Traffic Manager endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.subnets">
<code class="sig-name descname">subnets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.subnets" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">subnet</span></code> blocks as defined below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">first</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">last</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.target">
<code class="sig-name descname">target</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.target" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN DNS name of the target. This argument must be
provided for an endpoint of type <code class="docutils literal notranslate"><span class="pre">externalEndpoints</span></code>, for other types it
will be computed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.target_resource_id">
<code class="sig-name descname">target_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.target_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource id of an Azure resource to
target. This argument must be provided for an endpoint of type
<code class="docutils literal notranslate"><span class="pre">azureEndpoints</span></code> or <code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Endpoint type, must be one of:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">azureEndpoints</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">externalEndpoints</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.weight">
<code class="sig-name descname">weight</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.weight" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies how much traffic should be distributed to this
endpoint, this must be specified for Profiles using the  <code class="docutils literal notranslate"><span class="pre">Weighted</span></code> traffic
routing method. Supports values between 1 and 1000.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.trafficmanager.Endpoint.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">custom_headers=None</em>, <em class="sig-param">endpoint_location=None</em>, <em class="sig-param">endpoint_monitor_status=None</em>, <em class="sig-param">endpoint_status=None</em>, <em class="sig-param">geo_mappings=None</em>, <em class="sig-param">min_child_endpoints=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">profile_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">subnets=None</em>, <em class="sig-param">target=None</em>, <em class="sig-param">target_resource_id=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">weight=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Endpoint resource’s state with the given name, id, and optional extra
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
<dt id="pulumi_azure.trafficmanager.Endpoint.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.trafficmanager.Endpoint.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.trafficmanager.GetGeographicalLocationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.trafficmanager.</code><code class="sig-name descname">GetGeographicalLocationResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.GetGeographicalLocationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGeographicalLocation.</p>
<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.GetGeographicalLocationResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.GetGeographicalLocationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.trafficmanager.Profile">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.trafficmanager.</code><code class="sig-name descname">Profile</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dns_config=None</em>, <em class="sig-param">monitor_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">profile_status=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">traffic_routing_method=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.trafficmanager.Profile.dns_config">
<code class="sig-name descname">dns_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.dns_config" title="Permalink to this definition">¶</a></dt>
<dd><p>This block specifies the DNS configuration of the Profile, it supports the fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">relativeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Profile.fqdn">
<code class="sig-name descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the created Profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Profile.monitor_config">
<code class="sig-name descname">monitor_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.monitor_config" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.trafficmanager.Profile.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Traffic Manager profile. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Profile.profile_status">
<code class="sig-name descname">profile_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.profile_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the profile, can be set to either <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Profile.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Traffic Manager profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Profile.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Profile.traffic_routing_method">
<code class="sig-name descname">traffic_routing_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.traffic_routing_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the algorithm used to route traffic, possible values are:</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.trafficmanager.Profile.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dns_config=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">monitor_config=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">profile_status=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">traffic_routing_method=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Profile resource’s state with the given name, id, and optional extra
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
<dt id="pulumi_azure.trafficmanager.Profile.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.trafficmanager.Profile.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.trafficmanager.get_geographical_location">
<code class="sig-prename descclassname">pulumi_azure.trafficmanager.</code><code class="sig-name descname">get_geographical_location</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.get_geographical_location" title="Permalink to this definition">¶</a></dt>
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

</div>
