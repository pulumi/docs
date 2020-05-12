---
title: Module hbase
title_tag: Module hbase | Package pulumi_alicloud | Python SDK
linktitle: hbase
notitle: true
---

<div class="section" id="hbase">
<h1>hbase<a class="headerlink" href="#hbase" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.hbase"></span><dl class="py class">
<dt id="pulumi_alicloud.hbase.AwaitableGetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.hbase.</code><code class="sig-name descname">AwaitableGetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.hbase.AwaitableGetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.hbase.AwaitableGetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.hbase.</code><code class="sig-name descname">AwaitableGetZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.hbase.AwaitableGetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.hbase.GetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.hbase.</code><code class="sig-name descname">GetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.hbase.GetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstances.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.GetInstancesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.GetInstancesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.GetInstancesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.GetInstancesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The ids list of HBase instances</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.GetInstancesResult.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.GetInstancesResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of HBase instances. Its every element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.GetInstancesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.GetInstancesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>The names list of HBase instances</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.GetInstancesResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.GetInstancesResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.hbase.GetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.hbase.</code><code class="sig-name descname">GetZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.hbase.GetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZones.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.GetZonesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.GetZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.GetZonesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.GetZonesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of zone IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.GetZonesResult.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.GetZonesResult.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of availability zones. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.hbase.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.hbase.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cold_storage_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_disk_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_instance_quantity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deletion_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintain_end_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintain_start_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pay_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.hbase.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a HBase instance resource supports replica set instances only. the HBase provides stable, reliable, and automatic scalable database services. 
It offers a full range of database solutions, such as disaster recovery, backup, recovery, monitoring, and alarms.
You can see detail product introduction <a class="reference external" href="https://help.aliyun.com/product/49055.html">here</a></p>
<blockquote>
<div><p><strong>NOTE:</strong>  Available in 1.67.0+</p>
<p><strong>NOTE:</strong>  The following regions don’t support create Classic network HBase instance.
[<code class="docutils literal notranslate"><span class="pre">cn-hangzhou</span></code>,<code class="docutils literal notranslate"><span class="pre">cn-shanghai</span></code>,<code class="docutils literal notranslate"><span class="pre">cn-qingdao</span></code>,<code class="docutils literal notranslate"><span class="pre">cn-beijing</span></code>,<code class="docutils literal notranslate"><span class="pre">cn-shenzhen</span></code>,<code class="docutils literal notranslate"><span class="pre">ap-southeast-1a</span></code>,…..]
the official website mark  more regions. or you can call <a class="reference external" href="https://help.aliyun.com/document_detail/144489.html">DescribeRegions</a></p>
<p><strong>NOTE:</strong>  Create HBase instance or change instance type and storage would cost 15 minutes. Please make full preparation</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">hbase</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;default&quot;</span><span class="p">,</span>
    <span class="n">cold_storage_size</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="n">core_disk_size</span><span class="o">=</span><span class="mi">400</span><span class="p">,</span>
    <span class="n">core_disk_type</span><span class="o">=</span><span class="s2">&quot;cloud_efficiency&quot;</span><span class="p">,</span>
    <span class="n">core_instance_quantity</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">core_instance_type</span><span class="o">=</span><span class="s2">&quot;hbase.sn1.large&quot;</span><span class="p">,</span>
    <span class="n">engine_version</span><span class="o">=</span><span class="s2">&quot;2.0&quot;</span><span class="p">,</span>
    <span class="n">master_instance_type</span><span class="o">=</span><span class="s2">&quot;hbase.sn1.large&quot;</span><span class="p">,</span>
    <span class="n">pay_type</span><span class="o">=</span><span class="s2">&quot;PostPaid&quot;</span><span class="p">,</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="s2">&quot;cn-shenzhen-b&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">true</span></code>, <code class="docutils literal notranslate"><span class="pre">false</span></code>, System default to <code class="docutils literal notranslate"><span class="pre">false</span></code>, valid when pay_type = PrePaid.</p></li>
