---
title: Module batch
title_tag: Module batch | Package pulumi_azure | Python SDK
linktitle: batch
notitle: true
---

<div class="section" id="batch">
<h1>batch<a class="headerlink" href="#batch" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.batch"></span><dl class="class">
<dt id="pulumi_azure.batch.Account">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.batch.</code><code class="sig-name descname">Account</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">key_vault_reference=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pool_allocation_mode=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Batch account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key_vault_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">key_vault_reference</span></code> block that describes the Azure KeyVault reference to use when deploying the Azure Batch account using the <code class="docutils literal notranslate"><span class="pre">UserSubscription</span></code> pool allocation mode.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Batch account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>pool_allocation_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the mode to use for pool allocation. Possible values are <code class="docutils literal notranslate"><span class="pre">BatchService</span></code> or <code class="docutils literal notranslate"><span class="pre">UserSubscription</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">BatchService</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Batch account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the storage account to use for the Batch account. If not specified, Azure Batch will manage the storage.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>key_vault_reference</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure identifier of the Azure KeyVault to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTPS URL of the Azure KeyVault to use.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.batch.Account.account_endpoint">
<code class="sig-name descname">account_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.account_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The account endpoint used to interact with the Batch service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Account.key_vault_reference">
<code class="sig-name descname">key_vault_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.key_vault_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">key_vault_reference</span></code> block that describes the Azure KeyVault reference to use when deploying the Azure Batch account using the <code class="docutils literal notranslate"><span class="pre">UserSubscription</span></code> pool allocation mode.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Azure identifier of the Azure KeyVault to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The HTTPS URL of the Azure KeyVault to use.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Account.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Account.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Batch account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Account.pool_allocation_mode">
<code class="sig-name descname">pool_allocation_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.pool_allocation_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the mode to use for pool allocation. Possible values are <code class="docutils literal notranslate"><span class="pre">BatchService</span></code> or <code class="docutils literal notranslate"><span class="pre">UserSubscription</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">BatchService</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Account.primary_access_key">
<code class="sig-name descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Batch account primary access key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Account.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Batch account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Account.secondary_access_key">
<code class="sig-name descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Batch account secondary access key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Account.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the storage account to use for the Batch account. If not specified, Azure Batch will manage the storage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Account.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.batch.Account.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_endpoint=None</em>, <em class="sig-param">key_vault_reference=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pool_allocation_mode=None</em>, <em class="sig-param">primary_access_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_access_key=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Account.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Account resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account endpoint used to interact with the Batch service.</p></li>
<li><p><strong>key_vault_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">key_vault_reference</span></code> block that describes the Azure KeyVault reference to use when deploying the Azure Batch account using the <code class="docutils literal notranslate"><span class="pre">UserSubscription</span></code> pool allocation mode.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Batch account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>pool_allocation_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the mode to use for pool allocation. Possible values are <code class="docutils literal notranslate"><span class="pre">BatchService</span></code> or <code class="docutils literal notranslate"><span class="pre">UserSubscription</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">BatchService</span></code>.</p></li>
<li><p><strong>primary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Batch account primary access key.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Batch account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secondary_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Batch account secondary access key.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the storage account to use for the Batch account. If not specified, Azure Batch will manage the storage.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>key_vault_reference</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure identifier of the Azure KeyVault to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The HTTPS URL of the Azure KeyVault to use.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.batch.Account.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.batch.Account.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.batch.Application">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.batch.</code><code class="sig-name descname">Application</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">allow_updates=None</em>, <em class="sig-param">default_version=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Application" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages Azure Batch Application instance.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Batch account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>allow_updates</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A value indicating whether packages within the application may be overwritten using the same version string. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>default_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The package to use if a client requests the application but does not specify a version. This property can only be set to the name of an existing package.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the application.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the application. This must be unique within the account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group that contains the Batch account. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.batch.Application.account_name">
<code class="sig-name descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Application.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Batch account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Application.allow_updates">
<code class="sig-name descname">allow_updates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Application.allow_updates" title="Permalink to this definition">¶</a></dt>
<dd><p>A value indicating whether packages within the application may be overwritten using the same version string. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Application.default_version">
<code class="sig-name descname">default_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Application.default_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The package to use if a client requests the application but does not specify a version. This property can only be set to the name of an existing package.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Application.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Application.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name for the application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Application.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Application.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the application. This must be unique within the account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Application.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Application.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group that contains the Batch account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.batch.Application.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">allow_updates=None</em>, <em class="sig-param">default_version=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Application.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Application resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Batch account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>allow_updates</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A value indicating whether packages within the application may be overwritten using the same version string. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>default_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The package to use if a client requests the application but does not specify a version. This property can only be set to the name of an existing package.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the application.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the application. This must be unique within the account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group that contains the Batch account. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.batch.Application.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Application.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.batch.Application.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Application.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.batch.AwaitableGetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.batch.</code><code class="sig-name descname">AwaitableGetAccountResult</code><span class="sig-paren">(</span><em class="sig-param">account_endpoint=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">key_vault_references=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pool_allocation_mode=None</em>, <em class="sig-param">primary_access_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_access_key=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.AwaitableGetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.batch.AwaitableGetCertificateResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.batch.</code><code class="sig-name descname">AwaitableGetCertificateResult</code><span class="sig-paren">(</span><em class="sig-param">account_name=None</em>, <em class="sig-param">format=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">public_data=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">thumbprint=None</em>, <em class="sig-param">thumbprint_algorithm=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.AwaitableGetCertificateResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.batch.AwaitableGetPoolResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.batch.</code><code class="sig-name descname">AwaitableGetPoolResult</code><span class="sig-paren">(</span><em class="sig-param">account_name=None</em>, <em class="sig-param">auto_scales=None</em>, <em class="sig-param">certificates=None</em>, <em class="sig-param">container_configurations=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">fixed_scales=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">max_tasks_per_node=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_configuration=None</em>, <em class="sig-param">node_agent_sku_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">start_task=None</em>, <em class="sig-param">storage_image_references=None</em>, <em class="sig-param">vm_size=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.AwaitableGetPoolResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.batch.Certificate">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.batch.</code><code class="sig-name descname">Certificate</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">format=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">thumbprint=None</em>, <em class="sig-param">thumbprint_algorithm=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a certificate in an Azure Batch account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Batch account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64-encoded contents of the certificate.</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of the certificate. Possible values are <code class="docutils literal notranslate"><span class="pre">Cer</span></code> or <code class="docutils literal notranslate"><span class="pre">Pfx</span></code>.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password to access the certificate’s private key. This must and can only be specified when <code class="docutils literal notranslate"><span class="pre">format</span></code> is <code class="docutils literal notranslate"><span class="pre">Pfx</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Batch account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>thumbprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The thumbprint of the certificate. At this time the only supported value is ‘SHA1’.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.batch.Certificate.account_name">
<code class="sig-name descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Certificate.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Batch account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Certificate.certificate">
<code class="sig-name descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Certificate.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The base64-encoded contents of the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Certificate.format">
<code class="sig-name descname">format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Certificate.format" title="Permalink to this definition">¶</a></dt>
<dd><p>The format of the certificate. Possible values are <code class="docutils literal notranslate"><span class="pre">Cer</span></code> or <code class="docutils literal notranslate"><span class="pre">Pfx</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Certificate.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Certificate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The generated name of the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Certificate.password">
<code class="sig-name descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Certificate.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password to access the certificate’s private key. This must and can only be specified when <code class="docutils literal notranslate"><span class="pre">format</span></code> is <code class="docutils literal notranslate"><span class="pre">Pfx</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Certificate.public_data">
<code class="sig-name descname">public_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Certificate.public_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key of the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Certificate.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Certificate.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Batch account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Certificate.thumbprint">
<code class="sig-name descname">thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Certificate.thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The thumbprint of the certificate. At this time the only supported value is ‘SHA1’.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.batch.Certificate.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">certificate=None</em>, <em class="sig-param">format=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">public_data=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">thumbprint=None</em>, <em class="sig-param">thumbprint_algorithm=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Certificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Certificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Batch account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64-encoded contents of the certificate.</p></li>
<li><p><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of the certificate. Possible values are <code class="docutils literal notranslate"><span class="pre">Cer</span></code> or <code class="docutils literal notranslate"><span class="pre">Pfx</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The generated name of the certificate.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password to access the certificate’s private key. This must and can only be specified when <code class="docutils literal notranslate"><span class="pre">format</span></code> is <code class="docutils literal notranslate"><span class="pre">Pfx</span></code>.</p></li>
<li><p><strong>public_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key of the certificate.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Batch account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>thumbprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The thumbprint of the certificate. At this time the only supported value is ‘SHA1’.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.batch.Certificate.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Certificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.batch.Certificate.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Certificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.batch.GetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.batch.</code><code class="sig-name descname">GetAccountResult</code><span class="sig-paren">(</span><em class="sig-param">account_endpoint=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">key_vault_references=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pool_allocation_mode=None</em>, <em class="sig-param">primary_access_key=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secondary_access_key=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.account_endpoint">
<code class="sig-name descname">account_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.account_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The account endpoint used to interact with the Batch service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.key_vault_references">
<code class="sig-name descname">key_vault_references</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.key_vault_references" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">key_vault_reference</span></code> block that describes the Azure KeyVault reference to use when deploying the Azure Batch account using the <code class="docutils literal notranslate"><span class="pre">UserSubscription</span></code> pool allocation mode.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which this Batch account exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Batch account name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.pool_allocation_mode">
<code class="sig-name descname">pool_allocation_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.pool_allocation_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The pool allocation mode configured for this Batch account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.primary_access_key">
<code class="sig-name descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Batch account primary access key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.secondary_access_key">
<code class="sig-name descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Batch account secondary access key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Storage Account used for this Batch account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags assigned to the Batch account.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.batch.GetCertificateResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.batch.</code><code class="sig-name descname">GetCertificateResult</code><span class="sig-paren">(</span><em class="sig-param">account_name=None</em>, <em class="sig-param">format=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">public_data=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">thumbprint=None</em>, <em class="sig-param">thumbprint_algorithm=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.GetCertificateResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCertificate.</p>
<dl class="attribute">
<dt id="pulumi_azure.batch.GetCertificateResult.format">
<code class="sig-name descname">format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetCertificateResult.format" title="Permalink to this definition">¶</a></dt>
<dd><p>The format of the certificate, such as <code class="docutils literal notranslate"><span class="pre">Cer</span></code> or <code class="docutils literal notranslate"><span class="pre">Pfx</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetCertificateResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetCertificateResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetCertificateResult.public_data">
<code class="sig-name descname">public_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetCertificateResult.public_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key of the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetCertificateResult.thumbprint">
<code class="sig-name descname">thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetCertificateResult.thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The thumbprint of the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetCertificateResult.thumbprint_algorithm">
<code class="sig-name descname">thumbprint_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetCertificateResult.thumbprint_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The algorithm of the certificate thumbprint.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.batch.GetPoolResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.batch.</code><code class="sig-name descname">GetPoolResult</code><span class="sig-paren">(</span><em class="sig-param">account_name=None</em>, <em class="sig-param">auto_scales=None</em>, <em class="sig-param">certificates=None</em>, <em class="sig-param">container_configurations=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">fixed_scales=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">max_tasks_per_node=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_configuration=None</em>, <em class="sig-param">node_agent_sku_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">start_task=None</em>, <em class="sig-param">storage_image_references=None</em>, <em class="sig-param">vm_size=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPool.</p>
<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.account_name">
<code class="sig-name descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Batch account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.auto_scales">
<code class="sig-name descname">auto_scales</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.auto_scales" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">auto_scale</span></code> block that describes the scale settings when using auto scale.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.certificates">
<code class="sig-name descname">certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks that describe the certificates installed on each compute node in the pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.container_configurations">
<code class="sig-name descname">container_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.container_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>The container configuration used in the pool’s VMs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.fixed_scales">
<code class="sig-name descname">fixed_scales</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.fixed_scales" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">fixed_scale</span></code> block that describes the scale settings when using fixed scale.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.max_tasks_per_node">
<code class="sig-name descname">max_tasks_per_node</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.max_tasks_per_node" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of tasks that can run concurrently on a single compute node in the pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the endpoint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.node_agent_sku_id">
<code class="sig-name descname">node_agent_sku_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.node_agent_sku_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Sku of the node agents in the Batch pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.start_task">
<code class="sig-name descname">start_task</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.start_task" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">start_task</span></code> block that describes the start task settings for the Batch pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.storage_image_references">
<code class="sig-name descname">storage_image_references</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.storage_image_references" title="Permalink to this definition">¶</a></dt>
<dd><p>The reference of the storage image used by the nodes in the Batch pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.vm_size">
<code class="sig-name descname">vm_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.vm_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the VM created in the Batch pool.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.batch.Pool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.batch.</code><code class="sig-name descname">Pool</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">auto_scale=None</em>, <em class="sig-param">certificates=None</em>, <em class="sig-param">container_configuration=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">fixed_scale=None</em>, <em class="sig-param">max_tasks_per_node=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_configuration=None</em>, <em class="sig-param">node_agent_sku_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">start_task=None</em>, <em class="sig-param">stop_pending_resize_operation=None</em>, <em class="sig-param">storage_image_reference=None</em>, <em class="sig-param">vm_size=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Pool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Batch pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Batch account in which the pool will be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>auto_scale</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">auto_scale</span></code> block that describes the scale settings when using auto scale.</p></li>
<li><p><strong>certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks that describe the certificates to be installed on each compute node in the pool.</p></li>
<li><p><strong>container_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The container configuration used in the pool’s VMs.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the display name of the Batch pool.</p></li>
<li><p><strong>fixed_scale</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">fixed_scale</span></code> block that describes the scale settings when using fixed scale.</p></li>
<li><p><strong>max_tasks_per_node</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum number of tasks that can run concurrently on a single compute node in the pool. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of custom batch pool metadata.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Batch pool. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">network_configuration</span></code> block that describes the network configurations for the Batch pool.</p></li>
<li><p><strong>node_agent_sku_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Sku of the node agents that will be created in the Batch pool.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Batch pool. Changing this forces a new resource to be created.</p></li>
<li><p><strong>start_task</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">start_task</span></code> block that describes the start task settings for the Batch pool.</p></li>
<li><p><strong>storage_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_image_reference</span></code> for the virtual machines that will compose the Batch pool.</p></li>
<li><p><strong>vm_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the size of the VM created in the Batch pool.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auto_scale</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The interval to wait before evaluating if the pool needs to be scaled. Defaults to <code class="docutils literal notranslate"><span class="pre">PT15M</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formula</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The autoscale formula that needs to be used for scaling the Batch pool.</p></li>
</ul>
<p>The <strong>certificates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Batch Certificate to install on the Batch Pool, which must be inside the same Batch Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storeLocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location of the certificate store on the compute node into which to install the certificate. Possible values are <code class="docutils literal notranslate"><span class="pre">CurrentUser</span></code> or <code class="docutils literal notranslate"><span class="pre">LocalMachine</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the certificate store on the compute node into which to install the certificate. This property is applicable only for pools configured with Windows nodes (that is, created with cloudServiceConfiguration, or with virtualMachineConfiguration using a Windows image reference). Common store names include: <code class="docutils literal notranslate"><span class="pre">My</span></code>, <code class="docutils literal notranslate"><span class="pre">Root</span></code>, <code class="docutils literal notranslate"><span class="pre">CA</span></code>, <code class="docutils literal notranslate"><span class="pre">Trust</span></code>, <code class="docutils literal notranslate"><span class="pre">Disallowed</span></code>, <code class="docutils literal notranslate"><span class="pre">TrustedPeople</span></code>, <code class="docutils literal notranslate"><span class="pre">TrustedPublisher</span></code>, <code class="docutils literal notranslate"><span class="pre">AuthRoot</span></code>, <code class="docutils literal notranslate"><span class="pre">AddressBook</span></code>, but any custom store name can also be used. The default value is <code class="docutils literal notranslate"><span class="pre">My</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">visibilities</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Which user accounts on the compute node should have access to the private data of the certificate.</p></li>
</ul>
<p>The <strong>container_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerRegistries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Additional container registries from which container images can be pulled by the pool’s VMs.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password to log into the registry server. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">registryServer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The container registry URL. The default is “docker.io”. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user name to log into the registry server. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of container configuration. Possible value is <code class="docutils literal notranslate"><span class="pre">DockerCompatible</span></code>.</p></li>
</ul>
<p>The <strong>fixed_scale</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resizeTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The timeout for resize operations. Defaults to <code class="docutils literal notranslate"><span class="pre">PT15M</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetDedicatedNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of nodes in the Batch pool. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetLowPriorityNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of low priority nodes in the Batch pool. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
</ul>
<p>The <strong>network_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">endpointConfigurations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of inbound NAT pools that can be used to address specific ports on an individual compute node externally. Set as documented in the inbound_nat_pools block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">backend_port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port number on the compute node. Acceptable values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code> except for <code class="docutils literal notranslate"><span class="pre">29876</span></code>, <code class="docutils literal notranslate"><span class="pre">29877</span></code> as these are reserved. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontendPortRange</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The range of external ports that will be used to provide inbound access to the backendPort on individual compute nodes in the format of <code class="docutils literal notranslate"><span class="pre">1000-1100</span></code>. Acceptable values range between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">65534</span></code> except ports from <code class="docutils literal notranslate"><span class="pre">50000</span></code> to <code class="docutils literal notranslate"><span class="pre">55000</span></code> which are reserved by the Batch service. All ranges within a pool must be distinct and cannot overlap. Values must be a range of at least <code class="docutils literal notranslate"><span class="pre">100</span></code> nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the endpoint. The name must be unique within a Batch pool, can contain letters, numbers, underscores, periods, and hyphens. Names must start with a letter or number, must end with a letter, number, or underscore, and cannot exceed 77 characters. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkSecurityGroupRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of network security group rules that will be applied to the endpoint. The maximum number of rules that can be specified across all the endpoints on a Batch pool is <code class="docutils literal notranslate"><span class="pre">25</span></code>. If no network security group rules are specified, a default rule will be created to allow inbound access to the specified backendPort. Set as documented in the network_security_group_rules block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">access</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action that should be taken for a specified IP address, subnet range or tag. Acceptable values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The priority for this rule. The value must be at least <code class="docutils literal notranslate"><span class="pre">150</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_address_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The source address prefix or tag to match for the rule. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol of the endpoint. Acceptable values are <code class="docutils literal notranslate"><span class="pre">TCP</span></code> and <code class="docutils literal notranslate"><span class="pre">UDP</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of public ip ids that will be allocated to nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARM resource identifier of the virtual network subnet which the compute nodes of the pool will join. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>start_task</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commandLine</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The command line executed by the start task.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of strings (key,value) that represents the environment variables to set in the start task.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTaskRetryCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of retry count. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceFiles</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">resource_file</span></code> blocks that describe the files to be downloaded to a compute node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoStorageContainerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The storage container name in the auto storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">blobPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The blob prefix to use when downloading blobs from an Azure Storage container. Only the blobs whose names begin with the specified prefix will be downloaded. The property is valid only when <code class="docutils literal notranslate"><span class="pre">auto_storage_container_name</span></code> or <code class="docutils literal notranslate"><span class="pre">storage_container_url</span></code> is used. This prefix can be a partial filename or a subdirectory. If a prefix is not specified, all the files in the container will be downloaded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The file permission mode represented as a string in octal format (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;0644&quot;</span></code>). This property applies only to files being downloaded to Linux compute nodes. It will be ignored if it is specified for a <code class="docutils literal notranslate"><span class="pre">resource_file</span></code> which will be downloaded to a Windows node. If this property is not specified for a Linux node, then a default value of 0770 is applied to the file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filePath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location on the compute node to which to download the file, relative to the task’s working directory. If the <code class="docutils literal notranslate"><span class="pre">http_url</span></code> property is specified, the <code class="docutils literal notranslate"><span class="pre">file_path</span></code> is required and describes the path which the file will be downloaded to, including the filename. Otherwise, if the <code class="docutils literal notranslate"><span class="pre">auto_storage_container_name</span></code> or <code class="docutils literal notranslate"><span class="pre">storage_container_url</span></code> property is specified, <code class="docutils literal notranslate"><span class="pre">file_path</span></code> is optional and is the directory to download the files to. In the case where <code class="docutils literal notranslate"><span class="pre">file_path</span></code> is used as a directory, any directory structure already associated with the input data will be retained in full and appended to the specified filePath directory. The specified relative path cannot break out of the task’s working directory (for example by using ‘..’).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL of the file to download. If the URL is Azure Blob Storage, it must be readable using anonymous access; that is, the Batch service does not present any credentials when downloading the blob. There are two ways to get such a URL for a blob in Azure storage: include a Shared Access Signature (SAS) granting read permissions on the blob, or set the ACL for the blob or its container to allow public access.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageContainerUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL of the blob container within Azure Blob Storage. This URL must be readable and listable using anonymous access; that is, the Batch service does not present any credentials when downloading the blob. There are two ways to get such a URL for a blob in Azure storage: include a Shared Access Signature (SAS) granting read and list permissions on the blob, or set the ACL for the blob or its container to allow public access.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">userIdentity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">user_identity</span></code> block that describes the user identity under which the start task runs.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoUser</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">auto_user</span></code> block that describes the user identity under which the start task runs.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">elevationLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The elevation level of the user identity under which the start task runs. Possible values are <code class="docutils literal notranslate"><span class="pre">Admin</span></code> or <code class="docutils literal notranslate"><span class="pre">NonAdmin</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">NonAdmin</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The scope of the user identity under which the start task runs. Possible values are <code class="docutils literal notranslate"><span class="pre">Task</span></code> or <code class="docutils literal notranslate"><span class="pre">Pool</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Task</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">userName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username to be used by the Batch pool start task.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitForSuccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - A flag that indicates if the Batch pool should wait for the start task to be completed. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>storage_image_reference</strong> object supports the following:</p>
<blockquote>
<div><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the ID of the Custom Image which the virtual machines should be created from. Changing this forces a new resource to be created. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/batch/batch-custom-images">official documentation</a> for more details.</p></li>
</ul>
</div></blockquote>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the offer of the image used to create the virtual machines. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the publisher of the image used to create the virtual machines. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the SKU of the image used to create the virtual machines. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the version of the image used to create the virtual machines. Changing this forces a new resource to be created.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.account_name">
<code class="sig-name descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Batch account in which the pool will be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.auto_scale">
<code class="sig-name descname">auto_scale</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.auto_scale" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">auto_scale</span></code> block that describes the scale settings when using auto scale.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The interval to wait before evaluating if the pool needs to be scaled. Defaults to <code class="docutils literal notranslate"><span class="pre">PT15M</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formula</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The autoscale formula that needs to be used for scaling the Batch pool.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.certificates">
<code class="sig-name descname">certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks that describe the certificates to be installed on each compute node in the pool.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Batch Certificate to install on the Batch Pool, which must be inside the same Batch Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storeLocation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The location of the certificate store on the compute node into which to install the certificate. Possible values are <code class="docutils literal notranslate"><span class="pre">CurrentUser</span></code> or <code class="docutils literal notranslate"><span class="pre">LocalMachine</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the certificate store on the compute node into which to install the certificate. This property is applicable only for pools configured with Windows nodes (that is, created with cloudServiceConfiguration, or with virtualMachineConfiguration using a Windows image reference). Common store names include: <code class="docutils literal notranslate"><span class="pre">My</span></code>, <code class="docutils literal notranslate"><span class="pre">Root</span></code>, <code class="docutils literal notranslate"><span class="pre">CA</span></code>, <code class="docutils literal notranslate"><span class="pre">Trust</span></code>, <code class="docutils literal notranslate"><span class="pre">Disallowed</span></code>, <code class="docutils literal notranslate"><span class="pre">TrustedPeople</span></code>, <code class="docutils literal notranslate"><span class="pre">TrustedPublisher</span></code>, <code class="docutils literal notranslate"><span class="pre">AuthRoot</span></code>, <code class="docutils literal notranslate"><span class="pre">AddressBook</span></code>, but any custom store name can also be used. The default value is <code class="docutils literal notranslate"><span class="pre">My</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">visibilities</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Which user accounts on the compute node should have access to the private data of the certificate.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.container_configuration">
<code class="sig-name descname">container_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.container_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The container configuration used in the pool’s VMs.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerRegistries</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Additional container registries from which container images can be pulled by the pool’s VMs.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password to log into the registry server. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">registryServer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The container registry URL. The default is “docker.io”. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The user name to log into the registry server. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of container configuration. Possible value is <code class="docutils literal notranslate"><span class="pre">DockerCompatible</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the display name of the Batch pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.fixed_scale">
<code class="sig-name descname">fixed_scale</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.fixed_scale" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">fixed_scale</span></code> block that describes the scale settings when using fixed scale.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resizeTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The timeout for resize operations. Defaults to <code class="docutils literal notranslate"><span class="pre">PT15M</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetDedicatedNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of nodes in the Batch pool. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetLowPriorityNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of low priority nodes in the Batch pool. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.max_tasks_per_node">
<code class="sig-name descname">max_tasks_per_node</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.max_tasks_per_node" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum number of tasks that can run concurrently on a single compute node in the pool. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.metadata">
<code class="sig-name descname">metadata</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of custom batch pool metadata.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Batch pool. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.network_configuration">
<code class="sig-name descname">network_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.network_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">network_configuration</span></code> block that describes the network configurations for the Batch pool.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">endpointConfigurations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of inbound NAT pools that can be used to address specific ports on an individual compute node externally. Set as documented in the inbound_nat_pools block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">backend_port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port number on the compute node. Acceptable values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code> except for <code class="docutils literal notranslate"><span class="pre">29876</span></code>, <code class="docutils literal notranslate"><span class="pre">29877</span></code> as these are reserved. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontendPortRange</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The range of external ports that will be used to provide inbound access to the backendPort on individual compute nodes in the format of <code class="docutils literal notranslate"><span class="pre">1000-1100</span></code>. Acceptable values range between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">65534</span></code> except ports from <code class="docutils literal notranslate"><span class="pre">50000</span></code> to <code class="docutils literal notranslate"><span class="pre">55000</span></code> which are reserved by the Batch service. All ranges within a pool must be distinct and cannot overlap. Values must be a range of at least <code class="docutils literal notranslate"><span class="pre">100</span></code> nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the endpoint. The name must be unique within a Batch pool, can contain letters, numbers, underscores, periods, and hyphens. Names must start with a letter or number, must end with a letter, number, or underscore, and cannot exceed 77 characters. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkSecurityGroupRules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of network security group rules that will be applied to the endpoint. The maximum number of rules that can be specified across all the endpoints on a Batch pool is <code class="docutils literal notranslate"><span class="pre">25</span></code>. If no network security group rules are specified, a default rule will be created to allow inbound access to the specified backendPort. Set as documented in the network_security_group_rules block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">access</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The action that should be taken for a specified IP address, subnet range or tag. Acceptable values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The priority for this rule. The value must be at least <code class="docutils literal notranslate"><span class="pre">150</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_address_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The source address prefix or tag to match for the rule. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The protocol of the endpoint. Acceptable values are <code class="docutils literal notranslate"><span class="pre">TCP</span></code> and <code class="docutils literal notranslate"><span class="pre">UDP</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIps</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of public ip ids that will be allocated to nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARM resource identifier of the virtual network subnet which the compute nodes of the pool will join. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.node_agent_sku_id">
<code class="sig-name descname">node_agent_sku_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.node_agent_sku_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Sku of the node agents that will be created in the Batch pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Batch pool. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.start_task">
<code class="sig-name descname">start_task</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.start_task" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">start_task</span></code> block that describes the start task settings for the Batch pool.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commandLine</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The command line executed by the start task.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environment</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A map of strings (key,value) that represents the environment variables to set in the start task.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTaskRetryCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of retry count. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceFiles</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">resource_file</span></code> blocks that describe the files to be downloaded to a compute node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoStorageContainerName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The storage container name in the auto storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">blobPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The blob prefix to use when downloading blobs from an Azure Storage container. Only the blobs whose names begin with the specified prefix will be downloaded. The property is valid only when <code class="docutils literal notranslate"><span class="pre">auto_storage_container_name</span></code> or <code class="docutils literal notranslate"><span class="pre">storage_container_url</span></code> is used. This prefix can be a partial filename or a subdirectory. If a prefix is not specified, all the files in the container will be downloaded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The file permission mode represented as a string in octal format (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;0644&quot;</span></code>). This property applies only to files being downloaded to Linux compute nodes. It will be ignored if it is specified for a <code class="docutils literal notranslate"><span class="pre">resource_file</span></code> which will be downloaded to a Windows node. If this property is not specified for a Linux node, then a default value of 0770 is applied to the file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filePath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The location on the compute node to which to download the file, relative to the task’s working directory. If the <code class="docutils literal notranslate"><span class="pre">http_url</span></code> property is specified, the <code class="docutils literal notranslate"><span class="pre">file_path</span></code> is required and describes the path which the file will be downloaded to, including the filename. Otherwise, if the <code class="docutils literal notranslate"><span class="pre">auto_storage_container_name</span></code> or <code class="docutils literal notranslate"><span class="pre">storage_container_url</span></code> property is specified, <code class="docutils literal notranslate"><span class="pre">file_path</span></code> is optional and is the directory to download the files to. In the case where <code class="docutils literal notranslate"><span class="pre">file_path</span></code> is used as a directory, any directory structure already associated with the input data will be retained in full and appended to the specified filePath directory. The specified relative path cannot break out of the task’s working directory (for example by using ‘..’).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL of the file to download. If the URL is Azure Blob Storage, it must be readable using anonymous access; that is, the Batch service does not present any credentials when downloading the blob. There are two ways to get such a URL for a blob in Azure storage: include a Shared Access Signature (SAS) granting read permissions on the blob, or set the ACL for the blob or its container to allow public access.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageContainerUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL of the blob container within Azure Blob Storage. This URL must be readable and listable using anonymous access; that is, the Batch service does not present any credentials when downloading the blob. There are two ways to get such a URL for a blob in Azure storage: include a Shared Access Signature (SAS) granting read and list permissions on the blob, or set the ACL for the blob or its container to allow public access.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">userIdentity</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">user_identity</span></code> block that describes the user identity under which the start task runs.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoUser</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">auto_user</span></code> block that describes the user identity under which the start task runs.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">elevationLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The elevation level of the user identity under which the start task runs. Possible values are <code class="docutils literal notranslate"><span class="pre">Admin</span></code> or <code class="docutils literal notranslate"><span class="pre">NonAdmin</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">NonAdmin</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The scope of the user identity under which the start task runs. Possible values are <code class="docutils literal notranslate"><span class="pre">Task</span></code> or <code class="docutils literal notranslate"><span class="pre">Pool</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Task</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">userName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The username to be used by the Batch pool start task.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitForSuccess</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - A flag that indicates if the Batch pool should wait for the start task to be completed. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.storage_image_reference">
<code class="sig-name descname">storage_image_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.storage_image_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_image_reference</span></code> for the virtual machines that will compose the Batch pool.</p>
<blockquote>
<div><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the ID of the Custom Image which the virtual machines should be created from. Changing this forces a new resource to be created. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/batch/batch-custom-images">official documentation</a> for more details.</p></li>
</ul>
</div></blockquote>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the offer of the image used to create the virtual machines. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the publisher of the image used to create the virtual machines. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the SKU of the image used to create the virtual machines. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the version of the image used to create the virtual machines. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.vm_size">
<code class="sig-name descname">vm_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.vm_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the size of the VM created in the Batch pool.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.batch.Pool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">auto_scale=None</em>, <em class="sig-param">certificates=None</em>, <em class="sig-param">container_configuration=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">fixed_scale=None</em>, <em class="sig-param">max_tasks_per_node=None</em>, <em class="sig-param">metadata=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_configuration=None</em>, <em class="sig-param">node_agent_sku_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">start_task=None</em>, <em class="sig-param">stop_pending_resize_operation=None</em>, <em class="sig-param">storage_image_reference=None</em>, <em class="sig-param">vm_size=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Pool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Pool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Batch account in which the pool will be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>auto_scale</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">auto_scale</span></code> block that describes the scale settings when using auto scale.</p></li>
<li><p><strong>certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks that describe the certificates to be installed on each compute node in the pool.</p></li>
<li><p><strong>container_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The container configuration used in the pool’s VMs.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the display name of the Batch pool.</p></li>
<li><p><strong>fixed_scale</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">fixed_scale</span></code> block that describes the scale settings when using fixed scale.</p></li>
<li><p><strong>max_tasks_per_node</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum number of tasks that can run concurrently on a single compute node in the pool. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>metadata</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of custom batch pool metadata.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Batch pool. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">network_configuration</span></code> block that describes the network configurations for the Batch pool.</p></li>
<li><p><strong>node_agent_sku_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Sku of the node agents that will be created in the Batch pool.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Batch pool. Changing this forces a new resource to be created.</p></li>
<li><p><strong>start_task</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">start_task</span></code> block that describes the start task settings for the Batch pool.</p></li>
<li><p><strong>storage_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_image_reference</span></code> for the virtual machines that will compose the Batch pool.</p></li>
<li><p><strong>vm_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the size of the VM created in the Batch pool.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>auto_scale</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">evaluationInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The interval to wait before evaluating if the pool needs to be scaled. Defaults to <code class="docutils literal notranslate"><span class="pre">PT15M</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">formula</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The autoscale formula that needs to be used for scaling the Batch pool.</p></li>
</ul>
<p>The <strong>certificates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Batch Certificate to install on the Batch Pool, which must be inside the same Batch Account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storeLocation</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location of the certificate store on the compute node into which to install the certificate. Possible values are <code class="docutils literal notranslate"><span class="pre">CurrentUser</span></code> or <code class="docutils literal notranslate"><span class="pre">LocalMachine</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storeName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the certificate store on the compute node into which to install the certificate. This property is applicable only for pools configured with Windows nodes (that is, created with cloudServiceConfiguration, or with virtualMachineConfiguration using a Windows image reference). Common store names include: <code class="docutils literal notranslate"><span class="pre">My</span></code>, <code class="docutils literal notranslate"><span class="pre">Root</span></code>, <code class="docutils literal notranslate"><span class="pre">CA</span></code>, <code class="docutils literal notranslate"><span class="pre">Trust</span></code>, <code class="docutils literal notranslate"><span class="pre">Disallowed</span></code>, <code class="docutils literal notranslate"><span class="pre">TrustedPeople</span></code>, <code class="docutils literal notranslate"><span class="pre">TrustedPublisher</span></code>, <code class="docutils literal notranslate"><span class="pre">AuthRoot</span></code>, <code class="docutils literal notranslate"><span class="pre">AddressBook</span></code>, but any custom store name can also be used. The default value is <code class="docutils literal notranslate"><span class="pre">My</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">visibilities</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Which user accounts on the compute node should have access to the private data of the certificate.</p></li>
</ul>
<p>The <strong>container_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">containerRegistries</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Additional container registries from which container images can be pulled by the pool’s VMs.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password to log into the registry server. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">registryServer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The container registry URL. The default is “docker.io”. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">userName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The user name to log into the registry server. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of container configuration. Possible value is <code class="docutils literal notranslate"><span class="pre">DockerCompatible</span></code>.</p></li>
</ul>
<p>The <strong>fixed_scale</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">resizeTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The timeout for resize operations. Defaults to <code class="docutils literal notranslate"><span class="pre">PT15M</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetDedicatedNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of nodes in the Batch pool. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">targetLowPriorityNodes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of low priority nodes in the Batch pool. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
</ul>
<p>The <strong>network_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">endpointConfigurations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of inbound NAT pools that can be used to address specific ports on an individual compute node externally. Set as documented in the inbound_nat_pools block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">backend_port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The port number on the compute node. Acceptable values are between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">65535</span></code> except for <code class="docutils literal notranslate"><span class="pre">29876</span></code>, <code class="docutils literal notranslate"><span class="pre">29877</span></code> as these are reserved. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontendPortRange</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The range of external ports that will be used to provide inbound access to the backendPort on individual compute nodes in the format of <code class="docutils literal notranslate"><span class="pre">1000-1100</span></code>. Acceptable values range between <code class="docutils literal notranslate"><span class="pre">1</span></code> and <code class="docutils literal notranslate"><span class="pre">65534</span></code> except ports from <code class="docutils literal notranslate"><span class="pre">50000</span></code> to <code class="docutils literal notranslate"><span class="pre">55000</span></code> which are reserved by the Batch service. All ranges within a pool must be distinct and cannot overlap. Values must be a range of at least <code class="docutils literal notranslate"><span class="pre">100</span></code> nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the endpoint. The name must be unique within a Batch pool, can contain letters, numbers, underscores, periods, and hyphens. Names must start with a letter or number, must end with a letter, number, or underscore, and cannot exceed 77 characters. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkSecurityGroupRules</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of network security group rules that will be applied to the endpoint. The maximum number of rules that can be specified across all the endpoints on a Batch pool is <code class="docutils literal notranslate"><span class="pre">25</span></code>. If no network security group rules are specified, a default rule will be created to allow inbound access to the specified backendPort. Set as documented in the network_security_group_rules block below. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">access</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The action that should be taken for a specified IP address, subnet range or tag. Acceptable values are <code class="docutils literal notranslate"><span class="pre">Allow</span></code> and <code class="docutils literal notranslate"><span class="pre">Deny</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The priority for this rule. The value must be at least <code class="docutils literal notranslate"><span class="pre">150</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_address_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The source address prefix or tag to match for the rule. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protocol of the endpoint. Acceptable values are <code class="docutils literal notranslate"><span class="pre">TCP</span></code> and <code class="docutils literal notranslate"><span class="pre">UDP</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of public ip ids that will be allocated to nodes. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ARM resource identifier of the virtual network subnet which the compute nodes of the pool will join. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>start_task</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commandLine</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The command line executed by the start task.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A map of strings (key,value) that represents the environment variables to set in the start task.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTaskRetryCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of retry count. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceFiles</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">resource_file</span></code> blocks that describe the files to be downloaded to a compute node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoStorageContainerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The storage container name in the auto storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">blobPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The blob prefix to use when downloading blobs from an Azure Storage container. Only the blobs whose names begin with the specified prefix will be downloaded. The property is valid only when <code class="docutils literal notranslate"><span class="pre">auto_storage_container_name</span></code> or <code class="docutils literal notranslate"><span class="pre">storage_container_url</span></code> is used. This prefix can be a partial filename or a subdirectory. If a prefix is not specified, all the files in the container will be downloaded.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The file permission mode represented as a string in octal format (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;0644&quot;</span></code>). This property applies only to files being downloaded to Linux compute nodes. It will be ignored if it is specified for a <code class="docutils literal notranslate"><span class="pre">resource_file</span></code> which will be downloaded to a Windows node. If this property is not specified for a Linux node, then a default value of 0770 is applied to the file.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filePath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The location on the compute node to which to download the file, relative to the task’s working directory. If the <code class="docutils literal notranslate"><span class="pre">http_url</span></code> property is specified, the <code class="docutils literal notranslate"><span class="pre">file_path</span></code> is required and describes the path which the file will be downloaded to, including the filename. Otherwise, if the <code class="docutils literal notranslate"><span class="pre">auto_storage_container_name</span></code> or <code class="docutils literal notranslate"><span class="pre">storage_container_url</span></code> property is specified, <code class="docutils literal notranslate"><span class="pre">file_path</span></code> is optional and is the directory to download the files to. In the case where <code class="docutils literal notranslate"><span class="pre">file_path</span></code> is used as a directory, any directory structure already associated with the input data will be retained in full and appended to the specified filePath directory. The specified relative path cannot break out of the task’s working directory (for example by using ‘..’).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL of the file to download. If the URL is Azure Blob Storage, it must be readable using anonymous access; that is, the Batch service does not present any credentials when downloading the blob. There are two ways to get such a URL for a blob in Azure storage: include a Shared Access Signature (SAS) granting read permissions on the blob, or set the ACL for the blob or its container to allow public access.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageContainerUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL of the blob container within Azure Blob Storage. This URL must be readable and listable using anonymous access; that is, the Batch service does not present any credentials when downloading the blob. There are two ways to get such a URL for a blob in Azure storage: include a Shared Access Signature (SAS) granting read and list permissions on the blob, or set the ACL for the blob or its container to allow public access.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">userIdentity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">user_identity</span></code> block that describes the user identity under which the start task runs.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoUser</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">auto_user</span></code> block that describes the user identity under which the start task runs.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">elevationLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The elevation level of the user identity under which the start task runs. Possible values are <code class="docutils literal notranslate"><span class="pre">Admin</span></code> or <code class="docutils literal notranslate"><span class="pre">NonAdmin</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">NonAdmin</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The scope of the user identity under which the start task runs. Possible values are <code class="docutils literal notranslate"><span class="pre">Task</span></code> or <code class="docutils literal notranslate"><span class="pre">Pool</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Task</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">userName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The username to be used by the Batch pool start task.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitForSuccess</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - A flag that indicates if the Batch pool should wait for the start task to be completed. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>storage_image_reference</strong> object supports the following:</p>
<blockquote>
<div><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the ID of the Custom Image which the virtual machines should be created from. Changing this forces a new resource to be created. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/batch/batch-custom-images">official documentation</a> for more details.</p></li>
</ul>
</div></blockquote>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the offer of the image used to create the virtual machines. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the publisher of the image used to create the virtual machines. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the SKU of the image used to create the virtual machines. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the version of the image used to create the virtual machines. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.batch.Pool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Pool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.batch.Pool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Pool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.batch.get_account">
<code class="sig-prename descclassname">pulumi_azure.batch.</code><code class="sig-name descname">get_account</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.get_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Batch Account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Batch account.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where this Batch account exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.batch.get_certificate">
<code class="sig-prename descclassname">pulumi_azure.batch.</code><code class="sig-name descname">get_certificate</code><span class="sig-paren">(</span><em class="sig-param">account_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.get_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing certificate in a Batch Account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>account_name</strong> (<em>str</em>) – The name of the Batch account.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the Batch certificate.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where this Batch account exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.batch.get_pool">
<code class="sig-prename descclassname">pulumi_azure.batch.</code><code class="sig-name descname">get_pool</code><span class="sig-paren">(</span><em class="sig-param">account_name=None</em>, <em class="sig-param">certificates=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_configuration=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">start_task=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.get_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Batch pool</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>account_name</strong> (<em>str</em>) – The name of the Batch account.</p></li>
<li><p><strong>certificates</strong> (<em>list</em>) – One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks that describe the certificates installed on each compute node in the pool.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the endpoint.</p></li>
<li><p><strong>start_task</strong> (<em>dict</em>) – A <code class="docutils literal notranslate"><span class="pre">start_task</span></code> block that describes the start task settings for the Batch pool.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>certificates</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The fully qualified ID of the certificate installed on the pool.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storeLocation</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The location of the certificate store on the compute node into which the certificate is installed, either <code class="docutils literal notranslate"><span class="pre">CurrentUser</span></code> or <code class="docutils literal notranslate"><span class="pre">LocalMachine</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storeName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the certificate store on the compute node into which the certificate is installed.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">visibilities</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Which user accounts on the compute node have access to the private data of the certificate.</p></li>
</ul>
<p>The <strong>network_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">endpointConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - The inbound NAT pools that are used to address specific ports on the individual compute node externally.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">backend_port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The port number on the compute node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">frontendPortRange</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The range of external ports that are used to provide inbound access to the backendPort on the individual compute nodes in the format of <code class="docutils literal notranslate"><span class="pre">1000-1100</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">networkSecurityGroupRules</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The list of network security group rules that are applied to the endpoint.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">access</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The action that should be taken for a specified IP address, subnet range or tag.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The priority for this rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">source_address_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The source address prefix or tag to match for the rule.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The protocol of the endpoint.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ARM resource identifier of the virtual network subnet which the compute nodes of the pool are joined too.</p></li>
</ul>
<p>The <strong>start_task</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commandLine</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The command line executed by the start task.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">environment</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A map of strings (key,value) that represents the environment variables to set in the start task.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxTaskRetryCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of retry count.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceFiles</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">resource_file</span></code> blocks that describe the files to be downloaded to a compute node.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoStorageContainerName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The storage container name in the auto storage account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">blobPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The blob prefix used when downloading blobs from an Azure Storage container.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fileMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The file permission mode attribute represented as a string in octal format (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;0644&quot;</span></code>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filePath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The location on the compute node to which to download the file, relative to the task’s working directory. If the <code class="docutils literal notranslate"><span class="pre">http_url</span></code> property is specified, the <code class="docutils literal notranslate"><span class="pre">file_path</span></code> is required and describes the path which the file will be downloaded to, including the filename. Otherwise, if the <code class="docutils literal notranslate"><span class="pre">auto_storage_container_name</span></code> or <code class="docutils literal notranslate"><span class="pre">storage_container_url</span></code> property is specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL of the file to download. If the URL is Azure Blob Storage, it must be readable using anonymous access.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageContainerUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL of the blob container within Azure Blob Storage.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">userIdentities</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">user_identity</span></code> block that describes the user identity under which the start task runs.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoUsers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">auto_user</span></code> block that describes the user identity under which the start task runs.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">elevationLevel</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The elevation level of the user identity under which the start task runs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The scope of the user identity under which the start task runs.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">userName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The user name to log into the registry server.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">waitForSuccess</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - A flag that indicates if the Batch pool should wait for the start task to be completed.</p></li>
</ul>
</dd></dl>

</div>
