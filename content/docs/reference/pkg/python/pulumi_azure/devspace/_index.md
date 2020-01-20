---
title: Module devspace
title_tag: Module devspace | Package pulumi_azure | Python SDK
linktitle: devspace
notitle: true
---

<div class="section" id="devspace">
<h1>devspace<a class="headerlink" href="#devspace" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.devspace"></span><dl class="class">
<dt id="pulumi_azure.devspace.Controller">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.devspace.</code><code class="sig-name descname">Controller</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_container_host_credentials_base64=None</em>, <em class="sig-param">target_container_host_resource_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devspace.Controller" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a DevSpace Controller.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported location where the DevSpace Controller should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the DevSpace Controller. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the DevSpace Controller resource has to be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the SKU Name for this DevSpace Controller. Possible values are <code class="docutils literal notranslate"><span class="pre">S1</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>target_container_host_credentials_base64</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64 encoding of <code class="docutils literal notranslate"><span class="pre">kube_config_raw</span></code> of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>target_container_host_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource id of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the DevSpace Controller. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/devspace_controller.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/devspace_controller.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.data_plane_fqdn">
<code class="sig-name descname">data_plane_fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.data_plane_fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>DNS name for accessing DataPlane services.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.host_suffix">
<code class="sig-name descname">host_suffix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.host_suffix" title="Permalink to this definition">¶</a></dt>
<dd><p>The host suffix for the DevSpace Controller.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported location where the DevSpace Controller should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the DevSpace Controller. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group under which the DevSpace Controller resource has to be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the SKU Name for this DevSpace Controller. Possible values are <code class="docutils literal notranslate"><span class="pre">S1</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.target_container_host_credentials_base64">
<code class="sig-name descname">target_container_host_credentials_base64</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.target_container_host_credentials_base64" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64 encoding of <code class="docutils literal notranslate"><span class="pre">kube_config_raw</span></code> of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.target_container_host_resource_id">
<code class="sig-name descname">target_container_host_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.target_container_host_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource id of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.devspace.Controller.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">data_plane_fqdn=None</em>, <em class="sig-param">host_suffix=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_container_host_credentials_base64=None</em>, <em class="sig-param">target_container_host_resource_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devspace.Controller.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Controller resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data_plane_fqdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DNS name for accessing DataPlane services.</p></li>
<li><p><strong>host_suffix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The host suffix for the DevSpace Controller.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported location where the DevSpace Controller should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the DevSpace Controller. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the DevSpace Controller resource has to be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the SKU Name for this DevSpace Controller. Possible values are <code class="docutils literal notranslate"><span class="pre">S1</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>target_container_host_credentials_base64</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64 encoding of <code class="docutils literal notranslate"><span class="pre">kube_config_raw</span></code> of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>target_container_host_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource id of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the DevSpace Controller. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/devspace_controller.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/devspace_controller.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.devspace.Controller.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devspace.Controller.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.devspace.Controller.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devspace.Controller.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
