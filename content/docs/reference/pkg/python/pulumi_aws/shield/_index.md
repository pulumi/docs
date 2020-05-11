---
title: Module shield
title_tag: Module shield | Package pulumi_aws | Python SDK
linktitle: shield
notitle: true
---

<div class="section" id="shield">
<h1>shield<a class="headerlink" href="#shield" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.shield"></span><dl class="py class">
<dt id="pulumi_aws.shield.Protection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.shield.</code><code class="sig-name descname">Protection</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.shield.Protection" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables AWS Shield Advanced for a specific AWS resource.
The resource can be an Amazon CloudFront distribution, Elastic Load Balancing load balancer, AWS Global Accelerator accelerator, Elastic IP Address, or an Amazon Route 53 hosted zone.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">available</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_availability_zones</span><span class="p">()</span>
<span class="n">current_region</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_region</span><span class="p">()</span>
<span class="n">current_caller_identity</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_caller_identity</span><span class="p">()</span>
<span class="n">foo_eip</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">Eip</span><span class="p">(</span><span class="s2">&quot;fooEip&quot;</span><span class="p">,</span> <span class="n">vpc</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">foo_protection</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">shield</span><span class="o">.</span><span class="n">Protection</span><span class="p">(</span><span class="s2">&quot;fooProtection&quot;</span><span class="p">,</span> <span class="n">resource_arn</span><span class="o">=</span><span class="n">foo_eip</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="sa">f</span><span class="s2">&quot;arn:aws:ec2:</span><span class="si">{</span><span class="n">current_region</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="n">current_caller_identity</span><span class="o">.</span><span class="n">account_id</span><span class="si">}</span><span class="s2">:eip-allocation/</span><span class="si">{</span><span class="nb">id</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for the Protection you are creating.</p></li>
<li><p><strong>resource_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN (Amazon Resource Name) of the resource to be protected.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.shield.Protection.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.shield.Protection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A friendly name for the Protection you are creating.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.shield.Protection.resource_arn">
<code class="sig-name descname">resource_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.shield.Protection.resource_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN (Amazon Resource Name) of the resource to be protected.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.shield.Protection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_arn</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.shield.Protection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Protection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A friendly name for the Protection you are creating.</p></li>
<li><p><strong>resource_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN (Amazon Resource Name) of the resource to be protected.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.shield.Protection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.shield.Protection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.shield.Protection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.shield.Protection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
