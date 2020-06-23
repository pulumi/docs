---
title: Module cassandra
title_tag: Module cassandra | Package pulumi_alicloud | Python SDK
linktitle: cassandra
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "alicloud" >}}

<div class="section" id="cassandra">
<h1>cassandra<a class="headerlink" href="#cassandra" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.cassandra"></span><dl class="py class">
<dt id="pulumi_alicloud.cassandra.AwaitableGetClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cassandra.</code><code class="sig-name descname">AwaitableGetClustersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">clusters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cassandra.AwaitableGetClustersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cassandra.AwaitableGetDataCentersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cassandra.</code><code class="sig-name descname">AwaitableGetDataCentersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">centers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cassandra.AwaitableGetDataCentersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cassandra.AwaitableGetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cassandra.</code><code class="sig-name descname">AwaitableGetZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cassandra.AwaitableGetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cassandra.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cassandra.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_center_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_white</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintain_end_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintain_start_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">major_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pay_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cassandra cluster resource supports replica set clusters only. The Cassandra provides stable, reliable, and automatic scalable database services. 
It offers a full range of database solutions, such as disaster recovery, backup, recovery, monitoring, and alarms.
You can see detail product introduction <a class="reference external" href="https://www.alibabacloud.com/help/product/49055.htm">here</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong>  Available in 1.88.0+.</p>
<p><strong>NOTE:</strong>  The following regions support create Vpc network Cassandra cluster.
The official website mark more regions. Or you can call <a class="reference external" href="https://help.aliyun.com/document_detail/157540.html">DescribeRegions</a>.</p>
<p><strong>NOTE:</strong>  Create Cassandra cluster or change cluster type and storage would cost 30 minutes. Please make full preparation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Auto renew of dataCenter-1,<code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. System default to <code class="docutils literal notranslate"><span class="pre">false</span></code>, valid when pay_type = PrePaid.</p></li>
<li><p><strong>auto_renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Period of dataCenter-1 auto renew, if auto renew is <code class="docutils literal notranslate"><span class="pre">true</span></code>, one of <code class="docutils literal notranslate"><span class="pre">1,</span> <span class="pre">2,</span> <span class="pre">3,</span> <span class="pre">4,</span> <span class="pre">5,</span> <span class="pre">6,</span> <span class="pre">7,</span> <span class="pre">8,</span> <span class="pre">9,</span> <span class="pre">12,</span> <span class="pre">24,</span> <span class="pre">36,</span> <span class="pre">60</span></code>, valid when pay_type = Subscription. Unit: month.</p></li>
<li><p><strong>cluster*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Cassandra cluster name. Length must be 2~128 characters long. Only Chinese characters, English letters, numbers, period <code class="docutils literal notranslate"><span class="pre">.</span></code>, underline <cite>*`</cite>, or dash``-<a href="#id3"><span class="problematic" id="id4">``</span></a>are permitted.</p>
</p></li>
<li><p><strong>data_center_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cassandra dataCenter-1 name. Length must be 2~128 characters long. Only Chinese characters, English letters, numbers, period``.`, underline <cite>_`</cite>, or dash``-` are permitted.</p></li>
<li><p><strong>disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – User-defined Cassandra dataCenter-1 one node’s storage space.Unit: GB. Value range:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Custom</span> <span class="n">storage</span> <span class="n">space</span><span class="p">;</span> <span class="n">value</span> <span class="nb">range</span><span class="p">:</span> <span class="p">[</span><span class="mi">160</span><span class="p">,</span> <span class="mi">2000</span><span class="p">]</span><span class="o">.</span>
<span class="o">-</span> <span class="mi">80</span><span class="o">-</span><span class="n">GB</span> <span class="n">increments</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>disk_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The disk type of Cassandra dataCenter-1. Valid values are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>, <code class="docutils literal notranslate"><span class="pre">local_hdd_pro</span></code>, <code class="docutils literal notranslate"><span class="pre">local_ssd_pro</span></code>, local_disk size is fixed.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance specification. See <a class="reference external" href="https://help.aliyun.com/document_detail/157445.html">Instance specifications</a>. Or you can call describeInstanceType api.</p></li>
<li><p><strong>ip_white</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set the instance’s IP whitelist in VPC network.</p></li>
<li><p><strong>maintain_end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The end time of the operation and maintenance time period of the cluster, in the format of HH:mmZ (UTC time).</p></li>
<li><p><strong>maintain_start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The start time of the operation and maintenance time period of the cluster, in the format of HH:mmZ (UTC time).</p></li>
<li><p><strong>major_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cassandra major version. Now only support version <code class="docutils literal notranslate"><span class="pre">3.11</span></code>.</p></li>
<li><p><strong>node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The node count of Cassandra dataCenter-1 default to 2.</p></li>
<li><p><strong>pay_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pay type of Cassandra dataCenter-1. Valid values are <code class="docutils literal notranslate"><span class="pre">Subscription</span></code>, <code class="docutils literal notranslate"><span class="pre">PayAsYouGo</span></code>,System default to <code class="docutils literal notranslate"><span class="pre">PayAsYouGo</span></code>.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security group ids to associate with.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vswitch_id of dataCenter-1, can not empty.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the Cassandra cluster. If vswitch_id is not empty, this zone_id can be “” or consistent.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.Cluster.auto_renew">
<code class="sig-name descname">auto_renew</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.auto_renew" title="Permalink to this definition">¶</a></dt>
<dd><p>Auto renew of dataCenter-1,<code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. System default to <code class="docutils literal notranslate"><span class="pre">false</span></code>, valid when pay_type = PrePaid.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.Cluster.auto_renew_period">
<code class="sig-name descname">auto_renew_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.auto_renew_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Period of dataCenter-1 auto renew, if auto renew is <code class="docutils literal notranslate"><span class="pre">true</span></code>, one of <code class="docutils literal notranslate"><span class="pre">1,</span> <span class="pre">2,</span> <span class="pre">3,</span> <span class="pre">4,</span> <span class="pre">5,</span> <span class="pre">6,</span> <span class="pre">7,</span> <span class="pre">8,</span> <span class="pre">9,</span> <span class="pre">12,</span> <span class="pre">24,</span> <span class="pre">36,</span> <span class="pre">60</span></code>, valid when pay_type = Subscription. Unit: month.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.Cluster.cluster_name">
<code class="sig-name descname">cluster_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cassandra cluster name. Length must be 2~128 characters long. Only Chinese characters, English letters, numbers, period <code class="docutils literal notranslate"><span class="pre">.</span></code>, underline <code class="docutils literal notranslate"><span class="pre">_</span></code>, or dash <code class="docutils literal notranslate"><span class="pre">-</span></code> are permitted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.Cluster.data_center_name">
<code class="sig-name descname">data_center_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.data_center_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cassandra dataCenter-1 name. Length must be 2~128 characters long. Only Chinese characters, English letters, numbers, period <code class="docutils literal notranslate"><span class="pre">.</span></code>, underline <code class="docutils literal notranslate"><span class="pre">_</span></code>, or dash <code class="docutils literal notranslate"><span class="pre">-</span></code> are permitted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.Cluster.disk_size">
<code class="sig-name descname">disk_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined Cassandra dataCenter-1 one node’s storage space.Unit: GB. Value range:</p>
<ul class="simple">
<li><p>Custom storage space; value range: [160, 2000].</p></li>
<li><p>80-GB increments.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.Cluster.disk_type">
<code class="sig-name descname">disk_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.disk_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The disk type of Cassandra dataCenter-1. Valid values are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>, <code class="docutils literal notranslate"><span class="pre">local_hdd_pro</span></code>, <code class="docutils literal notranslate"><span class="pre">local_ssd_pro</span></code>, local_disk size is fixed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.Cluster.instance_type">
<code class="sig-name descname">instance_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance specification. See <a class="reference external" href="https://help.aliyun.com/document_detail/157445.html">Instance specifications</a>. Or you can call describeInstanceType api.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.Cluster.ip_white">
<code class="sig-name descname">ip_white</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.ip_white" title="Permalink to this definition">¶</a></dt>
<dd><p>Set the instance’s IP whitelist in VPC network.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.Cluster.maintain_end_time">
<code class="sig-name descname">maintain_end_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.maintain_end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The end time of the operation and maintenance time period of the cluster, in the format of HH:mmZ (UTC time).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.Cluster.maintain_start_time">
<code class="sig-name descname">maintain_start_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.maintain_start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The start time of the operation and maintenance time period of the cluster, in the format of HH:mmZ (UTC time).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.Cluster.major_version">
<code class="sig-name descname">major_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.major_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Cassandra major version. Now only support version <code class="docutils literal notranslate"><span class="pre">3.11</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.Cluster.node_count">
<code class="sig-name descname">node_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.node_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The node count of Cassandra dataCenter-1 default to 2.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.Cluster.pay_type">
<code class="sig-name descname">pay_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.pay_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The pay type of Cassandra dataCenter-1. Valid values are <code class="docutils literal notranslate"><span class="pre">Subscription</span></code>, <code class="docutils literal notranslate"><span class="pre">PayAsYouGo</span></code>,System default to <code class="docutils literal notranslate"><span class="pre">PayAsYouGo</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.Cluster.security_groups">
<code class="sig-name descname">security_groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.security_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of security group ids to associate with.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.Cluster.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.Cluster.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The vswitch_id of dataCenter-1, can not empty.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.Cluster.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Zone to launch the Cassandra cluster. If vswitch_id is not empty, this zone_id can be “” or consistent.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cassandra.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_center_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_white</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintain_end_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">maintain_start_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">major_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pay_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_points</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Auto renew of dataCenter-1,<code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. System default to <code class="docutils literal notranslate"><span class="pre">false</span></code>, valid when pay_type = PrePaid.</p></li>
<li><p><strong>auto_renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Period of dataCenter-1 auto renew, if auto renew is <code class="docutils literal notranslate"><span class="pre">true</span></code>, one of <code class="docutils literal notranslate"><span class="pre">1,</span> <span class="pre">2,</span> <span class="pre">3,</span> <span class="pre">4,</span> <span class="pre">5,</span> <span class="pre">6,</span> <span class="pre">7,</span> <span class="pre">8,</span> <span class="pre">9,</span> <span class="pre">12,</span> <span class="pre">24,</span> <span class="pre">36,</span> <span class="pre">60</span></code>, valid when pay_type = Subscription. Unit: month.</p></li>
<li><p><strong>cluster*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Cassandra cluster name. Length must be 2~128 characters long. Only Chinese characters, English letters, numbers, period <code class="docutils literal notranslate"><span class="pre">.</span></code>, underline <cite>*`</cite>, or dash``-<a href="#id8"><span class="problematic" id="id9">``</span></a>are permitted.</p>
</p></li>
<li><p><strong>data_center_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cassandra dataCenter-1 name. Length must be 2~128 characters long. Only Chinese characters, English letters, numbers, period``.`, underline <cite>_`</cite>, or dash``-` are permitted.</p></li>
<li><p><strong>disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – User-defined Cassandra dataCenter-1 one node’s storage space.Unit: GB. Value range:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Custom</span> <span class="n">storage</span> <span class="n">space</span><span class="p">;</span> <span class="n">value</span> <span class="nb">range</span><span class="p">:</span> <span class="p">[</span><span class="mi">160</span><span class="p">,</span> <span class="mi">2000</span><span class="p">]</span><span class="o">.</span>
<span class="o">-</span> <span class="mi">80</span><span class="o">-</span><span class="n">GB</span> <span class="n">increments</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>disk_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The disk type of Cassandra dataCenter-1. Valid values are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>, <code class="docutils literal notranslate"><span class="pre">local_hdd_pro</span></code>, <code class="docutils literal notranslate"><span class="pre">local_ssd_pro</span></code>, local_disk size is fixed.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Instance specification. See <a class="reference external" href="https://help.aliyun.com/document_detail/157445.html">Instance specifications</a>. Or you can call describeInstanceType api.</p>
</p></li>
<li><p><strong>ip_white</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set the instance’s IP whitelist in VPC network.</p></li>
<li><p><strong>maintain_end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The end time of the operation and maintenance time period of the cluster, in the format of HH:mmZ (UTC time).</p></li>
<li><p><strong>maintain_start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The start time of the operation and maintenance time period of the cluster, in the format of HH:mmZ (UTC time).</p></li>
<li><p><strong>major_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cassandra major version. Now only support version <code class="docutils literal notranslate"><span class="pre">3.11</span></code>.</p></li>
<li><p><strong>node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The node count of Cassandra dataCenter-1 default to 2.</p></li>
<li><p><strong>pay_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pay type of Cassandra dataCenter-1. Valid values are <code class="docutils literal notranslate"><span class="pre">Subscription</span></code>, <code class="docutils literal notranslate"><span class="pre">PayAsYouGo</span></code>,System default to <code class="docutils literal notranslate"><span class="pre">PayAsYouGo</span></code>.</p></li>
<li><p><strong>security_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of security group ids to associate with.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vswitch_id of dataCenter-1, can not empty.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the Cassandra cluster. If vswitch_id is not empty, this zone_id can be “” or consistent.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cassandra.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cassandra.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cassandra.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cassandra.DataCenter">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cassandra.</code><code class="sig-name descname">DataCenter</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_center_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pay_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cassandra.DataCenter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Cassandra dataCenter resource supports replica set dataCenters only. The Cassandra provides stable, reliable, and automatic scalable database services. 
It offers a full range of database solutions, such as disaster recovery, backup, recovery, monitoring, and alarms.
You can see detail product introduction <a class="reference external" href="https://www.alibabacloud.com/help/product/49055.htm">here</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong>  Available in 1.88.0+.</p>
<p><strong>NOTE:</strong>  Create a cassandra dataCenter need a clusterId,so need create a cassandra cluster first.</p>
<p><strong>NOTE:</strong>  The following regions support create Vpc network Cassandra cluster.
The official website mark  more regions. Or you can call <a class="reference external" href="https://help.aliyun.com/document_detail/157540.html">DescribeRegions</a>.</p>
<p><strong>NOTE:</strong>  Create Cassandra dataCenter or change dataCenter type and storage would cost 30 minutes. Please make full preparation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Auto renew of dataCenter-2,<code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. System default to <code class="docutils literal notranslate"><span class="pre">false</span></code>, valid when pay_type = Subscription.</p></li>
<li><p><strong>auto_renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Period of dataCenter-2 auto renew, if auto renew is <code class="docutils literal notranslate"><span class="pre">true</span></code>, one of <code class="docutils literal notranslate"><span class="pre">1,</span> <span class="pre">2,</span> <span class="pre">3,</span> <span class="pre">4,</span> <span class="pre">5,</span> <span class="pre">6,</span> <span class="pre">7,</span> <span class="pre">8,</span> <span class="pre">9,</span> <span class="pre">12,</span> <span class="pre">24,</span> <span class="pre">36,</span> <span class="pre">60</span></code>, valid when pay_type = Subscription. Unit: month.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cassandra cluster id of dataCenter-2 belongs to.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>data_center*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Cassandra dataCenter-2 name. Length must be 2~128 characters long. Only Chinese characters, English letters, numbers, period <code class="docutils literal notranslate"><span class="pre">.</span></code>, underline <cite>*`</cite>, or dash``-` are permitted.</p>
</p></li>
<li><p><strong>disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – User-defined Cassandra dataCenter one core node’s storage space.Unit: GB. Value range:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Custom</span> <span class="n">storage</span> <span class="n">space</span><span class="p">;</span> <span class="n">value</span> <span class="nb">range</span><span class="p">:</span> <span class="p">[</span><span class="mi">160</span><span class="p">,</span> <span class="mi">2000</span><span class="p">]</span><span class="o">.</span>
<span class="o">-</span> <span class="mi">80</span><span class="o">-</span><span class="n">GB</span> <span class="n">increments</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>disk_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The disk type of Cassandra dataCenter-2. Valid values are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>, <code class="docutils literal notranslate"><span class="pre">local_hdd_pro</span></code>, <code class="docutils literal notranslate"><span class="pre">local_ssd_pro</span></code>, local_disk size is fixed.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Instance specification. See <a class="reference external" href="https://help.aliyun.com/document_detail/157445.html">Instance specifications</a>. Or you can call describeInstanceType api.</p>
</p></li>
<li><p><strong>node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The node count of Cassandra dataCenter-2, default to 2.</p></li>
<li><p><strong>pay_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pay type of Cassandra dataCenter-2. Valid values are <code class="docutils literal notranslate"><span class="pre">Subscription</span></code>, <code class="docutils literal notranslate"><span class="pre">PayAsYouGo</span></code>. System default to <code class="docutils literal notranslate"><span class="pre">PayAsYouGo</span></code>.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vswitch_id of dataCenter-2, mast different of vswitch_id(dc-1), can not empty.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the Cassandra dataCenter-2. If vswitch_id is not empty, this zone_id can be “” or consistent.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.DataCenter.auto_renew">
<code class="sig-name descname">auto_renew</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.DataCenter.auto_renew" title="Permalink to this definition">¶</a></dt>
<dd><p>Auto renew of dataCenter-2,<code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. System default to <code class="docutils literal notranslate"><span class="pre">false</span></code>, valid when pay_type = Subscription.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.DataCenter.auto_renew_period">
<code class="sig-name descname">auto_renew_period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.DataCenter.auto_renew_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Period of dataCenter-2 auto renew, if auto renew is <code class="docutils literal notranslate"><span class="pre">true</span></code>, one of <code class="docutils literal notranslate"><span class="pre">1,</span> <span class="pre">2,</span> <span class="pre">3,</span> <span class="pre">4,</span> <span class="pre">5,</span> <span class="pre">6,</span> <span class="pre">7,</span> <span class="pre">8,</span> <span class="pre">9,</span> <span class="pre">12,</span> <span class="pre">24,</span> <span class="pre">36,</span> <span class="pre">60</span></code>, valid when pay_type = Subscription. Unit: month.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.DataCenter.cluster_id">
<code class="sig-name descname">cluster_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.DataCenter.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Cassandra cluster id of dataCenter-2 belongs to.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.DataCenter.data_center_name">
<code class="sig-name descname">data_center_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.DataCenter.data_center_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cassandra dataCenter-2 name. Length must be 2~128 characters long. Only Chinese characters, English letters, numbers, period <code class="docutils literal notranslate"><span class="pre">.</span></code>, underline <code class="docutils literal notranslate"><span class="pre">_</span></code>, or dash <code class="docutils literal notranslate"><span class="pre">-</span></code> are permitted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.DataCenter.disk_size">
<code class="sig-name descname">disk_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.DataCenter.disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined Cassandra dataCenter one core node’s storage space.Unit: GB. Value range:</p>
<ul class="simple">
<li><p>Custom storage space; value range: [160, 2000].</p></li>
<li><p>80-GB increments.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.DataCenter.disk_type">
<code class="sig-name descname">disk_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.DataCenter.disk_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The disk type of Cassandra dataCenter-2. Valid values are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>, <code class="docutils literal notranslate"><span class="pre">local_hdd_pro</span></code>, <code class="docutils literal notranslate"><span class="pre">local_ssd_pro</span></code>, local_disk size is fixed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.DataCenter.instance_type">
<code class="sig-name descname">instance_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.DataCenter.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance specification. See <a class="reference external" href="https://help.aliyun.com/document_detail/157445.html">Instance specifications</a>. Or you can call describeInstanceType api.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.DataCenter.node_count">
<code class="sig-name descname">node_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.DataCenter.node_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The node count of Cassandra dataCenter-2, default to 2.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.DataCenter.pay_type">
<code class="sig-name descname">pay_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.DataCenter.pay_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The pay type of Cassandra dataCenter-2. Valid values are <code class="docutils literal notranslate"><span class="pre">Subscription</span></code>, <code class="docutils literal notranslate"><span class="pre">PayAsYouGo</span></code>. System default to <code class="docutils literal notranslate"><span class="pre">PayAsYouGo</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.DataCenter.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.DataCenter.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The vswitch_id of dataCenter-2, mast different of vswitch_id(dc-1), can not empty.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.DataCenter.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.DataCenter.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Zone to launch the Cassandra dataCenter-2. If vswitch_id is not empty, this zone_id can be “” or consistent.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cassandra.DataCenter.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_renew_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_center_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_center_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_public</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pay_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period_unit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_points</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cassandra.DataCenter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DataCenter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_renew</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Auto renew of dataCenter-2,<code class="docutils literal notranslate"><span class="pre">true</span></code> or <code class="docutils literal notranslate"><span class="pre">false</span></code>. System default to <code class="docutils literal notranslate"><span class="pre">false</span></code>, valid when pay_type = Subscription.</p></li>
<li><p><strong>auto_renew_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Period of dataCenter-2 auto renew, if auto renew is <code class="docutils literal notranslate"><span class="pre">true</span></code>, one of <code class="docutils literal notranslate"><span class="pre">1,</span> <span class="pre">2,</span> <span class="pre">3,</span> <span class="pre">4,</span> <span class="pre">5,</span> <span class="pre">6,</span> <span class="pre">7,</span> <span class="pre">8,</span> <span class="pre">9,</span> <span class="pre">12,</span> <span class="pre">24,</span> <span class="pre">36,</span> <span class="pre">60</span></code>, valid when pay_type = Subscription. Unit: month.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cassandra cluster id of dataCenter-2 belongs to.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>data_center*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Cassandra dataCenter-2 name. Length must be 2~128 characters long. Only Chinese characters, English letters, numbers, period <code class="docutils literal notranslate"><span class="pre">.</span></code>, underline <cite>*`</cite>, or dash``-` are permitted.</p>
</p></li>
<li><p><strong>disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – User-defined Cassandra dataCenter one core node’s storage space.Unit: GB. Value range:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Custom</span> <span class="n">storage</span> <span class="n">space</span><span class="p">;</span> <span class="n">value</span> <span class="nb">range</span><span class="p">:</span> <span class="p">[</span><span class="mi">160</span><span class="p">,</span> <span class="mi">2000</span><span class="p">]</span><span class="o">.</span>
<span class="o">-</span> <span class="mi">80</span><span class="o">-</span><span class="n">GB</span> <span class="n">increments</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>disk_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The disk type of Cassandra dataCenter-2. Valid values are <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>, <code class="docutils literal notranslate"><span class="pre">local_hdd_pro</span></code>, <code class="docutils literal notranslate"><span class="pre">local_ssd_pro</span></code>, local_disk size is fixed.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Instance specification. See <a class="reference external" href="https://help.aliyun.com/document_detail/157445.html">Instance specifications</a>. Or you can call describeInstanceType api.</p>
</p></li>
<li><p><strong>node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The node count of Cassandra dataCenter-2, default to 2.</p></li>
<li><p><strong>pay_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The pay type of Cassandra dataCenter-2. Valid values are <code class="docutils literal notranslate"><span class="pre">Subscription</span></code>, <code class="docutils literal notranslate"><span class="pre">PayAsYouGo</span></code>. System default to <code class="docutils literal notranslate"><span class="pre">PayAsYouGo</span></code>.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The vswitch_id of dataCenter-2, mast different of vswitch_id(dc-1), can not empty.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the Cassandra dataCenter-2. If vswitch_id is not empty, this zone_id can be “” or consistent.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.cassandra.DataCenter.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cassandra.DataCenter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cassandra.DataCenter.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cassandra.DataCenter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cassandra.GetClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cassandra.</code><code class="sig-name descname">GetClustersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">clusters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cassandra.GetClustersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClusters.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.GetClustersResult.clusters">
<code class="sig-name descname">clusters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.GetClustersResult.clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Cassandra clusters. Its every element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.GetClustersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.GetClustersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.GetClustersResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.GetClustersResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of Cassandra cluster ids.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.GetClustersResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.GetClustersResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>The name list of Cassandra clusters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.GetClustersResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.GetClustersResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cassandra.GetDataCentersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cassandra.</code><code class="sig-name descname">GetDataCentersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">centers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cassandra.GetDataCentersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDataCenters.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.GetDataCentersResult.centers">
<code class="sig-name descname">centers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.GetDataCentersResult.centers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Cassandra data centers. Its every element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.GetDataCentersResult.cluster_id">
<code class="sig-name descname">cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.GetDataCentersResult.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Cassandra cluster.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.GetDataCentersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.GetDataCentersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.GetDataCentersResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.GetDataCentersResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of Cassandra data center ids.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.GetDataCentersResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.GetDataCentersResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>The name list of Cassandra data centers.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.cassandra.GetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cassandra.</code><code class="sig-name descname">GetZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cassandra.GetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZones.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.GetZonesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.GetZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.GetZonesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.GetZonesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of zone IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.cassandra.GetZonesResult.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cassandra.GetZonesResult.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of availability zones. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.cassandra.get_clusters">
<code class="sig-prename descclassname">pulumi_alicloud.cassandra.</code><code class="sig-name descname">get_clusters</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cassandra.get_clusters" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">cassandra.getClusters</span></code> data source provides a collection of Cassandra clusters available in Alicloud account.
Filters support regular expression for the cluster name, ids or tags.</p>
<blockquote>
<div><p><strong>NOTE:</strong>  Available in 1.88.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – The list of Cassandra cluster ids.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to apply to the cluster name.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.cassandra.get_data_centers">
<code class="sig-prename descclassname">pulumi_alicloud.cassandra.</code><code class="sig-name descname">get_data_centers</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cassandra.get_data_centers" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">cassandra.getDataCenters</span></code> data source provides a collection of Cassandra Data Centers available in Alicloud account.
Filters support regular expression for the cluster name or ids.</p>
<blockquote>
<div><p><strong>NOTE:</strong>  Available in 1.88.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_id</strong> (<em>str</em>) – The cluster id of dataCenters belongs to.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – The list of Cassandra data center ids.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to apply to the cluster name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.cassandra.get_zones">
<code class="sig-prename descclassname">pulumi_alicloud.cassandra.</code><code class="sig-name descname">get_zones</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">multi</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cassandra.get_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides availability zones for Cassandra that can be accessed by an Alibaba Cloud account within the region configured in the provider.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.88.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>multi</strong> (<em>bool</em>) – Indicate whether the zones can be used in a multi AZ configuration. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Multi AZ is usually used to launch Cassandra clusters.</p>
</dd>
</dl>
</dd></dl>

</div>
