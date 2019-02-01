<div class="section" id="module-pulumi_azure.cdn">
<span id="cdn"></span><h1>cdn<a class="headerlink" href="#module-pulumi_azure.cdn" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.cdn.Endpoint">
<em class="property">class </em><code class="descclassname">pulumi_azure.cdn.</code><code class="descname">Endpoint</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>content_types_to_compresses=None</em>, <em>geo_filters=None</em>, <em>is_compression_enabled=None</em>, <em>is_http_allowed=None</em>, <em>is_https_allowed=None</em>, <em>location=None</em>, <em>name=None</em>, <em>optimization_type=None</em>, <em>origins=None</em>, <em>origin_host_header=None</em>, <em>origin_path=None</em>, <em>probe_path=None</em>, <em>profile_name=None</em>, <em>querystring_caching_behaviour=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.Endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A CDN Endpoint is the entity within a CDN Profile containing configuration information regarding caching behaviors and origins. The CDN Endpoint is exposed using the URL format &lt;endpointname&gt;.azureedge.net.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>content_types_to_compresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings that indicates a content types on which compression will be applied. The value for the elements should be MIME types.</li>
<li><strong>geo_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Geo Filters for this CDN Endpoint. Each <cite>geo_filter</cite> block supports fields documented below.</li>
<li><strong>is_compression_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether compression is to be enabled. Defaults to false.</li>
<li><strong>is_http_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defaults to <cite>true</cite>.</li>
<li><strong>is_https_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defaults to <cite>true</cite>.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the CDN Endpoint. Changing this forces a new resource to be created.</li>
<li><strong>optimization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – What types of optimization should this CDN Endpoint optimize for? Possible values include <cite>DynamicSiteAcceleration</cite>, <cite>GeneralMediaStreaming</cite>, <cite>GeneralWebDelivery</cite>, <cite>LargeFileDownload</cite> and <cite>VideoOnDemandMediaStreaming</cite>.</li>
<li><strong>origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The set of origins of the CDN endpoint. When multiple origins exist, the first origin will be used as primary and rest will be used as failover options. Each <cite>origin</cite> block supports fields documented below.</li>
<li><strong>origin_host_header</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The host header CDN provider will send along with content requests to origins. Defaults to the host name of the origin.</li>
<li><strong>origin_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path used at for origin requests.</li>
<li><strong>probe_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the <cite>origin_path</cite>.</li>
<li><strong>profile_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CDN Profile to which to attach the CDN Endpoint.</li>
<li><strong>querystring_caching_behaviour</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets query string caching behavior. Allowed values are <cite>IgnoreQueryString</cite>, <cite>BypassCaching</cite> and <cite>UseQueryString</cite>. Defaults to <cite>IgnoreQueryString</cite>.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the CDN Endpoint.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.content_types_to_compresses">
<code class="descname">content_types_to_compresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.content_types_to_compresses" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of strings that indicates a content types on which compression will be applied. The value for the elements should be MIME types.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.geo_filters">
<code class="descname">geo_filters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.geo_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of Geo Filters for this CDN Endpoint. Each <cite>geo_filter</cite> block supports fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.is_compression_enabled">
<code class="descname">is_compression_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.is_compression_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether compression is to be enabled. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.is_http_allowed">
<code class="descname">is_http_allowed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.is_http_allowed" title="Permalink to this definition">¶</a></dt>
<dd><p>Defaults to <cite>true</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.is_https_allowed">
<code class="descname">is_https_allowed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.is_https_allowed" title="Permalink to this definition">¶</a></dt>
<dd><p>Defaults to <cite>true</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the CDN Endpoint. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.optimization_type">
<code class="descname">optimization_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.optimization_type" title="Permalink to this definition">¶</a></dt>
<dd><p>What types of optimization should this CDN Endpoint optimize for? Possible values include <cite>DynamicSiteAcceleration</cite>, <cite>GeneralMediaStreaming</cite>, <cite>GeneralWebDelivery</cite>, <cite>LargeFileDownload</cite> and <cite>VideoOnDemandMediaStreaming</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.origins">
<code class="descname">origins</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.origins" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of origins of the CDN endpoint. When multiple origins exist, the first origin will be used as primary and rest will be used as failover options. Each <cite>origin</cite> block supports fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.origin_host_header">
<code class="descname">origin_host_header</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.origin_host_header" title="Permalink to this definition">¶</a></dt>
<dd><p>The host header CDN provider will send along with content requests to origins. Defaults to the host name of the origin.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.origin_path">
<code class="descname">origin_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.origin_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path used at for origin requests.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.probe_path">
<code class="descname">probe_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.probe_path" title="Permalink to this definition">¶</a></dt>
<dd><p>the path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the <cite>origin_path</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.profile_name">
<code class="descname">profile_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.profile_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The CDN Profile to which to attach the CDN Endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.querystring_caching_behaviour">
<code class="descname">querystring_caching_behaviour</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.querystring_caching_behaviour" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets query string caching behavior. Allowed values are <cite>IgnoreQueryString</cite>, <cite>BypassCaching</cite> and <cite>UseQueryString</cite>. Defaults to <cite>IgnoreQueryString</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the CDN Endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.cdn.Endpoint.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cdn.Endpoint.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cdn.GetProfileResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.cdn.</code><code class="descname">GetProfileResult</code><span class="sig-paren">(</span><em>location=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.GetProfileResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProfile.</p>
<dl class="attribute">
<dt id="pulumi_azure.cdn.GetProfileResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.GetProfileResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region where the resource exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.GetProfileResult.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.GetProfileResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The pricing related information of current CDN profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.GetProfileResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.GetProfileResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.GetProfileResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.GetProfileResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.cdn.Profile">
<em class="property">class </em><code class="descclassname">pulumi_azure.cdn.</code><code class="descname">Profile</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.Profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a CDN Profile to create a collection of CDN Endpoints.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the CDN Profile. Changing this forces a
new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the CDN Profile.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pricing related information of current CDN profile. Accepted values are <cite>Standard_Akamai</cite>, <cite>Standard_ChinaCdn</cite>, <cite>Standard_Microsoft</cite>, <cite>Standard_Verizon</cite> or <cite>Premium_Verizon</cite>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.cdn.Profile.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Profile.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Profile.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Profile.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the CDN Profile. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Profile.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Profile.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the CDN Profile.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Profile.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Profile.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The pricing related information of current CDN profile. Accepted values are <cite>Standard_Akamai</cite>, <cite>Standard_ChinaCdn</cite>, <cite>Standard_Microsoft</cite>, <cite>Standard_Verizon</cite> or <cite>Premium_Verizon</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Profile.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Profile.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.cdn.Profile.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.Profile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cdn.Profile.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.Profile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cdn.get_profile">
<code class="descclassname">pulumi_azure.cdn.</code><code class="descname">get_profile</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.get_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing CDN Profile.</p>
</dd></dl>

</div>
