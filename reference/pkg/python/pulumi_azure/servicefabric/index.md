<div class="section" id="module-pulumi_azure.servicefabric">
<span id="servicefabric"></span><h1>servicefabric<a class="headerlink" href="#module-pulumi_azure.servicefabric" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.servicefabric.Cluster">
<em class="property">class </em><code class="descclassname">pulumi_azure.servicefabric.</code><code class="descname">Cluster</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>add_on_features=None</em>, <em>azure_active_directory=None</em>, <em>certificate=None</em>, <em>client_certificate_thumbprints=None</em>, <em>cluster_code_version=None</em>, <em>diagnostics_config=None</em>, <em>fabric_settings=None</em>, <em>location=None</em>, <em>management_endpoint=None</em>, <em>name=None</em>, <em>node_types=None</em>, <em>reliability_level=None</em>, <em>resource_group_name=None</em>, <em>reverse_proxy_certificate=None</em>, <em>tags=None</em>, <em>upgrade_mode=None</em>, <em>vm_image=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a Service Fabric Cluster.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<em>pulumi.ResourceOptions</em>) – Options for the resource.</li>
<li><strong>add_on_features</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A List of one or more features which should be enabled, such as <cite>DnsService</cite>.</li>
<li><strong>azure_active_directory</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <cite>azure_active_directory</cite> block as defined below. Changing this forces a new resource to be created.</li>
<li><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>certificate</cite> block as defined below.</li>
<li><strong>client_certificate_thumbprints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or two <cite>client_certificate_thumbprint</cite> blocks as defined below.</li>
<li><strong>cluster_code_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required if Upgrade Mode set to <cite>Manual</cite>, Specifies the Version of the Cluster Code of the cluster.</li>
<li><strong>diagnostics_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>diagnostics_config</cite> block as defined below. Changing this forces a new resource to be created.</li>
<li><strong>fabric_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <cite>fabric_settings</cite> blocks as defined below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>management_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Management Endpoint of the cluster such as <cite>http://example.com</cite>. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Service Fabric Cluster. Changing this forces a new resource to be created.</li>
<li><strong>node_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <cite>node_type</cite> blocks as defined below.</li>
<li><strong>reliability_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Reliability Level of the Cluster. Possible values include <cite>None</cite>, <cite>Bronze</cite>, <cite>Silver</cite>, <cite>Gold</cite> and <cite>Platinum</cite>.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.</li>
<li><strong>reverse_proxy_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>reverse_proxy_certificate</cite> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>upgrade_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Upgrade Mode of the cluster. Possible values are <cite>Automatic</cite> or <cite>Manual</cite>.</li>
<li><strong>vm_image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Image expected for the Service Fabric Cluster, such as <cite>Windows</cite>. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.add_on_features">
<code class="descname">add_on_features</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.add_on_features" title="Permalink to this definition">¶</a></dt>
<dd><p>A List of one or more features which should be enabled, such as <cite>DnsService</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.azure_active_directory">
<code class="descname">azure_active_directory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.azure_active_directory" title="Permalink to this definition">¶</a></dt>
<dd><p>An <cite>azure_active_directory</cite> block as defined below. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.certificate">
<code class="descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>certificate</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.client_certificate_thumbprints">
<code class="descname">client_certificate_thumbprints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.client_certificate_thumbprints" title="Permalink to this definition">¶</a></dt>
<dd><p>One or two <cite>client_certificate_thumbprint</cite> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.cluster_code_version">
<code class="descname">cluster_code_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.cluster_code_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Required if Upgrade Mode set to <cite>Manual</cite>, Specifies the Version of the Cluster Code of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.cluster_endpoint">
<code class="descname">cluster_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.cluster_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Cluster Endpoint for this Service Fabric Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.diagnostics_config">
<code class="descname">diagnostics_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.diagnostics_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>diagnostics_config</cite> block as defined below. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.fabric_settings">
<code class="descname">fabric_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.fabric_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>fabric_settings</cite> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.management_endpoint">
<code class="descname">management_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.management_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Management Endpoint of the cluster such as <cite>http://example.com</cite>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Service Fabric Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.node_types">
<code class="descname">node_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.node_types" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>node_type</cite> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.reliability_level">
<code class="descname">reliability_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.reliability_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Reliability Level of the Cluster. Possible values include <cite>None</cite>, <cite>Bronze</cite>, <cite>Silver</cite>, <cite>Gold</cite> and <cite>Platinum</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.reverse_proxy_certificate">
<code class="descname">reverse_proxy_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.reverse_proxy_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>reverse_proxy_certificate</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.upgrade_mode">
<code class="descname">upgrade_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.upgrade_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Upgrade Mode of the cluster. Possible values are <cite>Automatic</cite> or <cite>Manual</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.vm_image">
<code class="descname">vm_image</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.vm_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Image expected for the Service Fabric Cluster, such as <cite>Windows</cite>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.servicefabric.Cluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.servicefabric.Cluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
</dd></dl>

</dd></dl>

</div>
