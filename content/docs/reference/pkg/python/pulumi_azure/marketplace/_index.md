---
title: Module marketplace
title_tag: Module marketplace | Package pulumi_azure | Python SDK
linktitle: marketplace
notitle: true
---

<div class="section" id="marketplace">
<h1>marketplace<a class="headerlink" href="#marketplace" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.marketplace"></span><dl class="class">
<dt id="pulumi_azure.marketplace.Agreement">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.marketplace.</code><code class="sig-name descname">Agreement</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">offer=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">publisher=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.marketplace.Agreement" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows accepting the Legal Terms for a Marketplace Image.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/marketplace_agreement.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/marketplace_agreement.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>offer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Offer of the Marketplace Image. Changing this forces a new resource to be created.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Plan of the Marketplace Image. Changing this forces a new resource to be created.</p></li>
<li><p><strong>publisher</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Publisher of the Marketplace Image. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.marketplace.Agreement.offer">
<code class="sig-name descname">offer</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.marketplace.Agreement.offer" title="Permalink to this definition">¶</a></dt>
<dd><p>The Offer of the Marketplace Image. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.marketplace.Agreement.plan">
<code class="sig-name descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.marketplace.Agreement.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>The Plan of the Marketplace Image. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.marketplace.Agreement.publisher">
<code class="sig-name descname">publisher</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.marketplace.Agreement.publisher" title="Permalink to this definition">¶</a></dt>
<dd><p>The Publisher of the Marketplace Image. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.marketplace.Agreement.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">license_text_link=None</em>, <em class="sig-param">offer=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">privacy_policy_link=None</em>, <em class="sig-param">publisher=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.marketplace.Agreement.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Agreement resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>offer</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Offer of the Marketplace Image. Changing this forces a new resource to be created.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Plan of the Marketplace Image. Changing this forces a new resource to be created.</p></li>
<li><p><strong>publisher</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Publisher of the Marketplace Image. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.marketplace.Agreement.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.marketplace.Agreement.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_azure.marketplace.Agreement.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.marketplace.Agreement.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
