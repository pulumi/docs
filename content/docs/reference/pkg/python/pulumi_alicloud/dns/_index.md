---
title: Module dns
title_tag: Module dns | Package pulumi_alicloud | Python SDK
linktitle: dns
notitle: true
---

<div class="section" id="dns">
<h1>dns<a class="headerlink" href="#dns" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.dns"></span><dl class="class">
<dt id="pulumi_alicloud.dns.AwaitableGetDomainGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">AwaitableGetDomainGroupsResult</code><span class="sig-paren">(</span><em class="sig-param">groups=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.AwaitableGetDomainGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.dns.AwaitableGetDomainRecordsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">AwaitableGetDomainRecordsResult</code><span class="sig-paren">(</span><em class="sig-param">domain_name=None</em>, <em class="sig-param">host_record_regex=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">is_locked=None</em>, <em class="sig-param">line=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">records=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">urls=None</em>, <em class="sig-param">value_regex=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.AwaitableGetDomainRecordsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.dns.AwaitableGetDomainsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">AwaitableGetDomainsResult</code><span class="sig-paren">(</span><em class="sig-param">ali_domain=None</em>, <em class="sig-param">domain_name_regex=None</em>, <em class="sig-param">domains=None</em>, <em class="sig-param">group_name_regex=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">resource_group_id=None</em>, <em class="sig-param">version_code=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.AwaitableGetDomainsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.dns.AwaitableGetGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">AwaitableGetGroupsResult</code><span class="sig-paren">(</span><em class="sig-param">groups=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.AwaitableGetGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.dns.AwaitableGetRecordsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">AwaitableGetRecordsResult</code><span class="sig-paren">(</span><em class="sig-param">domain_name=None</em>, <em class="sig-param">host_record_regex=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">is_locked=None</em>, <em class="sig-param">line=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">records=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">urls=None</em>, <em class="sig-param">value_regex=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.AwaitableGetRecordsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.dns.AwaitableGetResolutionLinesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">AwaitableGetResolutionLinesResult</code><span class="sig-paren">(</span><em class="sig-param">domain_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">lang=None</em>, <em class="sig-param">line_codes=None</em>, <em class="sig-param">line_display_names=None</em>, <em class="sig-param">line_names=None</em>, <em class="sig-param">lines=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">user_client_ip=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.AwaitableGetResolutionLinesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.dns.DdosBgpInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">DdosBgpInstance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bandwidth=None</em>, <em class="sig-param">base_bandwidth=None</em>, <em class="sig-param">ip_count=None</em>, <em class="sig-param">ip_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.DdosBgpInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Anti-DDoS Advanced instance resource. “Ddosbgp” is the short term of this product.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The endpoint of bssopenapi used only support “business.aliyuncs.com” at present.</p>
<p><strong>NOTE:</strong> Available in 1.57.0+ .</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/ddosbgp_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/ddosbgp_instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Elastic defend bandwidth of the instance. This value must be larger than the base defend bandwidth. Valid values: 51,91,101,201,301. The unit is Gbps.</p></li>
<li><p><strong>base_bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Base defend bandwidth of the instance. Valid values: 20. The unit is Gbps. Default to <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><strong>ip_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – IP count of the instance. Valid values: 100.</p></li>
<li><p><strong>ip_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP version of the instance. Valid values: IPv4,IPv6.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the instance. This name can have a string of 1 to 63 characters.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy Ddosbgp instance (in month). Valid values: [1~9], 12, 24, 36. Default to 12. At present, the provider does not support modify “period”.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the instance. Valid values: Enterprise,Professional. Default to <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.dns.DdosBgpInstance.bandwidth">
<code class="sig-name descname">bandwidth</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.DdosBgpInstance.bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>Elastic defend bandwidth of the instance. This value must be larger than the base defend bandwidth. Valid values: 51,91,101,201,301. The unit is Gbps.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.DdosBgpInstance.base_bandwidth">
<code class="sig-name descname">base_bandwidth</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.DdosBgpInstance.base_bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>Base defend bandwidth of the instance. Valid values: 20. The unit is Gbps. Default to <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.DdosBgpInstance.ip_count">
<code class="sig-name descname">ip_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.DdosBgpInstance.ip_count" title="Permalink to this definition">¶</a></dt>
<dd><p>IP count of the instance. Valid values: 100.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.DdosBgpInstance.ip_type">
<code class="sig-name descname">ip_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.DdosBgpInstance.ip_type" title="Permalink to this definition">¶</a></dt>
<dd><p>IP version of the instance. Valid values: IPv4,IPv6.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.DdosBgpInstance.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.DdosBgpInstance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the instance. This name can have a string of 1 to 63 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.DdosBgpInstance.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.DdosBgpInstance.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration that you will buy Ddosbgp instance (in month). Valid values: [1~9], 12, 24, 36. Default to 12. At present, the provider does not support modify “period”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.DdosBgpInstance.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.DdosBgpInstance.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the instance. Valid values: Enterprise,Professional. Default to <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.dns.DdosBgpInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bandwidth=None</em>, <em class="sig-param">base_bandwidth=None</em>, <em class="sig-param">ip_count=None</em>, <em class="sig-param">ip_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.DdosBgpInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DdosBgpInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Elastic defend bandwidth of the instance. This value must be larger than the base defend bandwidth. Valid values: 51,91,101,201,301. The unit is Gbps.</p></li>
<li><p><strong>base_bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Base defend bandwidth of the instance. Valid values: 20. The unit is Gbps. Default to <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><strong>ip_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – IP count of the instance. Valid values: 100.</p></li>
<li><p><strong>ip_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IP version of the instance. Valid values: IPv4,IPv6.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the instance. This name can have a string of 1 to 63 characters.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy Ddosbgp instance (in month). Valid values: [1~9], 12, 24, 36. Default to 12. At present, the provider does not support modify “period”.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the instance. Valid values: Enterprise,Professional. Default to <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.dns.DdosBgpInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.DdosBgpInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.dns.DdosBgpInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.DdosBgpInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.dns.DdosCooInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">DdosCooInstance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bandwidth=None</em>, <em class="sig-param">base_bandwidth=None</em>, <em class="sig-param">domain_count=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">port_count=None</em>, <em class="sig-param">service_bandwidth=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.DdosCooInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>BGP-Line Anti-DDoS instance resource. “Ddoscoo” is the short term of this product. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/69319.htm">What is Anti-DDoS Pro</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The product region only support cn-hangzhou.</p>
<p><strong>NOTE:</strong> The endpoint of bssopenapi used only support “business.aliyuncs.com” at present.</p>
<p><strong>NOTE:</strong> Available in 1.37.0+ .</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/ddoscoo_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/ddoscoo_instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Elastic defend bandwidth of the instance. This value must be larger than the base defend bandwidth. Valid values: 30, 60, 100, 300, 400, 500, 600. The unit is Gbps. Only support upgrade.</p></li>
<li><p><strong>base_bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base defend bandwidth of the instance. Valid values: 30, 60, 100, 300, 400, 500, 600. The unit is Gbps. Only support upgrade.</p></li>
<li><p><strong>domain_count</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain retransmission rule count of the instance. At least 50. Increase 5 per step, such as 55, 60, 65. Only support upgrade.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the instance. This name can have a string of 1 to 63 characters.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy Ddoscoo instance (in month). Valid values: [1~9], 12, 24, 36. Default to 1. At present, the provider does not support modify “period”.</p></li>
<li><p><strong>port_count</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Port retransmission rule count of the instance. At least 50. Increase 5 per step, such as 55, 60, 65. Only support upgrade.</p></li>
<li><p><strong>service_bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Business bandwidth of the instance. At leaset 100. Increased 100 per step, such as 100, 200, 300. The unit is Mbps. Only support upgrade.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.dns.DdosCooInstance.bandwidth">
<code class="sig-name descname">bandwidth</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.DdosCooInstance.bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>Elastic defend bandwidth of the instance. This value must be larger than the base defend bandwidth. Valid values: 30, 60, 100, 300, 400, 500, 600. The unit is Gbps. Only support upgrade.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.DdosCooInstance.base_bandwidth">
<code class="sig-name descname">base_bandwidth</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.DdosCooInstance.base_bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>Base defend bandwidth of the instance. Valid values: 30, 60, 100, 300, 400, 500, 600. The unit is Gbps. Only support upgrade.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.DdosCooInstance.domain_count">
<code class="sig-name descname">domain_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.DdosCooInstance.domain_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain retransmission rule count of the instance. At least 50. Increase 5 per step, such as 55, 60, 65. Only support upgrade.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.DdosCooInstance.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.DdosCooInstance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the instance. This name can have a string of 1 to 63 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.DdosCooInstance.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.DdosCooInstance.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration that you will buy Ddoscoo instance (in month). Valid values: [1~9], 12, 24, 36. Default to 1. At present, the provider does not support modify “period”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.DdosCooInstance.port_count">
<code class="sig-name descname">port_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.DdosCooInstance.port_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Port retransmission rule count of the instance. At least 50. Increase 5 per step, such as 55, 60, 65. Only support upgrade.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.DdosCooInstance.service_bandwidth">
<code class="sig-name descname">service_bandwidth</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.DdosCooInstance.service_bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>Business bandwidth of the instance. At leaset 100. Increased 100 per step, such as 100, 200, 300. The unit is Mbps. Only support upgrade.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.dns.DdosCooInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bandwidth=None</em>, <em class="sig-param">base_bandwidth=None</em>, <em class="sig-param">domain_count=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">port_count=None</em>, <em class="sig-param">service_bandwidth=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.DdosCooInstance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DdosCooInstance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Elastic defend bandwidth of the instance. This value must be larger than the base defend bandwidth. Valid values: 30, 60, 100, 300, 400, 500, 600. The unit is Gbps. Only support upgrade.</p></li>
<li><p><strong>base_bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base defend bandwidth of the instance. Valid values: 30, 60, 100, 300, 400, 500, 600. The unit is Gbps. Only support upgrade.</p></li>
<li><p><strong>domain_count</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Domain retransmission rule count of the instance. At least 50. Increase 5 per step, such as 55, 60, 65. Only support upgrade.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the instance. This name can have a string of 1 to 63 characters.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The duration that you will buy Ddoscoo instance (in month). Valid values: [1~9], 12, 24, 36. Default to 1. At present, the provider does not support modify “period”.</p></li>
<li><p><strong>port_count</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Port retransmission rule count of the instance. At least 50. Increase 5 per step, such as 55, 60, 65. Only support upgrade.</p></li>
<li><p><strong>service_bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Business bandwidth of the instance. At leaset 100. Increased 100 per step, such as 100, 200, 300. The unit is Mbps. Only support upgrade.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.dns.DdosCooInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.DdosCooInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.dns.DdosCooInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.DdosCooInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.dns.Domain">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">Domain</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.Domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DNS resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The domain name which you want to add must be already registered and had not added by another account. Every domain name can only exist in a unique group.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/dns.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/dns.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of the group in which the domain will add. If not supplied, then use default group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or “-“, and must not begin or end with “-“, and “-” must not in the 3th and 4th character positions at the same time. Suffix <code class="docutils literal notranslate"><span class="pre">.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">.tel</span></code> are not supported.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of resource group which the dns belongs.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.dns.Domain.dns_servers">
<code class="sig-name descname">dns_servers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.Domain.dns_servers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the dns server name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.Domain.domain_id">
<code class="sig-name descname">domain_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.Domain.domain_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The domain ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.Domain.group_id">
<code class="sig-name descname">group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.Domain.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Id of the group in which the domain will add. If not supplied, then use default group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.Domain.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.Domain.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or “-“, and must not begin or end with “-“, and “-” must not in the 3th and 4th character positions at the same time. Suffix <code class="docutils literal notranslate"><span class="pre">.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">.tel</span></code> are not supported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.Domain.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.Domain.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of resource group which the dns belongs.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.dns.Domain.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dns_servers=None</em>, <em class="sig-param">domain_id=None</em>, <em class="sig-param">group_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.Domain.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Domain resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dns_servers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the dns server name.</p></li>
<li><p><strong>domain_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The domain ID.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of the group in which the domain will add. If not supplied, then use default group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or “-“, and must not begin or end with “-“, and “-” must not in the 3th and 4th character positions at the same time. Suffix <code class="docutils literal notranslate"><span class="pre">.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">.tel</span></code> are not supported.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Id of resource group which the dns belongs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.dns.Domain.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.Domain.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.dns.Domain.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.Domain.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.dns.GetDomainGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">GetDomainGroupsResult</code><span class="sig-paren">(</span><em class="sig-param">groups=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.GetDomainGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDomainGroups.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetDomainGroupsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetDomainGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.dns.GetDomainRecordsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">GetDomainRecordsResult</code><span class="sig-paren">(</span><em class="sig-param">domain_name=None</em>, <em class="sig-param">host_record_regex=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">is_locked=None</em>, <em class="sig-param">line=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">records=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">urls=None</em>, <em class="sig-param">value_regex=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.GetDomainRecordsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDomainRecords.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetDomainRecordsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetDomainRecordsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.dns.GetDomainsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">GetDomainsResult</code><span class="sig-paren">(</span><em class="sig-param">ali_domain=None</em>, <em class="sig-param">domain_name_regex=None</em>, <em class="sig-param">domains=None</em>, <em class="sig-param">group_name_regex=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">resource_group_id=None</em>, <em class="sig-param">version_code=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.GetDomainsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDomains.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetDomainsResult.ali_domain">
<code class="sig-name descname">ali_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetDomainsResult.ali_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the domain is an Alibaba Cloud domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetDomainsResult.domains">
<code class="sig-name descname">domains</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetDomainsResult.domains" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of domains. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetDomainsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetDomainsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetDomainsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetDomainsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of domain IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetDomainsResult.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetDomainsResult.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud analysis product ID of the domain.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetDomainsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetDomainsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of domain names.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetDomainsResult.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetDomainsResult.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Id of resource group which the dns belongs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetDomainsResult.version_code">
<code class="sig-name descname">version_code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetDomainsResult.version_code" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud analysis version code of the domain.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.dns.GetGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">GetGroupsResult</code><span class="sig-paren">(</span><em class="sig-param">groups=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.GetGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroups.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetGroupsResult.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetGroupsResult.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of groups. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetGroupsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetGroupsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetGroupsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of group IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetGroupsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetGroupsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of group names.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.dns.GetRecordsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">GetRecordsResult</code><span class="sig-paren">(</span><em class="sig-param">domain_name=None</em>, <em class="sig-param">host_record_regex=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">is_locked=None</em>, <em class="sig-param">line=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">records=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">urls=None</em>, <em class="sig-param">value_regex=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.GetRecordsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRecords.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetRecordsResult.domain_name">
<code class="sig-name descname">domain_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetRecordsResult.domain_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the domain the record belongs to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetRecordsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetRecordsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetRecordsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetRecordsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of record IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetRecordsResult.line">
<code class="sig-name descname">line</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetRecordsResult.line" title="Permalink to this definition">¶</a></dt>
<dd><p>ISP line of the record.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetRecordsResult.records">
<code class="sig-name descname">records</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetRecordsResult.records" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of records. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetRecordsResult.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetRecordsResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the record.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetRecordsResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetRecordsResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the record.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetRecordsResult.urls">
<code class="sig-name descname">urls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetRecordsResult.urls" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of entire URLs. Each item format as <code class="docutils literal notranslate"><span class="pre">&lt;host_record&gt;.&lt;domain_name&gt;</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.dns.GetResolutionLinesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">GetResolutionLinesResult</code><span class="sig-paren">(</span><em class="sig-param">domain_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">lang=None</em>, <em class="sig-param">line_codes=None</em>, <em class="sig-param">line_display_names=None</em>, <em class="sig-param">line_names=None</em>, <em class="sig-param">lines=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">user_client_ip=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.GetResolutionLinesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getResolutionLines.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetResolutionLinesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetResolutionLinesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetResolutionLinesResult.line_codes">
<code class="sig-name descname">line_codes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetResolutionLinesResult.line_codes" title="Permalink to this definition">¶</a></dt>
<dd><p>Line code.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetResolutionLinesResult.line_display_names">
<code class="sig-name descname">line_display_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetResolutionLinesResult.line_display_names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of line display names.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.GetResolutionLinesResult.lines">
<code class="sig-name descname">lines</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.GetResolutionLinesResult.lines" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of cloud resolution line. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.dns.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DNS Group resource.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/dns_group.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/dns_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the domain group.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.dns.Group.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the domain group.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.dns.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the domain group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.dns.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.dns.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.dns.Record">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">Record</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">host_record=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">routing=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.Record" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a DNS Record resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> When the site is an international site, the <code class="docutils literal notranslate"><span class="pre">type</span></code> neither supports <code class="docutils literal notranslate"><span class="pre">REDIRECT_URL</span></code> nor <code class="docutils literal notranslate"><span class="pre">REDIRECT_URL</span></code></p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/dns_record.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/dns_record.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>host_record</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Host record for the domain record. This host_record can have at most 253 characters, and each part split with “.” can have at most 63 characters, and must contain only alphanumeric characters or hyphens, such as “-“,”.”,”*”,”&#64;”,  and must not begin or end with “-“.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or “-“, and must not begin or end with “-“, and “-” must not in the 3th and 4th character positions at the same time. Suffix <code class="docutils literal notranslate"><span class="pre">.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">.tel</span></code> are not supported.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of domain record. Valid values are <code class="docutils literal notranslate"><span class="pre">[1-10]</span></code>. When the <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">MX</span></code>, this parameter is required.</p></li>
<li><p><strong>routing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resolution line of domain record. Valid values are <code class="docutils literal notranslate"><span class="pre">default</span></code>, <code class="docutils literal notranslate"><span class="pre">telecom</span></code>, <code class="docutils literal notranslate"><span class="pre">unicom</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile</span></code>, <code class="docutils literal notranslate"><span class="pre">oversea</span></code>, <code class="docutils literal notranslate"><span class="pre">edu</span></code>, <code class="docutils literal notranslate"><span class="pre">drpeng</span></code>, <code class="docutils literal notranslate"><span class="pre">btvn</span></code>, .etc. When the <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">FORWORD_URL</span></code>, this parameter must be <code class="docutils literal notranslate"><span class="pre">default</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">default</span></code>. For checking all resolution lines enumeration please visit <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/34339.htm">Alibaba Cloud DNS doc</a> or using dns.getResolutionLines in data source to get the value.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The effective time of domain record. Its scope depends on the edition of the cloud resolution. Free is <code class="docutils literal notranslate"><span class="pre">[600,</span> <span class="pre">86400]</span></code>, Basic is <code class="docutils literal notranslate"><span class="pre">[120,</span> <span class="pre">86400]</span></code>, Standard is <code class="docutils literal notranslate"><span class="pre">[60,</span> <span class="pre">86400]</span></code>, Ultimate is <code class="docutils literal notranslate"><span class="pre">[10,</span> <span class="pre">86400]</span></code>, Exclusive is <code class="docutils literal notranslate"><span class="pre">[1,</span> <span class="pre">86400]</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">600</span></code>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of domain record. Valid values are <code class="docutils literal notranslate"><span class="pre">A</span></code>,<code class="docutils literal notranslate"><span class="pre">NS</span></code>,<code class="docutils literal notranslate"><span class="pre">MX</span></code>,<code class="docutils literal notranslate"><span class="pre">TXT</span></code>,<code class="docutils literal notranslate"><span class="pre">CNAME</span></code>,<code class="docutils literal notranslate"><span class="pre">SRV</span></code>,<code class="docutils literal notranslate"><span class="pre">AAAA</span></code>,<code class="docutils literal notranslate"><span class="pre">CAA</span></code>, <code class="docutils literal notranslate"><span class="pre">REDIRECT_URL</span></code> and <code class="docutils literal notranslate"><span class="pre">FORWORD_URL</span></code>.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of domain record, When the <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">MX</span></code>,<code class="docutils literal notranslate"><span class="pre">NS</span></code>,<code class="docutils literal notranslate"><span class="pre">CNAME</span></code>,<code class="docutils literal notranslate"><span class="pre">SRV</span></code>, the server will treat the <code class="docutils literal notranslate"><span class="pre">value</span></code> as a fully qualified domain name, so it’s no need to add a <code class="docutils literal notranslate"><span class="pre">.</span></code> at the end.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.dns.Record.host_record">
<code class="sig-name descname">host_record</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.Record.host_record" title="Permalink to this definition">¶</a></dt>
<dd><p>Host record for the domain record. This host_record can have at most 253 characters, and each part split with “.” can have at most 63 characters, and must contain only alphanumeric characters or hyphens, such as “-“,”.”,”*”,”&#64;”,  and must not begin or end with “-“.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.Record.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.Record.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or “-“, and must not begin or end with “-“, and “-” must not in the 3th and 4th character positions at the same time. Suffix <code class="docutils literal notranslate"><span class="pre">.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">.tel</span></code> are not supported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.Record.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.Record.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of domain record. Valid values are <code class="docutils literal notranslate"><span class="pre">[1-10]</span></code>. When the <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">MX</span></code>, this parameter is required.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.Record.routing">
<code class="sig-name descname">routing</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.Record.routing" title="Permalink to this definition">¶</a></dt>
<dd><p>The resolution line of domain record. Valid values are <code class="docutils literal notranslate"><span class="pre">default</span></code>, <code class="docutils literal notranslate"><span class="pre">telecom</span></code>, <code class="docutils literal notranslate"><span class="pre">unicom</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile</span></code>, <code class="docutils literal notranslate"><span class="pre">oversea</span></code>, <code class="docutils literal notranslate"><span class="pre">edu</span></code>, <code class="docutils literal notranslate"><span class="pre">drpeng</span></code>, <code class="docutils literal notranslate"><span class="pre">btvn</span></code>, .etc. When the <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">FORWORD_URL</span></code>, this parameter must be <code class="docutils literal notranslate"><span class="pre">default</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">default</span></code>. For checking all resolution lines enumeration please visit <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/34339.htm">Alibaba Cloud DNS doc</a> or using dns.getResolutionLines in data source to get the value.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.Record.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.Record.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The record status. <code class="docutils literal notranslate"><span class="pre">Enable</span></code> or <code class="docutils literal notranslate"><span class="pre">Disable</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.Record.ttl">
<code class="sig-name descname">ttl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.Record.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The effective time of domain record. Its scope depends on the edition of the cloud resolution. Free is <code class="docutils literal notranslate"><span class="pre">[600,</span> <span class="pre">86400]</span></code>, Basic is <code class="docutils literal notranslate"><span class="pre">[120,</span> <span class="pre">86400]</span></code>, Standard is <code class="docutils literal notranslate"><span class="pre">[60,</span> <span class="pre">86400]</span></code>, Ultimate is <code class="docutils literal notranslate"><span class="pre">[10,</span> <span class="pre">86400]</span></code>, Exclusive is <code class="docutils literal notranslate"><span class="pre">[1,</span> <span class="pre">86400]</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">600</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.Record.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.Record.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of domain record. Valid values are <code class="docutils literal notranslate"><span class="pre">A</span></code>,<code class="docutils literal notranslate"><span class="pre">NS</span></code>,<code class="docutils literal notranslate"><span class="pre">MX</span></code>,<code class="docutils literal notranslate"><span class="pre">TXT</span></code>,<code class="docutils literal notranslate"><span class="pre">CNAME</span></code>,<code class="docutils literal notranslate"><span class="pre">SRV</span></code>,<code class="docutils literal notranslate"><span class="pre">AAAA</span></code>,<code class="docutils literal notranslate"><span class="pre">CAA</span></code>, <code class="docutils literal notranslate"><span class="pre">REDIRECT_URL</span></code> and <code class="docutils literal notranslate"><span class="pre">FORWORD_URL</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.dns.Record.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.dns.Record.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of domain record, When the <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">MX</span></code>,<code class="docutils literal notranslate"><span class="pre">NS</span></code>,<code class="docutils literal notranslate"><span class="pre">CNAME</span></code>,<code class="docutils literal notranslate"><span class="pre">SRV</span></code>, the server will treat the <code class="docutils literal notranslate"><span class="pre">value</span></code> as a fully qualified domain name, so it’s no need to add a <code class="docutils literal notranslate"><span class="pre">.</span></code> at the end.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.dns.Record.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">host_record=None</em>, <em class="sig-param">locked=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">routing=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">ttl=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.Record.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Record resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>host_record</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Host record for the domain record. This host_record can have at most 253 characters, and each part split with “.” can have at most 63 characters, and must contain only alphanumeric characters or hyphens, such as “-“,”.”,”*”,”&#64;”,  and must not begin or end with “-“.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the domain. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or “-“, and must not begin or end with “-“, and “-” must not in the 3th and 4th character positions at the same time. Suffix <code class="docutils literal notranslate"><span class="pre">.sh</span></code> and <code class="docutils literal notranslate"><span class="pre">.tel</span></code> are not supported.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of domain record. Valid values are <code class="docutils literal notranslate"><span class="pre">[1-10]</span></code>. When the <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">MX</span></code>, this parameter is required.</p></li>
<li><p><strong>routing</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The resolution line of domain record. Valid values are <code class="docutils literal notranslate"><span class="pre">default</span></code>, <code class="docutils literal notranslate"><span class="pre">telecom</span></code>, <code class="docutils literal notranslate"><span class="pre">unicom</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile</span></code>, <code class="docutils literal notranslate"><span class="pre">oversea</span></code>, <code class="docutils literal notranslate"><span class="pre">edu</span></code>, <code class="docutils literal notranslate"><span class="pre">drpeng</span></code>, <code class="docutils literal notranslate"><span class="pre">btvn</span></code>, .etc. When the <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">FORWORD_URL</span></code>, this parameter must be <code class="docutils literal notranslate"><span class="pre">default</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">default</span></code>. For checking all resolution lines enumeration please visit <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/34339.htm">Alibaba Cloud DNS doc</a> or using dns.getResolutionLines in data source to get the value.</p>
</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The record status. <code class="docutils literal notranslate"><span class="pre">Enable</span></code> or <code class="docutils literal notranslate"><span class="pre">Disable</span></code>.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The effective time of domain record. Its scope depends on the edition of the cloud resolution. Free is <code class="docutils literal notranslate"><span class="pre">[600,</span> <span class="pre">86400]</span></code>, Basic is <code class="docutils literal notranslate"><span class="pre">[120,</span> <span class="pre">86400]</span></code>, Standard is <code class="docutils literal notranslate"><span class="pre">[60,</span> <span class="pre">86400]</span></code>, Ultimate is <code class="docutils literal notranslate"><span class="pre">[10,</span> <span class="pre">86400]</span></code>, Exclusive is <code class="docutils literal notranslate"><span class="pre">[1,</span> <span class="pre">86400]</span></code>. Default value is <code class="docutils literal notranslate"><span class="pre">600</span></code>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of domain record. Valid values are <code class="docutils literal notranslate"><span class="pre">A</span></code>,<code class="docutils literal notranslate"><span class="pre">NS</span></code>,<code class="docutils literal notranslate"><span class="pre">MX</span></code>,<code class="docutils literal notranslate"><span class="pre">TXT</span></code>,<code class="docutils literal notranslate"><span class="pre">CNAME</span></code>,<code class="docutils literal notranslate"><span class="pre">SRV</span></code>,<code class="docutils literal notranslate"><span class="pre">AAAA</span></code>,<code class="docutils literal notranslate"><span class="pre">CAA</span></code>, <code class="docutils literal notranslate"><span class="pre">REDIRECT_URL</span></code> and <code class="docutils literal notranslate"><span class="pre">FORWORD_URL</span></code>.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of domain record, When the <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">MX</span></code>,<code class="docutils literal notranslate"><span class="pre">NS</span></code>,<code class="docutils literal notranslate"><span class="pre">CNAME</span></code>,<code class="docutils literal notranslate"><span class="pre">SRV</span></code>, the server will treat the <code class="docutils literal notranslate"><span class="pre">value</span></code> as a fully qualified domain name, so it’s no need to add a <code class="docutils literal notranslate"><span class="pre">.</span></code> at the end.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.dns.Record.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.Record.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.dns.Record.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.Record.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.dns.get_domain_groups">
<code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">get_domain_groups</code><span class="sig-paren">(</span><em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.get_domain_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.dns.get_domain_records">
<code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">get_domain_records</code><span class="sig-paren">(</span><em class="sig-param">domain_name=None</em>, <em class="sig-param">host_record_regex=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">is_locked=None</em>, <em class="sig-param">line=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">value_regex=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.get_domain_records" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.dns.get_domains">
<code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">get_domains</code><span class="sig-paren">(</span><em class="sig-param">ali_domain=None</em>, <em class="sig-param">domain_name_regex=None</em>, <em class="sig-param">group_name_regex=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">resource_group_id=None</em>, <em class="sig-param">version_code=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.get_domains" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of DNS Domains in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/dns_domains.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/dns_domains.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ali_domain</strong> (<em>bool</em>) – Specifies whether the domain is from Alibaba Cloud or not.</p></li>
<li><p><strong>domain_name_regex</strong> (<em>str</em>) – A regex string to filter results by the domain name.</p></li>
<li><p><strong>group_name_regex</strong> (<em>str</em>) – A regex string to filter results by the group name.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of domain IDs.</p></li>
<li><p><strong>instance_id</strong> (<em>str</em>) – Cloud analysis product ID.</p></li>
<li><p><strong>resource_group_id</strong> (<em>str</em>) – The Id of resource group which the dns belongs.</p></li>
<li><p><strong>version_code</strong> (<em>str</em>) – Cloud analysis version code.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `ids` (Optional, Available in 1.53.0+) - A list of domain IDs.
</pre></div>
</div>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.dns.get_groups">
<code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">get_groups</code><span class="sig-paren">(</span><em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.get_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of DNS Domain Groups in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/dns_groups.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/dns_groups.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of group IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by group name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.dns.get_records">
<code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">get_records</code><span class="sig-paren">(</span><em class="sig-param">domain_name=None</em>, <em class="sig-param">host_record_regex=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">is_locked=None</em>, <em class="sig-param">line=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">value_regex=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.get_records" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of DNS Domain Records in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/dns_records.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/dns_records.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain_name</strong> (<em>str</em>) – The domain name associated to the records.</p></li>
<li><p><strong>host_record_regex</strong> (<em>str</em>) – Host record regex.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of record IDs.</p></li>
<li><p><strong>is_locked</strong> (<em>bool</em>) – Whether the record is locked or not.</p></li>
<li><p><strong>line</strong> (<em>str</em>) – <p>ISP line. Valid items are <code class="docutils literal notranslate"><span class="pre">default</span></code>, <code class="docutils literal notranslate"><span class="pre">telecom</span></code>, <code class="docutils literal notranslate"><span class="pre">unicom</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile</span></code>, <code class="docutils literal notranslate"><span class="pre">oversea</span></code>, <code class="docutils literal notranslate"><span class="pre">edu</span></code>, <code class="docutils literal notranslate"><span class="pre">drpeng</span></code>, <code class="docutils literal notranslate"><span class="pre">btvn</span></code>, .etc. For checking all resolution lines enumeration please visit <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/34339.htm">Alibaba Cloud DNS doc</a></p>
</p></li>
<li><p><strong>status</strong> (<em>str</em>) – Record status. Valid items are <code class="docutils literal notranslate"><span class="pre">ENABLE</span></code> and <code class="docutils literal notranslate"><span class="pre">DISABLE</span></code>.</p></li>
<li><p><strong>type</strong> (<em>str</em>) – Record type. Valid items are <code class="docutils literal notranslate"><span class="pre">A</span></code>, <code class="docutils literal notranslate"><span class="pre">NS</span></code>, <code class="docutils literal notranslate"><span class="pre">MX</span></code>, <code class="docutils literal notranslate"><span class="pre">TXT</span></code>, <code class="docutils literal notranslate"><span class="pre">CNAME</span></code>, <code class="docutils literal notranslate"><span class="pre">SRV</span></code>, <code class="docutils literal notranslate"><span class="pre">AAAA</span></code>, <code class="docutils literal notranslate"><span class="pre">REDIRECT_URL</span></code>, <code class="docutils literal notranslate"><span class="pre">FORWORD_URL</span></code> .</p></li>
<li><p><strong>value_regex</strong> (<em>str</em>) – Host record value regex.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.dns.get_resolution_lines">
<code class="sig-prename descclassname">pulumi_alicloud.dns.</code><code class="sig-name descname">get_resolution_lines</code><span class="sig-paren">(</span><em class="sig-param">domain_name=None</em>, <em class="sig-param">lang=None</em>, <em class="sig-param">line_codes=None</em>, <em class="sig-param">line_display_names=None</em>, <em class="sig-param">line_names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">user_client_ip=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.dns.get_resolution_lines" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of DNS Resolution Lines in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.60.0.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/dns_resolution_lines.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/dns_resolution_lines.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>domain_name</strong> (<em>str</em>) – Domain Name.</p></li>
<li><p><strong>lang</strong> (<em>str</em>) – language.</p></li>
<li><p><strong>line_codes</strong> (<em>list</em>) – A list of lines codes.</p></li>
<li><p><strong>line_display_names</strong> (<em>list</em>) – A list of line display names.</p></li>
<li><p><strong>user_client_ip</strong> (<em>str</em>) – The ip of user client.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
