<div class="section" id="module-pulumi_aws.pricing">
<span id="pricing"></span><h1>pricing<a class="headerlink" href="#module-pulumi_aws.pricing" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.pricing.GetProductResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.pricing.</code><code class="descname">GetProductResult</code><span class="sig-paren">(</span><em>result=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.pricing.GetProductResult" title="Permalink to this definition">¶</a></dt>
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
</dd></dl>

</div>
