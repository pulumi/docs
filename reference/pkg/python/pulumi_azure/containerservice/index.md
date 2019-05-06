<div class="section" id="module-pulumi_azure.containerservice">
<span id="containerservice"></span><h1>containerservice<a class="headerlink" href="#module-pulumi_azure.containerservice" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.containerservice.</code><code class="descname">GetKubernetesClusterResult</code><span class="sig-paren">(</span><em>addon_profiles=None</em>, <em>agent_pool_profiles=None</em>, <em>dns_prefix=None</em>, <em>fqdn=None</em>, <em>kube_admin_configs=None</em>, <em>kube_admin_config_raw=None</em>, <em>kube_configs=None</em>, <em>kube_config_raw=None</em>, <em>kubernetes_version=None</em>, <em>linux_profiles=None</em>, <em>location=None</em>, <em>name=None</em>, <em>network_profiles=None</em>, <em>node_resource_group=None</em>, <em>resource_group_name=None</em>, <em>role_based_access_controls=None</em>, <em>service_principals=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getKubernetesCluster.</p>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.addon_profiles">
<code class="descname">addon_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.addon_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">addon_profile</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.agent_pool_profiles">
<code class="descname">agent_pool_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.agent_pool_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">agent_pool_profile</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.dns_prefix">
<code class="descname">dns_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.dns_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS Prefix of the managed Kubernetes cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.fqdn">
<code class="descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the Azure Kubernetes Managed Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.kube_admin_configs">
<code class="descname">kube_admin_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.kube_admin_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">kube_admin_config</span></code> block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.kube_admin_config_raw">
<code class="descname">kube_admin_config_raw</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.kube_admin_config_raw" title="Permalink to this definition">¶</a></dt>
<dd><p>Raw Kubernetes config for the admin account to be used by <a class="reference external" href="https://kubernetes.io/docs/reference/kubectl/overview/">kubectl</a> and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.kube_configs">
<code class="descname">kube_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.kube_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">kube_config</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.kube_config_raw">
<code class="descname">kube_config_raw</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.kube_config_raw" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64 encoded Kubernetes configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.kubernetes_version">
<code class="descname">kubernetes_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.kubernetes_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of Kubernetes used on the managed Kubernetes Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.linux_profiles">
<code class="descname">linux_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.linux_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">linux_profile</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which the managed Kubernetes Cluster exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name assigned to this pool of agents.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.network_profiles">
<code class="descname">network_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.network_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">network_profile</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.node_resource_group">
<code class="descname">node_resource_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.node_resource_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Auto-generated Resource Group containing AKS Cluster resources.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.role_based_access_controls">
<code class="descname">role_based_access_controls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.role_based_access_controls" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">role_based_access_control</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.service_principals">
<code class="descname">service_principals</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.service_principals" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">service_principal</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to this resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetKubernetesClusterResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetKubernetesClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.containerservice.GetRegistryResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.containerservice.</code><code class="descname">GetRegistryResult</code><span class="sig-paren">(</span><em>admin_enabled=None</em>, <em>admin_password=None</em>, <em>admin_username=None</em>, <em>location=None</em>, <em>login_server=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>storage_account_id=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRegistry.</p>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetRegistryResult.admin_enabled">
<code class="descname">admin_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.admin_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the Administrator account enabled for this Container Registry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetRegistryResult.admin_password">
<code class="descname">admin_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.admin_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password associated with the Container Registry Admin account - if the admin account is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetRegistryResult.admin_username">
<code class="descname">admin_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.admin_username" title="Permalink to this definition">¶</a></dt>
<dd><p>The Username associated with the Container Registry Admin account - if the admin account is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetRegistryResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which this Container Registry exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetRegistryResult.login_server">
<code class="descname">login_server</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.login_server" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL that can be used to log into the container registry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetRegistryResult.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU of this Container Registry, such as <code class="docutils literal notranslate"><span class="pre">Basic</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetRegistryResult.storage_account_id">
<code class="descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Storage Account used for this Container Registry. This is only returned for <code class="docutils literal notranslate"><span class="pre">Classic</span></code> SKU’s.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetRegistryResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags assigned to the Container Registry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.GetRegistryResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.GetRegistryResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.containerservice.Group">
<em class="property">class </em><code class="descclassname">pulumi_azure.containerservice.</code><code class="descname">Group</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>containers=None</em>, <em>diagnostics=None</em>, <em>dns_name_label=None</em>, <em>identity=None</em>, <em>image_registry_credentials=None</em>, <em>ip_address_type=None</em>, <em>location=None</em>, <em>name=None</em>, <em>os_type=None</em>, <em>resource_group_name=None</em>, <em>restart_policy=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage as an Azure Container Group instance.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>containers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The definition of a container that is part of the group as documented in the <code class="docutils literal notranslate"><span class="pre">container</span></code> block below. Changing this forces a new resource to be created.</li>
<li><strong>diagnostics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">diagnostics</span></code> block as documented below.</li>
<li><strong>dns_name_label</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The DNS label/name for the container groups IP.</li>
<li><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block.</li>
<li><strong>image_registry_credentials</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">image_registry_credential</span></code> block as documented below.</li>
<li><strong>ip_address_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ip address type of the container. <code class="docutils literal notranslate"><span class="pre">Public</span></code> is the only acceptable value at this time. Changing this forces a new resource to be created.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Container Group. Changing this forces a new resource to be created.</li>
<li><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OS for the container group. Allowed values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows</span></code>. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Container Group. Changing this forces a new resource to be created.</li>
<li><strong>restart_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Restart policy for the container group. Allowed values are <code class="docutils literal notranslate"><span class="pre">Always</span></code>, <code class="docutils literal notranslate"><span class="pre">Never</span></code>, <code class="docutils literal notranslate"><span class="pre">OnFailure</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Always</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.containers">
<code class="descname">containers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.containers" title="Permalink to this definition">¶</a></dt>
<dd><p>The definition of a container that is part of the group as documented in the <code class="docutils literal notranslate"><span class="pre">container</span></code> block below. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.diagnostics">
<code class="descname">diagnostics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.diagnostics" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">diagnostics</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.dns_name_label">
<code class="descname">dns_name_label</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.dns_name_label" title="Permalink to this definition">¶</a></dt>
<dd><p>The DNS label/name for the container groups IP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.fqdn">
<code class="descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the container group derived from <code class="docutils literal notranslate"><span class="pre">dns_name_label</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.identity">
<code class="descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.image_registry_credentials">
<code class="descname">image_registry_credentials</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.image_registry_credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">image_registry_credential</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.ip_address">
<code class="descname">ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The IP address allocated to the container group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.ip_address_type">
<code class="descname">ip_address_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.ip_address_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ip address type of the container. <code class="docutils literal notranslate"><span class="pre">Public</span></code> is the only acceptable value at this time. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Container Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.os_type">
<code class="descname">os_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.os_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The OS for the container group. Allowed values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Container Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.restart_policy">
<code class="descname">restart_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.restart_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Restart policy for the container group. Allowed values are <code class="docutils literal notranslate"><span class="pre">Always</span></code>, <code class="docutils literal notranslate"><span class="pre">Never</span></code>, <code class="docutils literal notranslate"><span class="pre">OnFailure</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Always</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Group.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Group.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.Group.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.Group.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.containerservice.KubernetesCluster">
<em class="property">class </em><code class="descclassname">pulumi_azure.containerservice.</code><code class="descname">KubernetesCluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>addon_profile=None</em>, <em>agent_pool_profile=None</em>, <em>dns_prefix=None</em>, <em>kubernetes_version=None</em>, <em>linux_profile=None</em>, <em>location=None</em>, <em>name=None</em>, <em>network_profile=None</em>, <em>resource_group_name=None</em>, <em>role_based_access_control=None</em>, <em>service_principal=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Managed Kubernetes Cluster (also known as AKS / Azure Kubernetes Service)</p>
<blockquote>
<div><strong>Note:</strong> All arguments including the client secret will be stored in the raw state as plain-text. <a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>addon_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">addon_profile</span></code> block.</li>
<li><strong>agent_pool_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">agent_pool_profile</span></code> block.  Currently only one agent pool can exist.</li>
<li><strong>dns_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.</li>
<li><strong>kubernetes_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won’t auto-upgrade).</li>
<li><strong>linux_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">linux_profile</span></code> block.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.</li>
<li><strong>network_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">network_profile</span></code> block.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.</li>
<li><strong>role_based_access_control</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">role_based_access_control</span></code> block. Changing this forces a new resource to be created.</li>
<li><strong>service_principal</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">service_principal</span></code> block as documented below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.addon_profile">
<code class="descname">addon_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.addon_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">addon_profile</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.agent_pool_profile">
<code class="descname">agent_pool_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.agent_pool_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">agent_pool_profile</span></code> block.  Currently only one agent pool can exist.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.dns_prefix">
<code class="descname">dns_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.dns_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>DNS prefix specified when creating the managed cluster. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.fqdn">
<code class="descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the Azure Kubernetes Managed Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.kube_admin_config">
<code class="descname">kube_admin_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.kube_admin_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">kube_admin_config</span></code> block as defined below. This is only available when Role Based Access Control with Azure Active Directory is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.kube_admin_config_raw">
<code class="descname">kube_admin_config_raw</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.kube_admin_config_raw" title="Permalink to this definition">¶</a></dt>
<dd><p>Raw Kubernetes config for the admin account to be used by <a class="reference external" href="https://kubernetes.io/docs/reference/kubectl/overview/">kubectl</a> and other compatible tools. This is only available when Role Based Access Control with Azure Active Directory is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.kube_config">
<code class="descname">kube_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.kube_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">kube_config</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.kube_config_raw">
<code class="descname">kube_config_raw</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.kube_config_raw" title="Permalink to this definition">¶</a></dt>
<dd><p>Raw Kubernetes config to be used by <a class="reference external" href="https://kubernetes.io/docs/reference/kubectl/overview/">kubectl</a> and other compatible tools</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.kubernetes_version">
<code class="descname">kubernetes_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.kubernetes_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of Kubernetes specified when creating the AKS managed cluster. If not specified, the latest recommended version will be used at provisioning time (but won’t auto-upgrade).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.linux_profile">
<code class="descname">linux_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.linux_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">linux_profile</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the Managed Kubernetes Cluster should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Managed Kubernetes Cluster to create. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.network_profile">
<code class="descname">network_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.network_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">network_profile</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.node_resource_group">
<code class="descname">node_resource_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.node_resource_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The auto-generated Resource Group which contains the resources for this Managed Kubernetes Cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Resource Group where the Managed Kubernetes Cluster should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.role_based_access_control">
<code class="descname">role_based_access_control</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.role_based_access_control" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">role_based_access_control</span></code> block. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.service_principal">
<code class="descname">service_principal</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.service_principal" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">service_principal</span></code> block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.KubernetesCluster.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.KubernetesCluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.KubernetesCluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.KubernetesCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.containerservice.Registry">
<em class="property">class </em><code class="descclassname">pulumi_azure.containerservice.</code><code class="descname">Registry</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>admin_enabled=None</em>, <em>georeplication_locations=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>storage_account=None</em>, <em>storage_account_id=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Registry" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Container Registry.</p>
<blockquote>
<div><strong>Note:</strong> All arguments including the access key will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>admin_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the admin user is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>georeplication_locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Azure locations where the container registry should be geo-replicated.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Container Registry. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Container Registry. Changing this forces a new resource to be created.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU name of the the container registry. Possible values are <code class="docutils literal notranslate"><span class="pre">Classic</span></code> (which was previously <code class="docutils literal notranslate"><span class="pre">Basic</span></code>), <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>.</li>
<li><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.admin_enabled">
<code class="descname">admin_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.admin_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the admin user is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.admin_password">
<code class="descname">admin_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.admin_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password associated with the Container Registry Admin account - if the admin account is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.admin_username">
<code class="descname">admin_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.admin_username" title="Permalink to this definition">¶</a></dt>
<dd><p>The Username associated with the Container Registry Admin account - if the admin account is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.georeplication_locations">
<code class="descname">georeplication_locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.georeplication_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Azure locations where the container registry should be geo-replicated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.login_server">
<code class="descname">login_server</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.login_server" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL that can be used to log into the container registry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Container Registry. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Container Registry. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU name of the the container registry. Possible values are <code class="docutils literal notranslate"><span class="pre">Classic</span></code> (which was previously <code class="docutils literal notranslate"><span class="pre">Basic</span></code>), <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.storage_account_id">
<code class="descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a Storage Account which must be located in the same Azure Region as the Container Registry.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Registry.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Registry.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.Registry.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Registry.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.Registry.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Registry.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_azure.containerservice.Service">
<em class="property">class </em><code class="descclassname">pulumi_azure.containerservice.</code><code class="descname">Service</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>agent_pool_profile=None</em>, <em>diagnostics_profile=None</em>, <em>linux_profile=None</em>, <em>location=None</em>, <em>master_profile=None</em>, <em>name=None</em>, <em>orchestration_platform=None</em>, <em>resource_group_name=None</em>, <em>service_principal=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Container Service Instance</p>
<blockquote>
<div><p><strong>NOTE:</strong> All arguments including the client secret will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
<p><strong>DEPRECATED:</strong> <a class="reference external" href="https://azure.microsoft.com/en-us/updates/azure-container-service-will-retire-on-january-31-2020/">Azure Container Service (ACS) has been deprecated by Azure in favour of Azure (Managed) Kubernetes Service (AKS)</a>. Support for ACS will be removed in the next major version of the AzureRM Provider (2.0) - and we <strong>strongly recommend</strong> you consider using Azure Kubernetes Service (AKS) for new deployments.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>agent_pool_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Agent Pool Profile’s block as documented below.</li>
<li><strong>diagnostics_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A VM Diagnostics Profile block as documented below.</li>
<li><strong>linux_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Linux Profile block as documented below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the Container Service instance should be created. Changing this forces a new resource to be created.</li>
<li><strong>master_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Master Profile block as documented below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique name of the agent pool profile in the context of the subscription and resource group.</li>
<li><strong>orchestration_platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Container Orchestration Platform to use. Currently can be either <code class="docutils literal notranslate"><span class="pre">DCOS</span></code>, <code class="docutils literal notranslate"><span class="pre">Kubernetes</span></code> or <code class="docutils literal notranslate"><span class="pre">Swarm</span></code>. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>service_principal</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Service Principal block as documented below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.agent_pool_profile">
<code class="descname">agent_pool_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.agent_pool_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A Agent Pool Profile’s block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.diagnostics_profile">
<code class="descname">diagnostics_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.diagnostics_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A VM Diagnostics Profile block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.linux_profile">
<code class="descname">linux_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.linux_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A Linux Profile block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the Container Service instance should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.master_profile">
<code class="descname">master_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.master_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A Master Profile block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique name of the agent pool profile in the context of the subscription and resource group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.orchestration_platform">
<code class="descname">orchestration_platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.orchestration_platform" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Container Orchestration Platform to use. Currently can be either <code class="docutils literal notranslate"><span class="pre">DCOS</span></code>, <code class="docutils literal notranslate"><span class="pre">Kubernetes</span></code> or <code class="docutils literal notranslate"><span class="pre">Swarm</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the resource group where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.service_principal">
<code class="descname">service_principal</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.service_principal" title="Permalink to this definition">¶</a></dt>
<dd><p>A Service Principal block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.containerservice.Service.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.containerservice.Service.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.containerservice.Service.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.containerservice.Service.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_azure.containerservice.get_kubernetes_cluster">
<code class="descclassname">pulumi_azure.containerservice.</code><code class="descname">get_kubernetes_cluster</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.get_kubernetes_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Managed Kubernetes Cluster (AKS).</p>
<blockquote>
<div><strong>Note:</strong> All arguments including the client secret will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.containerservice.get_registry">
<code class="descclassname">pulumi_azure.containerservice.</code><code class="descname">get_registry</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.containerservice.get_registry" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Container Registry.</p>
</dd></dl>

</div>
