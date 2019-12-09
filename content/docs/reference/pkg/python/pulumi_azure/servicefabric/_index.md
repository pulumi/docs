---
title: Module servicefabric
title_tag: Module servicefabric | Package pulumi_azure | Python SDK
linktitle: servicefabric
notitle: true
---

<div class="section" id="servicefabric">
<h1>servicefabric<a class="headerlink" href="#servicefabric" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.servicefabric"></span><dl class="class">
<dt id="pulumi_azure.servicefabric.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.servicefabric.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_on_features=None</em>, <em class="sig-param">azure_active_directory=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">certificate_common_names=None</em>, <em class="sig-param">client_certificate_thumbprints=None</em>, <em class="sig-param">cluster_code_version=None</em>, <em class="sig-param">diagnostics_config=None</em>, <em class="sig-param">fabric_settings=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">management_endpoint=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">node_types=None</em>, <em class="sig-param">reliability_level=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">reverse_proxy_certificate=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">upgrade_mode=None</em>, <em class="sig-param">vm_image=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Service Fabric Cluster.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>add_on_features</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A List of one or more features which should be enabled, such as <code class="docutils literal notranslate"><span class="pre">DnsService</span></code>.</p></li>
<li><p><strong>azure_active_directory</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">azure_active_directory</span></code> block as defined below.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">certificate</span></code> block as defined below. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_common_names</span></code>.</p></li>
<li><p><strong>certificate_common_names</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">certificate_common_names</span></code> block as defined below. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate</span></code>.</p></li>
<li><p><strong>client_certificate_thumbprints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or two <code class="docutils literal notranslate"><span class="pre">client_certificate_thumbprint</span></code> blocks as defined below.</p></li>
<li><p><strong>cluster_code_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required if Upgrade Mode set to <code class="docutils literal notranslate"><span class="pre">Manual</span></code>, Specifies the Version of the Cluster Code of the cluster.</p></li>
<li><p><strong>diagnostics_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">diagnostics_config</span></code> block as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>fabric_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">fabric_settings</span></code> blocks as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>management_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Management Endpoint of the cluster such as <code class="docutils literal notranslate"><span class="pre">http://example.com</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Service Fabric Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>node_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">node_type</span></code> blocks as defined below.</p></li>
<li><p><strong>reliability_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Reliability Level of the Cluster. Possible values include <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Bronze</span></code>, <code class="docutils literal notranslate"><span class="pre">Silver</span></code>, <code class="docutils literal notranslate"><span class="pre">Gold</span></code> and <code class="docutils literal notranslate"><span class="pre">Platinum</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>reverse_proxy_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">reverse_proxy_certificate</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>upgrade_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Upgrade Mode of the cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Automatic</span></code> or <code class="docutils literal notranslate"><span class="pre">Manual</span></code>.</p></li>
<li><p><strong>vm_image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Image expected for the Service Fabric Cluster, such as <code class="docutils literal notranslate"><span class="pre">Windows</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>azure_active_directory</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clientApplicationId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterApplicationId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>certificate</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprintSecondary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">x509StoreName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>certificate_common_names</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commonNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateCommonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateIssuerThumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">x509StoreName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>client_certificate_thumbprints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isAdmin</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>diagnostics_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">blobEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protectedAccountKeyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queueEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tableEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>fabric_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Service Fabric Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
<p>The <strong>node_types</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applicationPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">endPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">capacities</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientEndpointPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">durabilityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ephemeralPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">endPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpEndpointPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isPrimary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Service Fabric Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placementProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reverseProxyEndpointPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>reverse_proxy_certificate</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprintSecondary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">x509StoreName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/service_fabric_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/service_fabric_cluster.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.add_on_features">
<code class="sig-name descname">add_on_features</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.add_on_features" title="Permalink to this definition">¶</a></dt>
<dd><p>A List of one or more features which should be enabled, such as <code class="docutils literal notranslate"><span class="pre">DnsService</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.azure_active_directory">
<code class="sig-name descname">azure_active_directory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.azure_active_directory" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">azure_active_directory</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clientApplicationId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterApplicationId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.certificate">
<code class="sig-name descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">certificate</span></code> block as defined below. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_common_names</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprintSecondary</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">x509StoreName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.certificate_common_names">
<code class="sig-name descname">certificate_common_names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.certificate_common_names" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">certificate_common_names</span></code> block as defined below. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commonNames</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateCommonName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateIssuerThumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">x509StoreName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.client_certificate_thumbprints">
<code class="sig-name descname">client_certificate_thumbprints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.client_certificate_thumbprints" title="Permalink to this definition">¶</a></dt>
<dd><p>One or two <code class="docutils literal notranslate"><span class="pre">client_certificate_thumbprint</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isAdmin</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.cluster_code_version">
<code class="sig-name descname">cluster_code_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.cluster_code_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Required if Upgrade Mode set to <code class="docutils literal notranslate"><span class="pre">Manual</span></code>, Specifies the Version of the Cluster Code of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.cluster_endpoint">
<code class="sig-name descname">cluster_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.cluster_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Cluster Endpoint for this Service Fabric Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.diagnostics_config">
<code class="sig-name descname">diagnostics_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.diagnostics_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">diagnostics_config</span></code> block as defined below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">blobEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protectedAccountKeyName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queueEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tableEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.fabric_settings">
<code class="sig-name descname">fabric_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.fabric_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">fabric_settings</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Service Fabric Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.management_endpoint">
<code class="sig-name descname">management_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.management_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Management Endpoint of the cluster such as <code class="docutils literal notranslate"><span class="pre">http://example.com</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Service Fabric Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.node_types">
<code class="sig-name descname">node_types</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.node_types" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">node_type</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applicationPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">endPort</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startPort</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">capacities</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientEndpointPort</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">durabilityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ephemeralPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">endPort</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startPort</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpEndpointPort</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isPrimary</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Service Fabric Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placementProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reverseProxyEndpointPort</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.reliability_level">
<code class="sig-name descname">reliability_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.reliability_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Reliability Level of the Cluster. Possible values include <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Bronze</span></code>, <code class="docutils literal notranslate"><span class="pre">Silver</span></code>, <code class="docutils literal notranslate"><span class="pre">Gold</span></code> and <code class="docutils literal notranslate"><span class="pre">Platinum</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.reverse_proxy_certificate">
<code class="sig-name descname">reverse_proxy_certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.reverse_proxy_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">reverse_proxy_certificate</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprintSecondary</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">x509StoreName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.upgrade_mode">
<code class="sig-name descname">upgrade_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.upgrade_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Upgrade Mode of the cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Automatic</span></code> or <code class="docutils literal notranslate"><span class="pre">Manual</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.servicefabric.Cluster.vm_image">
<code class="sig-name descname">vm_image</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.vm_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Image expected for the Service Fabric Cluster, such as <code class="docutils literal notranslate"><span class="pre">Windows</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.servicefabric.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">add_on_features=None</em>, <em class="sig-param">azure_active_directory=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">certificate_common_names=None</em>, <em class="sig-param">client_certificate_thumbprints=None</em>, <em class="sig-param">cluster_code_version=None</em>, <em class="sig-param">cluster_endpoint=None</em>, <em class="sig-param">diagnostics_config=None</em>, <em class="sig-param">fabric_settings=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">management_endpoint=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">node_types=None</em>, <em class="sig-param">reliability_level=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">reverse_proxy_certificate=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">upgrade_mode=None</em>, <em class="sig-param">vm_image=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>add_on_features</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A List of one or more features which should be enabled, such as <code class="docutils literal notranslate"><span class="pre">DnsService</span></code>.</p></li>
<li><p><strong>azure_active_directory</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">azure_active_directory</span></code> block as defined below.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">certificate</span></code> block as defined below. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate_common_names</span></code>.</p></li>
<li><p><strong>certificate_common_names</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">certificate_common_names</span></code> block as defined below. Conflicts with <code class="docutils literal notranslate"><span class="pre">certificate</span></code>.</p></li>
<li><p><strong>client_certificate_thumbprints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or two <code class="docutils literal notranslate"><span class="pre">client_certificate_thumbprint</span></code> blocks as defined below.</p></li>
<li><p><strong>cluster_code_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required if Upgrade Mode set to <code class="docutils literal notranslate"><span class="pre">Manual</span></code>, Specifies the Version of the Cluster Code of the cluster.</p></li>
<li><p><strong>cluster_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Cluster Endpoint for this Service Fabric Cluster.</p></li>
<li><p><strong>diagnostics_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">diagnostics_config</span></code> block as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>fabric_settings</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">fabric_settings</span></code> blocks as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region where the Service Fabric Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>management_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Management Endpoint of the cluster such as <code class="docutils literal notranslate"><span class="pre">http://example.com</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Service Fabric Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>node_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">node_type</span></code> blocks as defined below.</p></li>
<li><p><strong>reliability_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Reliability Level of the Cluster. Possible values include <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Bronze</span></code>, <code class="docutils literal notranslate"><span class="pre">Silver</span></code>, <code class="docutils literal notranslate"><span class="pre">Gold</span></code> and <code class="docutils literal notranslate"><span class="pre">Platinum</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Service Fabric Cluster exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>reverse_proxy_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">reverse_proxy_certificate</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>upgrade_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Upgrade Mode of the cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Automatic</span></code> or <code class="docutils literal notranslate"><span class="pre">Manual</span></code>.</p></li>
<li><p><strong>vm_image</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Image expected for the Service Fabric Cluster, such as <code class="docutils literal notranslate"><span class="pre">Windows</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>azure_active_directory</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clientApplicationId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterApplicationId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>certificate</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprintSecondary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">x509StoreName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>certificate_common_names</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commonNames</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateCommonName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateIssuerThumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">x509StoreName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>client_certificate_thumbprints</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">isAdmin</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>diagnostics_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">blobEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protectedAccountKeyName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queueEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tableEndpoint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>fabric_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Service Fabric Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
</ul>
<p>The <strong>node_types</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">applicationPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">endPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">capacities</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientEndpointPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">durabilityLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ephemeralPorts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">endPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">startPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpEndpointPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instanceCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isPrimary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Service Fabric Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">placementProperties</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">reverseProxyEndpointPort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>reverse_proxy_certificate</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprint</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thumbprintSecondary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">x509StoreName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/service_fabric_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/service_fabric_cluster.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.servicefabric.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.servicefabric.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.servicefabric.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
