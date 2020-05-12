---
title: Module cdn
title_tag: Module cdn | Package pulumi_alicloud | Python SDK
linktitle: cdn
notitle: true
---

<div class="section" id="cdn">
<h1>cdn<a class="headerlink" href="#cdn" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.cdn"></span><dl class="py class">
<dt id="pulumi_alicloud.cdn.Domain">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cdn.</code><code class="sig-name descname">Domain</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">block_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cache_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cdn_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_header_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optimize_enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">page404_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">page_compress_enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameter_filter_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">range_enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refer_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">video_seek_enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cdn.Domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Domain resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] auth_config: The auth config of the accelerated domain.
:param pulumi.Input[list] cache_configs: The cache configs of the accelerated domain.
:param pulumi.Input[str] cdn_type: Cdn type of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">web</span></code>, <code class="docutils literal notranslate"><span class="pre">download</span></code>, <code class="docutils literal notranslate"><span class="pre">video</span></code>, <code class="docutils literal notranslate"><span class="pre">liveStream</span></code>.
:param pulumi.Input[str] domain_name: Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or “-“, and must not begin or end with “-“, and “-” must not in the 3th and 4th character positions at the same time. Suffix <code class="docutils literal notranslate"><span class="pre">.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">.tel</span></code> are not supported.
:param pulumi.Input[list] http_header_configs: The http header configs of the accelerated domain.
:param pulumi.Input[str] optimize_enable: Page Optimize config of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">off</span></code>. It can effectively remove the page redundant content, reduce the file size and improve the speed of distribution when this parameter value is <code class="docutils literal notranslate"><span class="pre">on</span></code>.
:param pulumi.Input[dict] page404_config: The error page config of the accelerated domain.
:param pulumi.Input[str] page_compress_enable: Page Compress config of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">off</span></code>.
:param pulumi.Input[dict] parameter_filter_config: The parameter filter config of the accelerated domain.
:param pulumi.Input[str] range_enable: Range Source config of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">off</span></code>.
:param pulumi.Input[dict] refer_config: The refer config of the accelerated domain.
:param pulumi.Input[str] scope: Scope of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">domestic</span></code>, <code class="docutils literal notranslate"><span class="pre">overseas</span></code>, <code class="docutils literal notranslate"><span class="pre">global</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">domestic</span></code>. This parameter’s setting is valid Only for the international users and domestic L3 and above users .
:param pulumi.Input[float] source_port: Source port of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">80</span></code> and <code class="docutils literal notranslate"><span class="pre">443</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">80</span></code>. You must use <code class="docutils literal notranslate"><span class="pre">80</span></code> when the <code class="docutils literal notranslate"><span class="pre">source_type</span></code> is <code class="docutils literal notranslate"><span class="pre">oss</span></code>.
:param pulumi.Input[str] source_type: Source type of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">ipaddr</span></code>, <code class="docutils literal notranslate"><span class="pre">domain</span></code>, <code class="docutils literal notranslate"><span class="pre">oss</span></code>. You must set this parameter when <code class="docutils literal notranslate"><span class="pre">cdn_type</span></code> value is not <code class="docutils literal notranslate"><span class="pre">liveStream</span></code>.
:param pulumi.Input[list] sources: Sources of the accelerated domain. It’s a list of domain names or IP address and consists of at most 20 items. You must set this parameter when <code class="docutils literal notranslate"><span class="pre">cdn_type</span></code> value is not <code class="docutils literal notranslate"><span class="pre">liveStream</span></code>.
:param pulumi.Input[str] video_seek_enable: Video Seek config of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
<p>The <strong>auth_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auth_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Auth type of the auth config. Valid values are  <code class="docutils literal notranslate"><span class="pre">no_auth</span></code>, <code class="docutils literal notranslate"><span class="pre">type_a</span></code>, <code class="docutils literal notranslate"><span class="pre">type_b</span></code> and <code class="docutils literal notranslate"><span class="pre">type_c</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">no_auth</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Master authentication key of the auth config. This parameter can have a string of 6 to 32 characters and must contain only alphanumeric characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">slaveKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Slave authentication key of the auth config. This parameter can have a string of 6 to 32 characters and must contain only alphanumeric characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Authentication cache time of the auth config. Default value is <code class="docutils literal notranslate"><span class="pre">1800</span></code>. It’s value is valid only when the <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> is <code class="docutils literal notranslate"><span class="pre">type_b</span></code> or <code class="docutils literal notranslate"><span class="pre">type_c</span></code>.</p></li>
</ul>
<p>The <strong>cache_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheContent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Cache content of the cache config. It’s value is a path string when the <code class="docutils literal notranslate"><span class="pre">cache_type</span></code> is <code class="docutils literal notranslate"><span class="pre">path</span></code>. When the <code class="docutils literal notranslate"><span class="pre">cache_type</span></code> is <code class="docutils literal notranslate"><span class="pre">suffix</span></code>, it’s value is a string which contains multiple file suffixes separated by commas.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Cache type of the cache config. Valid values are <code class="docutils literal notranslate"><span class="pre">suffix</span></code> and <code class="docutils literal notranslate"><span class="pre">path</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Cache time of the cache config.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Weight of the cache config. This parameter’s value is between 1 and 99. Default value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. The higher the value, the higher the priority.</p></li>
</ul>
<p>The <strong>certificate_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">private_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SSL private key. This is required if <code class="docutils literal notranslate"><span class="pre">server_certificate_status</span></code> is <code class="docutils literal notranslate"><span class="pre">on</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server_certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SSL server certificate string. This is required if <code class="docutils literal notranslate"><span class="pre">server_certificate_status</span></code> is <code class="docutils literal notranslate"><span class="pre">on</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverCertificateStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This parameter indicates whether or not enable https. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">on</span></code>.</p></li>
</ul>
<p>The <strong>http_header_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headerId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Header key of the http header. Valid values are <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code>, <code class="docutils literal notranslate"><span class="pre">Cache-Control</span></code>, <code class="docutils literal notranslate"><span class="pre">Content-Disposition</span></code>, <code class="docutils literal notranslate"><span class="pre">Content-Language</span></code>，<code class="docutils literal notranslate"><span class="pre">Expires</span></code>, <code class="docutils literal notranslate"><span class="pre">Access-Control-Allow-Origin</span></code>, <code class="docutils literal notranslate"><span class="pre">Access-Control-Allow-Methods</span></code> and <code class="docutils literal notranslate"><span class="pre">Access-Control-Max-Age</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Header value of the http header.</p></li>
</ul>
<p>The <strong>page404_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customPageUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Custom page url of the error page. It must be the full path under the accelerated domain name. It’s value must be <code class="docutils literal notranslate"><span class="pre">http://promotion.alicdn.com/help/oss/error.html</span></code> when <code class="docutils literal notranslate"><span class="pre">page_type</span></code> value is <code class="docutils literal notranslate"><span class="pre">charity</span></code> and It can not be set when <code class="docutils literal notranslate"><span class="pre">page_type</span></code> value is <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Page type of the error page. Valid values are <code class="docutils literal notranslate"><span class="pre">default</span></code>, <code class="docutils literal notranslate"><span class="pre">charity</span></code>, <code class="docutils literal notranslate"><span class="pre">other</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p></li>
</ul>
<p>The <strong>parameter_filter_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This parameter indicates whether or not the <code class="docutils literal notranslate"><span class="pre">parameter_filter_config</span></code> is enable. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hashKeyArgs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Reserved parameters of <code class="docutils literal notranslate"><span class="pre">parameter_filter_config</span></code>. It’s a list of string and consists of at most 10 items.</p></li>
</ul>
<p>The <strong>refer_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowEmpty</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This parameter indicates whether or not to allow empty refer access. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">on</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">referLists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of domain names of the refer config.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">referType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Refer type of the refer config. Valid values are <code class="docutils literal notranslate"><span class="pre">block</span></code> and <code class="docutils literal notranslate"><span class="pre">allow</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">block</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.Domain.auth_config">
<code class="sig-name descname">auth_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.auth_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The auth config of the accelerated domain.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auth_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Auth type of the auth config. Valid values are  <code class="docutils literal notranslate"><span class="pre">no_auth</span></code>, <code class="docutils literal notranslate"><span class="pre">type_a</span></code>, <code class="docutils literal notranslate"><span class="pre">type_b</span></code> and <code class="docutils literal notranslate"><span class="pre">type_c</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">no_auth</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Master authentication key of the auth config. This parameter can have a string of 6 to 32 characters and must contain only alphanumeric characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">slaveKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Slave authentication key of the auth config. This parameter can have a string of 6 to 32 characters and must contain only alphanumeric characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Authentication cache time of the auth config. Default value is <code class="docutils literal notranslate"><span class="pre">1800</span></code>. It’s value is valid only when the <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> is <code class="docutils literal notranslate"><span class="pre">type_b</span></code> or <code class="docutils literal notranslate"><span class="pre">type_c</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.Domain.cache_configs">
<code class="sig-name descname">cache_configs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.cache_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>The cache configs of the accelerated domain.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheContent</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Cache content of the cache config. It’s value is a path string when the <code class="docutils literal notranslate"><span class="pre">cache_type</span></code> is <code class="docutils literal notranslate"><span class="pre">path</span></code>. When the <code class="docutils literal notranslate"><span class="pre">cache_type</span></code> is <code class="docutils literal notranslate"><span class="pre">suffix</span></code>, it’s value is a string which contains multiple file suffixes separated by commas.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Cache type of the cache config. Valid values are <code class="docutils literal notranslate"><span class="pre">suffix</span></code> and <code class="docutils literal notranslate"><span class="pre">path</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Cache time of the cache config.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Weight of the cache config. This parameter’s value is between 1 and 99. Default value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. The higher the value, the higher the priority.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.Domain.cdn_type">
<code class="sig-name descname">cdn_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.cdn_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Cdn type of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">web</span></code>, <code class="docutils literal notranslate"><span class="pre">download</span></code>, <code class="docutils literal notranslate"><span class="pre">video</span></code>, <code class="docutils literal notranslate"><span class="pre">liveStream</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.Domain.domain_name">
<code class="sig-name descname">domain_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or “-“, and must not begin or end with “-“, and “-” must not in the 3th and 4th character positions at the same time. Suffix <code class="docutils literal notranslate"><span class="pre">.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">.tel</span></code> are not supported.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.Domain.http_header_configs">
<code class="sig-name descname">http_header_configs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.http_header_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>The http header configs of the accelerated domain.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headerId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Header key of the http header. Valid values are <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code>, <code class="docutils literal notranslate"><span class="pre">Cache-Control</span></code>, <code class="docutils literal notranslate"><span class="pre">Content-Disposition</span></code>, <code class="docutils literal notranslate"><span class="pre">Content-Language</span></code>，<code class="docutils literal notranslate"><span class="pre">Expires</span></code>, <code class="docutils literal notranslate"><span class="pre">Access-Control-Allow-Origin</span></code>, <code class="docutils literal notranslate"><span class="pre">Access-Control-Allow-Methods</span></code> and <code class="docutils literal notranslate"><span class="pre">Access-Control-Max-Age</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Header value of the http header.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.Domain.optimize_enable">
<code class="sig-name descname">optimize_enable</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.optimize_enable" title="Permalink to this definition">¶</a></dt>
<dd><p>Page Optimize config of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">off</span></code>. It can effectively remove the page redundant content, reduce the file size and improve the speed of distribution when this parameter value is <code class="docutils literal notranslate"><span class="pre">on</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.Domain.page404_config">
<code class="sig-name descname">page404_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.page404_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The error page config of the accelerated domain.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customPageUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Custom page url of the error page. It must be the full path under the accelerated domain name. It’s value must be <code class="docutils literal notranslate"><span class="pre">http://promotion.alicdn.com/help/oss/error.html</span></code> when <code class="docutils literal notranslate"><span class="pre">page_type</span></code> value is <code class="docutils literal notranslate"><span class="pre">charity</span></code> and It can not be set when <code class="docutils literal notranslate"><span class="pre">page_type</span></code> value is <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorCode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pageType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Page type of the error page. Valid values are <code class="docutils literal notranslate"><span class="pre">default</span></code>, <code class="docutils literal notranslate"><span class="pre">charity</span></code>, <code class="docutils literal notranslate"><span class="pre">other</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.Domain.page_compress_enable">
<code class="sig-name descname">page_compress_enable</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.page_compress_enable" title="Permalink to this definition">¶</a></dt>
<dd><p>Page Compress config of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.Domain.parameter_filter_config">
<code class="sig-name descname">parameter_filter_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.parameter_filter_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The parameter filter config of the accelerated domain.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - This parameter indicates whether or not the <code class="docutils literal notranslate"><span class="pre">parameter_filter_config</span></code> is enable. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hashKeyArgs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Reserved parameters of <code class="docutils literal notranslate"><span class="pre">parameter_filter_config</span></code>. It’s a list of string and consists of at most 10 items.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.Domain.range_enable">
<code class="sig-name descname">range_enable</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.range_enable" title="Permalink to this definition">¶</a></dt>
<dd><p>Range Source config of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.Domain.refer_config">
<code class="sig-name descname">refer_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.refer_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The refer config of the accelerated domain.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowEmpty</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - This parameter indicates whether or not to allow empty refer access. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">on</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">referLists</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of domain names of the refer config.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">referType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Refer type of the refer config. Valid values are <code class="docutils literal notranslate"><span class="pre">block</span></code> and <code class="docutils literal notranslate"><span class="pre">allow</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">block</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.Domain.scope">
<code class="sig-name descname">scope</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Scope of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">domestic</span></code>, <code class="docutils literal notranslate"><span class="pre">overseas</span></code>, <code class="docutils literal notranslate"><span class="pre">global</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">domestic</span></code>. This parameter’s setting is valid Only for the international users and domestic L3 and above users .</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.Domain.source_port">
<code class="sig-name descname">source_port</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.source_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Source port of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">80</span></code> and <code class="docutils literal notranslate"><span class="pre">443</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">80</span></code>. You must use <code class="docutils literal notranslate"><span class="pre">80</span></code> when the <code class="docutils literal notranslate"><span class="pre">source_type</span></code> is <code class="docutils literal notranslate"><span class="pre">oss</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.Domain.source_type">
<code class="sig-name descname">source_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.source_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Source type of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">ipaddr</span></code>, <code class="docutils literal notranslate"><span class="pre">domain</span></code>, <code class="docutils literal notranslate"><span class="pre">oss</span></code>. You must set this parameter when <code class="docutils literal notranslate"><span class="pre">cdn_type</span></code> value is not <code class="docutils literal notranslate"><span class="pre">liveStream</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.Domain.sources">
<code class="sig-name descname">sources</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.sources" title="Permalink to this definition">¶</a></dt>
<dd><p>Sources of the accelerated domain. It’s a list of domain names or IP address and consists of at most 20 items. You must set this parameter when <code class="docutils literal notranslate"><span class="pre">cdn_type</span></code> value is not <code class="docutils literal notranslate"><span class="pre">liveStream</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.Domain.video_seek_enable">
<code class="sig-name descname">video_seek_enable</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.video_seek_enable" title="Permalink to this definition">¶</a></dt>
<dd><p>Video Seek config of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cdn.Domain.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">block_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cache_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cdn_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_header_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">optimize_enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">page404_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">page_compress_enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameter_filter_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">range_enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refer_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_port</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">video_seek_enable</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Domain resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The auth config of the accelerated domain.</p></li>
<li><p><strong>cache_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The cache configs of the accelerated domain.</p></li>
<li><p><strong>cdn_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cdn type of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">web</span></code>, <code class="docutils literal notranslate"><span class="pre">download</span></code>, <code class="docutils literal notranslate"><span class="pre">video</span></code>, <code class="docutils literal notranslate"><span class="pre">liveStream</span></code>.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or “-“, and must not begin or end with “-“, and “-” must not in the 3th and 4th character positions at the same time. Suffix <code class="docutils literal notranslate"><span class="pre">.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">.tel</span></code> are not supported.</p></li>
<li><p><strong>http_header_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The http header configs of the accelerated domain.</p></li>
<li><p><strong>optimize_enable</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Page Optimize config of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">off</span></code>. It can effectively remove the page redundant content, reduce the file size and improve the speed of distribution when this parameter value is <code class="docutils literal notranslate"><span class="pre">on</span></code>.</p></li>
<li><p><strong>page404_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The error page config of the accelerated domain.</p></li>
<li><p><strong>page_compress_enable</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Page Compress config of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>parameter_filter_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The parameter filter config of the accelerated domain.</p></li>
<li><p><strong>range_enable</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Range Source config of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><strong>refer_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The refer config of the accelerated domain.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Scope of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">domestic</span></code>, <code class="docutils literal notranslate"><span class="pre">overseas</span></code>, <code class="docutils literal notranslate"><span class="pre">global</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">domestic</span></code>. This parameter’s setting is valid Only for the international users and domestic L3 and above users .</p></li>
<li><p><strong>source_port</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Source port of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">80</span></code> and <code class="docutils literal notranslate"><span class="pre">443</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">80</span></code>. You must use <code class="docutils literal notranslate"><span class="pre">80</span></code> when the <code class="docutils literal notranslate"><span class="pre">source_type</span></code> is <code class="docutils literal notranslate"><span class="pre">oss</span></code>.</p></li>
<li><p><strong>source_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Source type of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">ipaddr</span></code>, <code class="docutils literal notranslate"><span class="pre">domain</span></code>, <code class="docutils literal notranslate"><span class="pre">oss</span></code>. You must set this parameter when <code class="docutils literal notranslate"><span class="pre">cdn_type</span></code> value is not <code class="docutils literal notranslate"><span class="pre">liveStream</span></code>.</p></li>
<li><p><strong>sources</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Sources of the accelerated domain. It’s a list of domain names or IP address and consists of at most 20 items. You must set this parameter when <code class="docutils literal notranslate"><span class="pre">cdn_type</span></code> value is not <code class="docutils literal notranslate"><span class="pre">liveStream</span></code>.</p></li>
<li><p><strong>video_seek_enable</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Video Seek config of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auth_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auth_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Auth type of the auth config. Valid values are  <code class="docutils literal notranslate"><span class="pre">no_auth</span></code>, <code class="docutils literal notranslate"><span class="pre">type_a</span></code>, <code class="docutils literal notranslate"><span class="pre">type_b</span></code> and <code class="docutils literal notranslate"><span class="pre">type_c</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">no_auth</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">masterKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Master authentication key of the auth config. This parameter can have a string of 6 to 32 characters and must contain only alphanumeric characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">slaveKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Slave authentication key of the auth config. This parameter can have a string of 6 to 32 characters and must contain only alphanumeric characters.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Authentication cache time of the auth config. Default value is <code class="docutils literal notranslate"><span class="pre">1800</span></code>. It’s value is valid only when the <code class="docutils literal notranslate"><span class="pre">auth_type</span></code> is <code class="docutils literal notranslate"><span class="pre">type_b</span></code> or <code class="docutils literal notranslate"><span class="pre">type_c</span></code>.</p></li>
</ul>
<p>The <strong>cache_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">cacheContent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Cache content of the cache config. It’s value is a path string when the <code class="docutils literal notranslate"><span class="pre">cache_type</span></code> is <code class="docutils literal notranslate"><span class="pre">path</span></code>. When the <code class="docutils literal notranslate"><span class="pre">cache_type</span></code> is <code class="docutils literal notranslate"><span class="pre">suffix</span></code>, it’s value is a string which contains multiple file suffixes separated by commas.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cacheType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Cache type of the cache config. Valid values are <code class="docutils literal notranslate"><span class="pre">suffix</span></code> and <code class="docutils literal notranslate"><span class="pre">path</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ttl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Cache time of the cache config.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Weight of the cache config. This parameter’s value is between 1 and 99. Default value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. The higher the value, the higher the priority.</p></li>
</ul>
<p>The <strong>certificate_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">private_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SSL private key. This is required if <code class="docutils literal notranslate"><span class="pre">server_certificate_status</span></code> is <code class="docutils literal notranslate"><span class="pre">on</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server_certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SSL server certificate string. This is required if <code class="docutils literal notranslate"><span class="pre">server_certificate_status</span></code> is <code class="docutils literal notranslate"><span class="pre">on</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverCertificateStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This parameter indicates whether or not enable https. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">on</span></code>.</p></li>
</ul>
<p>The <strong>http_header_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">headerId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Header key of the http header. Valid values are <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code>, <code class="docutils literal notranslate"><span class="pre">Cache-Control</span></code>, <code class="docutils literal notranslate"><span class="pre">Content-Disposition</span></code>, <code class="docutils literal notranslate"><span class="pre">Content-Language</span></code>，<code class="docutils literal notranslate"><span class="pre">Expires</span></code>, <code class="docutils literal notranslate"><span class="pre">Access-Control-Allow-Origin</span></code>, <code class="docutils literal notranslate"><span class="pre">Access-Control-Allow-Methods</span></code> and <code class="docutils literal notranslate"><span class="pre">Access-Control-Max-Age</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headerValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Header value of the http header.</p></li>
</ul>
<p>The <strong>page404_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">customPageUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Custom page url of the error page. It must be the full path under the accelerated domain name. It’s value must be <code class="docutils literal notranslate"><span class="pre">http://promotion.alicdn.com/help/oss/error.html</span></code> when <code class="docutils literal notranslate"><span class="pre">page_type</span></code> value is <code class="docutils literal notranslate"><span class="pre">charity</span></code> and It can not be set when <code class="docutils literal notranslate"><span class="pre">page_type</span></code> value is <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">errorCode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pageType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Page type of the error page. Valid values are <code class="docutils literal notranslate"><span class="pre">default</span></code>, <code class="docutils literal notranslate"><span class="pre">charity</span></code>, <code class="docutils literal notranslate"><span class="pre">other</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">default</span></code>.</p></li>
</ul>
<p>The <strong>parameter_filter_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enable</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This parameter indicates whether or not the <code class="docutils literal notranslate"><span class="pre">parameter_filter_config</span></code> is enable. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">off</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hashKeyArgs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Reserved parameters of <code class="docutils literal notranslate"><span class="pre">parameter_filter_config</span></code>. It’s a list of string and consists of at most 10 items.</p></li>
</ul>
<p>The <strong>refer_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowEmpty</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This parameter indicates whether or not to allow empty refer access. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">on</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">referLists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of domain names of the refer config.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">referType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Refer type of the refer config. Valid values are <code class="docutils literal notranslate"><span class="pre">block</span></code> and <code class="docutils literal notranslate"><span class="pre">allow</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">block</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cdn.Domain.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cdn.Domain.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cdn.Domain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cdn.DomainConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cdn.</code><code class="sig-name descname">DomainConfig</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">function_args</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">function_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cdn.DomainConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CDN Accelerated Domain resource.</p>
<p>For information about domain config and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/zh/doc-detail/90915.htm">Batch set config</a></p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.34.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="c1"># Create a new Domain config.</span>
<span class="n">domain</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cdn</span><span class="o">.</span><span class="n">DomainNew</span><span class="p">(</span><span class="s2">&quot;domain&quot;</span><span class="p">,</span>
    <span class="n">cdn_type</span><span class="o">=</span><span class="s2">&quot;web&quot;</span><span class="p">,</span>
    <span class="n">domain_name</span><span class="o">=</span><span class="s2">&quot;tf-testacc</span><span class="si">%d</span><span class="s2">.xiaozhu.com&quot;</span><span class="p">,</span>
    <span class="n">scope</span><span class="o">=</span><span class="s2">&quot;overseas&quot;</span><span class="p">,</span>
    <span class="n">sources</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;content&quot;</span><span class="p">:</span> <span class="s2">&quot;1.1.1.1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="mi">80</span><span class="p">,</span>
        <span class="s2">&quot;priority&quot;</span><span class="p">:</span> <span class="s2">&quot;20&quot;</span><span class="p">,</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;ipaddr&quot;</span><span class="p">,</span>
        <span class="s2">&quot;weight&quot;</span><span class="p">:</span> <span class="s2">&quot;15&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">config</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">cdn</span><span class="o">.</span><span class="n">DomainConfig</span><span class="p">(</span><span class="s2">&quot;config&quot;</span><span class="p">,</span>
    <span class="n">domain_name</span><span class="o">=</span><span class="n">domain</span><span class="o">.</span><span class="n">domain_name</span><span class="p">,</span>
    <span class="n">function_args</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;argName&quot;</span><span class="p">:</span> <span class="s2">&quot;ip_list&quot;</span><span class="p">,</span>
        <span class="s2">&quot;argValue&quot;</span><span class="p">:</span> <span class="s2">&quot;110.110.110.110&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">function_name</span><span class="o">=</span><span class="s2">&quot;ip_allow_list_set&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or “-“, and must not begin or end with “-“, and “-” must not in the 3th and 4th character positions at the same time. Suffix <code class="docutils literal notranslate"><span class="pre">.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">.tel</span></code> are not supported.</p></li>
<li><p><strong>function_args</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The args of the domain config.</p></li>
<li><p><strong>function_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the domain config.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>function_args</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">argName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of arg.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">argValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of arg.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.DomainConfig.domain_name">
<code class="sig-name descname">domain_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.DomainConfig.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or “-“, and must not begin or end with “-“, and “-” must not in the 3th and 4th character positions at the same time. Suffix <code class="docutils literal notranslate"><span class="pre">.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">.tel</span></code> are not supported.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.DomainConfig.function_args">
<code class="sig-name descname">function_args</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.DomainConfig.function_args" title="Permalink to this definition">¶</a></dt>
<dd><p>The args of the domain config.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">argName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of arg.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">argValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of arg.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.DomainConfig.function_name">
<code class="sig-name descname">function_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.DomainConfig.function_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the domain config.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cdn.DomainConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">function_args</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">function_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cdn.DomainConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DomainConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or “-“, and must not begin or end with “-“, and “-” must not in the 3th and 4th character positions at the same time. Suffix <code class="docutils literal notranslate"><span class="pre">.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">.tel</span></code> are not supported.</p></li>
<li><p><strong>function_args</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The args of the domain config.</p></li>
<li><p><strong>function_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the domain config.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>function_args</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">argName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of arg.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">argValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of arg.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cdn.DomainConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cdn.DomainConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cdn.DomainConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cdn.DomainConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cdn.DomainNew">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cdn.</code><code class="sig-name descname">DomainNew</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cdn_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cdn.DomainNew" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a DomainNew resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] cdn_type: Cdn type of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">web</span></code>, <code class="docutils literal notranslate"><span class="pre">download</span></code>, <code class="docutils literal notranslate"><span class="pre">video</span></code>.
:param pulumi.Input[dict] certificate_config: Certificate config of the accelerated domain. It’s a list and consist of at most 1 item.
:param pulumi.Input[str] domain_name: Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or “-“, and must not begin or end with “-“, and “-” must not in the 3th and 4th character positions at the same time. Suffix <code class="docutils literal notranslate"><span class="pre">.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">.tel</span></code> are not supported.
:param pulumi.Input[str] resource_group_id: Resource group ID.
:param pulumi.Input[str] scope: Scope of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">domestic</span></code>, <code class="docutils literal notranslate"><span class="pre">overseas</span></code>, <code class="docutils literal notranslate"><span class="pre">global</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">domestic</span></code>. This parameter’s setting is valid Only for the international users and domestic L3 and above users .
:param pulumi.Input[dict] sources: The source address list of the accelerated domain. Defaults to null. See Block Sources.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.</p>
<p>The <strong>certificate_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SSL certificate name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SSL certificate type, can be “upload”, “cas” and “free”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceSet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Set <code class="docutils literal notranslate"><span class="pre">1</span></code> to ignore the repeated verification for certificate name, and cover the information of the origin certificate (with the same name). Set <code class="docutils literal notranslate"><span class="pre">0</span></code> to work the verification.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SSL private key. This is required if <code class="docutils literal notranslate"><span class="pre">server_certificate_status</span></code> is <code class="docutils literal notranslate"><span class="pre">on</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server_certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SSL server certificate string. This is required if <code class="docutils literal notranslate"><span class="pre">server_certificate_status</span></code> is <code class="docutils literal notranslate"><span class="pre">on</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverCertificateStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This parameter indicates whether or not enable https. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">on</span></code>.</p></li>
</ul>
<p>The <strong>sources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The adress of source. Valid values can be ip or doaminName. Each item’s <code class="docutils literal notranslate"><span class="pre">content</span></code> can not be repeated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port of source. Valid values are <code class="docutils literal notranslate"><span class="pre">443</span></code> and <code class="docutils literal notranslate"><span class="pre">80</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">80</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority of the source. Valid values are <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the source. Valid values are <code class="docutils literal notranslate"><span class="pre">ipaddr</span></code>, <code class="docutils literal notranslate"><span class="pre">domain</span></code> and <code class="docutils literal notranslate"><span class="pre">oss</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Weight of the source. Valid values are from <code class="docutils literal notranslate"><span class="pre">0</span></code> to <code class="docutils literal notranslate"><span class="pre">100</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">10</span></code>, but if type is <code class="docutils literal notranslate"><span class="pre">ipaddr</span></code>, the value can only be <code class="docutils literal notranslate"><span class="pre">10</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.DomainNew.cdn_type">
<code class="sig-name descname">cdn_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.DomainNew.cdn_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Cdn type of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">web</span></code>, <code class="docutils literal notranslate"><span class="pre">download</span></code>, <code class="docutils literal notranslate"><span class="pre">video</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.DomainNew.certificate_config">
<code class="sig-name descname">certificate_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.DomainNew.certificate_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Certificate config of the accelerated domain. It’s a list and consist of at most 1 item.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SSL certificate name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SSL certificate type, can be “upload”, “cas” and “free”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceSet</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Set <code class="docutils literal notranslate"><span class="pre">1</span></code> to ignore the repeated verification for certificate name, and cover the information of the origin certificate (with the same name). Set <code class="docutils literal notranslate"><span class="pre">0</span></code> to work the verification.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SSL private key. This is required if <code class="docutils literal notranslate"><span class="pre">server_certificate_status</span></code> is <code class="docutils literal notranslate"><span class="pre">on</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server_certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The SSL server certificate string. This is required if <code class="docutils literal notranslate"><span class="pre">server_certificate_status</span></code> is <code class="docutils literal notranslate"><span class="pre">on</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverCertificateStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - This parameter indicates whether or not enable https. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">on</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.DomainNew.domain_name">
<code class="sig-name descname">domain_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.DomainNew.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or “-“, and must not begin or end with “-“, and “-” must not in the 3th and 4th character positions at the same time. Suffix <code class="docutils literal notranslate"><span class="pre">.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">.tel</span></code> are not supported.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.DomainNew.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.DomainNew.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource group ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.DomainNew.scope">
<code class="sig-name descname">scope</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.DomainNew.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Scope of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">domestic</span></code>, <code class="docutils literal notranslate"><span class="pre">overseas</span></code>, <code class="docutils literal notranslate"><span class="pre">global</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">domestic</span></code>. This parameter’s setting is valid Only for the international users and domestic L3 and above users .</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.DomainNew.sources">
<code class="sig-name descname">sources</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.DomainNew.sources" title="Permalink to this definition">¶</a></dt>
<dd><p>The source address list of the accelerated domain. Defaults to null. See Block Sources.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The adress of source. Valid values can be ip or doaminName. Each item’s <code class="docutils literal notranslate"><span class="pre">content</span></code> can not be repeated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port of source. Valid values are <code class="docutils literal notranslate"><span class="pre">443</span></code> and <code class="docutils literal notranslate"><span class="pre">80</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">80</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Priority of the source. Valid values are <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of the source. Valid values are <code class="docutils literal notranslate"><span class="pre">ipaddr</span></code>, <code class="docutils literal notranslate"><span class="pre">domain</span></code> and <code class="docutils literal notranslate"><span class="pre">oss</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Weight of the source. Valid values are from <code class="docutils literal notranslate"><span class="pre">0</span></code> to <code class="docutils literal notranslate"><span class="pre">100</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">10</span></code>, but if type is <code class="docutils literal notranslate"><span class="pre">ipaddr</span></code>, the value can only be <code class="docutils literal notranslate"><span class="pre">10</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cdn.DomainNew.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cdn.DomainNew.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cdn.DomainNew.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cdn_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificate_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sources</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cdn.DomainNew.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DomainNew resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cdn_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cdn type of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">web</span></code>, <code class="docutils literal notranslate"><span class="pre">download</span></code>, <code class="docutils literal notranslate"><span class="pre">video</span></code>.</p></li>
<li><p><strong>certificate_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Certificate config of the accelerated domain. It’s a list and consist of at most 1 item.</p></li>
<li><p><strong>domain_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the accelerated domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or “-“, and must not begin or end with “-“, and “-” must not in the 3th and 4th character positions at the same time. Suffix <code class="docutils literal notranslate"><span class="pre">.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">.tel</span></code> are not supported.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource group ID.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Scope of the accelerated domain. Valid values are <code class="docutils literal notranslate"><span class="pre">domestic</span></code>, <code class="docutils literal notranslate"><span class="pre">overseas</span></code>, <code class="docutils literal notranslate"><span class="pre">global</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">domestic</span></code>. This parameter’s setting is valid Only for the international users and domestic L3 and above users .</p></li>
<li><p><strong>sources</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The source address list of the accelerated domain. Defaults to null. See Block Sources.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>certificate_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SSL certificate name.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SSL certificate type, can be “upload”, “cas” and “free”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forceSet</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Set <code class="docutils literal notranslate"><span class="pre">1</span></code> to ignore the repeated verification for certificate name, and cover the information of the origin certificate (with the same name). Set <code class="docutils literal notranslate"><span class="pre">0</span></code> to work the verification.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">private_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SSL private key. This is required if <code class="docutils literal notranslate"><span class="pre">server_certificate_status</span></code> is <code class="docutils literal notranslate"><span class="pre">on</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server_certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The SSL server certificate string. This is required if <code class="docutils literal notranslate"><span class="pre">server_certificate_status</span></code> is <code class="docutils literal notranslate"><span class="pre">on</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverCertificateStatus</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This parameter indicates whether or not enable https. Valid values are <code class="docutils literal notranslate"><span class="pre">on</span></code> and <code class="docutils literal notranslate"><span class="pre">off</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">on</span></code>.</p></li>
</ul>
<p>The <strong>sources</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The adress of source. Valid values can be ip or doaminName. Each item’s <code class="docutils literal notranslate"><span class="pre">content</span></code> can not be repeated.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port of source. Valid values are <code class="docutils literal notranslate"><span class="pre">443</span></code> and <code class="docutils literal notranslate"><span class="pre">80</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">80</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Priority of the source. Valid values are <code class="docutils literal notranslate"><span class="pre">0</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the source. Valid values are <code class="docutils literal notranslate"><span class="pre">ipaddr</span></code>, <code class="docutils literal notranslate"><span class="pre">domain</span></code> and <code class="docutils literal notranslate"><span class="pre">oss</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Weight of the source. Valid values are from <code class="docutils literal notranslate"><span class="pre">0</span></code> to <code class="docutils literal notranslate"><span class="pre">100</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">10</span></code>, but if type is <code class="docutils literal notranslate"><span class="pre">ipaddr</span></code>, the value can only be <code class="docutils literal notranslate"><span class="pre">10</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cdn.DomainNew.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cdn.DomainNew.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cdn.DomainNew.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cdn.DomainNew.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