<li><p><strong>cold_storage_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – 0 or 0+. 0 means is_cold_storage = false. 0+ means is_cold_storage = true</p></li>
<li><p><strong>core_disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – User-defined HBase instance one core node’s storage space.Unit: GB. Value range:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Custom</span> <span class="n">storage</span> <span class="n">space</span><span class="p">;</span> <span class="n">value</span> <span class="nb">range</span><span class="p">:</span> <span class="p">[</span><span class="mi">400</span><span class="p">,</span> <span class="mi">8000</span><span class="p">]</span>
<span class="o">-</span> <span class="mi">40</span><span class="o">-</span><span class="n">GB</span> <span class="n">increments</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>core_disk_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>, <code class="docutils literal notranslate"><span class="pre">local_hdd_pro</span></code>, <code class="docutils literal notranslate"><span class="pre">local_ssd_pro</span></code>. local_disk size is fixed.</p></li>
<li><p><strong>core_instance_quantity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – default=2. if core_instance_quantity &gt; 1,this is cluster’s instance.  if core_instance_quantity = 1,this is a single instance.</p></li>
<li><p><strong>deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – the switch of delete protection. true: delete protect, false: no delete protect. you must set false when you want to delete cluster.</p></li>
<li><p><strong>duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 60, valid when pay_type = PrePaid. unit: month.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – hbase major version. hbase:1.1/2.0, hbaseue:2.0, bds:1.0, unsupport other engine temporarily. Value options can refer to the latest docs <a class="reference external" href="https://help.aliyun.com/document_detail/144607.html">CreateInstance</a>.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `master_instance_type`、`core_instance_type` - (Required, ForceNew) Instance specification. see [Instance specifications](https://help.aliyun.com/document_detail/53532.html). or you can call describeInstanceType api.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>maintain_end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The end time of the operation and maintenance time period of the instance, in the format of HH:mmZ (UTC time).</p></li>
<li><p><strong>maintain_start*time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The start time of the operation and maintenance time period of the instance, in the format of HH:mmZ (UTC time).</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – HBase instance name. Length must be 2-128 characters long. Only Chinese characters, English letters, numbers, period (.), underline (<a href="#id3"><span class="problematic" id="id4">*</span></a>), or dash (-) are permitted.</p></li>
<li><p><strong>pay_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>,System default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – if vswitch_id is not empty, that mean net_type = vpc and has a same region. if vswitch_id is empty, net_type_classic</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the HBase instance. if vswitch_id is not empty, this zone_id can be “” or consistent.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.Instance.auto_renew">
<code class="sig-name descname">auto_renew</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.Instance.auto_renew" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">true</span></code>, <code class="docutils literal notranslate"><span class="pre">false</span></code>, System default to <code class="docutils literal notranslate"><span class="pre">false</span></code>, valid when pay_type = PrePaid.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.Instance.cold_storage_size">
<code class="sig-name descname">cold_storage_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.Instance.cold_storage_size" title="Permalink to this definition">¶</a></dt>
<dd><p>0 or 0+. 0 means is_cold_storage = false. 0+ means is_cold_storage = true</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.Instance.core_disk_size">
<code class="sig-name descname">core_disk_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.Instance.core_disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined HBase instance one core node’s storage space.Unit: GB. Value range:</p>
<ul class="simple">
<li><p>Custom storage space; value range: [400, 8000]</p></li>
<li><p>40-GB increments.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.Instance.core_disk_type">
<code class="sig-name descname">core_disk_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.Instance.core_disk_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid values are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>, <code class="docutils literal notranslate"><span class="pre">local_hdd_pro</span></code>, <code class="docutils literal notranslate"><span class="pre">local_ssd_pro</span></code>. local_disk size is fixed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.Instance.core_instance_quantity">
<code class="sig-name descname">core_instance_quantity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.Instance.core_instance_quantity" title="Permalink to this definition">¶</a></dt>
<dd><p>default=2. if core_instance_quantity &gt; 1,this is cluster’s instance.  if core_instance_quantity = 1,this is a single instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.Instance.deletion_protection">
<code class="sig-name descname">deletion_protection</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.Instance.deletion_protection" title="Permalink to this definition">¶</a></dt>
<dd><p>the switch of delete protection. true: delete protect, false: no delete protect. you must set false when you want to delete cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.Instance.duration">
<code class="sig-name descname">duration</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.Instance.duration" title="Permalink to this definition">¶</a></dt>
<dd><p>1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 60, valid when pay_type = PrePaid. unit: month.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.Instance.engine_version">
<code class="sig-name descname">engine_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.Instance.engine_version" title="Permalink to this definition">¶</a></dt>
<dd><p>hbase major version. hbase:1.1/2.0, hbaseue:2.0, bds:1.0, unsupport other engine temporarily. Value options can refer to the latest docs <a class="reference external" href="https://help.aliyun.com/document_detail/144607.html">CreateInstance</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">master_instance_type</span></code>、<code class="docutils literal notranslate"><span class="pre">core_instance_type</span></code> - (Required, ForceNew) Instance specification. see <a class="reference external" href="https://help.aliyun.com/document_detail/53532.html">Instance specifications</a>. or you can call describeInstanceType api.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.Instance.maintain_end_time">
<code class="sig-name descname">maintain_end_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.Instance.maintain_end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The end time of the operation and maintenance time period of the instance, in the format of HH:mmZ (UTC time).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.Instance.maintain_start_time">
<code class="sig-name descname">maintain_start_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.Instance.maintain_start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The start time of the operation and maintenance time period of the instance, in the format of HH:mmZ (UTC time).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.Instance.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>HBase instance name. Length must be 2-128 characters long. Only Chinese characters, English letters, numbers, period (.), underline (_), or dash (-) are permitted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.Instance.pay_type">
<code class="sig-name descname">pay_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.Instance.pay_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>,System default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.Instance.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.Instance.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.Instance.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>if vswitch_id is not empty, that mean net_type = vpc and has a same region. if vswitch_id is empty, net_type_classic</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.hbase.Instance.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.hbase.Instance.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Zone to launch the HBase instance. if vswitch_id is not empty, this zone_id can be “” or consistent.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.hbase.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cold_storage_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_disk_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_instance_quantity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">core_instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deletion_protection</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">engine_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintain_end_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintain_start_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pay_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.hbase.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <code class="docutils literal notranslate"><span class="pre">true</span></code>, <code class="docutils literal notranslate"><span class="pre">false</span></code>, System default to <code class="docutils literal notranslate"><span class="pre">false</span></code>, valid when pay_type = PrePaid.</p></li>
<li><p><strong>cold_storage_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – 0 or 0+. 0 means is_cold_storage = false. 0+ means is_cold_storage = true</p></li>
<li><p><strong>core_disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – User-defined HBase instance one core node’s storage space.Unit: GB. Value range:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Custom</span> <span class="n">storage</span> <span class="n">space</span><span class="p">;</span> <span class="n">value</span> <span class="nb">range</span><span class="p">:</span> <span class="p">[</span><span class="mi">400</span><span class="p">,</span> <span class="mi">8000</span><span class="p">]</span>
<span class="o">-</span> <span class="mi">40</span><span class="o">-</span><span class="n">GB</span> <span class="n">increments</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>core_disk_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>, <code class="docutils literal notranslate"><span class="pre">local_hdd_pro</span></code>, <code class="docutils literal notranslate"><span class="pre">local_ssd_pro</span></code>. local_disk size is fixed.</p></li>
<li><p><strong>core_instance_quantity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – default=2. if core_instance_quantity &gt; 1,this is cluster’s instance.  if core_instance_quantity = 1,this is a single instance.</p></li>
<li><p><strong>deletion_protection</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – the switch of delete protection. true: delete protect, false: no delete protect. you must set false when you want to delete cluster.</p></li>
<li><p><strong>duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 60, valid when pay_type = PrePaid. unit: month.</p></li>
<li><p><strong>engine_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>hbase major version. hbase:1.1/2.0, hbaseue:2.0, bds:1.0, unsupport other engine temporarily. Value options can refer to the latest docs <a class="reference external" href="https://help.aliyun.com/document_detail/144607.html">CreateInstance</a>.</p>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `master_instance_type`、`core_instance_type` - (Required, ForceNew) Instance specification. see [Instance specifications](https://help.aliyun.com/document_detail/53532.html). or you can call describeInstanceType api.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>maintain_end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The end time of the operation and maintenance time period of the instance, in the format of HH:mmZ (UTC time).</p></li>
<li><p><strong>maintain_start*time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The start time of the operation and maintenance time period of the instance, in the format of HH:mmZ (UTC time).</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – HBase instance name. Length must be 2-128 characters long. Only Chinese characters, English letters, numbers, period (.), underline (<a href="#id9"><span class="problematic" id="id10">*</span></a>), or dash (-) are permitted.</p></li>
<li><p><strong>pay_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>,System default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – if vswitch_id is not empty, that mean net_type = vpc and has a same region. if vswitch_id is empty, net_type_classic</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the HBase instance. if vswitch_id is not empty, this zone_id can be “” or consistent.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.hbase.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.hbase.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.hbase.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.hbase.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.hbase.get_instances">
<code class="sig-prename descclassname">pulumi_alicloud.hbase.</code><code class="sig-name descname">get_instances</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">availability_zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.hbase.get_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">hbase.getInstances</span></code> data source provides a collection of HBase instances available in Alicloud account.
Filters support regular expression for the instance name, ids or availability_zone.</p>
<blockquote>
<div><p><strong>NOTE:</strong>  Available in 1.67.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">hbase</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">hbase</span><span class="o">.</span><span class="n">get_instances</span><span class="p">(</span><span class="n">availability_zone</span><span class="o">=</span><span class="s2">&quot;cn-shenzhen-b&quot;</span><span class="p">,</span>
    <span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;tf_testAccHBase&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>availability_zone</strong> (<em>str</em>) – Instance availability zone.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – The ids list of HBase instances</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to apply to the instance name.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.hbase.get_zones">
<code class="sig-prename descclassname">pulumi_alicloud.hbase.</code><code class="sig-name descname">get_zones</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">multi</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.hbase.get_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides availability zones for HBase that can be accessed by an Alibaba Cloud account within the region configured in the provider.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.73.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">zones_ids</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">hbase</span><span class="o">.</span><span class="n">get_zones</span><span class="p">()</span>
<span class="c1"># Create an HBase instance with the first matched zone</span>
<span class="n">hbase</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">hbase</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;hbase&quot;</span><span class="p">,</span> <span class="n">zone_id</span><span class="o">=</span><span class="n">zones_ids</span><span class="o">.</span><span class="n">zones</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
<span class="c1"># Other properties...</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>multi</strong> (<em>bool</em>) – Indicate whether the zones can be used in a multi AZ configuration. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Multi AZ is usually used to launch HBase instances.</p>
</dd>
</dl>
</dd></dl>

</div>
