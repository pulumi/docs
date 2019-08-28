---
title: Module recoveryservices
---

<div class="section" id="recoveryservices">
<h1>recoveryservices<a class="headerlink" href="#recoveryservices" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.recoveryservices"></span><dl class="class">
<dt id="pulumi_azure.recoveryservices.AwaitableGetVMProtectionPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.recoveryservices.</code><code class="sig-name descname">AwaitableGetVMProtectionPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.AwaitableGetVMProtectionPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.recoveryservices.AwaitableGetVaultResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.recoveryservices.</code><code class="sig-name descname">AwaitableGetVaultResult</code><span class="sig-paren">(</span><em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.AwaitableGetVaultResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.recoveryservices.GetVMProtectionPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.recoveryservices.</code><code class="sig-name descname">GetVMProtectionPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.GetVMProtectionPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVMProtectionPolicy.</p>
<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.GetVMProtectionPolicyResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.GetVMProtectionPolicyResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.GetVMProtectionPolicyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.GetVMProtectionPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.recoveryservices.GetVaultResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.recoveryservices.</code><code class="sig-name descname">GetVaultResult</code><span class="sig-paren">(</span><em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.GetVaultResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVault.</p>
<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.GetVaultResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.GetVaultResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the resource resides.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.GetVaultResult.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.GetVaultResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The vault’s current SKU.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.GetVaultResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.GetVaultResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.GetVaultResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.GetVaultResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.recoveryservices.ProtectedVM">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.recoveryservices.</code><code class="sig-name descname">ProtectedVM</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backup_policy_id=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_vm_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Recovery Protected VM.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backup_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the id of the backup policy to use. Changing this forces a new resource to be created.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_vm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the VM to backup. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protected_vm.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protected_vm.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectedVM.backup_policy_id">
<code class="sig-name descname">backup_policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM.backup_policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the id of the backup policy to use. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectedVM.recovery_vault_name">
<code class="sig-name descname">recovery_vault_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM.recovery_vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectedVM.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectedVM.source_vm_id">
<code class="sig-name descname">source_vm_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM.source_vm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the VM to backup. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectedVM.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.ProtectedVM.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backup_policy_id=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_vm_id=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProtectedVM resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] backup_policy_id: Specifies the id of the backup policy to use. Changing this forces a new resource to be created.
:param pulumi.Input[str] recovery_vault_name: Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.
:param pulumi.Input[str] source_vm_id: Specifies the ID of the VM to backup. Changing this forces a new resource to be created.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protected_vm.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protected_vm.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.ProtectedVM.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.ProtectedVM.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.recoveryservices.</code><code class="sig-name descname">ProtectionPolicyVM</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backup=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">retention_daily=None</em>, <em class="sig-param">retention_monthly=None</em>, <em class="sig-param">retention_weekly=None</em>, <em class="sig-param">retention_yearly=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">timezone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Recovery Services VM Protection Policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>backup</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the Policy backup frequecent, times &amp; days as documented in the <code class="docutils literal notranslate"><span class="pre">backup</span></code> block below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recovery Services Vault Policy. Changing this forces a new resource to be created.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.</p></li>
<li><p><strong>retention_daily</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the policy daily retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_daily</span></code> block below. Required when backup frequency is <code class="docutils literal notranslate"><span class="pre">Daily</span></code>.</p></li>
<li><p><strong>retention_monthly</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the policy monthly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_monthly</span></code> block below.</p></li>
<li><p><strong>retention_weekly</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the policy weekly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_weekly</span></code> block below. Required when backup frequency is <code class="docutils literal notranslate"><span class="pre">Weekly</span></code>.</p></li>
<li><p><strong>retention_yearly</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the policy yearly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_yearly</span></code> block below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the timezone. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code></p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protection_policy_vm.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protection_policy_vm.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.backup">
<code class="sig-name descname">backup</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.backup" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the Policy backup frequecent, times &amp; days as documented in the <code class="docutils literal notranslate"><span class="pre">backup</span></code> block below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Recovery Services Vault Policy. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.recovery_vault_name">
<code class="sig-name descname">recovery_vault_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.recovery_vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_daily">
<code class="sig-name descname">retention_daily</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_daily" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the policy daily retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_daily</span></code> block below. Required when backup frequency is <code class="docutils literal notranslate"><span class="pre">Daily</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_monthly">
<code class="sig-name descname">retention_monthly</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_monthly" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the policy monthly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_monthly</span></code> block below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_weekly">
<code class="sig-name descname">retention_weekly</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_weekly" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the policy weekly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_weekly</span></code> block below. Required when backup frequency is <code class="docutils literal notranslate"><span class="pre">Weekly</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_yearly">
<code class="sig-name descname">retention_yearly</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_yearly" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the policy yearly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_yearly</span></code> block below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.timezone">
<code class="sig-name descname">timezone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the timezone. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backup=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">retention_daily=None</em>, <em class="sig-param">retention_monthly=None</em>, <em class="sig-param">retention_weekly=None</em>, <em class="sig-param">retention_yearly=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">timezone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProtectionPolicyVM resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] backup: Configures the Policy backup frequecent, times &amp; days as documented in the <code class="docutils literal notranslate"><span class="pre">backup</span></code> block below. 
:param pulumi.Input[str] name: Specifies the name of the Recovery Services Vault Policy. Changing this forces a new resource to be created.
:param pulumi.Input[str] recovery_vault_name: Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.
:param pulumi.Input[dict] retention_daily: Configures the policy daily retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_daily</span></code> block below. Required when backup frequency is <code class="docutils literal notranslate"><span class="pre">Daily</span></code>.
:param pulumi.Input[dict] retention_monthly: Configures the policy monthly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_monthly</span></code> block below.
:param pulumi.Input[dict] retention_weekly: Configures the policy weekly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_weekly</span></code> block below. Required when backup frequency is <code class="docutils literal notranslate"><span class="pre">Weekly</span></code>.
:param pulumi.Input[dict] retention_yearly: Configures the policy yearly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_yearly</span></code> block below.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
:param pulumi.Input[str] timezone: Specifies the timezone. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code></p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protection_policy_vm.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protection_policy_vm.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.Vault">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.recoveryservices.</code><code class="sig-name descname">Vault</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.Vault" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage an Recovery Services Vault.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recovery Services Vault. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Recovery Services Vault. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the vault’s SKU. Possible values include: <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">RS0</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_vault.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_vault.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.Vault.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.Vault.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.Vault.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.Vault.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Recovery Services Vault. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.Vault.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.Vault.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Recovery Services Vault. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.Vault.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.Vault.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the vault’s SKU. Possible values include: <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">RS0</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.Vault.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.Vault.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.Vault.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.Vault.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Vault resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] name: Specifies the name of the Recovery Services Vault. Changing this forces a new resource to be created.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Recovery Services Vault. Changing this forces a new resource to be created.
:param pulumi.Input[str] sku: Sets the vault’s SKU. Possible values include: <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">RS0</span></code>.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_vault.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_vault.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.Vault.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.Vault.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.Vault.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.Vault.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.get_vault">
<code class="sig-prename descclassname">pulumi_azure.recoveryservices.</code><code class="sig-name descname">get_vault</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.get_vault" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Recovery Services Vault.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/recovery_services_vault.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/recovery_services_vault.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.recoveryservices.get_vm_protection_policy">
<code class="sig-prename descclassname">pulumi_azure.recoveryservices.</code><code class="sig-name descname">get_vm_protection_policy</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.get_vm_protection_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Recovery Services VM Protection Policy.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/recovery_services_protection_policy_vm.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/recovery_services_protection_policy_vm.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
