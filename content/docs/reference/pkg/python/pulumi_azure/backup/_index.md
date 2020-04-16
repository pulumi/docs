---
title: Module backup
title_tag: Module backup | Package pulumi_azure | Python SDK
linktitle: backup
notitle: true
---

<div class="section" id="backup">
<h1>backup<a class="headerlink" href="#backup" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.backup"></span><dl class="class">
<dt id="pulumi_azure.backup.AwaitableGetPolicyVMResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.backup.</code><code class="sig-name descname">AwaitableGetPolicyVMResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.AwaitableGetPolicyVMResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.backup.ContainerStorageAccount">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.backup.</code><code class="sig-name descname">ContainerStorageAccount</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.ContainerStorageAccount" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages registration of a storage account with Azure Backup. Storage accounts must be registered with an Azure Recovery Vault in order to backup file shares within the storage account. Registering a storage account with a vault creates what is known as a protection container within Azure Recovery Services. Once the container is created, Azure file shares within the storage account can be backed up using the <code class="docutils literal notranslate"><span class="pre">backup.ProtectedFileShare</span></code> resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Azure Backup for Azure File Shares is currently in public preview. During the preview, the service is subject to additional limitations and unsupported backup scenarios. <a class="reference external" href="https://docs.microsoft.com/en-us/azure/backup/backup-azure-files#limitations-for-azure-file-share-backup-during-preview">Read More</a></p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vault where the storage account will be registered.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the resource group where the vault is located.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Azure Resource ID of the storage account to be registered</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.backup.ContainerStorageAccount.recovery_vault_name">
<code class="sig-name descname">recovery_vault_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.ContainerStorageAccount.recovery_vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the vault where the storage account will be registered.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.ContainerStorageAccount.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.ContainerStorageAccount.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the resource group where the vault is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.ContainerStorageAccount.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.ContainerStorageAccount.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Azure Resource ID of the storage account to be registered</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.backup.ContainerStorageAccount.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_account_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.ContainerStorageAccount.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ContainerStorageAccount resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vault where the storage account will be registered.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the resource group where the vault is located.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Azure Resource ID of the storage account to be registered</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.backup.ContainerStorageAccount.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.ContainerStorageAccount.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.backup.ContainerStorageAccount.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.ContainerStorageAccount.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.backup.GetPolicyVMResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.backup.</code><code class="sig-name descname">GetPolicyVMResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.GetPolicyVMResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPolicyVM.</p>
<dl class="attribute">
<dt id="pulumi_azure.backup.GetPolicyVMResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.GetPolicyVMResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.GetPolicyVMResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.GetPolicyVMResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.backup.PolicyFileShare">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.backup.</code><code class="sig-name descname">PolicyFileShare</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backup=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">retention_daily=None</em>, <em class="sig-param">timezone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.PolicyFileShare" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure File Share Backup Policy within a Recovery Services vault.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Azure Backup for Azure File Shares is currently in public preview. During the preview, the service is subject to additional limitations and unsupported backup scenarios. <a class="reference external" href="https://docs.microsoft.com/en-us/azure/backup/backup-azure-files#limitations-for-azure-file-share-backup-during-preview">Read More</a></p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backup</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the Policy backup frequency and times as documented in the <code class="docutils literal notranslate"><span class="pre">backup</span></code> block below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the policy. Changing this forces a new resource to be created.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the policy. Changing this forces a new resource to be created.</p></li>
<li><p><strong>retention_daily</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the policy daily retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_daily</span></code> block below.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the timezone. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code></p></li>
</ul>
</dd>
</dl>
<p>The <strong>backup</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">frequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Sets the backup frequency. Currently, only <code class="docutils literal notranslate"><span class="pre">Daily</span></code> is supported</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>retention_daily</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of daily backups to keep. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">180</span></code> (inclusive)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.backup.PolicyFileShare.backup">
<code class="sig-name descname">backup</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.PolicyFileShare.backup" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the Policy backup frequency and times as documented in the <code class="docutils literal notranslate"><span class="pre">backup</span></code> block below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">frequency</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Sets the backup frequency. Currently, only <code class="docutils literal notranslate"><span class="pre">Daily</span></code> is supported</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.PolicyFileShare.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.PolicyFileShare.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the policy. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.PolicyFileShare.recovery_vault_name">
<code class="sig-name descname">recovery_vault_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.PolicyFileShare.recovery_vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.PolicyFileShare.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.PolicyFileShare.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the policy. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.PolicyFileShare.retention_daily">
<code class="sig-name descname">retention_daily</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.PolicyFileShare.retention_daily" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the policy daily retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_daily</span></code> block below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of daily backups to keep. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">180</span></code> (inclusive)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.PolicyFileShare.timezone">
<code class="sig-name descname">timezone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.PolicyFileShare.timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the timezone. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.backup.PolicyFileShare.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backup=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">retention_daily=None</em>, <em class="sig-param">timezone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.PolicyFileShare.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PolicyFileShare resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backup</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the Policy backup frequency and times as documented in the <code class="docutils literal notranslate"><span class="pre">backup</span></code> block below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the policy. Changing this forces a new resource to be created.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the policy. Changing this forces a new resource to be created.</p></li>
<li><p><strong>retention_daily</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the policy daily retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_daily</span></code> block below.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the timezone. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code></p></li>
</ul>
</dd>
</dl>
<p>The <strong>backup</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">frequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Sets the backup frequency. Currently, only <code class="docutils literal notranslate"><span class="pre">Daily</span></code> is supported</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>retention_daily</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of daily backups to keep. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">180</span></code> (inclusive)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.backup.PolicyFileShare.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.PolicyFileShare.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.backup.PolicyFileShare.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.PolicyFileShare.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.backup.PolicyVM">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.backup.</code><code class="sig-name descname">PolicyVM</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backup=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">retention_daily=None</em>, <em class="sig-param">retention_monthly=None</em>, <em class="sig-param">retention_weekly=None</em>, <em class="sig-param">retention_yearly=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">timezone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.PolicyVM" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Backup VM Backup Policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backup</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the Policy backup frequency, times &amp; days as documented in the <code class="docutils literal notranslate"><span class="pre">backup</span></code> block below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Backup Policy. Changing this forces a new resource to be created.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the policy. Changing this forces a new resource to be created.</p></li>
<li><p><strong>retention_daily</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the policy daily retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_daily</span></code> block below. Required when backup frequency is <code class="docutils literal notranslate"><span class="pre">Daily</span></code>.</p></li>
<li><p><strong>retention_monthly</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the policy monthly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_monthly</span></code> block below.</p></li>
<li><p><strong>retention_weekly</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the policy weekly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_weekly</span></code> block below. Required when backup frequency is <code class="docutils literal notranslate"><span class="pre">Weekly</span></code>.</p></li>
<li><p><strong>retention_yearly</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the policy yearly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_yearly</span></code> block below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the timezone. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code></p></li>
</ul>
</dd>
</dl>
<p>The <strong>backup</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">frequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Sets the backup frequency. Must be either <code class="docutils literal notranslate"><span class="pre">Daily</span></code> or<code class="docutils literal notranslate"><span class="pre">Weekly</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The time of day to perform the backup in 24hour format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The weekday backups to retain . Must be one of <code class="docutils literal notranslate"><span class="pre">Sunday</span></code>, <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Thursday</span></code>, <code class="docutils literal notranslate"><span class="pre">Friday</span></code> or <code class="docutils literal notranslate"><span class="pre">Saturday</span></code>.</p></li>
</ul>
<p>The <strong>retention_daily</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of yearly backups to keep. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">9999</span></code></p></li>
</ul>
<p>The <strong>retention_monthly</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of yearly backups to keep. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">9999</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The weekday backups to retain . Must be one of <code class="docutils literal notranslate"><span class="pre">Sunday</span></code>, <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Thursday</span></code>, <code class="docutils literal notranslate"><span class="pre">Friday</span></code> or <code class="docutils literal notranslate"><span class="pre">Saturday</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weeks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The weeks of the month to retain backups of. Must be one of <code class="docutils literal notranslate"><span class="pre">First</span></code>, <code class="docutils literal notranslate"><span class="pre">Second</span></code>, <code class="docutils literal notranslate"><span class="pre">Third</span></code>, <code class="docutils literal notranslate"><span class="pre">Fourth</span></code>, <code class="docutils literal notranslate"><span class="pre">Last</span></code>.</p></li>
</ul>
<p>The <strong>retention_weekly</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of yearly backups to keep. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">9999</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The weekday backups to retain . Must be one of <code class="docutils literal notranslate"><span class="pre">Sunday</span></code>, <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Thursday</span></code>, <code class="docutils literal notranslate"><span class="pre">Friday</span></code> or <code class="docutils literal notranslate"><span class="pre">Saturday</span></code>.</p></li>
</ul>
<p>The <strong>retention_yearly</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of yearly backups to keep. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">9999</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">months</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The months of the year to retain backups of. Must be one of <code class="docutils literal notranslate"><span class="pre">January</span></code>, <code class="docutils literal notranslate"><span class="pre">February</span></code>, <code class="docutils literal notranslate"><span class="pre">March</span></code>, <code class="docutils literal notranslate"><span class="pre">April</span></code>, <code class="docutils literal notranslate"><span class="pre">May</span></code>, <code class="docutils literal notranslate"><span class="pre">June</span></code>, <code class="docutils literal notranslate"><span class="pre">July</span></code>, <code class="docutils literal notranslate"><span class="pre">Augest</span></code>, <code class="docutils literal notranslate"><span class="pre">September</span></code>, <code class="docutils literal notranslate"><span class="pre">October</span></code>, <code class="docutils literal notranslate"><span class="pre">November</span></code> and <code class="docutils literal notranslate"><span class="pre">December</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The weekday backups to retain . Must be one of <code class="docutils literal notranslate"><span class="pre">Sunday</span></code>, <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Thursday</span></code>, <code class="docutils literal notranslate"><span class="pre">Friday</span></code> or <code class="docutils literal notranslate"><span class="pre">Saturday</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weeks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The weeks of the month to retain backups of. Must be one of <code class="docutils literal notranslate"><span class="pre">First</span></code>, <code class="docutils literal notranslate"><span class="pre">Second</span></code>, <code class="docutils literal notranslate"><span class="pre">Third</span></code>, <code class="docutils literal notranslate"><span class="pre">Fourth</span></code>, <code class="docutils literal notranslate"><span class="pre">Last</span></code>.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.backup.PolicyVM.backup">
<code class="sig-name descname">backup</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.PolicyVM.backup" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the Policy backup frequency, times &amp; days as documented in the <code class="docutils literal notranslate"><span class="pre">backup</span></code> block below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">frequency</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Sets the backup frequency. Must be either <code class="docutils literal notranslate"><span class="pre">Daily</span></code> or<code class="docutils literal notranslate"><span class="pre">Weekly</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The time of day to perform the backup in 24hour format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The weekday backups to retain . Must be one of <code class="docutils literal notranslate"><span class="pre">Sunday</span></code>, <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Thursday</span></code>, <code class="docutils literal notranslate"><span class="pre">Friday</span></code> or <code class="docutils literal notranslate"><span class="pre">Saturday</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.PolicyVM.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.PolicyVM.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Backup Policy. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.PolicyVM.recovery_vault_name">
<code class="sig-name descname">recovery_vault_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.PolicyVM.recovery_vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.PolicyVM.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.PolicyVM.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the policy. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.PolicyVM.retention_daily">
<code class="sig-name descname">retention_daily</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.PolicyVM.retention_daily" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the policy daily retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_daily</span></code> block below. Required when backup frequency is <code class="docutils literal notranslate"><span class="pre">Daily</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of yearly backups to keep. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">9999</span></code></p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.PolicyVM.retention_monthly">
<code class="sig-name descname">retention_monthly</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.PolicyVM.retention_monthly" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the policy monthly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_monthly</span></code> block below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of yearly backups to keep. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">9999</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The weekday backups to retain . Must be one of <code class="docutils literal notranslate"><span class="pre">Sunday</span></code>, <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Thursday</span></code>, <code class="docutils literal notranslate"><span class="pre">Friday</span></code> or <code class="docutils literal notranslate"><span class="pre">Saturday</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weeks</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The weeks of the month to retain backups of. Must be one of <code class="docutils literal notranslate"><span class="pre">First</span></code>, <code class="docutils literal notranslate"><span class="pre">Second</span></code>, <code class="docutils literal notranslate"><span class="pre">Third</span></code>, <code class="docutils literal notranslate"><span class="pre">Fourth</span></code>, <code class="docutils literal notranslate"><span class="pre">Last</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.PolicyVM.retention_weekly">
<code class="sig-name descname">retention_weekly</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.PolicyVM.retention_weekly" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the policy weekly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_weekly</span></code> block below. Required when backup frequency is <code class="docutils literal notranslate"><span class="pre">Weekly</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of yearly backups to keep. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">9999</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The weekday backups to retain . Must be one of <code class="docutils literal notranslate"><span class="pre">Sunday</span></code>, <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Thursday</span></code>, <code class="docutils literal notranslate"><span class="pre">Friday</span></code> or <code class="docutils literal notranslate"><span class="pre">Saturday</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.PolicyVM.retention_yearly">
<code class="sig-name descname">retention_yearly</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.PolicyVM.retention_yearly" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the policy yearly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_yearly</span></code> block below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of yearly backups to keep. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">9999</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">months</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The months of the year to retain backups of. Must be one of <code class="docutils literal notranslate"><span class="pre">January</span></code>, <code class="docutils literal notranslate"><span class="pre">February</span></code>, <code class="docutils literal notranslate"><span class="pre">March</span></code>, <code class="docutils literal notranslate"><span class="pre">April</span></code>, <code class="docutils literal notranslate"><span class="pre">May</span></code>, <code class="docutils literal notranslate"><span class="pre">June</span></code>, <code class="docutils literal notranslate"><span class="pre">July</span></code>, <code class="docutils literal notranslate"><span class="pre">Augest</span></code>, <code class="docutils literal notranslate"><span class="pre">September</span></code>, <code class="docutils literal notranslate"><span class="pre">October</span></code>, <code class="docutils literal notranslate"><span class="pre">November</span></code> and <code class="docutils literal notranslate"><span class="pre">December</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The weekday backups to retain . Must be one of <code class="docutils literal notranslate"><span class="pre">Sunday</span></code>, <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Thursday</span></code>, <code class="docutils literal notranslate"><span class="pre">Friday</span></code> or <code class="docutils literal notranslate"><span class="pre">Saturday</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weeks</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The weeks of the month to retain backups of. Must be one of <code class="docutils literal notranslate"><span class="pre">First</span></code>, <code class="docutils literal notranslate"><span class="pre">Second</span></code>, <code class="docutils literal notranslate"><span class="pre">Third</span></code>, <code class="docutils literal notranslate"><span class="pre">Fourth</span></code>, <code class="docutils literal notranslate"><span class="pre">Last</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.PolicyVM.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.PolicyVM.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.PolicyVM.timezone">
<code class="sig-name descname">timezone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.PolicyVM.timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the timezone. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.backup.PolicyVM.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backup=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">retention_daily=None</em>, <em class="sig-param">retention_monthly=None</em>, <em class="sig-param">retention_weekly=None</em>, <em class="sig-param">retention_yearly=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">timezone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.PolicyVM.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PolicyVM resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backup</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the Policy backup frequency, times &amp; days as documented in the <code class="docutils literal notranslate"><span class="pre">backup</span></code> block below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Backup Policy. Changing this forces a new resource to be created.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the policy. Changing this forces a new resource to be created.</p></li>
<li><p><strong>retention_daily</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the policy daily retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_daily</span></code> block below. Required when backup frequency is <code class="docutils literal notranslate"><span class="pre">Daily</span></code>.</p></li>
<li><p><strong>retention_monthly</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the policy monthly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_monthly</span></code> block below.</p></li>
<li><p><strong>retention_weekly</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the policy weekly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_weekly</span></code> block below. Required when backup frequency is <code class="docutils literal notranslate"><span class="pre">Weekly</span></code>.</p></li>
<li><p><strong>retention_yearly</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the policy yearly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_yearly</span></code> block below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the timezone. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code></p></li>
</ul>
</dd>
</dl>
<p>The <strong>backup</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">frequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Sets the backup frequency. Must be either <code class="docutils literal notranslate"><span class="pre">Daily</span></code> or<code class="docutils literal notranslate"><span class="pre">Weekly</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The time of day to perform the backup in 24hour format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The weekday backups to retain . Must be one of <code class="docutils literal notranslate"><span class="pre">Sunday</span></code>, <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Thursday</span></code>, <code class="docutils literal notranslate"><span class="pre">Friday</span></code> or <code class="docutils literal notranslate"><span class="pre">Saturday</span></code>.</p></li>
</ul>
<p>The <strong>retention_daily</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of yearly backups to keep. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">9999</span></code></p></li>
</ul>
<p>The <strong>retention_monthly</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of yearly backups to keep. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">9999</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The weekday backups to retain . Must be one of <code class="docutils literal notranslate"><span class="pre">Sunday</span></code>, <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Thursday</span></code>, <code class="docutils literal notranslate"><span class="pre">Friday</span></code> or <code class="docutils literal notranslate"><span class="pre">Saturday</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weeks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The weeks of the month to retain backups of. Must be one of <code class="docutils literal notranslate"><span class="pre">First</span></code>, <code class="docutils literal notranslate"><span class="pre">Second</span></code>, <code class="docutils literal notranslate"><span class="pre">Third</span></code>, <code class="docutils literal notranslate"><span class="pre">Fourth</span></code>, <code class="docutils literal notranslate"><span class="pre">Last</span></code>.</p></li>
</ul>
<p>The <strong>retention_weekly</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of yearly backups to keep. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">9999</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The weekday backups to retain . Must be one of <code class="docutils literal notranslate"><span class="pre">Sunday</span></code>, <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Thursday</span></code>, <code class="docutils literal notranslate"><span class="pre">Friday</span></code> or <code class="docutils literal notranslate"><span class="pre">Saturday</span></code>.</p></li>
</ul>
<p>The <strong>retention_yearly</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of yearly backups to keep. Must be between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">9999</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">months</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The months of the year to retain backups of. Must be one of <code class="docutils literal notranslate"><span class="pre">January</span></code>, <code class="docutils literal notranslate"><span class="pre">February</span></code>, <code class="docutils literal notranslate"><span class="pre">March</span></code>, <code class="docutils literal notranslate"><span class="pre">April</span></code>, <code class="docutils literal notranslate"><span class="pre">May</span></code>, <code class="docutils literal notranslate"><span class="pre">June</span></code>, <code class="docutils literal notranslate"><span class="pre">July</span></code>, <code class="docutils literal notranslate"><span class="pre">Augest</span></code>, <code class="docutils literal notranslate"><span class="pre">September</span></code>, <code class="docutils literal notranslate"><span class="pre">October</span></code>, <code class="docutils literal notranslate"><span class="pre">November</span></code> and <code class="docutils literal notranslate"><span class="pre">December</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The weekday backups to retain . Must be one of <code class="docutils literal notranslate"><span class="pre">Sunday</span></code>, <code class="docutils literal notranslate"><span class="pre">Monday</span></code>, <code class="docutils literal notranslate"><span class="pre">Tuesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Wednesday</span></code>, <code class="docutils literal notranslate"><span class="pre">Thursday</span></code>, <code class="docutils literal notranslate"><span class="pre">Friday</span></code> or <code class="docutils literal notranslate"><span class="pre">Saturday</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weeks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The weeks of the month to retain backups of. Must be one of <code class="docutils literal notranslate"><span class="pre">First</span></code>, <code class="docutils literal notranslate"><span class="pre">Second</span></code>, <code class="docutils literal notranslate"><span class="pre">Third</span></code>, <code class="docutils literal notranslate"><span class="pre">Fourth</span></code>, <code class="docutils literal notranslate"><span class="pre">Last</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.backup.PolicyVM.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.PolicyVM.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.backup.PolicyVM.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.PolicyVM.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.backup.ProtectedFileShare">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.backup.</code><code class="sig-name descname">ProtectedFileShare</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backup_policy_id=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_file_share_name=None</em>, <em class="sig-param">source_storage_account_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.ProtectedFileShare" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Backup Protected File Share to enable backups for file shares within an Azure Storage Account</p>
<blockquote>
<div><p><strong>NOTE:</strong> Azure Backup for Azure File Shares is currently in public preview. During the preview, the service is subject to additional limitations and unsupported backup scenarios. <a class="reference external" href="https://docs.microsoft.com/en-us/azure/backup/backup-azure-files#limitations-for-azure-file-share-backup-during-preview">Read More</a></p>
<p><strong>NOTE</strong> Azure Backup for Azure File Shares does not support Soft Delete at this time. Deleting this resource will also delete all associated backup data. Please exercise caution. Consider using <cite>``protect`</cite> &lt;<a class="reference external" href="https://www.pulumi.com/docs/intro/concepts/programming-model/#protect">https://www.pulumi.com/docs/intro/concepts/programming-model/#protect</a>&gt;`_ to guard against accidental deletion.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backup_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the backup policy to use. The policy must be an Azure File Share backup policy. Other types are not supported.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Azure Backup Protected File Share. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_file_share_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the file share to backup. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the storage account of the file share to backup. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.backup.ProtectedFileShare.backup_policy_id">
<code class="sig-name descname">backup_policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.ProtectedFileShare.backup_policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the backup policy to use. The policy must be an Azure File Share backup policy. Other types are not supported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.ProtectedFileShare.recovery_vault_name">
<code class="sig-name descname">recovery_vault_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.ProtectedFileShare.recovery_vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.ProtectedFileShare.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.ProtectedFileShare.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Azure Backup Protected File Share. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.ProtectedFileShare.source_file_share_name">
<code class="sig-name descname">source_file_share_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.ProtectedFileShare.source_file_share_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the file share to backup. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.ProtectedFileShare.source_storage_account_id">
<code class="sig-name descname">source_storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.ProtectedFileShare.source_storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the storage account of the file share to backup. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.backup.ProtectedFileShare.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backup_policy_id=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_file_share_name=None</em>, <em class="sig-param">source_storage_account_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.ProtectedFileShare.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProtectedFileShare resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backup_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the backup policy to use. The policy must be an Azure File Share backup policy. Other types are not supported.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Azure Backup Protected File Share. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_file_share_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the file share to backup. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the storage account of the file share to backup. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.backup.ProtectedFileShare.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.ProtectedFileShare.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.backup.ProtectedFileShare.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.ProtectedFileShare.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.backup.ProtectedVM">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.backup.</code><code class="sig-name descname">ProtectedVM</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backup_policy_id=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_vm_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.ProtectedVM" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages Azure Backup for an Azure VM</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backup_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the id of the backup policy to use.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_vm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the VM to backup. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.backup.ProtectedVM.backup_policy_id">
<code class="sig-name descname">backup_policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.ProtectedVM.backup_policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the id of the backup policy to use.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.ProtectedVM.recovery_vault_name">
<code class="sig-name descname">recovery_vault_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.ProtectedVM.recovery_vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.ProtectedVM.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.ProtectedVM.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.ProtectedVM.source_vm_id">
<code class="sig-name descname">source_vm_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.ProtectedVM.source_vm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the VM to backup. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.backup.ProtectedVM.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.backup.ProtectedVM.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.backup.ProtectedVM.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backup_policy_id=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_vm_id=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.ProtectedVM.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProtectedVM resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backup_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the id of the backup policy to use.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_vm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the VM to backup. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.backup.ProtectedVM.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.ProtectedVM.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.backup.ProtectedVM.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.ProtectedVM.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.backup.get_policy_vm">
<code class="sig-prename descclassname">pulumi_azure.backup.</code><code class="sig-name descname">get_policy_vm</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.backup.get_policy_vm" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing VM Backup Policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the VM Backup Policy.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>str</em>) – Specifies the name of the Recovery Services Vault.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group in which the VM Backup Policy resides.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
