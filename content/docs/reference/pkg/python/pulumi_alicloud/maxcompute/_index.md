---
title: Module maxcompute
title_tag: Module maxcompute | Package pulumi_alicloud | Python SDK
linktitle: maxcompute
notitle: true
---

<div class="section" id="maxcompute">
<h1>maxcompute<a class="headerlink" href="#maxcompute" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.maxcompute"></span><dl class="py class">
<dt id="pulumi_alicloud.maxcompute.Project">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.maxcompute.</code><code class="sig-name descname">Project</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">order_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">specification_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.maxcompute.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project is the basic unit of operation in maxcompute. It is similar to the concept of Database or Schema in traditional databases, and sets the boundary for maxcompute multi-user isolation and access control. <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/27818.html">Refer to details</a>.</p>
<p>-&gt;<strong>NOTE:</strong> Available in 1.77.0+.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the maxcompute project.</p></li>
<li><p><strong>order_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of payment, only <code class="docutils literal notranslate"><span class="pre">PayAsYouGo</span></code> supported currently.</p></li>
<li><p><strong>specification_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of resource Specification, only <code class="docutils literal notranslate"><span class="pre">OdpsStandard</span></code> supported currently.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.maxcompute.Project.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.maxcompute.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the maxcompute project.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.maxcompute.Project.order_type">
<code class="sig-name descname">order_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.maxcompute.Project.order_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of payment, only <code class="docutils literal notranslate"><span class="pre">PayAsYouGo</span></code> supported currently.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.maxcompute.Project.specification_type">
<code class="sig-name descname">specification_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.maxcompute.Project.specification_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of resource Specification, only <code class="docutils literal notranslate"><span class="pre">OdpsStandard</span></code> supported currently.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.maxcompute.Project.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">order_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">specification_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.maxcompute.Project.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Project resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the maxcompute project.</p></li>
<li><p><strong>order_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of payment, only <code class="docutils literal notranslate"><span class="pre">PayAsYouGo</span></code> supported currently.</p></li>
<li><p><strong>specification_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of resource Specification, only <code class="docutils literal notranslate"><span class="pre">OdpsStandard</span></code> supported currently.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.maxcompute.Project.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.maxcompute.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.maxcompute.Project.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.maxcompute.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
