---
title: Module cen
title_tag: Module cen | Package pulumi_alicloud | Python SDK
linktitle: cen
notitle: true
---

<div class="section" id="cen">
<h1>cen<a class="headerlink" href="#cen" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.cen"></span><dl class="class">
<dt id="pulumi_alicloud.cen.AwaitableGetBandwidthLimitsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">AwaitableGetBandwidthLimitsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">instance_ids=None</em>, <em class="sig-param">limits=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.AwaitableGetBandwidthLimitsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.cen.AwaitableGetBandwidthPackagesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">AwaitableGetBandwidthPackagesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">packages=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.AwaitableGetBandwidthPackagesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.cen.AwaitableGetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">AwaitableGetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.AwaitableGetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.cen.AwaitableGetRegionRouteEntriesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">AwaitableGetRegionRouteEntriesResult</code><span class="sig-paren">(</span><em class="sig-param">entries=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">region_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.AwaitableGetRegionRouteEntriesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.cen.AwaitableGetRouteEntriesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">AwaitableGetRouteEntriesResult</code><span class="sig-paren">(</span><em class="sig-param">cidr_block=None</em>, <em class="sig-param">entries=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">route_table_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.AwaitableGetRouteEntriesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.cen.BandwidthLimit">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">BandwidthLimit</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bandwidth_limit=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">region_ids=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthLimit" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CEN cross-regional interconnection bandwidth resource. To connect networks in different regions, you must set cross-region interconnection bandwidth after buying a bandwidth package. The total bandwidth set for all the interconnected regions of a bandwidth package cannot exceed the bandwidth of the bandwidth package. By default, 1 Kbps bandwidth is provided for connectivity test. To run normal business, you must buy a bandwidth package and set a proper interconnection bandwidth.</p>
<p>For example, a CEN instance is bound to a bandwidth package of 20 Mbps and  the interconnection areas are Mainland China and North America. You can set the cross-region interconnection bandwidth between US West 1 and China East 1, China East 2, China South 1, and so on. However, the total bandwidth set for all the interconnected regions cannot exceed 20  Mbps.</p>
<p>For information about CEN and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/65983.htm">Cross-region interconnection bandwidth</a></p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cen_bandwidth_limit.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cen_bandwidth_limit.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bandwidth_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The bandwidth configured for the interconnected regions communication.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the CEN.</p></li>
<li><p><strong>region_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of the two regions to interconnect. Must be two different regions.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.cen.BandwidthLimit.bandwidth_limit">
<code class="sig-name descname">bandwidth_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthLimit.bandwidth_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The bandwidth configured for the interconnected regions communication.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.BandwidthLimit.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthLimit.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the CEN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.BandwidthLimit.region_ids">
<code class="sig-name descname">region_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthLimit.region_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of the two regions to interconnect. Must be two different regions.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cen.BandwidthLimit.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bandwidth_limit=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">region_ids=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthLimit.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BandwidthLimit resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bandwidth_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The bandwidth configured for the interconnected regions communication.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the CEN.</p></li>
<li><p><strong>region_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of the two regions to interconnect. Must be two different regions.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cen.BandwidthLimit.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthLimit.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cen.BandwidthLimit.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthLimit.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cen.BandwidthPackage">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">BandwidthPackage</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bandwidth=None</em>, <em class="sig-param">charge_type=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">geographic_region_ids=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthPackage" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CEN bandwidth package resource. The CEN bandwidth package is an abstracted object that includes an interconnection bandwidth and interconnection areas. To buy a bandwidth package, you must specify the areas to connect. An area consists of one or more Alibaba Cloud regions. The areas in CEN include Mainland China, Asia Pacific, North America, and Europe.</p>
<p>For information about CEN and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/65982.htm">Manage bandwidth packages</a>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cen_bandwidth_package.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cen_bandwidth_package.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The bandwidth in Mbps of the bandwidth package. Cannot be less than 2Mbps.</p></li>
<li><p><strong>charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing method. Valid value: PostPaid | PrePaid. Default to PostPaid. If set to PrePaid, the bandwidth package can’t be deleted before expired time.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the bandwidth package. Default to null.</p></li>
<li><p><strong>geographic_region_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of the two areas to connect. Valid value: China | North-America | Asia-Pacific | Europe | Middle-East.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bandwidth package. Defaults to null.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The purchase period in month. Valid value: 1, 2, 3, 6, 12. Default to 1.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.cen.BandwidthPackage.bandwidth">
<code class="sig-name descname">bandwidth</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthPackage.bandwidth" title="Permalink to this definition">¶</a></dt>
<dd><p>The bandwidth in Mbps of the bandwidth package. Cannot be less than 2Mbps.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.BandwidthPackage.charge_type">
<code class="sig-name descname">charge_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthPackage.charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The billing method. Valid value: PostPaid | PrePaid. Default to PostPaid. If set to PrePaid, the bandwidth package can’t be deleted before expired time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.BandwidthPackage.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthPackage.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the bandwidth package. Default to null.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.BandwidthPackage.expired_time">
<code class="sig-name descname">expired_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthPackage.expired_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time of the bandwidth package to expire.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.BandwidthPackage.geographic_region_ids">
<code class="sig-name descname">geographic_region_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthPackage.geographic_region_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of the two areas to connect. Valid value: China | North-America | Asia-Pacific | Europe | Middle-East.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.BandwidthPackage.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthPackage.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the bandwidth package. Defaults to null.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.BandwidthPackage.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthPackage.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The purchase period in month. Valid value: 1, 2, 3, 6, 12. Default to 1.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.BandwidthPackage.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthPackage.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of the bandwidth, including “InUse” and “Idle”.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cen.BandwidthPackage.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bandwidth=None</em>, <em class="sig-param">charge_type=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">expired_time=None</em>, <em class="sig-param">geographic_region_ids=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthPackage.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BandwidthPackage resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bandwidth</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The bandwidth in Mbps of the bandwidth package. Cannot be less than 2Mbps.</p></li>
<li><p><strong>charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The billing method. Valid value: PostPaid | PrePaid. Default to PostPaid. If set to PrePaid, the bandwidth package can’t be deleted before expired time.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the bandwidth package. Default to null.</p></li>
<li><p><strong>expired_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time of the bandwidth package to expire.</p></li>
<li><p><strong>geographic_region_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of the two areas to connect. Valid value: China | North-America | Asia-Pacific | Europe | Middle-East.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the bandwidth package. Defaults to null.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The purchase period in month. Valid value: 1, 2, 3, 6, 12. Default to 1.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of the bandwidth, including “InUse” and “Idle”.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cen.BandwidthPackage.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthPackage.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cen.BandwidthPackage.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthPackage.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cen.BandwidthPackageAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">BandwidthPackageAttachment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bandwidth_package_id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthPackageAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CEN bandwidth package attachment resource. The resource can be used to bind a bandwidth package to a specified CEN instance.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cen_bandwidth_package_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cen_bandwidth_package_attachment.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bandwidth_package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the bandwidth package.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the CEN.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.cen.BandwidthPackageAttachment.bandwidth_package_id">
<code class="sig-name descname">bandwidth_package_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthPackageAttachment.bandwidth_package_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the bandwidth package.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.BandwidthPackageAttachment.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthPackageAttachment.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the CEN.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cen.BandwidthPackageAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bandwidth_package_id=None</em>, <em class="sig-param">instance_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthPackageAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BandwidthPackageAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bandwidth_package_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the bandwidth package.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the CEN.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cen.BandwidthPackageAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthPackageAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cen.BandwidthPackageAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.BandwidthPackageAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cen.FlowLog">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">FlowLog</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cen_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">flow_log_name=None</em>, <em class="sig-param">log_store_name=None</em>, <em class="sig-param">project_name=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.FlowLog" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource used to create a flow log function in Cloud Enterprise Network (CEN). 
By using the flow log function, you can capture the traffic data of the network instances in different regions of a CEN. 
You can also use the data aggregated in flow logs to analyze cross-region traffic flows, minimize traffic costs, and troubleshoot network faults.</p>
<p>For information about CEN flow log and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/123006.htm">Manage CEN flowlog</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.73.0+</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cen_flowlog.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cen_flowlog.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cen_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the CEN Instance.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of flowlog.</p></li>
<li><p><strong>flow_log_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of flowlog.</p></li>
<li><p><strong>log_store_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the log store which is in the  <code class="docutils literal notranslate"><span class="pre">project_name</span></code> SLS project.</p></li>
<li><p><strong>project_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SLS project.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of flowlog. Valid values: [“Active”, “Inactive”]. Default to “Active”.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.cen.FlowLog.cen_id">
<code class="sig-name descname">cen_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.FlowLog.cen_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the CEN Instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.FlowLog.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.FlowLog.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of flowlog.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.FlowLog.flow_log_name">
<code class="sig-name descname">flow_log_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.FlowLog.flow_log_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of flowlog.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.FlowLog.log_store_name">
<code class="sig-name descname">log_store_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.FlowLog.log_store_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the log store which is in the  <code class="docutils literal notranslate"><span class="pre">project_name</span></code> SLS project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.FlowLog.project_name">
<code class="sig-name descname">project_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.FlowLog.project_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the SLS project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.FlowLog.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.FlowLog.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The status of flowlog. Valid values: [“Active”, “Inactive”]. Default to “Active”.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cen.FlowLog.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cen_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">flow_log_name=None</em>, <em class="sig-param">log_store_name=None</em>, <em class="sig-param">project_name=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.FlowLog.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FlowLog resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cen_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the CEN Instance.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of flowlog.</p></li>
<li><p><strong>flow_log_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of flowlog.</p></li>
<li><p><strong>log_store_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the log store which is in the  <code class="docutils literal notranslate"><span class="pre">project_name</span></code> SLS project.</p></li>
<li><p><strong>project_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the SLS project.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The status of flowlog. Valid values: [“Active”, “Inactive”]. Default to “Active”.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cen.FlowLog.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.FlowLog.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cen.FlowLog.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.FlowLog.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cen.GetBandwidthLimitsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">GetBandwidthLimitsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">instance_ids=None</em>, <em class="sig-param">limits=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.GetBandwidthLimitsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBandwidthLimits.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.cen.GetBandwidthLimitsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.GetBandwidthLimitsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.GetBandwidthLimitsResult.limits">
<code class="sig-name descname">limits</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.GetBandwidthLimitsResult.limits" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of CEN Bandwidth Limits. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.cen.GetBandwidthPackagesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">GetBandwidthPackagesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">packages=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.GetBandwidthPackagesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBandwidthPackages.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.cen.GetBandwidthPackagesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.GetBandwidthPackagesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.GetBandwidthPackagesResult.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.GetBandwidthPackagesResult.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of CEN instance that owns the CEN Bandwidth Package.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.GetBandwidthPackagesResult.packages">
<code class="sig-name descname">packages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.GetBandwidthPackagesResult.packages" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of CEN bandwidth package. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.cen.GetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">GetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">ids=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.GetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstances.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.cen.GetInstancesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.GetInstancesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.GetInstancesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.GetInstancesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of CEN instances IDs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.GetInstancesResult.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.GetInstancesResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of CEN instances. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.GetInstancesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.GetInstancesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of CEN instances names.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.cen.GetRegionRouteEntriesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">GetRegionRouteEntriesResult</code><span class="sig-paren">(</span><em class="sig-param">entries=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">region_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.GetRegionRouteEntriesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegionRouteEntries.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.cen.GetRegionRouteEntriesResult.entries">
<code class="sig-name descname">entries</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.GetRegionRouteEntriesResult.entries" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of CEN Route Entries. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.GetRegionRouteEntriesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.GetRegionRouteEntriesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.cen.GetRouteEntriesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">GetRouteEntriesResult</code><span class="sig-paren">(</span><em class="sig-param">cidr_block=None</em>, <em class="sig-param">entries=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">route_table_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.GetRouteEntriesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRouteEntries.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.cen.GetRouteEntriesResult.cidr_block">
<code class="sig-name descname">cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.GetRouteEntriesResult.cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination CIDR block of the conflicted route entry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.GetRouteEntriesResult.entries">
<code class="sig-name descname">entries</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.GetRouteEntriesResult.entries" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of CEN Route Entries. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.GetRouteEntriesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.GetRouteEntriesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.GetRouteEntriesResult.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.GetRouteEntriesResult.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the CEN child instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.GetRouteEntriesResult.route_table_id">
<code class="sig-name descname">route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.GetRouteEntriesResult.route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the route table.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.cen.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CEN instance resource. Cloud Enterprise Network (CEN) is a service that allows you to create a global network for rapidly building a distributed business system with a hybrid cloud computing solution. CEN enables you to build a secure, private, and enterprise-class interconnected network between VPCs in different regions and your local data centers. CEN provides enterprise-class scalability that automatically responds to your dynamic computing requirements.</p>
<p>For information about CEN and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/59870.htm">What is Cloud Enterprise Network</a>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cen_instance.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cen_instance.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource*name</strong> (<em>str</em>) – <p>The name of the resource.</p>
</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the CEN instance. Defaults to null. The description must be 2 to 256 characters in length. It must start with a letter, and cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the CEN instance. Defaults to null. The name must be 2 to 128 characters in length and can contain letters, numbers, periods (.), underscores (<a href="#id3"><span class="problematic" id="id4">*</span></a>), and hyphens (-). The name must start with a letter, but cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.cen.Instance.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.Instance.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the CEN instance. Defaults to null. The description must be 2 to 256 characters in length. It must start with a letter, and cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.Instance.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the CEN instance. Defaults to null. The name must be 2 to 128 characters in length and can contain letters, numbers, periods (.), underscores (_), and hyphens (-). The name must start with a letter, but cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cen.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource*name</strong> (<em>str</em>) – <p>The unique name of the resulting resource.</p>
</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the CEN instance. Defaults to null. The description must be 2 to 256 characters in length. It must start with a letter, and cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the CEN instance. Defaults to null. The name must be 2 to 128 characters in length and can contain letters, numbers, periods (.), underscores (<a href="#id7"><span class="problematic" id="id8">*</span></a>), and hyphens (-). The name must start with a letter, but cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cen.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cen.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cen.InstanceAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">InstanceAttachment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">child_instance_id=None</em>, <em class="sig-param">child_instance_owner_id=None</em>, <em class="sig-param">child_instance_region_id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.InstanceAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CEN child instance attachment resource.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cen_instance_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cen_instance_attachment.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>child_instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the child instance to attach.</p></li>
<li><p><strong>child_instance_owner_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The uid of the child instance. Only used when attach a child instance of other account.</p></li>
<li><p><strong>child_instance_region_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region ID of the child instance to attach.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the CEN.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.cen.InstanceAttachment.child_instance_id">
<code class="sig-name descname">child_instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.InstanceAttachment.child_instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the child instance to attach.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.InstanceAttachment.child_instance_owner_id">
<code class="sig-name descname">child_instance_owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.InstanceAttachment.child_instance_owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The uid of the child instance. Only used when attach a child instance of other account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.InstanceAttachment.child_instance_region_id">
<code class="sig-name descname">child_instance_region_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.InstanceAttachment.child_instance_region_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The region ID of the child instance to attach.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.InstanceAttachment.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.InstanceAttachment.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the CEN.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cen.InstanceAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">child_instance_id=None</em>, <em class="sig-param">child_instance_owner_id=None</em>, <em class="sig-param">child_instance_region_id=None</em>, <em class="sig-param">instance_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.InstanceAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InstanceAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>child_instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the child instance to attach.</p></li>
<li><p><strong>child_instance_owner_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The uid of the child instance. Only used when attach a child instance of other account.</p></li>
<li><p><strong>child_instance_region_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region ID of the child instance to attach.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the CEN.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cen.InstanceAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.InstanceAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cen.InstanceAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.InstanceAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cen.InstanceGrant">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">InstanceGrant</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cen_id=None</em>, <em class="sig-param">cen_owner_id=None</em>, <em class="sig-param">child_instance_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.InstanceGrant" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CEN child instance grant resource, which allow you to authorize a VPC or VBR to a CEN of a different account.</p>
<p>For more information about how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/73645.htm">Attach a network in a different account</a>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cen_instance_grant.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cen_instance_grant.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cen_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the CEN.</p></li>
<li><p><strong>cen_owner_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner UID of the  CEN which the child instance granted to.</p></li>
<li><p><strong>child_instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the child instance to grant.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.cen.InstanceGrant.cen_id">
<code class="sig-name descname">cen_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.InstanceGrant.cen_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the CEN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.InstanceGrant.cen_owner_id">
<code class="sig-name descname">cen_owner_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.InstanceGrant.cen_owner_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The owner UID of the  CEN which the child instance granted to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.InstanceGrant.child_instance_id">
<code class="sig-name descname">child_instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.InstanceGrant.child_instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the child instance to grant.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cen.InstanceGrant.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cen_id=None</em>, <em class="sig-param">cen_owner_id=None</em>, <em class="sig-param">child_instance_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.InstanceGrant.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InstanceGrant resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cen_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the CEN.</p></li>
<li><p><strong>cen_owner_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The owner UID of the  CEN which the child instance granted to.</p></li>
<li><p><strong>child_instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the child instance to grant.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cen.InstanceGrant.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.InstanceGrant.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cen.InstanceGrant.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.InstanceGrant.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cen.RouteEntry">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">RouteEntry</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cidr_block=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">route_table_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.RouteEntry" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CEN route entry resource. Cloud Enterprise Network (CEN) supports publishing and withdrawing route entries of attached networks. You can publish a route entry of an attached VPC or VBR to a CEN instance, then other attached networks can learn the route if there is no route conflict. You can withdraw a published route entry when CEN does not need it any more.</p>
<p>For information about CEN route entries publishment and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/86980.htm">Manage network routes</a>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cen_route_entry.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cen_route_entry.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination CIDR block of the route entry to publish.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the CEN.</p></li>
<li><p><strong>route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The route table of the attached VBR or VPC.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.cen.RouteEntry.cidr_block">
<code class="sig-name descname">cidr_block</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.RouteEntry.cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>The destination CIDR block of the route entry to publish.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.RouteEntry.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.RouteEntry.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the CEN.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cen.RouteEntry.route_table_id">
<code class="sig-name descname">route_table_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cen.RouteEntry.route_table_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The route table of the attached VBR or VPC.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cen.RouteEntry.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cidr_block=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">route_table_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.RouteEntry.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RouteEntry resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The destination CIDR block of the route entry to publish.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the CEN.</p></li>
<li><p><strong>route_table_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The route table of the attached VBR or VPC.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cen.RouteEntry.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.RouteEntry.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cen.RouteEntry.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.RouteEntry.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cen.get_bandwidth_limits">
<code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">get_bandwidth_limits</code><span class="sig-paren">(</span><em class="sig-param">instance_ids=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.get_bandwidth_limits" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides CEN Bandwidth Limits available to the user.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/cen_bandwidth_limits.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/cen_bandwidth_limits.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>instance_ids</strong> (<em>list</em>) – A list of CEN instances IDs.</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.cen.get_bandwidth_packages">
<code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">get_bandwidth_packages</code><span class="sig-paren">(</span><em class="sig-param">ids=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.get_bandwidth_packages" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides CEN Bandwidth Packages available to the user.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/cen_bandwidth_packages.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/cen_bandwidth_packages.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – Limit search to a list of specific CEN Bandwidth Package IDs.</p></li>
<li><p><strong>instance_id</strong> (<em>str</em>) – ID of a CEN instance.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter CEN Bandwidth Package by name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.cen.get_instances">
<code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">get_instances</code><span class="sig-paren">(</span><em class="sig-param">ids=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.get_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides CEN instances available to the user.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/cen_instances.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/cen_instances.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of CEN instances IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter CEN instances by name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.cen.get_region_route_entries">
<code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">get_region_route_entries</code><span class="sig-paren">(</span><em class="sig-param">instance_id=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">region_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.get_region_route_entries" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides CEN Regional Route Entries available to the user.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/cen_region_route_entries.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/cen_region_route_entries.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>instance_id</strong> (<em>str</em>) – ID of the CEN instance.</p></li>
<li><p><strong>region_id</strong> (<em>str</em>) – ID of the region.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.cen.get_route_entries">
<code class="sig-prename descclassname">pulumi_alicloud.cen.</code><code class="sig-name descname">get_route_entries</code><span class="sig-paren">(</span><em class="sig-param">cidr_block=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">route_table_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cen.get_route_entries" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides CEN Route Entries available to the user.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/cen_route_entries.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/cen_route_entries.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cidr_block</strong> (<em>str</em>) – The destination CIDR block of the route entry to query.</p></li>
<li><p><strong>instance_id</strong> (<em>str</em>) – ID of the CEN instance.</p></li>
<li><p><strong>route_table_id</strong> (<em>str</em>) – ID of the route table of the VPC or VBR.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
