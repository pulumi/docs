---
title: Module waf
title_tag: Module waf | Package pulumi_alicloud | Python SDK
linktitle: waf
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "alicloud" >}}

<div class="section" id="waf">
<h1>waf<a class="headerlink" href="#waf" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.waf"></span><dl class="py class">
<dt id="pulumi_alicloud.waf.AwaitableGetDomainsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.waf.</code><code class="sig-name descname">AwaitableGetDomainsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.waf.AwaitableGetDomainsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.waf.Domain">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.waf.</code><code class="sig-name descname">Domain</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http2_ports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_ports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_to_user_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">https_ports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">https_redirect</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_access_product</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_headers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">write_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.waf.Domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Domain resource to create domain in the Web Application Firewall.</p>
<p>For information about WAF and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/28517.htm">What is Alibaba Cloud WAF</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.82.0+ .</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">domain</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">waf</span><span class="o">.</span><span class="n">Domain</span><span class="p">(</span><span class="s2">&quot;domain&quot;</span><span class="p">,</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="s2">&quot;PhysicalCluster&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;www.aliyun.com&quot;</span><span class="p">,</span>
    <span class="n">http2_ports</span><span class="o">=</span><span class="mi">443</span><span class="p">,</span>
    <span class="n">http_ports</span><span class="o">=</span><span class="mi">80</span><span class="p">,</span>
    <span class="n">http_to_user_ip</span><span class="o">=</span><span class="s2">&quot;Off&quot;</span><span class="p">,</span>
    <span class="n">https_ports</span><span class="o">=</span><span class="mi">443</span><span class="p">,</span>
    <span class="n">https_redirect</span><span class="o">=</span><span class="s2">&quot;Off&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="s2">&quot;waf-123455&quot;</span><span class="p">,</span>
    <span class="n">is_access_product</span><span class="o">=</span><span class="s2">&quot;On&quot;</span><span class="p">,</span>
    <span class="n">load_balancing</span><span class="o">=</span><span class="s2">&quot;IpHash&quot;</span><span class="p">,</span>
    <span class="n">log_headers</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;foo&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;http&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">source_ips</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;1.1.1.1&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the WAF cluster. Valid values: “PhysicalCluster” and “VirtualCluster”. Default to “PhysicalCluster”.</p></li>
