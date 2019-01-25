<div class="section" id="module-pulumi_azure.devspace">
<span id="devspace"></span><h1>devspace<a class="headerlink" href="#module-pulumi_azure.devspace" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.devspace.Controller">
<em class="property">class </em><code class="descclassname">pulumi_azure.devspace.</code><code class="descname">Controller</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>host_suffix=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>target_container_host_credentials_base64=None</em>, <em>target_container_host_resource_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devspace.Controller" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a DevSpace Controller.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>host_suffix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The host suffix for the DevSpace Controller. Changing this forces a new resource to be created.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported location where the DevSpace Controller should exist. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the DevSpace Controller. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the DevSpace Controller resource has to be created. Changing this forces a new resource to be created.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>sku</cite> block as documented below. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>target_container_host_credentials_base64</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base64 encoding of <cite>kube_config_raw</cite> of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.</li>
<li><strong>target_container_host_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource id of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
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
<dd><p>A <cite>sku</cite> block as documented below. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.target_container_host_credentials_base64">
<code class="descname">target_container_host_credentials_base64</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.target_container_host_credentials_base64" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64 encoding of <cite>kube_config_raw</cite> of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devspace.Controller.target_container_host_resource_id">
<code class="descname">target_container_host_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devspace.Controller.target_container_host_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource id of Azure Kubernetes Service cluster. Changing this forces a new resource to be created.</p>
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
