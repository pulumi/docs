---
title: Module drds
title_tag: Module drds | Package pulumi_alicloud | Python SDK
linktitle: drds
notitle: true
---

<div class="section" id="drds">
<h1>drds<a class="headerlink" href="#drds" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.drds"></span><dl class="py class">
<dt id="pulumi_alicloud.drds.AwaitableGetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.drds.</code><code class="sig-name descname">AwaitableGetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">descriptions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.drds.AwaitableGetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.drds.GetInstancesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.drds.</code><code class="sig-name descname">GetInstancesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">descriptions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instances</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.drds.GetInstancesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstances.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.drds.GetInstancesResult.descriptions">
<code class="sig-name descname">descriptions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.drds.GetInstancesResult.descriptions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of DRDS descriptions.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.drds.GetInstancesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.drds.GetInstancesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.drds.GetInstancesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.drds.GetInstancesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of DRDS instance IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.drds.GetInstancesResult.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.drds.GetInstancesResult.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of DRDS instances.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.drds.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.drds.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_series</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">specification</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.drds.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Distributed Relational Database Service (DRDS) is a lightweight (stateless), flexible, stable, and efficient middleware product independently developed by Alibaba Group to resolve scalability issues with single-host relational databases.
With its compatibility with MySQL protocols and syntaxes, DRDS enables database/table sharding, smooth scaling, configuration upgrade/downgrade,
transparent read/write splitting, and distributed transactions, providing O&amp;M capabilities for distributed databases throughout their entire lifecycle.</p>
<p>For information about DRDS and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/29659.htm">What is DRDS</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> At present, DRDS instance only can be supported in the regions: cn-shenzhen, cn-beijing, cn-hangzhou, cn-hongkong, cn-qingdao.</p>
<p><strong>NOTE:</strong> Currently, this resource only support <code class="docutils literal notranslate"><span class="pre">Domestic</span> <span class="pre">Site</span> <span class="pre">Account</span></code>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the DRDS instance, This description can have a string of 2 to 256 characters.</p></li>
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>instance_series</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-defined DRDS instance node spec. Value range:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `drds.sn1.4c8g` for DRDS instance Starter version;
- `drds.sn1.8c16g` for DRDS instance Standard edition;
- `drds.sn1.16c32g` for DRDS instance Enterprise Edition;
- `drds.sn1.32c64g` for DRDS instance Extreme Edition;
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>specification</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-defined DRDS instance specification. Value range:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `drds.sn1.4c8g` for DRDS instance Starter version;
- value range : `drds.sn1.4c8g.8c16g`, `drds.sn1.4c8g.16c32g`, `drds.sn1.4c8g.32c64g`, `drds.sn1.4c8g.64c128g`
- `drds.sn1.8c16g` for DRDS instance Standard edition;
- value range : `drds.sn1.8c16g.16c32g`, `drds.sn1.8c16g.32c64g`, `drds.sn1.8c16g.64c128g`
- `drds.sn1.16c32g` for DRDS instance Enterprise Edition;
- value range : `drds.sn1.16c32g.32c64g`, `drds.sn1.16c32g.64c128g`
- `drds.sn1.32c64g` for DRDS instance Extreme Edition;
- value range : `drds.sn1.32c64g.128c256g`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VSwitch ID to launch in.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the DRDS instance.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.drds.Instance.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.drds.Instance.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the DRDS instance, This description can have a string of 2 to 256 characters.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.drds.Instance.instance_charge_type">
<code class="sig-name descname">instance_charge_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.drds.Instance.instance_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.drds.Instance.instance_series">
<code class="sig-name descname">instance_series</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.drds.Instance.instance_series" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined DRDS instance node spec. Value range:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">drds.sn1.4c8g</span></code> for DRDS instance Starter version;</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">drds.sn1.8c16g</span></code> for DRDS instance Standard edition;</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">drds.sn1.16c32g</span></code> for DRDS instance Enterprise Edition;</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">drds.sn1.32c64g</span></code> for DRDS instance Extreme Edition;</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.drds.Instance.specification">
<code class="sig-name descname">specification</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.drds.Instance.specification" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined DRDS instance specification. Value range:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">drds.sn1.4c8g</span></code> for DRDS instance Starter version;</p></li>
<li><p>value range : <code class="docutils literal notranslate"><span class="pre">drds.sn1.4c8g.8c16g</span></code>, <code class="docutils literal notranslate"><span class="pre">drds.sn1.4c8g.16c32g</span></code>, <code class="docutils literal notranslate"><span class="pre">drds.sn1.4c8g.32c64g</span></code>, <code class="docutils literal notranslate"><span class="pre">drds.sn1.4c8g.64c128g</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">drds.sn1.8c16g</span></code> for DRDS instance Standard edition;</p></li>
<li><p>value range : <code class="docutils literal notranslate"><span class="pre">drds.sn1.8c16g.16c32g</span></code>, <code class="docutils literal notranslate"><span class="pre">drds.sn1.8c16g.32c64g</span></code>, <code class="docutils literal notranslate"><span class="pre">drds.sn1.8c16g.64c128g</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">drds.sn1.16c32g</span></code> for DRDS instance Enterprise Edition;</p></li>
<li><p>value range : <code class="docutils literal notranslate"><span class="pre">drds.sn1.16c32g.32c64g</span></code>, <code class="docutils literal notranslate"><span class="pre">drds.sn1.16c32g.64c128g</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">drds.sn1.32c64g</span></code> for DRDS instance Extreme Edition;</p></li>
<li><p>value range : <code class="docutils literal notranslate"><span class="pre">drds.sn1.32c64g.128c256g</span></code></p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.drds.Instance.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.drds.Instance.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The VSwitch ID to launch in.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.drds.Instance.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.drds.Instance.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Zone to launch the DRDS instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.drds.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_series</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">specification</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.drds.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the DRDS instance, This description can have a string of 2 to 256 characters.</p></li>
<li><p><strong>instance_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>, Default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>instance_series</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-defined DRDS instance node spec. Value range:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `drds.sn1.4c8g` for DRDS instance Starter version;
- `drds.sn1.8c16g` for DRDS instance Standard edition;
- `drds.sn1.16c32g` for DRDS instance Enterprise Edition;
- `drds.sn1.32c64g` for DRDS instance Extreme Edition;
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>specification</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-defined DRDS instance specification. Value range:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `drds.sn1.4c8g` for DRDS instance Starter version;
- value range : `drds.sn1.4c8g.8c16g`, `drds.sn1.4c8g.16c32g`, `drds.sn1.4c8g.32c64g`, `drds.sn1.4c8g.64c128g`
- `drds.sn1.8c16g` for DRDS instance Standard edition;
- value range : `drds.sn1.8c16g.16c32g`, `drds.sn1.8c16g.32c64g`, `drds.sn1.8c16g.64c128g`
- `drds.sn1.16c32g` for DRDS instance Enterprise Edition;
- value range : `drds.sn1.16c32g.32c64g`, `drds.sn1.16c32g.64c128g`
- `drds.sn1.32c64g` for DRDS instance Extreme Edition;
- value range : `drds.sn1.32c64g.128c256g`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VSwitch ID to launch in.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone to launch the DRDS instance.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.drds.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.drds.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.drds.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.drds.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.drds.get_instances">
<code class="sig-prename descclassname">pulumi_alicloud.drds.</code><code class="sig-name descname">get_instances</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.drds.get_instances" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p>The <code class="docutils literal notranslate"><span class="pre">drds.Instance</span></code> data source provides a collection of DRDS instances available in Alibaba Cloud account.</p>
</div></blockquote>
<p>Filters support regular expression for the instance name, searches by tags, and other filters which are listed below.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.35.0+.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of DRDS instance IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter results by instance name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
