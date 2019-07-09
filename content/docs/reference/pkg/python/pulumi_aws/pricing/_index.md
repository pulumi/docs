---
---

<div class="section" id="pricing">
<h1>pricing<a class="headerlink" href="#pricing" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.pricing"></span><dl class="class">
<dt id="pulumi_aws.pricing.GetProductResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.pricing.</code><code class="descname">GetProductResult</code><span class="sig-paren">(</span><em>filters=None</em>, <em>result=None</em>, <em>service_code=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pricing.GetProductResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProduct.</p>
<dl class="attribute">
<dt id="pulumi_aws.pricing.GetProductResult.result">
<code class="descname">result</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pricing.GetProductResult.result" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the product returned from the API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.pricing.GetProductResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.pricing.GetProductResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_aws.pricing.get_product">
<code class="descclassname">pulumi_aws.pricing.</code><code class="descname">get_product</code><span class="sig-paren">(</span><em>filters=None</em>, <em>service_code=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pricing.get_product" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the pricing information of all products in AWS.
This data source is only available in a us-east-1 or ap-south-1 provider.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/pricing_product.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/pricing_product.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
