---
title: Module cdn
---

<div class="section" id="cdn">
<h1>cdn<a class="headerlink" href="#cdn" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_azure.cdn"></span><dl class="class">
<dt id="pulumi_azure.cdn.AwaitableGetProfileResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.cdn.</code><code class="descname">AwaitableGetProfileResult</code><span class="sig-paren">(</span><em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.AwaitableGetProfileResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.cdn.Endpoint">
<em class="property">class </em><code class="descclassname">pulumi_azure.cdn.</code><code class="descname">Endpoint</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>content_types_to_compresses=None</em>, <em>geo_filters=None</em>, <em>is_compression_enabled=None</em>, <em>is_http_allowed=None</em>, <em>is_https_allowed=None</em>, <em>location=None</em>, <em>name=None</em>, <em>optimization_type=None</em>, <em>origins=None</em>, <em>origin_host_header=None</em>, <em>origin_path=None</em>, <em>probe_path=None</em>, <em>profile_name=None</em>, <em>querystring_caching_behaviour=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.Endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A CDN Endpoint is the entity within a CDN Profile containing configuration information regarding caching behaviors and origins. The CDN Endpoint is exposed using the URL format <span class="raw-html-m2r"><endpointname></span>.azureedge.net.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>content_types_to_compresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings that indicates a content types on which compression will be applied. The value for the elements should be MIME types.</li>
<li><strong>geo_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Geo Filters for this CDN Endpoint. Each <code class="docutils literal notranslate"><span class="pre">geo_filter</span></code> block supports fields documented below.</li>
<li><strong>is_compression_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether compression is to be enabled. Defaults to false.</li>
<li><strong>is_http_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>is_https_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the CDN Endpoint. Changing this forces a new resource to be created.</li>
<li><strong>optimization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – What types of optimization should this CDN Endpoint optimize for? Possible values include <code class="docutils literal notranslate"><span class="pre">DynamicSiteAcceleration</span></code>, <code class="docutils literal notranslate"><span class="pre">GeneralMediaStreaming</span></code>, <code class="docutils literal notranslate"><span class="pre">GeneralWebDelivery</span></code>, <code class="docutils literal notranslate"><span class="pre">LargeFileDownload</span></code> and <code class="docutils literal notranslate"><span class="pre">VideoOnDemandMediaStreaming</span></code>.</li>
<li><strong>origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The set of origins of the CDN endpoint. When multiple origins exist, the first origin will be used as primary and rest will be used as failover options. Each <code class="docutils literal notranslate"><span class="pre">origin</span></code> block supports fields documented below.</li>
<li><strong>origin_host_header</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The host header CDN provider will send along with content requests to origins. Defaults to the host name of the origin.</li>
<li><strong>origin_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path used at for origin requests.</li>
<li><strong>probe_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the <code class="docutils literal notranslate"><span class="pre">origin_path</span></code>.</li>
<li><strong>profile_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CDN Profile to which to attach the CDN Endpoint.</li>
<li><strong>querystring_caching_behaviour</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets query string caching behavior. Allowed values are <code class="docutils literal notranslate"><span class="pre">IgnoreQueryString</span></code>, <code class="docutils literal notranslate"><span class="pre">BypassCaching</span></code> and <code class="docutils literal notranslate"><span class="pre">UseQueryString</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IgnoreQueryString</span></code>.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the CDN Endpoint.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/cdn_endpoint.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/cdn_endpoint.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.content_types_to_compresses">
<code class="descname">content_types_to_compresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.content_types_to_compresses" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of strings that indicates a content types on which compression will be applied. The value for the elements should be MIME types.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.geo_filters">
<code class="descname">geo_filters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.geo_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of Geo Filters for this CDN Endpoint. Each <code class="docutils literal notranslate"><span class="pre">geo_filter</span></code> block supports fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.is_compression_enabled">
<code class="descname">is_compression_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.is_compression_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether compression is to be enabled. Defaults to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.is_http_allowed">
<code class="descname">is_http_allowed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.is_http_allowed" title="Permalink to this definition">¶</a></dt>
<dd><p>Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.is_https_allowed">
<code class="descname">is_https_allowed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.is_https_allowed" title="Permalink to this definition">¶</a></dt>
<dd><p>Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
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
<dd><p>What types of optimization should this CDN Endpoint optimize for? Possible values include <code class="docutils literal notranslate"><span class="pre">DynamicSiteAcceleration</span></code>, <code class="docutils literal notranslate"><span class="pre">GeneralMediaStreaming</span></code>, <code class="docutils literal notranslate"><span class="pre">GeneralWebDelivery</span></code>, <code class="docutils literal notranslate"><span class="pre">LargeFileDownload</span></code> and <code class="docutils literal notranslate"><span class="pre">VideoOnDemandMediaStreaming</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.origins">
<code class="descname">origins</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.origins" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of origins of the CDN endpoint. When multiple origins exist, the first origin will be used as primary and rest will be used as failover options. Each <code class="docutils literal notranslate"><span class="pre">origin</span></code> block supports fields documented below.</p>
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
<dd><p>the path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the <code class="docutils literal notranslate"><span class="pre">origin_path</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.profile_name">
<code class="descname">profile_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.profile_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The CDN Profile to which to attach the CDN Endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Endpoint.querystring_caching_behaviour">
<code class="descname">querystring_caching_behaviour</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.querystring_caching_behaviour" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets query string caching behavior. Allowed values are <code class="docutils literal notranslate"><span class="pre">IgnoreQueryString</span></code>, <code class="docutils literal notranslate"><span class="pre">BypassCaching</span></code> and <code class="docutils literal notranslate"><span class="pre">UseQueryString</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IgnoreQueryString</span></code>.</p>
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

