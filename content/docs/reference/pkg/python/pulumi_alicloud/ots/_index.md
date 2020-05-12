---
title: Module ots
title_tag: Module ots | Package pulumi_alicloud | Python SDK
linktitle: ots
notitle: true
---

<div class="section" id="ots">
<h1>ots<a class="headerlink" href="#ots" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.ots"></span><dl class="py class">
<dt id="pulumi_alicloud.ots.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ots.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessed_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ots.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource will help you to manager a <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/27280.htm">Table Store</a> Instance.
It is foundation of creating data table.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="c1"># Create an OTS instance</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ots</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">accessed_by</span><span class="o">=</span><span class="s2">&quot;Vpc&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;for table&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;Created&quot;</span><span class="p">:</span> <span class="s2">&quot;TF&quot;</span><span class="p">,</span>
        <span class="s2">&quot;For&quot;</span><span class="p">:</span> <span class="s2">&quot;Building table&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessed_by</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network limitation of accessing instance. Valid values:</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the instance. Currently, it does not support modifying.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of instance. Valid values are “Capacity” and “HighPerformance”. Default to “HighPerformance”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the instance.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ots.Instance.accessed_by">
<code class="sig-name descname">accessed_by</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ots.Instance.accessed_by" title="Permalink to this definition">¶</a></dt>
<dd><p>The network limitation of accessing instance. Valid values:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ots.Instance.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ots.Instance.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the instance. Currently, it does not support modifying.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ots.Instance.instance_type">
<code class="sig-name descname">instance_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ots.Instance.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of instance. Valid values are “Capacity” and “HighPerformance”. Default to “HighPerformance”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ots.Instance.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ots.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ots.Instance.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ots.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ots.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accessed_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ots.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accessed_by</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network limitation of accessing instance. Valid values:</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the instance. Currently, it does not support modifying.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of instance. Valid values are “Capacity” and “HighPerformance”. Default to “HighPerformance”.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the instance.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ots.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ots.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ots.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ots.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ots.InstanceAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ots.</code><code class="sig-name descname">InstanceAttachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ots.InstanceAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource will help you to bind a VPC to an OTS instance.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="c1"># Create an OTS instance</span>
<span class="n">foo_instance</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ots</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;fooInstance&quot;</span><span class="p">,</span>
    <span class="n">accessed_by</span><span class="o">=</span><span class="s2">&quot;Vpc&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;for table&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;Created&quot;</span><span class="p">:</span> <span class="s2">&quot;TF&quot;</span><span class="p">,</span>
        <span class="s2">&quot;For&quot;</span><span class="p">:</span> <span class="s2">&quot;Building table&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">foo_zones</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">get_zones</span><span class="p">(</span><span class="n">available_resource_creation</span><span class="o">=</span><span class="s2">&quot;VSwitch&quot;</span><span class="p">)</span>
