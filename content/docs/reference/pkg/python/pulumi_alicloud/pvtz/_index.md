---
title: Module pvtz
title_tag: Module pvtz | Package pulumi_alicloud | Python SDK
linktitle: pvtz
notitle: true
---

<div class="section" id="pvtz">
<h1>pvtz<a class="headerlink" href="#pvtz" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.pvtz"></span><dl class="py class">
<dt id="pulumi_alicloud.pvtz.AwaitableGetZoneRecordsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.pvtz.</code><code class="sig-name descname">AwaitableGetZoneRecordsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keyword</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">records</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.pvtz.AwaitableGetZoneRecordsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.pvtz.AwaitableGetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.pvtz.</code><code class="sig-name descname">AwaitableGetZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keyword</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.pvtz.AwaitableGetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.pvtz.GetZoneRecordsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.pvtz.</code><code class="sig-name descname">GetZoneRecordsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keyword</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">records</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.pvtz.GetZoneRecordsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZoneRecords.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.GetZoneRecordsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.GetZoneRecordsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.GetZoneRecordsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.GetZoneRecordsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Private Zone Record IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.GetZoneRecordsResult.records">
<code class="sig-name descname">records</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.GetZoneRecordsResult.records" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of zone records. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.pvtz.GetZonesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.pvtz.</code><code class="sig-name descname">GetZonesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keyword</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zones</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.pvtz.GetZonesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getZones.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.GetZonesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.GetZonesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.GetZonesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.GetZonesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of zone IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.GetZonesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.GetZonesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of zone names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.GetZonesResult.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.GetZonesResult.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of zones. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.pvtz.Zone">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.pvtz.</code><code class="sig-name descname">Zone</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lang</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_pattern</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remark</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_client_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.pvtz.Zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Zone resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] lang: The language. Valid values: “zh”, “en”, “jp”.
:param pulumi.Input[str] name: The name of the Private Zone.
:param pulumi.Input[str] proxy_pattern: The recursive DNS proxy. Valid values:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">ZONE</span><span class="p">:</span> <span class="n">indicates</span> <span class="n">that</span> <span class="n">the</span> <span class="n">recursive</span> <span class="n">DNS</span> <span class="n">proxy</span> <span class="ow">is</span> <span class="n">disabled</span><span class="o">.</span>
<span class="o">-</span> <span class="n">RECORD</span><span class="p">:</span> <span class="n">indicates</span> <span class="n">that</span> <span class="n">the</span> <span class="n">recursive</span> <span class="n">DNS</span> <span class="n">proxy</span> <span class="ow">is</span> <span class="n">enabled</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>remark</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The remark of the Private Zone.</p></li>
<li><p><strong>user_client_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the client.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.Zone.lang">
<code class="sig-name descname">lang</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.Zone.lang" title="Permalink to this definition">¶</a></dt>
<dd><p>The language. Valid values: “zh”, “en”, “jp”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.Zone.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.Zone.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Private Zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.Zone.proxy_pattern">
<code class="sig-name descname">proxy_pattern</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.Zone.proxy_pattern" title="Permalink to this definition">¶</a></dt>
<dd><p>The recursive DNS proxy. Valid values:</p>
<ul class="simple">
<li><p>ZONE: indicates that the recursive DNS proxy is disabled.</p></li>
<li><p>RECORD: indicates that the recursive DNS proxy is enabled.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.Zone.record_count">
<code class="sig-name descname">record_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.Zone.record_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The count of the Private Zone Record.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.Zone.remark">
<code class="sig-name descname">remark</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.Zone.remark" title="Permalink to this definition">¶</a></dt>
<dd><p>The remark of the Private Zone.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.Zone.user_client_ip">
<code class="sig-name descname">user_client_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.Zone.user_client_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address of the client.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.pvtz.Zone.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">creation_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_ptr</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lang</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">proxy_pattern</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">record_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remark</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_client_ip</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.pvtz.Zone.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Zone resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>lang</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The language. Valid values: “zh”, “en”, “jp”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Private Zone.</p></li>
<li><p><strong>proxy_pattern</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The recursive DNS proxy. Valid values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">ZONE</span><span class="p">:</span> <span class="n">indicates</span> <span class="n">that</span> <span class="n">the</span> <span class="n">recursive</span> <span class="n">DNS</span> <span class="n">proxy</span> <span class="ow">is</span> <span class="n">disabled</span><span class="o">.</span>
<span class="o">-</span> <span class="n">RECORD</span><span class="p">:</span> <span class="n">indicates</span> <span class="n">that</span> <span class="n">the</span> <span class="n">recursive</span> <span class="n">DNS</span> <span class="n">proxy</span> <span class="ow">is</span> <span class="n">enabled</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>record_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The count of the Private Zone Record.</p></li>
<li><p><strong>remark</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The remark of the Private Zone.</p></li>
<li><p><strong>user_client_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address of the client.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.pvtz.Zone.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.pvtz.Zone.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.pvtz.Zone.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.pvtz.Zone.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.pvtz.ZoneAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.pvtz.</code><code class="sig-name descname">ZoneAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lang</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_client_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpcs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ZoneAttachment resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] lang: The language of code.
:param pulumi.Input[str] user_client_ip: The user custom IP address.
:param pulumi.Input[list] vpc_ids: The id List of the VPC with the same region, for example:[“vpc-1”,”vpc-2”]. 
:param pulumi.Input[list] vpcs: The List of the VPC:
:param pulumi.Input[str] zone_id: The name of the Private Zone Record.</p>
<p>The <strong>vpcs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">regionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region of the vpc. If not set, the current region will instead of.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Id of the vpc.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.ZoneAttachment.lang">
<code class="sig-name descname">lang</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneAttachment.lang" title="Permalink to this definition">¶</a></dt>
<dd><p>The language of code.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.ZoneAttachment.user_client_ip">
<code class="sig-name descname">user_client_ip</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneAttachment.user_client_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>The user custom IP address.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.ZoneAttachment.vpc_ids">
<code class="sig-name descname">vpc_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneAttachment.vpc_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The id List of the VPC with the same region, for example:[“vpc-1”,”vpc-2”].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.ZoneAttachment.vpcs">
<code class="sig-name descname">vpcs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneAttachment.vpcs" title="Permalink to this definition">¶</a></dt>
<dd><p>The List of the VPC:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">regionId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The region of the vpc. If not set, the current region will instead of.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Id of the vpc.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.ZoneAttachment.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneAttachment.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Private Zone Record.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.pvtz.ZoneAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lang</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_client_ip</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpcs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ZoneAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>lang</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The language of code.</p></li>
<li><p><strong>user_client_ip</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user custom IP address.</p></li>
<li><p><strong>vpc_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The id List of the VPC with the same region, for example:[“vpc-1”,”vpc-2”].</p></li>
<li><p><strong>vpcs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The List of the VPC:</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Private Zone Record.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>vpcs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">regionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The region of the vpc. If not set, the current region will instead of.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Id of the vpc.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.pvtz.ZoneAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.pvtz.ZoneAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.pvtz.ZoneRecord">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.pvtz.</code><code class="sig-name descname">ZoneRecord</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_record</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneRecord" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ZoneRecord resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[float] priority: The priority of the Private Zone Record. At present, only can “MX” record support it. Valid values: [1-50]. Default to 1.
:param pulumi.Input[str] resource_record: The resource record of the Private Zone Record.
:param pulumi.Input[float] ttl: The ttl of the Private Zone Record.
:param pulumi.Input[str] type: The type of the Private Zone Record. Valid values: A, CNAME, TXT, MX, PTR.
:param pulumi.Input[str] value: The value of the Private Zone Record.
:param pulumi.Input[str] zone_id: The name of the Private Zone Record.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.ZoneRecord.priority">
<code class="sig-name descname">priority</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneRecord.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The priority of the Private Zone Record. At present, only can “MX” record support it. Valid values: [1-50]. Default to 1.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.ZoneRecord.record_id">
<code class="sig-name descname">record_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneRecord.record_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Private Zone Record ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.ZoneRecord.resource_record">
<code class="sig-name descname">resource_record</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneRecord.resource_record" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource record of the Private Zone Record.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.ZoneRecord.ttl">
<code class="sig-name descname">ttl</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneRecord.ttl" title="Permalink to this definition">¶</a></dt>
<dd><p>The ttl of the Private Zone Record.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.ZoneRecord.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneRecord.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the Private Zone Record. Valid values: A, CNAME, TXT, MX, PTR.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.ZoneRecord.value">
<code class="sig-name descname">value</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneRecord.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the Private Zone Record.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.pvtz.ZoneRecord.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneRecord.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Private Zone Record.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.pvtz.ZoneRecord.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">record_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_record</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ttl</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneRecord.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ZoneRecord resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The priority of the Private Zone Record. At present, only can “MX” record support it. Valid values: [1-50]. Default to 1.</p></li>
<li><p><strong>record_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Private Zone Record ID.</p></li>
<li><p><strong>resource_record</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource record of the Private Zone Record.</p></li>
<li><p><strong>ttl</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ttl of the Private Zone Record.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the Private Zone Record. Valid values: A, CNAME, TXT, MX, PTR.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the Private Zone Record.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Private Zone Record.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.pvtz.ZoneRecord.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneRecord.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.pvtz.ZoneRecord.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.pvtz.ZoneRecord.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.pvtz.get_zone_records">
<code class="sig-prename descclassname">pulumi_alicloud.pvtz.</code><code class="sig-name descname">get_zone_records</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keyword</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.pvtz.get_zone_records" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides Private Zone Records resource information owned by an Alibaba Cloud account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">records_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">pvtz</span><span class="o">.</span><span class="n">get_zone_records</span><span class="p">(</span><span class="n">keyword</span><span class="o">=</span><span class="n">alicloud_pvtz_zone_record</span><span class="p">[</span><span class="s2">&quot;foo&quot;</span><span class="p">][</span><span class="s2">&quot;value&quot;</span><span class="p">],</span>
    <span class="n">zone_id</span><span class="o">=</span><span class="n">alicloud_pvtz_zone</span><span class="p">[</span><span class="s2">&quot;basic&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstRecordId&quot;</span><span class="p">,</span> <span class="n">records_ds</span><span class="o">.</span><span class="n">records</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of Private Zone Record IDs.</p></li>
<li><p><strong>keyword</strong> (<em>str</em>) – Keyword for record rr and value.</p></li>
<li><p><strong>zone_id</strong> (<em>str</em>) – ID of the Private Zone.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.pvtz.get_zones">
<code class="sig-prename descclassname">pulumi_alicloud.pvtz.</code><code class="sig-name descname">get_zones</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keyword</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.pvtz.get_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source lists a number of Private Zones resource information owned by an Alibaba Cloud account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">pvtz_zones_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">pvtz</span><span class="o">.</span><span class="n">get_zones</span><span class="p">(</span><span class="n">keyword</span><span class="o">=</span><span class="n">alicloud_pvtz_zone</span><span class="p">[</span><span class="s2">&quot;basic&quot;</span><span class="p">][</span><span class="s2">&quot;zone_name&quot;</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstZoneId&quot;</span><span class="p">,</span> <span class="n">pvtz_zones_ds</span><span class="o">.</span><span class="n">zones</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of zone IDs.</p></li>
<li><p><strong>keyword</strong> (<em>str</em>) – keyword for zone name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
