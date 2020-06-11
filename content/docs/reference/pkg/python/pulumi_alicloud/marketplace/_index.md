---
title: Module marketplace
title_tag: Module marketplace | Package pulumi_alicloud | Python SDK
linktitle: marketplace
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "alicloud" >}}

<div class="section" id="marketplace">
<h1>marketplace<a class="headerlink" href="#marketplace" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.marketplace"></span><dl class="py class">
<dt id="pulumi_alicloud.marketplace.AwaitableGetProductResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.marketplace.</code><code class="sig-name descname">AwaitableGetProductResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">available_region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">products</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.marketplace.AwaitableGetProductResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.marketplace.AwaitableGetProductsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.marketplace.</code><code class="sig-name descname">AwaitableGetProductsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">category_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">products</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_term</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suggested_price</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">supplier_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">supplier_name_keyword</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.marketplace.AwaitableGetProductsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.marketplace.GetProductResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.marketplace.</code><code class="sig-name descname">GetProductResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">available_region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">products</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.marketplace.GetProductResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProduct.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.marketplace.GetProductResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.marketplace.GetProductResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.marketplace.GetProductResult.products">
<code class="sig-name descname">products</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.marketplace.GetProductResult.products" title="Permalink to this definition">¶</a></dt>
<dd><p>A product. It contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.marketplace.GetProductsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.marketplace.</code><code class="sig-name descname">GetProductsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">category_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">products</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_term</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suggested_price</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">supplier_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">supplier_name_keyword</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.marketplace.GetProductsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProducts.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.marketplace.GetProductsResult.category_id">
<code class="sig-name descname">category_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.marketplace.GetProductsResult.category_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The category id of the product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.marketplace.GetProductsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.marketplace.GetProductsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.marketplace.GetProductsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.marketplace.GetProductsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of product codes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.marketplace.GetProductsResult.products">
<code class="sig-name descname">products</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.marketplace.GetProductsResult.products" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of products. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.marketplace.GetProductsResult.suggested_price">
<code class="sig-name descname">suggested_price</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.marketplace.GetProductsResult.suggested_price" title="Permalink to this definition">¶</a></dt>
<dd><p>The suggested price of the product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.marketplace.GetProductsResult.supplier_id">
<code class="sig-name descname">supplier_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.marketplace.GetProductsResult.supplier_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The supplier id of the product.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.marketplace.Order">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.marketplace.</code><code class="sig-name descname">Order</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">coupon_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pay_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pricing_cycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quantity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.marketplace.Order" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Order resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] components: Service providers customize additional components.
:param pulumi.Input[str] coupon_id: The coupon id of the market product.
:param pulumi.Input[float] duration: The number of purchase cycles.
:param pulumi.Input[str] package_version: The package version of the market product.
:param pulumi.Input[str] pay_type: Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>,System default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.
:param pulumi.Input[str] pricing_cycle: The purchase cycle of the product, valid values are <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Month</span></code> and <code class="docutils literal notranslate"><span class="pre">Year</span></code>.
:param pulumi.Input[str] product_code: The product_code of market place product.
:param pulumi.Input[float] quantity: The quantity of the market product will be purchased.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.marketplace.Order.components">
<code class="sig-name descname">components</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.marketplace.Order.components" title="Permalink to this definition">¶</a></dt>
<dd><p>Service providers customize additional components.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.marketplace.Order.coupon_id">
<code class="sig-name descname">coupon_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.marketplace.Order.coupon_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The coupon id of the market product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.marketplace.Order.duration">
<code class="sig-name descname">duration</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.marketplace.Order.duration" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of purchase cycles.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.marketplace.Order.package_version">
<code class="sig-name descname">package_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.marketplace.Order.package_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The package version of the market product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.marketplace.Order.pay_type">
<code class="sig-name descname">pay_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.marketplace.Order.pay_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>,System default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.marketplace.Order.pricing_cycle">
<code class="sig-name descname">pricing_cycle</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.marketplace.Order.pricing_cycle" title="Permalink to this definition">¶</a></dt>
<dd><p>The purchase cycle of the product, valid values are <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Month</span></code> and <code class="docutils literal notranslate"><span class="pre">Year</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.marketplace.Order.product_code">
<code class="sig-name descname">product_code</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.marketplace.Order.product_code" title="Permalink to this definition">¶</a></dt>
<dd><p>The product_code of market place product.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.marketplace.Order.quantity">
<code class="sig-name descname">quantity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.marketplace.Order.quantity" title="Permalink to this definition">¶</a></dt>
<dd><p>The quantity of the market product will be purchased.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.marketplace.Order.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">components</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">coupon_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">package_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pay_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pricing_cycle</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">quantity</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.marketplace.Order.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Order resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>components</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Service providers customize additional components.</p></li>
<li><p><strong>coupon_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The coupon id of the market product.</p></li>
<li><p><strong>duration</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of purchase cycles.</p></li>
<li><p><strong>package_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The package version of the market product.</p></li>
<li><p><strong>pay_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Valid values are <code class="docutils literal notranslate"><span class="pre">PrePaid</span></code>, <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>,System default to <code class="docutils literal notranslate"><span class="pre">PostPaid</span></code>.</p></li>
<li><p><strong>pricing_cycle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The purchase cycle of the product, valid values are <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Month</span></code> and <code class="docutils literal notranslate"><span class="pre">Year</span></code>.</p></li>
<li><p><strong>product_code</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The product_code of market place product.</p></li>
<li><p><strong>quantity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The quantity of the market product will be purchased.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.marketplace.Order.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.marketplace.Order.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.marketplace.Order.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.marketplace.Order.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.marketplace.get_product">
<code class="sig-prename descclassname">pulumi_alicloud.marketplace.</code><code class="sig-name descname">get_product</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">available_region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product_code</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.marketplace.get_product" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the Market product item details of Alibaba Cloud.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.69.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">default</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">marketplace</span><span class="o">.</span><span class="n">get_product</span><span class="p">(</span><span class="n">product_code</span><span class="o">=</span><span class="s2">&quot;cmapi022206&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;productName&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">.</span><span class="n">products</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstProductSkuCode&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">.</span><span class="n">products</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;skuses&quot;</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;skuCode&quot;</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstProductPackageVersion&quot;</span><span class="p">,</span> <span class="n">default</span><span class="o">.</span><span class="n">products</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;skuses&quot;</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;packageVersions&quot;</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;package_version&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>available_region</strong> (<em>str</em>) – A available region id used to filter market place Ecs images.</p></li>
<li><p><strong>product_code</strong> (<em>str</em>) – The product code of the market product.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.marketplace.get_products">
<code class="sig-prename descclassname">pulumi_alicloud.marketplace.</code><code class="sig-name descname">get_products</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">category_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search_term</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suggested_price</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">supplier_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">supplier_name_keyword</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.marketplace.get_products" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides the Market product items of Alibaba Cloud.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.64.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>category_id</strong> (<em>str</em>) – The Category ID of products. For more information, see <a class="reference external" href="https://help.aliyun.com/document_detail/89834.htm">DescribeProducts</a>.</p></li>
<li><p><strong>ids</strong> (<em>list</em>) – A list of product code.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to apply to the product name.</p></li>
<li><p><strong>product_type</strong> (<em>str</em>) – The type of products, Valid values: <code class="docutils literal notranslate"><span class="pre">APP</span></code>, <code class="docutils literal notranslate"><span class="pre">SERVICE</span></code>, <code class="docutils literal notranslate"><span class="pre">MIRROR</span></code>, <code class="docutils literal notranslate"><span class="pre">DOWNLOAD</span></code> and <code class="docutils literal notranslate"><span class="pre">API_SERVICE</span></code>.</p></li>
<li><p><strong>search_term</strong> (<em>str</em>) – Search term in this query.</p></li>
<li><p><strong>sort</strong> (<em>str</em>) – This field determines how to sort the filtered results, Valid values: <code class="docutils literal notranslate"><span class="pre">user_count-desc</span></code>, <code class="docutils literal notranslate"><span class="pre">created_on-desc</span></code>, <code class="docutils literal notranslate"><span class="pre">price-desc</span></code> and <code class="docutils literal notranslate"><span class="pre">score-desc</span></code>.</p></li>
<li><p><strong>suggested_price</strong> (<em>float</em>) – The suggested price of the product.</p></li>
<li><p><strong>supplier_id</strong> (<em>str</em>) – The supplier id of the product.</p></li>
<li><p><strong>supplier_name_keyword</strong> (<em>str</em>) – The supplier name keyword of the product.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
