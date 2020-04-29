---
title: Module pricing
title_tag: Module pricing | Package pulumi_aws | Python SDK
linktitle: pricing
notitle: true
---

<div class="section" id="pricing">
<h1>pricing<a class="headerlink" href="#pricing" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.pricing"></span><dl class="class">
<dt id="pulumi_aws.pricing.AwaitableGetProductResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.pricing.</code><code class="sig-name descname">AwaitableGetProductResult</code><span class="sig-paren">(</span><em class="sig-param">filters=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">result=None</em>, <em class="sig-param">service_code=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pricing.AwaitableGetProductResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.pricing.GetProductResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.pricing.</code><code class="sig-name descname">GetProductResult</code><span class="sig-paren">(</span><em class="sig-param">filters=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">result=None</em>, <em class="sig-param">service_code=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pricing.GetProductResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProduct.</p>
<dl class="attribute">
<dt id="pulumi_aws.pricing.GetProductResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pricing.GetProductResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pricing.GetProductResult.result">
<code class="sig-name descname">result</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pricing.GetProductResult.result" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the product returned from the API.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.pricing.get_product">
<code class="sig-prename descclassname">pulumi_aws.pricing.</code><code class="sig-name descname">get_product</code><span class="sig-paren">(</span><em class="sig-param">filters=None</em>, <em class="sig-param">service_code=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pricing.get_product" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the pricing information of all products in AWS.
This data source is only available in a us-east-1 or ap-south-1 provider.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filters</strong> (<em>list</em>) – A list of filters. Passed directly to the API (see GetProducts API reference). These filters must describe a single product, this resource will fail if more than one product is returned by the API.</p></li>
<li><p><strong>service_code</strong> (<em>str</em>) – The code of the service. Available service codes can be fetched using the DescribeServices pricing API call.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">field</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The product attribute name that you want to filter on.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The product attribute value that you want to filter on.</p></li>
</ul>
</dd></dl>

</div>
