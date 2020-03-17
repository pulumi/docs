---
title: Module hpc
title_tag: Module hpc | Package pulumi_azure | Python SDK
linktitle: hpc
notitle: true
---

<div class="section" id="hpc">
<h1>hpc<a class="headerlink" href="#hpc" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.hpc"></span><dl class="class">
<dt id="pulumi_azure.hpc.Cache">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.hpc.</code><code class="sig-name descname">Cache</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cache_size_in_gb=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hpc.Cache" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HPC Cache.</p>
<blockquote>
<div><p><strong>Note</strong>: During the first several months of the GA release, a request must be made to the Azure HPC Cache team to add your subscription to the access list before it can be used to create a cache instance. Fill out <a class="reference external" href="https://aka.ms/onboard-hpc-cache">this form</a> to request access.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hpc_cache.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/hpc_cache.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cache_size_in_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the HPC Cache, in GB. Possible values are <code class="docutils literal notranslate"><span class="pre">3072</span></code>, <code class="docutils literal notranslate"><span class="pre">6144</span></code>, <code class="docutils literal notranslate"><span class="pre">12288</span></code>, <code class="docutils literal notranslate"><span class="pre">24576</span></code>, and <code class="docutils literal notranslate"><span class="pre">49152</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure Region where the HPC Cache should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the HPC Cache. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which to create the HPC Cache. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU of HPC Cache to use. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard_2G</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_4G</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard_8G</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet for the HPC Cache. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.hpc.Cache.cache_size_in_gb">
<code class="sig-name descname">cache_size_in_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hpc.Cache.cache_size_in_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the HPC Cache, in GB. Possible values are <code class="docutils literal notranslate"><span class="pre">3072</span></code>, <code class="docutils literal notranslate"><span class="pre">6144</span></code>, <code class="docutils literal notranslate"><span class="pre">12288</span></code>, <code class="docutils literal notranslate"><span class="pre">24576</span></code>, and <code class="docutils literal notranslate"><span class="pre">49152</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hpc.Cache.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hpc.Cache.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure Region where the HPC Cache should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hpc.Cache.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hpc.Cache.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the HPC Cache. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hpc.Cache.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hpc.Cache.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which to create the HPC Cache. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hpc.Cache.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hpc.Cache.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU of HPC Cache to use. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard_2G</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_4G</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard_8G</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hpc.Cache.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hpc.Cache.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Subnet for the HPC Cache. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hpc.Cache.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cache_size_in_gb=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">subnet_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hpc.Cache.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cache resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cache_size_in_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the HPC Cache, in GB. Possible values are <code class="docutils literal notranslate"><span class="pre">3072</span></code>, <code class="docutils literal notranslate"><span class="pre">6144</span></code>, <code class="docutils literal notranslate"><span class="pre">12288</span></code>, <code class="docutils literal notranslate"><span class="pre">24576</span></code>, and <code class="docutils literal notranslate"><span class="pre">49152</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure Region where the HPC Cache should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the HPC Cache. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which to create the HPC Cache. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU of HPC Cache to use. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard_2G</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard_4G</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard_8G</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet for the HPC Cache. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hpc.Cache.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hpc.Cache.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hpc.Cache.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hpc.Cache.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