<li><p><strong>connection_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The connection timeout for WAF exclusive clusters. Unit: seconds.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain that you want to add to WAF.</p></li>
<li><p><strong>http2_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of the HTTP 2.0 ports.</p></li>
<li><p><strong>http_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of the HTTP ports</p></li>
<li><p><strong>http_to_user_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to enable the HTTP back-to-origin feature. After this feature is enabled, the WAF instance can use HTTP to forward HTTPS requests to the origin server. 
By default, port 80 is used to forward the requests to the origin server. Valid values: “On” and “Off”. Default to “Off”.</p></li>
<li><p><strong>https_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of the HTTPS ports</p></li>
<li><p><strong>https_redirect</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to redirect HTTP requests as HTTPS requests. Valid values: “On” and “Off”. Default to “Off”.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF instance.</p></li>
<li><p><strong>is_access_product</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to configure a Layer-7 proxy, such as Anti-DDoS Pro or CDN, to filter the inbound traffic before it is forwarded to WAF. Valid values: “On” and “Off”. Default to “Off”.</p></li>
<li><p><strong>load_balancing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The load balancing algorithm that is used to forward requests to the origin. Valid values: “IpHash” and “RoundRobin”. Default to “IpHash”.</p></li>
<li><p><strong>log_headers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The key-value pair that is used to mark the traffic that flows through WAF to the domain. Each item contains two field:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">key</span><span class="p">:</span> <span class="n">The</span> <span class="n">key</span> <span class="n">of</span> <span class="n">label</span>
<span class="o">*</span> <span class="n">value</span><span class="p">:</span> <span class="n">The</span> <span class="n">value</span> <span class="n">of</span> <span class="n">label</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>read_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The read timeout of a WAF exclusive cluster. Unit: seconds.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resource group to which the queried domain belongs in Resource Management. By default, no value is specified, indicating that the domain belongs to the default resource group.</p></li>
<li><p><strong>source_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of the IP address or domain of the origin server to which the specified domain points.</p></li>
<li><p><strong>write_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The timeout period for a WAF exclusive cluster write connection. Unit: seconds.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>log_headers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Domain.cluster_type">
<code class="sig-name descname">cluster_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Domain.cluster_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the WAF cluster. Valid values: “PhysicalCluster” and “VirtualCluster”. Default to “PhysicalCluster”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Domain.cname">
<code class="sig-name descname">cname</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Domain.cname" title="Permalink to this definition">¶</a></dt>
<dd><p>The CNAME record assigned by the WAF instance to the specified domain.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Domain.connection_time">
<code class="sig-name descname">connection_time</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Domain.connection_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The connection timeout for WAF exclusive clusters. Unit: seconds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Domain.domain">
<code class="sig-name descname">domain</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Domain.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain that you want to add to WAF.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Domain.http2_ports">
<code class="sig-name descname">http2_ports</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Domain.http2_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>List of the HTTP 2.0 ports.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Domain.http_ports">
<code class="sig-name descname">http_ports</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Domain.http_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>List of the HTTP ports</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Domain.http_to_user_ip">
<code class="sig-name descname">http_to_user_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Domain.http_to_user_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to enable the HTTP back-to-origin feature. After this feature is enabled, the WAF instance can use HTTP to forward HTTPS requests to the origin server. 
By default, port 80 is used to forward the requests to the origin server. Valid values: “On” and “Off”. Default to “Off”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Domain.https_ports">
<code class="sig-name descname">https_ports</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Domain.https_ports" title="Permalink to this definition">¶</a></dt>
<dd><p>List of the HTTPS ports</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Domain.https_redirect">
<code class="sig-name descname">https_redirect</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Domain.https_redirect" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to redirect HTTP requests as HTTPS requests. Valid values: “On” and “Off”. Default to “Off”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Domain.instance_id">
<code class="sig-name descname">instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Domain.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the WAF instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Domain.is_access_product">
<code class="sig-name descname">is_access_product</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Domain.is_access_product" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to configure a Layer-7 proxy, such as Anti-DDoS Pro or CDN, to filter the inbound traffic before it is forwarded to WAF. Valid values: “On” and “Off”. Default to “Off”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Domain.load_balancing">
<code class="sig-name descname">load_balancing</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Domain.load_balancing" title="Permalink to this definition">¶</a></dt>
<dd><p>The load balancing algorithm that is used to forward requests to the origin. Valid values: “IpHash” and “RoundRobin”. Default to “IpHash”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Domain.log_headers">
<code class="sig-name descname">log_headers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Domain.log_headers" title="Permalink to this definition">¶</a></dt>
<dd><p>The key-value pair that is used to mark the traffic that flows through WAF to the domain. Each item contains two field:</p>
<ul class="simple">
<li><p>key: The key of label</p></li>
<li><p>value: The value of label</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Domain.read_time">
<code class="sig-name descname">read_time</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Domain.read_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The read timeout of a WAF exclusive cluster. Unit: seconds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Domain.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Domain.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the resource group to which the queried domain belongs in Resource Management. By default, no value is specified, indicating that the domain belongs to the default resource group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Domain.source_ips">
<code class="sig-name descname">source_ips</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Domain.source_ips" title="Permalink to this definition">¶</a></dt>
<dd><p>List of the IP address or domain of the origin server to which the specified domain points.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Domain.write_time">
<code class="sig-name descname">write_time</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Domain.write_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The timeout period for a WAF exclusive cluster write connection. Unit: seconds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.waf.Domain.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cname</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http2_ports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_ports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_to_user_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">https_ports</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">https_redirect</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_access_product</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">load_balancing</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_headers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_ips</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">write_time</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.waf.Domain.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Domain resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the WAF cluster. Valid values: “PhysicalCluster” and “VirtualCluster”. Default to “PhysicalCluster”.</p></li>
<li><p><strong>cname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CNAME record assigned by the WAF instance to the specified domain.</p></li>
<li><p><strong>connection_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The connection timeout for WAF exclusive clusters. Unit: seconds.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain that you want to add to WAF.</p></li>
<li><p><strong>http2_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of the HTTP 2.0 ports.</p></li>
<li><p><strong>http_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of the HTTP ports</p></li>
<li><p><strong>http_to_user_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to enable the HTTP back-to-origin feature. After this feature is enabled, the WAF instance can use HTTP to forward HTTPS requests to the origin server. 
By default, port 80 is used to forward the requests to the origin server. Valid values: “On” and “Off”. Default to “Off”.</p></li>
<li><p><strong>https_ports</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of the HTTPS ports</p></li>
<li><p><strong>https_redirect</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to redirect HTTP requests as HTTPS requests. Valid values: “On” and “Off”. Default to “Off”.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the WAF instance.</p></li>
<li><p><strong>is_access_product</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether to configure a Layer-7 proxy, such as Anti-DDoS Pro or CDN, to filter the inbound traffic before it is forwarded to WAF. Valid values: “On” and “Off”. Default to “Off”.</p></li>
<li><p><strong>load_balancing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The load balancing algorithm that is used to forward requests to the origin. Valid values: “IpHash” and “RoundRobin”. Default to “IpHash”.</p></li>
<li><p><strong>log_headers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The key-value pair that is used to mark the traffic that flows through WAF to the domain. Each item contains two field:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">key</span><span class="p">:</span> <span class="n">The</span> <span class="n">key</span> <span class="n">of</span> <span class="n">label</span>
<span class="o">*</span> <span class="n">value</span><span class="p">:</span> <span class="n">The</span> <span class="n">value</span> <span class="n">of</span> <span class="n">label</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>read_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The read timeout of a WAF exclusive cluster. Unit: seconds.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resource group to which the queried domain belongs in Resource Management. By default, no value is specified, indicating that the domain belongs to the default resource group.</p></li>
<li><p><strong>source_ips</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of the IP address or domain of the origin server to which the specified domain points.</p></li>
<li><p><strong>write_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The timeout period for a WAF exclusive cluster write connection. Unit: seconds.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>log_headers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.waf.Domain.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.waf.Domain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.waf.Domain.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.waf.Domain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.waf.GetDomainsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.waf.</code><code class="sig-name descname">GetDomainsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">domains</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.waf.GetDomainsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDomains.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.waf.GetDomainsResult.domains">
<code class="sig-name descname">domains</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.GetDomainsResult.domains" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Domains. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.GetDomainsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.GetDomainsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.GetDomainsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.GetDomainsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) A list of WAF domain names. Each item is domain name.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.waf.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.waf.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">big_screen</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclusive_ip_package</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ext_bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ext_domain_package</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_storage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">modify_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prefessional_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renew_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renewal_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subscription_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">waf_log</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.waf.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF Instance resource to create instance in the Web Application Firewall.</p>
<p>For information about WAF and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/28517.htm">What is Alibaba Cloud WAF</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.83.0+ .</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">waf</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">big_screen</span><span class="o">=</span><span class="s2">&quot;0&quot;</span><span class="p">,</span>
    <span class="n">exclusive_ip_package</span><span class="o">=</span><span class="s2">&quot;1&quot;</span><span class="p">,</span>
    <span class="n">ext_bandwidth</span><span class="o">=</span><span class="s2">&quot;50&quot;</span><span class="p">,</span>
    <span class="n">ext_domain_package</span><span class="o">=</span><span class="s2">&quot;1&quot;</span><span class="p">,</span>
    <span class="n">log_storage</span><span class="o">=</span><span class="s2">&quot;3&quot;</span><span class="p">,</span>
    <span class="n">log_time</span><span class="o">=</span><span class="s2">&quot;180&quot;</span><span class="p">,</span>
    <span class="n">package_code</span><span class="o">=</span><span class="s2">&quot;version_3&quot;</span><span class="p">,</span>
    <span class="n">period</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">prefessional_service</span><span class="o">=</span><span class="s2">&quot;false&quot;</span><span class="p">,</span>
    <span class="n">resource_group_id</span><span class="o">=</span><span class="s2">&quot;rs-abc12345&quot;</span><span class="p">,</span>
    <span class="n">subscription_type</span><span class="o">=</span><span class="s2">&quot;Subscription&quot;</span><span class="p">,</span>
    <span class="n">waf_log</span><span class="o">=</span><span class="s2">&quot;false&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>big_screen</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify whether big screen is supported. Valid values: [“0”, “1”]. “0” for false and “1” for true.</p></li>
