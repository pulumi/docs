<div class="section" id="module-pulumi_azure.recoveryservices">
<span id="recoveryservices"></span><h1>recoveryservices<a class="headerlink" href="#module-pulumi_azure.recoveryservices" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.recoveryservices.GetVaultResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.recoveryservices.</code><code class="descname">GetVaultResult</code><span class="sig-paren">(</span><em>location=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.GetVaultResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVault.</p>
<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.GetVaultResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.GetVaultResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the resource resides.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.GetVaultResult.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.GetVaultResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The vault’s current SKU.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.GetVaultResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.GetVaultResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.GetVaultResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.GetVaultResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.recoveryservices.ProtectedVM">
<em class="property">class </em><code class="descclassname">pulumi_azure.recoveryservices.</code><code class="descname">ProtectedVM</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>backup_policy_id=None</em>, <em>recovery_vault_name=None</em>, <em>resource_group_name=None</em>, <em>source_vm_id=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Recovery Protected VM.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>backup_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the id of the backup policy to use. Changing this forces a new resource to be created.</li>
<li><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.</li>
<li><strong>source_vm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the VM to backup. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectedVM.backup_policy_id">
<code class="descname">backup_policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM.backup_policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the id of the backup policy to use. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectedVM.recovery_vault_name">
<code class="descname">recovery_vault_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM.recovery_vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectedVM.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectedVM.source_vm_id">
<code class="descname">source_vm_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM.source_vm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the VM to backup. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectedVM.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.ProtectedVM.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.ProtectedVM.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM">
<em class="property">class </em><code class="descclassname">pulumi_azure.recoveryservices.</code><code class="descname">ProtectionPolicyVM</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>backup=None</em>, <em>name=None</em>, <em>recovery_vault_name=None</em>, <em>resource_group_name=None</em>, <em>retention_daily=None</em>, <em>retention_monthly=None</em>, <em>retention_weekly=None</em>, <em>retention_yearly=None</em>, <em>tags=None</em>, <em>timezone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Recovery Services VM Protection Policy.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>backup</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the Policy backup frequecent, times &amp; days as documented in the <code class="docutils literal notranslate"><span class="pre">backup</span></code> block below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recovery Services Vault Policy. Changing this forces a new resource to be created.</li>
<li><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.</li>
<li><strong>retention_daily</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the policy daily retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_daily</span></code> block below. Required when backup frequency is <code class="docutils literal notranslate"><span class="pre">Daily</span></code>.</li>
<li><strong>retention_monthly</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the policy monthly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_monthly</span></code> block below.</li>
<li><strong>retention_weekly</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the policy weekly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_weekly</span></code> block below. Required when backup frequency is <code class="docutils literal notranslate"><span class="pre">Weekly</span></code>.</li>
<li><strong>retention_yearly</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the policy yearly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_yearly</span></code> block below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the timezone. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code></li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.backup">
<code class="descname">backup</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.backup" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the Policy backup frequecent, times &amp; days as documented in the <code class="docutils literal notranslate"><span class="pre">backup</span></code> block below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Recovery Services Vault Policy. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.recovery_vault_name">
<code class="descname">recovery_vault_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.recovery_vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_daily">
<code class="descname">retention_daily</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_daily" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the policy daily retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_daily</span></code> block below. Required when backup frequency is <code class="docutils literal notranslate"><span class="pre">Daily</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_monthly">
<code class="descname">retention_monthly</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_monthly" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the policy monthly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_monthly</span></code> block below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_weekly">
<code class="descname">retention_weekly</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_weekly" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the policy weekly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_weekly</span></code> block below. Required when backup frequency is <code class="docutils literal notranslate"><span class="pre">Weekly</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_yearly">
<code class="descname">retention_yearly</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_yearly" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the policy yearly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_yearly</span></code> block below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.timezone">
<code class="descname">timezone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the timezone. Defaults to <code class="docutils literal notranslate"><span class="pre">UTC</span></code></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.Vault">
<em class="property">class </em><code class="descclassname">pulumi_azure.recoveryservices.</code><code class="descname">Vault</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.Vault" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage an Recovery Services Vault.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recovery Services Vault. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Recovery Services Vault. Changing this forces a new resource to be created.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the vault’s SKU. Possible values include: <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">RS0</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.Vault.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.Vault.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.Vault.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.Vault.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Recovery Services Vault. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.Vault.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.Vault.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Recovery Services Vault. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.Vault.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.Vault.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the vault’s SKU. Possible values include: <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">RS0</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.Vault.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.Vault.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.Vault.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.Vault.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.Vault.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.Vault.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.get_vault">
<code class="descclassname">pulumi_azure.recoveryservices.</code><code class="descname">get_vault</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.get_vault" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Recovery Services Vault.</p>
</dd></dl>

</div>
