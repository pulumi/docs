---
title: Module mediastore
title_tag: Module mediastore | Package pulumi_aws | Python SDK
linktitle: mediastore
notitle: true
---

<div class="section" id="mediastore">
<h1>mediastore<a class="headerlink" href="#mediastore" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.mediastore"></span><dl class="py class">
<dt id="pulumi_aws.mediastore.Container">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.mediastore.</code><code class="sig-name descname">Container</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediastore.Container" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a MediaStore Container.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">mediastore</span><span class="o">.</span><span class="n">Container</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the container. Must contain alphanumeric characters or underscores.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.mediastore.Container.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediastore.Container.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the container.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.mediastore.Container.endpoint">
<code class="sig-name descname">endpoint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediastore.Container.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS endpoint of the container.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.mediastore.Container.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediastore.Container.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the container. Must contain alphanumeric characters or underscores.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.mediastore.Container.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediastore.Container.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.mediastore.Container.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediastore.Container.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Container resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the container.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS endpoint of the container.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the container. Must contain alphanumeric characters or underscores.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.mediastore.Container.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediastore.Container.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.mediastore.Container.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediastore.Container.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.mediastore.ContainerPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.mediastore.</code><code class="sig-name descname">ContainerPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediastore.ContainerPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a MediaStore Container Policy.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">current_region</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_region</span><span class="p">()</span>
<span class="n">current_caller_identity</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">get_caller_identity</span><span class="p">()</span>
<span class="n">example_container</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">mediastore</span><span class="o">.</span><span class="n">Container</span><span class="p">(</span><span class="s2">&quot;exampleContainer&quot;</span><span class="p">)</span>
<span class="n">example_container_policy</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">mediastore</span><span class="o">.</span><span class="n">ContainerPolicy</span><span class="p">(</span><span class="s2">&quot;exampleContainerPolicy&quot;</span><span class="p">,</span>
    <span class="n">container_name</span><span class="o">=</span><span class="n">example_container</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">policy</span><span class="o">=</span><span class="n">example_container</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">name</span><span class="p">:</span> <span class="sa">f</span><span class="s2">&quot;&quot;&quot;</span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">        &quot;Version&quot;: &quot;2012-10-17&quot;,</span>
<span class="s2">        &quot;Statement&quot;: [</span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                &quot;Sid&quot;: &quot;MediaStoreFullAccess&quot;,</span>
<span class="s2">                &quot;Action&quot;: [ &quot;mediastore:*&quot; ],</span>
<span class="s2">                &quot;Principal&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2">&quot;AWS&quot; : &quot;arn:aws:iam::</span><span class="si">{</span><span class="n">current_caller_identity</span><span class="o">.</span><span class="n">account_id</span><span class="si">}</span><span class="s2">:root&quot;</span><span class="se">&#x7D;&#x7D;</span><span class="s2">,</span>
<span class="s2">                &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">                &quot;Resource&quot;: &quot;arn:aws:mediastore:</span><span class="si">{</span><span class="n">current_caller_identity</span><span class="o">.</span><span class="n">account_id</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="n">current_region</span><span class="o">.</span><span class="n">name</span><span class="si">}</span><span class="s2">:container/</span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s2">/*&quot;,</span>
<span class="s2">                &quot;Condition&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">                        &quot;Bool&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"> &quot;aws:SecureTransport&quot;: &quot;true&quot; </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">                </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">        </span><span class="se">&#x7D;&#x7D;</span><span class="s2">]</span>
<span class="se">&#x7D;&#x7D;</span><span class="s2"></span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the container.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of the policy.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.mediastore.ContainerPolicy.container_name">
<code class="sig-name descname">container_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediastore.ContainerPolicy.container_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the container.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.mediastore.ContainerPolicy.policy">
<code class="sig-name descname">policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.mediastore.ContainerPolicy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The contents of the policy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.mediastore.ContainerPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediastore.ContainerPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ContainerPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the container.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The contents of the policy.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.mediastore.ContainerPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediastore.ContainerPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.mediastore.ContainerPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.mediastore.ContainerPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
