---
title: Module cdn
title_tag: Module cdn | Package pulumi_azure | Python SDK
linktitle: cdn
notitle: true
---

<div class="section" id="cdn">
<h1>cdn<a class="headerlink" href="#cdn" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.cdn"></span><dl class="py class">
<dt id="pulumi_azure.cdn.AwaitableGetProfileResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.cdn.</code><code class="sig-name descname">AwaitableGetProfileResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.AwaitableGetProfileResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.cdn.Endpoint">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.cdn.</code><code class="sig-name descname">Endpoint</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_types_to_compresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delivery_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">geo_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_delivery_rule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_compression_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_http_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_https_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optimization_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_host_header</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">probe_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">profile_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">querystring_caching_behaviour</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.Endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>A CDN Endpoint is the entity within a CDN Profile containing configuration information regarding caching behaviours and origins. The CDN Endpoint is exposed using the URL format <span class="raw-html-m2r"><endpointname></span>.azureedge.net.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West Europe&quot;</span><span class="p">)</span>
<span class="n">example_profile</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cdn</span><span class="o">.</span><span class="n">Profile</span><span class="p">(</span><span class="s2">&quot;exampleProfile&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">sku</span><span class="o">=</span><span class="s2">&quot;Standard_Verizon&quot;</span><span class="p">)</span>
<span class="n">example_endpoint</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cdn</span><span class="o">.</span><span class="n">Endpoint</span><span class="p">(</span><span class="s2">&quot;exampleEndpoint&quot;</span><span class="p">,</span>
    <span class="n">profile_name</span><span class="o">=</span><span class="n">example_profile</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">origin</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;example&quot;</span><span class="p">,</span>
        <span class="s2">&quot;hostName&quot;</span><span class="p">:</span> <span class="s2">&quot;www.example.com&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content_types_to_compresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings that indicates a content types on which compression will be applied. The value for the elements should be MIME types.</p></li>
<li><p><strong>delivery_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Rules for the rules engine. An endpoint can contain up until 4 of those rules that consist of conditions and actions. A <code class="docutils literal notranslate"><span class="pre">delivery_rule</span></code> blocks as defined below.</p></li>
<li><p><strong>geo_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Geo Filters for this CDN Endpoint. Each <code class="docutils literal notranslate"><span class="pre">geo_filter</span></code> block supports fields documented below.</p></li>
<li><p><strong>global_delivery_rule</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Actions that are valid for all resources regardless of any conditions. A <code class="docutils literal notranslate"><span class="pre">global_delivery_rule</span></code> block as defined below.</p></li>
<li><p><strong>is_compression_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether compression is to be enabled. Defaults to false.</p></li>
<li><p><strong>is_http_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>is_https_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the origin. This is an arbitrary value. However, this value needs to be unique under the endpoint. Changing this forces a new resource to be created.</p></li>
<li><p><strong>optimization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – What types of optimization should this CDN Endpoint optimize for? Possible values include <code class="docutils literal notranslate"><span class="pre">DynamicSiteAcceleration</span></code>, <code class="docutils literal notranslate"><span class="pre">GeneralMediaStreaming</span></code>, <code class="docutils literal notranslate"><span class="pre">GeneralWebDelivery</span></code>, <code class="docutils literal notranslate"><span class="pre">LargeFileDownload</span></code> and <code class="docutils literal notranslate"><span class="pre">VideoOnDemandMediaStreaming</span></code>.</p></li>
<li><p><strong>origin_host_header</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The host header CDN provider will send along with content requests to origins. Defaults to the host name of the origin.</p></li>
<li><p><strong>origin_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path used at for origin requests.</p></li>
<li><p><strong>origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The set of origins of the CDN endpoint. When multiple origins exist, the first origin will be used as primary and rest will be used as failover options. Each <code class="docutils literal notranslate"><span class="pre">origin</span></code> block supports fields documented below.</p></li>
<li><p><strong>probe_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the <code class="docutils literal notranslate"><span class="pre">origin_path</span></code>.</p></li>
<li><p><strong>profile_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CDN Profile to which to attach the CDN Endpoint.</p></li>
<li><p><strong>querystring_caching_behaviour</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets query string caching behavior. Allowed values are <code class="docutils literal notranslate"><span class="pre">IgnoreQueryString</span></code>, <code class="docutils literal notranslate"><span class="pre">BypassCaching</span></code> and <code class="docutils literal notranslate"><span class="pre">UseQueryString</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IgnoreQueryString</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the CDN Endpoint.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>delivery_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheExpirationAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cache_expiration_action</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">behavior</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behavior of the cache. Valid values are <code class="docutils literal notranslate"><span class="pre">BypassCache</span></code>, <code class="docutils literal notranslate"><span class="pre">Override</span></code> and <code class="docutils literal notranslate"><span class="pre">SetIfMissing</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Duration of the cache. Only allowed when <code class="docutils literal notranslate"><span class="pre">behavior</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Override</span></code> or <code class="docutils literal notranslate"><span class="pre">SetIfMissing</span></code>. Format: <code class="docutils literal notranslate"><span class="pre">[d.]hh:mm:ss</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheKeyQueryStringAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cache_key_query_string_action</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">behavior</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behavior of the cache key for query strings. Valid values are <code class="docutils literal notranslate"><span class="pre">Exclude</span></code>, <code class="docutils literal notranslate"><span class="pre">ExcludeAll</span></code>, <code class="docutils literal notranslate"><span class="pre">Include</span></code> and <code class="docutils literal notranslate"><span class="pre">IncludeAll</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comma separated list of parameter values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookiesConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cookies_condition</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of values for the cookie.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the cookie.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">device_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Desktop</span></code> and <code class="docutils literal notranslate"><span class="pre">Mobile</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Equal</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpVersionConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">http_version_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">0.9</span></code>, <code class="docutils literal notranslate"><span class="pre">1.0</span></code>, <code class="docutils literal notranslate"><span class="pre">1.1</span></code> and <code class="docutils literal notranslate"><span class="pre">2.0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Equal</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">modifyRequestHeaderActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">modify_request_header_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Action to be executed on a header value. Valid values are <code class="docutils literal notranslate"><span class="pre">Append</span></code>, <code class="docutils literal notranslate"><span class="pre">Delete</span></code> and <code class="docutils literal notranslate"><span class="pre">Overwrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the header. Only needed when <code class="docutils literal notranslate"><span class="pre">action</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Append</span></code> or <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">modifyResponseHeaderActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">modify_response_header_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Action to be executed on a header value. Valid values are <code class="docutils literal notranslate"><span class="pre">Append</span></code>, <code class="docutils literal notranslate"><span class="pre">Delete</span></code> and <code class="docutils literal notranslate"><span class="pre">Overwrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the header. Only needed when <code class="docutils literal notranslate"><span class="pre">action</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Append</span></code> or <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this Delivery Rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The order used for this rule, which must be larger than 1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">postArgConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">post_arg_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the post arg.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryStringConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">query_string_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteAddressConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">remote_address_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of string values. For <code class="docutils literal notranslate"><span class="pre">GeoMatch</span></code> <code class="docutils literal notranslate"><span class="pre">operator</span></code> this should be a list of country codes (e.g. <code class="docutils literal notranslate"><span class="pre">US</span></code> or <code class="docutils literal notranslate"><span class="pre">DE</span></code>). List of IP address if <code class="docutils literal notranslate"><span class="pre">operator</span></code> equals to <code class="docutils literal notranslate"><span class="pre">IPMatch</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">GeoMatch</span></code> and <code class="docutils literal notranslate"><span class="pre">IPMatch</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestBodyConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">request_body_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestHeaderConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">request_header_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of header values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMethodCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">request_method_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code> and <code class="docutils literal notranslate"><span class="pre">PUT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Equal</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestSchemeCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">request_scheme_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> and <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Equal</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestUriConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">request_uri_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlFileExtensionConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_file_extension_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlFileNameConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_file_name_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlPathConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_path_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlRedirectAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_redirect_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fragment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the fragment part of the URL. This value must not start with a <code class="docutils literal notranslate"><span class="pre">#</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the hostname part of the URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the path part of the URL. This value must begin with a <code class="docutils literal notranslate"><span class="pre">/</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the protocol part of the URL. Valid values are <code class="docutils literal notranslate"><span class="pre">Http</span></code> and <code class="docutils literal notranslate"><span class="pre">Https</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the query string part of the URL. This value must not start with a <code class="docutils literal notranslate"><span class="pre">?</span></code> or <code class="docutils literal notranslate"><span class="pre">&amp;</span></code> and must be in <code class="docutils literal notranslate"><span class="pre">&lt;key&gt;=&lt;value&gt;</span></code> format separated by <code class="docutils literal notranslate"><span class="pre">&amp;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of the redirect. Valid values are <code class="docutils literal notranslate"><span class="pre">Found</span></code>, <code class="docutils literal notranslate"><span class="pre">Moved</span></code>, <code class="docutils literal notranslate"><span class="pre">PermanentRedirect</span></code> and <code class="docutils literal notranslate"><span class="pre">TemporaryRedirect</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlRewriteAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_rewrite_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This value must start with a <code class="docutils literal notranslate"><span class="pre">/</span></code> and can’t be longer than 260 characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preserveUnmatchedPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourcePattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This value must start with a <code class="docutils literal notranslate"><span class="pre">/</span></code> and can’t be longer than 260 characters.</p></li>
</ul>
</li>
</ul>
<p>The <strong>geo_filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Action of the Geo Filter. Possible values include <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Block</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">countryCodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A List of two letter country codes (e.g. <code class="docutils literal notranslate"><span class="pre">US</span></code>, <code class="docutils literal notranslate"><span class="pre">GB</span></code>) to be associated with this Geo Filter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">relative_path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The relative path applicable to geo filter.</p></li>
</ul>
<p>The <strong>global_delivery_rule</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheExpirationAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cache_expiration_action</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">behavior</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behavior of the cache. Valid values are <code class="docutils literal notranslate"><span class="pre">BypassCache</span></code>, <code class="docutils literal notranslate"><span class="pre">Override</span></code> and <code class="docutils literal notranslate"><span class="pre">SetIfMissing</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Duration of the cache. Only allowed when <code class="docutils literal notranslate"><span class="pre">behavior</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Override</span></code> or <code class="docutils literal notranslate"><span class="pre">SetIfMissing</span></code>. Format: <code class="docutils literal notranslate"><span class="pre">[d.]hh:mm:ss</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheKeyQueryStringAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cache_key_query_string_action</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">behavior</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behavior of the cache key for query strings. Valid values are <code class="docutils literal notranslate"><span class="pre">Exclude</span></code>, <code class="docutils literal notranslate"><span class="pre">ExcludeAll</span></code>, <code class="docutils literal notranslate"><span class="pre">Include</span></code> and <code class="docutils literal notranslate"><span class="pre">IncludeAll</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comma separated list of parameter values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">modifyRequestHeaderActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">modify_request_header_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Action to be executed on a header value. Valid values are <code class="docutils literal notranslate"><span class="pre">Append</span></code>, <code class="docutils literal notranslate"><span class="pre">Delete</span></code> and <code class="docutils literal notranslate"><span class="pre">Overwrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the header. Only needed when <code class="docutils literal notranslate"><span class="pre">action</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Append</span></code> or <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">modifyResponseHeaderActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">modify_response_header_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Action to be executed on a header value. Valid values are <code class="docutils literal notranslate"><span class="pre">Append</span></code>, <code class="docutils literal notranslate"><span class="pre">Delete</span></code> and <code class="docutils literal notranslate"><span class="pre">Overwrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the header. Only needed when <code class="docutils literal notranslate"><span class="pre">action</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Append</span></code> or <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlRedirectAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_redirect_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fragment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the fragment part of the URL. This value must not start with a <code class="docutils literal notranslate"><span class="pre">#</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the hostname part of the URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the path part of the URL. This value must begin with a <code class="docutils literal notranslate"><span class="pre">/</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the protocol part of the URL. Valid values are <code class="docutils literal notranslate"><span class="pre">Http</span></code> and <code class="docutils literal notranslate"><span class="pre">Https</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the query string part of the URL. This value must not start with a <code class="docutils literal notranslate"><span class="pre">?</span></code> or <code class="docutils literal notranslate"><span class="pre">&amp;</span></code> and must be in <code class="docutils literal notranslate"><span class="pre">&lt;key&gt;=&lt;value&gt;</span></code> format separated by <code class="docutils literal notranslate"><span class="pre">&amp;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of the redirect. Valid values are <code class="docutils literal notranslate"><span class="pre">Found</span></code>, <code class="docutils literal notranslate"><span class="pre">Moved</span></code>, <code class="docutils literal notranslate"><span class="pre">PermanentRedirect</span></code> and <code class="docutils literal notranslate"><span class="pre">TemporaryRedirect</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlRewriteAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_rewrite_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This value must start with a <code class="docutils literal notranslate"><span class="pre">/</span></code> and can’t be longer than 260 characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preserveUnmatchedPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourcePattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This value must start with a <code class="docutils literal notranslate"><span class="pre">/</span></code> and can’t be longer than 260 characters.</p></li>
</ul>
</li>
</ul>
<p>The <strong>origins</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A string that determines the hostname/IP address of the origin server. This string can be a domain name, Storage Account endpoint, Web App endpoint, IPv4 address or IPv6 address. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTP port of the origin. Defaults to <code class="docutils literal notranslate"><span class="pre">80</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpsPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTPS port of the origin. Defaults to <code class="docutils literal notranslate"><span class="pre">443</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the origin. This is an arbitrary value. However, this value needs to be unique under the endpoint. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.content_types_to_compresses">
<code class="sig-name descname">content_types_to_compresses</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.content_types_to_compresses" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of strings that indicates a content types on which compression will be applied. The value for the elements should be MIME types.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.delivery_rules">
<code class="sig-name descname">delivery_rules</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.delivery_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Rules for the rules engine. An endpoint can contain up until 4 of those rules that consist of conditions and actions. A <code class="docutils literal notranslate"><span class="pre">delivery_rule</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheExpirationAction</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cache_expiration_action</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">behavior</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The behavior of the cache. Valid values are <code class="docutils literal notranslate"><span class="pre">BypassCache</span></code>, <code class="docutils literal notranslate"><span class="pre">Override</span></code> and <code class="docutils literal notranslate"><span class="pre">SetIfMissing</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Duration of the cache. Only allowed when <code class="docutils literal notranslate"><span class="pre">behavior</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Override</span></code> or <code class="docutils literal notranslate"><span class="pre">SetIfMissing</span></code>. Format: <code class="docutils literal notranslate"><span class="pre">[d.]hh:mm:ss</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheKeyQueryStringAction</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cache_key_query_string_action</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">behavior</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The behavior of the cache key for query strings. Valid values are <code class="docutils literal notranslate"><span class="pre">Exclude</span></code>, <code class="docutils literal notranslate"><span class="pre">ExcludeAll</span></code>, <code class="docutils literal notranslate"><span class="pre">Include</span></code> and <code class="docutils literal notranslate"><span class="pre">IncludeAll</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Comma separated list of parameter values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookiesConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cookies_condition</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of values for the cookie.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the cookie.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">device_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Desktop</span></code> and <code class="docutils literal notranslate"><span class="pre">Mobile</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Equal</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpVersionConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">http_version_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">0.9</span></code>, <code class="docutils literal notranslate"><span class="pre">1.0</span></code>, <code class="docutils literal notranslate"><span class="pre">1.1</span></code> and <code class="docutils literal notranslate"><span class="pre">2.0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Equal</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">modifyRequestHeaderActions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">modify_request_header_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Action to be executed on a header value. Valid values are <code class="docutils literal notranslate"><span class="pre">Append</span></code>, <code class="docutils literal notranslate"><span class="pre">Delete</span></code> and <code class="docutils literal notranslate"><span class="pre">Overwrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of the header. Only needed when <code class="docutils literal notranslate"><span class="pre">action</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Append</span></code> or <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">modifyResponseHeaderActions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">modify_response_header_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Action to be executed on a header value. Valid values are <code class="docutils literal notranslate"><span class="pre">Append</span></code>, <code class="docutils literal notranslate"><span class="pre">Delete</span></code> and <code class="docutils literal notranslate"><span class="pre">Overwrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of the header. Only needed when <code class="docutils literal notranslate"><span class="pre">action</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Append</span></code> or <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name which should be used for this Delivery Rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The order used for this rule, which must be larger than 1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">postArgConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">post_arg_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the post arg.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryStringConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">query_string_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteAddressConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">remote_address_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of string values. For <code class="docutils literal notranslate"><span class="pre">GeoMatch</span></code> <code class="docutils literal notranslate"><span class="pre">operator</span></code> this should be a list of country codes (e.g. <code class="docutils literal notranslate"><span class="pre">US</span></code> or <code class="docutils literal notranslate"><span class="pre">DE</span></code>). List of IP address if <code class="docutils literal notranslate"><span class="pre">operator</span></code> equals to <code class="docutils literal notranslate"><span class="pre">IPMatch</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">GeoMatch</span></code> and <code class="docutils literal notranslate"><span class="pre">IPMatch</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestBodyConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">request_body_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestHeaderConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">request_header_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of header values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMethodCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">request_method_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code> and <code class="docutils literal notranslate"><span class="pre">PUT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Equal</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestSchemeCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">request_scheme_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> and <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Equal</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestUriConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">request_uri_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlFileExtensionConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_file_extension_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlFileNameConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_file_name_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlPathConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_path_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlRedirectAction</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_redirect_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fragment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the fragment part of the URL. This value must not start with a <code class="docutils literal notranslate"><span class="pre">#</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the hostname part of the URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the path part of the URL. This value must begin with a <code class="docutils literal notranslate"><span class="pre">/</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the protocol part of the URL. Valid values are <code class="docutils literal notranslate"><span class="pre">Http</span></code> and <code class="docutils literal notranslate"><span class="pre">Https</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryString</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the query string part of the URL. This value must not start with a <code class="docutils literal notranslate"><span class="pre">?</span></code> or <code class="docutils literal notranslate"><span class="pre">&amp;</span></code> and must be in <code class="docutils literal notranslate"><span class="pre">&lt;key&gt;=&lt;value&gt;</span></code> format separated by <code class="docutils literal notranslate"><span class="pre">&amp;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Type of the redirect. Valid values are <code class="docutils literal notranslate"><span class="pre">Found</span></code>, <code class="docutils literal notranslate"><span class="pre">Moved</span></code>, <code class="docutils literal notranslate"><span class="pre">PermanentRedirect</span></code> and <code class="docutils literal notranslate"><span class="pre">TemporaryRedirect</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlRewriteAction</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_rewrite_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - This value must start with a <code class="docutils literal notranslate"><span class="pre">/</span></code> and can’t be longer than 260 characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preserveUnmatchedPath</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourcePattern</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - This value must start with a <code class="docutils literal notranslate"><span class="pre">/</span></code> and can’t be longer than 260 characters.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.geo_filters">
<code class="sig-name descname">geo_filters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.geo_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of Geo Filters for this CDN Endpoint. Each <code class="docutils literal notranslate"><span class="pre">geo_filter</span></code> block supports fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Action of the Geo Filter. Possible values include <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Block</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">countryCodes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A List of two letter country codes (e.g. <code class="docutils literal notranslate"><span class="pre">US</span></code>, <code class="docutils literal notranslate"><span class="pre">GB</span></code>) to be associated with this Geo Filter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">relative_path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The relative path applicable to geo filter.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.global_delivery_rule">
<code class="sig-name descname">global_delivery_rule</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.global_delivery_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Actions that are valid for all resources regardless of any conditions. A <code class="docutils literal notranslate"><span class="pre">global_delivery_rule</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheExpirationAction</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cache_expiration_action</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">behavior</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The behavior of the cache. Valid values are <code class="docutils literal notranslate"><span class="pre">BypassCache</span></code>, <code class="docutils literal notranslate"><span class="pre">Override</span></code> and <code class="docutils literal notranslate"><span class="pre">SetIfMissing</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Duration of the cache. Only allowed when <code class="docutils literal notranslate"><span class="pre">behavior</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Override</span></code> or <code class="docutils literal notranslate"><span class="pre">SetIfMissing</span></code>. Format: <code class="docutils literal notranslate"><span class="pre">[d.]hh:mm:ss</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheKeyQueryStringAction</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cache_key_query_string_action</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">behavior</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The behavior of the cache key for query strings. Valid values are <code class="docutils literal notranslate"><span class="pre">Exclude</span></code>, <code class="docutils literal notranslate"><span class="pre">ExcludeAll</span></code>, <code class="docutils literal notranslate"><span class="pre">Include</span></code> and <code class="docutils literal notranslate"><span class="pre">IncludeAll</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Comma separated list of parameter values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">modifyRequestHeaderActions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">modify_request_header_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Action to be executed on a header value. Valid values are <code class="docutils literal notranslate"><span class="pre">Append</span></code>, <code class="docutils literal notranslate"><span class="pre">Delete</span></code> and <code class="docutils literal notranslate"><span class="pre">Overwrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of the header. Only needed when <code class="docutils literal notranslate"><span class="pre">action</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Append</span></code> or <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">modifyResponseHeaderActions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">modify_response_header_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Action to be executed on a header value. Valid values are <code class="docutils literal notranslate"><span class="pre">Append</span></code>, <code class="docutils literal notranslate"><span class="pre">Delete</span></code> and <code class="docutils literal notranslate"><span class="pre">Overwrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of the header. Only needed when <code class="docutils literal notranslate"><span class="pre">action</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Append</span></code> or <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlRedirectAction</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_redirect_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fragment</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the fragment part of the URL. This value must not start with a <code class="docutils literal notranslate"><span class="pre">#</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the hostname part of the URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the path part of the URL. This value must begin with a <code class="docutils literal notranslate"><span class="pre">/</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the protocol part of the URL. Valid values are <code class="docutils literal notranslate"><span class="pre">Http</span></code> and <code class="docutils literal notranslate"><span class="pre">Https</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryString</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the query string part of the URL. This value must not start with a <code class="docutils literal notranslate"><span class="pre">?</span></code> or <code class="docutils literal notranslate"><span class="pre">&amp;</span></code> and must be in <code class="docutils literal notranslate"><span class="pre">&lt;key&gt;=&lt;value&gt;</span></code> format separated by <code class="docutils literal notranslate"><span class="pre">&amp;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Type of the redirect. Valid values are <code class="docutils literal notranslate"><span class="pre">Found</span></code>, <code class="docutils literal notranslate"><span class="pre">Moved</span></code>, <code class="docutils literal notranslate"><span class="pre">PermanentRedirect</span></code> and <code class="docutils literal notranslate"><span class="pre">TemporaryRedirect</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlRewriteAction</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_rewrite_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - This value must start with a <code class="docutils literal notranslate"><span class="pre">/</span></code> and can’t be longer than 260 characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preserveUnmatchedPath</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourcePattern</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - This value must start with a <code class="docutils literal notranslate"><span class="pre">/</span></code> and can’t be longer than 260 characters.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.host_name">
<code class="sig-name descname">host_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.host_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A string that determines the hostname/IP address of the origin server. This string can be a domain name, Storage Account endpoint, Web App endpoint, IPv4 address or IPv6 address. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.is_compression_enabled">
<code class="sig-name descname">is_compression_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.is_compression_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether compression is to be enabled. Defaults to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.is_http_allowed">
<code class="sig-name descname">is_http_allowed</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.is_http_allowed" title="Permalink to this definition">¶</a></dt>
<dd><p>Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.is_https_allowed">
<code class="sig-name descname">is_https_allowed</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.is_https_allowed" title="Permalink to this definition">¶</a></dt>
<dd><p>Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the origin. This is an arbitrary value. However, this value needs to be unique under the endpoint. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.optimization_type">
<code class="sig-name descname">optimization_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.optimization_type" title="Permalink to this definition">¶</a></dt>
<dd><p>What types of optimization should this CDN Endpoint optimize for? Possible values include <code class="docutils literal notranslate"><span class="pre">DynamicSiteAcceleration</span></code>, <code class="docutils literal notranslate"><span class="pre">GeneralMediaStreaming</span></code>, <code class="docutils literal notranslate"><span class="pre">GeneralWebDelivery</span></code>, <code class="docutils literal notranslate"><span class="pre">LargeFileDownload</span></code> and <code class="docutils literal notranslate"><span class="pre">VideoOnDemandMediaStreaming</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.origin_host_header">
<code class="sig-name descname">origin_host_header</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.origin_host_header" title="Permalink to this definition">¶</a></dt>
<dd><p>The host header CDN provider will send along with content requests to origins. Defaults to the host name of the origin.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.origin_path">
<code class="sig-name descname">origin_path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.origin_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path used at for origin requests.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.origins">
<code class="sig-name descname">origins</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.origins" title="Permalink to this definition">¶</a></dt>
<dd><p>The set of origins of the CDN endpoint. When multiple origins exist, the first origin will be used as primary and rest will be used as failover options. Each <code class="docutils literal notranslate"><span class="pre">origin</span></code> block supports fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A string that determines the hostname/IP address of the origin server. This string can be a domain name, Storage Account endpoint, Web App endpoint, IPv4 address or IPv6 address. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpPort</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The HTTP port of the origin. Defaults to <code class="docutils literal notranslate"><span class="pre">80</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpsPort</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The HTTPS port of the origin. Defaults to <code class="docutils literal notranslate"><span class="pre">443</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the origin. This is an arbitrary value. However, this value needs to be unique under the endpoint. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.probe_path">
<code class="sig-name descname">probe_path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.probe_path" title="Permalink to this definition">¶</a></dt>
<dd><p>the path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the <code class="docutils literal notranslate"><span class="pre">origin_path</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.profile_name">
<code class="sig-name descname">profile_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.profile_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The CDN Profile to which to attach the CDN Endpoint.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.querystring_caching_behaviour">
<code class="sig-name descname">querystring_caching_behaviour</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.querystring_caching_behaviour" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets query string caching behavior. Allowed values are <code class="docutils literal notranslate"><span class="pre">IgnoreQueryString</span></code>, <code class="docutils literal notranslate"><span class="pre">BypassCaching</span></code> and <code class="docutils literal notranslate"><span class="pre">UseQueryString</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IgnoreQueryString</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the CDN Endpoint.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Endpoint.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cdn.Endpoint.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_types_to_compresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delivery_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">geo_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">global_delivery_rule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_compression_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_http_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_https_allowed</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optimization_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_host_header</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">probe_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">profile_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">querystring_caching_behaviour</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Endpoint resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content_types_to_compresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of strings that indicates a content types on which compression will be applied. The value for the elements should be MIME types.</p></li>
<li><p><strong>delivery_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Rules for the rules engine. An endpoint can contain up until 4 of those rules that consist of conditions and actions. A <code class="docutils literal notranslate"><span class="pre">delivery_rule</span></code> blocks as defined below.</p></li>
<li><p><strong>geo_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of Geo Filters for this CDN Endpoint. Each <code class="docutils literal notranslate"><span class="pre">geo_filter</span></code> block supports fields documented below.</p></li>
<li><p><strong>global_delivery_rule</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Actions that are valid for all resources regardless of any conditions. A <code class="docutils literal notranslate"><span class="pre">global_delivery_rule</span></code> block as defined below.</p></li>
<li><p><strong>host_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string that determines the hostname/IP address of the origin server. This string can be a domain name, Storage Account endpoint, Web App endpoint, IPv4 address or IPv6 address. Changing this forces a new resource to be created.</p></li>
<li><p><strong>is_compression_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether compression is to be enabled. Defaults to false.</p></li>
<li><p><strong>is_http_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>is_https_allowed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the origin. This is an arbitrary value. However, this value needs to be unique under the endpoint. Changing this forces a new resource to be created.</p></li>
<li><p><strong>optimization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – What types of optimization should this CDN Endpoint optimize for? Possible values include <code class="docutils literal notranslate"><span class="pre">DynamicSiteAcceleration</span></code>, <code class="docutils literal notranslate"><span class="pre">GeneralMediaStreaming</span></code>, <code class="docutils literal notranslate"><span class="pre">GeneralWebDelivery</span></code>, <code class="docutils literal notranslate"><span class="pre">LargeFileDownload</span></code> and <code class="docutils literal notranslate"><span class="pre">VideoOnDemandMediaStreaming</span></code>.</p></li>
<li><p><strong>origin_host_header</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The host header CDN provider will send along with content requests to origins. Defaults to the host name of the origin.</p></li>
<li><p><strong>origin_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path used at for origin requests.</p></li>
<li><p><strong>origins</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The set of origins of the CDN endpoint. When multiple origins exist, the first origin will be used as primary and rest will be used as failover options. Each <code class="docutils literal notranslate"><span class="pre">origin</span></code> block supports fields documented below.</p></li>
<li><p><strong>probe_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – the path to a file hosted on the origin which helps accelerate delivery of the dynamic content and calculate the most optimal routes for the CDN. This is relative to the <code class="docutils literal notranslate"><span class="pre">origin_path</span></code>.</p></li>
<li><p><strong>profile_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CDN Profile to which to attach the CDN Endpoint.</p></li>
<li><p><strong>querystring_caching_behaviour</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets query string caching behavior. Allowed values are <code class="docutils literal notranslate"><span class="pre">IgnoreQueryString</span></code>, <code class="docutils literal notranslate"><span class="pre">BypassCaching</span></code> and <code class="docutils literal notranslate"><span class="pre">UseQueryString</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IgnoreQueryString</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the CDN Endpoint.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>delivery_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheExpirationAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cache_expiration_action</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">behavior</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behavior of the cache. Valid values are <code class="docutils literal notranslate"><span class="pre">BypassCache</span></code>, <code class="docutils literal notranslate"><span class="pre">Override</span></code> and <code class="docutils literal notranslate"><span class="pre">SetIfMissing</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Duration of the cache. Only allowed when <code class="docutils literal notranslate"><span class="pre">behavior</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Override</span></code> or <code class="docutils literal notranslate"><span class="pre">SetIfMissing</span></code>. Format: <code class="docutils literal notranslate"><span class="pre">[d.]hh:mm:ss</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheKeyQueryStringAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cache_key_query_string_action</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">behavior</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behavior of the cache key for query strings. Valid values are <code class="docutils literal notranslate"><span class="pre">Exclude</span></code>, <code class="docutils literal notranslate"><span class="pre">ExcludeAll</span></code>, <code class="docutils literal notranslate"><span class="pre">Include</span></code> and <code class="docutils literal notranslate"><span class="pre">IncludeAll</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comma separated list of parameter values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cookiesConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cookies_condition</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of values for the cookie.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the cookie.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">deviceCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">device_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Desktop</span></code> and <code class="docutils literal notranslate"><span class="pre">Mobile</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Equal</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpVersionConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">http_version_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">0.9</span></code>, <code class="docutils literal notranslate"><span class="pre">1.0</span></code>, <code class="docutils literal notranslate"><span class="pre">1.1</span></code> and <code class="docutils literal notranslate"><span class="pre">2.0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Equal</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">modifyRequestHeaderActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">modify_request_header_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Action to be executed on a header value. Valid values are <code class="docutils literal notranslate"><span class="pre">Append</span></code>, <code class="docutils literal notranslate"><span class="pre">Delete</span></code> and <code class="docutils literal notranslate"><span class="pre">Overwrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the header. Only needed when <code class="docutils literal notranslate"><span class="pre">action</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Append</span></code> or <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">modifyResponseHeaderActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">modify_response_header_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Action to be executed on a header value. Valid values are <code class="docutils literal notranslate"><span class="pre">Append</span></code>, <code class="docutils literal notranslate"><span class="pre">Delete</span></code> and <code class="docutils literal notranslate"><span class="pre">Overwrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the header. Only needed when <code class="docutils literal notranslate"><span class="pre">action</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Append</span></code> or <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this Delivery Rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">order</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The order used for this rule, which must be larger than 1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">postArgConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">post_arg_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the post arg.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryStringConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">query_string_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">remoteAddressConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">remote_address_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of string values. For <code class="docutils literal notranslate"><span class="pre">GeoMatch</span></code> <code class="docutils literal notranslate"><span class="pre">operator</span></code> this should be a list of country codes (e.g. <code class="docutils literal notranslate"><span class="pre">US</span></code> or <code class="docutils literal notranslate"><span class="pre">DE</span></code>). List of IP address if <code class="docutils literal notranslate"><span class="pre">operator</span></code> equals to <code class="docutils literal notranslate"><span class="pre">IPMatch</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">GeoMatch</span></code> and <code class="docutils literal notranslate"><span class="pre">IPMatch</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestBodyConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">request_body_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestHeaderConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">request_header_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of header values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">selector</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestMethodCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">request_method_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">HEAD</span></code>, <code class="docutils literal notranslate"><span class="pre">OPTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code> and <code class="docutils literal notranslate"><span class="pre">PUT</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Equal</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestSchemeCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">request_scheme_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> and <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Equal</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">requestUriConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">request_uri_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlFileExtensionConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_file_extension_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlFileNameConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_file_name_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlPathConditions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_path_condition</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of string values.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">negateCondition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Any</span></code>, <code class="docutils literal notranslate"><span class="pre">BeginsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Contains</span></code>, <code class="docutils literal notranslate"><span class="pre">EndsWith</span></code>, <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code> and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">transforms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Valid values are <code class="docutils literal notranslate"><span class="pre">Lowercase</span></code> and <code class="docutils literal notranslate"><span class="pre">Uppercase</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlRedirectAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_redirect_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fragment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the fragment part of the URL. This value must not start with a <code class="docutils literal notranslate"><span class="pre">#</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the hostname part of the URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the path part of the URL. This value must begin with a <code class="docutils literal notranslate"><span class="pre">/</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the protocol part of the URL. Valid values are <code class="docutils literal notranslate"><span class="pre">Http</span></code> and <code class="docutils literal notranslate"><span class="pre">Https</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the query string part of the URL. This value must not start with a <code class="docutils literal notranslate"><span class="pre">?</span></code> or <code class="docutils literal notranslate"><span class="pre">&amp;</span></code> and must be in <code class="docutils literal notranslate"><span class="pre">&lt;key&gt;=&lt;value&gt;</span></code> format separated by <code class="docutils literal notranslate"><span class="pre">&amp;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of the redirect. Valid values are <code class="docutils literal notranslate"><span class="pre">Found</span></code>, <code class="docutils literal notranslate"><span class="pre">Moved</span></code>, <code class="docutils literal notranslate"><span class="pre">PermanentRedirect</span></code> and <code class="docutils literal notranslate"><span class="pre">TemporaryRedirect</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlRewriteAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_rewrite_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This value must start with a <code class="docutils literal notranslate"><span class="pre">/</span></code> and can’t be longer than 260 characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preserveUnmatchedPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourcePattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This value must start with a <code class="docutils literal notranslate"><span class="pre">/</span></code> and can’t be longer than 260 characters.</p></li>
</ul>
</li>
</ul>
<p>The <strong>geo_filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Action of the Geo Filter. Possible values include <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Block</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">countryCodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A List of two letter country codes (e.g. <code class="docutils literal notranslate"><span class="pre">US</span></code>, <code class="docutils literal notranslate"><span class="pre">GB</span></code>) to be associated with this Geo Filter.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">relative_path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The relative path applicable to geo filter.</p></li>
</ul>
<p>The <strong>global_delivery_rule</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheExpirationAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cache_expiration_action</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">behavior</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behavior of the cache. Valid values are <code class="docutils literal notranslate"><span class="pre">BypassCache</span></code>, <code class="docutils literal notranslate"><span class="pre">Override</span></code> and <code class="docutils literal notranslate"><span class="pre">SetIfMissing</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Duration of the cache. Only allowed when <code class="docutils literal notranslate"><span class="pre">behavior</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Override</span></code> or <code class="docutils literal notranslate"><span class="pre">SetIfMissing</span></code>. Format: <code class="docutils literal notranslate"><span class="pre">[d.]hh:mm:ss</span></code></p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheKeyQueryStringAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">cache_key_query_string_action</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">behavior</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behavior of the cache key for query strings. Valid values are <code class="docutils literal notranslate"><span class="pre">Exclude</span></code>, <code class="docutils literal notranslate"><span class="pre">ExcludeAll</span></code>, <code class="docutils literal notranslate"><span class="pre">Include</span></code> and <code class="docutils literal notranslate"><span class="pre">IncludeAll</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Comma separated list of parameter values.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">modifyRequestHeaderActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">modify_request_header_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Action to be executed on a header value. Valid values are <code class="docutils literal notranslate"><span class="pre">Append</span></code>, <code class="docutils literal notranslate"><span class="pre">Delete</span></code> and <code class="docutils literal notranslate"><span class="pre">Overwrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the header. Only needed when <code class="docutils literal notranslate"><span class="pre">action</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Append</span></code> or <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">modifyResponseHeaderActions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">modify_response_header_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Action to be executed on a header value. Valid values are <code class="docutils literal notranslate"><span class="pre">Append</span></code>, <code class="docutils literal notranslate"><span class="pre">Delete</span></code> and <code class="docutils literal notranslate"><span class="pre">Overwrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The header name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the header. Only needed when <code class="docutils literal notranslate"><span class="pre">action</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Append</span></code> or <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlRedirectAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_redirect_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">fragment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the fragment part of the URL. This value must not start with a <code class="docutils literal notranslate"><span class="pre">#</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the hostname part of the URL.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the path part of the URL. This value must begin with a <code class="docutils literal notranslate"><span class="pre">/</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the protocol part of the URL. Valid values are <code class="docutils literal notranslate"><span class="pre">Http</span></code> and <code class="docutils literal notranslate"><span class="pre">Https</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryString</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the query string part of the URL. This value must not start with a <code class="docutils literal notranslate"><span class="pre">?</span></code> or <code class="docutils literal notranslate"><span class="pre">&amp;</span></code> and must be in <code class="docutils literal notranslate"><span class="pre">&lt;key&gt;=&lt;value&gt;</span></code> format separated by <code class="docutils literal notranslate"><span class="pre">&amp;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">redirectType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of the redirect. Valid values are <code class="docutils literal notranslate"><span class="pre">Found</span></code>, <code class="docutils literal notranslate"><span class="pre">Moved</span></code>, <code class="docutils literal notranslate"><span class="pre">PermanentRedirect</span></code> and <code class="docutils literal notranslate"><span class="pre">TemporaryRedirect</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">urlRewriteAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">url_rewrite_action</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">destination</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This value must start with a <code class="docutils literal notranslate"><span class="pre">/</span></code> and can’t be longer than 260 characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">preserveUnmatchedPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourcePattern</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This value must start with a <code class="docutils literal notranslate"><span class="pre">/</span></code> and can’t be longer than 260 characters.</p></li>
</ul>
</li>
</ul>
<p>The <strong>origins</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A string that determines the hostname/IP address of the origin server. This string can be a domain name, Storage Account endpoint, Web App endpoint, IPv4 address or IPv6 address. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTP port of the origin. Defaults to <code class="docutils literal notranslate"><span class="pre">80</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpsPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The HTTPS port of the origin. Defaults to <code class="docutils literal notranslate"><span class="pre">443</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the origin. This is an arbitrary value. However, this value needs to be unique under the endpoint. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cdn.Endpoint.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cdn.Endpoint.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.Endpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cdn.GetProfileResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.cdn.</code><code class="sig-name descname">GetProfileResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.GetProfileResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProfile.</p>
<dl class="py attribute">
<dt id="pulumi_azure.cdn.GetProfileResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.GetProfileResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.GetProfileResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.GetProfileResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region where the resource exists.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.GetProfileResult.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.GetProfileResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The pricing related information of current CDN profile.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.GetProfileResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.GetProfileResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.cdn.Profile">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.cdn.</code><code class="sig-name descname">Profile</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.Profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a CDN Profile to create a collection of CDN Endpoints.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West US&quot;</span><span class="p">)</span>
<span class="n">example_profile</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cdn</span><span class="o">.</span><span class="n">Profile</span><span class="p">(</span><span class="s2">&quot;exampleProfile&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West US&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">sku</span><span class="o">=</span><span class="s2">&quot;Standard_Verizon&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;environment&quot;</span><span class="p">:</span> <span class="s2">&quot;Production&quot;</span><span class="p">,</span>
        <span class="s2">&quot;cost_center&quot;</span><span class="p">:</span> <span class="s2">&quot;MSFT&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the CDN Profile. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the CDN Profile.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pricing related information of current CDN profile. Accepted values are <code class="docutils literal notranslate"><span class="pre">Standard_Akamai</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_ChinaCdn</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_Microsoft</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_Verizon</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium_Verizon</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.cdn.Profile.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Profile.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Profile.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Profile.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the CDN Profile. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Profile.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Profile.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the CDN Profile.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Profile.sku">
<code class="sig-name descname">sku</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Profile.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The pricing related information of current CDN profile. Accepted values are <code class="docutils literal notranslate"><span class="pre">Standard_Akamai</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_ChinaCdn</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_Microsoft</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_Verizon</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium_Verizon</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.cdn.Profile.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.cdn.Profile.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cdn.Profile.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.Profile.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Profile resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the CDN Profile. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the CDN Profile.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pricing related information of current CDN profile. Accepted values are <code class="docutils literal notranslate"><span class="pre">Standard_Akamai</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_ChinaCdn</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_Microsoft</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_Verizon</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium_Verizon</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.cdn.Profile.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.Profile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.cdn.Profile.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.Profile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_azure.cdn.get_profile">
<code class="sig-prename descclassname">pulumi_azure.cdn.</code><code class="sig-name descname">get_profile</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.cdn.get_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing CDN Profile.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">cdn</span><span class="o">.</span><span class="n">get_profile</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;myfirstcdnprofile&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;example-resources&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;cdnProfileId&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the CDN Profile.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group in which the CDN Profile exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