<span class="n">foo_network</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;fooNetwork&quot;</span><span class="p">,</span> <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;172.16.0.0/16&quot;</span><span class="p">)</span>
<span class="n">foo_switch</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Switch</span><span class="p">(</span><span class="s2">&quot;fooSwitch&quot;</span><span class="p">,</span>
    <span class="n">availability_zone</span><span class="o">=</span><span class="n">foo_zones</span><span class="o">.</span><span class="n">zones</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;172.16.1.0/24&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">foo_network</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">foo_instance_attachment</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ots</span><span class="o">.</span><span class="n">InstanceAttachment</span><span class="p">(</span><span class="s2">&quot;fooInstanceAttachment&quot;</span><span class="p">,</span>
    <span class="n">instance_name</span><span class="o">=</span><span class="n">foo_instance</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">vpc_name</span><span class="o">=</span><span class="s2">&quot;attachment1&quot;</span><span class="p">,</span>
    <span class="n">vswitch_id</span><span class="o">=</span><span class="n">foo_switch</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the OTS instance.</p></li>
<li><p><strong>vpc_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of attaching VPC to instance.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of attaching VSwitch to instance.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ots.InstanceAttachment.instance_name">
<code class="sig-name descname">instance_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ots.InstanceAttachment.instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the OTS instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ots.InstanceAttachment.vpc_id">
<code class="sig-name descname">vpc_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ots.InstanceAttachment.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of attaching VPC to instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ots.InstanceAttachment.vpc_name">
<code class="sig-name descname">vpc_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ots.InstanceAttachment.vpc_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of attaching VPC to instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ots.InstanceAttachment.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ots.InstanceAttachment.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of attaching VSwitch to instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ots.InstanceAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ots.InstanceAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InstanceAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the OTS instance.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of attaching VPC to instance.</p></li>
<li><p><strong>vpc_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of attaching VPC to instance.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of attaching VSwitch to instance.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ots.InstanceAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ots.InstanceAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ots.InstanceAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ots.InstanceAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ots.Table">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ots.</code><code class="sig-name descname">Table</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deviation_cell_version_in_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">table_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_to_live</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ots.Table" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Table resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] deviation_cell_version_in_sec: The max version offset of the table. The valid value is 1-9223372036854775807. Defaults to 86400.
:param pulumi.Input[str] instance_name: The name of the OTS instance in which table will located.
:param pulumi.Input[float] max_version: The maximum number of versions stored in this table. The valid value is 1-2147483647.
:param pulumi.Input[list] primary_keys: The property of <code class="docutils literal notranslate"><span class="pre">TableMeta</span></code> which indicates the structure information of a table. It describes the attribute value of primary key. The number of <code class="docutils literal notranslate"><span class="pre">primary_key</span></code> should not be less than one and not be more than four.
:param pulumi.Input[str] table_name: The table name of the OTS instance. If changed, a new table would be created.
:param pulumi.Input[float] time_to_live: The retention time of data stored in this table (unit: second). The value maximum is 2147483647 and -1 means never expired.</p>
<p>The <strong>primary_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name for primary key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type for primary key. Only <code class="docutils literal notranslate"><span class="pre">Integer</span></code>, <code class="docutils literal notranslate"><span class="pre">String</span></code> or <code class="docutils literal notranslate"><span class="pre">Binary</span></code> is allowed.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.ots.Table.deviation_cell_version_in_sec">
<code class="sig-name descname">deviation_cell_version_in_sec</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ots.Table.deviation_cell_version_in_sec" title="Permalink to this definition">¶</a></dt>
<dd><p>The max version offset of the table. The valid value is 1-9223372036854775807. Defaults to 86400.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ots.Table.instance_name">
<code class="sig-name descname">instance_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ots.Table.instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the OTS instance in which table will located.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ots.Table.max_version">
<code class="sig-name descname">max_version</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ots.Table.max_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of versions stored in this table. The valid value is 1-2147483647.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ots.Table.primary_keys">
<code class="sig-name descname">primary_keys</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ots.Table.primary_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>The property of <code class="docutils literal notranslate"><span class="pre">TableMeta</span></code> which indicates the structure information of a table. It describes the attribute value of primary key. The number of <code class="docutils literal notranslate"><span class="pre">primary_key</span></code> should not be less than one and not be more than four.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name for primary key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Type for primary key. Only <code class="docutils literal notranslate"><span class="pre">Integer</span></code>, <code class="docutils literal notranslate"><span class="pre">String</span></code> or <code class="docutils literal notranslate"><span class="pre">Binary</span></code> is allowed.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ots.Table.table_name">
<code class="sig-name descname">table_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ots.Table.table_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The table name of the OTS instance. If changed, a new table would be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ots.Table.time_to_live">
<code class="sig-name descname">time_to_live</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ots.Table.time_to_live" title="Permalink to this definition">¶</a></dt>
<dd><p>The retention time of data stored in this table (unit: second). The value maximum is 2147483647 and -1 means never expired.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ots.Table.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">deviation_cell_version_in_sec</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">primary_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">table_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_to_live</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ots.Table.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Table resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>deviation_cell_version_in_sec</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The max version offset of the table. The valid value is 1-9223372036854775807. Defaults to 86400.</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the OTS instance in which table will located.</p></li>
<li><p><strong>max_version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of versions stored in this table. The valid value is 1-2147483647.</p></li>
<li><p><strong>primary_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The property of <code class="docutils literal notranslate"><span class="pre">TableMeta</span></code> which indicates the structure information of a table. It describes the attribute value of primary key. The number of <code class="docutils literal notranslate"><span class="pre">primary_key</span></code> should not be less than one and not be more than four.</p></li>
<li><p><strong>table_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The table name of the OTS instance. If changed, a new table would be created.</p></li>
<li><p><strong>time_to_live</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The retention time of data stored in this table (unit: second). The value maximum is 2147483647 and -1 means never expired.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>primary_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name for primary key.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type for primary key. Only <code class="docutils literal notranslate"><span class="pre">Integer</span></code>, <code class="docutils literal notranslate"><span class="pre">String</span></code> or <code class="docutils literal notranslate"><span class="pre">Binary</span></code> is allowed.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ots.Table.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ots.Table.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ots.Table.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ots.Table.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
