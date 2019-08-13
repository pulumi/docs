---
title: Module devspace
---

<div class="section" id="devspace">
<h1>devspace<a class="headerlink" href="#devspace" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_azure.devspace"></span><dl class="class">
<dt id="pulumi_azure.devspace.Controller">
<em class="property">class </em><code class="descclassname">pulumi_azure.devspace.</code><code class="descname">Controller</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>host_suffix=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>target_container_host_credentials_base64=None</em>, <em>target_container_host_resource_id=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devspace.Controller" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a DevSpace Controller.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>host_suffix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The host suffix for the DevSpace Controller. Changing this forces a new resource to be created.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported location where the DevSpace Controller should exist. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the DevSpace Controller. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the DevSpace Controller resource has to be created. Changing this forces a new resource to be created.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as documented below. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>target_container_host_credentials_base64</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64 encoding of <code class="docutils literal notranslate"><span class="pre">kube_config_raw</span></code> of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.</li>
<li><strong>target_container_host_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource id of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/devspace_controller.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/devspace_controller.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.data_plane_fqdn">
<code class="descname">data_plane_fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.data_plane_fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>DNS name for accessing DataPlane services.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.host_suffix">
<code class="descname">host_suffix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.host_suffix" title="Permalink to this definition">¶</a></dt>
<dd><p>The host suffix for the DevSpace Controller. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported location where the DevSpace Controller should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the DevSpace Controller. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group under which the DevSpace Controller resource has to be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as documented below. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.target_container_host_credentials_base64">
<code class="descname">target_container_host_credentials_base64</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.target_container_host_credentials_base64" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64 encoding of <code class="docutils literal notranslate"><span class="pre">kube_config_raw</span></code> of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.target_container_host_resource_id">
<code class="descname">target_container_host_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.target_container_host_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource id of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_azure.devspace.Controller.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>data_plane_fqdn=None</em>, <em>host_suffix=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>target_container_host_credentials_base64=None</em>, <em>target_container_host_resource_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devspace.Controller.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Controller resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] data_plane_fqdn: DNS name for accessing DataPlane services.
:param pulumi.Input[str] host_suffix: The host suffix for the DevSpace Controller. Changing this forces a new resource to be created.
:param pulumi.Input[str] location: Specifies the supported location where the DevSpace Controller should exist. Changing this forces a new resource to be created.
:param pulumi.Input[str] name: Specifies the name of the DevSpace Controller. Changing this forces a new resource to be created.
:param pulumi.Input[str] resource_group_name: The name of the resource group under which the DevSpace Controller resource has to be created. Changing this forces a new resource to be created.
:param pulumi.Input[dict] sku: A <code class="docutils literal notranslate"><span class="pre">sku</span></code> block as documented below. Changing this forces a new resource to be created.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
:param pulumi.Input[str] target_container_host_credentials_base64: Base64 encoding of <code class="docutils literal notranslate"><span class="pre">kube_config_raw</span></code> of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.
:param pulumi.Input[str] target_container_host_resource_id: The resource id of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/devspace_controller.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/devspace_controller.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.devspace.Controller.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devspace.Controller.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.devspace.Controller.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devspace.Controller.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

</div>
