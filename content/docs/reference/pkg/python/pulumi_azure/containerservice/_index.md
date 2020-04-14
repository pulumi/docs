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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">AwaitableGetKubernetesClusterResult</code><span class="sig-paren">(</span><em class="sig-param">addon_profiles=None</em>, <em class="sig-param">agent_pool_profiles=None</em>, <em class="sig-param">api_server_authorized_ip_ranges=None</em>, <em class="sig-param">dns_prefix=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">kube_admin_config_raw=None</em>, <em class="sig-param">kube_admin_configs=None</em>, <em class="sig-param">kube_config_raw=None</em>, <em class="sig-param">kube_configs=None</em>, <em class="sig-param">kubernetes_version=None</em>, <em class="sig-param">linux_profiles=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_profiles=None</em>, <em class="sig-param">node_resource_group=None</em>, <em class="sig-param">private_fqdn=None</em>, <em class="sig-param">private_link_enabled=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">role_based_access_controls=None</em>, <em class="sig-param">service_principals=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">windows_profiles=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.AwaitableGetKubernetesClusterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.containerservice.AwaitableGetKubernetesServiceVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">AwaitableGetKubernetesServiceVersionsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">include_preview=None</em>, <em class="sig-param">latest_version=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">version_prefix=None</em>, <em class="sig-param">versions=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.AwaitableGetKubernetesServiceVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.containerservice.AwaitableGetRegistryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">AwaitableGetRegistryResult</code><span class="sig-paren">(</span><em class="sig-param">admin_enabled=None</em>, <em class="sig-param">admin_password=None</em>, <em class="sig-param">admin_username=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">login_server=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.AwaitableGetRegistryResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">GetKubernetesClusterResult</code><span class="sig-paren">(</span><em class="sig-param">addon_profiles=None</em>, <em class="sig-param">agent_pool_profiles=None</em>, <em class="sig-param">api_server_authorized_ip_ranges=None</em>, <em class="sig-param">dns_prefix=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">kube_admin_config_raw=None</em>, <em class="sig-param">kube_admin_configs=None</em>, <em class="sig-param">kube_config_raw=None</em>, <em class="sig-param">kube_configs=None</em>, <em class="sig-param">kubernetes_version=None</em>, <em class="sig-param">linux_profiles=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_profiles=None</em>, <em class="sig-param">node_resource_group=None</em>, <em class="sig-param">private_fqdn=None</em>, <em class="sig-param">private_link_enabled=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">role_based_access_controls=None</em>, <em class="sig-param">service_principals=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">windows_profiles=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.kube_admin_config_raw">
<code class="sig-name descname">kube_admin_config_raw</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.kube_admin_config_raw" title="Permalink to this definition">¶</a></dt>
<dd><p>Raw Kubernetes config for the admin account to be used by <a class="reference external" href="https://kubernetes.io/docs/reference/kubectl/overview/">kubectl</a> and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.kube_admin_configs">
<code class="sig-name descname">kube_admin_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.kube_admin_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">kube_admin_config</span></code> block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.kube_config_raw">
<code class="sig-name descname">kube_config_raw</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.kube_config_raw" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64 encoded Kubernetes configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.kube_configs">
<code class="sig-name descname">kube_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.kube_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">kube_config</span></code> block as defined below.</p>
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
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.windows_profiles">
<code class="sig-name descname">windows_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.windows_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">windows_profile</span></code> block as documented below.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.containerservice.GetKubernetesServiceVersionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">GetKubernetesServiceVersionsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">include_preview=None</em>, <em class="sig-param">latest_version=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">version_prefix=None</em>, <em class="sig-param">versions=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesServiceVersionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKubernetesServiceVersions.</p>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesServiceVersionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesServiceVersionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesServiceVersionsResult.latest_version">
<code class="sig-name descname">latest_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesServiceVersionsResult.latest_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The most recent version available. If <code class="docutils literal notranslate"><span class="pre">include_preview</span> <span class="pre">==</span> <span class="pre">false</span></code>, this is the most recent non-preview version available.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesServiceVersionsResult.versions">
<code class="sig-name descname">versions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesServiceVersionsResult.versions" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of all supported versions.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.containerservice.GetRegistryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">GetRegistryResult</code><span class="sig-paren">(</span><em class="sig-param">admin_enabled=None</em>, <em class="sig-param">admin_password=None</em>, <em class="sig-param">admin_username=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">login_server=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.GetRegistryResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
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

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.containerservice.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">containers=None</em>, <em class="sig-param">diagnostics=None</em>, <em class="sig-param">dns_name_label=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">image_registry_credentials=None</em>, <em class="sig-param">ip_address_type=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_profile_id=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">restart_policy=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages as an Azure Container Group instance.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_group.html.markdown</a>.</p>
</div></blockquote>
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
<li><p><code class="docutils literal notranslate"><span class="pre">commands</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of commands which should be run on the container. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The required number of CPU cores of the containers. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environmentVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A list of environment variables to be set on the container. Specified as a map of name/value pairs. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">gpu</span></code> block as defined below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of GPUs which should be assigned to this container. Allowed values are <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, or <code class="docutils literal notranslate"><span class="pre">4</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Sku which should be used for the GPU. Possible values are <code class="docutils literal notranslate"><span class="pre">K80</span></code>, <code class="docutils literal notranslate"><span class="pre">P100</span></code>, or <code class="docutils literal notranslate"><span class="pre">V100</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The container image name. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">livenessProbe</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The definition of a readiness probe for this container as documented in the <code class="docutils literal notranslate"><span class="pre">liveness_probe</span></code> block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">execs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Commands to be run to validate container readiness. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How many times to try the probe before restarting the container (liveness probe) or marking the container as unhealthy (readiness probe). The default value is <code class="docutils literal notranslate"><span class="pre">3</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpGets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The definition of the httpget for this container as documented in the <code class="docutils literal notranslate"><span class="pre">httpget</span></code> block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Path to access on the HTTP server. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port number the container will expose. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Scheme to use for connecting to the host. Possible values are <code class="docutils literal notranslate"><span class="pre">Http</span></code> and <code class="docutils literal notranslate"><span class="pre">Https</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelaySeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of seconds after the container has started before liveness or readiness probes are initiated. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">periodSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How often (in seconds) to perform the probe. The default value is <code class="docutils literal notranslate"><span class="pre">10</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Minimum consecutive successes for the probe to be considered successful after having failed. The default value is <code class="docutils literal notranslate"><span class="pre">1</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of seconds after which the probe times out. The default value is <code class="docutils literal notranslate"><span class="pre">1</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">memory</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The required memory of the containers in GB. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Container Group. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A set of public ports for the container. Changing this forces a new resource to be created. Set as documented in the <code class="docutils literal notranslate"><span class="pre">ports</span></code> block below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port number the container will expose. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The network protocol associated with port. Possible values are <code class="docutils literal notranslate"><span class="pre">TCP</span></code> &amp; <code class="docutils literal notranslate"><span class="pre">UDP</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">readinessProbe</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The definition of a readiness probe for this container as documented in the <code class="docutils literal notranslate"><span class="pre">readiness_probe</span></code> block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">execs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Commands to be run to validate container readiness. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How many times to try the probe before restarting the container (liveness probe) or marking the container as unhealthy (readiness probe). The default value is <code class="docutils literal notranslate"><span class="pre">3</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpGets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The definition of the httpget for this container as documented in the <code class="docutils literal notranslate"><span class="pre">httpget</span></code> block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Path to access on the HTTP server. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port number the container will expose. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Scheme to use for connecting to the host. Possible values are <code class="docutils literal notranslate"><span class="pre">Http</span></code> and <code class="docutils literal notranslate"><span class="pre">Https</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelaySeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of seconds after the container has started before liveness or readiness probes are initiated. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">periodSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How often (in seconds) to perform the probe. The default value is <code class="docutils literal notranslate"><span class="pre">10</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Minimum consecutive successes for the probe to be considered successful after having failed. The default value is <code class="docutils literal notranslate"><span class="pre">1</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of seconds after which the probe times out. The default value is <code class="docutils literal notranslate"><span class="pre">1</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">secureEnvironmentVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A list of sensitive environment variables to be set on the container. Specified as a map of name/value pairs. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The definition of a volume mount for this container as documented in the <code class="docutils literal notranslate"><span class="pre">volume</span></code> block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path on which this volume is to be mounted. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Container Group. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specify if the volume is to be mounted as read only or not. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">share_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure storage share that is to be mounted as a volume. This must be created on the storage account specified as above. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The access key for the Azure Storage account specified as above. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure storage account from which the volume is to be mounted. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>diagnostics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">logAnalytics</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">log_analytics</span></code> block as defined below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">logType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The log type which should be used. Possible values are <code class="docutils literal notranslate"><span class="pre">ContainerInsights</span></code> and <code class="docutils literal notranslate"><span class="pre">ContainerInstanceLogs</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Any metadata required for Log Analytics. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Workspace ID of the Log Analytics Workspace. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspaceKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Workspace Key of the Log Analytics Workspace. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a list of user managed identity ids to be assigned. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Managed Service Identity Type of this container group. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> (where Azure will generate a Service Principal for you), <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> where you can specify the Service Principal IDs in the <code class="docutils literal notranslate"><span class="pre">identity_ids</span></code> field, and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code> which assigns both a system managed identity as well as the specified user assigned identities. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>image_registry_credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password with which to connect to the registry. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The address to use to connect to the registry without protocol (“https”/”http”). For example: “myacr.acr.io”. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username with which to connect to the registry. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.containers">
<code class="sig-name descname">containers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.containers" title="Permalink to this definition">¶</a></dt>
<dd><p>The definition of a container that is part of the group as documented in the <code class="docutils literal notranslate"><span class="pre">container</span></code> block below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commands</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of commands which should be run on the container. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpu</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The required number of CPU cores of the containers. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environmentVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A list of environment variables to be set on the container. Specified as a map of name/value pairs. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpu</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">gpu</span></code> block as defined below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of GPUs which should be assigned to this container. Allowed values are <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, or <code class="docutils literal notranslate"><span class="pre">4</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Sku which should be used for the GPU. Possible values are <code class="docutils literal notranslate"><span class="pre">K80</span></code>, <code class="docutils literal notranslate"><span class="pre">P100</span></code>, or <code class="docutils literal notranslate"><span class="pre">V100</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The container image name. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">livenessProbe</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The definition of a readiness probe for this container as documented in the <code class="docutils literal notranslate"><span class="pre">liveness_probe</span></code> block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">execs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Commands to be run to validate container readiness. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How many times to try the probe before restarting the container (liveness probe) or marking the container as unhealthy (readiness probe). The default value is <code class="docutils literal notranslate"><span class="pre">3</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpGets</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The definition of the httpget for this container as documented in the <code class="docutils literal notranslate"><span class="pre">httpget</span></code> block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Path to access on the HTTP server. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port number the container will expose. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Scheme to use for connecting to the host. Possible values are <code class="docutils literal notranslate"><span class="pre">Http</span></code> and <code class="docutils literal notranslate"><span class="pre">Https</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelaySeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of seconds after the container has started before liveness or readiness probes are initiated. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">periodSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How often (in seconds) to perform the probe. The default value is <code class="docutils literal notranslate"><span class="pre">10</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Minimum consecutive successes for the probe to be considered successful after having failed. The default value is <code class="docutils literal notranslate"><span class="pre">1</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of seconds after which the probe times out. The default value is <code class="docutils literal notranslate"><span class="pre">1</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">memory</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The required memory of the containers in GB. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Container Group. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A set of public ports for the container. Changing this forces a new resource to be created. Set as documented in the <code class="docutils literal notranslate"><span class="pre">ports</span></code> block below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port number the container will expose. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The network protocol associated with port. Possible values are <code class="docutils literal notranslate"><span class="pre">TCP</span></code> &amp; <code class="docutils literal notranslate"><span class="pre">UDP</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">readinessProbe</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The definition of a readiness probe for this container as documented in the <code class="docutils literal notranslate"><span class="pre">readiness_probe</span></code> block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">execs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Commands to be run to validate container readiness. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How many times to try the probe before restarting the container (liveness probe) or marking the container as unhealthy (readiness probe). The default value is <code class="docutils literal notranslate"><span class="pre">3</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpGets</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The definition of the httpget for this container as documented in the <code class="docutils literal notranslate"><span class="pre">httpget</span></code> block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Path to access on the HTTP server. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port number the container will expose. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Scheme to use for connecting to the host. Possible values are <code class="docutils literal notranslate"><span class="pre">Http</span></code> and <code class="docutils literal notranslate"><span class="pre">Https</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelaySeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of seconds after the container has started before liveness or readiness probes are initiated. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">periodSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How often (in seconds) to perform the probe. The default value is <code class="docutils literal notranslate"><span class="pre">10</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Minimum consecutive successes for the probe to be considered successful after having failed. The default value is <code class="docutils literal notranslate"><span class="pre">1</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of seconds after which the probe times out. The default value is <code class="docutils literal notranslate"><span class="pre">1</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">secureEnvironmentVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A list of sensitive environment variables to be set on the container. Specified as a map of name/value pairs. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The definition of a volume mount for this container as documented in the <code class="docutils literal notranslate"><span class="pre">volume</span></code> block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path on which this volume is to be mounted. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Container Group. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specify if the volume is to be mounted as read only or not. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">share_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Azure storage share that is to be mounted as a volume. This must be created on the storage account specified as above. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The access key for the Azure Storage account specified as above. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Azure storage account from which the volume is to be mounted. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.diagnostics">
<code class="sig-name descname">diagnostics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.diagnostics" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">diagnostics</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">logAnalytics</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">log_analytics</span></code> block as defined below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">logType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The log type which should be used. Possible values are <code class="docutils literal notranslate"><span class="pre">ContainerInsights</span></code> and <code class="docutils literal notranslate"><span class="pre">ContainerInstanceLogs</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Any metadata required for Log Analytics. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Workspace ID of the Log Analytics Workspace. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspaceKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Workspace Key of the Log Analytics Workspace. Changing this forces a new resource to be created.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies a list of user managed identity ids to be assigned. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Managed Service Identity Type of this container group. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> (where Azure will generate a Service Principal for you), <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> where you can specify the Service Principal IDs in the <code class="docutils literal notranslate"><span class="pre">identity_ids</span></code> field, and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code> which assigns both a system managed identity as well as the specified user assigned identities. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.image_registry_credentials">
<code class="sig-name descname">image_registry_credentials</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.image_registry_credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">image_registry_credential</span></code> block as documented below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password with which to connect to the registry. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The address to use to connect to the registry without protocol (“https”/”http”). For example: “myacr.acr.io”. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username with which to connect to the registry. Changing this forces a new resource to be created.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">commands</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of commands which should be run on the container. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The required number of CPU cores of the containers. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environmentVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A list of environment variables to be set on the container. Specified as a map of name/value pairs. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gpu</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">gpu</span></code> block as defined below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of GPUs which should be assigned to this container. Allowed values are <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, or <code class="docutils literal notranslate"><span class="pre">4</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Sku which should be used for the GPU. Possible values are <code class="docutils literal notranslate"><span class="pre">K80</span></code>, <code class="docutils literal notranslate"><span class="pre">P100</span></code>, or <code class="docutils literal notranslate"><span class="pre">V100</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The container image name. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">livenessProbe</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The definition of a readiness probe for this container as documented in the <code class="docutils literal notranslate"><span class="pre">liveness_probe</span></code> block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">execs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Commands to be run to validate container readiness. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How many times to try the probe before restarting the container (liveness probe) or marking the container as unhealthy (readiness probe). The default value is <code class="docutils literal notranslate"><span class="pre">3</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpGets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The definition of the httpget for this container as documented in the <code class="docutils literal notranslate"><span class="pre">httpget</span></code> block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Path to access on the HTTP server. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port number the container will expose. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Scheme to use for connecting to the host. Possible values are <code class="docutils literal notranslate"><span class="pre">Http</span></code> and <code class="docutils literal notranslate"><span class="pre">Https</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelaySeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of seconds after the container has started before liveness or readiness probes are initiated. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">periodSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How often (in seconds) to perform the probe. The default value is <code class="docutils literal notranslate"><span class="pre">10</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Minimum consecutive successes for the probe to be considered successful after having failed. The default value is <code class="docutils literal notranslate"><span class="pre">1</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of seconds after which the probe times out. The default value is <code class="docutils literal notranslate"><span class="pre">1</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">memory</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The required memory of the containers in GB. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Container Group. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A set of public ports for the container. Changing this forces a new resource to be created. Set as documented in the <code class="docutils literal notranslate"><span class="pre">ports</span></code> block below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port number the container will expose. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The network protocol associated with port. Possible values are <code class="docutils literal notranslate"><span class="pre">TCP</span></code> &amp; <code class="docutils literal notranslate"><span class="pre">UDP</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">readinessProbe</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - The definition of a readiness probe for this container as documented in the <code class="docutils literal notranslate"><span class="pre">readiness_probe</span></code> block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">execs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Commands to be run to validate container readiness. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failureThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How many times to try the probe before restarting the container (liveness probe) or marking the container as unhealthy (readiness probe). The default value is <code class="docutils literal notranslate"><span class="pre">3</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpGets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The definition of the httpget for this container as documented in the <code class="docutils literal notranslate"><span class="pre">httpget</span></code> block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Path to access on the HTTP server. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port number the container will expose. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scheme</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Scheme to use for connecting to the host. Possible values are <code class="docutils literal notranslate"><span class="pre">Http</span></code> and <code class="docutils literal notranslate"><span class="pre">Https</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialDelaySeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of seconds after the container has started before liveness or readiness probes are initiated. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">periodSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How often (in seconds) to perform the probe. The default value is <code class="docutils literal notranslate"><span class="pre">10</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">successThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Minimum consecutive successes for the probe to be considered successful after having failed. The default value is <code class="docutils literal notranslate"><span class="pre">1</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeoutSeconds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of seconds after which the probe times out. The default value is <code class="docutils literal notranslate"><span class="pre">1</span></code> and the minimum value is <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">secureEnvironmentVariables</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A list of sensitive environment variables to be set on the container. Specified as a map of name/value pairs. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">volumes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The definition of a volume mount for this container as documented in the <code class="docutils literal notranslate"><span class="pre">volume</span></code> block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mountPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path on which this volume is to be mounted. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Container Group. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specify if the volume is to be mounted as read only or not. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">share_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure storage share that is to be mounted as a volume. This must be created on the storage account specified as above. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The access key for the Azure Storage account specified as above. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure storage account from which the volume is to be mounted. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>diagnostics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">logAnalytics</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">log_analytics</span></code> block as defined below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">logType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The log type which should be used. Possible values are <code class="docutils literal notranslate"><span class="pre">ContainerInsights</span></code> and <code class="docutils literal notranslate"><span class="pre">ContainerInstanceLogs</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metadata</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Any metadata required for Log Analytics. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Workspace ID of the Log Analytics Workspace. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">workspaceKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Workspace Key of the Log Analytics Workspace. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a list of user managed identity ids to be assigned. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Managed Service Identity Type of this container group. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> (where Azure will generate a Service Principal for you), <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> where you can specify the Service Principal IDs in the <code class="docutils literal notranslate"><span class="pre">identity_ids</span></code> field, and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code> which assigns both a system managed identity as well as the specified user assigned identities. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>image_registry_credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password with which to connect to the registry. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The address to use to connect to the registry without protocol (“https”/”http”). For example: “myacr.acr.io”. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username with which to connect to the registry. Changing this forces a new resource to be created.</p></li>
</ul>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">KubernetesCluster</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">addon_profile=None</em>, <em class="sig-param">api_server_authorized_ip_ranges=None</em>, <em class="sig-param">default_node_pool=None</em>, <em class="sig-param">dns_prefix=None</em>, <em class="sig-param">enable_pod_security_policy=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">kubernetes_version=None</em>, <em class="sig-param">linux_profile=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_profile=None</em>, <em class="sig-param">node_resource_group=None</em>, <em class="sig-param">private_link_enabled=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">role_based_access_control=None</em>, <em class="sig-param">service_principal=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">windows_profile=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Managed Kubernetes Cluster (also known as AKS / Azure Kubernetes Service)</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kubernetes_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kubernetes_cluster.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>addon_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">addon_profile</span></code> block as defined below.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">aciConnectorLinux</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">aci_connector_linux</span></code> block. For more details, please visit <a class="reference external" href="https://docs.microsoft.com/en-us/azure/aks/virtual-nodes-portal">Create and configure an AKS cluster to use virtual nodes</a>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the virtual node addon enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The subnet name for the virtual nodes to run. This is required when <code class="docutils literal notranslate"><span class="pre">aci_connector_linux</span></code> <code class="docutils literal notranslate"><span class="pre">enabled</span></code> argument is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">azurePolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">azure_policy</span></code> block as defined below. For more details please visit <a class="reference external" href="https://docs.microsoft.com/en-ie/azure/governance/policy/concepts/rego-for-aks">Understand Azure Policy for Azure Kubernetes Service</a></p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Azure Policy for Kubernetes Add On enabled?</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpApplicationRouting</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">http_application_routing</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is HTTP Application Routing Enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpApplicationRoutingZoneName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Zone Name of the HTTP Application Routing.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kubeDashboard</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">kube_dashboard</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Kubernetes Dashboard enabled?</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">omsAgent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">oms_agent</span></code> block as defined below. For more details, please visit <a class="reference external" href="https://docs.microsoft.com/en-us/azure/monitoring/monitoring-container-insights-onboard">How to onboard Azure Monitor for containers</a>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the OMS Agent Enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_analytics_workspace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Log Analytics Workspace which the OMS Agent should send data to. Must be present if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>default_node_pool</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Availability Zones across which the Node Pool should be spread.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_auto_scaling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should <a class="reference external" href="https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler">the Kubernetes Auto Scaler</a> be enabled for this Node Pool? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_node_public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should nodes in this Node Pool have a Public IP Address? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of nodes which should exist in this Node Pool. If specified this must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_pods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of nodes which should exist in this Node Pool. If specified this must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name which should be used for the default Kubernetes Node Pool. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The initial number of nodes which should exist in this Node Pool. If specified this must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code> and between <code class="docutils literal notranslate"><span class="pre">min_count</span></code> and <code class="docutils literal notranslate"><span class="pre">max_count</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of Kubernetes labels which should be applied to nodes in the Default Node Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g <code class="docutils literal notranslate"><span class="pre">key=value:NoSchedule</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the OS Disk which should be used for each agent in the Node Pool. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of tags to assign to the Node Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Node Pool which should be created. Possible values are <code class="docutils literal notranslate"><span class="pre">AvailabilitySet</span></code> and <code class="docutils literal notranslate"><span class="pre">VirtualMachineScaleSets</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">VirtualMachineScaleSets</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The size of the Virtual Machine, such as <code class="docutils literal notranslate"><span class="pre">Standard_DS2_v2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vnet_subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of a Subnet where the Kubernetes Node Pool should exist. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The principal id of the system assigned identity which is used by master components.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Tenant ID used for Azure Active Directory Application. If this isn’t specified the Tenant ID of the current Subscription is used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of identity used for the managed cluster. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
<p>The <strong>linux_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Admin Username for the Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssh_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">ssh_key</span></code> block. Only one is currently allowed. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Public SSH Key used to access the cluster. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>network_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dnsServiceIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - IP address within the Kubernetes service address range that will be used by cluster service discovery (kube-dns). This is required when <code class="docutils literal notranslate"><span class="pre">network_plugin</span></code> is set to <code class="docutils literal notranslate"><span class="pre">azure</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dockerBridgeCidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - IP address (in CIDR notation) used as the Docker bridge IP address on nodes. This is required when <code class="docutils literal notranslate"><span class="pre">network_plugin</span></code> is set to <code class="docutils literal notranslate"><span class="pre">azure</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerProfile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">load_balancer_profile</span></code> block. This can only be specified when <code class="docutils literal notranslate"><span class="pre">load_balancer_sku</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">effectiveOutboundIps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The outcome (resource IDs) of the specified arguments.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedOutboundIpCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Count of desired managed outbound IPs for the cluster load balancer. Must be in the range of [1, 100].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outboundIpAddressIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The ID of the Public IP Addresses which should be used for outbound communication for the cluster load balancer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outboundIpPrefixIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The ID of the outbound Public IP Address Prefixes which should be used for the cluster load balancer.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerSku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the SKU of the Load Balancer used for this Kubernetes Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkPlugin</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Network plugin to use for networking. Currently supported values are <code class="docutils literal notranslate"><span class="pre">azure</span></code> and <code class="docutils literal notranslate"><span class="pre">kubenet</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Sets up network policy to be used with Azure CNI. <a class="reference external" href="https://docs.microsoft.com/en-us/azure/aks/use-network-policies">Network policy allows us to control the traffic flow between pods</a>. Currently supported values are <code class="docutils literal notranslate"><span class="pre">calico</span></code> and <code class="docutils literal notranslate"><span class="pre">azure</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outboundType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The outbound (egress) routing method which should be used for this Kubernetes Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">loadBalancer</span></code> and <code class="docutils literal notranslate"><span class="pre">userDefinedRouting</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">loadBalancer</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">podCidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CIDR to use for pod IP addresses. This field can only be set when <code class="docutils literal notranslate"><span class="pre">network_plugin</span></code> is set to <code class="docutils literal notranslate"><span class="pre">kubenet</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceCidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Network Range used by the Kubernetes service. This is required when <code class="docutils literal notranslate"><span class="pre">network_plugin</span></code> is set to <code class="docutils literal notranslate"><span class="pre">azure</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>role_based_access_control</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">azure_active_directory</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">azure_active_directory</span></code> block.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">clientAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Client ID of an Azure Active Directory Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Server ID of an Azure Active Directory Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverAppSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Server Secret of an Azure Active Directory Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Tenant ID used for Azure Active Directory Application. If this isn’t specified the Tenant ID of the current Subscription is used.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is Role Based Access Control Enabled? Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>service_principal</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Client ID for the Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Client Secret for the Service Principal.</p></li>
</ul>
<p>The <strong>windows_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Admin Password for Windows VMs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Admin Username for Windows VMs.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.addon_profile">
<code class="sig-name descname">addon_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.addon_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">addon_profile</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">aciConnectorLinux</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">aci_connector_linux</span></code> block. For more details, please visit <a class="reference external" href="https://docs.microsoft.com/en-us/azure/aks/virtual-nodes-portal">Create and configure an AKS cluster to use virtual nodes</a>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the virtual node addon enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The subnet name for the virtual nodes to run. This is required when <code class="docutils literal notranslate"><span class="pre">aci_connector_linux</span></code> <code class="docutils literal notranslate"><span class="pre">enabled</span></code> argument is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">azurePolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">azure_policy</span></code> block as defined below. For more details please visit <a class="reference external" href="https://docs.microsoft.com/en-ie/azure/governance/policy/concepts/rego-for-aks">Understand Azure Policy for Azure Kubernetes Service</a></p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the Azure Policy for Kubernetes Add On enabled?</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpApplicationRouting</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">http_application_routing</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is HTTP Application Routing Enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpApplicationRoutingZoneName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Zone Name of the HTTP Application Routing.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kubeDashboard</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">kube_dashboard</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the Kubernetes Dashboard enabled?</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">omsAgent</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">oms_agent</span></code> block as defined below. For more details, please visit <a class="reference external" href="https://docs.microsoft.com/en-us/azure/monitoring/monitoring-container-insights-onboard">How to onboard Azure Monitor for containers</a>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the OMS Agent Enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_analytics_workspace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Log Analytics Workspace which the OMS Agent should send data to. Must be present if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of Availability Zones across which the Node Pool should be spread.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_auto_scaling</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should <a class="reference external" href="https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler">the Kubernetes Auto Scaler</a> be enabled for this Node Pool? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_node_public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should nodes in this Node Pool have a Public IP Address? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of nodes which should exist in this Node Pool. If specified this must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_pods</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The minimum number of nodes which should exist in this Node Pool. If specified this must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name which should be used for the default Kubernetes Node Pool. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The initial number of nodes which should exist in this Node Pool. If specified this must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code> and between <code class="docutils literal notranslate"><span class="pre">min_count</span></code> and <code class="docutils literal notranslate"><span class="pre">max_count</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_labels</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A map of Kubernetes labels which should be applied to nodes in the Default Node Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_taints</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g <code class="docutils literal notranslate"><span class="pre">key=value:NoSchedule</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the OS Disk which should be used for each agent in the Node Pool. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A mapping of tags to assign to the Node Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of Node Pool which should be created. Possible values are <code class="docutils literal notranslate"><span class="pre">AvailabilitySet</span></code> and <code class="docutils literal notranslate"><span class="pre">VirtualMachineScaleSets</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">VirtualMachineScaleSets</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The size of the Virtual Machine, such as <code class="docutils literal notranslate"><span class="pre">Standard_DS2_v2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vnet_subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of a Subnet where the Kubernetes Node Pool should exist. Changing this forces a new resource to be created.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Tenant ID used for Azure Active Directory Application. If this isn’t specified the Tenant ID of the current Subscription is used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of identity used for the managed cluster. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.kube_admin_config_raw">
<code class="sig-name descname">kube_admin_config_raw</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.kube_admin_config_raw" title="Permalink to this definition">¶</a></dt>
<dd><p>Raw Kubernetes config for the admin account to be used by <a class="reference external" href="https://kubernetes.io/docs/reference/kubectl/overview/">kubectl</a> and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.kube_admin_configs">
<code class="sig-name descname">kube_admin_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.kube_admin_configs" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.KubernetesCluster.kube_config_raw">
<code class="sig-name descname">kube_config_raw</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.kube_config_raw" title="Permalink to this definition">¶</a></dt>
<dd><p>Raw Kubernetes config to be used by <a class="reference external" href="https://kubernetes.io/docs/reference/kubectl/overview/">kubectl</a> and other compatible tools</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.kube_configs">
<code class="sig-name descname">kube_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.kube_configs" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.KubernetesCluster.kubernetes_version">
<code class="sig-name descname">kubernetes_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.kubernetes_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won’t auto-upgrade).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.linux_profile">
<code class="sig-name descname">linux_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.linux_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">linux_profile</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Admin Username for the Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssh_key</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - An <code class="docutils literal notranslate"><span class="pre">ssh_key</span></code> block. Only one is currently allowed. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyData</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Public SSH Key used to access the cluster. Changing this forces a new resource to be created.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">dnsServiceIp</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - IP address within the Kubernetes service address range that will be used by cluster service discovery (kube-dns). This is required when <code class="docutils literal notranslate"><span class="pre">network_plugin</span></code> is set to <code class="docutils literal notranslate"><span class="pre">azure</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dockerBridgeCidr</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - IP address (in CIDR notation) used as the Docker bridge IP address on nodes. This is required when <code class="docutils literal notranslate"><span class="pre">network_plugin</span></code> is set to <code class="docutils literal notranslate"><span class="pre">azure</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerProfile</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">load_balancer_profile</span></code> block. This can only be specified when <code class="docutils literal notranslate"><span class="pre">load_balancer_sku</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">effectiveOutboundIps</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The outcome (resource IDs) of the specified arguments.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedOutboundIpCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Count of desired managed outbound IPs for the cluster load balancer. Must be in the range of [1, 100].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outboundIpAddressIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The ID of the Public IP Addresses which should be used for outbound communication for the cluster load balancer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outboundIpPrefixIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The ID of the outbound Public IP Address Prefixes which should be used for the cluster load balancer.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerSku</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the SKU of the Load Balancer used for this Kubernetes Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkPlugin</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Network plugin to use for networking. Currently supported values are <code class="docutils literal notranslate"><span class="pre">azure</span></code> and <code class="docutils literal notranslate"><span class="pre">kubenet</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Sets up network policy to be used with Azure CNI. <a class="reference external" href="https://docs.microsoft.com/en-us/azure/aks/use-network-policies">Network policy allows us to control the traffic flow between pods</a>. Currently supported values are <code class="docutils literal notranslate"><span class="pre">calico</span></code> and <code class="docutils literal notranslate"><span class="pre">azure</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outboundType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The outbound (egress) routing method which should be used for this Kubernetes Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">loadBalancer</span></code> and <code class="docutils literal notranslate"><span class="pre">userDefinedRouting</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">loadBalancer</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">podCidr</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The CIDR to use for pod IP addresses. This field can only be set when <code class="docutils literal notranslate"><span class="pre">network_plugin</span></code> is set to <code class="docutils literal notranslate"><span class="pre">kubenet</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceCidr</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Network Range used by the Kubernetes service. This is required when <code class="docutils literal notranslate"><span class="pre">network_plugin</span></code> is set to <code class="docutils literal notranslate"><span class="pre">azure</span></code>. Changing this forces a new resource to be created.</p></li>
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
<dd><p>The FQDN for the Kubernetes Cluster when private link has been enabled, which is only resolvable inside the Virtual Network used by the Kubernetes Cluster.</p>
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
<li><p><code class="docutils literal notranslate"><span class="pre">azure_active_directory</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - An <code class="docutils literal notranslate"><span class="pre">azure_active_directory</span></code> block.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">clientAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Client ID of an Azure Active Directory Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Server ID of an Azure Active Directory Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverAppSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Server Secret of an Azure Active Directory Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Tenant ID used for Azure Active Directory Application. If this isn’t specified the Tenant ID of the current Subscription is used.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is Role Based Access Control Enabled? Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.service_principal">
<code class="sig-name descname">service_principal</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.service_principal" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">service_principal</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Client ID for the Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Client Secret for the Service Principal.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">admin_password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Admin Password for Windows VMs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Admin Username for Windows VMs.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.KubernetesCluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">addon_profile=None</em>, <em class="sig-param">api_server_authorized_ip_ranges=None</em>, <em class="sig-param">default_node_pool=None</em>, <em class="sig-param">dns_prefix=None</em>, <em class="sig-param">enable_pod_security_policy=None</em>, <em class="sig-param">fqdn=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">kube_admin_config_raw=None</em>, <em class="sig-param">kube_admin_configs=None</em>, <em class="sig-param">kube_config_raw=None</em>, <em class="sig-param">kube_configs=None</em>, <em class="sig-param">kubernetes_version=None</em>, <em class="sig-param">linux_profile=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_profile=None</em>, <em class="sig-param">node_resource_group=None</em>, <em class="sig-param">private_fqdn=None</em>, <em class="sig-param">private_link_enabled=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">role_based_access_control=None</em>, <em class="sig-param">service_principal=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">windows_profile=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing KubernetesCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>addon_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">addon_profile</span></code> block as defined below.</p></li>
<li><p><strong>api_server_authorized_ip_ranges</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The IP ranges to whitelist for incoming traffic to the masters.</p></li>
<li><p><strong>default_node_pool</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">default_node_pool</span></code> block as defined below.</p></li>
<li><p><strong>dns_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.</p></li>
<li><p><strong>enable_pod_security_policy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether Pod Security Policies are enabled. Note that this also requires role based access control to be enabled.</p></li>
<li><p><strong>fqdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FQDN of the Azure Kubernetes Managed Cluster.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>kube_admin_config_raw</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Raw Kubernetes config for the admin account to be used by <a class="reference external" href="https://kubernetes.io/docs/reference/kubectl/overview/">kubectl</a> and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.</p>
</p></li>
<li><p><strong>kube_admin_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">kube_admin_config</span></code> block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.</p></li>
<li><p><strong>kube_config_raw</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Raw Kubernetes config to be used by <a class="reference external" href="https://kubernetes.io/docs/reference/kubectl/overview/">kubectl</a> and other compatible tools</p>
</p></li>
<li><p><strong>kube_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">kube_config</span></code> block as defined below.</p></li>
<li><p><strong>kubernetes_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won’t auto-upgrade).</p></li>
<li><p><strong>linux_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">linux_profile</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">network_profile</span></code> block as defined below.</p></li>
<li><p><strong>node_resource_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Kubernetes Nodes should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>private_fqdn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FQDN for the Kubernetes Cluster when private link has been enabled, which is only resolvable inside the Virtual Network used by the Kubernetes Cluster.</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">aciConnectorLinux</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">aci_connector_linux</span></code> block. For more details, please visit <a class="reference external" href="https://docs.microsoft.com/en-us/azure/aks/virtual-nodes-portal">Create and configure an AKS cluster to use virtual nodes</a>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the virtual node addon enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnetName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The subnet name for the virtual nodes to run. This is required when <code class="docutils literal notranslate"><span class="pre">aci_connector_linux</span></code> <code class="docutils literal notranslate"><span class="pre">enabled</span></code> argument is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">azurePolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">azure_policy</span></code> block as defined below. For more details please visit <a class="reference external" href="https://docs.microsoft.com/en-ie/azure/governance/policy/concepts/rego-for-aks">Understand Azure Policy for Azure Kubernetes Service</a></p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Azure Policy for Kubernetes Add On enabled?</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpApplicationRouting</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">http_application_routing</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is HTTP Application Routing Enabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpApplicationRoutingZoneName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Zone Name of the HTTP Application Routing.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">kubeDashboard</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">kube_dashboard</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the Kubernetes Dashboard enabled?</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">omsAgent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">oms_agent</span></code> block as defined below. For more details, please visit <a class="reference external" href="https://docs.microsoft.com/en-us/azure/monitoring/monitoring-container-insights-onboard">How to onboard Azure Monitor for containers</a>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the OMS Agent Enabled?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log_analytics_workspace_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Log Analytics Workspace which the OMS Agent should send data to. Must be present if <code class="docutils literal notranslate"><span class="pre">enabled</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>default_node_pool</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">availability_zones</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Availability Zones across which the Node Pool should be spread.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_auto_scaling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should <a class="reference external" href="https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler">the Kubernetes Auto Scaler</a> be enabled for this Node Pool? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_node_public_ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should nodes in this Node Pool have a Public IP Address? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of nodes which should exist in this Node Pool. If specified this must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max_pods</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of pods that can run on each agent. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The minimum number of nodes which should exist in this Node Pool. If specified this must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name which should be used for the default Kubernetes Node Pool. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The initial number of nodes which should exist in this Node Pool. If specified this must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code> and between <code class="docutils literal notranslate"><span class="pre">min_count</span></code> and <code class="docutils literal notranslate"><span class="pre">max_count</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of Kubernetes labels which should be applied to nodes in the Default Node Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">node_taints</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g <code class="docutils literal notranslate"><span class="pre">key=value:NoSchedule</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the OS Disk which should be used for each agent in the Node Pool. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A mapping of tags to assign to the Node Pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Node Pool which should be created. Possible values are <code class="docutils literal notranslate"><span class="pre">AvailabilitySet</span></code> and <code class="docutils literal notranslate"><span class="pre">VirtualMachineScaleSets</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">VirtualMachineScaleSets</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vm_size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The size of the Virtual Machine, such as <code class="docutils literal notranslate"><span class="pre">Standard_DS2_v2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vnet_subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of a Subnet where the Kubernetes Node Pool should exist. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The principal id of the system assigned identity which is used by master components.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Tenant ID used for Azure Active Directory Application. If this isn’t specified the Tenant ID of the current Subscription is used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of identity used for the managed cluster. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
<p>The <strong>kube_admin_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">clientCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Base64 encoded public certificate used by clients to authenticate to the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clientKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Base64 encoded private key used by clients to authenticate to the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">clusterCaCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Base64 encoded public CA certificate used as the root of trust for the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Kubernetes cluster server host.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A password or token used to authenticate to the Kubernetes cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A username used to authenticate to the Kubernetes cluster.</p></li>
</ul>
<p>The <strong>kube_configs</strong> object supports the following:</p>
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
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Admin Username for the Cluster. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ssh_key</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">ssh_key</span></code> block. Only one is currently allowed. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Public SSH Key used to access the cluster. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
</ul>
<p>The <strong>network_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dnsServiceIp</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - IP address within the Kubernetes service address range that will be used by cluster service discovery (kube-dns). This is required when <code class="docutils literal notranslate"><span class="pre">network_plugin</span></code> is set to <code class="docutils literal notranslate"><span class="pre">azure</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dockerBridgeCidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - IP address (in CIDR notation) used as the Docker bridge IP address on nodes. This is required when <code class="docutils literal notranslate"><span class="pre">network_plugin</span></code> is set to <code class="docutils literal notranslate"><span class="pre">azure</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerProfile</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">load_balancer_profile</span></code> block. This can only be specified when <code class="docutils literal notranslate"><span class="pre">load_balancer_sku</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">effectiveOutboundIps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The outcome (resource IDs) of the specified arguments.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedOutboundIpCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Count of desired managed outbound IPs for the cluster load balancer. Must be in the range of [1, 100].</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outboundIpAddressIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The ID of the Public IP Addresses which should be used for outbound communication for the cluster load balancer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outboundIpPrefixIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The ID of the outbound Public IP Address Prefixes which should be used for the cluster load balancer.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerSku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the SKU of the Load Balancer used for this Kubernetes Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkPlugin</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Network plugin to use for networking. Currently supported values are <code class="docutils literal notranslate"><span class="pre">azure</span></code> and <code class="docutils literal notranslate"><span class="pre">kubenet</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkPolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Sets up network policy to be used with Azure CNI. <a class="reference external" href="https://docs.microsoft.com/en-us/azure/aks/use-network-policies">Network policy allows us to control the traffic flow between pods</a>. Currently supported values are <code class="docutils literal notranslate"><span class="pre">calico</span></code> and <code class="docutils literal notranslate"><span class="pre">azure</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">outboundType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The outbound (egress) routing method which should be used for this Kubernetes Cluster. Possible values are <code class="docutils literal notranslate"><span class="pre">loadBalancer</span></code> and <code class="docutils literal notranslate"><span class="pre">userDefinedRouting</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">loadBalancer</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">podCidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The CIDR to use for pod IP addresses. This field can only be set when <code class="docutils literal notranslate"><span class="pre">network_plugin</span></code> is set to <code class="docutils literal notranslate"><span class="pre">kubenet</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceCidr</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Network Range used by the Kubernetes service. This is required when <code class="docutils literal notranslate"><span class="pre">network_plugin</span></code> is set to <code class="docutils literal notranslate"><span class="pre">azure</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>role_based_access_control</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">azure_active_directory</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - An <code class="docutils literal notranslate"><span class="pre">azure_active_directory</span></code> block.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">clientAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Client ID of an Azure Active Directory Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverAppId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Server ID of an Azure Active Directory Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serverAppSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Server Secret of an Azure Active Directory Application.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Tenant ID used for Azure Active Directory Application. If this isn’t specified the Tenant ID of the current Subscription is used.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is Role Based Access Control Enabled? Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>service_principal</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">client_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Client ID for the Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">client_secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Client Secret for the Service Principal.</p></li>
</ul>
<p>The <strong>windows_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Admin Password for Windows VMs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Admin Username for Windows VMs.</p></li>
</ul>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">KubernetesClusterNodePool</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">availability_zones=None</em>, <em class="sig-param">enable_auto_scaling=None</em>, <em class="sig-param">enable_node_public_ip=None</em>, <em class="sig-param">kubernetes_cluster_id=None</em>, <em class="sig-param">max_count=None</em>, <em class="sig-param">max_pods=None</em>, <em class="sig-param">min_count=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">node_count=None</em>, <em class="sig-param">node_labels=None</em>, <em class="sig-param">node_taints=None</em>, <em class="sig-param">os_disk_size_gb=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vm_size=None</em>, <em class="sig-param">vnet_subnet_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Node Pool within a Kubernetes Cluster</p>
<blockquote>
<div><p><strong>NOTE:</strong> Multiple Node Pools are only supported when the Kubernetes Cluster is using Virtual Machine Scale Sets.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kubernetes_cluster_node_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/kubernetes_cluster_node_pool.html.markdown</a>.</p>
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
<li><p><strong>node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The initial number of nodes which should exist within this Node Pool. Valid values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code> and must be a value in the range <code class="docutils literal notranslate"><span class="pre">min_count</span></code> - <code class="docutils literal notranslate"><span class="pre">max_count</span></code>.</p></li>
<li><p><strong>node_labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Kubernetes labels which should be applied to nodes in this Node Pool.</p></li>
<li><p><strong>node_taints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g <code class="docutils literal notranslate"><span class="pre">key=value:NoSchedule</span></code>).</p></li>
<li><p><strong>os_disk_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Agent Operating System disk size in GB. Changing this forces a new resource to be created.</p></li>
<li><p><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Operating System which should be used for this Node Pool. Changing this forces a new resource to be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Linux</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vm_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU which should be used for the Virtual Machines used in this Node Pool. Changing this forces a new resource to be created.</p></li>
<li><p><strong>vnet_subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet where this Node Pool should exist.</p></li>
</ul>
</dd>
</dl>
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
<dd><p>The initial number of nodes which should exist within this Node Pool. Valid values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code> and must be a value in the range <code class="docutils literal notranslate"><span class="pre">min_count</span></code> - <code class="docutils literal notranslate"><span class="pre">max_count</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.node_labels">
<code class="sig-name descname">node_labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.node_labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Kubernetes labels which should be applied to nodes in this Node Pool.</p>
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
<dt id="pulumi_azure.containerservice.KubernetesClusterNodePool.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
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
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">availability_zones=None</em>, <em class="sig-param">enable_auto_scaling=None</em>, <em class="sig-param">enable_node_public_ip=None</em>, <em class="sig-param">kubernetes_cluster_id=None</em>, <em class="sig-param">max_count=None</em>, <em class="sig-param">max_pods=None</em>, <em class="sig-param">min_count=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">node_count=None</em>, <em class="sig-param">node_labels=None</em>, <em class="sig-param">node_taints=None</em>, <em class="sig-param">os_disk_size_gb=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vm_size=None</em>, <em class="sig-param">vnet_subnet_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesClusterNodePool.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>node_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The initial number of nodes which should exist within this Node Pool. Valid values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">100</span></code> and must be a value in the range <code class="docutils literal notranslate"><span class="pre">min_count</span></code> - <code class="docutils literal notranslate"><span class="pre">max_count</span></code>.</p></li>
<li><p><strong>node_labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Kubernetes labels which should be applied to nodes in this Node Pool.</p></li>
<li><p><strong>node_taints</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g <code class="docutils literal notranslate"><span class="pre">key=value:NoSchedule</span></code>).</p></li>
<li><p><strong>os_disk_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Agent Operating System disk size in GB. Changing this forces a new resource to be created.</p></li>
<li><p><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Operating System which should be used for this Node Pool. Changing this forces a new resource to be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Linux</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>vm_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU which should be used for the Virtual Machines used in this Node Pool. Changing this forces a new resource to be created.</p></li>
<li><p><strong>vnet_subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet where this Node Pool should exist.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">Registry</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_enabled=None</em>, <em class="sig-param">georeplication_locations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_rule_set=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Registry" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Container Registry.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_registry.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_registry.html.markdown</a>.</p>
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
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU name of the container registry. Possible values are  <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. <code class="docutils literal notranslate"><span class="pre">Classic</span></code> (which was previously <code class="docutils literal notranslate"><span class="pre">Basic</span></code>) is supported only for existing resources.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>network_rule_set</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behaviour for requests matching no rules. Either <code class="docutils literal notranslate"><span class="pre">Allow</span></code> or <code class="docutils literal notranslate"><span class="pre">Deny</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Allow</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ip_rule</span></code> blocks as defined below.</p>
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
<li><p><code class="docutils literal notranslate"><span class="pre">default_action</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The behaviour for requests matching no rules. Either <code class="docutils literal notranslate"><span class="pre">Allow</span></code> or <code class="docutils literal notranslate"><span class="pre">Deny</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Allow</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_rules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ip_rule</span></code> blocks as defined below.</p>
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
<dd><p>The SKU name of the container registry. Possible values are  <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. <code class="docutils literal notranslate"><span class="pre">Classic</span></code> (which was previously <code class="docutils literal notranslate"><span class="pre">Basic</span></code>) is supported only for existing resources.</p>
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
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">admin_enabled=None</em>, <em class="sig-param">admin_password=None</em>, <em class="sig-param">admin_username=None</em>, <em class="sig-param">georeplication_locations=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">login_server=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_rule_set=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Registry.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU name of the container registry. Possible values are  <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. <code class="docutils literal notranslate"><span class="pre">Classic</span></code> (which was previously <code class="docutils literal notranslate"><span class="pre">Basic</span></code>) is supported only for existing resources.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>network_rule_set</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default_action</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The behaviour for requests matching no rules. Either <code class="docutils literal notranslate"><span class="pre">Allow</span></code> or <code class="docutils literal notranslate"><span class="pre">Deny</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Allow</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_rules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ip_rule</span></code> blocks as defined below.</p>
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
<dt id="pulumi_azure.containerservice.RegistryWebhook">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">RegistryWebhook</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">actions=None</em>, <em class="sig-param">custom_headers=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">registry_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">service_uri=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebhook" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Container Registry Webhook.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_registry_webhook.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_registry_webhook.html.markdown</a>.</p>
</div></blockquote>
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
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the scope of repositories that can trigger an event. For example, <code class="docutils literal notranslate"><span class="pre">foo:*</span></code> means events for all tags under repository <code class="docutils literal notranslate"><span class="pre">foo</span></code>. <code class="docutils literal notranslate"><span class="pre">foo:bar</span></code> means events for ‘foo:bar’ only. <code class="docutils literal notranslate"><span class="pre">foo</span></code> is equivalent to <code class="docutils literal notranslate"><span class="pre">foo:latest</span></code>. Empty means all events.</p></li>
<li><p><strong>service_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the service URI for the Webhook to post notifications.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if this Webhook triggers notifications or not. Valid values: <code class="docutils literal notranslate"><span class="pre">enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">disabled</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">enabled</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.RegistryWebhook.actions">
<code class="sig-name descname">actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebhook.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of actions that trigger the Webhook to post notifications. At least one action needs to be specified. Valid values are: <code class="docutils literal notranslate"><span class="pre">push</span></code>, <code class="docutils literal notranslate"><span class="pre">delete</span></code>, <code class="docutils literal notranslate"><span class="pre">quarantine</span></code>, <code class="docutils literal notranslate"><span class="pre">chart_push</span></code>, <code class="docutils literal notranslate"><span class="pre">chart_delete</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.RegistryWebhook.custom_headers">
<code class="sig-name descname">custom_headers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebhook.custom_headers" title="Permalink to this definition">¶</a></dt>
<dd><p>Custom headers that will be added to the webhook notifications request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.RegistryWebhook.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebhook.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.RegistryWebhook.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebhook.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Container Registry Webhook. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.RegistryWebhook.registry_name">
<code class="sig-name descname">registry_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebhook.registry_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Name of Container registry this Webhook belongs to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.RegistryWebhook.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebhook.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Container Registry Webhook. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.RegistryWebhook.scope">
<code class="sig-name descname">scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebhook.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the scope of repositories that can trigger an event. For example, <code class="docutils literal notranslate"><span class="pre">foo:*</span></code> means events for all tags under repository <code class="docutils literal notranslate"><span class="pre">foo</span></code>. <code class="docutils literal notranslate"><span class="pre">foo:bar</span></code> means events for ‘foo:bar’ only. <code class="docutils literal notranslate"><span class="pre">foo</span></code> is equivalent to <code class="docutils literal notranslate"><span class="pre">foo:latest</span></code>. Empty means all events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.RegistryWebhook.service_uri">
<code class="sig-name descname">service_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebhook.service_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the service URI for the Webhook to post notifications.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.RegistryWebhook.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebhook.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if this Webhook triggers notifications or not. Valid values: <code class="docutils literal notranslate"><span class="pre">enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">disabled</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">enabled</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.RegistryWebhook.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">actions=None</em>, <em class="sig-param">custom_headers=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">registry_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">scope=None</em>, <em class="sig-param">service_uri=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebhook.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RegistryWebhook resource’s state with the given name, id, and optional extra
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
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the scope of repositories that can trigger an event. For example, <code class="docutils literal notranslate"><span class="pre">foo:*</span></code> means events for all tags under repository <code class="docutils literal notranslate"><span class="pre">foo</span></code>. <code class="docutils literal notranslate"><span class="pre">foo:bar</span></code> means events for ‘foo:bar’ only. <code class="docutils literal notranslate"><span class="pre">foo</span></code> is equivalent to <code class="docutils literal notranslate"><span class="pre">foo:latest</span></code>. Empty means all events.</p></li>
<li><p><strong>service_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the service URI for the Webhook to post notifications.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if this Webhook triggers notifications or not. Valid values: <code class="docutils literal notranslate"><span class="pre">enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">disabled</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">enabled</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.RegistryWebhook.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebhook.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.RegistryWebhook.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.RegistryWebhook.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_registry_webhook.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/container_registry_webhook.html.markdown</a>.</p>
</div></blockquote>
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
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the scope of repositories that can trigger an event. For example, <code class="docutils literal notranslate"><span class="pre">foo:*</span></code> means events for all tags under repository <code class="docutils literal notranslate"><span class="pre">foo</span></code>. <code class="docutils literal notranslate"><span class="pre">foo:bar</span></code> means events for ‘foo:bar’ only. <code class="docutils literal notranslate"><span class="pre">foo</span></code> is equivalent to <code class="docutils literal notranslate"><span class="pre">foo:latest</span></code>. Empty means all events.</p></li>
<li><p><strong>service_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the service URI for the Webhook to post notifications.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if this Webhook triggers notifications or not. Valid values: <code class="docutils literal notranslate"><span class="pre">enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">disabled</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">enabled</span></code>.</p></li>
</ul>
</dd>
</dl>
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
<dd><p>Specifies the scope of repositories that can trigger an event. For example, <code class="docutils literal notranslate"><span class="pre">foo:*</span></code> means events for all tags under repository <code class="docutils literal notranslate"><span class="pre">foo</span></code>. <code class="docutils literal notranslate"><span class="pre">foo:bar</span></code> means events for ‘foo:bar’ only. <code class="docutils literal notranslate"><span class="pre">foo</span></code> is equivalent to <code class="docutils literal notranslate"><span class="pre">foo:latest</span></code>. Empty means all events.</p>
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
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the scope of repositories that can trigger an event. For example, <code class="docutils literal notranslate"><span class="pre">foo:*</span></code> means events for all tags under repository <code class="docutils literal notranslate"><span class="pre">foo</span></code>. <code class="docutils literal notranslate"><span class="pre">foo:bar</span></code> means events for ‘foo:bar’ only. <code class="docutils literal notranslate"><span class="pre">foo</span></code> is equivalent to <code class="docutils literal notranslate"><span class="pre">foo:latest</span></code>. Empty means all events.</p></li>
<li><p><strong>service_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the service URI for the Webhook to post notifications.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies if this Webhook triggers notifications or not. Valid values: <code class="docutils literal notranslate"><span class="pre">enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">disabled</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">enabled</span></code>.</p></li>
</ul>
</dd>
</dl>
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

