<div class="section" id="module-pulumi_azure.trafficmanager">
<span id="trafficmanager"></span><h1>trafficmanager<a class="headerlink" href="#module-pulumi_azure.trafficmanager" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.trafficmanager.Endpoint">
<em class="property">class </em><code class="descclassname">pulumi_azure.trafficmanager.</code><code class="descname">Endpoint</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>endpoint_location=None</em>, <em>endpoint_status=None</em>, <em>geo_mappings=None</em>, <em>min_child_endpoints=None</em>, <em>name=None</em>, <em>priority=None</em>, <em>profile_name=None</em>, <em>resource_group_name=None</em>, <em>target=None</em>, <em>target_resource_id=None</em>, <em>type=None</em>, <em>weight=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Traffic Manager Endpoint.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>endpoint_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure location of the Endpoint,
this must be specified for Profiles using the <cite>Performance</cite> routing method
if the Endpoint is of either type <cite>nestedEndpoints</cite> or <cite>externalEndpoints</cite>.
For Endpoints of type <cite>azureEndpoints</cite> the value will be taken from the
location of the Azure target resource.</li>
<li><strong>endpoint_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the Endpoint, can be set to
either <cite>Enabled</cite> or <cite>Disabled</cite>. Defaults to <cite>Enabled</cite>.</li>
<li><strong>geo_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Geographic Regions used to distribute traffic, such as <cite>WORLD</cite>, <cite>UK</cite> or <cite>DE</cite>. The same location can’t be specified in two endpoints. [See the Geographic Hierarchies documentation for more information](<a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/trafficmanager/geographichierarchies/getdefault">https://docs.microsoft.com/en-us/rest/api/trafficmanager/geographichierarchies/getdefault</a>).</li>
<li><strong>min_child_endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – This argument specifies the minimum number
of endpoints that must be ‘online’ in the child profile in order for the
parent profile to direct traffic to any of the endpoints in that child
profile. This argument only applies to Endpoints of type <cite>nestedEndpoints</cite>
and defaults to <cite>1</cite>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Traffic Manager endpoint. Changing this forces a
new resource to be created.</li>
<li><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies the priority of this Endpoint, this must be
specified for Profiles using the <cite>Priority</cite> traffic routing method. Supports
values between 1 and 1000, with no Endpoints sharing the same value. If
omitted the value will be computed in order of creation.</li>
<li><strong>profile_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Traffic Manager Profile to attach
create the Traffic Manager endpoint.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the Traffic Manager endpoint.</li>
<li><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FQDN DNS name of the target. This argument must be
provided for an endpoint of type <cite>externalEndpoints</cite>, for other types it
will be computed.</li>
<li><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource id of an Azure resource to
target. This argument must be provided for an endpoint of type
<cite>azureEndpoints</cite> or <cite>nestedEndpoints</cite>.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Endpoint type, must be one of:
- <cite>azureEndpoints</cite>
- <cite>externalEndpoints</cite>
- <cite>nestedEndpoints</cite></li>
<li><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies how much traffic should be distributed to this
endpoint, this must be specified for Profiles using the  <cite>Weighted</cite> traffic
routing method. Supports values between 1 and 1000.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.endpoint_location">
<code class="descname">endpoint_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.endpoint_location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure location of the Endpoint,
this must be specified for Profiles using the <cite>Performance</cite> routing method
if the Endpoint is of either type <cite>nestedEndpoints</cite> or <cite>externalEndpoints</cite>.
For Endpoints of type <cite>azureEndpoints</cite> the value will be taken from the
location of the Azure target resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.endpoint_status">
<code class="descname">endpoint_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.endpoint_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the Endpoint, can be set to
either <cite>Enabled</cite> or <cite>Disabled</cite>. Defaults to <cite>Enabled</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.geo_mappings">
<code class="descname">geo_mappings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.geo_mappings" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Geographic Regions used to distribute traffic, such as <cite>WORLD</cite>, <cite>UK</cite> or <cite>DE</cite>. The same location can’t be specified in two endpoints. [See the Geographic Hierarchies documentation for more information](<a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/trafficmanager/geographichierarchies/getdefault">https://docs.microsoft.com/en-us/rest/api/trafficmanager/geographichierarchies/getdefault</a>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.min_child_endpoints">
<code class="descname">min_child_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.min_child_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>This argument specifies the minimum number
of endpoints that must be ‘online’ in the child profile in order for the
parent profile to direct traffic to any of the endpoints in that child
profile. This argument only applies to Endpoints of type <cite>nestedEndpoints</cite>
and defaults to <cite>1</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Traffic Manager endpoint. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.priority">
<code class="descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the priority of this Endpoint, this must be
specified for Profiles using the <cite>Priority</cite> traffic routing method. Supports
values between 1 and 1000, with no Endpoints sharing the same value. If
omitted the value will be computed in order of creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.profile_name">
<code class="descname">profile_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.profile_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Traffic Manager Profile to attach
create the Traffic Manager endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the Traffic Manager endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.target">
<code class="descname">target</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.target" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN DNS name of the target. This argument must be
provided for an endpoint of type <cite>externalEndpoints</cite>, for other types it
will be computed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.target_resource_id">
<code class="descname">target_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.target_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource id of an Azure resource to
target. This argument must be provided for an endpoint of type
<cite>azureEndpoints</cite> or <cite>nestedEndpoints</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Endpoint type, must be one of:
- <cite>azureEndpoints</cite>
- <cite>externalEndpoints</cite>
- <cite>nestedEndpoints</cite></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.weight">
<code class="descname">weight</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.weight" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies how much traffic should be distributed to this
endpoint, this must be specified for Profiles using the  <cite>Weighted</cite> traffic
routing method. Supports values between 1 and 1000.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.trafficmanager.Endpoint.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.trafficmanager.Endpoint.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.trafficmanager.GetGeographicalLocationResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.trafficmanager.</code><code class="descname">GetGeographicalLocationResult</code><span class="sig-paren">(</span><em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.GetGeographicalLocationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGeographicalLocation.</p>
<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.GetGeographicalLocationResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.GetGeographicalLocationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.trafficmanager.Profile">
<em class="property">class </em><code class="descclassname">pulumi_azure.trafficmanager.</code><code class="descname">Profile</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>dns_configs=None</em>, <em>monitor_configs=None</em>, <em>name=None</em>, <em>profile_status=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>traffic_routing_method=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Traffic Manager Profile to which multiple endpoints can be attached.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>dns_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – This block specifies the DNS configuration of the
Profile, it supports the fields documented below.</li>
<li><strong>monitor_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – This block specifies the Endpoint monitoring
configuration for the Profile, it supports the fields documented below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual network. Changing this forces a
new resource to be created.</li>
<li><strong>profile_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the profile, can be set to either
<cite>Enabled</cite> or <cite>Disabled</cite>. Defaults to <cite>Enabled</cite>.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the virtual network.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>traffic_routing_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the algorithm used to route
traffic, possible values are:
- <cite>Geographic</cite> - Traffic is routed based on Geographic regions specified in the Endpoint.
- <cite>Performance</cite> - Traffic is routed via the User’s closest Endpoint
- <cite>Weighted</cite> - Traffic is spread across Endpoints proportional to their <cite>weight</cite> value.
- <cite>Priority</cite> - Traffic is routed to the Endpoint with the lowest <cite>priority</cite> value.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Profile.dns_configs">
<code class="descname">dns_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.dns_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>This block specifies the DNS configuration of the
Profile, it supports the fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Profile.fqdn">
<code class="descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the created Profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Profile.monitor_configs">
<code class="descname">monitor_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.monitor_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>This block specifies the Endpoint monitoring
configuration for the Profile, it supports the fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Profile.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the virtual network. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Profile.profile_status">
<code class="descname">profile_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.profile_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the profile, can be set to either
<cite>Enabled</cite> or <cite>Disabled</cite>. Defaults to <cite>Enabled</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Profile.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the virtual network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Profile.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Profile.traffic_routing_method">
<code class="descname">traffic_routing_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.traffic_routing_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the algorithm used to route
traffic, possible values are:
- <cite>Geographic</cite> - Traffic is routed based on Geographic regions specified in the Endpoint.
- <cite>Performance</cite> - Traffic is routed via the User’s closest Endpoint
- <cite>Weighted</cite> - Traffic is spread across Endpoints proportional to their <cite>weight</cite> value.
- <cite>Priority</cite> - Traffic is routed to the Endpoint with the lowest <cite>priority</cite> value.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.trafficmanager.Profile.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.trafficmanager.Profile.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_azure.trafficmanager.get_geographical_location">
<code class="descclassname">pulumi_azure.trafficmanager.</code><code class="descname">get_geographical_location</code><span class="sig-paren">(</span><em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.get_geographical_location" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access the ID of a specified Traffic Manager Geographical Location within the Geographical Hierarchy.</p>
</dd></dl>

</div>
