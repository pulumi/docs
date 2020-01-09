---
title: Module containerservice
title_tag: Module containerservice | Package pulumi_azure | Python SDK
linktitle: containerservice
notitle: true
---

<div class="section" id="containerservice">
<h1>containerservice<a class="headerlink" href="#containerservice" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.containerservice"></span><dl class="class">
<dt id="pulumi_azure.containerservice.AwaitableGetKubernetesClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">AwaitableGetKubernetesClusterResult</code><span class="sig-paren">(</span><em class="sig-param">addon_profiles=None</em>, <em class="sig-param">agent_pool_profiles=None</em>, <em class="sig-param">api_server_authorized_ip_ranges=None</em>, <em class="sig-param">dns_prefix=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">kube_admin_configs=None</em>, <em class="sig-param">kube_admin_config_raw=None</em>, <em class="sig-param">kube_configs=None</em>, <em class="sig-param">kube_config_raw=None</em>, <em class="sig-param">kubernetes_version=None</em>, <em class="sig-param">linux_profiles=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_profiles=None</em>, <em class="sig-param">node_resource_group=None</em>, <em class="sig-param">private_fqdn=None</em>, <em class="sig-param">private_link_enabled=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">role_based_access_controls=None</em>, <em class="sig-param">service_principals=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">windows_profiles=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.AwaitableGetKubernetesClusterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.containerservice.AwaitableGetKubernetesServiceVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">AwaitableGetKubernetesServiceVersionsResult</code><span class="sig-paren">(</span><em class="sig-param">latest_version=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">version_prefix=None</em>, <em class="sig-param">versions=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.AwaitableGetKubernetesServiceVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.containerservice.AwaitableGetRegistryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">AwaitableGetRegistryResult</code><span class="sig-paren">(</span><em class="sig-param">admin_enabled=None</em>, <em class="sig-param">admin_password=None</em>, <em class="sig-param">admin_username=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">login_server=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.AwaitableGetRegistryResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">GetKubernetesClusterResult</code><span class="sig-paren">(</span><em class="sig-param">addon_profiles=None</em>, <em class="sig-param">agent_pool_profiles=None</em>, <em class="sig-param">api_server_authorized_ip_ranges=None</em>, <em class="sig-param">dns_prefix=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">kube_admin_configs=None</em>, <em class="sig-param">kube_admin_config_raw=None</em>, <em class="sig-param">kube_configs=None</em>, <em class="sig-param">kube_config_raw=None</em>, <em class="sig-param">kubernetes_version=None</em>, <em class="sig-param">linux_profiles=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_profiles=None</em>, <em class="sig-param">node_resource_group=None</em>, <em class="sig-param">private_fqdn=None</em>, <em class="sig-param">private_link_enabled=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">role_based_access_controls=None</em>, <em class="sig-param">service_principals=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">windows_profiles=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKubernetesCluster.</p>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.addon_profiles">
<code class="sig-name descname">addon_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.addon_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">addon_profile</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.agent_pool_profiles">
<code class="sig-name descname">agent_pool_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.agent_pool_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">agent_pool_profile</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.api_server_authorized_ip_ranges">
<code class="sig-name descname">api_server_authorized_ip_ranges</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.api_server_authorized_ip_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP ranges to whitelist for incoming traffic to the masters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.dns_prefix">
<code class="sig-name descname">dns_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.dns_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS Prefix of the managed Kubernetes cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.fqdn">
<code class="sig-name descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the Azure Kubernetes Managed Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.kube_admin_configs">
<code class="sig-name descname">kube_admin_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.kube_admin_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">kube_admin_config</span></code> block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.kube_admin_config_raw">
<code class="sig-name descname">kube_admin_config_raw</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.kube_admin_config_raw" title="Permalink to this definition">¶</a></dt>
<dd><p>Raw Kubernetes config for the admin account to be used by <a class="reference external" href="https://kubernetes.io/docs/reference/kubectl/overview/">kubectl</a> and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.kube_configs">
<code class="sig-name descname">kube_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.kube_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">kube_config</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.kube_config_raw">
<code class="sig-name descname">kube_config_raw</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.kube_config_raw" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64 encoded Kubernetes configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.kubernetes_version">
<code class="sig-name descname">kubernetes_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.kubernetes_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of Kubernetes used on the managed Kubernetes Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.linux_profiles">
<code class="sig-name descname">linux_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.linux_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">linux_profile</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which the managed Kubernetes Cluster exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name assigned to this pool of agents.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.network_profiles">
<code class="sig-name descname">network_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.network_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">network_profile</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.node_resource_group">
<code class="sig-name descname">node_resource_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.node_resource_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Auto-generated Resource Group containing AKS Cluster resources.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.private_fqdn">
<code class="sig-name descname">private_fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.private_fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of this Kubernetes Cluster when private link has been enabled. This name is only resolvable inside the Virtual Network where the Azure Kubernetes Service is located</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.private_link_enabled">
<code class="sig-name descname">private_link_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.private_link_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Does this Kubernetes Cluster have the Kubernetes API exposed via Private Link?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.role_based_access_controls">
<code class="sig-name descname">role_based_access_controls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.role_based_access_controls" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">role_based_access_control</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.service_principals">
<code class="sig-name descname">service_principals</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.service_principals" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">service_principal</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to this resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.windows_profiles">
<code class="sig-name descname">windows_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.windows_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">windows_profile</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.containerservice.GetKubernetesServiceVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">GetKubernetesServiceVersionsResult</code><span class="sig-paren">(</span><em class="sig-param">latest_version=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">version_prefix=None</em>, <em class="sig-param">versions=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesServiceVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKubernetesServiceVersions.</p>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesServiceVersionsResult.latest_version">
<code class="sig-name descname">latest_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesServiceVersionsResult.latest_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The most recent version available.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesServiceVersionsResult.versions">
<code class="sig-name descname">versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesServiceVersionsResult.versions" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of all supported versions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesServiceVersionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesServiceVersionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.containerservice.GetRegistryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">GetRegistryResult</code><span class="sig-paren">(</span><em class="sig-param">admin_enabled=None</em>, <em class="sig-param">admin_password=None</em>, <em class="sig-param">admin_username=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">login_server=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegistry.</p>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetRegistryResult.admin_enabled">
<code class="sig-name descname">admin_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.admin_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the Administrator account enabled for this Container Registry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetRegistryResult.admin_password">
<code class="sig-name descname">admin_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.admin_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password associated with the Container Registry Admin account - if the admin account is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetRegistryResult.admin_username">
<code class="sig-name descname">admin_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.admin_username" title="Permalink to this definition">¶</a></dt>
<dd><p>The Username associated with the Container Registry Admin account - if the admin account is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetRegistryResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which this Container Registry exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetRegistryResult.login_server">
<code class="sig-name descname">login_server</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.login_server" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL that can be used to log into the container registry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetRegistryResult.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU of this Container Registry, such as <code class="docutils literal notranslate"><span class="pre">Basic</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetRegistryResult.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Storage Account used for this Container Registry. This is only returned for <code class="docutils literal notranslate"><span class="pre">Classic</span></code> SKU’s.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetRegistryResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags assigned to the Container Registry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetRegistryResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.containerservice.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">containers=None</em>, <em class="sig-param">diagnostics=None</em>, <em class="sig-param">dns_name_label=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">image_registry_credentials=None</em>, <em class="sig-param">ip_address_type=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_profile_id=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">restart_policy=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages as an Azure Container Group instance.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>containers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The definition of a container that is part of the group as documented in the <code class="docutils literal notranslate"><span class="pre">container</span></code> block below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>diagnostics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">diagnostics</span></code> block as documented below.</p></li>
<li><p><strong>dns_name_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS label/name for the container groups IP. Changing this forces a new resource to be created.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>image_registry_credentials</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">image_registry_credential</span></code> block as documented below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>ip_address_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ip address type of the container. <code class="docutils literal notranslate"><span class="pre">Public</span></code> or <code class="docutils literal notranslate"><span class="pre">Private</span></code>. Changing this forces a new resource to be created. If set to <code class="docutils literal notranslate"><span class="pre">Private</span></code>, <code class="docutils literal notranslate"><span class="pre">network_profile_id</span></code> also needs to be set.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Container Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_profile_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network profile ID for deploying to virtual network.</p></li>
<li><p><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OS for the container group. Allowed values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Container Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>restart_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Restart policy for the container group. Allowed values are <code class="docutils literal notranslate"><span class="pre">Always</span></code>, <code class="docutils literal notranslate"><span class="pre">Never</span></code>, <code class="docutils literal notranslate"><span class="pre">OnFailure</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Always</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>containers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">command</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commands</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environmentVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">livenessProbe</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">execs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpGets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelaySeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">periodSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">memory</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Container Group. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readinessProbe</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">execs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpGets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelaySeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">periodSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">secureEnvironmentVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Container Group. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shareName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>diagnostics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">logAnalytics</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">logType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspaceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspaceKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>image_registry_credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_group.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.containers">
<code class="sig-name descname">containers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.containers" title="Permalink to this definition">¶</a></dt>
<dd><p>The definition of a container that is part of the group as documented in the <code class="docutils literal notranslate"><span class="pre">container</span></code> block below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">command</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commands</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpu</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environmentVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpu</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">livenessProbe</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">execs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpGets</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelaySeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">periodSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">memory</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Container Group. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readinessProbe</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">execs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpGets</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelaySeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">periodSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">secureEnvironmentVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Container Group. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shareName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.diagnostics">
<code class="sig-name descname">diagnostics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.diagnostics" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">diagnostics</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">logAnalytics</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">logType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspaceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspaceKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.dns_name_label">
<code class="sig-name descname">dns_name_label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.dns_name_label" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS label/name for the container groups IP. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.fqdn">
<code class="sig-name descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the container group derived from <code class="docutils literal notranslate"><span class="pre">dns_name_label</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.image_registry_credentials">
<code class="sig-name descname">image_registry_credentials</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.image_registry_credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">image_registry_credential</span></code> block as documented below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.ip_address">
<code class="sig-name descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address allocated to the container group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.ip_address_type">
<code class="sig-name descname">ip_address_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.ip_address_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ip address type of the container. <code class="docutils literal notranslate"><span class="pre">Public</span></code> or <code class="docutils literal notranslate"><span class="pre">Private</span></code>. Changing this forces a new resource to be created. If set to <code class="docutils literal notranslate"><span class="pre">Private</span></code>, <code class="docutils literal notranslate"><span class="pre">network_profile_id</span></code> also needs to be set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Container Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.network_profile_id">
<code class="sig-name descname">network_profile_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.network_profile_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Network profile ID for deploying to virtual network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.os_type">
<code class="sig-name descname">os_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.os_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The OS for the container group. Allowed values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Container Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.restart_policy">
<code class="sig-name descname">restart_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.restart_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Restart policy for the container group. Allowed values are <code class="docutils literal notranslate"><span class="pre">Always</span></code>, <code class="docutils literal notranslate"><span class="pre">Never</span></code>, <code class="docutils literal notranslate"><span class="pre">OnFailure</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Always</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">containers=None</em>, <em class="sig-param">diagnostics=None</em>, <em class="sig-param">dns_name_label=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">image_registry_credentials=None</em>, <em class="sig-param">ip_address=None</em>, <em class="sig-param">ip_address_type=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_profile_id=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">restart_policy=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>containers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The definition of a container that is part of the group as documented in the <code class="docutils literal notranslate"><span class="pre">container</span></code> block below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>diagnostics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">diagnostics</span></code> block as documented below.</p></li>
<li><p><strong>dns_name_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS label/name for the container groups IP. Changing this forces a new resource to be created.</p></li>
<li><p><strong>fqdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FQDN of the container group derived from <code class="docutils literal notranslate"><span class="pre">dns_name_label</span></code>.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>image_registry_credentials</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">image_registry_credential</span></code> block as documented below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IP address allocated to the container group.</p></li>
<li><p><strong>ip_address_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ip address type of the container. <code class="docutils literal notranslate"><span class="pre">Public</span></code> or <code class="docutils literal notranslate"><span class="pre">Private</span></code>. Changing this forces a new resource to be created. If set to <code class="docutils literal notranslate"><span class="pre">Private</span></code>, <code class="docutils literal notranslate"><span class="pre">network_profile_id</span></code> also needs to be set.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Container Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_profile_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network profile ID for deploying to virtual network.</p></li>
<li><p><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OS for the container group. Allowed values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Container Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>restart_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Restart policy for the container group. Allowed values are <code class="docutils literal notranslate"><span class="pre">Always</span></code>, <code class="docutils literal notranslate"><span class="pre">Never</span></code>, <code class="docutils literal notranslate"><span class="pre">OnFailure</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Always</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>containers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">command</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">commands</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environmentVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">livenessProbe</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">execs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpGets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelaySeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">periodSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">memory</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Container Group. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readinessProbe</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">execs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpGets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelaySeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">periodSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">secureEnvironmentVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Container Group. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shareName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>diagnostics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">logAnalytics</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">logType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspaceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspaceKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>image_registry_credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_group.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.KubernetesCluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">KubernetesCluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">addon_profile=None</em>, <em class="sig-param">agent_pool_profiles=None</em>, <em class="sig-param">api_server_authorized_ip_ranges=None</em>, <em class="sig-param">default_node_pool=None</em>, <em class="sig-param">dns_prefix=None</em>, <em class="sig-param">enable_pod_security_policy=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">kubernetes_version=None</em>, <em class="sig-param">linux_profile=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_profile=None</em>, <em class="sig-param">node_resource_group=None</em>, <em class="sig-param">private_link_enabled=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">role_based_access_control=None</em>, <em class="sig-param">service_principal=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">windows_profile=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Managed Kubernetes Cluster (also known as AKS / Azure Kubernetes Service)</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the client secret will be stored in the raw state as plain-text. <a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>addon_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">addon_profile</span></code> block as defined below.</p></li>
<li><p><strong>agent_pool_profiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">agent_pool_profile</span></code> blocks as defined below.</p></li>
<li><p><strong>api_server_authorized_ip_ranges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The IP ranges to whitelist for incoming traffic to the masters.</p></li>
<li><p><strong>default_node_pool</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">default_node_pool</span></code> block as defined below.</p></li>
<li><p><strong>dns_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>enable_pod_security_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Pod Security Policies are enabled. Note that this also requires role based access control to be enabled.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>kubernetes_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won’t auto-upgrade).</p></li>
<li><p><strong>linux_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">linux_profile</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">network_profile</span></code> block as defined below.</p></li>
<li><p><strong>node_resource_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Kubernetes Nodes should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>role_based_access_control</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">role_based_access_control</span></code> block. Changing this forces a new resource to be created.</p></li>
<li><p><strong>service_principal</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">service_principal</span></code> block as documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>windows_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">windows_profile</span></code> block as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>addon_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aciConnectorLinux</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">azurePolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpApplicationRouting</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">http_application_routing</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpApplicationRoutingZoneName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Zone Name of the HTTP Application Routing.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kubeDashboard</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">omsAgent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logAnalyticsWorkspaceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>agent_pool_profiles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dns_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_auto_scaling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_node_public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fqdn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The FQDN of the Azure Kubernetes Managed Cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_pods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vnet_subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>default_node_pool</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_auto_scaling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_node_public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_pods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vnet_subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The principal id of the system assigned identity which is used by master components.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenantId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tenant id of the system assigned identity which is used by master components.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>linux_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>network_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dnsServiceIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dockerBridgeCidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerSku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkPlugin</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">podCidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceCidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>role_based_access_control</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">azureActiveDirectory</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">clientAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverAppSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenantId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tenant id of the system assigned identity which is used by master components.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>service_principal</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>windows_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kubernetes_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kubernetes_cluster.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.addon_profile">
<code class="sig-name descname">addon_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.addon_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">addon_profile</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aciConnectorLinux</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">azurePolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpApplicationRouting</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">http_application_routing</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpApplicationRoutingZoneName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Zone Name of the HTTP Application Routing.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kubeDashboard</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">omsAgent</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logAnalyticsWorkspaceId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.agent_pool_profiles">
<code class="sig-name descname">agent_pool_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.agent_pool_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">agent_pool_profile</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dns_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_auto_scaling</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_node_public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fqdn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The FQDN of the Azure Kubernetes Managed Cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_pods</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_taints</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vnet_subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.api_server_authorized_ip_ranges">
<code class="sig-name descname">api_server_authorized_ip_ranges</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.api_server_authorized_ip_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP ranges to whitelist for incoming traffic to the masters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.default_node_pool">
<code class="sig-name descname">default_node_pool</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.default_node_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">default_node_pool</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_auto_scaling</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_node_public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_pods</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_taints</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vnet_subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.dns_prefix">
<code class="sig-name descname">dns_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.dns_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.enable_pod_security_policy">
<code class="sig-name descname">enable_pod_security_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.enable_pod_security_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether Pod Security Policies are enabled. Note that this also requires role based access control to be enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.fqdn">
<code class="sig-name descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the Azure Kubernetes Managed Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The principal id of the system assigned identity which is used by master components.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenantId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tenant id of the system assigned identity which is used by master components.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.kube_admin_config">
<code class="sig-name descname">kube_admin_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.kube_admin_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">kube_admin_config</span></code> block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterCaCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Kubernetes cluster server host.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A password or token used to authenticate to the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A username used to authenticate to the Kubernetes cluster.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.kube_admin_config_raw">
<code class="sig-name descname">kube_admin_config_raw</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.kube_admin_config_raw" title="Permalink to this definition">¶</a></dt>
<dd><p>Raw Kubernetes config for the admin account to be used by <a class="reference external" href="https://kubernetes.io/docs/reference/kubectl/overview/">kubectl</a> and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.kube_config">
<code class="sig-name descname">kube_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.kube_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">kube_config</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterCaCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Kubernetes cluster server host.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A password or token used to authenticate to the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A username used to authenticate to the Kubernetes cluster.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.kube_config_raw">
<code class="sig-name descname">kube_config_raw</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.kube_config_raw" title="Permalink to this definition">¶</a></dt>
<dd><p>Raw Kubernetes config to be used by <a class="reference external" href="https://kubernetes.io/docs/reference/kubectl/overview/">kubectl</a> and other compatible tools</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.kubernetes_version">
<code class="sig-name descname">kubernetes_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.kubernetes_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won’t auto-upgrade).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.linux_profile">
<code class="sig-name descname">linux_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.linux_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">linux_profile</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyData</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.network_profile">
<code class="sig-name descname">network_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.network_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">network_profile</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dnsServiceIp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dockerBridgeCidr</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerSku</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkPlugin</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">podCidr</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceCidr</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.node_resource_group">
<code class="sig-name descname">node_resource_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.node_resource_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Kubernetes Nodes should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.private_fqdn">
<code class="sig-name descname">private_fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.private_fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN for the Kubernetes Cluster when private link has been enabled, which is is only resolvable inside the Virtual Network used by the Kubernetes Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.role_based_access_control">
<code class="sig-name descname">role_based_access_control</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.role_based_access_control" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">role_based_access_control</span></code> block. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">azureActiveDirectory</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">clientAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverAppSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenantId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The tenant id of the system assigned identity which is used by master components.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.service_principal">
<code class="sig-name descname">service_principal</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.service_principal" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">service_principal</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.windows_profile">
<code class="sig-name descname">windows_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.windows_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">windows_profile</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.KubernetesCluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">addon_profile=None</em>, <em class="sig-param">agent_pool_profiles=None</em>, <em class="sig-param">api_server_authorized_ip_ranges=None</em>, <em class="sig-param">default_node_pool=None</em>, <em class="sig-param">dns_prefix=None</em>, <em class="sig-param">enable_pod_security_policy=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">kube_admin_config=None</em>, <em class="sig-param">kube_admin_config_raw=None</em>, <em class="sig-param">kube_config=None</em>, <em class="sig-param">kube_config_raw=None</em>, <em class="sig-param">kubernetes_version=None</em>, <em class="sig-param">linux_profile=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_profile=None</em>, <em class="sig-param">node_resource_group=None</em>, <em class="sig-param">private_fqdn=None</em>, <em class="sig-param">private_link_enabled=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">role_based_access_control=None</em>, <em class="sig-param">service_principal=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">windows_profile=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KubernetesCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>addon_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">addon_profile</span></code> block as defined below.</p></li>
<li><p><strong>agent_pool_profiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">agent_pool_profile</span></code> blocks as defined below.</p></li>
<li><p><strong>api_server_authorized_ip_ranges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The IP ranges to whitelist for incoming traffic to the masters.</p></li>
<li><p><strong>default_node_pool</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">default_node_pool</span></code> block as defined below.</p></li>
<li><p><strong>dns_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>enable_pod_security_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Pod Security Policies are enabled. Note that this also requires role based access control to be enabled.</p></li>
<li><p><strong>fqdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FQDN of the Azure Kubernetes Managed Cluster.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>kube_admin_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">kube_admin_config</span></code> block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.</p></li>
<li><p><strong>kube_admin_config_raw</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Raw Kubernetes config for the admin account to be used by <a class="reference external" href="https://kubernetes.io/docs/reference/kubectl/overview/">kubectl</a> and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.</p>
</p></li>
<li><p><strong>kube_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">kube_config</span></code> block as defined below.</p></li>
<li><p><strong>kube_config_raw</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Raw Kubernetes config to be used by <a class="reference external" href="https://kubernetes.io/docs/reference/kubectl/overview/">kubectl</a> and other compatible tools</p>
</p></li>
<li><p><strong>kubernetes_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won’t auto-upgrade).</p></li>
<li><p><strong>linux_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">linux_profile</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">network_profile</span></code> block as defined below.</p></li>
<li><p><strong>node_resource_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Kubernetes Nodes should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>private_fqdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FQDN for the Kubernetes Cluster when private link has been enabled, which is is only resolvable inside the Virtual Network used by the Kubernetes Cluster.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>role_based_access_control</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">role_based_access_control</span></code> block. Changing this forces a new resource to be created.</p></li>
<li><p><strong>service_principal</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">service_principal</span></code> block as documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>windows_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">windows_profile</span></code> block as defined below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>addon_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aciConnectorLinux</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">azurePolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpApplicationRouting</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">http_application_routing</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpApplicationRoutingZoneName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Zone Name of the HTTP Application Routing.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kubeDashboard</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">omsAgent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logAnalyticsWorkspaceId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>agent_pool_profiles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dns_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_auto_scaling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_node_public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fqdn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The FQDN of the Azure Kubernetes Managed Cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_pods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vnet_subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>default_node_pool</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_auto_scaling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_node_public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_pods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vnet_subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The principal id of the system assigned identity which is used by master components.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenantId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tenant id of the system assigned identity which is used by master components.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>kube_admin_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterCaCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Kubernetes cluster server host.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A password or token used to authenticate to the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A username used to authenticate to the Kubernetes cluster.</p></li>
</ul>
<p>The <strong>kube_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterCaCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Kubernetes cluster server host.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A password or token used to authenticate to the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A username used to authenticate to the Kubernetes cluster.</p></li>
</ul>
<p>The <strong>linux_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>network_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dnsServiceIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dockerBridgeCidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerSku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkPlugin</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">podCidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceCidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>role_based_access_control</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">azureActiveDirectory</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">clientAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverAppSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenantId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The tenant id of the system assigned identity which is used by master components.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>service_principal</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>windows_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kubernetes_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kubernetes_cluster.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.KubernetesCluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.KubernetesCluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">KubernetesClusterNodePool</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">availability_zones=None</em>, <em class="sig-param">enable_auto_scaling=None</em>, <em class="sig-param">enable_node_public_ip=None</em>, <em class="sig-param">kubernetes_cluster_id=None</em>, <em class="sig-param">max_count=None</em>, <em class="sig-param">max_pods=None</em>, <em class="sig-param">min_count=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">node_count=None</em>, <em class="sig-param">node_taints=None</em>, <em class="sig-param">os_disk_size_gb=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">vm_size=None</em>, <em class="sig-param">vnet_subnet_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Node Pool within a Kubernetes Cluster</p>
<blockquote>
<div><p><strong>NOTE:</strong> Multiple Node Pools are only supported when the Kubernetes Cluster is using Virtual Machine Scale Sets.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Availability Zones where the Nodes in this Node Pool should be created in.</p></li>
<li><p><strong>enable_auto_scaling</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable <a class="reference external" href="https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler">auto-scaler</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_node_public_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should each node have a Public IP Address? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>kubernetes_cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Kubernetes Cluster where this Node Pool should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of nodes which should exist within this Node Pool. Valid values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code> and must be greater than or equal to <code class="docutils literal notranslate"><span class="pre">min_count</span></code>.</p></li>
<li><p><strong>max_pods</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.</p></li>
<li><p><strong>min_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of nodes which should exist within this Node Pool. Valid values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code> and must be less than or equal to <code class="docutils literal notranslate"><span class="pre">max_count</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Node Pool which should be created within the Kubernetes Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of nodes which should exist within this Node Pool. Valid values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><strong>node_taints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g <code class="docutils literal notranslate"><span class="pre">key=value:NoSchedule</span></code>).</p></li>
<li><p><strong>os_disk_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Agent Operating System disk size in GB. Changing this forces a new resource to be created.</p></li>
<li><p><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Operating System which should be used for this Node Pool. Changing this forces a new resource to be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Linux</span></code>.</p></li>
<li><p><strong>vm_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU which should be used for the Virtual Machines used in this Node Pool. Changing this forces a new resource to be created.</p></li>
<li><p><strong>vnet_subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet where this Node Pool should exist.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kubernetes_cluster_node_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kubernetes_cluster_node_pool.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.availability_zones">
<code class="sig-name descname">availability_zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.availability_zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Availability Zones where the Nodes in this Node Pool should be created in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.enable_auto_scaling">
<code class="sig-name descname">enable_auto_scaling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.enable_auto_scaling" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable <a class="reference external" href="https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler">auto-scaler</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.enable_node_public_ip">
<code class="sig-name descname">enable_node_public_ip</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.enable_node_public_ip" title="Permalink to this definition">¶</a></dt>
<dd><p>Should each node have a Public IP Address? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.kubernetes_cluster_id">
<code class="sig-name descname">kubernetes_cluster_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.kubernetes_cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Kubernetes Cluster where this Node Pool should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.max_count">
<code class="sig-name descname">max_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.max_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of nodes which should exist within this Node Pool. Valid values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code> and must be greater than or equal to <code class="docutils literal notranslate"><span class="pre">min_count</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.max_pods">
<code class="sig-name descname">max_pods</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.max_pods" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.min_count">
<code class="sig-name descname">min_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.min_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum number of nodes which should exist within this Node Pool. Valid values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code> and must be less than or equal to <code class="docutils literal notranslate"><span class="pre">max_count</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Node Pool which should be created within the Kubernetes Cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.node_count">
<code class="sig-name descname">node_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.node_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of nodes which should exist within this Node Pool. Valid values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.node_taints">
<code class="sig-name descname">node_taints</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.node_taints" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g <code class="docutils literal notranslate"><span class="pre">key=value:NoSchedule</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.os_disk_size_gb">
<code class="sig-name descname">os_disk_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.os_disk_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The Agent Operating System disk size in GB. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.os_type">
<code class="sig-name descname">os_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.os_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Operating System which should be used for this Node Pool. Changing this forces a new resource to be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Linux</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.vm_size">
<code class="sig-name descname">vm_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.vm_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU which should be used for the Virtual Machines used in this Node Pool. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.vnet_subnet_id">
<code class="sig-name descname">vnet_subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.vnet_subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Subnet where this Node Pool should exist.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">availability_zones=None</em>, <em class="sig-param">enable_auto_scaling=None</em>, <em class="sig-param">enable_node_public_ip=None</em>, <em class="sig-param">kubernetes_cluster_id=None</em>, <em class="sig-param">max_count=None</em>, <em class="sig-param">max_pods=None</em>, <em class="sig-param">min_count=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">node_count=None</em>, <em class="sig-param">node_taints=None</em>, <em class="sig-param">os_disk_size_gb=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">vm_size=None</em>, <em class="sig-param">vnet_subnet_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KubernetesClusterNodePool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Availability Zones where the Nodes in this Node Pool should be created in.</p></li>
<li><p><strong>enable_auto_scaling</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Whether to enable <a class="reference external" href="https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler">auto-scaler</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</p></li>
<li><p><strong>enable_node_public_ip</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should each node have a Public IP Address? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>kubernetes_cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Kubernetes Cluster where this Node Pool should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of nodes which should exist within this Node Pool. Valid values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code> and must be greater than or equal to <code class="docutils literal notranslate"><span class="pre">min_count</span></code>.</p></li>
<li><p><strong>max_pods</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.</p></li>
<li><p><strong>min_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of nodes which should exist within this Node Pool. Valid values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code> and must be less than or equal to <code class="docutils literal notranslate"><span class="pre">max_count</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Node Pool which should be created within the Kubernetes Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of nodes which should exist within this Node Pool. Valid values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><strong>node_taints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g <code class="docutils literal notranslate"><span class="pre">key=value:NoSchedule</span></code>).</p></li>
<li><p><strong>os_disk_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Agent Operating System disk size in GB. Changing this forces a new resource to be created.</p></li>
<li><p><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Operating System which should be used for this Node Pool. Changing this forces a new resource to be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Linux</span></code>.</p></li>
<li><p><strong>vm_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU which should be used for the Virtual Machines used in this Node Pool. Changing this forces a new resource to be created.</p></li>
<li><p><strong>vnet_subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet where this Node Pool should exist.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kubernetes_cluster_node_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kubernetes_cluster_node_pool.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.Registry">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">Registry</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_enabled=None</em>, <em class="sig-param">georeplication_locations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_rule_set=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">storage_account=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Registry" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Container Registry.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the access key will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the admin user is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>georeplication_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Azure locations where the container registry should be geo-replicated.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Container Registry. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_rule_set</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">network_rule_set</span></code> block as documented below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Container Registry. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU name of the container registry. Possible values are <code class="docutils literal notranslate"><span class="pre">Classic</span></code> (which was previously <code class="docutils literal notranslate"><span class="pre">Basic</span></code>), <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>network_rule_set</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behaviour for requests matching no rules. Either <code class="docutils literal notranslate"><span class="pre">Allow</span></code> or <code class="docutils literal notranslate"><span class="pre">Deny</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Allow</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ip_rule</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behaviour for requests matching this rule. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Allow</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRange</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CIDR block from which requests will match the rule.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNetworks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">virtual_network</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behaviour for requests matching this rule. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Allow</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The subnet id from which requests will match the rule.</p></li>
</ul>
</li>
</ul>
<p>The <strong>storage_account</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Container Registry. Changing this forces a new resource to be created.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_registry.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_registry.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.admin_enabled">
<code class="sig-name descname">admin_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.admin_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the admin user is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.admin_password">
<code class="sig-name descname">admin_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.admin_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password associated with the Container Registry Admin account - if the admin account is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.admin_username">
<code class="sig-name descname">admin_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.admin_username" title="Permalink to this definition">¶</a></dt>
<dd><p>The Username associated with the Container Registry Admin account - if the admin account is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.georeplication_locations">
<code class="sig-name descname">georeplication_locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.georeplication_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Azure locations where the container registry should be geo-replicated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.login_server">
<code class="sig-name descname">login_server</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.login_server" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL that can be used to log into the container registry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Container Registry. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.network_rule_set">
<code class="sig-name descname">network_rule_set</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.network_rule_set" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">network_rule_set</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The behaviour for requests matching no rules. Either <code class="docutils literal notranslate"><span class="pre">Allow</span></code> or <code class="docutils literal notranslate"><span class="pre">Deny</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Allow</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ip_rule</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The behaviour for requests matching this rule. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Allow</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRange</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The CIDR block from which requests will match the rule.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNetworks</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">virtual_network</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The behaviour for requests matching this rule. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Allow</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The subnet id from which requests will match the rule.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Container Registry. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU name of the container registry. Possible values are <code class="docutils literal notranslate"><span class="pre">Classic</span></code> (which was previously <code class="docutils literal notranslate"><span class="pre">Basic</span></code>), <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.Registry.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_enabled=None</em>, <em class="sig-param">admin_password=None</em>, <em class="sig-param">admin_username=None</em>, <em class="sig-param">georeplication_locations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">login_server=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_rule_set=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">storage_account=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Registry.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Registry resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>admin_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the admin user is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>admin_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password associated with the Container Registry Admin account - if the admin account is enabled.</p></li>
<li><p><strong>admin_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Username associated with the Container Registry Admin account - if the admin account is enabled.</p></li>
<li><p><strong>georeplication_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Azure locations where the container registry should be geo-replicated.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>login_server</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL that can be used to log into the container registry.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Container Registry. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_rule_set</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">network_rule_set</span></code> block as documented below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Container Registry. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU name of the container registry. Possible values are <code class="docutils literal notranslate"><span class="pre">Classic</span></code> (which was previously <code class="docutils literal notranslate"><span class="pre">Basic</span></code>), <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>network_rule_set</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behaviour for requests matching no rules. Either <code class="docutils literal notranslate"><span class="pre">Allow</span></code> or <code class="docutils literal notranslate"><span class="pre">Deny</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Allow</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ip_rule</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behaviour for requests matching this rule. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Allow</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipRange</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CIDR block from which requests will match the rule.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">virtualNetworks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">virtual_network</span></code> blocks as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behaviour for requests matching this rule. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Allow</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The subnet id from which requests will match the rule.</p></li>
</ul>
</li>
</ul>
<p>The <strong>storage_account</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">accessKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Container Registry. Changing this forces a new resource to be created.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_registry.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_registry.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.Registry.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Registry.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.Registry.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Registry.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.RegistryWebook">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">RegistryWebook</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">actions=None</em>, <em class="sig-param">custom_headers=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">registry_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">service_uri=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebook" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Container Registry Webhook.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of actions that trigger the Webhook to post notifications. At least one action needs to be specified. Valid values are: <code class="docutils literal notranslate"><span class="pre">push</span></code>, <code class="docutils literal notranslate"><span class="pre">delete</span></code>, <code class="docutils literal notranslate"><span class="pre">quarantine</span></code>, <code class="docutils literal notranslate"><span class="pre">chart_push</span></code>, <code class="docutils literal notranslate"><span class="pre">chart_delete</span></code></p></li>
<li><p><strong>custom_headers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Custom headers that will be added to the webhook notifications request.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Container Registry Webhook. Changing this forces a new resource to be created.</p></li>
<li><p><strong>registry_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of Container registry this Webhook belongs to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Container Registry Webhook. Changing this forces a new resource to be created.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the scope of repositories that can trigger an event. For example, ‘foo:<a href="#id8"><span class="problematic" id="id9">*</span></a>’ means events for all tags under repository ‘foo’. ‘foo:bar’ means events for ‘foo:bar’ only. ‘foo’ is equivalent to ‘foo:latest’. Empty means all events.</p></li>
<li><p><strong>service_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the service URI for the Webhook to post notifications.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if this Webhook triggers notifications or not. Valid values: <code class="docutils literal notranslate"><span class="pre">enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">disabled</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">enabled</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_registry_webhook.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_registry_webhook.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.RegistryWebook.actions">
<code class="sig-name descname">actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebook.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of actions that trigger the Webhook to post notifications. At least one action needs to be specified. Valid values are: <code class="docutils literal notranslate"><span class="pre">push</span></code>, <code class="docutils literal notranslate"><span class="pre">delete</span></code>, <code class="docutils literal notranslate"><span class="pre">quarantine</span></code>, <code class="docutils literal notranslate"><span class="pre">chart_push</span></code>, <code class="docutils literal notranslate"><span class="pre">chart_delete</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.RegistryWebook.custom_headers">
<code class="sig-name descname">custom_headers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebook.custom_headers" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom headers that will be added to the webhook notifications request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.RegistryWebook.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebook.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.RegistryWebook.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebook.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Container Registry Webhook. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.RegistryWebook.registry_name">
<code class="sig-name descname">registry_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebook.registry_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of Container registry this Webhook belongs to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.RegistryWebook.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebook.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Container Registry Webhook. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.RegistryWebook.scope">
<code class="sig-name descname">scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebook.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the scope of repositories that can trigger an event. For example, ‘foo:<a href="#id10"><span class="problematic" id="id11">*</span></a>’ means events for all tags under repository ‘foo’. ‘foo:bar’ means events for ‘foo:bar’ only. ‘foo’ is equivalent to ‘foo:latest’. Empty means all events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.RegistryWebook.service_uri">
<code class="sig-name descname">service_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebook.service_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the service URI for the Webhook to post notifications.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.RegistryWebook.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebook.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if this Webhook triggers notifications or not. Valid values: <code class="docutils literal notranslate"><span class="pre">enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">disabled</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">enabled</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.RegistryWebook.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">actions=None</em>, <em class="sig-param">custom_headers=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">registry_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">service_uri=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebook.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RegistryWebook resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of actions that trigger the Webhook to post notifications. At least one action needs to be specified. Valid values are: <code class="docutils literal notranslate"><span class="pre">push</span></code>, <code class="docutils literal notranslate"><span class="pre">delete</span></code>, <code class="docutils literal notranslate"><span class="pre">quarantine</span></code>, <code class="docutils literal notranslate"><span class="pre">chart_push</span></code>, <code class="docutils literal notranslate"><span class="pre">chart_delete</span></code></p></li>
<li><p><strong>custom_headers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Custom headers that will be added to the webhook notifications request.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Container Registry Webhook. Changing this forces a new resource to be created.</p></li>
<li><p><strong>registry_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Name of Container registry this Webhook belongs to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Container Registry Webhook. Changing this forces a new resource to be created.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the scope of repositories that can trigger an event. For example, ‘foo:<a href="#id12"><span class="problematic" id="id13">*</span></a>’ means events for all tags under repository ‘foo’. ‘foo:bar’ means events for ‘foo:bar’ only. ‘foo’ is equivalent to ‘foo:latest’. Empty means all events.</p></li>
<li><p><strong>service_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the service URI for the Webhook to post notifications.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if this Webhook triggers notifications or not. Valid values: <code class="docutils literal notranslate"><span class="pre">enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">disabled</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">enabled</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_registry_webhook.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_registry_webhook.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.RegistryWebook.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebook.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.RegistryWebook.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebook.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.Service">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">Service</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">agent_pool_profile=None</em>, <em class="sig-param">diagnostics_profile=None</em>, <em class="sig-param">linux_profile=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">master_profile=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">orchestration_platform=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_principal=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Container Service Instance</p>
<blockquote>
<div><p><strong>NOTE:</strong> All arguments including the client secret will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
<p><strong>DEPRECATED:</strong> <a class="reference external" href="https://azure.microsoft.com/en-us/updates/azure-container-service-will-retire-on-january-31-2020/">Azure Container Service (ACS) has been deprecated by Azure in favour of Azure (Managed) Kubernetes Service (AKS)</a>. Support for ACS will be removed in the next major version of the AzureRM Provider (2.0) - and we <strong>strongly recommend</strong> you consider using Azure Kubernetes Service (AKS) for new deployments.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_pool_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Agent Pool Profile’s block as documented below.</p></li>
<li><p><strong>diagnostics_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A VM Diagnostics Profile block as documented below.</p></li>
<li><p><strong>linux_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Linux Profile block as documented below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the Container Service instance should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>master_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Master Profile block as documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique name of the agent pool profile in the context of the subscription and resource group.</p></li>
<li><p><strong>orchestration_platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Container Orchestration Platform to use. Currently can be either <code class="docutils literal notranslate"><span class="pre">DCOS</span></code>, <code class="docutils literal notranslate"><span class="pre">Kubernetes</span></code> or <code class="docutils literal notranslate"><span class="pre">Swarm</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>service_principal</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Service Principal block as documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>agent_pool_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive). The default value is 1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dns_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The DNS Prefix given to Agents in this Agent Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fqdn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Unique name of the agent pool profile in the context of the subscription and resource group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The VM Size of each of the Agent Pool VM’s (e.g. Standard_F1 / Standard_D2v2).</p></li>
</ul>
<p>The <strong>diagnostics_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should VM Diagnostics be enabled for the Container Service VM’s</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>linux_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Admin Username for the Cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An SSH Key block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Public SSH Key used to access the cluster.</p></li>
</ul>
</li>
</ul>
<p>The <strong>master_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive). The default value is 1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dns_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The DNS Prefix given to Agents in this Agent Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fqdn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>service_principal</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID for the Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secret password associated with the service principal.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_service.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_service.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.agent_pool_profile">
<code class="sig-name descname">agent_pool_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.agent_pool_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A Agent Pool Profile’s block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive). The default value is 1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dns_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The DNS Prefix given to Agents in this Agent Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fqdn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Unique name of the agent pool profile in the context of the subscription and resource group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The VM Size of each of the Agent Pool VM’s (e.g. Standard_F1 / Standard_D2v2).</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.diagnostics_profile">
<code class="sig-name descname">diagnostics_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.diagnostics_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A VM Diagnostics Profile block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should VM Diagnostics be enabled for the Container Service VM’s</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.linux_profile">
<code class="sig-name descname">linux_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.linux_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A Linux Profile block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Admin Username for the Cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - An SSH Key block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyData</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Public SSH Key used to access the cluster.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the Container Service instance should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.master_profile">
<code class="sig-name descname">master_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.master_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A Master Profile block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive). The default value is 1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dns_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The DNS Prefix given to Agents in this Agent Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fqdn</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique name of the agent pool profile in the context of the subscription and resource group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.orchestration_platform">
<code class="sig-name descname">orchestration_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.orchestration_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Container Orchestration Platform to use. Currently can be either <code class="docutils literal notranslate"><span class="pre">DCOS</span></code>, <code class="docutils literal notranslate"><span class="pre">Kubernetes</span></code> or <code class="docutils literal notranslate"><span class="pre">Swarm</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.service_principal">
<code class="sig-name descname">service_principal</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.service_principal" title="Permalink to this definition">¶</a></dt>
<dd><p>A Service Principal block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID for the Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The secret password associated with the service principal.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.Service.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">agent_pool_profile=None</em>, <em class="sig-param">diagnostics_profile=None</em>, <em class="sig-param">linux_profile=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">master_profile=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">orchestration_platform=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_principal=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Service.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Service resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_pool_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Agent Pool Profile’s block as documented below.</p></li>
<li><p><strong>diagnostics_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A VM Diagnostics Profile block as documented below.</p></li>
<li><p><strong>linux_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Linux Profile block as documented below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the Container Service instance should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>master_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Master Profile block as documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique name of the agent pool profile in the context of the subscription and resource group.</p></li>
<li><p><strong>orchestration_platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Container Orchestration Platform to use. Currently can be either <code class="docutils literal notranslate"><span class="pre">DCOS</span></code>, <code class="docutils literal notranslate"><span class="pre">Kubernetes</span></code> or <code class="docutils literal notranslate"><span class="pre">Swarm</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>service_principal</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Service Principal block as documented below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>agent_pool_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive). The default value is 1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dns_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The DNS Prefix given to Agents in this Agent Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fqdn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Unique name of the agent pool profile in the context of the subscription and resource group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The VM Size of each of the Agent Pool VM’s (e.g. Standard_F1 / Standard_D2v2).</p></li>
</ul>
<p>The <strong>diagnostics_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should VM Diagnostics be enabled for the Container Service VM’s</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>linux_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Admin Username for the Cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An SSH Key block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Public SSH Key used to access the cluster.</p></li>
</ul>
</li>
</ul>
<p>The <strong>master_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive). The default value is 1.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dns_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The DNS Prefix given to Agents in this Agent Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fqdn</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>service_principal</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID for the Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secret password associated with the service principal.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_service.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_service.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.Service.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.Service.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_azure.containerservice.get_kubernetes_cluster">
<code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">get_kubernetes_cluster</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.get_kubernetes_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Managed Kubernetes Cluster (AKS).</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the client secret will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the managed Kubernetes Cluster.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group in which the managed Kubernetes Cluster exists.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/kubernetes_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/kubernetes_cluster.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.containerservice.get_kubernetes_service_versions">
<code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">get_kubernetes_service_versions</code><span class="sig-paren">(</span><em class="sig-param">location=None</em>, <em class="sig-param">version_prefix=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.get_kubernetes_service_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve the version of Kubernetes supported by Azure Kubernetes Service.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>location</strong> (<em>str</em>) – Specifies the location in which to query for versions.</p></li>
<li><p><strong>version_prefix</strong> (<em>str</em>) – A prefix filter for the versions of Kubernetes which should be returned; for example <code class="docutils literal notranslate"><span class="pre">1.</span></code> will return <code class="docutils literal notranslate"><span class="pre">1.9</span></code> to <code class="docutils literal notranslate"><span class="pre">1.14</span></code>, whereas <code class="docutils literal notranslate"><span class="pre">1.12</span></code> will return <code class="docutils literal notranslate"><span class="pre">1.12.2</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/kubernetes_service_versions.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/kubernetes_service_versions.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.containerservice.get_registry">
<code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">get_registry</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.get_registry" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Container Registry.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Container Registry.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where this Container Registry exists.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/container_registry.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/container_registry.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
