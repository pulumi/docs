---
---

<div class="section" id="trafficmanager">
<h1>trafficmanager<a class="headerlink" href="#trafficmanager" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azure">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azure/issues">terraform-providers/terraform-provider-azure repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_azure.trafficmanager"></span><dl class="class">
<dt id="pulumi_azure.trafficmanager.Endpoint">
<em class="property">class </em><code class="descclassname">pulumi_azure.trafficmanager.</code><code class="descname">Endpoint</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>endpoint_location=None</em>, <em>endpoint_status=None</em>, <em>geo_mappings=None</em>, <em>min_child_endpoints=None</em>, <em>name=None</em>, <em>priority=None</em>, <em>profile_name=None</em>, <em>resource_group_name=None</em>, <em>target=None</em>, <em>target_resource_id=None</em>, <em>type=None</em>, <em>weight=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Traffic Manager Endpoint.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>endpoint_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure location of the Endpoint,
this must be specified for Profiles using the <code class="docutils literal notranslate"><span class="pre">Performance</span></code> routing method
if the Endpoint is of either type <code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code> or <code class="docutils literal notranslate"><span class="pre">externalEndpoints</span></code>.
For Endpoints of type <code class="docutils literal notranslate"><span class="pre">azureEndpoints</span></code> the value will be taken from the
location of the Azure target resource.</li>
<li><strong>endpoint_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the Endpoint, can be set to
either <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</li>
<li><strong>geo_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Geographic Regions used to distribute traffic, such as <code class="docutils literal notranslate"><span class="pre">WORLD</span></code>, <code class="docutils literal notranslate"><span class="pre">UK</span></code> or <code class="docutils literal notranslate"><span class="pre">DE</span></code>. The same location can’t be specified in two endpoints. <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/trafficmanager/geographichierarchies/getdefault">See the Geographic Hierarchies documentation for more information</a>.</li>
<li><strong>min_child_endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – This argument specifies the minimum number
of endpoints that must be ‘online’ in the child profile in order for the
parent profile to direct traffic to any of the endpoints in that child
profile. This argument only applies to Endpoints of type <code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code>
and defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Traffic Manager endpoint. Changing this forces a
new resource to be created.</li>
<li><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the priority of this Endpoint, this must be
specified for Profiles using the <code class="docutils literal notranslate"><span class="pre">Priority</span></code> traffic routing method. Supports
values between 1 and 1000, with no Endpoints sharing the same value. If
omitted the value will be computed in order of creation.</li>
<li><strong>profile_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Traffic Manager Profile to attach
create the Traffic Manager endpoint.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the Traffic Manager endpoint.</li>
<li><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FQDN DNS name of the target. This argument must be
provided for an endpoint of type <code class="docutils literal notranslate"><span class="pre">externalEndpoints</span></code>, for other types it
will be computed.</li>
<li><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource id of an Azure resource to
target. This argument must be provided for an endpoint of type
<code class="docutils literal notranslate"><span class="pre">azureEndpoints</span></code> or <code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code>.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Endpoint type, must be one of:</li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>weight</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies how much traffic should be distributed to this
endpoint, this must be specified for Profiles using the  <code class="docutils literal notranslate"><span class="pre">Weighted</span></code> traffic
routing method. Supports values between 1 and 1000.</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/traffic_manager_endpoint.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/traffic_manager_endpoint.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.endpoint_location">
<code class="descname">endpoint_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.endpoint_location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure location of the Endpoint,
this must be specified for Profiles using the <code class="docutils literal notranslate"><span class="pre">Performance</span></code> routing method
if the Endpoint is of either type <code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code> or <code class="docutils literal notranslate"><span class="pre">externalEndpoints</span></code>.
For Endpoints of type <code class="docutils literal notranslate"><span class="pre">azureEndpoints</span></code> the value will be taken from the
location of the Azure target resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.endpoint_status">
<code class="descname">endpoint_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.endpoint_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the Endpoint, can be set to
either <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.geo_mappings">
<code class="descname">geo_mappings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.geo_mappings" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Geographic Regions used to distribute traffic, such as <code class="docutils literal notranslate"><span class="pre">WORLD</span></code>, <code class="docutils literal notranslate"><span class="pre">UK</span></code> or <code class="docutils literal notranslate"><span class="pre">DE</span></code>. The same location can’t be specified in two endpoints. <a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/trafficmanager/geographichierarchies/getdefault">See the Geographic Hierarchies documentation for more information</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.min_child_endpoints">
<code class="descname">min_child_endpoints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.min_child_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>This argument specifies the minimum number
of endpoints that must be ‘online’ in the child profile in order for the
parent profile to direct traffic to any of the endpoints in that child
profile. This argument only applies to Endpoints of type <code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code>
and defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
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
specified for Profiles using the <code class="docutils literal notranslate"><span class="pre">Priority</span></code> traffic routing method. Supports
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
provided for an endpoint of type <code class="docutils literal notranslate"><span class="pre">externalEndpoints</span></code>, for other types it
will be computed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.target_resource_id">
<code class="descname">target_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.target_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource id of an Azure resource to
target. This argument must be provided for an endpoint of type
<code class="docutils literal notranslate"><span class="pre">azureEndpoints</span></code> or <code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Endpoint type, must be one of:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">azureEndpoints</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">externalEndpoints</span></code></li>
<li><code class="docutils literal notranslate"><span class="pre">nestedEndpoints</span></code></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.Endpoint.weight">
<code class="descname">weight</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.weight" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies how much traffic should be distributed to this
endpoint, this must be specified for Profiles using the  <code class="docutils literal notranslate"><span class="pre">Weighted</span></code> traffic
routing method. Supports values between 1 and 1000.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.trafficmanager.Endpoint.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.trafficmanager.Endpoint.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Endpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.trafficmanager.GetGeographicalLocationResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.trafficmanager.</code><code class="descname">GetGeographicalLocationResult</code><span class="sig-paren">(</span><em>name=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.GetGeographicalLocationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGeographicalLocation.</p>
<dl class="attribute">
<dt id="pulumi_azure.trafficmanager.GetGeographicalLocationResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.trafficmanager.GetGeographicalLocationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.trafficmanager.Profile">
<em class="property">class </em><code class="descclassname">pulumi_azure.trafficmanager.</code><code class="descname">Profile</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>dns_configs=None</em>, <em>monitor_configs=None</em>, <em>name=None</em>, <em>profile_status=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>traffic_routing_method=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Traffic Manager Profile to which multiple endpoints can be attached.</p>
<p>The Traffic Manager is created with the location <code class="docutils literal notranslate"><span class="pre">global</span></code>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>dns_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – This block specifies the DNS configuration of the
Profile, it supports the fields documented below.</li>
<li><strong>monitor_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – This block specifies the Endpoint monitoring
configuration for the Profile, it supports the fields documented below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual network. Changing this forces a
new resource to be created.</li>
<li><strong>profile_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the profile, can be set to either
<code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the virtual network.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>traffic_routing_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the algorithm used to route traffic, possible values are:</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/traffic_manager_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/traffic_manager_profile.html.markdown</a>.</div></blockquote>
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
<code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>.</p>
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
<dd><p>Specifies the algorithm used to route traffic, possible values are:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">Geographic</span></code> - Traffic is routed based on Geographic regions specified in the Endpoint.</li>
<li><code class="docutils literal notranslate"><span class="pre">MultiValue</span></code>- All healthy Endpoints are returned.  MultiValue routing method works only if all the endpoints of type ‘External’ and are specified as IPv4 or IPv6 addresses.</li>
<li><code class="docutils literal notranslate"><span class="pre">Performance</span></code> - Traffic is routed via the User’s closest Endpoint</li>
<li><code class="docutils literal notranslate"><span class="pre">Priority</span></code> - Traffic is routed to the Endpoint with the lowest <code class="docutils literal notranslate"><span class="pre">priority</span></code> value.</li>
<li><code class="docutils literal notranslate"><span class="pre">Subnet</span></code> - Traffic is routed based on a mapping of sets of end-user IP address ranges to a specific Endpoint within a Traffic Manager profile.</li>
<li><code class="docutils literal notranslate"><span class="pre">Weighted</span></code> - Traffic is spread across Endpoints proportional to their <code class="docutils literal notranslate"><span class="pre">weight</span></code> value.</li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.trafficmanager.Profile.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.trafficmanager.Profile.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.Profile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.trafficmanager.get_geographical_location">
<code class="descclassname">pulumi_azure.trafficmanager.</code><code class="descname">get_geographical_location</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.trafficmanager.get_geographical_location" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access the ID of a specified Traffic Manager Geographical Location within the Geographical Hierarchy.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/traffic_manager_geographical_location.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/traffic_manager_geographical_location.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