<li><p><strong>exclusive_ip_package</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the number of exclusive WAF IP addresses.</p></li>
<li><p><strong>ext_bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The extra bandwidth. Unit: Mbit/s.</p></li>
<li><p><strong>ext_domain_package</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The number of extra domains.</p></li>
<li><p><strong>log_storage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Log storage size. Unit: T. Valid values: [3, 5, 10, 20, 50].</p></li>
<li><p><strong>log_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Log storage period. Unit: day. Valid values: [180, 360].</p></li>
<li><p><strong>modify_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of configuration change. Valid value: Upgrade.</p></li>
<li><p><strong>package_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subscription plan:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">China</span> <span class="n">site</span> <span class="n">customers</span> <span class="n">can</span> <span class="n">purchase</span> <span class="n">the</span> <span class="n">following</span> <span class="n">versions</span> <span class="n">of</span> <span class="n">China</span> <span class="n">Mainland</span> <span class="n">region</span><span class="p">,</span> <span class="n">valid</span> <span class="n">values</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;version_3&quot;</span><span class="p">,</span> <span class="s2">&quot;version_4&quot;</span><span class="p">,</span> <span class="s2">&quot;version_5&quot;</span><span class="p">]</span><span class="o">.</span>
<span class="o">*</span> <span class="n">China</span> <span class="n">site</span> <span class="n">customers</span> <span class="n">can</span> <span class="n">purchase</span> <span class="n">the</span> <span class="n">following</span> <span class="n">versions</span> <span class="n">of</span> <span class="n">International</span> <span class="n">region</span><span class="p">,</span> <span class="n">valid</span> <span class="n">values</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;version_pro_asia&quot;</span><span class="p">,</span> <span class="s2">&quot;version_business_asia&quot;</span><span class="p">,</span> <span class="s2">&quot;version_enterprise_asia&quot;</span><span class="p">]</span>
<span class="o">*</span> <span class="n">International</span> <span class="n">site</span> <span class="n">customers</span> <span class="n">can</span> <span class="n">purchase</span> <span class="n">the</span> <span class="n">following</span> <span class="n">versions</span> <span class="n">of</span> <span class="n">China</span> <span class="n">Mainland</span> <span class="n">region</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;version_pro_china&quot;</span><span class="p">,</span> <span class="s2">&quot;version_business_china&quot;</span><span class="p">,</span> <span class="s2">&quot;version_enterprise_china&quot;</span><span class="p">]</span>
<span class="o">*</span> <span class="n">International</span> <span class="n">site</span> <span class="n">customers</span> <span class="n">can</span> <span class="n">purchase</span> <span class="n">the</span> <span class="n">following</span> <span class="n">versions</span> <span class="n">of</span> <span class="n">International</span> <span class="n">region</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;version_pro&quot;</span><span class="p">,</span> <span class="s2">&quot;version_business&quot;</span><span class="p">,</span> <span class="s2">&quot;version_enterprise&quot;</span><span class="p">]</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Service time of Web Application Firewall.</p></li>
<li><p><strong>prefessional_service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify whether professional service is supported. Valid values: [“true”, “false”]</p></li>
<li><p><strong>renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Renewal period of WAF service. Unit: month</p></li>
<li><p><strong>renewal_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Renewal status of WAF service. Valid values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">AutoRenewal</span><span class="p">:</span> <span class="n">The</span> <span class="n">service</span> <span class="n">time</span> <span class="n">of</span> <span class="n">WAF</span> <span class="ow">is</span> <span class="n">renewed</span> <span class="n">automatically</span><span class="o">.</span>
<span class="o">*</span> <span class="n">ManualRenewal</span> <span class="p">(</span><span class="n">default</span><span class="p">):</span> <span class="n">The</span> <span class="n">service</span> <span class="n">time</span> <span class="n">of</span> <span class="n">WAF</span> <span class="ow">is</span> <span class="n">renewed</span> <span class="n">manually</span><span class="o">.</span><span class="n">Specifies</span> <span class="n">whether</span> <span class="n">to</span> <span class="n">configure</span> <span class="n">a</span> <span class="n">Layer</span><span class="o">-</span><span class="mi">7</span> <span class="n">proxy</span><span class="p">,</span> <span class="n">such</span> <span class="k">as</span> <span class="n">Anti</span><span class="o">-</span><span class="n">DDoS</span> <span class="n">Pro</span> <span class="ow">or</span> <span class="n">CDN</span><span class="p">,</span> <span class="n">to</span> <span class="nb">filter</span> <span class="n">the</span> <span class="n">inbound</span> <span class="n">traffic</span> <span class="n">before</span> <span class="n">it</span> <span class="ow">is</span> <span class="n">forwarded</span> <span class="n">to</span> <span class="n">WAF</span><span class="o">.</span> <span class="n">Valid</span> <span class="n">values</span><span class="p">:</span> <span class="s2">&quot;On&quot;</span> <span class="ow">and</span> <span class="s2">&quot;Off&quot;</span><span class="o">.</span> <span class="n">Default</span> <span class="n">to</span> <span class="s2">&quot;Off&quot;</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource group ID.</p></li>
<li><p><strong>subscription_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subscription of WAF service. Valid values: [“Subscription”, “PayAsYouGo”].</p></li>
<li><p><strong>waf_log</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify whether Log service is supported. Valid values: [“true”, “false”]</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Instance.big_screen">
<code class="sig-name descname">big_screen</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Instance.big_screen" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify whether big screen is supported. Valid values: [“0”, “1”]. “0” for false and “1” for true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Instance.exclusive_ip_package">
<code class="sig-name descname">exclusive_ip_package</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Instance.exclusive_ip_package" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the number of exclusive WAF IP addresses.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Instance.ext_bandwidth">
<code class="sig-name descname">ext_bandwidth</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Instance.ext_bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>The extra bandwidth. Unit: Mbit/s.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Instance.ext_domain_package">
<code class="sig-name descname">ext_domain_package</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Instance.ext_domain_package" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of extra domains.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Instance.log_storage">
<code class="sig-name descname">log_storage</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Instance.log_storage" title="Permalink to this definition">¶</a></dt>
<dd><p>Log storage size. Unit: T. Valid values: [3, 5, 10, 20, 50].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Instance.log_time">
<code class="sig-name descname">log_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Instance.log_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Log storage period. Unit: day. Valid values: [180, 360].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Instance.modify_type">
<code class="sig-name descname">modify_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Instance.modify_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of configuration change. Valid value: Upgrade.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Instance.package_code">
<code class="sig-name descname">package_code</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Instance.package_code" title="Permalink to this definition">¶</a></dt>
<dd><p>Subscription plan:</p>
<ul class="simple">
<li><p>China site customers can purchase the following versions of China Mainland region, valid values: [“version_3”, “version_4”, “version_5”].</p></li>
<li><p>China site customers can purchase the following versions of International region, valid values: [“version_pro_asia”, “version_business_asia”, “version_enterprise_asia”]</p></li>
<li><p>International site customers can purchase the following versions of China Mainland region: [“version_pro_china”, “version_business_china”, “version_enterprise_china”]</p></li>
<li><p>International site customers can purchase the following versions of International region: [“version_pro”, “version_business”, “version_enterprise”].</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Instance.period">
<code class="sig-name descname">period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Instance.period" title="Permalink to this definition">¶</a></dt>
<dd><p>Service time of Web Application Firewall.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Instance.prefessional_service">
<code class="sig-name descname">prefessional_service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Instance.prefessional_service" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify whether professional service is supported. Valid values: [“true”, “false”]</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Instance.renew_period">
<code class="sig-name descname">renew_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Instance.renew_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Renewal period of WAF service. Unit: month</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Instance.renewal_status">
<code class="sig-name descname">renewal_status</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Instance.renewal_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Renewal status of WAF service. Valid values:</p>
<ul class="simple">
<li><p>AutoRenewal: The service time of WAF is renewed automatically.</p></li>
<li><p>ManualRenewal (default): The service time of WAF is renewed manually.Specifies whether to configure a Layer-7 proxy, such as Anti-DDoS Pro or CDN, to filter the inbound traffic before it is forwarded to WAF. Valid values: “On” and “Off”. Default to “Off”.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Instance.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Instance.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource group ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Instance.status">
<code class="sig-name descname">status</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Instance.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Instance.subscription_type">
<code class="sig-name descname">subscription_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Instance.subscription_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Subscription of WAF service. Valid values: [“Subscription”, “PayAsYouGo”].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.waf.Instance.waf_log">
<code class="sig-name descname">waf_log</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.waf.Instance.waf_log" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify whether Log service is supported. Valid values: [“true”, “false”]</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.waf.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">big_screen</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclusive_ip_package</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ext_bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ext_domain_package</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_storage</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">modify_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prefessional_service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renew_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renewal_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subscription_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">waf_log</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.waf.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>big_screen</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify whether big screen is supported. Valid values: [“0”, “1”]. “0” for false and “1” for true.</p></li>
<li><p><strong>exclusive_ip_package</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the number of exclusive WAF IP addresses.</p></li>
<li><p><strong>ext_bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The extra bandwidth. Unit: Mbit/s.</p></li>
<li><p><strong>ext_domain_package</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The number of extra domains.</p></li>
<li><p><strong>log_storage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Log storage size. Unit: T. Valid values: [3, 5, 10, 20, 50].</p></li>
<li><p><strong>log_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Log storage period. Unit: day. Valid values: [180, 360].</p></li>
<li><p><strong>modify_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of configuration change. Valid value: Upgrade.</p></li>
<li><p><strong>package_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subscription plan:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">China</span> <span class="n">site</span> <span class="n">customers</span> <span class="n">can</span> <span class="n">purchase</span> <span class="n">the</span> <span class="n">following</span> <span class="n">versions</span> <span class="n">of</span> <span class="n">China</span> <span class="n">Mainland</span> <span class="n">region</span><span class="p">,</span> <span class="n">valid</span> <span class="n">values</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;version_3&quot;</span><span class="p">,</span> <span class="s2">&quot;version_4&quot;</span><span class="p">,</span> <span class="s2">&quot;version_5&quot;</span><span class="p">]</span><span class="o">.</span>
<span class="o">*</span> <span class="n">China</span> <span class="n">site</span> <span class="n">customers</span> <span class="n">can</span> <span class="n">purchase</span> <span class="n">the</span> <span class="n">following</span> <span class="n">versions</span> <span class="n">of</span> <span class="n">International</span> <span class="n">region</span><span class="p">,</span> <span class="n">valid</span> <span class="n">values</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;version_pro_asia&quot;</span><span class="p">,</span> <span class="s2">&quot;version_business_asia&quot;</span><span class="p">,</span> <span class="s2">&quot;version_enterprise_asia&quot;</span><span class="p">]</span>
<span class="o">*</span> <span class="n">International</span> <span class="n">site</span> <span class="n">customers</span> <span class="n">can</span> <span class="n">purchase</span> <span class="n">the</span> <span class="n">following</span> <span class="n">versions</span> <span class="n">of</span> <span class="n">China</span> <span class="n">Mainland</span> <span class="n">region</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;version_pro_china&quot;</span><span class="p">,</span> <span class="s2">&quot;version_business_china&quot;</span><span class="p">,</span> <span class="s2">&quot;version_enterprise_china&quot;</span><span class="p">]</span>
<span class="o">*</span> <span class="n">International</span> <span class="n">site</span> <span class="n">customers</span> <span class="n">can</span> <span class="n">purchase</span> <span class="n">the</span> <span class="n">following</span> <span class="n">versions</span> <span class="n">of</span> <span class="n">International</span> <span class="n">region</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;version_pro&quot;</span><span class="p">,</span> <span class="s2">&quot;version_business&quot;</span><span class="p">,</span> <span class="s2">&quot;version_enterprise&quot;</span><span class="p">]</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Service time of Web Application Firewall.</p></li>
<li><p><strong>prefessional_service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify whether professional service is supported. Valid values: [“true”, “false”]</p></li>
<li><p><strong>renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Renewal period of WAF service. Unit: month</p></li>
<li><p><strong>renewal_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Renewal status of WAF service. Valid values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">AutoRenewal</span><span class="p">:</span> <span class="n">The</span> <span class="n">service</span> <span class="n">time</span> <span class="n">of</span> <span class="n">WAF</span> <span class="ow">is</span> <span class="n">renewed</span> <span class="n">automatically</span><span class="o">.</span>
<span class="o">*</span> <span class="n">ManualRenewal</span> <span class="p">(</span><span class="n">default</span><span class="p">):</span> <span class="n">The</span> <span class="n">service</span> <span class="n">time</span> <span class="n">of</span> <span class="n">WAF</span> <span class="ow">is</span> <span class="n">renewed</span> <span class="n">manually</span><span class="o">.</span><span class="n">Specifies</span> <span class="n">whether</span> <span class="n">to</span> <span class="n">configure</span> <span class="n">a</span> <span class="n">Layer</span><span class="o">-</span><span class="mi">7</span> <span class="n">proxy</span><span class="p">,</span> <span class="n">such</span> <span class="k">as</span> <span class="n">Anti</span><span class="o">-</span><span class="n">DDoS</span> <span class="n">Pro</span> <span class="ow">or</span> <span class="n">CDN</span><span class="p">,</span> <span class="n">to</span> <span class="nb">filter</span> <span class="n">the</span> <span class="n">inbound</span> <span class="n">traffic</span> <span class="n">before</span> <span class="n">it</span> <span class="ow">is</span> <span class="n">forwarded</span> <span class="n">to</span> <span class="n">WAF</span><span class="o">.</span> <span class="n">Valid</span> <span class="n">values</span><span class="p">:</span> <span class="s2">&quot;On&quot;</span> <span class="ow">and</span> <span class="s2">&quot;Off&quot;</span><span class="o">.</span> <span class="n">Default</span> <span class="n">to</span> <span class="s2">&quot;Off&quot;</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource group ID.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The status of the instance.</p></li>
<li><p><strong>subscription_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Subscription of WAF service. Valid values: [“Subscription”, “PayAsYouGo”].</p></li>
<li><p><strong>waf_log</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify whether Log service is supported. Valid values: [“true”, “false”]</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.waf.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.waf.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.waf.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.waf.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.waf.get_domains">
<code class="sig-prename descclassname">pulumi_alicloud.waf.</code><code class="sig-name descname">get_domains</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.waf.get_domains" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a WAF datasource to retrieve domains.</p>
<p>For information about WAF and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/28517.htm">What is Alibaba Cloud WAF</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.86.0+ .</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">waf</span><span class="o">.</span><span class="n">get_domains</span><span class="p">(</span><span class="n">instance_id</span><span class="o">=</span><span class="s2">&quot;waf-cf-xxxxx&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of WAF domain names. Each item is domain name.</p></li>
<li><p><strong>instance_id</strong> (<em>str</em>) – The Id of waf instance to which waf domain belongs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
