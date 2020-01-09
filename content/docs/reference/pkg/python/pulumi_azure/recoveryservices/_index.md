---
title: Module recoveryservices
title_tag: Module recoveryservices | Package pulumi_azure | Python SDK
linktitle: recoveryservices
notitle: true
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
<dt id="pulumi_azure.recoveryservices.Fabric">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.recoveryservices.</code><code class="sig-name descname">Fabric</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.Fabric" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>NOTE:</strong> This resource has been deprecated in favour of the <code class="docutils literal notranslate"><span class="pre">siterecovery.Fabric</span></code> resource and will be removed in the next major version of the AzureRM Provider. The new resource shares the same fields as this one, and information on migrating across can be found in this guide.</p>
</div></blockquote>
<p>Manages a Azure recovery vault fabric.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – In what region should the fabric be located.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the network mapping.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vault that should be updated.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the resource group where the vault that should be updated is located.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_fabric.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_fabric.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.Fabric.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.Fabric.location" title="Permalink to this definition">¶</a></dt>
<dd><p>In what region should the fabric be located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.Fabric.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.Fabric.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the network mapping.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.Fabric.recovery_vault_name">
<code class="sig-name descname">recovery_vault_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.Fabric.recovery_vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the vault that should be updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.Fabric.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.Fabric.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the resource group where the vault that should be updated is located.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.Fabric.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.Fabric.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Fabric resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – In what region should the fabric be located.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the network mapping.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vault that should be updated.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the resource group where the vault that should be updated is located.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_fabric.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_fabric.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.Fabric.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.Fabric.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.Fabric.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.Fabric.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.NetworkMapping">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.recoveryservices.</code><code class="sig-name descname">NetworkMapping</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_network_id=None</em>, <em class="sig-param">source_recovery_fabric_name=None</em>, <em class="sig-param">target_network_id=None</em>, <em class="sig-param">target_recovery_fabric_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.NetworkMapping" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>NOTE:</strong> This resource has been deprecated in favour of the <code class="docutils literal notranslate"><span class="pre">siterecovery.NetworkMapping</span></code> resource and will be removed in the next major version of the AzureRM Provider. The new resource shares the same fields as this one, and information on migrating across can be found in this guide.</p>
</div></blockquote>
<p>Manages a site recovery network mapping on Azure. A network mapping decides how to translate connected netwroks when a VM is migrated from one region to another.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the network mapping.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vault that should be updated.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the resource group where the vault that should be updated is located.</p></li>
<li><p><strong>source_network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the primary network.</p></li>
<li><p><strong>source_recovery_fabric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ASR fabric where mapping should be created.</p></li>
<li><p><strong>target_network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the recovery network.</p></li>
<li><p><strong>target_recovery_fabric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Site Recovery fabric object corresponding to the recovery Azure region.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_network_mapping.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_network_mapping.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.NetworkMapping.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.NetworkMapping.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the network mapping.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.NetworkMapping.recovery_vault_name">
<code class="sig-name descname">recovery_vault_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.NetworkMapping.recovery_vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the vault that should be updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.NetworkMapping.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.NetworkMapping.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the resource group where the vault that should be updated is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.NetworkMapping.source_network_id">
<code class="sig-name descname">source_network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.NetworkMapping.source_network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the primary network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.NetworkMapping.source_recovery_fabric_name">
<code class="sig-name descname">source_recovery_fabric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.NetworkMapping.source_recovery_fabric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ASR fabric where mapping should be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.NetworkMapping.target_network_id">
<code class="sig-name descname">target_network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.NetworkMapping.target_network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the recovery network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.NetworkMapping.target_recovery_fabric_name">
<code class="sig-name descname">target_recovery_fabric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.NetworkMapping.target_recovery_fabric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Site Recovery fabric object corresponding to the recovery Azure region.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.NetworkMapping.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_network_id=None</em>, <em class="sig-param">source_recovery_fabric_name=None</em>, <em class="sig-param">target_network_id=None</em>, <em class="sig-param">target_recovery_fabric_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.NetworkMapping.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkMapping resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the network mapping.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vault that should be updated.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the resource group where the vault that should be updated is located.</p></li>
<li><p><strong>source_network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the primary network.</p></li>
<li><p><strong>source_recovery_fabric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ASR fabric where mapping should be created.</p></li>
<li><p><strong>target_network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the recovery network.</p></li>
<li><p><strong>target_recovery_fabric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Site Recovery fabric object corresponding to the recovery Azure region.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_network_mapping.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_network_mapping.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.NetworkMapping.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.NetworkMapping.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.NetworkMapping.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.NetworkMapping.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.ProtectedVM">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.recoveryservices.</code><code class="sig-name descname">ProtectedVM</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">backup_policy_id=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_vm_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>NOTE:</strong> This resource has been deprecated in favour of the <code class="docutils literal notranslate"><span class="pre">backup.ProtectedVM</span></code> resource and will be removed in the next major version of the AzureRM Provider. The new resource shares the same fields as this one, and information on migrating across can be found in this guide.</p>
</div></blockquote>
<p>Manages an Recovery Protected VM.</p>
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
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protected_vm.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protected_vm.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectedVM.backup_policy_id">
<code class="sig-name descname">backup_policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectedVM.backup_policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the id of the backup policy to use.</p>
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
<dt id="pulumi_azure.recoveryservices.ProtectionContainer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.recoveryservices.</code><code class="sig-name descname">ProtectionContainer</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_fabric_name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainer" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>NOTE:</strong> This resource has been deprecated in favour of the <code class="docutils literal notranslate"><span class="pre">siterecovery.ProtectionContainer</span></code> resource and will be removed in the next major version of the AzureRM Provider. The new resource shares the same fields as this one, and information on migrating across can be found in this guide.</p>
</div></blockquote>
<p>Manages a Azure recovery vault protection container.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the network mapping.</p></li>
<li><p><strong>recovery_fabric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of fabric that should contain this protection container.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vault that should be updated.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the resource group where the vault that should be updated is located.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protection_container.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protection_container.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionContainer.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainer.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the network mapping.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionContainer.recovery_fabric_name">
<code class="sig-name descname">recovery_fabric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainer.recovery_fabric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of fabric that should contain this protection container.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionContainer.recovery_vault_name">
<code class="sig-name descname">recovery_vault_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainer.recovery_vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the vault that should be updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionContainer.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainer.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the resource group where the vault that should be updated is located.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.ProtectionContainer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_fabric_name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProtectionContainer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the network mapping.</p></li>
<li><p><strong>recovery_fabric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of fabric that should contain this protection container.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vault that should be updated.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the resource group where the vault that should be updated is located.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protection_container.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protection_container.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.ProtectionContainer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.ProtectionContainer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.ProtectionContainerMapping">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.recoveryservices.</code><code class="sig-name descname">ProtectionContainerMapping</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_fabric_name=None</em>, <em class="sig-param">recovery_replication_policy_id=None</em>, <em class="sig-param">recovery_source_protection_container_name=None</em>, <em class="sig-param">recovery_target_protection_container_id=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainerMapping" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>NOTE:</strong> This resource has been deprecated in favour of the <code class="docutils literal notranslate"><span class="pre">siterecovery.ProtectionContainerMapping</span></code> resource and will be removed in the next major version of the AzureRM Provider. The new resource shares the same fields as this one, and information on migrating across can be found in this guide.</p>
</div></blockquote>
<p>Manages a Azure recovery vault protection container mapping. A network protection container mapping decides how to translate the protection container when a VM is migrated from one region to another.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the network mapping.</p></li>
<li><p><strong>recovery_fabric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of fabric that should contains the protection container to map.</p></li>
<li><p><strong>recovery_replication_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of the policy to use for this mapping.</p></li>
<li><p><strong>recovery_source_protection_container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the protection container to map.</p></li>
<li><p><strong>recovery_target_protection_container_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of protection container to map to.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vault that should be updated.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the resource group where the vault that should be updated is located.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protection_container_mapping.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protection_container_mapping.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionContainerMapping.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainerMapping.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the network mapping.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionContainerMapping.recovery_fabric_name">
<code class="sig-name descname">recovery_fabric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainerMapping.recovery_fabric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of fabric that should contains the protection container to map.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionContainerMapping.recovery_replication_policy_id">
<code class="sig-name descname">recovery_replication_policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainerMapping.recovery_replication_policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Id of the policy to use for this mapping.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionContainerMapping.recovery_source_protection_container_name">
<code class="sig-name descname">recovery_source_protection_container_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainerMapping.recovery_source_protection_container_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the protection container to map.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionContainerMapping.recovery_target_protection_container_id">
<code class="sig-name descname">recovery_target_protection_container_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainerMapping.recovery_target_protection_container_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Id of protection container to map to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionContainerMapping.recovery_vault_name">
<code class="sig-name descname">recovery_vault_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainerMapping.recovery_vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the vault that should be updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionContainerMapping.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainerMapping.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the resource group where the vault that should be updated is located.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.ProtectionContainerMapping.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_fabric_name=None</em>, <em class="sig-param">recovery_replication_policy_id=None</em>, <em class="sig-param">recovery_source_protection_container_name=None</em>, <em class="sig-param">recovery_target_protection_container_id=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainerMapping.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProtectionContainerMapping resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the network mapping.</p></li>
<li><p><strong>recovery_fabric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of fabric that should contains the protection container to map.</p></li>
<li><p><strong>recovery_replication_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of the policy to use for this mapping.</p></li>
<li><p><strong>recovery_source_protection_container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the protection container to map.</p></li>
<li><p><strong>recovery_target_protection_container_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of protection container to map to.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vault that should be updated.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the resource group where the vault that should be updated is located.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protection_container_mapping.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protection_container_mapping.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.ProtectionContainerMapping.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainerMapping.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.ProtectionContainerMapping.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionContainerMapping.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dd><blockquote>
<div><p><strong>NOTE:</strong> This resource has been deprecated in favour of the <code class="docutils literal notranslate"><span class="pre">backup.PolicyVM</span></code> resource and will be removed in the next major version of the AzureRM Provider. The new resource shares the same fields as this one, and information on migrating across can be found in this guide.</p>
</div></blockquote>
<p>Manages an Recovery Services VM Protection Policy.</p>
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
<p>The <strong>backup</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">frequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>retention_daily</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>retention_monthly</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weeks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>retention_weekly</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>retention_yearly</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">months</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weeks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protection_policy_vm.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_protection_policy_vm.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.backup">
<code class="sig-name descname">backup</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.backup" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the Policy backup frequecent, times &amp; days as documented in the <code class="docutils literal notranslate"><span class="pre">backup</span></code> block below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">frequency</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
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
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_monthly">
<code class="sig-name descname">retention_monthly</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_monthly" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the policy monthly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_monthly</span></code> block below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weeks</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_weekly">
<code class="sig-name descname">retention_weekly</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_weekly" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the policy weekly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_weekly</span></code> block below. Required when backup frequency is <code class="docutils literal notranslate"><span class="pre">Weekly</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_yearly">
<code class="sig-name descname">retention_yearly</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ProtectionPolicyVM.retention_yearly" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the policy yearly retention as documented in the <code class="docutils literal notranslate"><span class="pre">retention_yearly</span></code> block below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">months</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weeks</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
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
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<p>The <strong>backup</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">frequency</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>retention_daily</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>retention_monthly</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weeks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>retention_weekly</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<p>The <strong>retention_yearly</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">months</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weekdays</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weeks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
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
<dt id="pulumi_azure.recoveryservices.ReplicatedVm">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.recoveryservices.</code><code class="sig-name descname">ReplicatedVm</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">managed_disks=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_replication_policy_id=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_recovery_fabric_name=None</em>, <em class="sig-param">source_recovery_protection_container_name=None</em>, <em class="sig-param">source_vm_id=None</em>, <em class="sig-param">target_availability_set_id=None</em>, <em class="sig-param">target_recovery_fabric_id=None</em>, <em class="sig-param">target_recovery_protection_container_id=None</em>, <em class="sig-param">target_resource_group_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicatedVm" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>NOTE:</strong> This resource has been deprecated in favour of the <code class="docutils literal notranslate"><span class="pre">siterecovery.ReplicatedVM</span></code> resource and will be removed in the next major version of the AzureRM Provider. The new resource shares the same fields as this one, and information on migrating across can be found in this guide.</p>
</div></blockquote>
<p>Manages a Azure recovery replicated vms (Azure to Azure). An replicated VM keeps a copiously updated image of the vm in another region in order to be able to start the VM in that region in case of a disaster.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>managed_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">managed_disk</span></code> block.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the network mapping.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vault that should be updated.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the resource group where the vault that should be updated is located.</p></li>
<li><p><strong>source_recovery_fabric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of fabric that should contains this replication.</p></li>
<li><p><strong>source_recovery_protection_container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the protection container to use.</p></li>
<li><p><strong>source_vm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of the VM to replicate</p></li>
<li><p><strong>target_availability_set_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of availability set that the new VM should belong to when a failover is done.</p></li>
<li><p><strong>target_recovery_fabric_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of fabric where the VM replication should be handled when a failover is done.</p></li>
<li><p><strong>target_recovery_protection_container_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of protection container where the VM replication should be created when a failover is done.</p></li>
<li><p><strong>target_resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of resource group where the VM should be created when a failover is done.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>managed_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">diskId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stagingStorageAccountId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetReplicaDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_resource_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Id of resource group where the VM should be created when a failover is done.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_replicated_vm.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_replicated_vm.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ReplicatedVm.managed_disks">
<code class="sig-name descname">managed_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicatedVm.managed_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">managed_disk</span></code> block.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">diskId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stagingStorageAccountId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetReplicaDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_resource_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Id of resource group where the VM should be created when a failover is done.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ReplicatedVm.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicatedVm.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the network mapping.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ReplicatedVm.recovery_vault_name">
<code class="sig-name descname">recovery_vault_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicatedVm.recovery_vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the vault that should be updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ReplicatedVm.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicatedVm.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the resource group where the vault that should be updated is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ReplicatedVm.source_recovery_fabric_name">
<code class="sig-name descname">source_recovery_fabric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicatedVm.source_recovery_fabric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of fabric that should contains this replication.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ReplicatedVm.source_recovery_protection_container_name">
<code class="sig-name descname">source_recovery_protection_container_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicatedVm.source_recovery_protection_container_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the protection container to use.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ReplicatedVm.source_vm_id">
<code class="sig-name descname">source_vm_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicatedVm.source_vm_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Id of the VM to replicate</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ReplicatedVm.target_availability_set_id">
<code class="sig-name descname">target_availability_set_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicatedVm.target_availability_set_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Id of availability set that the new VM should belong to when a failover is done.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ReplicatedVm.target_recovery_fabric_id">
<code class="sig-name descname">target_recovery_fabric_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicatedVm.target_recovery_fabric_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Id of fabric where the VM replication should be handled when a failover is done.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ReplicatedVm.target_recovery_protection_container_id">
<code class="sig-name descname">target_recovery_protection_container_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicatedVm.target_recovery_protection_container_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Id of protection container where the VM replication should be created when a failover is done.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ReplicatedVm.target_resource_group_id">
<code class="sig-name descname">target_resource_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicatedVm.target_resource_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Id of resource group where the VM should be created when a failover is done.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.ReplicatedVm.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">managed_disks=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_replication_policy_id=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_recovery_fabric_name=None</em>, <em class="sig-param">source_recovery_protection_container_name=None</em>, <em class="sig-param">source_vm_id=None</em>, <em class="sig-param">target_availability_set_id=None</em>, <em class="sig-param">target_recovery_fabric_id=None</em>, <em class="sig-param">target_recovery_protection_container_id=None</em>, <em class="sig-param">target_resource_group_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicatedVm.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ReplicatedVm resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>managed_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">managed_disk</span></code> block.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the network mapping.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vault that should be updated.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the resource group where the vault that should be updated is located.</p></li>
<li><p><strong>source_recovery_fabric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of fabric that should contains this replication.</p></li>
<li><p><strong>source_recovery_protection_container_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the protection container to use.</p></li>
<li><p><strong>source_vm_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of the VM to replicate</p></li>
<li><p><strong>target_availability_set_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of availability set that the new VM should belong to when a failover is done.</p></li>
<li><p><strong>target_recovery_fabric_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of fabric where the VM replication should be handled when a failover is done.</p></li>
<li><p><strong>target_recovery_protection_container_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of protection container where the VM replication should be created when a failover is done.</p></li>
<li><p><strong>target_resource_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of resource group where the VM should be created when a failover is done.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>managed_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">diskId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stagingStorageAccountId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetReplicaDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target_resource_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Id of resource group where the VM should be created when a failover is done.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_replicated_vm.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_replicated_vm.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.ReplicatedVm.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicatedVm.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.ReplicatedVm.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicatedVm.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.ReplicationPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.recoveryservices.</code><code class="sig-name descname">ReplicationPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_consistent_snapshot_frequency_in_minutes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_point_retention_in_minutes=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicationPolicy" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p><strong>NOTE:</strong> This resource has been deprecated in favour of the <code class="docutils literal notranslate"><span class="pre">siterecovery.ReplicationPolicy</span></code> resource and will be removed in the next major version of the AzureRM Provider. The new resource shares the same fields as this one, and information on migrating across can be found in this guide.</p>
</div></blockquote>
<p>Manages a Azure recovery vault replication policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_consistent_snapshot_frequency_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the frequency(in minutes) at which to create application consistent recovery points.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the network mapping.</p></li>
<li><p><strong>recovery_point_retention_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Retain the recovery points for given time in minutes.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vault that should be updated.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the resource group where the vault that should be updated is located.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_replication_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_replication_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ReplicationPolicy.application_consistent_snapshot_frequency_in_minutes">
<code class="sig-name descname">application_consistent_snapshot_frequency_in_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicationPolicy.application_consistent_snapshot_frequency_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the frequency(in minutes) at which to create application consistent recovery points.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ReplicationPolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicationPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the network mapping.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ReplicationPolicy.recovery_point_retention_in_minutes">
<code class="sig-name descname">recovery_point_retention_in_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicationPolicy.recovery_point_retention_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>Retain the recovery points for given time in minutes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ReplicationPolicy.recovery_vault_name">
<code class="sig-name descname">recovery_vault_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicationPolicy.recovery_vault_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the vault that should be updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.recoveryservices.ReplicationPolicy.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicationPolicy.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the resource group where the vault that should be updated is located.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.ReplicationPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_consistent_snapshot_frequency_in_minutes=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recovery_point_retention_in_minutes=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicationPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ReplicationPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_consistent_snapshot_frequency_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the frequency(in minutes) at which to create application consistent recovery points.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the network mapping.</p></li>
<li><p><strong>recovery_point_retention_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Retain the recovery points for given time in minutes.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the vault that should be updated.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the resource group where the vault that should be updated is located.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_replication_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/recovery_services_replication_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.recoveryservices.ReplicationPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicationPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.recoveryservices.ReplicationPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.ReplicationPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dd><p>Manages an Recovery Services Vault.</p>
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
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Recovery Services Vault.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group in which the Recovery Services Vault resides.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/recovery_services_vault.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/recovery_services_vault.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.recoveryservices.get_vm_protection_policy">
<code class="sig-prename descclassname">pulumi_azure.recoveryservices.</code><code class="sig-name descname">get_vm_protection_policy</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">recovery_vault_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.recoveryservices.get_vm_protection_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Recovery Services VM Protection Policy.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Recovery Services VM Protection Policy.</p></li>
<li><p><strong>recovery_vault_name</strong> (<em>str</em>) – Specifies the name of the Recovery Services Vault.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group in which the Recovery Services VM Protection Policy resides.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/recovery_services_protection_policy_vm.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/recovery_services_protection_policy_vm.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
