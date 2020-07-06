---
title: Module eci
title_tag: Module eci | Package pulumi_alicloud | Python SDK
linktitle: eci
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "alicloud" >}}

<div class="section" id="eci">
<h1>eci<a class="headerlink" href="#eci" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.eci"></span><dl class="py class">
<dt id="pulumi_alicloud.eci.OpenApiImageCache">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.eci.</code><code class="sig-name descname">OpenApiImageCache</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">eip_instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_cache_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_cache_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_registry_credentials</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">images</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.eci.OpenApiImageCache" title="Permalink to this definition">¶</a></dt>
<dd><p>An ECI Image Cache can help user to solve the time-consuming problem of image pull. For information about Alicloud ECI Image Cache and how to use it, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/146891.htm">What is Resource Alicloud ECI Image Cache</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in v1.89.0+.</p>
<p><strong>NOTE:</strong> Each image cache corresponds to a snapshot, and the user does not delete the snapshot directly, otherwise the cache will fail.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>eip_instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The instance ID of the Elastic IP Address (EIP). If you want to pull images from the Internet, you must specify an EIP to make sure that the container group can access the Internet. You can also configure the network address translation (NAT) gateway. We recommend that you configure the NAT gateway for the Internet access. Refer to <a class="reference external" href="https://help.aliyun.com/document_detail/99146.html">Public Network Access Method</a></p></li>
<li><p><strong>image_cache_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the image cache.</p></li>
<li><p><strong>image_cache_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the image cache. Default to <code class="docutils literal notranslate"><span class="pre">20</span></code>. Unit: GiB.</p></li>
<li><p><strong>image_registry_credentials</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The Image Registry parameters about the image to be cached.</p></li>
<li><p><strong>images</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The images to be cached. The image name must be versioned.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resource group.</p></li>
<li><p><strong>retention_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The retention days of the image cache. Once the image cache expires, it will be cleared. By default, the image cache never expires. Note: The image cache that fails to be created is retained for only one day.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the security group. You do not need to specify the same security group as the container group.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VSwitch. You do not need to specify the same VSwitch as the container group.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone id to cache image.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>image_registry_credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password of the Image Registry.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The address of Image Registry without <code class="docutils literal notranslate"><span class="pre">http://</span></code> or <code class="docutils literal notranslate"><span class="pre">https://</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user name of Image Registry.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.eci.OpenApiImageCache.container_group_id">
<code class="sig-name descname">container_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.eci.OpenApiImageCache.container_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the container group job that is used to create the image cache.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> -The status of the image cache.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.eci.OpenApiImageCache.eip_instance_id">
<code class="sig-name descname">eip_instance_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.eci.OpenApiImageCache.eip_instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The instance ID of the Elastic IP Address (EIP). If you want to pull images from the Internet, you must specify an EIP to make sure that the container group can access the Internet. You can also configure the network address translation (NAT) gateway. We recommend that you configure the NAT gateway for the Internet access. Refer to <a class="reference external" href="https://help.aliyun.com/document_detail/99146.html">Public Network Access Method</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.eci.OpenApiImageCache.image_cache_name">
<code class="sig-name descname">image_cache_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.eci.OpenApiImageCache.image_cache_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the image cache.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.eci.OpenApiImageCache.image_cache_size">
<code class="sig-name descname">image_cache_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.eci.OpenApiImageCache.image_cache_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the image cache. Default to <code class="docutils literal notranslate"><span class="pre">20</span></code>. Unit: GiB.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.eci.OpenApiImageCache.image_registry_credentials">
<code class="sig-name descname">image_registry_credentials</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.eci.OpenApiImageCache.image_registry_credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>The Image Registry parameters about the image to be cached.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password of the Image Registry.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The address of Image Registry without <code class="docutils literal notranslate"><span class="pre">http://</span></code> or <code class="docutils literal notranslate"><span class="pre">https://</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The user name of Image Registry.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.eci.OpenApiImageCache.images">
<code class="sig-name descname">images</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.eci.OpenApiImageCache.images" title="Permalink to this definition">¶</a></dt>
<dd><p>The images to be cached. The image name must be versioned.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.eci.OpenApiImageCache.resource_group_id">
<code class="sig-name descname">resource_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.eci.OpenApiImageCache.resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the resource group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.eci.OpenApiImageCache.retention_days">
<code class="sig-name descname">retention_days</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.eci.OpenApiImageCache.retention_days" title="Permalink to this definition">¶</a></dt>
<dd><p>The retention days of the image cache. Once the image cache expires, it will be cleared. By default, the image cache never expires. Note: The image cache that fails to be created is retained for only one day.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.eci.OpenApiImageCache.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.eci.OpenApiImageCache.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the security group. You do not need to specify the same security group as the container group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.eci.OpenApiImageCache.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.eci.OpenApiImageCache.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the VSwitch. You do not need to specify the same VSwitch as the container group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.eci.OpenApiImageCache.zone_id">
<code class="sig-name descname">zone_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.eci.OpenApiImageCache.zone_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone id to cache image.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.eci.OpenApiImageCache.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">eip_instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_cache_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_cache_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_registry_credentials</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">images</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.eci.OpenApiImageCache.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OpenApiImageCache resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>container_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the container group job that is used to create the image cache.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `status` -The status of the image cache.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>eip_instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The instance ID of the Elastic IP Address (EIP). If you want to pull images from the Internet, you must specify an EIP to make sure that the container group can access the Internet. You can also configure the network address translation (NAT) gateway. We recommend that you configure the NAT gateway for the Internet access. Refer to <a class="reference external" href="https://help.aliyun.com/document_detail/99146.html">Public Network Access Method</a></p>
</p></li>
<li><p><strong>image_cache_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the image cache.</p></li>
<li><p><strong>image_cache_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the image cache. Default to <code class="docutils literal notranslate"><span class="pre">20</span></code>. Unit: GiB.</p></li>
<li><p><strong>image_registry_credentials</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The Image Registry parameters about the image to be cached.</p></li>
<li><p><strong>images</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The images to be cached. The image name must be versioned.</p></li>
<li><p><strong>resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resource group.</p></li>
<li><p><strong>retention_days</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The retention days of the image cache. Once the image cache expires, it will be cleared. By default, the image cache never expires. Note: The image cache that fails to be created is retained for only one day.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the security group. You do not need to specify the same security group as the container group.</p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the VSwitch. You do not need to specify the same VSwitch as the container group.</p></li>
<li><p><strong>zone_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone id to cache image.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>image_registry_credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password of the Image Registry.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The address of Image Registry without <code class="docutils literal notranslate"><span class="pre">http://</span></code> or <code class="docutils literal notranslate"><span class="pre">https://</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">user_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user name of Image Registry.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.eci.OpenApiImageCache.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.eci.OpenApiImageCache.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.eci.OpenApiImageCache.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.eci.OpenApiImageCache.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