<dl class="function">
<dt id="pulumi_azure.containerservice.get_kubernetes_cluster">
<code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">get_kubernetes_cluster</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.get_kubernetes_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Managed Kubernetes Cluster (AKS).</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/kubernetes_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/kubernetes_cluster.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the managed Kubernetes Cluster.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group in which the managed Kubernetes Cluster exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.containerservice.get_kubernetes_service_versions">
<code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">get_kubernetes_service_versions</code><span class="sig-paren">(</span><em class="sig-param">include_preview=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">version_prefix=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.get_kubernetes_service_versions" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve the version of Kubernetes supported by Azure Kubernetes Service.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/kubernetes_service_versions.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/kubernetes_service_versions.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>include_preview</strong> (<em>bool</em>) – Should Preview versions of Kubernetes in AKS be included? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p><strong>location</strong> (<em>str</em>) – Specifies the location in which to query for versions.</p></li>
<li><p><strong>version_prefix</strong> (<em>str</em>) – A prefix filter for the versions of Kubernetes which should be returned; for example <code class="docutils literal notranslate"><span class="pre">1.</span></code> will return <code class="docutils literal notranslate"><span class="pre">1.9</span></code> to <code class="docutils literal notranslate"><span class="pre">1.14</span></code>, whereas <code class="docutils literal notranslate"><span class="pre">1.12</span></code> will return <code class="docutils literal notranslate"><span class="pre">1.12.2</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.containerservice.get_registry">
<code class="sig-prename descclassname">pulumi_azure.containerservice.</code><code class="sig-name descname">get_registry</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.get_registry" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Container Registry.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/container_registry.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/container_registry.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Container Registry.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where this Container Registry exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
