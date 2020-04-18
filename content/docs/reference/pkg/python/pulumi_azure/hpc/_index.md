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
<dt id="pulumi_azure.hpc.Cache.mount_addresses">
<code class="sig-name descname">mount_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hpc.Cache.mount_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of IP Addresses where the HPC Cache can be mounted.</p>
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
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cache_size_in_gb=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">mount_addresses=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">subnet_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hpc.Cache.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>mount_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of IP Addresses where the HPC Cache can be mounted.</p></li>
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

<dl class="class">
<dt id="pulumi_azure.hpc.CacheBlobTarget">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.hpc.</code><code class="sig-name descname">CacheBlobTarget</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cache_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_path=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_container_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hpc.CacheBlobTarget" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Blob Target within a HPC Cache.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cache_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name HPC Cache, which the HPC Cache Blob Target will be added to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the HPC Cache Blob Target. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client-facing file path of the HPC Cache Blob Target.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which to create the HPC Cache Blob Target. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_container_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Resource Manager ID of the Storage Container used as the HPC Cache Blob Target. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.hpc.CacheBlobTarget.cache_name">
<code class="sig-name descname">cache_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hpc.CacheBlobTarget.cache_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name HPC Cache, which the HPC Cache Blob Target will be added to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hpc.CacheBlobTarget.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hpc.CacheBlobTarget.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the HPC Cache Blob Target. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hpc.CacheBlobTarget.namespace_path">
<code class="sig-name descname">namespace_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hpc.CacheBlobTarget.namespace_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The client-facing file path of the HPC Cache Blob Target.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hpc.CacheBlobTarget.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hpc.CacheBlobTarget.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which to create the HPC Cache Blob Target. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hpc.CacheBlobTarget.storage_container_id">
<code class="sig-name descname">storage_container_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hpc.CacheBlobTarget.storage_container_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Resource Manager ID of the Storage Container used as the HPC Cache Blob Target. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hpc.CacheBlobTarget.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cache_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_path=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_container_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hpc.CacheBlobTarget.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CacheBlobTarget resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cache_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name HPC Cache, which the HPC Cache Blob Target will be added to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the HPC Cache Blob Target. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client-facing file path of the HPC Cache Blob Target.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which to create the HPC Cache Blob Target. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_container_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Resource Manager ID of the Storage Container used as the HPC Cache Blob Target. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hpc.CacheBlobTarget.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hpc.CacheBlobTarget.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hpc.CacheBlobTarget.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hpc.CacheBlobTarget.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.hpc.CacheNfsTarget">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.hpc.</code><code class="sig-name descname">CacheNfsTarget</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cache_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_junctions=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">target_host_name=None</em>, <em class="sig-param">usage_model=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hpc.CacheNfsTarget" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a NFS Target within a HPC Cache.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cache_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name HPC Cache, which the HPC Cache NFS Target will be added to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the HPC Cache NFS Target. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_junctions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Can be specified multiple times to define multiple <code class="docutils literal notranslate"><span class="pre">namespace_junction</span></code>. Each <code class="docutils literal notranslate"><span class="pre">namespace_juntion</span></code> block supports fields documented below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which to create the HPC Cache NFS Target. Changing this forces a new resource to be created.</p></li>
<li><p><strong>target_host_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address or fully qualified domain name (FQDN) of the HPC Cache NFS target. Changing this forces a new resource to be created.</p></li>
<li><p><strong>usage_model</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of usage of the HPC Cache NFS Target.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>namespace_junctions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">namespace_path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client-facing file path of this NFS target within the HPC Cache NFS Target.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nfsExport</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The NFS export of this NFS target within the HPC Cache NFS Target.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The relative subdirectory path from the <code class="docutils literal notranslate"><span class="pre">nfs_export</span></code> to map to the <code class="docutils literal notranslate"><span class="pre">namespace_path</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>, in which case the whole <code class="docutils literal notranslate"><span class="pre">nfs_export</span></code> is exported.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.hpc.CacheNfsTarget.cache_name">
<code class="sig-name descname">cache_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hpc.CacheNfsTarget.cache_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name HPC Cache, which the HPC Cache NFS Target will be added to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hpc.CacheNfsTarget.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hpc.CacheNfsTarget.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the HPC Cache NFS Target. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hpc.CacheNfsTarget.namespace_junctions">
<code class="sig-name descname">namespace_junctions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hpc.CacheNfsTarget.namespace_junctions" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be specified multiple times to define multiple <code class="docutils literal notranslate"><span class="pre">namespace_junction</span></code>. Each <code class="docutils literal notranslate"><span class="pre">namespace_juntion</span></code> block supports fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">namespace_path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The client-facing file path of this NFS target within the HPC Cache NFS Target.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nfsExport</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The NFS export of this NFS target within the HPC Cache NFS Target.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The relative subdirectory path from the <code class="docutils literal notranslate"><span class="pre">nfs_export</span></code> to map to the <code class="docutils literal notranslate"><span class="pre">namespace_path</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>, in which case the whole <code class="docutils literal notranslate"><span class="pre">nfs_export</span></code> is exported.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hpc.CacheNfsTarget.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hpc.CacheNfsTarget.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which to create the HPC Cache NFS Target. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hpc.CacheNfsTarget.target_host_name">
<code class="sig-name descname">target_host_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hpc.CacheNfsTarget.target_host_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address or fully qualified domain name (FQDN) of the HPC Cache NFS target. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.hpc.CacheNfsTarget.usage_model">
<code class="sig-name descname">usage_model</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.hpc.CacheNfsTarget.usage_model" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of usage of the HPC Cache NFS Target.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hpc.CacheNfsTarget.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cache_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">namespace_junctions=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">target_host_name=None</em>, <em class="sig-param">usage_model=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hpc.CacheNfsTarget.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CacheNfsTarget resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cache_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name HPC Cache, which the HPC Cache NFS Target will be added to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the HPC Cache NFS Target. Changing this forces a new resource to be created.</p></li>
<li><p><strong>namespace_junctions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Can be specified multiple times to define multiple <code class="docutils literal notranslate"><span class="pre">namespace_junction</span></code>. Each <code class="docutils literal notranslate"><span class="pre">namespace_juntion</span></code> block supports fields documented below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which to create the HPC Cache NFS Target. Changing this forces a new resource to be created.</p></li>
<li><p><strong>target_host_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address or fully qualified domain name (FQDN) of the HPC Cache NFS target. Changing this forces a new resource to be created.</p></li>
<li><p><strong>usage_model</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of usage of the HPC Cache NFS Target.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>namespace_junctions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">namespace_path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The client-facing file path of this NFS target within the HPC Cache NFS Target.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nfsExport</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The NFS export of this NFS target within the HPC Cache NFS Target.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The relative subdirectory path from the <code class="docutils literal notranslate"><span class="pre">nfs_export</span></code> to map to the <code class="docutils literal notranslate"><span class="pre">namespace_path</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">&quot;&quot;</span></code>, in which case the whole <code class="docutils literal notranslate"><span class="pre">nfs_export</span></code> is exported.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.hpc.CacheNfsTarget.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hpc.CacheNfsTarget.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.hpc.CacheNfsTarget.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.hpc.CacheNfsTarget.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
