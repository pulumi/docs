---
title: Module ddos
title_tag: Module ddos | Package pulumi_alicloud | Python SDK
linktitle: ddos
notitle: true
---

<div class="section" id="ddos">
<h1>ddos<a class="headerlink" href="#ddos" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.ddos"></span><dl class="py class">
<dt id="pulumi_alicloud.ddos.AwaitableGetDdosBgpInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ddos.</code><code class="sig-name descname">AwaitableGetDdosBgpInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ddos.AwaitableGetDdosBgpInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ddos.AwaitableGetDdosCooInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ddos.</code><code class="sig-name descname">AwaitableGetDdosCooInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ddos.AwaitableGetDdosCooInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ddos.DdosBgpInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ddos.</code><code class="sig-name descname">DdosBgpInstance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">base_bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ddos.DdosBgpInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>Anti-DDoS Advanced instance resource. “Ddosbgp” is the short term of this product.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The endpoint of bssopenapi used only support “business.aliyuncs.com” at present.</p>
<p><strong>NOTE:</strong> Available in 1.57.0+ .</p>
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
<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.DdosBgpInstance.bandwidth">
<code class="sig-name descname">bandwidth</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.DdosBgpInstance.bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>Elastic defend bandwidth of the instance. This value must be larger than the base defend bandwidth. Valid values: 51,91,101,201,301. The unit is Gbps.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.DdosBgpInstance.base_bandwidth">
<code class="sig-name descname">base_bandwidth</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.DdosBgpInstance.base_bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>Base defend bandwidth of the instance. Valid values: 20. The unit is Gbps. Default to <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.DdosBgpInstance.ip_count">
<code class="sig-name descname">ip_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.DdosBgpInstance.ip_count" title="Permalink to this definition">¶</a></dt>
<dd><p>IP count of the instance. Valid values: 100.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.DdosBgpInstance.ip_type">
<code class="sig-name descname">ip_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.DdosBgpInstance.ip_type" title="Permalink to this definition">¶</a></dt>
<dd><p>IP version of the instance. Valid values: IPv4,IPv6.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.DdosBgpInstance.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.DdosBgpInstance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the instance. This name can have a string of 1 to 63 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.DdosBgpInstance.period">
<code class="sig-name descname">period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.DdosBgpInstance.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration that you will buy Ddosbgp instance (in month). Valid values: [1~9], 12, 24, 36. Default to 12. At present, the provider does not support modify “period”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.DdosBgpInstance.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.DdosBgpInstance.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the instance. Valid values: Enterprise,Professional. Default to <code class="docutils literal notranslate"><span class="pre">Enterprise</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ddos.DdosBgpInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">base_bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ddos.DdosBgpInstance.get" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_alicloud.ddos.DdosBgpInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ddos.DdosBgpInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ddos.DdosBgpInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ddos.DdosBgpInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ddos.DdosCooInstance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ddos.</code><code class="sig-name descname">DdosCooInstance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">base_bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ddos.DdosCooInstance" title="Permalink to this definition">¶</a></dt>
<dd><p>BGP-Line Anti-DDoS instance resource. “Ddoscoo” is the short term of this product. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/69319.htm">What is Anti-DDoS Pro</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The product region only support cn-hangzhou.</p>
<p><strong>NOTE:</strong> The endpoint of bssopenapi used only support “business.aliyuncs.com” at present.</p>
<p><strong>NOTE:</strong> Available in 1.37.0+ .</p>
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
<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.DdosCooInstance.bandwidth">
<code class="sig-name descname">bandwidth</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.DdosCooInstance.bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>Elastic defend bandwidth of the instance. This value must be larger than the base defend bandwidth. Valid values: 30, 60, 100, 300, 400, 500, 600. The unit is Gbps. Only support upgrade.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.DdosCooInstance.base_bandwidth">
<code class="sig-name descname">base_bandwidth</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.DdosCooInstance.base_bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>Base defend bandwidth of the instance. Valid values: 30, 60, 100, 300, 400, 500, 600. The unit is Gbps. Only support upgrade.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.DdosCooInstance.domain_count">
<code class="sig-name descname">domain_count</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.DdosCooInstance.domain_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Domain retransmission rule count of the instance. At least 50. Increase 5 per step, such as 55, 60, 65. Only support upgrade.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.DdosCooInstance.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.DdosCooInstance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the instance. This name can have a string of 1 to 63 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.DdosCooInstance.period">
<code class="sig-name descname">period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.DdosCooInstance.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The duration that you will buy Ddoscoo instance (in month). Valid values: [1~9], 12, 24, 36. Default to 1. At present, the provider does not support modify “period”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.DdosCooInstance.port_count">
<code class="sig-name descname">port_count</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.DdosCooInstance.port_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Port retransmission rule count of the instance. At least 50. Increase 5 per step, such as 55, 60, 65. Only support upgrade.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.DdosCooInstance.service_bandwidth">
<code class="sig-name descname">service_bandwidth</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.DdosCooInstance.service_bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>Business bandwidth of the instance. At leaset 100. Increased 100 per step, such as 100, 200, 300. The unit is Mbps. Only support upgrade.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ddos.DdosCooInstance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">base_bandwidth</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">port_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_bandwidth</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ddos.DdosCooInstance.get" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_alicloud.ddos.DdosCooInstance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ddos.DdosCooInstance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ddos.DdosCooInstance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ddos.DdosCooInstance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ddos.GetDdosBgpInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ddos.</code><code class="sig-name descname">GetDdosBgpInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ddos.GetDdosBgpInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDdosBgpInstances.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.GetDdosBgpInstancesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.GetDdosBgpInstancesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.GetDdosBgpInstancesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.GetDdosBgpInstancesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instance IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.GetDdosBgpInstancesResult.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.GetDdosBgpInstancesResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of apis. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.GetDdosBgpInstancesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.GetDdosBgpInstancesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instance names.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ddos.GetDdosCooInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ddos.</code><code class="sig-name descname">GetDdosCooInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ddos.GetDdosCooInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDdosCooInstances.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.GetDdosCooInstancesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.GetDdosCooInstancesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.GetDdosCooInstancesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.GetDdosCooInstancesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instance IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.GetDdosCooInstancesResult.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.GetDdosCooInstancesResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of apis. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ddos.GetDdosCooInstancesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ddos.GetDdosCooInstancesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of instance names.</p>
</dd></dl>

</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ddos.get_ddos_bgp_instances">
<code class="sig-prename descclassname">pulumi_alicloud.ddos.</code><code class="sig-name descname">get_ddos_bgp_instances</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ddos.get_ddos_bgp_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of Anti-DDoS Advanced instances in an Alibaba Cloud account according to the specified filters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.57.0+ .</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of instance IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by the instance name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ddos.get_ddos_coo_instances">
<code class="sig-prename descclassname">pulumi_alicloud.ddos.</code><code class="sig-name descname">get_ddos_coo_instances</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ddos.get_ddos_coo_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of BGP-Line Anti-DDoS Pro instances in an Alibaba Cloud account according to the specified filters.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of instance IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by the instance name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