<dl class="staticmethod">
<dt id="pulumi_azure.cdn.Endpoint.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>content_types_to_compresses=None</em>, <em>geo_filters=None</em>, <em>host_name=None</em>, <em>is_compression_enabled=None</em>, <em>is_http_allowed=None</em>, <em>is_https_allowed=None</em>, <em>location=None</em>, <em>name=None</em>, <em>optimization_type=None</em>, <em>origins=None</em>, <em>origin_host_header=None</em>, <em>origin_path=None</em>, <em>probe_path=None</em>, <em>profile_name=None</em>, <em>querystring_caching_behaviour=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Endpoint resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] content_types_to_compresses: An array of strings that indicates a content types on which compression will be applied. The value for the elements should be MIME types.
:param pulumi.Input[list] geo_filters: A set of Geo Filters for this CDN Endpoint. Each <code class="docutils literal notranslate"><span class="pre">geo_filter</span></code> block supports fields documented below.
:param pulumi.Input[bool] is_compression_enabled: Indicates whether compression is to be enabled. Defaults to false.
:param pulumi.Input[bool] is_http_allowed: Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.
:param pulumi.Input[bool] is_https_allowed: Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.
:param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] name: Specifies the name of the CDN Endpoint. Changing this forces a new resource to be created.
:param pulumi.Input[str] optimization_type: What types of optimization should this CDN Endpoint optimize for? Possible values include <code class="docutils literal notranslate"><span class="pre">DynamicSiteAcceleration</span></code>, <code class="docutils literal notranslate"><span class="pre">GeneralMediaStreaming</span></code>, <code class="docutils literal notranslate"><span class="pre">GeneralWebDelivery</span></code>, <code class="docutils literal notranslate"><span class="pre">LargeFileDownload</span></code> and <code class="docutils literal notranslate"><span class="pre">VideoOnDemandMediaStreaming</span></code>.
:param pulumi.Input[list] origins: The set of origins of the CDN endpoint. When multiple origins exist, the first origin will be used as primary and rest will be used as failover options. Each <code class="docutils literal notranslate"><span class="pre">origin</span></code> block supports fields documented below.
:param pulumi.Input[str] origin_host_header: The host header CDN provider will send along with content requests to origins. Defaults to the host name of the origin.
:param pulumi.Input[str] origin_path: The path used at for origin requests.
:param pulumi.Input[str] probe_path: the path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the <code class="docutils literal notranslate"><span class="pre">origin_path</span></code>.
:param pulumi.Input[str] profile_name: The CDN Profile to which to attach the CDN Endpoint.
:param pulumi.Input[str] querystring_caching_behaviour: Sets query string caching behavior. Allowed values are <code class="docutils literal notranslate"><span class="pre">IgnoreQueryString</span></code>, <code class="docutils literal notranslate"><span class="pre">BypassCaching</span></code> and <code class="docutils literal notranslate"><span class="pre">UseQueryString</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IgnoreQueryString</span></code>.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the CDN Endpoint.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/cdn_endpoint.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/cdn_endpoint.html.markdown</a>.</div></blockquote>
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
<em class="property">class </em><code class="descclassname">pulumi_azure.cdn.</code><code class="descname">GetProfileResult</code><span class="sig-paren">(</span><em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.GetProfileResult" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="descclassname">pulumi_azure.cdn.</code><code class="descname">Profile</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.Profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a CDN Profile to create a collection of CDN Endpoints.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the CDN Profile. Changing this forces a
new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the CDN Profile.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pricing related information of current CDN profile. Accepted values are <code class="docutils literal notranslate"><span class="pre">Standard_Akamai</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_ChinaCdn</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_Microsoft</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_Verizon</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium_Verizon</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/cdn_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/cdn_profile.html.markdown</a>.</div></blockquote>
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
<dd><p>The pricing related information of current CDN profile. Accepted values are <code class="docutils literal notranslate"><span class="pre">Standard_Akamai</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_ChinaCdn</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_Microsoft</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_Verizon</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium_Verizon</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.cdn.Profile.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Profile.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_azure.cdn.Profile.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.Profile.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Profile resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] name: Specifies the name of the CDN Profile. Changing this forces a</p>
<blockquote>
<div>new resource to be created.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the CDN Profile.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pricing related information of current CDN profile. Accepted values are <code class="docutils literal notranslate"><span class="pre">Standard_Akamai</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_ChinaCdn</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_Microsoft</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_Verizon</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium_Verizon</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/cdn_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/cdn_profile.html.markdown</a>.</div></blockquote>
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
<code class="descclassname">pulumi_azure.cdn.</code><code class="descname">get_profile</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.get_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing CDN Profile.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/cdn_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/cdn_profile.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
