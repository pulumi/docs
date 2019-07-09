---
---

<div class="section" id="module-pulumi_azure.servicefabric">
<span id="servicefabric"></span><h1>servicefabric<a class="headerlink" href="#module-pulumi_azure.servicefabric" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.servicefabric.Cluster">
<em class="property">class </em><code class="descclassname">pulumi_azure.servicefabric.</code><code class="descname">Cluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>add_on_features=None</em>, <em>azure_active_directory=None</em>, <em>certificate=None</em>, <em>certificate_common_names=None</em>, <em>client_certificate_thumbprints=None</em>, <em>cluster_code_version=None</em>, <em>diagnostics_config=None</em>, <em>fabric_settings=None</em>, <em>location=None</em>, <em>management_endpoint=None</em>, <em>name=None</em>, <em>node_types=None</em>, <em>reliability_level=None</em>, <em>resource_group_name=None</em>, <em>reverse_proxy_certificate=None</em>, <em>tags=None</em>, <em>upgrade_mode=None</em>, <em>vm_image=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a Service Fabric Cluster.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>add_on_features</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A List of one or more features which should be enabled, such as <code class="docutils literal notranslate"><span class="pre">DnsService</span></code>.</li>
<li><strong>azure_active_directory</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">azure_active_directory</span></code> block as defined below.</li>
<li><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">certificate</span></code> block as defined below. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_common_names</span></code>.</li>
<li><strong>certificate_common_names</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">certificate_common_names</span></code> block as defined below. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate</span></code>.</li>
<li><strong>client_certificate_thumbprints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or two <code class="docutils literal notranslate"><span class="pre">client_certificate_thumbprint</span></code> blocks as defined below.</li>
<li><strong>cluster_code_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required if Upgrade Mode set to <code class="docutils literal notranslate"><span class="pre">Manual</span></code>, Specifies the Version of the Cluster Code of the cluster.</li>
<li><strong>diagnostics_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">diagnostics_config</span></code> block as defined below. Changing this forces a new resource to be created.</li>
<li><strong>fabric_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">fabric_settings</span></code> blocks as defined below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>management_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Management Endpoint of the cluster such as <code class="docutils literal notranslate"><span class="pre">http://example.com</span></code>. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Service Fabric Cluster. Changing this forces a new resource to be created.</li>
<li><strong>node_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">node_type</span></code> blocks as defined below.</li>
<li><strong>reliability_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Reliability Level of the Cluster. Possible values include <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Bronze</span></code>, <code class="docutils literal notranslate"><span class="pre">Silver</span></code>, <code class="docutils literal notranslate"><span class="pre">Gold</span></code> and <code class="docutils literal notranslate"><span class="pre">Platinum</span></code>.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.</li>
<li><strong>reverse_proxy_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">reverse_proxy_certificate</span></code> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>upgrade_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Upgrade Mode of the cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Automatic</span></code> or <code class="docutils literal notranslate"><span class="pre">Manual</span></code>.</li>
<li><strong>vm_image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Image expected for the Service Fabric Cluster, such as <code class="docutils literal notranslate"><span class="pre">Windows</span></code>. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/service_fabric_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/service_fabric_cluster.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.add_on_features">
<code class="descname">add_on_features</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.add_on_features" title="Permalink to this definition">¶</a></dt>
<dd><p>A List of one or more features which should be enabled, such as <code class="docutils literal notranslate"><span class="pre">DnsService</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.azure_active_directory">
<code class="descname">azure_active_directory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.azure_active_directory" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">azure_active_directory</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.certificate">
<code class="descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">certificate</span></code> block as defined below. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_common_names</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.certificate_common_names">
<code class="descname">certificate_common_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.certificate_common_names" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">certificate_common_names</span></code> block as defined below. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.client_certificate_thumbprints">
<code class="descname">client_certificate_thumbprints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.client_certificate_thumbprints" title="Permalink to this definition">¶</a></dt>
<dd><p>One or two <code class="docutils literal notranslate"><span class="pre">client_certificate_thumbprint</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.cluster_code_version">
<code class="descname">cluster_code_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.cluster_code_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Required if Upgrade Mode set to <code class="docutils literal notranslate"><span class="pre">Manual</span></code>, Specifies the Version of the Cluster Code of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.cluster_endpoint">
<code class="descname">cluster_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.cluster_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Cluster Endpoint for this Service Fabric Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.diagnostics_config">
<code class="descname">diagnostics_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.diagnostics_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">diagnostics_config</span></code> block as defined below. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.fabric_settings">
<code class="descname">fabric_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.fabric_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">fabric_settings</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.management_endpoint">
<code class="descname">management_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.management_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Management Endpoint of the cluster such as <code class="docutils literal notranslate"><span class="pre">http://example.com</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Service Fabric Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.node_types">
<code class="descname">node_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.node_types" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">node_type</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.reliability_level">
<code class="descname">reliability_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.reliability_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Reliability Level of the Cluster. Possible values include <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Bronze</span></code>, <code class="docutils literal notranslate"><span class="pre">Silver</span></code>, <code class="docutils literal notranslate"><span class="pre">Gold</span></code> and <code class="docutils literal notranslate"><span class="pre">Platinum</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.reverse_proxy_certificate">
<code class="descname">reverse_proxy_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.reverse_proxy_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">reverse_proxy_certificate</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.upgrade_mode">
<code class="descname">upgrade_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.upgrade_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Upgrade Mode of the cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Automatic</span></code> or <code class="docutils literal notranslate"><span class="pre">Manual</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.vm_image">
<code class="descname">vm_image</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.vm_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Image expected for the Service Fabric Cluster, such as <code class="docutils literal notranslate"><span class="pre">Windows</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.servicefabric.Cluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicefabric.Cluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
